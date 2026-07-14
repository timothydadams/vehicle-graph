# Independent Review Findings: <review-id>

Use stable IDs in the form `<review-id>-F001`, incrementing without reuse. Keep
closed and superseded findings in this file. Classify each finding at the
earliest failed workflow layer using
[Independent Review](../../../docs/INDEPENDENT_REVIEW.md#finding-taxonomy).

Allowed classes are `candidate_defect`, `missing_ambiguity`,
`incorrect_ambiguity_attachment`, `source_language_defect`,
`evidence_inventory_defect`, `extraction_boundary_defect`,
`applicability_defect`, `unsupported_interpretation_or_derivation`,
`acceptance_ready_candidate`, and `properly_unresolved_claim`.

## <review-id>-F001

- Review ID: `<review-id>`
- Finding ID: `<review-id>-F001`
- Finding class: `<allowed class>`
- Affected candidate or workflow artifact: `<stable candidate ID or repository path>`
- Source evidence: `<evidence ID and precise source location>`
- Description: `<what failed or was verified>`
- Exact assertion or field affected: `<field/assertion, or not applicable with reason>`
- Required action: `<specific remediation or none>`
- Blocking status: `blocking | non_blocking | informational`
- Affected scope: `<candidate IDs, convention users, evidence dependents, applicability set, or boundary>`
- Required re-review scope: `candidate | dependent_candidates | ambiguity_attachments | source_language_dependents | evidence_dependents | applicability_dependents | complete_boundary`
- Resolution status: `open | proposed | resolved | verified | deferred | superseded`
- Resolution commit: `<full-git-commit or pending>`
- Reviewer verification: `<reviewer, date, evidence checked, and result or pending>`
