#!/usr/bin/env python3
"""Validate reviewed translation records without mutating them."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas/translation-record.schema.json"


class ValidationError(Exception):
    pass


def resolve(schema, root):
    if "$ref" not in schema:
        return schema
    node = root
    for part in schema["$ref"].removeprefix("#/").split("/"):
        node = node[part]
    return node


def structural(value, schema, root, path="$", errors=None):
    errors = [] if errors is None else errors
    schema = resolve(schema, root)
    for branch in schema.get("allOf", []):
        structural(value, branch, root, path, errors)
    expected = schema.get("type")
    checks = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float), "boolean": bool}
    if expected and (not isinstance(value, checks[expected]) or expected in {"integer", "number"} and isinstance(value, bool)):
        errors.append(f"{path}: expected {expected}")
        return errors
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not allowed")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0): errors.append(f"{path}: must not be empty")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value): errors.append(f"{path}: does not match required pattern")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]: errors.append(f"{path}: below minimum")
        if "exclusiveMinimum" in schema and value <= schema["exclusiveMinimum"]: errors.append(f"{path}: must exceed minimum")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0): errors.append(f"{path}: has too few items")
        if schema.get("uniqueItems") and len({json.dumps(x, sort_keys=True) for x in value}) != len(value): errors.append(f"{path}: items must be unique")
        for index, item in enumerate(value): structural(item, schema.get("items", {}), root, f"{path}[{index}]", errors)
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value: errors.append(f"{path}.{key}: required field is missing")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value.keys() - properties.keys(): errors.append(f"{path}.{key}: unexpected field")
        for key, item in value.items():
            if key in properties: structural(item, properties[key], root, f"{path}.{key}", errors)
    return errors


def has_coordinate(location):
    return any(key in location for key in ("pdf_page", "printed_page", "section", "figure", "table", "region_id", "source_region"))


def substantive(value):
    return isinstance(value, str) and bool(value.strip())


def require_human_review(review, path, errors):
    if review.get("status") == "human_language_verified" and (
        review.get("reviewer_role") != "human_language_reviewer"
        or not substantive(review.get("reviewer_qualification"))
    ):
        errors.append(
            f"{path}: human verification requires a human_language_reviewer "
            "role and qualification"
        )


def semantic(record):
    errors = []
    record_id = record.get("record_id")
    publication = record.get("source_publication_id")
    primary = record.get("primary_evidence", {})
    if primary.get("source_publication_id") != publication:
        errors.append("$.primary_evidence.source_publication_id: must match the record's original source publication")
    if primary.get("source_publication_id") == record_id:
        errors.append("$.primary_evidence: a translation record cannot identify itself as primary evidence")
    if not has_coordinate(primary.get("source_location", {})):
        errors.append("$.primary_evidence.source_location: at least one source coordinate is required")

    units = record.get("content_units", [])
    ids = [unit.get("unit_id") for unit in units]
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates: errors.append(f"$.content_units: duplicate unit_id values: {', '.join(duplicates)}")
    known_units = set(ids)
    for index, unit in enumerate(units):
        unit_path = f"$.content_units[{index}]"
        transcription = unit.get("source_transcription", {})
        transcription_status = transcription.get("status")
        transcription_text = transcription.get("text")
        if transcription_status == "exact" and not substantive(transcription_text):
            errors.append(f"{unit_path}.source_transcription.text: substantive text is required when status is exact")
        if transcription_status in {"partially_unreadable", "unreadable"} and not substantive(transcription.get("reason")):
            errors.append(f"{unit_path}.source_transcription.reason: substantive reason is required when status is {transcription_status}")
        if transcription_status == "unreadable" and substantive(transcription_text):
            errors.append(f"{unit_path}.source_transcription.text: unreadable transcription must not contain non-whitespace text")
        literal = unit.get("literal_translation", {})
        literal_status = literal.get("status")
        literal_text = literal.get("text")
        if literal_status == "present" and not substantive(literal_text):
            errors.append(f"{unit_path}.literal_translation.text: substantive text is required when status is present")
        if literal_status != "present" and not substantive(literal.get("reason")):
            errors.append(f"{unit_path}.literal_translation.reason: substantive reason is required when literal translation is not present")
        if literal_status != "present" and substantive(literal_text):
            errors.append(f"{unit_path}.literal_translation.text: non-present literal translation must not contain non-whitespace text")
        normalized = unit.get("normalized_engineering_wording")
        if normalized is not None and not substantive(normalized.get("text")):
            errors.append(f"{unit_path}.normalized_engineering_wording.text: substantive text is required when normalized wording is present")
        for name in ("source_reading", "literal_translation"):
            review = unit.get("reviews", {}).get(name, {})
            require_human_review(review, f"{unit_path}.reviews.{name}", errors)

    record_reviews = record.get("reviews", {})
    for name in ("source_reading", "literal_translation"):
        require_human_review(record_reviews.get(name, {}), f"$.reviews.{name}", errors)

    for index, dependency in enumerate(record.get("interpretive_dependencies", [])):
        if dependency.get("source_publication_id") != publication:
            errors.append(f"$.interpretive_dependencies[{index}]: must be a location in the original publication")
        if dependency.get("source_publication_id") == record_id or dependency.get("dependency_id") == record_id:
            errors.append(f"$.interpretive_dependencies[{index}]: a translation record cannot be an interpretive dependency")
        if not has_coordinate(dependency.get("source_location", {})):
            errors.append(f"$.interpretive_dependencies[{index}].source_location: at least one source coordinate is required")
        unknown = set(dependency.get("affected_content_unit_ids", [])) - known_units
        if unknown: errors.append(f"$.interpretive_dependencies[{index}].affected_content_unit_ids: unknown content units: {', '.join(sorted(unknown))}")

    coverage = record.get("coverage", {})
    translated = coverage.get("translated_region_ids", [])
    translated_set = set(translated)
    unit_regions = {unit.get("source_region_id") for unit in units}
    for index, unit in enumerate(units):
        region_id = unit.get("source_region_id")
        if region_id not in translated_set:
            errors.append(
                f"$.content_units[{index}].source_region_id: region {region_id!r} "
                f"for content unit {unit.get('unit_id')!r} is not listed in "
                "coverage.translated_region_ids"
            )
    for region_id in translated:
        if region_id not in unit_regions:
            errors.append(
                "$.coverage.translated_region_ids: translated region "
                f"{region_id!r} has no content unit"
            )

    category_ids = {}
    for field in ("excluded_regions", "unreadable_regions", "omitted_content"):
        region_ids = [item.get("region_id") for item in coverage.get(field, [])]
        category_ids[field] = set(region_ids)
        duplicate_regions = sorted({region_id for region_id in region_ids if region_ids.count(region_id) > 1})
        for region_id in duplicate_regions:
            errors.append(f"$.coverage.{field}: duplicate region_id {region_id!r}")
        for region_id in sorted(translated_set & category_ids[field]):
            errors.append(
                f"$.coverage: region {region_id!r} appears in incompatible "
                f"categories translated_region_ids and {field}"
            )
    fields = tuple(category_ids)
    for left_index, left in enumerate(fields):
        for right in fields[left_index + 1:]:
            for region_id in sorted(category_ids[left] & category_ids[right]):
                errors.append(
                    f"$.coverage: region {region_id!r} appears in incompatible "
                    f"categories {left} and {right}"
                )

    if coverage.get("kind") == "complete_bounded":
        for field in ("excluded_regions", "unreadable_regions", "omitted_content"):
            if coverage.get(field): errors.append(f"$.coverage.{field}: must be empty for complete_bounded coverage")
    if record.get("record_status") in {"review_ready", "provisionally_accepted", "fully_reviewed"} and not substantive(coverage.get("boundary_description")):
        errors.append("$.coverage.boundary_description: required for review-ready or accepted records")
    if record.get("record_status") in {"provisionally_accepted", "fully_reviewed"} and not substantive(record.get("acceptance_scope")):
        errors.append("$.acceptance_scope: accepted records require a limited stated purpose or boundary")
    if record.get("record_status") == "fully_reviewed":
        required_record_reviews = {
            "proposal": "corroborated",
            "source_reading": "human_language_verified",
            "literal_translation": "human_language_verified",
            "engineering_terminology": "engineering_reviewed",
        }
        for name, expected in required_record_reviews.items():
            actual = record_reviews.get(name, {}).get("status")
            if actual != expected:
                errors.append(f"$.reviews.{name}.status: fully_reviewed requires {expected!r}, found {actual!r}")
        if coverage.get("unreadable_regions"):
            errors.append("$.coverage.unreadable_regions: fully_reviewed records cannot retain unreadable regions")
        for index, unit in enumerate(units):
            unit_path = f"$.content_units[{index}]"
            reviews = unit.get("reviews", {})
            if unit.get("source_transcription", {}).get("status") == "unreadable":
                errors.append(f"{unit_path}.source_transcription.status: fully_reviewed cannot retain a fully unreadable content unit")
            if reviews.get("source_reading", {}).get("status") != "human_language_verified":
                errors.append(f"{unit_path}.reviews.source_reading.status: fully_reviewed requires 'human_language_verified'")
            if unit.get("literal_translation", {}).get("status") != "not_applicable" and reviews.get("literal_translation", {}).get("status") != "human_language_verified":
                errors.append(f"{unit_path}.reviews.literal_translation.status: fully_reviewed requires 'human_language_verified' unless literal translation is not_applicable")
            if unit.get("normalized_engineering_wording") is not None:
                if reviews.get("proposal", {}).get("status") != "corroborated":
                    errors.append(f"{unit_path}.reviews.proposal.status: normalized wording in fully_reviewed requires 'corroborated'")
                if reviews.get("engineering_terminology", {}).get("status") != "engineering_reviewed":
                    errors.append(f"{unit_path}.reviews.engineering_terminology.status: normalized wording in fully_reviewed requires 'engineering_reviewed'")
    return errors


def validate(path, schema):
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"$: cannot read JSON: {error}"]
    errors = structural(record, schema, schema)
    if not errors:
        errors.extend(semantic(record))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="+", type=Path)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()
    try:
        schema = json.loads(args.schema.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot load schema {args.schema}: {error}", file=sys.stderr)
        return 2
    failed = False
    for path in args.records:
        errors = validate(path, schema)
        if errors:
            failed = True
            for error in errors: print(f"{path}: {error}", file=sys.stderr)
        else:
            print(f"{path}: valid")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
