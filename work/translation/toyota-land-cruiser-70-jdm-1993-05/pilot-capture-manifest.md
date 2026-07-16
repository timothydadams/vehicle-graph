# Frozen Pilot Capture Manifest

## Artifact and Boundary

- Source publication: `toyota-land-cruiser-70-jdm-1993-05`
- Source-labeled identifier: `品番 6742601`
- Ignored artifact path: `.evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf`
- SHA-256: `1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6`
- Size: `101456077` bytes
- Page count: `90`
- Frozen boundary version: `2026-07-16`

Source files and any local page derivatives remain gitignored. This manifest
contains navigation metadata only, not source images, OCR, accepted
translation, or factory-authored English.

## Inspection Checklist

| Stable ID | PDF page | Printed page / region | Role | Mapping verified | Local capture required | Review readiness |
| --- | ---: | --- | --- | --- | --- | --- |
| `PILOT-TGT-001` | 2 | none visible | target | yes | yes, for future review package only | source-language review pending |
| `PILOT-TGT-002` | 5 | `1-2` | target | yes | yes, for future review package only | source-language review pending |
| `PILOT-TGT-003` | 80 | `5-2` | target | yes | yes, for future review package only | source-language review pending |
| `PILOT-TGT-004` | 18 | `2-6` | target | yes | yes, for future review package only | source-language review pending |
| `PILOT-TGT-005` | 15 | `2-3` | target | yes | yes, including color fidelity | source-language review pending |
| `PILOT-TGT-006` | 19 | `2-7` | target | yes | yes, including color fidelity | source-language review pending |
| `PILOT-TGT-007` | 6 | `1-3` | target | yes | yes, for future review package only | source-language review pending |
| `PILOT-TGT-008` | 40 | `3-2` | target | yes | yes, at connector-label legibility | source-language review pending |
| `PILOT-DEP-001` | 5 | `1-2`, full page | dependency | yes | shared with target capture | source-language review pending |
| `PILOT-DEP-002` | 6 | `1-3`, full page | dependency | yes | shared with target capture | source-language review pending |
| `PILOT-DEP-003` | 7 | `1-4`, right-side region | dependency | yes | yes, bounded region | source-language review pending |
| `PILOT-DEP-004` | 8 | `1-5`, full page | dependency | yes | yes | source-language review pending |
| `PILOT-DEP-005` | 9 | `1-6`, full page | dependency | yes | yes | source-language review pending |
| `PILOT-DEP-006` | 10 | `1-7`, left-side region | dependency | yes | yes, bounded region | source-language review pending |

Supporting navigation pages are PDF 3, 4 (`1-1`), 12 (`2-1`), 13 (`2-1`),
39 (`3-1`), and 79 (`5-1`). They require no standalone capture unless a later
review package needs navigation context. All other PDF pages are excluded.

## Unresolved Blockers

All mappings are resolved. Applicable conventions and Japanese wording remain
unreviewed and are hard blockers only where they could force materially
different transcription or translation. No human language verification is
claimed. Destination/market, normalized terminology, 1990 PZJ70 applicability,
and cross-publication connector identity are not established.

## Verification Commands

```sh
python3 scripts/fingerprint-source.py \
  .evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf
pdfinfo .evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf
git check-ignore -v \
  .evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf
```

The capture and evidence manifests must be updated together if the boundary or
artifact fingerprint changes.
