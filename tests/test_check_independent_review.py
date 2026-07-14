import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMMAND = PROJECT_ROOT / "scripts/check-independent-review"
IR_001 = PROJECT_ROOT / "work/independent-review/IR-001"


class CheckIndependentReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.package = Path(self.temporary.name) / "IR-001"
        shutil.copytree(IR_001, self.package)

    def tearDown(self):
        self.temporary.cleanup()

    def run_check(self, *, expected=0):
        result = subprocess.run(
            [sys.executable, str(COMMAND), str(self.package)],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expected, result.returncode, result.stderr or result.stdout)
        return result

    def replace(self, filename, old, new):
        path = self.package / filename
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def remove_field(self, filename, label):
        path = self.package / filename
        text = path.read_text(encoding="utf-8")
        changed, count = re.subn(
            rf"^- {re.escape(label)}: `[^`]*`\n",
            "",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        self.assertEqual(1, count)
        path.write_text(changed, encoding="utf-8")

    def add_result_narrative(self, text):
        self.replace("review-summary.md", "## Result\n\n", f"## Result\n\n{text}\n\n")

    def set_package_state(self, state):
        self.replace(
            "review-manifest.md",
            "Package state: `review_complete`",
            f"Package state: `{state}`",
        )

    def test_ir_001_completed_artifacts_pass(self):
        result = self.run_check()
        self.assertIn("Independent review package is valid", result.stdout)

    def test_missing_reviewer_identity_fails(self):
        self.remove_field("review-summary.md", "Reviewer")
        self.assertIn("reviewer identity", self.run_check(expected=1).stderr)

    def test_placeholder_reviewer_identity_fails(self):
        self.replace(
            "review-summary.md",
            "Reviewer: `Codex — fresh independent-review session`",
            "Reviewer: `<name-or-process>`",
        )
        self.assertIn("non-placeholder reviewer", self.run_check(expected=1).stderr)

    def test_missing_source_account_reviewer_identity_fails(self):
        self.remove_field("independent-source-account.md", "Reviewer")
        self.assertIn("source account", self.run_check(expected=1).stderr)

    def test_missing_review_date_fails(self):
        self.remove_field("review-summary.md", "Review date")
        self.assertIn("review date", self.run_check(expected=1).stderr)

    def test_missing_method_validity_fails(self):
        self.remove_field("review-summary.md", "Method validity")
        self.assertIn("method validity", self.run_check(expected=1).stderr)

    def test_invalid_method_validity_text_fails(self):
        self.replace(
            "review-summary.md", "Method validity: `valid`", "Method validity: `complete`"
        )
        self.assertIn("must be 'valid'", self.run_check(expected=1).stderr)

    def test_missing_disposition_fails(self):
        self.remove_field("review-summary.md", "Disposition")
        self.assertIn("needs a disposition", self.run_check(expected=1).stderr)

    def test_missing_reviewer_declaration_fails(self):
        path = self.package / "review-summary.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.split("\n## Reviewer Declaration\n", 1)[0] + "\n",
            encoding="utf-8",
        )
        self.assertIn("Reviewer Declaration", self.run_check(expected=1).stderr)

    def test_missing_declaration_timestamp_fails(self):
        self.remove_field("review-summary.md", "Recorded at")
        self.assertIn("recorded-at timestamp", self.run_check(expected=1).stderr)

    def test_combined_manifest_state_and_disposition_fails(self):
        self.replace(
            "review-manifest.md",
            "Package state: `review_complete`",
            "Package revision/status: `review complete — changes required`",
        )
        result = self.run_check(expected=1)
        self.assertIn("must not be combined", result.stderr)

    def test_review_complete_and_separate_changes_required_pass(self):
        self.assertIn(
            "Package state: `review_complete`",
            (self.package / "review-manifest.md").read_text(encoding="utf-8"),
        )
        self.assertIn(
            "Disposition: `changes_required`",
            (self.package / "review-summary.md").read_text(encoding="utf-8"),
        )
        self.run_check()

    def test_findings_prevent_review_completion_fails(self):
        self.add_result_narrative("Five findings prevent review completion.")
        result = self.run_check(expected=1)
        self.assertIn("prevent review completion", result.stderr)
        self.assertIn("acceptance-ready result", result.stderr)

    def test_open_findings_prevent_review_completion_fails(self):
        self.add_result_narrative("Open findings prevent review completion.")
        self.assertIn(
            "prevent review completion",
            self.run_check(expected=1).stderr,
        )

    def test_findings_completion_check_is_case_insensitive(self):
        self.add_result_narrative("OPEN FINDINGS PREVENT REVIEW COMPLETION.")
        self.assertIn(
            "prevent review completion",
            self.run_check(expected=1).stderr,
        )

    def test_review_cannot_be_complete_because_findings_fails(self):
        self.add_result_narrative(
            "The review cannot be complete because open findings remain."
        )
        self.assertIn(
            "pending remediation prevent review completion",
            self.run_check(expected=1).stderr,
        )

    def test_findings_may_prevent_acceptance_ready_result(self):
        self.add_result_narrative("Findings prevent an acceptance-ready result.")
        self.run_check()

    def test_findings_may_prevent_canonical_acceptance(self):
        self.add_result_narrative("Findings prevent canonical acceptance.")
        self.run_check()

    def test_methodological_incompleteness_is_allowed_before_completion(self):
        self.set_package_state("in_review")
        self.add_result_narrative(
            "The review is incomplete because the source-to-candidate pass was not "
            "performed."
        )
        self.run_check()

    def test_findings_prose_check_runs_only_for_review_complete(self):
        self.set_package_state("findings_issued")
        self.add_result_narrative("Open findings prevent review completion.")
        self.run_check()

    def test_package_state_rejects_review_disposition_vocabulary(self):
        self.replace(
            "review-manifest.md",
            "Package state: `review_complete`",
            "Package state: `changes_required`",
        )
        self.assertIn("invalid package state", self.run_check(expected=1).stderr)

    def test_disposition_rejects_package_state_vocabulary(self):
        self.replace(
            "review-summary.md",
            "Disposition: `changes_required`",
            "Disposition: `review_complete`",
        )
        self.assertIn("invalid review disposition", self.run_check(expected=1).stderr)

    def test_validation_does_not_modify_canonical_acceptance(self):
        acceptance = self.package / "canonical-acceptance.md"
        before = hashlib.sha256(acceptance.read_bytes()).hexdigest()
        self.run_check()
        self.assertEqual(before, hashlib.sha256(acceptance.read_bytes()).hexdigest())
        self.assertIn("Decision: `accepted |", acceptance.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
