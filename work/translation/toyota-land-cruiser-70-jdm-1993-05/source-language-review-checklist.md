# Source-Language Review Checklist

## Status

Milestone 6 machine-assisted review was performed on 2026-07-17. `reviewed`
does not mean human Japanese-language verification. Detailed evidence and
limitations are in [source-language-review-results.md](source-language-review-results.md).

| Review item | Status | Exact source location | Affected targets | Review notes / disposition | Ambiguities |
| --- | --- | --- | --- | --- | --- |
| Title and identifier | reviewed_with_ambiguity | PDF 2, title and lower-right imprint | `PILOT-TGT-001` | Exact strings stable; English normalization remains open | `TR-AMB-001`, `002` |
| Publication date and production applicability | reviewed_with_ambiguity | PDF 2, title qualifiers, third introductory paragraph, lower-right imprint | `PILOT-TGT-001` | January 1995 and `1993-5～` are distinct; no destination or 1990 applicability inferred | `TR-AMB-004`, `007` |
| Model-family notation | reviewed | PDF 2, title qualifier block | `PILOT-TGT-001` | Preserve `KZJ7#系`, `PZJ7#系`, `HZJ7#系` and `#` | — |
| Chapter organization | reviewed_with_ambiguity | PDF 5 / `1-2`, five numbered descriptions | `PILOT-TGT-002` | Five roles stable; English chapter names provisional | `TR-AMB-001` |
| Printed page numbering | reviewed | frozen mappings; PDF 12 and 13 both printed `2-1` | all | Always preserve PDF and printed coordinates | `TR-AMB-003` |
| Index/list table fields and reading order | reviewed | PDF 10 / `1-7` left; PDF 18 / `2-6`; PDF 80 / `5-2` | `PILOT-TGT-003`, `004` | Horizontal rows; component, connector, system-page, layout-page fields; blank has no inferred meaning | — |
| Grid and location references | reviewed | PDF 6 / `1-3`, `ロケーション`; PDF 15 / `2-3`; PDF 19 / `2-7` | `PILOT-TGT-004`–`006` | Number/letter intersection locates connector callouts | — |
| Connector/local identifiers | reviewed | PDF 6 / `1-3`; PDF 8 / `1-5`; PDF 9 / `1-6` | `PILOT-TGT-004`–`006`, `008` | Preserve case, punctuation, number, shape, and cavity position | — |
| Harness labels, association, routing, and color | reviewed | PDF 6 / `1-3`; target legends PDF 15 / `2-3`, PDF 19 / `2-7` | `PILOT-TGT-005`, `006` | Target legends explicitly associate symbol/name with swatch; do not generalize beyond these layouts | `TR-AMB-008` resolved |
| Parenthetical qualifiers | reviewed_with_ambiguity | PDF 2, 18, 19, 40, 80; `（リヤ用）` on PDF 80 / `5-2` | terminology-bearing targets | Parenthetical attaches locally; preserve before normalization | `TR-AMB-006`, term-specific `009` |
| Pilot-needed abbreviations | reviewed_with_ambiguity | PDF 5 / `1-2`, abbreviation table | `PILOT-TGT-003`, `004`, `008` | `F/B`, `J/B`, `R/B`, `LH`, `RH`, `FR`, `RR` reviewed; unused entries remain out of detailed scope | term-specific `TR-AMB-009` |
| Circuit page, block, terminal, contact, and join notation | reviewed | PDF 7 / `1-4` right; PDF 8 / `1-5`; PDF 9 / `1-6`; PDF 40 / `3-2` | `PILOT-TGT-008` | Applicable marks support a stable circuit transcription | — |
| Wire-color notation | reviewed | PDF 8 / `1-5`, `線色`; PDF 40 / `3-2` | `PILOT-TGT-008` | Japanese color names; first of two colors is base, second stripe; preserve separator | — |
| Continuation notation | not_applicable | PDF 8 / `1-5` and full PDF 40 / `3-2` margins/edges | `PILOT-TGT-008` | Inspected; no continuation instance found, high confidence | — |
| State/contact table and switch-state legend | not_applicable | full PDF 40 / `3-2` | `PILOT-TGT-008` | No separate table/legend found; ignition contact depiction and production legend remain in scope | — |
| Operating-condition text | not_applicable | PDF 8 / `1-5` definition; full PDF 40 / `3-2` | `PILOT-TGT-008` | Definition reviewed; no target instance found, high confidence | — |
| Legibility and unreadable-text handling | reviewed_with_ambiguity | every target/dependency; tiny-label regions on PDF 15, 19, 40, 80 | all | Minor wear/bleed-through; no specific materially unreadable in-boundary region found | `TR-AMB-011` retained as cell-level handling rule |
| Full explanatory prose | pending_human_review | PDF 6 / `1-3`, full page | `PILOT-TGT-007` | Conventions usable as dependency; full-page prose translation blocked pending qualified review | term-specific `TR-AMB-009` |
| Transcription/literal/normalized separation | reviewed | all review artifacts | all | Review notes keep exact strings, provisional gloss, and navigation/normalization distinct | — |
