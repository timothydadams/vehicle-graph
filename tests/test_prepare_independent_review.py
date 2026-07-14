import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
COMMAND = PROJECT_ROOT / "scripts/prepare-independent-review"


class PrepareIndependentReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.env = os.environ.copy()
        self.env.update(
            {
                "GIT_AUTHOR_NAME": "Fixture Preparer",
                "GIT_AUTHOR_EMAIL": "fixture@example.test",
                "GIT_COMMITTER_NAME": "Fixture Preparer",
                "GIT_COMMITTER_EMAIL": "fixture@example.test",
            }
        )
        self._build_repository()

    def tearDown(self):
        self.temporary.cleanup()

    def run_command(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(COMMAND), *args],
            cwd=self.root,
            env=self.env,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(expected, result.returncode, result.stderr or result.stdout)
        return result

    def git(self, *args):
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            env=self.env,
            text=True,
            capture_output=True,
            check=True,
        ).stdout.strip()

    def write(self, path, text="# Fixture\n"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def _build_repository(self):
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture Preparer")
        self.git("config", "user.email", "fixture@example.test")
        for path in (
            "AGENTS.md",
            "docs/PROVENANCE.md",
            "docs/APPLICABILITY.md",
            "docs/SOURCE_LANGUAGE.md",
            "docs/EXTRACTION_WORKFLOW.md",
            "docs/INDEPENDENT_REVIEW.md",
            "prompts/independent-review.md",
        ):
            self.write(path)
        template = self.root / "work/independent-review/template"
        template.mkdir(parents=True)
        for name in (
            "review-manifest.md",
            "independent-source-account.md",
            "findings.md",
            "review-summary.md",
            "finding-resolutions.md",
            "canonical-acceptance.md",
        ):
            shutil.copyfile(PROJECT_ROOT / "work/independent-review/template" / name, template / name)

        artifacts = {
            "publication_identity": "work/one-diagram/publication.json",
            "applicability": "work/one-diagram/applicability.md",
            "evidence_inventory": "work/one-diagram/evidence-inventory.md",
            "source_language": "work/one-diagram/source-language.md",
            "extraction_boundary": "work/one-diagram/extraction-boundary.md",
            "candidate_ledger": "work/one-diagram/candidate-ledger.md",
            "ambiguity_log": "work/one-diagram/ambiguity-log.md",
        }
        evidence_content = "fixture evidence\n"
        self.evidence_sha256 = hashlib.sha256(evidence_content.encode()).hexdigest()
        for path in artifacts.values():
            self.write(path)
        self.write(
            "work/one-diagram/publication.json",
            json.dumps(
                {
                    "publication_number": "FIXTURE-1",
                    "expected_local_artifact": "private/evidence.pdf",
                    "sha256": self.evidence_sha256,
                    "fingerprint_status": "recorded",
                },
                indent=2,
            )
            + "\n",
        )
        self.write(
            "work/one-diagram/readiness.md",
            "# Readiness\n[x] candidate extraction authorized\n",
        )
        self.write("private/evidence.pdf", evidence_content)
        config = {
            "workspace_id": "one-diagram",
            "artifacts": artifacts,
            "readiness_signal": {
                "path": "work/one-diagram/readiness.md",
                "required_text": "[x] candidate extraction authorized",
            },
            "source_materials": ["private/evidence.pdf"],
            "disclosure": {
                "initial": [
                    "review-manifest.md",
                    "AGENTS.md",
                    "work/one-diagram/publication.json",
                    "work/one-diagram/applicability.md",
                    "work/one-diagram/evidence-inventory.md",
                    "work/one-diagram/extraction-boundary.md",
                    "work/one-diagram/source-language.md",
                    "private/evidence.pdf",
                ],
                "stage2": ["work/one-diagram/candidate-ledger.md"],
                "stage3": ["work/one-diagram/ambiguity-log.md"],
                "notes": ["Fixture disclosure decision."],
            },
        }
        self.write(
            "work/one-diagram/review-preparation.json",
            json.dumps(config, indent=2) + "\n",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")

    def test_successful_dry_run_makes_no_changes(self):
        result = self.run_command("one-diagram", "--check")
        self.assertIn("Independent review preparation (dry run)", result.stdout)
        self.assertIn("review_id: IR-001", result.stdout)
        self.assertIn(
            "review_preparation_configuration: work/one-diagram/review-preparation.json",
            result.stdout,
        )
        self.assertIn(f"verified SHA-256 {self.evidence_sha256}", result.stdout)
        self.assertIn("stage_1_initial_materials:", result.stdout)
        self.assertFalse((self.root / "work/independent-review/IR-001").exists())
        self.assertEqual("", self.git("status", "--short"))

    def test_successful_creation_populates_mechanical_fields_only(self):
        extraction = self.root / "work/one-diagram/candidate-ledger.md"
        before = hashlib.sha256(extraction.read_bytes()).hexdigest()
        self.run_command("one-diagram")
        package = self.root / "work/independent-review/IR-001"
        commit = self.git("rev-parse", "HEAD")
        self.assertTrue(package.is_dir())
        manifest = (package / "review-manifest.md").read_text()
        self.assertIn(commit, manifest)
        self.assertIn("Review revision: `R0`", manifest)
        self.assertIn("Package revision/status: `draft`", manifest)
        self.assertIn(
            "Review-preparation configuration: `work/one-diagram/review-preparation.json`",
            manifest,
        )
        self.assertIn(f"SHA-256 {self.evidence_sha256} verified", manifest)
        self.assertIn("Stage 1 — Initial-Review Materials", manifest)
        self.assertIn("Stage 2 — Candidate Comparison Materials", manifest)
        self.assertIn("Stage 3 — Ambiguity and Rationale Materials", manifest)
        task = (package / "REVIEW_TASK.md").read_text()
        self.assertIn("prompts/independent-review.md", task)
        self.assertIn("Do not", task)
        source_account = (package / "independent-source-account.md").read_text()
        acceptance = (package / "canonical-acceptance.md").read_text()
        summary = (package / "review-summary.md").read_text()
        self.assertIn("Reviewer: `<name-or-process>`", source_account)
        self.assertIn("Human acceptor: `<name>`", acceptance)
        self.assertIn("Disposition: `accepted |", summary)
        self.assertEqual(before, hashlib.sha256(extraction.read_bytes()).hexdigest())

    def test_automatic_review_id_allocation(self):
        (self.root / "work/independent-review/IR-001").mkdir()
        result = self.run_command("one-diagram", "--check")
        self.assertIn("review_id: IR-002", result.stdout)

    def test_explicit_review_id(self):
        self.run_command("one-diagram", "--review-id", "IR-007")
        self.assertTrue((self.root / "work/independent-review/IR-007").is_dir())

    def test_refuses_existing_target(self):
        (self.root / "work/independent-review/IR-001").mkdir()
        result = self.run_command("one-diagram", "--review-id", "IR-001", expected=1)
        self.assertIn("target package already exists", result.stderr)

    def test_refuses_dirty_required_artifact(self):
        with (self.root / "work/one-diagram/candidate-ledger.md").open("a") as handle:
            handle.write("dirty\n")
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("uncommitted changes", result.stderr)
        self.assertIn("candidate-ledger.md", result.stderr)

    def test_refuses_dirty_review_preparation_configuration(self):
        config_path = self.root / "work/one-diagram/review-preparation.json"
        with config_path.open("a") as handle:
            handle.write("\n")
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("configuration has uncommitted changes", result.stderr)
        self.assertIn("work/one-diagram/review-preparation.json", result.stderr)

    def test_refuses_uncommitted_review_preparation_configuration_path(self):
        original = self.root / "work/one-diagram/review-preparation.json"
        config = json.loads(original.read_text())
        config["workspace_id"] = "uncommitted-workspace"
        self.write(
            "work/uncommitted-workspace/review-preparation.json",
            json.dumps(config, indent=2) + "\n",
        )
        result = self.run_command(
            "work/uncommitted-workspace", "--check", expected=1
        )
        self.assertIn("configuration is not committed at HEAD", result.stderr)
        self.assertIn(
            "work/uncommitted-workspace/review-preparation.json", result.stderr
        )

    def test_refuses_private_source_fingerprint_mismatch(self):
        metadata_path = self.root / "work/one-diagram/publication.json"
        metadata = json.loads(metadata_path.read_text())
        expected = "0" * 64
        metadata["sha256"] = expected
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
        self.git("add", "work/one-diagram/publication.json")
        self.git("commit", "-qm", "record mismatching fingerprint")
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("private source fingerprint mismatch", result.stderr)
        self.assertIn("private/evidence.pdf", result.stderr)
        self.assertIn(f"Expected SHA-256: {expected}", result.stderr)
        self.assertIn(f"Actual SHA-256: {self.evidence_sha256}", result.stderr)

    def test_missing_recorded_fingerprint_is_reported(self):
        metadata_path = self.root / "work/one-diagram/publication.json"
        metadata = json.loads(metadata_path.read_text())
        del metadata["sha256"]
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")
        self.git("add", "work/one-diagram/publication.json")
        self.git("commit", "-qm", "remove recorded fingerprint")
        result = self.run_command("one-diagram", "--check")
        self.assertIn("no recorded SHA-256; fingerprint not verified", result.stdout)

    def test_refuses_missing_required_artifact(self):
        (self.root / "work/one-diagram/evidence-inventory.md").unlink()
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("evidence inventory is missing", result.stderr)

    def test_refuses_ambiguous_discovery(self):
        config_path = self.root / "work/one-diagram/review-preparation.json"
        config = json.loads(config_path.read_text())
        del config["artifacts"]["applicability"]
        config_path.write_text(json.dumps(config, indent=2) + "\n")
        self.write("work/one-diagram/target-applicability.md")
        self.git("add", ".")
        self.git("commit", "-qm", "make applicability discovery ambiguous")
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("Cannot identify a unique applicability artifact", result.stderr)
        self.assertIn("applicability.md", result.stderr)
        self.assertIn("target-applicability.md", result.stderr)

    def test_refuses_uncommitted_artifact_mapping(self):
        self.write("work/one-diagram/untracked-ledger.md")
        config_path = self.root / "work/one-diagram/review-preparation.json"
        config = json.loads(config_path.read_text())
        config["artifacts"]["candidate_ledger"] = "work/one-diagram/untracked-ledger.md"
        config_path.write_text(json.dumps(config, indent=2) + "\n")
        self.git("add", "work/one-diagram/review-preparation.json")
        self.git("commit", "-qm", "map an uncommitted candidate ledger")
        result = self.run_command("one-diagram", "--check", expected=1)
        self.assertIn("candidate ledger is not committed at HEAD", result.stderr)


if __name__ == "__main__":
    unittest.main()
