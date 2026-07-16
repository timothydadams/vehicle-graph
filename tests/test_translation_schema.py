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
        expected = {"invalid-missing-primary-evidence.json": "primary_evidence", "invalid-collapsed-review-status.json": "source_reading", "invalid-translation-dependency.json": "cannot be an interpretive dependency", "invalid-human-verification.json": "human verification requires", "invalid-complete-with-omission.json": "must be empty for complete_bounded"}
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
