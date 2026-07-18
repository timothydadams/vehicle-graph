# Pilot Source-Language Review Results

## Review authority and method

This is a machine-assisted review package, not an accepted translation and not
human Japanese-language verification. On 2026-07-17 the reviewer re-verified the
ignored PDF (`sha256:1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6`,
101456077 bytes, 90 pages), inspected each frozen page directly, manually
transcribed only the short strings needed below, used machine-assisted Japanese
reading for provisional glosses, and compared targets with explanatory pages in
the same publication. No OCR, bulk text extraction, or external terminology
source was used. The visual source controls every reading.

`Transcription status` below means review readiness, not that a full-page
transcription was created. `Human review` identifies the remaining language
review needed before acceptance; it does not falsely claim that review occurred.

## Primary targets

| ID | Location and review scope | Visible headings / identifiers and material qualifiers | Transcription / convention status | Dependencies | Unresolved readings / ambiguity | Disposition and rationale | Human review / downstream readiness |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `PILOT-TGT-001` | PDF 2, full page; identity, organization, scope prose | `トヨタ ランドクルーザー70 配線図集`; `KZJ7#系`, `PZJ7#系`, `HZJ7#系`; `（1993-5～）`; `1995年1月`; `品番 6742601` | Short strings exact/high confidence; prose legible; organization and applicability structure reviewed | none | `TR-AMB-001`, `TR-AMB-002`, `TR-AMB-004`, `TR-AMB-007`; normalization and destination remain unresolved, but visible scope is stable | `cleared_with_recorded_ambiguity`: literal source structure is stable and ambiguities do not require a different transcription | Human language review required for accepted translation, not to choose between material source readings; ready for proposal with ambiguities |
| `PILOT-TGT-002` | PDF 5 / `1-2`, full page; five-part organization, explanatory prose, bounded abbreviation table | `本書の構成`; `略語の説明`; chapter labels `総説`, `配線艤装図 & リレーロケーション`, `システム別配線図`, `共通コネクター`, `索引` | Headings and table structure legible; only abbreviations used by the pilot need later transcription | none (primary evidence for itself) | `TR-AMB-001`, term-specific `TR-AMB-009`; normalized chapter wording remains open | `cleared_with_recorded_ambiguity`: page roles and abbreviation-field structure are stable; normalization is soft | Human review required before acceptance; ready for bounded pilot translation, excluding unused abbreviation entries from detailed review |
| `PILOT-TGT-003` | PDF 80 / `5-2`, full component-name-order index | `索引（部品名称順）`; `部品名`; `コネクター NO.`; `システム別配線図ページ`; `配線艤装図ページ`; row qualifiers including engine/body/door/location parentheses | Table is legible; left-to-right field order and independent two-panel reading reviewed | `PILOT-DEP-006` | `TR-AMB-006`, term-specific `TR-AMB-009`; dense terminology needs human checking, but cells are structurally unambiguous | `cleared_with_recorded_ambiguity`: identifiers and page references can be copied faithfully; terminology normalization remains soft | Human review required for Japanese term fidelity; ready for translation proposal with term-level ambiguities |
| `PILOT-TGT-004` | PDF 18 / `2-6`, full instrument-panel component/connector list | `インストルメントパネル（1HZ, 1PZ）`; connector IDs, grid locations, component names, date/body/side parentheses | Full page legible; row pattern is connector ID, grid coordinate, component name; punctuation and case are material | `PILOT-DEP-002`, `PILOT-DEP-006` | term-specific `TR-AMB-009`; no material structural ambiguity found | `cleared_with_recorded_ambiguity`: table correspondence is stable; loanword normalization is not | Human review required for accepted term translations; structurally ready |
| `PILOT-TGT-005` | PDF 15 / `2-3`, full engine harness layout | `エンジン（1HZ, 1PZ）`; grid `1`–`6` / `A`–`D`; connector, ground, and harness identifiers; harness legend and color swatches | Legible, including tiny identifiers on direct high-resolution inspection; label-to-object, grid, connector, ground, routing, and color-key conventions reviewed | `PILOT-DEP-002` | no material hard ambiguity; `TR-AMB-008` resolved for this target | `cleared_for_pilot_translation`: relevant notation is explicit and no materially different source reading remains | Human review still required by the later acceptance workflow, but not to choose the source structure; ready for Milestone 7 proposal |
| `PILOT-TGT-006` | PDF 19 / `2-7`, full left instrument-panel harness layout | `インストルメントパネル（1HZ, 1PZ左側）`; grid, connector, ground, harness IDs; harness legend and swatches; date qualifiers | Legible; connector/list correspondence, routing, grid, qualifier, and color-key conventions reviewed | `PILOT-DEP-002` | no material hard ambiguity; `TR-AMB-008` resolved for this target | `cleared_for_pilot_translation`: source associations and applicable conventions are stable | Human review still required before acceptance; ready for Milestone 7 proposal |
| `PILOT-TGT-007` | PDF 6 / `1-3`, full prose-heavy explanatory page | `各章の見方`; `配線艤装図`; multiple explanatory callouts and footnotes | Headings and convention callouts are legible; full prose has not received qualified human language-fidelity review | none; its separate dependency role is only for other targets | `TR-AMB-001`, term-specific `TR-AMB-009`; sustained explanatory grammar could materially alter a full-page English rendering | `blocked_pending_human_language_review`: structural conventions are usable as a dependency, but the frozen full-page translation target needs qualified prose review | Human Japanese-language review required before translating this full target; not ready |
| `PILOT-TGT-008` | PDF 40 / `3-2`, full single-page circuit | `電源（1HZ, 1PZ）`; production legend `○：～'95.1`, `□：'95.1～`; wire-color labels, component/connector/terminal identifiers | Full page legible; component boundaries, joins, relay contacts, terminals, source/ground, wire color, state qualifiers, and page-local IDs reviewed | `PILOT-DEP-003`, `PILOT-DEP-004`, `PILOT-DEP-005` | no material hard ambiguity found | `cleared_for_pilot_translation`: applicable circuit notation is defined or visibly stable | Human review required for accepted label wording, not circuit transcription; ready for Milestone 7 proposal |

## Publication identity and applicability wording

| Exact source string | Confidence | Provisional literal meaning | Normalized navigation meaning | Remaining question |
| --- | --- | --- | --- | --- |
| `トヨタ ランドクルーザー70 配線図集` | high | Toyota Land Cruiser 70 collection of wiring diagrams | Land Cruiser 70 electrical wiring diagram publication | Factory-style English title remains terminology review (`TR-AMB-001`). |
| `品番 6742601` | high | product/part number 6742601 | source-labeled identifier 6742601 | Whether English should say “part number” remains `TR-AMB-002`. |
| `1995年1月` | high | January 1995 | publication statement | None material to transcription. |
| `KZJ7#系`, `PZJ7#系`, `HZJ7#系` | high | KZJ7#, PZJ7#, HZJ7# families/series | stated model families | Does not establish destination or a 1990 PZJ70. |
| `（1993-5～）` | high | from 1993-5 onward | production applicability begins May 1993 | Must remain distinct from publication date and target-vehicle applicability. |

Nearby prose states that the book contains wiring diagrams for vehicles
produced from May 1993 and that replacement editions may be issued for
specification changes. It does not visibly establish “JDM,” coverage before the
stated start, or identity with EWD168F.

## Abbreviations needed by this pilot

Only pilot-visible abbreviations were reviewed; unused table entries remain
outside the detailed boundary.

| Source abbreviation | Source explanation | Provisional literal reading | Affected targets | Confidence / human review |
| --- | --- | --- | --- | --- |
| `F/B` | `ヒューズブロック` | fuse block | `PILOT-TGT-008` | high; normalization review remains |
| `J/B` | `ジャンクションブロック` | junction block | `PILOT-TGT-008` | high |
| `R/B` | `リレーブロック` | relay block | `PILOT-TGT-008` | high |
| `LH`, `RH` | `レフトハンド`, `ライトハンド` | left hand, right hand | `PILOT-TGT-003`, `PILOT-TGT-004` | high; preserve source abbreviation |
| `FR`, `RR` | `フロント`, `リヤ` | front, rear | table targets | high |

## Interpretive dependencies

| ID | Location / scope | Reviewed conventions | Status and affected targets | Uncertainty / disposition |
| --- | --- | --- | --- | --- |
| `PILOT-DEP-002` | PDF 6 / `1-3`, full page | component connector No.; component name; ground-point symbol/name; title; harness symbol/name; connector shape and cavity number; location lookup; wire-to-wire connector number/name/shape; grid association; identifier examples | reviewed for `PILOT-TGT-004`–`006` | No material convention blocker. Color semantics are supplied on the targets' own legends, not this page. |
| `PILOT-DEP-003` | PDF 7 / `1-4`, right power/ground region | fuse-load and ground-load presentations; fuse/ground names; system name plus referenced page; fuse mounting location; ground symbol meaning | reviewed for `PILOT-TGT-008` | Relay-location half is outside the bounded dependency and non-material to this target. |
| `PILOT-DEP-004` | PDF 8 / `1-5`, full page | upper circuit/lower connector-shape page structure; supplied-power indication; title; J/B; fuse name/location; internal circuit; connector and terminal depiction; connector color; wire color; operating condition; source-local cross-references | reviewed for `PILOT-TGT-008` | Wire color is written as Japanese color names; two-color example describes base color plus a stripe. No shield/twist special mark occurs on the target. |
| `PILOT-DEP-005` | PDF 9 / `1-6`, full page | J/B/R/B names; relays, fuses, internal circuits; block-side versus harness-side connector shapes; terminal numbers; wire-to-wire mating shapes and connector numbers; female/male terminal footnotes | reviewed for `PILOT-TGT-008` | Target uses R/B No.1 but no material wire-to-wire or J/B internal depiction; those reviewed conventions are non-material there. |
| `PILOT-DEP-006` | PDF 10 / `1-7`, left index region | connector-number-order and component-name-order index roles; component name, connector No., system-circuit page, harness-layout page; rows read horizontally within independent panels | reviewed for `PILOT-TGT-003`, `PILOT-TGT-004` | No defined ditto mark or defined blank-cell meaning was found. Blank cells must remain blank; do not infer repetition. |

## Circuit convention occurrence on `PILOT-TGT-008`

| Convention | Result |
| --- | --- |
| Component boundaries, terminals, relay contacts, joins, connector shapes, wire colors, source/ground marks | present and materially required |
| Production/state qualifier legend (`○`, `□`) | present and materially required |
| Page-to-page continuation mark | absent; full circuit edges and the lower connector strip were inspected, high confidence |
| Separate state/contact table | absent; circuit and margins inspected, high confidence |
| Switch-state legend | absent; ignition-switch contact drawing and production legend are present, high confidence |
| Operating-condition prose | absent; no applicable prose instance found, high confidence |
| Wire-to-wire connector and J/B internal-circuit conventions | absent/non-material on this target |

Wire colors on the selected circuit are Japanese color names, including
single colors such as `白`, `赤`, `黒`, `緑`, `黄`, `青` and paired forms such as
`青－白`, `黒－黄`, `白－青`. The publication's explanation says that when two
colors are shown, the first is the base and the second is the stripe. Preserve
the exact source labels and separator; English-letter color abbreviations are
not the applicable convention here.

## Qualifiers and legibility

Parentheses attach locally to the immediately preceding component or heading;
they preserve engine, door, front/rear, side, production-date, or equipment
scope. For `ウインドシールドワイパーリレー（リヤ用）`, the exact
transcription is stable and the parenthetical grammatically modifies the relay:
provisional literal structure, “windshield wiper relay (for rear).” A final
Toyota-normalized name remains `TR-AMB-006`.

All reviewed pages have minor scan wear/bleed-through but no materially
unreadable in-boundary text was found during direct inspection. Tiny labels on
PDF 15, 19, 40, and 80 require high-resolution inspection. `TR-AMB-011` remains
a handling rule for any later cell-level transcription, not an attachment to
these targets absent a specifically unreadable region.
