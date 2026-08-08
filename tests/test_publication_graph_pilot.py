import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "work/publication-graph-pilot/issue-44/phase-2"
COMMAND = ROOT / "scripts/validate-publication-graph-pilot.py"
SPEC = importlib.util.spec_from_file_location("pilot_validator", COMMAND)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PublicationGraphPilotTests(unittest.TestCase):
    def test_committed_package_validates(self):
        self.assertEqual([], VALIDATOR.validate(PACKAGE))

    def mutated(self, relative, mutate):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "phase-2"
            import shutil
            shutil.copytree(PACKAGE, package)
            path = package / relative
            record = json.loads(path.read_text(encoding="utf-8"))
            mutate(record)
            path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return "\n".join(VALIDATOR.validate(package))

    def test_rejects_second_selected_ground(self):
        def mutate(record):
            for occurrence in record["occurrences"]:
                occurrence.pop("candidate_role", None)
        self.assertIn("exactly one ground", self.mutated("publication-representation.json", mutate))

    def test_rejects_default_production_scope(self):
        self.assertIn("explicitly unresolved", self.mutated("applicability.json", lambda record: record.update(candidate_specific_production_scope="both_ranges")))

    def test_rejects_translation_as_primary(self):
        self.assertIn("non-primary", self.mutated("translation-binding.json", lambda record: record.update(is_primary_evidence=True)))

    def test_rejects_acceptance_with_open_applicability(self):
        self.assertIn("prohibit acceptance", self.mutated("candidate.json", lambda record: record.update(canonical_acceptance_prohibited=False)))

    def test_rejects_candidate_source_identity_collision(self):
        self.assertIn("separate from source identities", self.mutated("candidate.json", lambda record: record.update(candidate_id="I44-SO-TERMINAL-1-D-001")))


if __name__ == "__main__":
    unittest.main()
