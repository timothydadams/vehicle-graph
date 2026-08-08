import importlib.util
import json
import shutil
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
    def copied(self):
        directory = tempfile.TemporaryDirectory()
        package = Path(directory.name) / "phase-2"
        shutil.copytree(PACKAGE, package)
        return directory, package

    def mutated(self, relative, mutate):
        directory, package = self.copied()
        try:
            path = package / relative
            record = json.loads(path.read_text(encoding="utf-8"))
            mutate(record)
            path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return "\n".join(VALIDATOR.validate(package))
        finally:
            directory.cleanup()

    def removed(self, relative):
        directory, package = self.copied()
        try:
            (package / relative).unlink()
            return "\n".join(VALIDATOR.validate(package))
        finally:
            directory.cleanup()

    def records(self):
        return (
            json.loads((PACKAGE / "candidate.json").read_text(encoding="utf-8")),
            json.loads((PACKAGE / "review/result.json").read_text(encoding="utf-8")),
            json.loads((PACKAGE / "eligibility.json").read_text(encoding="utf-8")),
        )

    def test_committed_package_validates(self):
        self.assertEqual([], VALIDATOR.validate(PACKAGE))

    def test_baseline_v1_dependencies_are_fresh(self):
        candidate, review, eligibility = self.records()
        states = VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V1)
        self.assertEqual({"fresh"}, set(states.values()))

    def test_isolated_v2_activation_derives_transitive_staleness(self):
        candidate, review, eligibility = self.records()
        states = VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V2)
        self.assertEqual("stale", states["candidate"])
        self.assertEqual("review_required", states["extraction_review"])
        self.assertEqual("review_required", states["eligibility"])
        self.assertEqual("review_required", states["disposition_reference"])

    def test_explicit_v1_restoration_returns_to_baseline(self):
        candidate, review, eligibility = self.records()
        VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V2)
        restored = VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V1)
        self.assertEqual({"fresh"}, set(restored.values()))

    def test_rejects_silent_candidate_dependency_retargeting(self):
        def mutate(record):
            record["relationship"]["source_structure_dependency"] = VALIDATOR.V2
        self.assertIn("committed baseline", self.mutated("candidate.json", mutate))

    def test_rejects_asserting_fresh_during_v2_activation(self):
        def mutate(record):
            record["transitions"][1]["expected_states"] = {key: "fresh" for key in record["transitions"][1]["expected_states"]}
        self.assertIn("disagree with derived", self.mutated("lifecycle-test.json", mutate))

    def test_factory_evidence_identity_is_unchanged_during_lifecycle(self):
        self.assertIn("preserve factory evidence identity", self.mutated("lifecycle-relationship-v2.json", lambda record: record.update(factory_artifact_fingerprint="sha256:changed")))

    def test_in_memory_transition_does_not_mutate_factory_evidence(self):
        candidate, review, eligibility = self.records()
        before = candidate["primary_evidence"]["artifact_fingerprint"]
        VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V1)
        VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V2)
        VALIDATOR.derive_dependency_states(candidate, review, eligibility, VALIDATOR.V1)
        self.assertEqual(before, candidate["primary_evidence"]["artifact_fingerprint"])
        self.assertEqual(VALIDATOR.HASH, before)

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

    def test_rejects_misleading_review_classification(self):
        def mutate(record):
            record["findings"][0]["class"] = "acceptance" + "_ready_candidate"
        self.assertIn("acceptance-ready", self.mutated("review/result.json", mutate))

    def test_required_artifact_deletions_fail(self):
        for relative in (
            "eligibility.json",
            "lifecycle-test.json",
            "lifecycle-relationship-v2.json",
            "review/result.json",
            "review/independent-source-account.md",
            "review/REVIEW_TASK.md",
        ):
            with self.subTest(relative=relative):
                self.assertIn(f"missing {relative}", self.removed(relative))

    def test_review_and_candidate_ids_must_align(self):
        self.assertIn("same candidate ID", self.mutated("review/result.json", lambda record: record.update(candidate_id="another-candidate")))

    def test_eligibility_must_reference_exact_candidate(self):
        self.assertIn("exact candidate", self.mutated("eligibility.json", lambda record: record.update(reviewed_candidate_id="another-candidate")))

    def test_eligibility_must_reference_exact_review(self):
        self.assertIn("exact extraction review", self.mutated("eligibility.json", lambda record: record.update(extraction_review_id="another-review")))

    def test_frozen_commits_must_align(self):
        self.assertIn("frozen commits disagree", self.mutated("review/result.json", lambda record: record.update(frozen_commit="0" * 40)))

    def test_review_outcome_must_be_permitted(self):
        self.assertIn("outside manifest permitted outcomes", self.mutated("review/result.json", lambda record: record.update(outcome="invented")))

    def test_eligibility_cannot_accept_or_reject(self):
        self.assertIn("requires ineligible", self.mutated("eligibility.json", lambda record: record.update(decision="accepted")))
        self.assertIn("ineligible is not rejected", self.mutated("eligibility.json", lambda record: record.update(rejected=True)))

    def test_canonical_graph_write_is_rejected_at_every_gate(self):
        self.assertIn("review package may not mutate", self.mutated("review/result.json", lambda record: record.update(canonical_graph_write=True)))
        self.assertIn("eligibility may not mutate", self.mutated("eligibility.json", lambda record: record.update(canonical_graph_write=True)))

    def test_second_candidate_record_fails(self):
        directory, package = self.copied()
        try:
            extra = json.loads((package / "candidate.json").read_text(encoding="utf-8"))
            extra["candidate_id"] = "I44-CAND-CONNECTIVITY-002-v1"
            (package / "candidate-2.json").write_text(json.dumps(extra, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            errors = "\n".join(VALIDATOR.validate(package))
            self.assertIn("exactly one engineering candidate record", errors)
            self.assertIn("exactly one candidate relationship", errors)
        finally:
            directory.cleanup()

    def test_second_candidate_relationship_fails(self):
        def mutate(record):
            record["relationships"] = [{"kind": "electrically_connected_to", "source_structure_dependency": VALIDATOR.V1}]
        self.assertIn("second candidate relationship", self.mutated("candidate.json", mutate))


if __name__ == "__main__":
    unittest.main()
