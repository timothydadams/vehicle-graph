# Frozen Translation Pilot Boundary

## Governing Artifact

Boundary version: `2026-07-16`.

- Source publication: `toyota-land-cruiser-70-jdm-1993-05`
- Source-labeled identifier: `品番 6742601`
- Verified ignored path: `.evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf`
- SHA-256: `1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6`
- Size: `101456077` bytes
- PDF page count: `90`

This fingerprint, rather than the path alone, governs the reproducible boundary.
The Japanese publication remains primary evidence. English descriptions below
are provisional navigation descriptions, and the boundary is not cleared for
translation until applicable source-language review gates are complete.

## Included Primary Targets

| Target ID | PDF page | Printed page | Scope | Provisional navigation description |
| --- | ---: | --- | --- | --- |
| `PILOT-TGT-001` | 2 | none visible | full page | title, identity, and applicability page |
| `PILOT-TGT-002` | 5 | `1-2` | full page | manual organization and abbreviations |
| `PILOT-TGT-003` | 80 | `5-2` | full page | component-name index |
| `PILOT-TGT-004` | 18 | `2-6` | full page | instrument-panel harness component list (`1HZ, 1PZ`) |
| `PILOT-TGT-005` | 15 | `2-3` | full page | engine harness layout (`1HZ, 1PZ`) |
| `PILOT-TGT-006` | 19 | `2-7` | full page | instrument-panel harness layout (`1HZ, 1PZ`) |
| `PILOT-TGT-007` | 6 | `1-3` | full page | prose-heavy harness-layout explanation |
| `PILOT-TGT-008` | 40 | `3-2` | full page | power system circuit (`1HZ, 1PZ`) |

## Included Interpretive Dependencies

The dependency inventory is defined in
[pilot-page-inventory.md](pilot-page-inventory.md). Five dependencies remain:
`PILOT-DEP-002` through `PILOT-DEP-006`, on PDF pages 6 through 10. The stable-ID
gap is deliberate. PDF page 5 is only primary evidence for `PILOT-TGT-002`, not
an interpretive dependency.

PDF page 6 has dual primary-target and interpretive-dependency roles for
different pilot boundaries. `PILOT-TGT-007` translates the full page as its own
primary evidence; `PILOT-DEP-002` records that page's conventions only for the
separate harness-layout targets `PILOT-TGT-004`, `PILOT-TGT-005`, and
`PILOT-TGT-006`. Neither role makes page 6 a dependency of itself.

## Supporting Navigation

PDF pages 3 (publication/replacement history), 4 / printed `1-1` (chapter 1
contents), 12 and 13 / printed `2-1` (two distinct PDF coordinates bearing the
same printed identifier), 39 / printed `3-1` (chapter 3 contents), and 79 /
printed `5-1` (adjacent index context) are included only for navigation.

## Excluded Publication Content

All other pages and all regions outside the specifically bounded dependency
region on printed `1-4` and `1-7` are excluded. The boundary also excludes
source images, OCR output, full-manual indexing or translation, accepted
translation JSON, terminology promotion, rendered English manuals, graph
extraction, EWD168F connector equivalence, and applicability to a 1990 PZJ70.

## Unresolved Mappings

There are no unresolved PDF mappings for selected targets or dependencies.
The artifact contains repeated printed page `2-1` at PDF pages 12 and 13; both
coordinates are preserved and neither was guessed away.

## Hard Blockers and Soft Uncertainties

Hard blockers are the pending source-language reviews of identity/applicability
wording, organization and abbreviations, harness and grid conventions, table
fields, circuit notation, wire-color notation, connector/terminal depiction,
and junction/continuation conventions where used. No human language verification
is claimed.

Soft uncertainties include normalized English terminology, destination/market,
the semantic role of harness color unless it changes transcription, and later
vehicle selection. Scan legibility remains candidate-specific: it becomes hard
only for a region where materially different transcriptions remain possible.
