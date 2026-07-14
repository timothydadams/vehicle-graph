# Independent Review Manifest: <review-id>

## Identity and Freeze

- Review ID: `<review-id>`
- Extraction or milestone ID: `<id>`
- Frozen candidate commit: `<full-git-commit>`
- Package revision/status: `draft | frozen | in_review | findings_issued | remediation | re_review | review_complete | closed`
- Prepared by: `<name-or-process>`
- Prepared date: `<YYYY-MM-DD>`

The frozen commit identifies candidate content. Later review-output commits do
not change that candidate snapshot.

## Extraction Inputs

- Extraction boundary: `<repository path at frozen commit>`
- Publication identity artifact: `<repository path>`
- Applicability artifact: `<repository path>`
- Evidence inventory: `<repository path>`
- Source-language artifact: `<repository path>`
- Primary source artifacts: `<evidence IDs, printed locations, repository or approved local paths, and fingerprints/status>`
- Candidate ledger: `<repository path>`
- Ambiguity log: `<repository path>`
- Relevant working rationale, if any: `<repository path or none>`

## Initial-Review Materials

List only material available before the independent source account is saved.
When one artifact mixes neutral source guidance with candidate-specific
rationale, identify the exact initially disclosed headings or sections.

- `<governing documentation path>`
- `<publication identity and applicability path>`
- `<evidence inventory path>`
- `<extraction boundary path>`
- `<source-language record and source evidence>`
- `<primary source artifact or approved local path>`

## Intentionally Delayed Materials

- Candidate ledger: `<path>`
- Candidate-attached ambiguity IDs: `<where recorded>`
- Ambiguity log: `<path>`
- Extractor rationale: `<path or none>`
- Prior conclusions or downstream design material: `<path or none>`

## Required Review Outputs

- Independent source account: `independent-source-account.md`
- Findings: `findings.md`
- Review summary/disposition: `review-summary.md`
- Finding resolutions: `finding-resolutions.md`
- Canonical acceptance reference: `canonical-acceptance.md`

## Access and Completeness Check

- [ ] Every repository path resolves at the frozen commit.
- [ ] Required private evidence is available to the reviewer.
- [ ] Private evidence is bound to recorded source identity or fingerprint.
- [ ] Initial materials are sufficient to identify and read the complete boundary.
- [ ] Delayed materials are not required to perform the independent source account.
- [ ] Candidate content has no uncommitted or moving dependency.
- [ ] Package is ready to freeze.

## Disclosure Log

| Stage | Completed at | Commit or saved-output reference | Materials newly disclosed | Notes or premature exposure |
| --- | --- | --- | --- | --- |
| Independent source account | `<timestamp>` | `<reference>` | Initial-review materials only | `<notes>` |
| Candidate comparison | `<timestamp>` | `<reference>` | Candidate ledger | `<notes>` |
| Ambiguity and rationale check | `<timestamp>` | `<reference>` | Ambiguity log and relevant rationale | `<notes>` |
