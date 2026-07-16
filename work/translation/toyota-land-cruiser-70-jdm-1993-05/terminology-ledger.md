# Provisional Terminology Ledger

## Status and Entry Convention

This pre-canonical ledger records terminology proposals; it is not an approved
glossary. Each entry preserves the Japanese source term, optional
transliteration, literal translation, proposed normalized Toyota English,
source location, parallel English terminology evidence, scope, independent
proposal and review statuses, ambiguity references, rationale, and required
reviewer roles. Literal and normalized forms remain separate. No status implies
acceptance of a page or graph fact.

Proposal lifecycle, language-fidelity review, and engineering-terminology
review are independent fields. Progress in one does not imply progress in
another.

The conservative working vocabularies are:

- **Proposal status:** `unreviewed`, `proposed`, `corroborated`, or `rejected`.
- **Language-fidelity status:** `unreviewed`, `machine-cross-checked`, or
  `human-language-verified`.
- **Engineering-terminology status:** `unreviewed`, `engineering-reviewed`, or
  `changes-required`.

These values are descriptive workspace states, not numeric confidence scores
and not an implementation schema.

## Seed Entries

The terms below were visibly encountered in reviewed planning samples. Where a
precise printed location has not been established, it remains pending.

| Japanese source term | Transliteration | Literal translation | Proposed normalized Toyota English | Source location | Parallel English terminology evidence | Scope | Proposal status | Language-fidelity status | Engineering-terminology status | Ambiguity references | Rationale | Reviewer roles needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `配線図集` | haisenzushū | collection of wiring diagrams | Electrical Wiring Diagram | Publication title; printed/PDF pending | Not yet cited | Publication title only | proposed | unreviewed | unreviewed | `TR-AMB-001` | Catalog uses a provisional normalized title; factory-style singular wording requires review. | Japanese language-fidelity; Toyota engineering terminology |
| `配線艤装図` | haisen gisōzu | wiring outfitting/layout diagram | Electrical Wiring Routing | Reviewed sample; exact location pending | Not yet cited | Chapter/page-type label only | unreviewed | unreviewed | unreviewed | `TR-AMB-001`, `TR-AMB-010` | Literal sense and Toyota page-type normalization must remain distinct. | Japanese language-fidelity; Toyota engineering terminology |
| `システム別配線図` | shisutemu-betsu haisenzu | wiring diagrams by system | System Circuits | Reviewed sample; exact location pending | Not yet cited | Chapter/page-type label only | unreviewed | unreviewed | unreviewed | `TR-AMB-001`, `TR-AMB-010` | Proposed wording must be checked against source role and parallel terminology. | Japanese language-fidelity; Toyota engineering terminology |
| `共通コネクター` | kyōtsū konekutā | common connector | Common Connector | Reviewed sample; exact location pending | Not yet cited | Publication-defined connector term only | unreviewed | unreviewed | unreviewed | `TR-AMB-005`, `TR-AMB-009` | A matching English label cannot establish connector identity across manuals. | Japanese language-fidelity; Toyota engineering terminology |
| `索引` | sakuin | index | Index | Reviewed index sample; exact page attachment pending | Not yet cited | Page/table heading only | proposed | unreviewed | unreviewed | — | Direct proposal remains subject to table-context review. | Japanese language-fidelity |
| `部品名` | buhinmei | part/component name | Component Name | Reviewed index sample; `2-6` or `5-2` attachment pending | Not yet cited | Table heading only | proposed | unreviewed | unreviewed | — | Table context must establish whether “part” or “component” is the better normalized wording. | Japanese language-fidelity; Toyota engineering terminology |
| `コネクター NO.` | konekutā nanbā | connector number | Connector No. | Reviewed index sample; exact attachment pending | Not yet cited | Table heading/identifier label only | proposed | unreviewed | unreviewed | `TR-AMB-009` | Preserve the source-local number separately from normalized punctuation. | Japanese language-fidelity; Toyota engineering terminology |
| `ウインドシールドワイパーリレー（リヤ用）` | uindoshīrudo waipā rirē (riya-yō) | windshield wiper relay (for rear) | Rear Windshield Wiper Relay | Reviewed sample; exact location pending | Not yet cited | Component label only | unreviewed | unreviewed | unreviewed | `TR-AMB-006`, `TR-AMB-009` | Parenthetical scope must remain visible; Toyota word order is unresolved. | Japanese language-fidelity; Toyota engineering terminology |
| `コンビネーションメーター` | konbinēshon mētā | combination meter | Combination Meter | Reviewed sample; exact location pending | Not yet cited | Component label only | proposed | unreviewed | unreviewed | `TR-AMB-009` | Loanword transcription is clear enough for a proposal; engineering usage needs evidence. | Japanese language-fidelity; Toyota engineering terminology |
| `コンビネーションスイッチ` | konbinēshon suicchi | combination switch | Combination Switch | Reviewed sample; exact location pending | Not yet cited | Component label only | proposed | unreviewed | unreviewed | `TR-AMB-009` | Preserve the source term while checking Toyota English usage. | Japanese language-fidelity; Toyota engineering terminology |
| `グロープラグリレー` | gurō puragu rirē | glow plug relay | Glow Plug Relay | Reviewed sample; exact location pending | Not yet cited | Component label only | proposed | unreviewed | unreviewed | `TR-AMB-009` | Proposed normalization is plausible but not yet evidenced here. | Japanese language-fidelity; Toyota engineering terminology |
| `ダイアグノーシスコネクター` | daiagunōshisu konekutā | diagnosis connector | Diagnosis Connector | Reviewed sample; exact location pending | Not yet cited | Component label only | unreviewed | unreviewed | unreviewed | `TR-AMB-009` | Toyota-specific loanword and normalized English require direct terminology evidence. | Japanese language-fidelity; Toyota engineering terminology |

Future entries should attach an ambiguity only when resolving it could
materially change that entry's transcription, literal translation, normalized
wording, scope, or disposition.
