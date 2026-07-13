# EWD168F Headlight Candidate Extraction Ledger

## Status

Pre-canonical working ledger for **One Diagram**. Every entry remains a candidate until checked against preserved evidence, assigned provenance and applicability, and independently reviewed.

## Extraction unit

- Publication: EWD168F
- Primary circuit page: 191
- Group: Heavy-Duty System Circuits 5
- Variants:
  - Headlight (Except Europe), index location 5-4
  - Headlight (Europe), index location 5-6

## Detailed Transcription Precondition

EWD168F pages 4–7 are mandatory boundary-review material. Page 191 may not be
interpreted without reviewing those definitions, but each candidate cites only
the source-language guidance materially required to read it, as recorded in
[source-language.md](source-language.md).

The previous detailed extraction commit was reverted during the policy task.
Detailed transcription may proceed only when the
[hard gate](extraction-boundary.md#hard-gate) passes. Open soft ambiguities must
be cited on affected entries; soft status does not authorize interpretation,
completion, or silent resolution. Authorization is recorded in the
[source-language review checklist](source-language-review-checklist.md).

## Candidate object ledger

| Candidate ID | Source label | Code | Candidate kind | Evidence | State |
| --- | --- | --- | --- | --- | --- |
| OBJ-H5 | Headlight LH | H5 | part/load | pp. 188, 191; pp. 84–85 location | discovered |
| OBJ-H6 | Headlight RH | H6 | part/load | pp. 188, 191; pp. 84–85 location | discovered |
| OBJ-C15-LIGHT | Light Control SW [Comb. SW] | C15 | switch function within part | pp. 188, 191 | discovered |
| OBJ-C15-DIMMER | Dimmer SW [Comb. SW] | C15 | switch function within part | pp. 188, 191 | discovered |
| OBJ-C13-HIGH | High Beam Indicator Light [Comb. Meter] | C13 | indicator function within part | pp. 188, 191 | discovered |
| OBJ-J1 | Junction Connector No. 1 | J1 | junction connector | pp. 189, 191; pp. 100–101 location | discovered |
| OBJ-J3 | Junction Connector No. 3 | J3 | junction connector | pp. 189, 191; pp. 100–101 location | discovered |
| OBJ-HEAD-RELAY | Headlight Relay | — | relay | pp. 29, 191 | discovered |
| OBJ-FUSE-BLOCK-1 | Fuse Block No. 1 | — | assembly | pp. 29–31, 191 | discovered |

## Candidate connector observations

| Candidate | Observation | Evidence | State |
| --- | --- | --- | --- |
| H5 | three displayed cavities numbered 1, 2, 3 | p. 188 | discovered |
| H6 | three displayed cavities numbered 1, 2, 3 | p. 188 | discovered |
| H5 | location references 5-4 and 5-7 | p. 188 | discovered |
| H6 | location references 5-4 and 5-8 | p. 188 | discovered |
| C15 | connector color Black | p. 188 | discovered |
| C13 | connector color Blue | p. 188 | discovered |
| J1 | connector color Orange | p. 189 | discovered |
| J3 | connector color Blue | p. 189 | discovered |

## Candidate fuse observations

### Europe

Page 30 visibly identifies four 10 A positions:

- HEAD (LH-LWR)
- HEAD (RH-LWR)
- HEAD (LH-UPR)
- HEAD (RH-UPR)

Their precise circuit relationships must be transcribed from page 191 rather than inferred from labels.

### Except Europe

Page 31 visibly identifies:

- HEAD (LH), 10 A
- HEAD (RH), 10 A

Their precise circuit relationships must be transcribed from page 191.

## Candidate location observations

| Candidate | Source statement | Evidence | State |
| --- | --- | --- | --- |
| H5 | shown in RHD 1PZ engine-compartment view | pp. 84–85 | discovered |
| H6 | shown in RHD 1PZ engine-compartment view | pp. 84–85 | discovered |
| C13 | Combination Meter in RHD instrument-panel table | pp. 100–101 | discovered |
| C15 | Combination SW in RHD instrument-panel table | pp. 100–101 | discovered |
| J1 | Junction Connector No. 1 in RHD instrument-panel table | pp. 100–101 | discovered |
| J3 | Junction Connector No. 3 in RHD instrument-panel table | pp. 100–101 | discovered |
| Headlight Relay | position shown in Relay Block No. 1 | p. 29 | discovered |

## Source-language concepts earned so far

These candidate modeling needs are forced by the reviewed source:

1. Publication
2. Evidence location
3. Applicability statement
4. Part
5. Function within a part
6. Connector
7. Terminal or cavity
8. Junction connector
9. Fuse
10. Relay
11. Conductor segment
12. Internal connection or switch-contact state
13. Ground reference
14. Related-system continuation
15. Physical-location claim
16. Variant

## Concepts not yet earned

- universal automotive ontology
- service part numbers
- replacement compatibility
- diagnostic symptom rules
- current/voltage simulation
- failure-impact edges
- canonical `feeds`, `powers`, or `controls` relationships
- renderer coordinates
- database-specific node/edge structures

## Open extraction questions

1. Does the target vehicle use Europe or Except-Europe headlights?
2. What are the exact wire-color codes on each segment?
3. Which J1 and J3 grouped-letter positions correspond to the visible page-191 circuit connections? H5, H6, C15, and C13 terminal numbers are now legible in the working captures.
4. How should C15's separately named Light Control and Dimmer functions be represented?
5. What exactly do J1's and J3's grouped letters mean electrically?
6. Do the candidate continuation identifiers transcribe as BH and BI for Except Europe and EA, EB, IE, and IF for Europe, and how do they map to the relevant ground or continuation pages?
7. Which crossings are joins, crossovers, or continuations?
8. For which equipment application does the visible `From Headlight Cleaner SW (5-1)` input apply, and how should that referenced input be represented?
9. Which claims involving the visible D2 Daytime Running Light Relay are Iceland/Denmark-specific, and which Europe-circuit claims are common to other markets?
10. Which facts are common to both variants and which are variant-specific?

## Page-191 transcription passes

### Pass 1 — Regions

Assign provisional region IDs:

- `P191-R1`: Except-Europe fuse and headlamp area
- `P191-R2`: Except-Europe switching/junction area
- `P191-R3`: Europe switching/junction area
- `P191-R4`: Europe fuse, headlamp, and indicator area
- `P191-R5`: lower grounds and continuation references

### Pass 2 — Visible objects

List every labeled component, fuse, relay, switch function, connector, junction, indicator, ground, and continuation marker.

### Pass 3 — Connection points

Record every terminal, cavity, contact, and junction group before recording conductors.

### Pass 4 — Conductors

Trace each uninterrupted segment between meaningful endpoints and preserve Toyota's printed wire-color code exactly.

### Pass 5 — Applicability

Assign each candidate to:

- common heavy-duty headlight context
- Headlight (Except Europe)
- Headlight (Europe)
- unresolved/shared context

### Pass 6 — Review

Check every entry against the preserved source region. Preserve illegibility and ambiguity instead of resolving them from electrical intuition.

## Page-191 evidence status

Overlapping high-resolution working captures covering the five proposed regions
have been reviewed and are adequate for candidate conductor-level transcription.
They are not currently repository evidence assets, and their relationship to the
user's physical source still needs to be recorded. Any transcription from these
captures remains a candidate until checked against adequately identified
evidence, assigned provenance and applicability, and independently reviewed.

## Except-Europe Detailed Candidate Transcription

This transcription is limited to EWD168F printed page 191, PDF page 186
(one-based; PDF index 185), **Headlight (Except Europe)** beginning at location
`5-4`. It copies source-visible candidates and does not assert applicability to
the identified target vehicle or acceptance as factory knowledge.

Citation shorthand used below:

- `P191`: EWD168F printed page 191, PDF page 186, location `5-4`.
- `SL4`: printed page 4, example System Circuit.
- `SL5`: printed page 5, System Circuit notation definitions.
- `SL6`: printed page 6, System Circuit Connectors explanation.
- `SL7`: printed page 7, abbreviations and terminal-code distinction.
- `RB29`: printed page 29, Relay Block No. 1 layout support.
- `SC189`: printed page 189, J1 and J3 connector-detail support.

The tables use `—` where no material interpretive dependency, supporting
evidence, or candidate-specific ambiguity is attached. Ambiguity IDs are listed
explicitly rather than propagated through category shorthand.

### 1. Visible Objects

| Candidate ID | Exact Toyota label | Printed source code | Source location | Descriptive kind | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-EX-HEAD-RELAY | HEADLIGHT RELAY | — | `P191-R1`, `5-4` | relay | Headlight (Except Europe) | `P191` | — | `RB29` (Relay Block No. 1 layout) | — | candidate |
| OBJ-EX-FUSE-BLOCK-1 | FUSE BLOCK NO. 1 | — | `P191-R1`, `5-4` | fuse block | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-FUSE-HEAD-LH | 10A HEAD LH | — | `P191-R1`, `5-4` | fuse | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-FUSE-HEAD-RH | 10A HEAD RH | — | `P191-R1`, `5-4` | fuse | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-H5 | HEADLIGHT | H5 | `P191-R1`, `5-4` | part | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-H6 | HEADLIGHT | H6 | `P191-R1`, `5-4` | part | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-J3 | JUNCTION CONNECTOR NO. 3 | J3 | `P191-R2`, `5-4` | junction connector | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-C15-LIGHT | LIGHT CONTROL SW [COMB. SW] | C15 | `P191-R2`, `5-4` | printed switch function within part | Headlight (Except Europe) | `P191` | `SL5` (shared connector naming) | — | `AMB-CON-004` | candidate |
| OBJ-EX-C15-DIMMER | DIMMER SW [COMB. SW] | C15 | `P191-R2`, `5-4` | printed switch function within part | Headlight (Except Europe) | `P191` | `SL5` (shared connector naming) | — | `AMB-CON-004` | candidate |
| OBJ-EX-C13-HIGH | HIGH BEAM INDICATOR LIGHT [COMB. METER] | C13 | `P191-R2`, `5-4` | printed indicator function within part | Headlight (Except Europe) | `P191` | `SL5` (shared connector naming) | — | — | candidate |
| OBJ-EX-J1 | JUNCTION CONNECTOR NO. 1 | J1 | `P191-R2`, `5-4` | junction connector | Headlight (Except Europe) | `P191` | — | — | — | candidate |
| OBJ-EX-D10 | DIODE (for Rear Fog Light) | D10 | `P191-R2`, `5-4` | part | Headlight (Except Europe), boundary treatment unresolved | `P191` | — | — | `AMB-BOUND-001` | candidate |

Page 191 prints `LH` separately with H5 and `RH` separately with H6; these are
preserved as printed qualifiers rather than folded into the exact `HEADLIGHT`
label.

### 2. Terminals and Contacts

Repeated J1 and J3 letters are recorded by their displayed page-191 positions;
no broader grouped-letter meaning is assigned.

| Candidate terminal ID | Owning object | Exact printed designation | Source location | Attached printed wire-color code | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TERM-EX-RELAY-1 | OBJ-EX-HEAD-RELAY | 1 | `P191-R1` | R | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-RELAY-2 | OBJ-EX-HEAD-RELAY | 2 | `P191-R1` | R-G | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-RELAY-3 | OBJ-EX-HEAD-RELAY | 3 | `P191-R1` | R-W | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-RELAY-4 | OBJ-EX-HEAD-RELAY | 4 | `P191-R1` | R | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-FB1-1 | OBJ-EX-FUSE-BLOCK-1 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-FB1-2 | OBJ-EX-FUSE-BLOCK-1 | 2 | `P191-R1` | R-B | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-FB1-3 | OBJ-EX-FUSE-BLOCK-1 | 3 | `P191-R1` | R-L | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H5-1 | OBJ-EX-H5 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H5-2 | OBJ-EX-H5 | 2 | `P191-R1` | R-Y | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H5-3 | OBJ-EX-H5 | 3 | `P191-R1` | R-L | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H6-1 | OBJ-EX-H6 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H6-2 | OBJ-EX-H6 | 2 | `P191-R1` | R-Y | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-H6-3 | OBJ-EX-H6 | 3 | `P191-R1` | R-B | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-J3-H-TOP | OBJ-EX-J3 | H (top displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J3-H-RIGHT | OBJ-EX-J3 | H (right displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J3-H-BOTTOM | OBJ-EX-J3 | H (bottom displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J3-G-TOP | OBJ-EX-J3 | G (top displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J3-G-RIGHT | OBJ-EX-J3 | G (right displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J3-G-BOTTOM | OBJ-EX-J3 | G (bottom displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-C15L-T11 | OBJ-EX-C15-LIGHT | T / 11 | `P191-R2` | LG-R | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-C15L-EL10 | OBJ-EX-C15-LIGHT | EL / 10 | `P191-R2` | W-B | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-C15L-H4 | OBJ-EX-C15-LIGHT | H / 4 | `P191-R2` | R-W; R-B | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-D10-1 | OBJ-EX-D10 | 1 | `P191-R2` | R-W | `P191` | `SL5` (wire color and pin number) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-D10-2 | OBJ-EX-D10 | 2 | `P191-R2` | R-B | `P191` | `SL5` (wire color and pin number) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-D10-3 | OBJ-EX-D10 | 3 | `P191-R2` | R-L | `P191` | `SL5` (wire color and pin number) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-C15D-HF12 | OBJ-EX-C15-DIMMER | HF / 12 | `P191-R2` | R-W | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-C15D-HL6 | OBJ-EX-C15-DIMMER | HL / 6 | `P191-R2` | R-G | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-C15D-HU5 | OBJ-EX-C15-DIMMER | HU / 5 | `P191-R2` | R-Y | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-C15D-ED13 | OBJ-EX-C15-DIMMER | ED / 13 | `P191-R2` | W-B | `P191` | `SL5` (wire color and pin number); `SL7` (terminal code) | — | `AMB-CON-004` | candidate |
| TERM-EX-J1-A-LEFT | OBJ-EX-J1 | A (left displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J1-A-RIGHT | OBJ-EX-J1 | A (right displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J1-A-BOTTOM | OBJ-EX-J1 | A (bottom displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J1-B-TOP | OBJ-EX-J1 | B (top displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-J1-B-BOTTOM | OBJ-EX-J1 | B (bottom displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | candidate |
| TERM-EX-C13-10 | OBJ-EX-C13-HIGH | 10 | `P191-R2` | R-G | `P191` | `SL5` (wire color and pin number) | — | — | candidate |
| TERM-EX-C13-13 | OBJ-EX-C13-HIGH | 13 | `P191-R2` | W-B | `P191` | `SL5` (wire color and pin number) | — | — | candidate |

### 3. Conductor Segments

`CONT-EX-B`, `CONT-EX-REAR-FOG`, `CONT-EX-TAILLIGHT`, `CONT-EX-BH`, and
`CONT-EX-BI` are the continuation candidates recorded in section 8. Junction
IDs are defined in section 7.

| Candidate segment ID | Endpoint A | Endpoint B | Printed wire-color code | Branches | Continuation references | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEG-EX-001 | CONT-EX-B | TERM-EX-RELAY-4 | R | JUNC-EX-B-4 | B | Headlight (Except Europe) | `P191`, `P191-R1` | `SL5` (wire color) | — | — | high |
| SEG-EX-002 | CONT-EX-B | TERM-EX-RELAY-1 | R | JUNC-EX-B-1 | B | Headlight (Except Europe) | `P191`, `P191-R1` | `SL5` (wire color) | — | — | high |
| SEG-EX-003 | TERM-EX-RELAY-2 | TERM-EX-FB1-1 | R-G | JUNC-EX-FB1-1 | — | Headlight (Except Europe) | `P191`, `P191-R1` | `SL5` (wire color) | — | — | high |
| SEG-EX-004 | TERM-EX-FB1-3 | TERM-EX-H5-3 | R-L | — | — | Headlight (Except Europe) | `P191`, `P191-R1` | `SL5` (wire color) | — | — | high |
| SEG-EX-005 | TERM-EX-FB1-2 | TERM-EX-H6-3 | R-B | — | — | Headlight (Except Europe) | `P191`, `P191-R1` | `SL5` (wire color) | — | — | high |
| SEG-EX-006 | TERM-EX-H5-1 | TERM-EX-J3-H-TOP | R-G | JUNC-EX-J3-H | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-007 | TERM-EX-H6-1 | TERM-EX-J3-H-RIGHT | R-G | JUNC-EX-J3-H | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-008 | TERM-EX-J3-H-BOTTOM | JUNC-EX-RG | R-G | JUNC-EX-J3-H; JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-009 | JUNC-EX-RG | TERM-EX-C15D-HL6 | R-G | JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | `AMB-CON-004` | high |
| SEG-EX-010 | JUNC-EX-RG | TERM-EX-C13-10 | R-G | JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color) | — | — | high |
| SEG-EX-011 | TERM-EX-H5-2 | TERM-EX-J3-G-TOP | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-012 | TERM-EX-H6-2 | TERM-EX-J3-G-RIGHT | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-013 | TERM-EX-J3-G-BOTTOM | TERM-EX-C15D-HU5 | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-001`; `AMB-CON-003`; `AMB-CON-004` | high |
| SEG-EX-014 | TERM-EX-RELAY-3 | JUNC-EX-RW-UPPER | R-W | JUNC-EX-RW-UPPER | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color) | — | — | high |
| SEG-EX-015 | JUNC-EX-RW-UPPER | TERM-EX-D10-1 | R-W | JUNC-EX-RW-UPPER | — | Headlight (Except Europe), boundary treatment unresolved | `P191`, `P191-R2` | `SL5` (wire color) | — | `AMB-BOUND-001` | high |
| SEG-EX-016 | JUNC-EX-RW-UPPER | TERM-EX-C15L-H4 | R-W | JUNC-EX-RW-UPPER; JUNC-EX-C15-H4 | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | `AMB-CON-004` | high |
| SEG-EX-017 | TERM-EX-D10-2 | TERM-EX-C15L-H4 | R-B | JUNC-EX-C15-H4 | — | Headlight (Except Europe), boundary treatment unresolved | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | `AMB-BOUND-001`; `AMB-CON-004` | high |
| SEG-EX-018 | CONT-EX-REAR-FOG | TERM-EX-D10-3 | R-L | — | From Rear Fog Light SW (2-8) | boundary reference; Except-Europe circuit | `P191`, `P191-R2` | `SL5` (wire color and related-system notation) | — | `AMB-BOUND-001` | high |
| SEG-EX-019 | TERM-EX-C15L-H4 | TERM-EX-C15D-HF12 | R-W | JUNC-EX-C15-H4 | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL7` (terminal code) | — | `AMB-CON-004` | high |
| SEG-EX-020 | CONT-EX-TAILLIGHT | TERM-EX-C15L-T11 | LG-R | — | From Taillight Relay (4-1) | boundary reference; Except-Europe circuit | `P191`, `P191-R2` | `SL5` (wire color and related-system notation); `SL7` (terminal code) | — | `AMB-BOUND-001`; `AMB-CON-004` | high |
| SEG-EX-021 | TERM-EX-C15L-EL10 | TERM-EX-J1-A-LEFT | W-B | JUNC-EX-J1-A | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-001`; `AMB-CON-003`; `AMB-CON-004` | high |
| SEG-EX-022 | TERM-EX-C15D-ED13 | TERM-EX-J1-A-RIGHT | W-B | JUNC-EX-J1-A | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-001`; `AMB-CON-003`; `AMB-CON-004` | high |
| SEG-EX-023 | TERM-EX-J1-A-BOTTOM | JUNC-EX-WB-LHD | W-B | JUNC-EX-J1-A; JUNC-EX-WB-LHD | — | Headlight (Except Europe) | `P191`, `P191-R2`–`R5` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-024 | JUNC-EX-WB-LHD | CONT-EX-BH | W-B | JUNC-EX-WB-LHD | BH | Headlight (Except Europe), LHD | `P191`, `P191-R5` | `SL5` (wire color and ground-point notation); `SL7` (LHD) | — | `AMB-GND-001` | high |
| SEG-EX-025 | JUNC-EX-WB-LHD | JUNC-EX-WB-RHD | W-B | JUNC-EX-WB-LHD; JUNC-EX-WB-RHD | — | Headlight (Except Europe) | `P191`, `P191-R5` | `SL5` (wire color) | — | — | high |
| SEG-EX-026 | JUNC-EX-WB-RHD | CONT-EX-BI | W-B | JUNC-EX-WB-RHD | BI | Headlight (Except Europe), RHD | `P191`, `P191-R5` | `SL5` (wire color and ground-point notation); `SL7` (RHD) | — | `AMB-GND-001` | high |
| SEG-EX-027 | JUNC-EX-WB-RHD | TERM-EX-J1-B-BOTTOM | W-B | JUNC-EX-WB-RHD; JUNC-EX-J1-B | — | Headlight (Except Europe) | `P191`, `P191-R2`–`R5` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |
| SEG-EX-028 | TERM-EX-J1-B-TOP | TERM-EX-C13-13 | W-B | JUNC-EX-J1-B | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` | high |

### 4. Switch Contacts

These tables copy the marks printed by Toyota. A dash joins terminals shown in
continuity; `none depicted` means the source row contains no continuity mark.
No operating behavior is assigned.

| Function name | Printed terminals | Switch position | Depicted continuity | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | OFF | none depicted | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | TAIL | T—EL | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | HEAD | T—EL—H | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |
| DIMMER SW [COMB. SW] | HF, HL, HU, ED | FLASH | HF—HU—ED | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |
| DIMMER SW [COMB. SW] | HF, HL, HU, ED | LOW | HL—ED | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |
| DIMMER SW [COMB. SW] | HF, HL, HU, ED | HIGH | HU—ED | `P191`, `P191-R2` | `SL7` (terminal-code distinction) | — | `AMB-CON-004` |

### 5. Relay

| Candidate | Printed terminals | Coil terminals | Contact terminals | Depicted normal contact state | Relay Block reference | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-EX-HEAD-RELAY | 1, 2, 3, 4 | 4—3 | 1—2 | open | circled `1`; Relay Block No. 1 | `P191`, `P191-R1` | `SL5` (Relay Block notation) | `RB29` (Relay Block No. 1 layout) | — |

The Relay Block reference is recorded separately from connector and junction
identifiers. No energized state, polarity, or current direction is asserted.

### 6. Fuse Table

| Printed label | Printed rating | Endpoint A | Endpoint B | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HEAD LH | 10A | TERM-EX-FB1-1 | TERM-EX-FB1-3 | Headlight (Except Europe) | `P191`, `P191-R1` | — | — | — |
| HEAD RH | 10A | TERM-EX-FB1-1 | TERM-EX-FB1-2 | Headlight (Except Europe) | `P191`, `P191-R1` | — | — | — |

### 7. Junctions

J1 and J3 grouped letters are copied as displayed. The other rows record
source-visible black-dot joins; they do not add a derived electrical role.

| Candidate junction ID | Printed object or displayed group | Visible connections | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- |
| JUNC-EX-B-4 | B line, branch at relay terminal 4 conductor | CONT-EX-B; TERM-EX-RELAY-4 | `P191`, `P191-R1` | `SL4` (black-dot join depiction) | — | — |
| JUNC-EX-B-1 | B line, branch at relay terminal 1 conductor | CONT-EX-B; TERM-EX-RELAY-1 | `P191`, `P191-R1` | `SL4` (black-dot join depiction) | — | — |
| JUNC-EX-FB1-1 | Fuse Block No. 1 terminal 1 common printed line | TERM-EX-RELAY-2; both printed fuse terminal-1 sides | `P191`, `P191-R1` | — | — | — |
| JUNC-EX-J3-H | J3 grouped letter H | TERM-EX-J3-H-TOP; TERM-EX-J3-H-RIGHT; TERM-EX-J3-H-BOTTOM | `P191`, `P191-R2` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |
| JUNC-EX-J3-G | J3 grouped letter G | TERM-EX-J3-G-TOP; TERM-EX-J3-G-RIGHT; TERM-EX-J3-G-BOTTOM | `P191`, `P191-R2` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |
| JUNC-EX-RG | black-dot join on R-G conductors | SEG-EX-008; SEG-EX-009; SEG-EX-010 | `P191`, `P191-R2` | `SL4` (black-dot join depiction) | — | — |
| JUNC-EX-RW-UPPER | black-dot join on R-W conductors | SEG-EX-014; SEG-EX-015; SEG-EX-016 | `P191`, `P191-R2` | `SL4` (black-dot join depiction) | — | `AMB-BOUND-001` |
| JUNC-EX-C15-H4 | black-dot join at C15 H / 4 | SEG-EX-016; SEG-EX-017; SEG-EX-019 | `P191`, `P191-R2` | `SL4` (black-dot join depiction); `SL7` (terminal code) | — | `AMB-BOUND-001`; `AMB-CON-004` |
| JUNC-EX-J1-A | J1 grouped letter A | TERM-EX-J1-A-LEFT; TERM-EX-J1-A-RIGHT; TERM-EX-J1-A-BOTTOM | `P191`, `P191-R2` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |
| JUNC-EX-WB-LHD | black-dot join on W-B (LHD) conductors | SEG-EX-023; SEG-EX-024; SEG-EX-025 | `P191`, `P191-R5` | `SL4` (black-dot join depiction); `SL7` (LHD) | — | — |
| JUNC-EX-WB-RHD | black-dot join on W-B (RHD) conductors | SEG-EX-025; SEG-EX-026; SEG-EX-027 | `P191`, `P191-R5` | `SL4` (black-dot join depiction); `SL7` (RHD) | — | — |
| JUNC-EX-J1-B | J1 grouped letter B | TERM-EX-J1-B-BOTTOM; TERM-EX-J1-B-TOP | `P191`, `P191-R2` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |

### 8. Continuations

| Candidate continuation ID | Exact printed identifier or label | Attached printed wire-color code | Source location | Source-described context | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONT-EX-B | B | R at the two selected branches | `P191-R1`, top common line | page-spanning printed line identified `B` | `P191` | `SL5` (wire color) | — | — | candidate |
| CONT-EX-REAR-FOG | From Rear Fog Light SW (2-8) | R-L | `P191-R2` | related-system reference | `P191` | `SL5` (wire color and related-system notation) | — | `AMB-BOUND-001` | candidate |
| CONT-EX-TAILLIGHT | From Taillight Relay (4-1) | LG-R | `P191-R2` | related-system reference | `P191` | `SL5` (wire color and related-system notation) | — | `AMB-BOUND-001` | candidate |
| CONT-EX-BH | BH | W-B (LHD) | `P191-R5` | printed ground-point identifier; legend: `Located on lower back panel inner` | `P191` | `SL5` (wire color and ground-point notation); `SL7` (LHD) | — | `AMB-GND-001` | candidate |
| CONT-EX-BI | BI | W-B (RHD) | `P191-R5` | printed ground-point identifier; legend: `Located on cross member frame` | `P191` | `SL5` (wire color and ground-point notation); `SL7` (RHD) | — | `AMB-GND-001` | candidate |

BH and BI remain open for confirmation and mapping to the relevant ground-point
pages under `AMB-GND-001`.

### 9. Related-System References

| Printed label | Destination | Source location | Reason retained | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| From Rear Fog Light SW (2-8) | location `2-8` | `P191-R2`, attached to D10 terminal 3 by R-L | visible reference leaving the selected boundary; referenced system is not imported | `P191` | `SL5` (related-system notation) | — | `AMB-BOUND-001` |
| From Taillight Relay (4-1) | location `4-1` | `P191-R2`, attached to C15 T / 11 by LG-R | visible reference leaving the selected boundary; referenced system is not imported | `P191` | `SL5` (related-system notation) | — | `AMB-BOUND-001` |

Headlight Cleaner, Winch, Back-Up Light, and the Europe headlight circuit are
not extracted here.

### 10. Extraction Summary

| Candidate category | Count |
| --- | ---: |
| objects | 12 |
| terminals | 36 |
| conductors | 28 |
| relays | 1 |
| fuses | 2 |
| junctions | 12 |
| continuations | 5 |
| related-system references | 2 |
| attached ambiguity IDs | 5 |

The five attached ambiguities are `AMB-GND-001`, `AMB-CON-001`,
`AMB-CON-003`, `AMB-CON-004`, and `AMB-BOUND-001`. `AMB-APP-001` and
`AMB-APP-002` remain open for target-vehicle selection but do not attach to
neutral Except-Europe source candidates that make no target-vehicle claim.
`AMB-CON-002` remains open in the ambiguity log but does not attach to any
selected candidate because the source-visible crossings, joins, branches, and
continuations can be transcribed faithfully. `AMB-DEP-001` and `AMB-DEP-002`
concern only the excluded Europe circuit.

Review confirmed that each attached ambiguity passed the candidate-specific
attachment test and each interpretive dependency materially supports how its
candidate is read. Page 191 remains the primary evidence for the circuit claims;
no source-language page is cited as though it directly contains those claims.
No candidate confidence changed. The transcription continues to add no current
flow, switching polarity, diagnostic, failure-mode, or target-vehicle claim.
