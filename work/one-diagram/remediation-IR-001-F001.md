# IR-001-F001 Remediation Record

## Status

Remediation has been prepared for focused re-review. This record does not state
that `IR-001-F001` is closed, accepted, verified, or passed. It performs no
canonical acceptance and does not modify the authoritative IR-001 review
package.

## Finding and Root Cause

- Finding ID: `IR-001-F001`
- Earliest failed workflow layer: `candidate extraction`
- Root cause: the frozen extraction boundary included both heavy-duty headlight
  variants, but the detailed candidate extraction omitted the Europe
  arrangement and said that it had not been extracted.

## Prepared Remediation

The Europe arrangement was transcribed from EWD168F printed page 191, PDF page
186 (one-based; PDF index 185), locations `5-6` through `5-8`, including the
directly connected shared material at the left edge of `P191-R3` needed to
preserve the printed Europe arrangement. The transcription covers the visible
Headlight Relay, Dimmer Relay, D10 boundary object, Europe Fuse Block No. 1 and
four headlight fuses, H5, H6, C13, C15, J1, D2, conductors, terminal
designations, contact tables, geographic qualifiers, continuations, ground
identifiers, joins, and related-system boundary references.

The repository has no separate candidate-file index or identifier allocator.
New detailed identifiers follow the existing ledger convention: a candidate-
kind prefix, the `EU` variant token, a source-oriented suffix, and an unbroken
zero-padded sequence for conductor segments.

### New Candidate Identifiers

Summary-ledger identifiers:

- `OBJ-DIMMER-RELAY`
- `OBJ-D2`

Europe object identifiers:

- `OBJ-EU-HEAD-RELAY`
- `OBJ-EU-DIMMER-RELAY`
- `OBJ-EU-D10-REF`
- `OBJ-EU-FUSE-BLOCK-1`
- `OBJ-EU-FUSE-HEAD-LH-HI`
- `OBJ-EU-FUSE-HEAD-RH-HI`
- `OBJ-EU-FUSE-HEAD-LH-LO`
- `OBJ-EU-FUSE-HEAD-RH-LO`
- `OBJ-EU-H5`
- `OBJ-EU-H6`
- `OBJ-EU-C13-HIGH`
- `OBJ-EU-C15-LIGHT`
- `OBJ-EU-C15-DIMMER`
- `OBJ-EU-J1`
- `OBJ-EU-D2`

Europe terminal identifiers:

- `TERM-EU-HEAD-RELAY-1`, `TERM-EU-HEAD-RELAY-2`,
  `TERM-EU-HEAD-RELAY-3`, `TERM-EU-HEAD-RELAY-4`
- `TERM-EU-D10-1`, `TERM-EU-D10-2`
- `TERM-EU-DIMMER-1`, `TERM-EU-DIMMER-2`, `TERM-EU-DIMMER-3`,
  `TERM-EU-DIMMER-4`
- `TERM-EU-FB1-HI-1`, `TERM-EU-FB1-LO-1`
- `TERM-EU-FUSE-LH-HI-3`, `TERM-EU-FUSE-RH-HI-2`,
  `TERM-EU-FUSE-LH-LO-3`, `TERM-EU-FUSE-RH-LO-2`
- `TERM-EU-H5-1`, `TERM-EU-H5-2`, `TERM-EU-H5-3`, `TERM-EU-H6-1`,
  `TERM-EU-H6-2`, `TERM-EU-H6-3`
- `TERM-EU-C13-10`, `TERM-EU-C13-13`
- `TERM-EU-C15L-T11`, `TERM-EU-C15L-EL10`, `TERM-EU-C15L-H4`
- `TERM-EU-C15D-HF12`, `TERM-EU-C15D-HU5`, `TERM-EU-C15D-ED13`
- `TERM-EU-J1-A-LEFT`, `TERM-EU-J1-A-RIGHT`,
  `TERM-EU-J1-A-BOTTOM`, `TERM-EU-J1-B-TOP`,
  `TERM-EU-J1-B-BOTTOM`
- `TERM-EU-D2-13`, `TERM-EU-D2-14`, `TERM-EU-D2-6`,
  `TERM-EU-D2-4`, `TERM-EU-D2-5`, `TERM-EU-D2-2`, `TERM-EU-D2-3`,
  `TERM-EU-D2-10`, `TERM-EU-D2-11`, `TERM-EU-D2-12`,
  `TERM-EU-D2-1`, `TERM-EU-D2-8`, `TERM-EU-D2-7`

Europe conductor identifiers:

- `SEG-EU-001`, `SEG-EU-002`, `SEG-EU-003`, `SEG-EU-004`, `SEG-EU-005`,
  `SEG-EU-006`, `SEG-EU-007`, `SEG-EU-008`, `SEG-EU-009`, `SEG-EU-010`,
  `SEG-EU-011`
- `SEG-EU-012`, `SEG-EU-013`, `SEG-EU-014`, `SEG-EU-015`, `SEG-EU-016`,
  `SEG-EU-017`, `SEG-EU-018`, `SEG-EU-019`, `SEG-EU-020`, `SEG-EU-021`,
  `SEG-EU-022`
- `SEG-EU-023`, `SEG-EU-024`, `SEG-EU-025`, `SEG-EU-026`, `SEG-EU-027`,
  `SEG-EU-028`, `SEG-EU-029`, `SEG-EU-030`, `SEG-EU-031`, `SEG-EU-032`,
  `SEG-EU-033`
- `SEG-EU-034`, `SEG-EU-035`, `SEG-EU-036`, `SEG-EU-037`, `SEG-EU-038`,
  `SEG-EU-039`, `SEG-EU-040`, `SEG-EU-041`, `SEG-EU-042`, `SEG-EU-043`,
  `SEG-EU-044`

Europe junction identifiers:

- `JUNC-EU-B-4`
- `JUNC-EU-B-1`
- `JUNC-EU-RG-RELAY`
- `JUNC-EU-RG-C15`
- `JUNC-EU-RG-HLC`
- `JUNC-EU-RW`
- `JUNC-EU-RY`
- `JUNC-EU-FB-HI-1`
- `JUNC-EU-FB-LO-1`
- `JUNC-EU-RL-HI`
- `JUNC-EU-J1-A`
- `JUNC-EU-J1-B`
- `JUNC-EU-EA`
- `JUNC-EU-EB`
- `JUNC-EU-IE`
- `JUNC-EU-IF`

Europe continuation identifiers:

- `CONT-EU-B`
- `CONT-EU-REAR-FOG-HLC-RW`
- `CONT-EU-TAILLIGHT-C15`
- `CONT-EU-DAYTIME-C15`
- `CONT-EU-HEADLIGHT-CLEANER-RG`
- `CONT-EU-LIGHT-CONTROL`
- `CONT-EU-TAILLIGHT-D2`
- `CONT-EU-REAR-FOG-D2`
- `CONT-EU-DOME`
- `CONT-EU-ENGINE`
- `CONT-EU-CHARGE`
- `CONT-EU-CLOCK`
- `CONT-EU-EA`
- `CONT-EU-EB`
- `CONT-EU-IE`
- `CONT-EU-IF`

The switch-contact and fuse-table rows follow the existing ledger structure and
do not allocate separate row identifiers.

## Existing Candidates Changed

No existing Except-Europe candidate was changed. In particular, no existing
`OBJ-EX-*`, `TERM-EX-*`, `SEG-EX-*`, `JUNC-EX-*`, or `CONT-EX-*` row was
rewritten. The two non-candidate statements that described Europe as excluded
or unextracted were replaced because they contradicted the frozen boundary and
the prepared Europe candidate section. The summary object ledger gained the
two missing source-discovered objects listed above.

## Ambiguity Attachments

No attachment that predated the F001 remediation was removed or changed. No
new ambiguity was created.

New candidate attachments are:

- `AMB-CON-004`: `OBJ-EU-C15-LIGHT`, `OBJ-EU-C15-DIMMER`
- `AMB-CON-003`: `TERM-EU-J1-A-LEFT`, `TERM-EU-J1-A-RIGHT`,
  `TERM-EU-J1-A-BOTTOM`, `TERM-EU-J1-B-TOP`, `TERM-EU-J1-B-BOTTOM`,
  `SEG-EU-030`, `SEG-EU-031`, `SEG-EU-034`, `SEG-EU-035`,
  `SEG-EU-036`, `JUNC-EU-J1-A`, `JUNC-EU-J1-B`
- `AMB-CON-001`: `JUNC-EU-J1-A`, `JUNC-EU-J1-B`
- `AMB-DEP-001`: `SEG-EU-009`, `SEG-EU-012`,
  `CONT-EU-REAR-FOG-HLC-RW`,
  `CONT-EU-HEADLIGHT-CLEANER-RG`

The post-remediation attachment interaction check removed `AMB-DEP-001` from
the two corresponding unnumbered related-system-reference rows. Those rows
only copy the visible labels, destinations, source locations, and fixed
boundary treatment; resolving equipment applicability cannot change those
claims. The ambiguity remains open and attached to the four candidates whose
applicability or representation can change.

`AMB-APP-001` and `AMB-APP-002` remain open without attachment because no new
candidate asserts target-vehicle applicability. `AMB-DEP-002` remains open,
but the D2 candidates preserve the printed `(Iceland, Denmark)` object scope or
an explicit conductor qualifier rather than asserting broader Europe scope.
`AMB-GND-001` remains open without attachment to the neutral EA, EB, IE, and IF
transcriptions. `AMB-CON-002` remains open without attachment because no
selected crossing requires a choice between materially different
transcriptions.

## Post-remediation Ambiguity-Attachment Interaction Check

This check is limited to ambiguity attachments introduced by the F001 Europe
extraction. It does not remediate or alter the separate IR-001 findings, their
affected Except-Europe candidates, or the ambiguity log.

### `AMB-CON-004`

Unresolved question: how the separately named C15 Light Control SW and Dimmer
SW constructs should be distinguished without asserting unsupported internal
semantics. Primary evidence is page 191 `P191-R3`, which prints separate labels
and contact tables, while page 188 `SC188` shows both labels under code C15.
Page 5 supplies only the shared-connector naming convention.

| Candidate | Exact candidate claim | Material change if resolved | Decision and candidate-specific basis |
| --- | --- | --- | --- |
| `OBJ-EU-C15-LIGHT` | A separate candidate with exact label `LIGHT CONTROL SW [COMB. SW]`, code C15, and descriptive kind `source-labeled construct`. | Resolution could change whether this remains a separate construct candidate, is represented as a named aspect of one C15 object, or requires a different neutral descriptive kind. The exact source label and code would remain unchanged. | Retained. The attachment qualifies the candidate's construct boundary and representation, not any terminal, contact mark, conductor, or behavior. |
| `OBJ-EU-C15-DIMMER` | A separate candidate with exact label `DIMMER SW [COMB. SW]`, code C15, and descriptive kind `source-labeled construct`. | Resolution could change whether this remains a separate construct candidate, is represented as a named aspect of one C15 object, or requires a different neutral descriptive kind. The exact source label and code would remain unchanged. | Retained for the same candidate-specific representation reason. |

These attachments do not repeat `IR-001-F003`. That finding rejects
`AMB-CON-004` on direct contact-table and conductor transcriptions because the
ambiguity cannot change their printed states, endpoints, or wire colors. The
two Europe attachments instead qualify the narrow object/construct separation
that `IR-001-F002` expressly identifies as still affected by the unresolved C15
representation question. No Europe contact row, terminal candidate, or
conductor carries `AMB-CON-004`.

### `AMB-CON-003`

Unresolved question: which displayed J1 grouped-letter position corresponds to
each visible page-191 connection. Evidence for every attachment is the
candidate's visible position or endpoint on page 191 (`P191-R3` or `P191-R4`)
read jointly with the J1 connector view on page 189 (`SC189`) using page 6's
connector-view convention.

| Candidate | Exact candidate claim | Material change if resolved | Decision |
| --- | --- | --- | --- |
| `TERM-EU-J1-A-LEFT` | J1 `A (left displayed position)`, W-B. | The displayed-position mapping and therefore the terminal candidate's positional designation could change. | Retained. |
| `TERM-EU-J1-A-RIGHT` | J1 `A (right displayed position)`, W-B. | The displayed-position mapping and positional designation could change. | Retained. |
| `TERM-EU-J1-A-BOTTOM` | J1 `A (bottom displayed position)`, W-B. | The displayed-position mapping and positional designation could change. | Retained. |
| `TERM-EU-J1-B-TOP` | J1 `B (top displayed position)`, W-B. | The displayed-position mapping and positional designation could change. | Retained. |
| `TERM-EU-J1-B-BOTTOM` | J1 `B (bottom displayed position)`, W-B. | The displayed-position mapping and positional designation could change. | Retained. |
| `SEG-EU-030` | W-B segment from C13 terminal 13 to `TERM-EU-J1-B-TOP`. | The J1 endpoint could change if the top B-position correspondence changes. | Retained. |
| `SEG-EU-031` | W-B segment from `TERM-EU-J1-B-BOTTOM` to continuation IE. | The J1 endpoint could change if the bottom B-position correspondence changes. | Retained. |
| `SEG-EU-034` | W-B segment from C15 Light Control EL / 10 to `TERM-EU-J1-A-LEFT`. | The J1 endpoint could change if the left A-position correspondence changes. | Retained. |
| `SEG-EU-035` | W-B segment from C15 Dimmer ED / 13 to `TERM-EU-J1-A-RIGHT`. | The J1 endpoint could change if the right A-position correspondence changes. | Retained. |
| `SEG-EU-036` | W-B segment from `TERM-EU-J1-A-BOTTOM` to continuation IE. | The J1 endpoint could change if the bottom A-position correspondence changes. | Retained. |
| `JUNC-EU-J1-A` | Group A visibly connects the left, right, and bottom displayed A positions. | The membership list could change if any displayed A position is mapped differently. | Retained. |
| `JUNC-EU-J1-B` | Group B visibly connects the top and bottom displayed B positions. | The membership list could change if either displayed B position is mapped differently. | Retained. |

Each attachment is tied to a positional designation, segment endpoint, or
group-membership field. None is justified by J1 ownership, page proximity, or
circuit membership alone.

### `AMB-CON-001`

Unresolved question: what the displayed J1 grouped letters mean electrically
beyond their visible grouping. Primary evidence is the grouped J1 depiction on
page 191, with page 189 `SC189` supplying the J1 connector view and page 6 the
connector-view convention.

| Candidate | Exact candidate claim | Material change if resolved | Decision and candidate-specific basis |
| --- | --- | --- | --- |
| `JUNC-EU-J1-A` | A candidate junction/group claim that the three listed A positions form the displayed J1 group A. | Resolution could change whether this row may remain classified and interpreted as one junction group, or must be narrowed to a non-semantic record of the displayed A correspondence. | Retained. The attachment qualifies the grouped-junction assertion itself, not the three terminal rows merely because they belong to J1. |
| `JUNC-EU-J1-B` | A candidate junction/group claim that the two listed B positions form the displayed J1 group B. | Resolution could change whether this row may remain classified and interpreted as one junction group, or must be narrowed to a non-semantic record of the displayed B correspondence. | Retained for the same grouped-meaning reason. |

The attachment is not propagated to the J1 object, terminal candidates, or
segments. Those structural candidates carry `AMB-CON-003` only where their
positional mapping can change.

### `AMB-DEP-001`

Unresolved question: which equipment application uses the visible `From
Headlight Cleaner SW (5-1)` input and how that input should be represented while
the separate Headlight Cleaner system remains outside the boundary. Primary
evidence is page 191 `P191-R3`, which visibly prints the two Headlight Cleaner
references and their R-G and R-W conductors. Page 5 defines related-system
reference notation.

| Candidate | Exact candidate claim | Material change if resolved | Decision and boundary basis |
| --- | --- | --- | --- |
| `SEG-EU-009` | R-G segment from `CONT-EU-HEADLIGHT-CLEANER-RG` to `JUNC-EU-RG-HLC`, with reference `From Headlight Cleaner SW (5-1)` and applicability `equipment applicability unresolved`. | The applicability field could be narrowed to supported equipment scope, and the segment's treatment as an applicable boundary input could change. Its visible endpoints and R-G code would not change. | Retained. It records only the source-visible incoming reference and conductor needed at the headlight boundary. |
| `SEG-EU-012` | R-W segment from `CONT-EU-REAR-FOG-HLC-RW` to `JUNC-EU-RW`, preserving the printed Rear Fog Light and Headlight Cleaner references with equipment applicability unresolved. | Resolution could change the Headlight Cleaner portion of the applicability and whether the combined input must be split or conditionally represented; the visible R-W transcription and Rear Fog Light reference would remain. | Retained. |
| `CONT-EU-REAR-FOG-HLC-RW` | One visible R-W input carrying the printed labels `From Rear Fog Light SW (2-8)` and `From Headlight Cleaner SW (5-1)`. | Resolution could require the continuation candidate to distinguish conditional equipment scope or separate the Headlight Cleaner reference from the shared visible input representation. | Retained. |
| `CONT-EU-HEADLIGHT-CLEANER-RG` | Exact label `From Headlight Cleaner SW (5-1)`, R-G, with context `equipment applicability unresolved`. | Resolution could change the explicit context/applicability and boundary-reference representation. | Retained. |

All four retained candidates stop at the visible headlight-boundary input. They
contain no Headlight Cleaner component, terminal, internal conductor, contact,
behavior, or target-vehicle applicability claim. They do not import location
`5-1` or widen the frozen page-191 headlight boundary.

Two additional `AMB-DEP-001` attachments were examined and removed:

| Examined row | Claim | Why attachment was removed |
| --- | --- | --- |
| Related-system row `From Rear Fog Light SW (2-8); From Headlight Cleaner SW (5-1)` | The visible labels enter the selected Europe arrangement and the referenced systems are not imported. | Resolving equipment applicability cannot change the printed labels, their source locations, or the frozen decision not to import those systems. |
| Related-system row `From Headlight Cleaner SW (5-1)` | The visible R-G reference enters at the D2 terminal-5 path and Headlight Cleaner is not imported. | Resolution cannot change that direct source transcription or the fixed boundary treatment. Applicability uncertainty remains on the identified segment and continuation candidates instead. |

### Interaction-check result

- Attachment instances examined: 22.
- Retained: 20 candidate-specific attachments.
- Removed: 2 `AMB-DEP-001` attachments from unnumbered duplicate
  related-system rows.
- No new `AMB-CON-004` instance repeats the direct structural over-attachment
  described by `IR-001-F003`.
- No Headlight Cleaner candidate exceeds boundary-reference scope.
- No pre-existing attachment or IR-001 record was changed.

## Validation

- `python3 -m unittest discover -s tests -v`: 43 tests passed.
- `python3 scripts/check-independent-review work/independent-review/IR-001`:
  package valid.
- `git diff --check`: passed.
- Markdown table-width check over the ledger and this record: passed.
- Europe candidate-row attachment count: 2 `AMB-CON-004`, 12
  `AMB-CON-003`, 2 `AMB-CON-001`, and 4 `AMB-DEP-001`, matching the 20
  retained attachment instances documented above.
- Existing Except-Europe candidate-row comparison against `HEAD`: no changes.
- `work/independent-review/IR-001` diff check: no changes.

## Files Changed

- `work/one-diagram/headlight-extraction-ledger.md`
- `work/one-diagram/source-language-review-checklist.md`
- `work/one-diagram/README.md`
- `work/one-diagram/remediation-IR-001-F001.md`

The checklist's authorization boundary was corrected from Except-Europe only
to the already frozen complete headlight boundary at locations `5-4` through
`5-8`. This records that the existing checked hard preconditions govern the
complete boundary used for the remediation; it does not change a source
definition, extraction boundary, or evidence conclusion.

## Exclusions Preserved

Headlight Cleaner remains outside the boundary as a separate system; only its
printed inputs are retained as boundary references under `AMB-DEP-001`. Winch,
Back-Up Light, light-duty headlight circuits, beam-level control, body-routing
pages 104–105, service part numbers, and inferred operating behavior or current
flow were not extracted. Other page-191 systems did not enter the boundary by
page proximity.

## Unresolved Human Judgment

- whether the Europe or Except-Europe circuit applies to the identified target
  vehicle (`AMB-APP-001`);
- whether the August 1992 publication applies to the identified 1990 vehicle
  (`AMB-APP-002`);
- Headlight Cleaner equipment applicability and boundary treatment
  (`AMB-DEP-001`);
- the claim-level scope of D2 material beyond qualifiers explicitly printed by
  the source (`AMB-DEP-002`);
- broader J1 grouped-letter meaning and positional correspondence
  (`AMB-CON-001`, `AMB-CON-003`);
- future representation of the two printed C15 functions (`AMB-CON-004`); and
- mapping of EA, EB, IE, and IF beyond their neutral page-191 transcriptions
  (`AMB-GND-001`).

These matters remain unresolved and are not decisions made by this
remediation.

## Focused Re-review Scope

1. Repeat source-to-candidate review over the complete headlight boundary at
   EWD168F printed page 191, locations `5-4` through `5-8`.
2. Perform candidate-to-source review for every new or changed candidate and
   every new or changed ambiguity attachment listed in this record.

The prepared remediation must be frozen in a new committed candidate revision
before that re-review begins. This record does not perform the freeze, re-review,
reviewer verification, finding resolution, or canonical acceptance.
