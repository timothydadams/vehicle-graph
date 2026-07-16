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
        transcription = unit.get("source_transcription", {})
        if transcription.get("status") == "exact" and "text" not in transcription:
            errors.append(f"$.content_units[{index}].source_transcription.text: required when status is exact")
        literal = unit.get("literal_translation", {})
        if literal.get("status") == "present" and "text" not in literal:
            errors.append(f"$.content_units[{index}].literal_translation.text: required when status is present")
        if literal.get("status") != "present" and not literal.get("reason"):
            errors.append(f"$.content_units[{index}].literal_translation.reason: required when literal translation is not present")
        for name in ("source_reading", "literal_translation"):
            review = unit.get("reviews", {}).get(name, {})
            if review.get("status") == "human_language_verified" and (review.get("reviewer_role") != "human_language_reviewer" or not review.get("reviewer_qualification")):
                errors.append(f"$.content_units[{index}].reviews.{name}: human verification requires a human_language_reviewer role and qualification")

    for scope, reviews in [("$.reviews", record.get("reviews", {}))]:
        for name in ("source_reading", "literal_translation"):
            review = reviews.get(name, {})
            if review.get("status") == "human_language_verified" and (review.get("reviewer_role") != "human_language_reviewer" or not review.get("reviewer_qualification")):
                errors.append(f"{scope}.{name}: human verification requires a human_language_reviewer role and qualification")

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
    if coverage.get("kind") == "complete_bounded":
        for field in ("excluded_regions", "unreadable_regions", "omitted_content"):
            if coverage.get(field): errors.append(f"$.coverage.{field}: must be empty for complete_bounded coverage")
    if record.get("record_status") in {"review_ready", "provisionally_accepted", "fully_reviewed"} and not coverage.get("boundary_description"):
        errors.append("$.coverage.boundary_description: required for review-ready or accepted records")
    if record.get("record_status") in {"provisionally_accepted", "fully_reviewed"} and not record.get("acceptance_scope"):
        errors.append("$.acceptance_scope: accepted records require a limited stated purpose or boundary")
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
