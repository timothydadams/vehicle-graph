# Independent Review Summary: <review-id>

- Review ID: `<review-id>`
- Frozen candidate commit for this revision: `<full-git-commit>`
- Reviewer: `<name-or-process>`
- Review date: `<YYYY-MM-DD>`
- Method validity: `valid | invalid — <reason>`
- Disposition: `accepted | accepted_with_unresolved_ambiguities | changes_required | blocked_by_source_language | blocked_by_evidence | boundary_revision_required`

## Review Revision

- Original reviewed candidate commit: `<full-git-commit>`
- Remediated candidate commit: `<full-git-commit or none for initial review>`
- Review revision: `<R0, R1, R2, ...>`
- Re-review basis: `<initial review or finding IDs, resolution commits, and scope>`
- Source account reused: `yes | no — <reason; yes requires unchanged relevant evidence and extraction boundary>`

## Coverage

- Frozen boundary reviewed: `<path and concise scope>`
- Source-to-candidate pass: `complete | incomplete — <reason>`
- Candidate-to-source pass: `complete | incomplete — <reason>`
- Ambiguity review: `complete | incomplete — <reason>`
- Staged disclosure followed: `yes | no — <effect>`

## Result

- Blocking findings: `<IDs or none>`
- Non-blocking findings: `<IDs or none>`
- Acceptance-ready candidates: `<IDs, range, or referenced inventory; individual findings are not required>`
- Properly unresolved claims: `<ambiguity IDs, optional finding IDs, referenced inventory, or none>`
- Required remediation and re-review: `<concise routing>`
- Evidence or scope limitations: `<limitations or none>`

## Reviewer Declaration

I evaluated evidence-to-claim fidelity and did not use engineering plausibility,
extractor conclusions, or a desired graph shape as evidence. This disposition
is not canonical acceptance.

- Reviewer: `<name-or-process>`
- Recorded at: `<timestamp>`
