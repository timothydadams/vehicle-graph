import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/translation"
COMMAND = ROOT / "scripts/validate-translation-records.py"
SCHEMA = ROOT / "schemas/translation-record.schema.json"
SPEC = importlib.util.spec_from_file_location("translation_validator", COMMAND)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class TranslationSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        cls.minimal = json.loads((FIXTURES / "valid-minimal.json").read_text(encoding="utf-8"))

    def errors(self, record):
        errors = VALIDATOR.structural(record, self.schema, self.schema)
        if not errors:
            errors.extend(VALIDATOR.semantic(record))
        return errors

    def test_valid_fixtures_pass(self):
        for name in ("valid-minimal.json", "valid-table-entry.json", "valid-interpretive-dependency.json"):
            with self.subTest(name=name):
                self.assertEqual([], VALIDATOR.validate(FIXTURES / name, self.schema))

    def test_invalid_fixtures_fail_for_intended_reason(self):
        expected = {"invalid-missing-primary-evidence.json": "primary_evidence", "invalid-collapsed-review-status.json": "source_reading", "invalid-translation-dependency.json": "cannot be an interpretive dependency", "invalid-human-verification.json": "human verification requires", "invalid-complete-with-omission.json": "must be empty for complete_bounded", "invalid-unbound-content-region.json": "is not listed in coverage.translated_region_ids"}
        for name, message in expected.items():
            with self.subTest(name=name):
                self.assertIn(message, "\n".join(VALIDATOR.validate(FIXTURES / name, self.schema)))

    def test_duplicate_content_ids_fail(self):
        record = copy.deepcopy(self.minimal)
        record["content_units"].append(copy.deepcopy(record["content_units"][0]))
        self.assertIn("duplicate unit_id", "\n".join(self.errors(record)))

    def test_missing_source_location_fails(self):
        record = copy.deepcopy(self.minimal)
        record["primary_evidence"]["source_location"] = {}
        self.assertIn("source coordinate", "\n".join(self.errors(record)))

    def test_review_dimensions_are_independent(self):
        record = copy.deepcopy(self.minimal)
        reviews = record["content_units"][0]["reviews"]
        reviews["proposal"]["status"] = "corroborated"
        reviews["source_reading"]["status"] = "machine_cross_checked"
        reviews["literal_translation"]["status"] = "changes_required"
        reviews["engineering_terminology"]["status"] = "engineering_reviewed"
        self.assertEqual([], self.errors(record))

    def test_translated_region_must_have_content_unit(self):
        record = copy.deepcopy(self.minimal)
        record["coverage"]["translated_region_ids"].append("empty-region")
        self.assertIn("translated region 'empty-region' has no content unit", "\n".join(self.errors(record)))

    def test_translated_and_non_translated_regions_are_mutually_exclusive(self):
        record = copy.deepcopy(self.minimal)
        record["coverage"]["kind"] = "partial_bounded"
        record["coverage"]["omitted_content"] = [{"region_id": "region-heading", "reason": "Synthetic conflict."}]
        errors = "\n".join(self.errors(record))
        self.assertIn("translated_region_ids and omitted_content", errors)

    def test_non_translated_categories_are_mutually_exclusive(self):
        record = copy.deepcopy(self.minimal)
        record["coverage"]["kind"] = "partial_bounded"
        item = {"region_id": "region-outside", "reason": "Synthetic conflict."}
        record["coverage"]["excluded_regions"] = [item]
        record["coverage"]["unreadable_regions"] = [item]
        self.assertIn("excluded_regions and unreadable_regions", "\n".join(self.errors(record)))

    def test_region_id_is_unique_within_coverage_category(self):
        record = copy.deepcopy(self.minimal)
        record["coverage"]["kind"] = "partial_bounded"
        record["coverage"]["excluded_regions"] = [
            {"region_id": "duplicate-region", "reason": "First reason."},
            {"region_id": "duplicate-region", "reason": "Different reason."},
        ]
        self.assertIn("duplicate region_id 'duplicate-region'", "\n".join(self.errors(record)))

    def test_completed_text_states_require_substantive_text(self):
        cases = (
            ("exact-empty", ("source_transcription", "text"), ""),
            ("exact-whitespace", ("source_transcription", "text"), "  \t"),
            ("literal-empty", ("literal_translation", "text"), ""),
            ("literal-whitespace", ("literal_translation", "text"), " \n"),
        )
        for name, (object_name, field), value in cases:
            with self.subTest(name=name):
                record = copy.deepcopy(self.minimal)
                record["content_units"][0][object_name][field] = value
                self.assertTrue(self.errors(record))

    def test_normalized_wording_requires_substantive_text(self):
        for text in ("", " \t"):
            with self.subTest(text=repr(text)):
                record = copy.deepcopy(self.minimal)
                record["content_units"][0]["normalized_engineering_wording"] = {"status": "proposed", "text": text}
                self.assertTrue(self.errors(record))

    def test_unreadable_transcription_state_is_consistent(self):
        unit = self.minimal["content_units"][0]
        cases = (
            ({"status": "partially_unreadable", "text": "試"}, "reason"),
            ({"status": "unreadable"}, "reason"),
            ({"status": "unreadable", "reason": "Illegible synthetic region.", "text": "試験"}, "must not contain"),
        )
        for transcription, message in cases:
            with self.subTest(transcription=transcription):
                record = copy.deepcopy(self.minimal)
                record["content_units"][0] = copy.deepcopy(unit)
                record["content_units"][0]["source_transcription"] = transcription
                self.assertIn(message, "\n".join(self.errors(record)))

    def test_non_present_literal_translation_rejects_text(self):
        record = copy.deepcopy(self.minimal)
        record["content_units"][0]["literal_translation"] = {"status": "pending", "reason": "Awaiting review.", "text": "partial text"}
        self.assertIn("must not contain non-whitespace text", "\n".join(self.errors(record)))

    @staticmethod
    def human_verified(review):
        review.update(status="human_language_verified", reviewer_role="human_language_reviewer", reviewer_qualification="Qualified synthetic reviewer")

    def fully_reviewed_record(self, *, normalized=False):
        record = copy.deepcopy(self.minimal)
        record.update(record_status="fully_reviewed", acceptance_scope="Synthetic bounded fixture only.")
        record["reviews"]["proposal"]["status"] = "corroborated"
        self.human_verified(record["reviews"]["source_reading"])
        self.human_verified(record["reviews"]["literal_translation"])
        record["reviews"]["engineering_terminology"]["status"] = "engineering_reviewed"
        unit = record["content_units"][0]
        self.human_verified(unit["reviews"]["source_reading"])
        self.human_verified(unit["reviews"]["literal_translation"])
        if normalized:
            unit["normalized_engineering_wording"] = {"status": "proposed", "text": "Synthetic Heading"}
            unit["reviews"]["proposal"]["status"] = "corroborated"
            unit["reviews"]["engineering_terminology"]["status"] = "engineering_reviewed"
        return record

    def test_fully_reviewed_rejects_incomplete_reviews(self):
        record = copy.deepcopy(self.minimal)
        record.update(record_status="fully_reviewed", acceptance_scope="Synthetic boundary.")
        self.assertIn("fully_reviewed requires", "\n".join(self.errors(record)))

    def test_fully_reviewed_rejects_unreadable_content(self):
        record = self.fully_reviewed_record()
        record["content_units"][0]["source_transcription"] = {"status": "unreadable", "reason": "Synthetic region remains illegible."}
        self.assertIn("cannot retain a fully unreadable content unit", "\n".join(self.errors(record)))

    def test_correctly_fully_reviewed_record_passes_without_unit_normalization(self):
        self.assertEqual([], self.errors(self.fully_reviewed_record()))

    def test_fully_reviewed_normalization_requires_proposal_and_engineering_review(self):
        record = self.fully_reviewed_record(normalized=True)
        record["content_units"][0]["reviews"]["proposal"]["status"] = "proposed"
        record["content_units"][0]["reviews"]["engineering_terminology"]["status"] = "unreviewed"
        errors = "\n".join(self.errors(record))
        self.assertIn("normalized wording in fully_reviewed requires 'corroborated'", errors)
        self.assertIn("normalized wording in fully_reviewed requires 'engineering_reviewed'", errors)

    def test_provisionally_accepted_allows_incomplete_reviews(self):
        record = copy.deepcopy(self.minimal)
        record.update(record_status="provisionally_accepted", acceptance_scope="Limited synthetic review use only.")
        self.assertEqual([], self.errors(record))

    def test_human_verification_requires_human_role_and_qualification(self):
        record = copy.deepcopy(self.minimal)
        review = record["reviews"]["source_reading"]
        review.update(status="human_language_verified", reviewer_role="machine_tool")
        self.assertIn("human_language_reviewer", "\n".join(self.errors(record)))

    def test_parallel_terminology_evidence_is_not_primary_evidence(self):
        record = json.loads((FIXTURES / "valid-table-entry.json").read_text(encoding="utf-8"))
        self.assertNotEqual(record["supporting_evidence"][0]["source_id"], record["primary_evidence"]["source_publication_id"])
        self.assertEqual("terminology_normalization", record["supporting_evidence"][0]["role"])
        self.assertEqual([], self.errors(record))

    def test_translation_status_has_no_graph_acceptance_field(self):
        record = copy.deepcopy(self.minimal)
        record.update(record_status="provisionally_accepted", acceptance_scope="Synthetic translation boundary only; no graph acceptance.")
        self.assertEqual([], self.errors(record))
        record["graph_status"] = "accepted"
        self.assertIn("unexpected field", "\n".join(self.errors(record)))

    def test_cli_errors_are_stable_and_readable(self):
        result = subprocess.run([sys.executable, str(COMMAND), str(FIXTURES / "invalid-human-verification.json")], text=True, capture_output=True, check=False)
        self.assertEqual(1, result.returncode)
        self.assertIn("$.content_units[0].reviews.source_reading", result.stderr)
        self.assertIn("human verification requires", result.stderr)


if __name__ == "__main__":
    unittest.main()
