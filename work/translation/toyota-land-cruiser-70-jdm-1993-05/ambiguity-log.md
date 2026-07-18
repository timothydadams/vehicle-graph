# Translation Pilot Ambiguity Log

## Status and Attachment Rule

This pre-canonical log preserves document-specific uncertainty. An ambiguity
attaches only to content it could materially change; shared page, object,
category, or proximity is insufficient. Hard status is limited to the target
where the ambiguity would force materially different transcription or
translation.

| ID | Statement | Affected content | Type | Pilot status | What could materially change | Evidence needed | Current disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `TR-AMB-001` | Are provisional English section names the best evidenced Toyota normalizations? | Terminology entries for publication and chapter/page-type names | terminology normalization | soft | Normalized engineering wording, not Japanese transcription | Language-fidelity review plus cited parallel Toyota English usage | Open; retain literal wording separately. |
| `TR-AMB-002` | Should source-visible `品番` be normalized as “part number” in English? | Normalized identifier label for `品番 6742601` on PDF 2 only | terminology and identifier semantics | soft | Normalized label, not exact transcription or identifier value | Human Japanese review and cited Toyota identifier usage | Sharpened; exact transcription and identifier value are resolved; preserve `品番 6742601`. |
| `TR-AMB-003` | The artifact contains two distinct PDF pages bearing printed page `2-1`. | Supporting navigation at PDF pages 12 and 13 only | repeated printed-page identity | soft when both coordinates are preserved; hard only if a future citation uses `2-1` without a PDF coordinate | Which local artifact page a citation identifies | Preserve publication identity, printed page, and PDF coordinate together | Sharpened; pilot target and dependency mappings are resolved. Do not collapse PDF pages 12 and 13. |
| `TR-AMB-004` | No destination/market designation was found in the reviewed PDF 2 title, applicability, organization, or imprint material. | Only a destination/market assertion about the publication | applicability | soft for neutral translation; hard for a market-specific assertion | Claimed destination | Explicit source wording | Sharpened; neutral publication scope is clear, but absence does not prove a destination. Do not state factory-defined JDM. |
| `TR-AMB-005` | Similar connector IDs or terms in EWD168F may not identify the same physical connector. | Any later cross-publication comparison | cross-publication identity | soft for translation; hard for an equivalence claim | Entity identity, supporting role, and downstream applicability | Explicit equivalence evidence independent of matching labels | Open; equivalence excluded. |
| `TR-AMB-006` | How should `ウインドシールドワイパーリレー（リヤ用）` be normalized after preserving its parenthetical? | That PDF 80 / `5-2` component-name cell only | normalized wording | soft | Final English word order | Human Japanese review and cited Toyota English terminology | Sharpened; exact transcription and attachment are stable: the parenthetical modifies the relay (“for rear” provisionally). |
| `TR-AMB-007` | The publication does not establish applicability of later harness layouts to a 1990 PZJ70. | Any target-vehicle applicability assertion based on layout pages | applicability | soft for publication translation; hard for target-vehicle selection | Claimed vehicle scope | Source-stated scope plus independent target-vehicle evidence | Open; 1990 PZJ70 applicability excluded. |
| `TR-AMB-008` | What role does color have on the two selected harness layouts? | Harness identity/routing on PDF 15 / `2-3` and PDF 19 / `2-7` only | source-language convention | resolved | Harness association on those targets | Target-local legends and adequate color capture | Resolved: each target legend pairs harness symbol/name with a color swatch. Apply only to these targets; do not infer a publication-wide rule. |
| `TR-AMB-009` | How should Toyota-specific katakana loanwords be transliterated and normalized? | Only terminology entries containing affected loanwords | language and terminology | soft where Japanese is legible; hard only for an unreadable term | Transliteration, literal wording, or normalized engineering wording | Human Japanese review and cited parallel Toyota terminology | Open; assess term by term, not category-wide. |
| `TR-AMB-010` | Did source-language review require narrowing either selected full-page target? | `PILOT-TGT-007` and `PILOT-TGT-008` boundary decision only | boundary review | resolved | Full-page versus bounded scope | Completed review | Resolved: no narrowing proposed. `PILOT-TGT-007` remains full-page and blocked pending human language review; `008` is cleared. |
| `TR-AMB-011` | Later cell-level transcription may reveal a materially unreadable tiny label despite the page-level legibility review. | Only a later source region specifically shown unreadable | legibility and transcription | conditionally hard at that region | Literal source text, identifier, qualifier, or table cell | Direct high-resolution inspection or better capture | Sharpened; current targets show minor wear/bleed-through but no specifically unreadable in-boundary region, so this is not attached page-wide. |

No ambiguity in this table is automatically attached to every pilot page or
terminology entry.

Visual inspection of the target-local legends resolved `TR-AMB-008` only for
`PILOT-TGT-005` and `PILOT-TGT-006`.
