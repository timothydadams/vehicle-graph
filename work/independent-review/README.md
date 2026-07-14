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
```

Do not place current extraction conclusions in the reusable template. A real
package may link to existing extraction artifacts; it need not copy them.

## Manual Workflow

1. **Prepare.** Copy the template, assign a review ID, complete the manifest,
   list every artifact, and divide materials into initial and delayed stages.
   Confirm that private evidence is lawfully available to the reviewer and tied
   to the recorded source identity or fingerprint.
2. **Freeze.** Commit the complete candidate extraction, then record that full
   commit hash in the package manifest. Commit the prepared manifest before the
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

The initial capability is intentionally manual. It adds no agent service, CI
gate, database, schema framework, or automatic acceptance mechanism.
