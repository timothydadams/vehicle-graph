# Frozen Pilot Page Inventory

## Status

The targets below were mapped by visual inspection of the verified local
artifact on 2026-07-16. English descriptions are provisional navigation aids,
not accepted translations. Mapping readiness does not satisfy the
source-language review gate.

| Target ID | PDF page | Printed page | Page category | Scope | Selection rationale / capability tested | Known qualifiers | Material source-language dependencies | Intended future record type | Readiness and blockers |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| `PILOT-TGT-001` | 2 | none visible | title and applicability | full page | Tests source identity, publication date, model notation, applicability wording, and source-local identifier. | `KZJ7#`, `PZJ7#`, `HZJ7#`; `1993-5～`; `品番 6742601` | Exact Japanese identity/applicability wording requires language review. | page | Evidence mapped; hard language-review gate remains. |
| `PILOT-TGT-002` | 5 | `1-2` | manual organization and abbreviations | full page | Tests chapter organization, prose, tables, abbreviations, and page roles. | Chapter 1 context. | None identified; applicable organization and abbreviation review occurs within this target's primary-evidence boundary. | page | Evidence mapped; organization and abbreviations unreviewed. |
| `PILOT-TGT-003` | 80 | `5-2` | component-name index | full page | Tests dense table structure, component terms, identifiers, qualifiers, and page references. | Chapter 5; source-visible component-name ordering. | `PILOT-DEP-006` | page | Evidence mapped; table reading and identifier conventions unreviewed. |
| `PILOT-TGT-004` | 18 | `2-6` | harness-layout component list | full page | Tests table headings, connector numbers, component labels, grid references, and qualifiers. | `1HZ, 1PZ`; instrument-panel context. | `PILOT-DEP-002`, `PILOT-DEP-006` | page | Evidence mapped; table, grid, and connector conventions unreviewed. |
| `PILOT-TGT-005` | 15 | `2-3` | engine harness layout | full page | Tests labels embedded in a colored diagram, source-local identifiers, grids, and engine qualifiers. | `1HZ, 1PZ`. | `PILOT-DEP-002` | page | Evidence mapped; harness conventions and color role unreviewed. |
| `PILOT-TGT-006` | 19 | `2-7` | instrument-panel harness layout | full page | Adds a dense layout paired with the `2-6` list and exercises connector/label correspondence. | `1HZ, 1PZ`. | `PILOT-DEP-002` | page | Evidence mapped; harness conventions, label association, and color role unreviewed. |
| `PILOT-TGT-007` | 6 | `1-3` | prose-heavy harness explanation | full page | Sustained explanatory text and callouts test transcription, literal wording, normalized wording, punctuation, qualifiers, paragraph structure, and cross-references. It is not dominated by tiny labels. | Chapter 1 explanatory context. | None identified; this page separately supplies `PILOT-DEP-002` conventions to other layout targets and is not its own dependency. | page | Evidence mapped; no translation performed; Japanese language review required. |
| `PILOT-TGT-008` | 40 | `3-2` | system circuit | full page | Bounded single-page circuit tests notation, components, connectors, wire labels, source-local identifiers, and engine qualifiers without a multi-page target. | Provisional system description: power (`1HZ, 1PZ`). | `PILOT-DEP-003`, `PILOT-DEP-004`, `PILOT-DEP-005` | page | Evidence mapped; diagram conventions remain hard review blockers. No page-to-page circuit continuation was observed for this target. |

The IDs are independent of translated titles and are reserved for later records
and review packages. No target was selected based on presumed applicability to
a 1990 PZJ70 or on correspondence with another publication.

## Dependency Inventory

All dependencies use source publication
`toyota-land-cruiser-70-jdm-1993-05`. They were located, not language-reviewed.

| Dependency ID | PDF page | Printed page / region | Dependency role and convention defined | Affected targets | Review status | Blocker classification |
| --- | ---: | --- | --- | --- | --- | --- |
| `PILOT-DEP-002` | 6 | `1-3`, full page | Harness-layout labels, connector symbols, grid/location references, ground-point marks, and label association. | `PILOT-TGT-004`, `PILOT-TGT-005`, `PILOT-TGT-006` | Located; source-language review pending. | Hard for affected layout conventions. |
| `PILOT-DEP-003` | 7 | `1-4`, right-side power/ground region | Power-source and ground presentation used by system circuits. | `PILOT-TGT-008` | Located; source-language review pending. | Hard if marks permit materially different circuit transcription. |
| `PILOT-DEP-004` | 8 | `1-5`, full page | System-circuit page structure, connector/terminal depiction, wire color, operating conditions, and related references. | `PILOT-TGT-008` | Located; source-language review pending. | Hard for circuit transcription. |
| `PILOT-DEP-005` | 9 | `1-6`, full page | Junction/relay block and wire-to-wire connector shapes and terminal numbering. | `PILOT-TGT-008` | Located; source-language review pending. | Hard where those symbols occur. |
| `PILOT-DEP-006` | 10 | `1-7`, left-side index region | Connector-number/component-name index lookup fields and referenced-page columns. | `PILOT-TGT-003`, `PILOT-TGT-004` | Located; source-language review pending. | Hard for table-field interpretation; soft for literal visible-cell transcription. |

A repository-created translation is not an interpretive dependency. Dependencies
are attached only to targets whose reading they can materially change.
`PILOT-DEP-001` was removed after pre-merge review found no non-circular,
target-specific interpretive role. The five active dependency IDs retain the
deliberate gap rather than being renumbered.
