# Japanese Land Cruiser 70 EWD Translation Workspace

This directory prepares a small, representative translation pilot for the
Japanese Toyota Land Cruiser 70 electrical wiring diagram identified by the
source-labeled part number `6742601` (`品番 6742601`). It contains no accepted
translation records or factory knowledge.

The catalog describes a Japanese-language publication dated **January 1995**
whose stated production applicability begins **May 1993** for `KZJ7#`, `PZJ7#`,
and `HZJ7#`. Publication date and production-applicability start are distinct.
The destination or market designation remains unestablished, and the catalog
does not establish applicability to a 1990 PZJ70.

The ignored local artifact was verified and the pilot evidence boundary frozen
on 2026-07-16. Its SHA-256 is
`1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6`;
it contains 90 PDF pages and is 101456077 bytes. These values identify the
reviewed local input without distributing it. The Milestone 6 machine-assisted
review package was completed on 2026-07-17 and is pending review and merge in
PR #24; the milestone remains in progress until that merge. The package does
not claim human Japanese-language verification or translation acceptance.
Three targets are cleared for Milestone 7 proposals, four are cleared with
recorded soft ambiguity, and the prose-heavy target remains blocked pending
qualified human language review.

## Supporting Records

- [Translation boundary](translation-boundary.md) defines the smallest current
  pilot and its exclusions.
- [Source-language record](source-language.md) inventories publication-specific
  language and layout conventions that require review.
- [Source-language review checklist](source-language-review-checklist.md)
  provides the pre-translation gate.
- [Source-language review results](source-language-review-results.md) records
  the method, dependency findings, and per-target dispositions.
- [Pilot review matrix](pilot-review-matrix.md) is the compact Milestone 7
  handoff.
- [Boundary review disposition](boundary-review-disposition.md) records that
  no amendment to the frozen boundary is proposed.
- [Evidence manifest](evidence-manifest.md) separates target pages,
  same-publication interpretive dependencies, supporting evidence, and local
  derivatives.
- [Terminology ledger](terminology-ledger.md) records provisional wording
  proposals without creating an approved glossary.
- [Ambiguity log](ambiguity-log.md) preserves document-specific uncertainty at
  the narrowest affected content.
- [Review checklist](review-checklist.md) separates language-fidelity review
  from engineering-terminology review.
- [Pilot page inventory](pilot-page-inventory.md) prioritizes representative
  target pages using verified locations and stable IDs.
- [Pilot capture manifest](pilot-capture-manifest.md) freezes the concise local
  inspection checklist for future review sessions.

## Intended Work Sequence

1. Re-verify the frozen artifact fingerprint before local review.
2. Review publication-specific source language for the mapped dependencies.
3. Narrow a target if an applicable hard blocker remains.
4. Preserve the frozen targets and dependency attachments during review.
5. Record terminology proposals and candidate-specific ambiguities.
6. Complete language-fidelity and engineering-review preparation.
7. Only then create real translation records in separately authorized work.

The minimum record shape is now implemented in
[`schemas/translation-record.schema.json`](../../../schemas/translation-record.schema.json),
but this workspace still contains no Toyota translation record. When the
source-language gates and boundary are ready in a later PR, canonical page
records will belong under
`translations/toyota/land-cruiser-70-jdm-1993-05/pages/`. This implementation
does not complete the workflow or authorize translating the pilot pages.

The governing workflow is [Reviewed Source Translation](../../../docs/TRANSLATION_WORKFLOW.md),
and source identity remains anchored in the [source catalog](../../../sources/toyota/land-cruiser-70-jdm-1993-05/README.md).
