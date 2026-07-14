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
| OBJ-DIMMER-RELAY | Dimmer Relay | — | source-labeled object | p. 191 | discovered |
| OBJ-D2 | Daytime Running Light Relay (Iceland, Denmark) | D2 | source-labeled object | p. 191 | discovered |
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
| TERM-EX-RELAY-1 | OBJ-EX-HEAD-RELAY | 1 | `P191-R1` | R | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-RELAY-2 | OBJ-EX-HEAD-RELAY | 2 | `P191-R1` | R-G | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-RELAY-3 | OBJ-EX-HEAD-RELAY | 3 | `P191-R1` | R-W | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-RELAY-4 | OBJ-EX-HEAD-RELAY | 4 | `P191-R1` | R | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-FB1-1 | OBJ-EX-FUSE-BLOCK-1 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-FB1-2 | OBJ-EX-FUSE-BLOCK-1 | 2 | `P191-R1` | R-B | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-FB1-3 | OBJ-EX-FUSE-BLOCK-1 | 3 | `P191-R1` | R-L | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H5-1 | OBJ-EX-H5 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H5-2 | OBJ-EX-H5 | 2 | `P191-R1` | R-Y | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H5-3 | OBJ-EX-H5 | 3 | `P191-R1` | R-L | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H6-1 | OBJ-EX-H6 | 1 | `P191-R1` | R-G | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H6-2 | OBJ-EX-H6 | 2 | `P191-R1` | R-Y | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-H6-3 | OBJ-EX-H6 | 3 | `P191-R1` | R-B | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-J3-H-TOP | OBJ-EX-J3 | H (top displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J3-H-RIGHT | OBJ-EX-J3 | H (right displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J3-H-BOTTOM | OBJ-EX-J3 | H (bottom displayed position) | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J3-G-TOP | OBJ-EX-J3 | G (top displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J3-G-RIGHT | OBJ-EX-J3 | G (right displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J3-G-BOTTOM | OBJ-EX-J3 | G (bottom displayed position) | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-C15L-T11 | OBJ-EX-C15-LIGHT | T / 11 | `P191-R2` | LG-R | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-C15L-EL10 | OBJ-EX-C15-LIGHT | EL / 10 | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-C15L-H4 | OBJ-EX-C15-LIGHT | H / 4 | `P191-R2` | R-W; R-B | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-D10-1 | OBJ-EX-D10 | 1 | `P191-R2` | R-W | `P191` | `SL5` (wire color) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-D10-2 | OBJ-EX-D10 | 2 | `P191-R2` | R-B | `P191` | `SL5` (wire color) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-D10-3 | OBJ-EX-D10 | 3 | `P191-R2` | R-L | `P191` | `SL5` (wire color) | — | `AMB-BOUND-001` | candidate |
| TERM-EX-C15D-HF12 | OBJ-EX-C15-DIMMER | HF / 12 | `P191-R2` | R-W | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-C15D-HL6 | OBJ-EX-C15-DIMMER | HL / 6 | `P191-R2` | R-G | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-C15D-HU5 | OBJ-EX-C15-DIMMER | HU / 5 | `P191-R2` | R-Y | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-C15D-ED13 | OBJ-EX-C15-DIMMER | ED / 13 | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL7` (terminal code) | — | — | candidate |
| TERM-EX-J1-A-LEFT | OBJ-EX-J1 | A (left displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J1-A-RIGHT | OBJ-EX-J1 | A (right displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J1-A-BOTTOM | OBJ-EX-J1 | A (bottom displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J1-B-TOP | OBJ-EX-J1 | B (top displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-J1-B-BOTTOM | OBJ-EX-J1 | B (bottom displayed position) | `P191-R2` | W-B | `P191` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EX-C13-10 | OBJ-EX-C13-HIGH | 10 | `P191-R2` | R-G | `P191` | `SL5` (wire color) | — | — | candidate |
| TERM-EX-C13-13 | OBJ-EX-C13-HIGH | 13 | `P191-R2` | W-B | `P191` | `SL5` (wire color) | — | — | candidate |

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
| SEG-EX-006 | TERM-EX-H5-1 | TERM-EX-J3-H-TOP | R-G | JUNC-EX-J3-H | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-007 | TERM-EX-H6-1 | TERM-EX-J3-H-RIGHT | R-G | JUNC-EX-J3-H | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-008 | TERM-EX-J3-H-BOTTOM | JUNC-EX-RG | R-G | JUNC-EX-J3-H; JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-009 | JUNC-EX-RG | TERM-EX-C15D-HL6 | R-G | JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | — | high |
| SEG-EX-010 | JUNC-EX-RG | TERM-EX-C13-10 | R-G | JUNC-EX-RG | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color) | — | — | high |
| SEG-EX-011 | TERM-EX-H5-2 | TERM-EX-J3-G-TOP | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-012 | TERM-EX-H6-2 | TERM-EX-J3-G-RIGHT | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-013 | TERM-EX-J3-G-BOTTOM | TERM-EX-C15D-HU5 | R-Y | JUNC-EX-J3-G | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-014 | TERM-EX-RELAY-3 | JUNC-EX-RW-UPPER | R-W | JUNC-EX-RW-UPPER | — | Headlight (Except Europe) | `P191`, `P191-R1`–`R2` | `SL5` (wire color) | — | — | high |
| SEG-EX-015 | JUNC-EX-RW-UPPER | TERM-EX-D10-1 | R-W | JUNC-EX-RW-UPPER | — | Headlight (Except Europe), boundary treatment unresolved | `P191`, `P191-R2` | `SL5` (wire color) | — | `AMB-BOUND-001` | high |
| SEG-EX-016 | JUNC-EX-RW-UPPER | TERM-EX-C15L-H4 | R-W | JUNC-EX-RW-UPPER; JUNC-EX-C15-H4 | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | — | high |
| SEG-EX-017 | TERM-EX-D10-2 | TERM-EX-C15L-H4 | R-B | JUNC-EX-C15-H4 | — | Headlight (Except Europe), boundary treatment unresolved | `P191`, `P191-R2` | `SL5` (wire color); `SL7` (terminal code) | — | `AMB-BOUND-001` | high |
| SEG-EX-018 | CONT-EX-REAR-FOG | TERM-EX-D10-3 | R-L | — | From Rear Fog Light SW (2-8) | boundary reference; Except-Europe circuit | `P191`, `P191-R2` | `SL5` (wire color and related-system notation) | — | `AMB-BOUND-001` | high |
| SEG-EX-019 | TERM-EX-C15L-H4 | TERM-EX-C15D-HF12 | R-W | JUNC-EX-C15-H4 | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL7` (terminal code) | — | `AMB-CON-004` | high |
| SEG-EX-020 | CONT-EX-TAILLIGHT | TERM-EX-C15L-T11 | LG-R | — | From Taillight Relay (4-1) | boundary reference; Except-Europe circuit | `P191`, `P191-R2` | `SL5` (wire color and related-system notation); `SL7` (terminal code) | — | `AMB-BOUND-001` | high |
| SEG-EX-021 | TERM-EX-C15L-EL10 | TERM-EX-J1-A-LEFT | W-B | JUNC-EX-J1-A | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-022 | TERM-EX-C15D-ED13 | TERM-EX-J1-A-RIGHT | W-B | JUNC-EX-J1-A | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color and shared connector); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-023 | TERM-EX-J1-A-BOTTOM | JUNC-EX-WB-LHD | W-B | JUNC-EX-J1-A; JUNC-EX-WB-LHD | — | Headlight (Except Europe) | `P191`, `P191-R2`–`R5` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-024 | JUNC-EX-WB-LHD | CONT-EX-BH | W-B | JUNC-EX-WB-LHD | BH | Headlight (Except Europe), LHD | `P191`, `P191-R5` | `SL5` (wire color and ground-point notation); `SL7` (LHD) | — | `AMB-GND-001` | high |
| SEG-EX-025 | JUNC-EX-WB-LHD | JUNC-EX-WB-RHD | W-B | JUNC-EX-WB-LHD; JUNC-EX-WB-RHD | — | Headlight (Except Europe) | `P191`, `P191-R5` | `SL5` (wire color) | — | — | high |
| SEG-EX-026 | JUNC-EX-WB-RHD | CONT-EX-BI | W-B | JUNC-EX-WB-RHD | BI | Headlight (Except Europe), RHD | `P191`, `P191-R5` | `SL5` (wire color and ground-point notation); `SL7` (RHD) | — | `AMB-GND-001` | high |
| SEG-EX-027 | JUNC-EX-WB-RHD | TERM-EX-J1-B-BOTTOM | W-B | JUNC-EX-WB-RHD; JUNC-EX-J1-B | — | Headlight (Except Europe) | `P191`, `P191-R2`–`R5` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EX-028 | TERM-EX-J1-B-TOP | TERM-EX-C13-13 | W-B | JUNC-EX-J1-B | — | Headlight (Except Europe) | `P191`, `P191-R2` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |

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
| JUNC-EX-C15-H4 | black-dot join at C15 H / 4 | SEG-EX-016; SEG-EX-017; SEG-EX-019 | `P191`, `P191-R2` | `SL4` (black-dot join depiction); `SL7` (terminal code) | — | `AMB-BOUND-001` |
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

Headlight Cleaner, Winch, and Back-Up Light are not extracted as separate
systems. The Europe headlight circuit is transcribed separately below.

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
are evaluated in the Europe detailed extraction below.

Review confirmed that each attached ambiguity passed the candidate-specific
attachment test. `AMB-CON-001` attaches only to the four candidates that assert
grouped J1/J3 junction semantics. `AMB-CON-003` remains on displayed J1/J3
terminal positions, conductors whose endpoints use those positions, and the
grouped-junction candidates because resolving positional correspondence could
change their mappings, endpoints, or visible connections. `AMB-CON-004` attaches
only to the two C15 function objects, the six function-specific switch-table
rows, and `SEG-EX-019`, which explicitly relates terminals assigned to the two
distinct printed functions.

Each interpretive dependency materially supports how its candidate is read;
page 5 supplies wire-color interpretation but is not cited as pin-number
guidance for ordinary component terminals. Page 191 remains the primary
evidence for the circuit claims, and no source-language page is cited as though
it directly contains those claims. No candidate confidence changed. The
transcription continues to add no current flow, switching polarity, diagnostic,
failure-mode, or target-vehicle claim.

## Europe Detailed Candidate Transcription

This transcription is limited to EWD168F printed page 191, PDF page 186
(one-based; PDF index 185), **Headlight (Europe)** at locations `5-6` through
`5-8`, including the directly connected shared material needed to preserve the
printed arrangement. It copies source-visible candidates and does not assert
applicability to the identified target vehicle or acceptance as factory
knowledge.

Candidate identifiers follow the ledger's existing kind-and-variant convention:
`EU` distinguishes Europe candidates from the existing `EX` candidates, and
conductor identifiers use an unbroken zero-padded sequence. The repository has
no separate candidate identifier allocator or candidate-file index.

Citation shorthand used below:

- `P191-EU`: EWD168F printed page 191, PDF page 186, locations `5-6` through
  `5-8` and the directly connected left-boundary material in `P191-R3`.
- `SL4`: printed page 4, example System Circuit.
- `SL5`: printed page 5, System Circuit notation definitions.
- `SL6`: printed page 6, System Circuit Connectors explanation.
- `SL7`: printed page 7, abbreviations and terminal-code distinction.
- `RB29`: printed page 29, Relay Block No. 1 layout support.
- `FB30`: printed page 30, Europe Fuse Block No. 1 layout support.
- `SC188`: printed page 188, C13, C15, H5, and H6 connector-detail support.
- `SC189`: printed page 189, J1 connector-detail support.

The tables use `—` where no material interpretive dependency, supporting
evidence, or candidate-specific ambiguity is attached. Market qualifiers are
copied only on the candidates beside which they are printed or whose endpoint
is the explicitly qualified D2 object.

### 1. Visible Objects

| Candidate ID | Exact Toyota label | Printed source code | Source location | Descriptive kind | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-EU-HEAD-RELAY | HEADLIGHT RELAY | — | `P191-R3` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `RB29` (Relay Block No. 1 layout) | — | candidate |
| OBJ-EU-DIMMER-RELAY | DIMMER RELAY | — | `P191-R3` | source-labeled object | Headlight (Europe) | `P191-EU` | — | — | — | candidate |
| OBJ-EU-D10-REF | DIODE (For Rear Fog Light) | D10 | `P191-R3`, left boundary | source-labeled boundary object | Headlight (Europe); adjacent path marked `Ex. Iceland, Denmark` | `P191-EU` | — | — | — | candidate |
| OBJ-EU-FUSE-BLOCK-1 | FUSE BLOCK NO. 1 | — | `P191-R4`, `5-7`–`5-8` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `FB30` | — | candidate |
| OBJ-EU-FUSE-HEAD-LH-HI | 10A HEAD LH-HI | — | `P191-R4`, `5-7` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `FB30` | — | candidate |
| OBJ-EU-FUSE-HEAD-RH-HI | 10A HEAD RH-HI | — | `P191-R4`, `5-7` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `FB30` | — | candidate |
| OBJ-EU-FUSE-HEAD-LH-LO | 10A HEAD LH-LO | — | `P191-R4`, `5-8` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `FB30` | — | candidate |
| OBJ-EU-FUSE-HEAD-RH-LO | 10A HEAD RH-LO | — | `P191-R4`, `5-8` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `FB30` | — | candidate |
| OBJ-EU-H5 | HEADLIGHT | H5 | `P191-R4`, `5-7` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `SC188` | — | candidate |
| OBJ-EU-H6 | HEADLIGHT | H6 | `P191-R4`, `5-8` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `SC188` | — | candidate |
| OBJ-EU-C13-HIGH | HIGH BEAM INDICATOR LIGHT [COMB. METER] | C13 | `P191-R4`, `5-8` | source-labeled construct | Headlight (Europe) | `P191-EU` | `SL5` (shared connector naming) | `SC188` | — | candidate |
| OBJ-EU-C15-LIGHT | LIGHT CONTROL SW [COMB. SW] | C15 | `P191-R3`, `5-6` | source-labeled construct | Headlight (Europe) | `P191-EU` | `SL5` (shared connector naming) | `SC188` | `AMB-CON-004` | candidate |
| OBJ-EU-C15-DIMMER | DIMMER SW [COMB. SW] | C15 | `P191-R3`, `5-6` | source-labeled construct | Headlight (Europe) | `P191-EU` | `SL5` (shared connector naming) | `SC188` | `AMB-CON-004` | candidate |
| OBJ-EU-J1 | JUNCTION CONNECTOR NO. 1 | J1 | `P191-R3` and `P191-R4` | source-labeled object | Headlight (Europe) | `P191-EU` | — | `SC189` | — | candidate |
| OBJ-EU-D2 | DAYTIME RUNNING LIGHT RELAY (Iceland, Denmark) | D2 | `P191-R3`, `5-7` | source-labeled object | Headlight (Europe), Iceland and Denmark | `P191-EU` | — | — | — | candidate |

Page 191 prints `LH` separately with H5 and `RH` separately with H6; those
qualifiers are preserved separately from the exact `HEADLIGHT` label.

### 2. Terminals and Contacts

Repeated J1 letters are recorded by their displayed page-191 positions; no
broader grouped-letter meaning is assigned. D2 terminal candidates are scoped
to the source-labeled Iceland-and-Denmark object without extending that scope
to adjacent Europe claims.

| Candidate terminal ID | Owning object | Exact printed designation | Source location | Attached printed wire-color code | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TERM-EU-HEAD-RELAY-1 | OBJ-EU-HEAD-RELAY | 1 | `P191-R3` | R | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-HEAD-RELAY-2 | OBJ-EU-HEAD-RELAY | 2 | `P191-R3` | R-B | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-HEAD-RELAY-3 | OBJ-EU-HEAD-RELAY | 3 | `P191-R3` | R-G | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-HEAD-RELAY-4 | OBJ-EU-HEAD-RELAY | 4 | `P191-R3` | R | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D10-1 | OBJ-EU-D10-REF | 1 | `P191-R3` | R-G | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D10-2 | OBJ-EU-D10-REF | 2 | `P191-R3` | R-W | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-DIMMER-1 | OBJ-EU-DIMMER-RELAY | 1 | `P191-R3` | R-B | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-DIMMER-2 | OBJ-EU-DIMMER-RELAY | 2 | `P191-R3` | R-L | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-DIMMER-3 | OBJ-EU-DIMMER-RELAY | 3 | `P191-R3` | R-W | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-DIMMER-4 | OBJ-EU-DIMMER-RELAY | 4 | `P191-R3` | R-Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-FB1-HI-1 | OBJ-EU-FUSE-BLOCK-1 | 1 (HI pair) | `P191-R4` | R-L | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-FB1-LO-1 | OBJ-EU-FUSE-BLOCK-1 | 1 (LO pair) | `P191-R4` | R-W | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-FUSE-LH-HI-3 | OBJ-EU-FUSE-HEAD-LH-HI | 3 | `P191-R4` | R-Y | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-FUSE-RH-HI-2 | OBJ-EU-FUSE-HEAD-RH-HI | 2 | `P191-R4` | R-L | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-FUSE-LH-LO-3 | OBJ-EU-FUSE-HEAD-LH-LO | 3 | `P191-R4` | R-B | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-FUSE-RH-LO-2 | OBJ-EU-FUSE-HEAD-RH-LO | 2 | `P191-R4` | R-G | `P191-EU` | `SL5` (wire color) | `FB30` | — | candidate |
| TERM-EU-H5-1 | OBJ-EU-H5 | 1 | `P191-R4` | R-B | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-H5-2 | OBJ-EU-H5 | 2 | `P191-R4` | R-Y | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-H5-3 | OBJ-EU-H5 | 3 | `P191-R4` | W-B | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-H6-1 | OBJ-EU-H6 | 1 | `P191-R4` | R-G | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-H6-2 | OBJ-EU-H6 | 2 | `P191-R4` | R-L | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-H6-3 | OBJ-EU-H6 | 3 | `P191-R4` | W-B | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-C13-10 | OBJ-EU-C13-HIGH | 10 | `P191-R4` | R-L | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-C13-13 | OBJ-EU-C13-HIGH | 13 | `P191-R4` | W-B | `P191-EU` | `SL5` (wire color) | `SC188` | — | candidate |
| TERM-EU-C15L-T11 | OBJ-EU-C15-LIGHT | T / 11 | `P191-R3` | G-Y (Iceland, Denmark); LG-R (Ex. Iceland, Denmark) | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-C15L-EL10 | OBJ-EU-C15-LIGHT | EL / 10 | `P191-R3` | W-B | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-C15L-H4 | OBJ-EU-C15-LIGHT | H / 4 | `P191-R3` | R-W | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-C15D-HF12 | OBJ-EU-C15-DIMMER | HF / 12 | `P191-R3` | R-G | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-C15D-HU5 | OBJ-EU-C15-DIMMER | HU / 5 | `P191-R3` | R-Y; Y (Iceland, Denmark) | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-C15D-ED13 | OBJ-EU-C15-DIMMER | ED / 13 | `P191-R3` | W-B | `P191-EU` | `SL5` (wire color); `SL7` (terminal code) | `SC188` | — | candidate |
| TERM-EU-J1-A-LEFT | OBJ-EU-J1 | A (left displayed position) | `P191-R3` | W-B | `P191-EU` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EU-J1-A-RIGHT | OBJ-EU-J1 | A (right displayed position) | `P191-R3` | W-B | `P191-EU` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EU-J1-A-BOTTOM | OBJ-EU-J1 | A (bottom displayed position) | `P191-R3` | W-B | `P191-EU` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EU-J1-B-TOP | OBJ-EU-J1 | B (top displayed position) | `P191-R4` | W-B | `P191-EU` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EU-J1-B-BOTTOM | OBJ-EU-J1 | B (bottom displayed position) | `P191-R4` | W-B | `P191-EU` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | candidate |
| TERM-EU-D2-13 | OBJ-EU-D2 | 13 | `P191-R3` | Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-14 | OBJ-EU-D2 | 14 | `P191-R3` | R-Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-6 | OBJ-EU-D2 | 6 | `P191-R3` | R-G | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-4 | OBJ-EU-D2 | 4 | `P191-R3` | R-W | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-5 | OBJ-EU-D2 | 5 | `P191-R3` | R-G | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-2 | OBJ-EU-D2 | 2 | `P191-R3` | G-Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-3 | OBJ-EU-D2 | 3 | `P191-R3` | LG-R | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-10 | OBJ-EU-D2 | 10 | `P191-R3` | BR | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-11 | OBJ-EU-D2 | 11 | `P191-R3` | R-L | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-12 | OBJ-EU-D2 | 12 | `P191-R3` | R | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-1 | OBJ-EU-D2 | 1 | `P191-R3` | B-Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-8 | OBJ-EU-D2 | 8 | `P191-R3` | Y | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| TERM-EU-D2-7 | OBJ-EU-D2 | 7 | `P191-R3` | G | `P191-EU` | `SL5` (wire color) | — | — | candidate |

The `HL` column is present in the printed Europe Dimmer SW table, but page 191
does not display a terminal number or external conductor at that column. It is
therefore preserved in the contact rows below without inventing a terminal
candidate.

### 3. Conductor Segments

Continuation candidates are defined in section 8 and junction candidates in
section 7. A market qualifier is not inherited by a neighboring segment.

| Candidate segment ID | Endpoint A | Endpoint B | Printed wire-color code | Branches | Continuation references | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEG-EU-001 | CONT-EU-B | TERM-EU-HEAD-RELAY-4 | R | JUNC-EU-B-4 | B | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-002 | CONT-EU-B | TERM-EU-HEAD-RELAY-1 | R | JUNC-EU-B-1 | B | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-003 | TERM-EU-HEAD-RELAY-3 | JUNC-EU-RG-RELAY | R-G | JUNC-EU-RG-RELAY | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-004 | JUNC-EU-RG-RELAY | TERM-EU-D10-1 | R-G | JUNC-EU-RG-RELAY | — | Headlight (Europe), Ex. Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-005 | JUNC-EU-RG-RELAY | JUNC-EU-RG-C15 | R-G | JUNC-EU-RG-RELAY; JUNC-EU-RG-C15 | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-006 | JUNC-EU-RG-C15 | TERM-EU-C15D-HF12 | R-G | JUNC-EU-RG-C15 | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color); `SL7` (terminal code) | — | — | high |
| SEG-EU-007 | JUNC-EU-RG-C15 | TERM-EU-D2-6 | R-G | JUNC-EU-RG-C15 | — | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-008 | JUNC-EU-RG-C15 | JUNC-EU-RG-HLC | R-G | JUNC-EU-RG-C15; JUNC-EU-RG-HLC | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-009 | CONT-EU-HEADLIGHT-CLEANER-RG | JUNC-EU-RG-HLC | R-G | JUNC-EU-RG-HLC | From Headlight Cleaner SW (5-1) | Headlight (Europe); equipment applicability unresolved | `P191-EU`, `P191-R3` | `SL5` (wire color, related-system, and variation notation) | — | `AMB-DEP-001` | high |
| SEG-EU-010 | JUNC-EU-RG-HLC | TERM-EU-D2-5 | R-G | JUNC-EU-RG-HLC | — | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-011 | TERM-EU-HEAD-RELAY-2 | TERM-EU-DIMMER-1 | R-B | — | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-012 | CONT-EU-REAR-FOG-HLC-RW | JUNC-EU-RW | R-W | JUNC-EU-RW | From Rear Fog Light SW (2-8); From Headlight Cleaner SW (5-1) | Headlight (Europe); equipment applicability unresolved | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | `AMB-DEP-001` | high |
| SEG-EU-013 | TERM-EU-D10-2 | JUNC-EU-RW | R-W | JUNC-EU-RW | — | Headlight (Europe), Ex. Iceland and Denmark path | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-014 | JUNC-EU-RW | TERM-EU-C15L-H4 | R-W | JUNC-EU-RW | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color); `SL7` (terminal code) | — | — | high |
| SEG-EU-015 | JUNC-EU-RW | TERM-EU-D2-4 | R-W | JUNC-EU-RW | — | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-016 | TERM-EU-DIMMER-3 | TERM-EU-FB1-LO-1 | R-W | JUNC-EU-FB-LO-1 | — | Headlight (Europe) | `P191-EU`, `P191-R3`–`R4` | `SL5` (wire color) | `FB30` | — | high |
| SEG-EU-017 | TERM-EU-DIMMER-2 | TERM-EU-FB1-HI-1 | R-L | JUNC-EU-FB-HI-1 | — | Headlight (Europe) | `P191-EU`, `P191-R3`–`R4` | `SL5` (wire color) | `FB30` | — | high |
| SEG-EU-018 | TERM-EU-DIMMER-4 | JUNC-EU-RY | R-Y | JUNC-EU-RY | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color) | — | — | high |
| SEG-EU-019 | JUNC-EU-RY | TERM-EU-C15D-HU5 | R-Y | JUNC-EU-RY | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color); `SL7` (terminal code) | — | — | high |
| SEG-EU-020 | JUNC-EU-RY | TERM-EU-D2-14 | R-Y | JUNC-EU-RY | — | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation) | — | — | high |
| SEG-EU-021 | TERM-EU-C15D-HU5 | TERM-EU-D2-13 | Y | — | — | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and variation notation); `SL7` (terminal code) | — | — | high |
| SEG-EU-022 | TERM-EU-FUSE-LH-HI-3 | TERM-EU-H5-2 | R-Y | — | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `FB30`; `SC188` | — | high |
| SEG-EU-023 | TERM-EU-FUSE-RH-HI-2 | JUNC-EU-RL-HI | R-L | JUNC-EU-RL-HI | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `FB30` | — | high |
| SEG-EU-024 | JUNC-EU-RL-HI | TERM-EU-H6-2 | R-L | JUNC-EU-RL-HI | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `SC188` | — | high |
| SEG-EU-025 | JUNC-EU-RL-HI | TERM-EU-C13-10 | R-L | JUNC-EU-RL-HI | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `SC188` | — | high |
| SEG-EU-026 | TERM-EU-FUSE-LH-LO-3 | TERM-EU-H5-1 | R-B | — | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `FB30`; `SC188` | — | high |
| SEG-EU-027 | TERM-EU-FUSE-RH-LO-2 | TERM-EU-H6-1 | R-G | — | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color) | `FB30`; `SC188` | — | high |
| SEG-EU-028 | TERM-EU-H5-3 | CONT-EU-EB | W-B | JUNC-EU-EB | EB | Headlight (Europe) | `P191-EU`, `P191-R4`–`R5` | `SL5` (wire color and ground-point notation) | `SC188` | — | high |
| SEG-EU-029 | TERM-EU-H6-3 | CONT-EU-EA | W-B | JUNC-EU-EA | EA | Headlight (Europe) | `P191-EU`, `P191-R4`–`R5` | `SL5` (wire color and ground-point notation) | `SC188` | — | high |
| SEG-EU-030 | TERM-EU-C13-13 | TERM-EU-J1-B-TOP | W-B | JUNC-EU-J1-B | — | Headlight (Europe) | `P191-EU`, `P191-R4` | `SL5` (wire color); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EU-031 | TERM-EU-J1-B-BOTTOM | CONT-EU-IE | W-B | JUNC-EU-J1-B; JUNC-EU-IE | IE | Headlight (Europe) | `P191-EU`, `P191-R4`–`R5` | `SL5` (wire color and ground-point notation); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EU-032 | CONT-EU-TAILLIGHT-C15 | TERM-EU-C15L-T11 | LG-R | — | From Taillight Relay (Ex. Iceland, Denmark) (4-1) | Headlight (Europe), Ex. Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color, related-system, and variation notation); `SL7` (terminal code) | — | — | high |
| SEG-EU-033 | CONT-EU-DAYTIME-C15 | TERM-EU-C15L-T11 | G-Y | — | From Daytime Running Light Relay (5-7) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color, related-system, and variation notation); `SL7` (terminal code) | — | — | high |
| SEG-EU-034 | TERM-EU-C15L-EL10 | TERM-EU-J1-A-LEFT | W-B | JUNC-EU-J1-A | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-003` | high |
| SEG-EU-035 | TERM-EU-C15D-ED13 | TERM-EU-J1-A-RIGHT | W-B | JUNC-EU-J1-A | — | Headlight (Europe) | `P191-EU`, `P191-R3` | `SL5` (wire color); `SL6` (connector-view convention); `SL7` (terminal code) | `SC189` | `AMB-CON-003` | high |
| SEG-EU-036 | TERM-EU-J1-A-BOTTOM | CONT-EU-IE | W-B | JUNC-EU-J1-A; JUNC-EU-IE | IE | Headlight (Europe) | `P191-EU`, `P191-R3`–`R5` | `SL5` (wire color and ground-point notation); `SL6` (connector-view convention) | `SC189` | `AMB-CON-003` | high |
| SEG-EU-037 | TERM-EU-D2-2 | CONT-EU-LIGHT-CONTROL | G-Y | — | To Light Control SW (5-6) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-038 | CONT-EU-TAILLIGHT-D2 | TERM-EU-D2-3 | LG-R | — | From Taillight Relay (4-1) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-039 | TERM-EU-D2-10 | CONT-EU-IF | BR | JUNC-EU-IF | IF | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3`–`R5` | `SL5` (wire color and ground-point notation) | — | — | high |
| SEG-EU-040 | CONT-EU-REAR-FOG-D2 | TERM-EU-D2-11 | R-L | — | From Rear Fog Light SW (2-8) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-041 | CONT-EU-DOME | TERM-EU-D2-12 | R | — | From "DOME" Fuse (8-2) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-042 | CONT-EU-ENGINE | TERM-EU-D2-1 | B-Y | — | From "ENGINE" Fuse (2-1) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-043 | TERM-EU-D2-8 | CONT-EU-CHARGE | Y | — | To "CHARGE" Fuse (2-2) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |
| SEG-EU-044 | TERM-EU-D2-7 | CONT-EU-CLOCK | G | — | To Clock (9-1) | Headlight (Europe), Iceland and Denmark | `P191-EU`, `P191-R3` | `SL5` (wire color and related-system notation) | — | — | high |

### 4. Switch Contacts

These rows copy the marks printed by Toyota. A dash joins terminals shown in
continuity; `none depicted` means the source row contains no continuity mark.
They do not assert operating behavior. `AMB-CON-004` remains on the two
function-object candidates and is not propagated to these direct table
transcriptions.

| Function name | Printed terminals | Switch position | Depicted continuity | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | OFF | none depicted | `P191-EU`, `P191-R3` | `SL7` (terminal-code distinction) | — | — |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | TAIL | T—EL | `P191-EU`, `P191-R3` | `SL7` (terminal-code distinction) | — | — |
| LIGHT CONTROL SW [COMB. SW] | T, EL, H | HEAD | T—EL—H | `P191-EU`, `P191-R3` | `SL7` (terminal-code distinction) | — | — |
| DIMMER SW [COMB. SW] | HF, HL, HU, ED | FLASH | HF—HU—ED | `P191-EU`, `P191-R3` | `SL7` (terminal-code distinction) | — | — |
| DIMMER SW [COMB. SW] | HF, HL, HU, ED | HIGH | HU—ED | `P191-EU`, `P191-R3` | `SL7` (terminal-code distinction) | — | — |

### 5. Relay Depictions

| Candidate | Printed terminals | Coil terminals | Contact depiction | Relay Block reference | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-EU-HEAD-RELAY | 1, 2, 3, 4 | 4—3 | contact between 1 and 2 depicted open | circled `1`; Relay Block No. 1 | `P191-EU`, `P191-R3` | `SL5` (Relay Block notation) | `RB29` | — |
| OBJ-EU-DIMMER-RELAY | 1, 2, 3, 4 | 1—3 | printed movable-contact line and separate terminal-2 and terminal-4 marks | circled `1`; Relay Block No. 1 | `P191-EU`, `P191-R3` | `SL5` (Relay Block notation) | — | — |

The Dimmer Relay row deliberately records only the visible marks. It does not
assign an energized state, switching sequence, polarity, or current direction.
D2 is preserved as a source-labeled object with visible terminals; page 191
does not expose internal contacts for transcription.

### 6. Fuse Table

| Printed label | Printed rating | Endpoint A | Endpoint B | Applicability | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HEAD LH-HI | 10A | TERM-EU-FB1-HI-1 | TERM-EU-FUSE-LH-HI-3 | Headlight (Europe) | `P191-EU`, `P191-R4` | — | `FB30` | — |
| HEAD RH-HI | 10A | TERM-EU-FB1-HI-1 | TERM-EU-FUSE-RH-HI-2 | Headlight (Europe) | `P191-EU`, `P191-R4` | — | `FB30` | — |
| HEAD LH-LO | 10A | TERM-EU-FB1-LO-1 | TERM-EU-FUSE-LH-LO-3 | Headlight (Europe) | `P191-EU`, `P191-R4` | — | `FB30` | — |
| HEAD RH-LO | 10A | TERM-EU-FB1-LO-1 | TERM-EU-FUSE-RH-LO-2 | Headlight (Europe) | `P191-EU`, `P191-R4` | — | `FB30` | — |

### 7. Junctions

J1 grouped letters are copied as displayed. The remaining rows record visible
black-dot joins or common printed fuse lines without assigning a derived role.

| Candidate junction ID | Printed object or displayed group | Visible connections | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- |
| JUNC-EU-B-4 | B line, branch at Headlight Relay terminal 4 conductor | CONT-EU-B; TERM-EU-HEAD-RELAY-4 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction) | — | — |
| JUNC-EU-B-1 | B line, branch at Headlight Relay terminal 1 conductor | CONT-EU-B; TERM-EU-HEAD-RELAY-1 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction) | — | — |
| JUNC-EU-RG-RELAY | black-dot join at Headlight Relay terminal 3 path | SEG-EU-003; SEG-EU-004; SEG-EU-005 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction); `SL5` (wire color) | — | — |
| JUNC-EU-RG-C15 | black-dot join on R-G conductors | SEG-EU-005; SEG-EU-006; SEG-EU-007; SEG-EU-008 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction); `SL5` (wire color) | — | — |
| JUNC-EU-RG-HLC | black-dot join at the Headlight Cleaner reference | SEG-EU-008; SEG-EU-009; SEG-EU-010 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction); `SL5` (wire color) | — | — |
| JUNC-EU-RW | black-dot join on R-W conductors | SEG-EU-012; SEG-EU-013; SEG-EU-014; SEG-EU-015 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction); `SL5` (wire color) | — | — |
| JUNC-EU-RY | black-dot join at C15 HU / 5 path | SEG-EU-018; SEG-EU-019; SEG-EU-020 | `P191-EU`, `P191-R3` | `SL4` (black-dot join depiction); `SL5` (wire color); `SL7` (terminal code) | — | — |
| JUNC-EU-FB-HI-1 | Fuse Block No. 1 terminal 1 common printed HI line | TERM-EU-DIMMER-2; both printed HI fuse terminal-1 sides | `P191-EU`, `P191-R4` | — | `FB30` | — |
| JUNC-EU-FB-LO-1 | Fuse Block No. 1 terminal 1 common printed LO line | TERM-EU-DIMMER-3; both printed LO fuse terminal-1 sides | `P191-EU`, `P191-R4` | — | `FB30` | — |
| JUNC-EU-RL-HI | black-dot join on RH-HI R-L conductor | SEG-EU-023; SEG-EU-024; SEG-EU-025 | `P191-EU`, `P191-R4` | `SL4` (black-dot join depiction); `SL5` (wire color) | — | — |
| JUNC-EU-J1-A | J1 grouped letter A | TERM-EU-J1-A-LEFT; TERM-EU-J1-A-RIGHT; TERM-EU-J1-A-BOTTOM | `P191-EU`, `P191-R3` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |
| JUNC-EU-J1-B | J1 grouped letter B | TERM-EU-J1-B-TOP; TERM-EU-J1-B-BOTTOM | `P191-EU`, `P191-R4` | `SL6` (connector-view convention) | `SC189` | `AMB-CON-001`; `AMB-CON-003` |
| JUNC-EU-EA | black-dot join on EA W-B continuation | SEG-EU-029; CONT-EU-EA | `P191-EU`, `P191-R5` | `SL4` (black-dot join depiction); `SL5` (ground-point notation) | — | — |
| JUNC-EU-EB | black-dot join on EB W-B continuation | SEG-EU-028; CONT-EU-EB | `P191-EU`, `P191-R5` | `SL4` (black-dot join depiction); `SL5` (ground-point notation) | — | — |
| JUNC-EU-IE | black-dot joins on IE W-B continuation | SEG-EU-031; SEG-EU-036; CONT-EU-IE | `P191-EU`, `P191-R5` | `SL4` (black-dot join depiction); `SL5` (ground-point notation) | — | — |
| JUNC-EU-IF | black-dot join on IF BR continuation | SEG-EU-039; CONT-EU-IF | `P191-EU`, `P191-R5` | `SL4` (black-dot join depiction); `SL5` (ground-point notation) | — | — |

### 8. Continuations

| Candidate continuation ID | Exact printed identifier or label | Attached printed wire-color code | Source location | Source-described context | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONT-EU-B | B | R at the two selected branches | `P191-R3`, top common line | page-spanning printed line identified `B` | `P191-EU` | `SL5` (wire color) | — | — | candidate |
| CONT-EU-REAR-FOG-HLC-RW | From Rear Fog Light SW (2-8); From Headlight Cleaner SW (5-1) | R-W | `P191-R3` | two printed related-system labels at one visible input | `P191-EU` | `SL5` (wire color and related-system notation) | — | `AMB-DEP-001` | candidate |
| CONT-EU-TAILLIGHT-C15 | From Taillight Relay (Ex. Iceland, Denmark) (4-1) | LG-R | `P191-R3` | related-system reference | `P191-EU` | `SL5` (wire color, related-system, and variation notation) | — | — | candidate |
| CONT-EU-DAYTIME-C15 | From Daytime Running Light Relay (5-7) | G-Y | `P191-R3` | related-system reference | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-HEADLIGHT-CLEANER-RG | From Headlight Cleaner SW (5-1) | R-G | `P191-R3` | related-system reference; equipment applicability unresolved | `P191-EU` | `SL5` (wire color and related-system notation) | — | `AMB-DEP-001` | candidate |
| CONT-EU-LIGHT-CONTROL | To Light Control SW (5-6) | G-Y | `P191-R3`, D2 terminal 2 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-TAILLIGHT-D2 | From Taillight Relay (4-1) | LG-R | `P191-R3`, D2 terminal 3 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-REAR-FOG-D2 | From Rear Fog Light SW (2-8) | R-L | `P191-R3`, D2 terminal 11 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-DOME | From "DOME" Fuse (8-2) | R | `P191-R3`, D2 terminal 12 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-ENGINE | From "ENGINE" Fuse (2-1) | B-Y | `P191-R3`, D2 terminal 1 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-CHARGE | To "CHARGE" Fuse (2-2) | Y | `P191-R3`, D2 terminal 8 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-CLOCK | To Clock (9-1) | G | `P191-R3`, D2 terminal 7 | related-system reference printed at D2 | `P191-EU` | `SL5` (wire color and related-system notation) | — | — | candidate |
| CONT-EU-EA | EA | W-B | `P191-R5` | printed ground-point identifier; legend: `Located on front right fender` | `P191-EU` | `SL5` (wire color and ground-point notation) | — | — | candidate |
| CONT-EU-EB | EB | W-B | `P191-R5` | printed ground-point identifier; legend: `Located on front left fender` | `P191-EU` | `SL5` (wire color and ground-point notation) | — | — | candidate |
| CONT-EU-IE | IE | W-B | `P191-R5` | printed ground-point identifier; legend: `Located on left kick panel` | `P191-EU` | `SL5` (wire color and ground-point notation) | — | — | candidate |
| CONT-EU-IF | IF | BR | `P191-R5` | printed ground-point identifier; legend: `Located on right kick panel` | `P191-EU` | `SL5` (wire color and ground-point notation) | — | — | candidate |

`AMB-GND-001` remains open for mapping beyond the legible page-191 identifiers.
It is not attached to these neutral continuation transcriptions because resolving
an external mapping would not change their visible identifiers, wire colors, or
printed legends.

### 9. Related-System References

| Printed label | Destination | Source location | Reason retained | Primary evidence | Interpretive dependencies | Supporting evidence | Ambiguity IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| From Rear Fog Light SW (2-8); From Headlight Cleaner SW (5-1) | locations `2-8` and `5-1` | `P191-R3`, R-W input joined to the selected Europe arrangement | visible references entering the boundary; referenced systems are not imported | `P191-EU` | `SL5` (related-system notation) | — | — |
| From Headlight Cleaner SW (5-1) | location `5-1` | `P191-R3`, R-G input at the D2 terminal-5 path | visible reference entering the boundary; Headlight Cleaner is not imported | `P191-EU` | `SL5` (related-system notation) | — | — |
| From Taillight Relay (Ex. Iceland, Denmark) (4-1) | location `4-1` | `P191-R3`, LG-R input at C15 T / 11 | visible reference entering the boundary; Taillight is not imported | `P191-EU` | `SL5` (related-system and variation notation) | — | — |
| From Daytime Running Light Relay (5-7) | location `5-7` | `P191-R3`, G-Y input at C15 T / 11 | visible reference entering the boundary | `P191-EU` | `SL5` (related-system notation) | — | — |
| To Light Control SW (5-6) | location `5-6` | `P191-R3`, D2 terminal 2 by G-Y | visible reference leaving D2 | `P191-EU` | `SL5` (related-system notation) | — | — |
| From Taillight Relay (4-1) | location `4-1` | `P191-R3`, D2 terminal 3 by LG-R | visible reference entering D2; Taillight is not imported | `P191-EU` | `SL5` (related-system notation) | — | — |
| From Rear Fog Light SW (2-8) | location `2-8` | `P191-R3`, D2 terminal 11 by R-L | visible reference entering D2; Rear Fog Light is not imported | `P191-EU` | `SL5` (related-system notation) | — | — |
| From "DOME" Fuse (8-2) | location `8-2` | `P191-R3`, D2 terminal 12 by R | visible reference entering D2 | `P191-EU` | `SL5` (related-system notation) | — | — |
| From "ENGINE" Fuse (2-1) | location `2-1` | `P191-R3`, D2 terminal 1 by B-Y | visible reference entering D2 | `P191-EU` | `SL5` (related-system notation) | — | — |
| To "CHARGE" Fuse (2-2) | location `2-2` | `P191-R3`, D2 terminal 8 by Y | visible reference leaving D2 | `P191-EU` | `SL5` (related-system notation) | — | — |
| To Clock (9-1) | location `9-1` | `P191-R3`, D2 terminal 7 by G | visible reference leaving D2 | `P191-EU` | `SL5` (related-system notation) | — | — |

Headlight Cleaner, Rear Fog Light, Taillight, Clock, and the named fuse systems
are retained only as printed boundary references. Headlight Cleaner is not
extracted as a separate system. Winch, Back-Up Light, light-duty circuits, and
other page-191 systems remain outside the boundary.

### 10. Europe Extraction Summary

| Candidate category | Count |
| --- | ---: |
| objects | 15 |
| terminals | 48 |
| conductors | 44 |
| source-labeled relay objects | 3 |
| fuses | 4 |
| junctions | 16 |
| continuations | 16 |
| related-system references | 11 |
| attached ambiguity IDs | 4 |

The four attached ambiguity IDs are `AMB-CON-001`, `AMB-CON-003`,
`AMB-CON-004`, and `AMB-DEP-001`. `AMB-CON-001` attaches only to the two J1
grouped-meaning candidates. `AMB-CON-003` attaches to displayed J1 positions,
segments whose endpoints use those positions, and the two grouped-junction
candidates because resolving positional correspondence could change those
mappings. `AMB-CON-004` attaches only to the two C15 construct candidates;
it is not propagated to direct terminal, conductor, or contact-table
transcriptions. `AMB-DEP-001` attaches only to candidates whose applicability
or boundary treatment could change with the Headlight Cleaner equipment answer.

`AMB-APP-001` and `AMB-APP-002` remain open but do not attach because these
candidates assert only source-labeled Europe scope, not target-vehicle
applicability. `AMB-DEP-002` remains open, but each D2 candidate preserves the
printed `(Iceland, Denmark)` object scope or an explicit conductor qualifier;
no broader Europe claim is made that its resolution could change.
`AMB-GND-001` remains open for external continuation mapping but does not attach
to legible neutral EA, EB, IE, or IF transcriptions. `AMB-CON-002` remains open
with no attachment because no selected crossing in this transcription requires
a choice between materially different source readings.

No existing Except-Europe candidate was changed by this Europe extraction. No
current flow, hidden relay behavior, switching logic, component equivalence,
diagnostic meaning, or target-vehicle applicability is asserted.
