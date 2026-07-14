# Independent Review Working Material

This directory contains the reusable, pre-canonical convention for independent
review packages. Review records are auditable working material; neither their
presence in Git nor an `accepted` review disposition makes candidate knowledge
canonical.

The detailed method is [Independent Review](../../docs/INDEPENDENT_REVIEW.md).
The [template](template/) is kept under `work/` because it creates working review
records, not canonical JSON or a new knowledge layer.

## Package Layout

Copy `template/` to a stable package directory such as:

```text
work/independent-review/<review-id>/
```

Keep these filenames so a contributor can locate each review stage:

```text
review-manifest.md
independent-source-account.md
findings.md
review-summary.md
finding-resolutions.md
canonical-acceptance.md
REVIEW_TASK.md
```

Do not place current extraction conclusions in the reusable template. A real
package may link to existing extraction artifacts; it need not copy them. The
six review records are instantiated from `template/`; the preparation command
generates `REVIEW_TASK.md` from the frozen operational inputs.

## Prepare a Package

Candidate extraction must be clean and committed before preparation. Preview
the discovered artifact mappings, frozen commit, allocated review ID, package
path, and all three disclosure stages without writing anything:

```shell
scripts/prepare-independent-review one-diagram --check
```

An explicit ID may be previewed or created with `--review-id IR-001`. Otherwise
the command deterministically allocates the next unused `IR-NNN` directory.
Create the package only after checking the preview:

```shell
scripts/prepare-independent-review one-diagram
```

The command validates required and disclosed paths, the reusable templates, the
workspace's explicit readiness signal, committed extraction inputs, local
source-material availability, and target-package absence. It then populates
mechanically known manifest fields and creates `REVIEW_TASK.md`. It never
overwrites a package, commits files, invokes Codex, performs review, populates
findings or reviewer declarations, or records canonical acceptance.

One Diagram uses
[`review-preparation.json`](../one-diagram/review-preparation.json) because its
publication/applicability material and source-language record do not map safely
to disclosure stages by filename alone. The configuration records only paths,
an existing readiness signal, exact section disclosures, and unavoidable
exposure. It does not duplicate evidence or extraction conclusions. A missing,
ambiguous, unreadable, uncommitted, escaped, or structurally incomplete input
causes an actionable failure rather than a guessed mapping.

After package creation, review the generated manifest, commit the prepared
package, and paste `REVIEW_TASK.md` into a fresh Codex session rooted at the
repository. Package preparation itself is not independent review or acceptance.

## Review Workflow

1. **Prepare.** Run the preparation command against a clean, committed
   extraction, inspect its staged-disclosure decisions, and confirm private
   evidence is lawfully available to the reviewer and tied to the recorded
   source identity or fingerprint.
2. **Freeze.** The command records the complete candidate extraction's full
   commit hash in the package manifest. Commit the prepared package before the
   review begins. Do not review a moving branch or uncommitted candidate state.
3. **Launch fresh.** Start a fresh Codex session at the repository root. Provide
   only the repository path, review ID or manifest path, frozen commit, output
   path, and [reviewer prompt](../../prompts/independent-review.md). Do not pass
   extractor conclusions or suspected findings.
4. **Review.** The reviewer opens initial-stage material, writes and saves the
   independent source account, then opens the candidate ledger, and only later
   opens the ambiguity log and relevant rationale. The reviewer writes findings
   and a review summary without changing extraction artifacts.
5. **Remediate.** The extractor or another designated contributor resolves
   findings in separate commits and records each resolution in
   `finding-resolutions.md`.
6. **Re-review.** Freeze the remediated candidate commit and record a new review
   revision, its basis, and whether the source account is reused. Reuse requires
   an explicit reason and unchanged relevant evidence and extraction boundary.
   The reviewer checks that frozen commit using the scope required by each
   finding and records verification. Boundary, evidence, source-language, or
   applicability changes may require broader re-review.
7. **Accept or defer.** A human records the canonical acceptance decision in
   `canonical-acceptance.md`, referencing the reviewed candidate and resolution
   commits. Review completion alone never canonicalizes knowledge.

Preparation remains a local, contributor-invoked operation. It adds no agent
service, CI gate, database, schema framework, or automatic acceptance mechanism.
