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

This transcription covers EWD168F printed page 191, one-based PDF page index
186 (zero-based index 185), Heavy-Duty System Circuits 5, beginning at source
location 5-4. The local PDF hash matched the committed source metadata before
inspection. Every entry below is pre-canonical candidate work and requires
independent review.

### Visible Objects

| Provisional candidate ID | Exact source label | Source code | Source location | Candidate descriptive kind | Visible terminal labels | Applicability | Transcription status | Notes or ambiguity reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OBJ-EX-HEAD-RELAY | `HEADLIGHT RELAY` | — | EWD168F p. 191, PDF index 186, location 4, P191-R1 | relay | `1`, `2`, `3`, `4` | Headlight (Ex. Europe) | candidate transcribed; review pending | Target applicability not asserted (AMB-APP-001; AMB-APP-002). |
| OBJ-EX-FUSE-BLOCK-1 | `FUSE BLOCK NO. 1` | — | EWD168F p. 191, PDF index 186, location 4, P191-R1 | fuse block | `1`, `2`, `3` | Headlight (Ex. Europe) | candidate transcribed; review pending | Terminal `1` is visibly common to both depicted fuses. |
| OBJ-EX-FUSE-HEAD-LH | `10A HEAD LH` | — | EWD168F p. 191, PDF index 186, location 4, P191-R1 | fuse | `1`, `3` | Headlight (Ex. Europe) | candidate transcribed; review pending | Exact printed label and rating retained. |
| OBJ-EX-FUSE-HEAD-RH | `10A HEAD RH` | — | EWD168F p. 191, PDF index 186, location 4, P191-R1 | fuse | `1`, `2` | Headlight (Ex. Europe) | candidate transcribed; review pending | Exact printed label and rating retained. |
| OBJ-EX-H5 | `HEADLIGHT` | `H5 LH` | EWD168F p. 191, PDF index 186, location 4, P191-R1 | headlight | `1`, `2`, `3` | Headlight (Ex. Europe) | candidate transcribed; review pending | Duplicate-looking headlight symbols remain separate source objects. |
| OBJ-EX-H6 | `HEADLIGHT` | `H6 RH` | EWD168F p. 191, PDF index 186, location 4, P191-R1 | headlight | `1`, `2`, `3` | Headlight (Ex. Europe) | candidate transcribed; review pending | Duplicate-looking headlight symbols remain separate source objects. |
| OBJ-EX-J3 | `JUNCTION CONNECTOR No. 3` | `J3` | EWD168F p. 191, PDF index 186, location 4, P191-R1/P191-R2 | junction connector | `H` at three displayed points; `G` at three displayed points | Headlight (Ex. Europe) | candidate transcribed; review pending | Distinct displayed points are retained; grouped-letter semantics remain open (AMB-CON-001). |
| OBJ-EX-C15-LIGHT | `LIGHT CONTROL SW [COMB. SW]` | `C15` | EWD168F p. 191, PDF index 186, location 4, P191-R2 | switch function within source-labeled part | `T`/`11`, `EL`/`10`, `H`/`4` | Headlight (Ex. Europe) | candidate transcribed; review pending | Separate C15 source function retained (AMB-CON-004). D10 boundary remains open (AMB-BOUND-001). |
| OBJ-EX-C15-DIMMER | `DIMMER SW [COMB. SW]` | `C15` | EWD168F p. 191, PDF index 186, location 4, P191-R2 | switch function within source-labeled part | `HF`/`12`, `HL`/`6`, `HU`/`5`, `ED`/`13` | Headlight (Ex. Europe) | candidate transcribed; review pending | Separate C15 source function retained (AMB-CON-004). |
| OBJ-EX-C13 | `HIGH BEAM INDICATOR LIGHT [COMB. METER]` | `C13` | EWD168F p. 191, PDF index 186, location 4, P191-R2 | indicator light within source-labeled part | `10`, `13` | Headlight (Ex. Europe) | candidate transcribed; review pending | No function beyond the exact source label is asserted. |
| OBJ-EX-J1 | `JUNCTION CONNECTOR No. 1` | `J1` | EWD168F p. 191, PDF index 186, location 4, P191-R2 | junction connector | `A` at three displayed points; `B` at two displayed points | Headlight (Ex. Europe) | candidate transcribed; review pending | Distinct displayed points are retained; grouped-letter semantics remain open (AMB-CON-001). |
| OBJ-EX-D10 | `DIODE (for Rear Fog Light)` | `D10` | EWD168F p. 191, PDF index 186, location 4, P191-R2 | diode | `1`, `2`, `3` | Visible within the Headlight (Ex. Europe) boundary; equipment scope unresolved | candidate transcribed; boundary review pending | Two internal diode symbols are depicted; no operating behavior is inferred (AMB-BOUND-001). |

### Terminal and Contact Candidates

| Provisional terminal ID | Owning source object | Exact printed terminal number or code | Source location | Visible attached wire-color code | Role only when explicitly printed | Ambiguity reference | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TERM-EX-RELAY-1 | OBJ-EX-HEAD-RELAY | `1` | p. 191, PDF index 186, location 4, P191-R1 | `R` | — | — | clear candidate; review pending |
| TERM-EX-RELAY-2 | OBJ-EX-HEAD-RELAY | `2` | p. 191, PDF index 186, location 4, P191-R1 | `R-G` | — | — | clear candidate; review pending |
| TERM-EX-RELAY-3 | OBJ-EX-HEAD-RELAY | `3` | p. 191, PDF index 186, location 4, P191-R1 | `R-W` | — | — | clear candidate; review pending |
| TERM-EX-RELAY-4 | OBJ-EX-HEAD-RELAY | `4` | p. 191, PDF index 186, location 4, P191-R1 | `R` | — | — | clear candidate; review pending |
| TERM-EX-FB1-1 | OBJ-EX-FUSE-BLOCK-1 | `1` | p. 191, PDF index 186, location 4, P191-R1 | `R-G` | — | — | clear common terminal candidate; review pending |
| TERM-EX-FB1-2 | OBJ-EX-FUSE-BLOCK-1 | `2` | p. 191, PDF index 186, location 4, P191-R1 | `R-B` | — | — | clear candidate; review pending |
| TERM-EX-FB1-3 | OBJ-EX-FUSE-BLOCK-1 | `3` | p. 191, PDF index 186, location 4, P191-R1 | `R-L` | — | — | clear candidate; review pending |
| TERM-EX-H5-1 | OBJ-EX-H5 | `1` | p. 191, PDF index 186, location 4, P191-R1 | `R-G` | — | — | clear candidate; review pending |
| TERM-EX-H5-2 | OBJ-EX-H5 | `2` | p. 191, PDF index 186, location 4, P191-R1 | `R-Y` | — | — | clear candidate; review pending |
| TERM-EX-H5-3 | OBJ-EX-H5 | `3` | p. 191, PDF index 186, location 4, P191-R1 | `R-L` | — | — | clear candidate; review pending |
| TERM-EX-H6-1 | OBJ-EX-H6 | `1` | p. 191, PDF index 186, location 4, P191-R1 | `R-G` | — | — | clear candidate; review pending |
| TERM-EX-H6-2 | OBJ-EX-H6 | `2` | p. 191, PDF index 186, location 4, P191-R1 | `R-Y` | — | — | clear candidate; review pending |
| TERM-EX-H6-3 | OBJ-EX-H6 | `3` | p. 191, PDF index 186, location 4, P191-R1 | `R-B` | — | — | clear candidate; review pending |
| TERM-EX-J3-H-TOP | OBJ-EX-J3 | `H` (displayed top) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-G` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J3-H-RIGHT | OBJ-EX-J3 | `H` (displayed right) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-G` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J3-H-BOTTOM | OBJ-EX-J3 | `H` (displayed bottom) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-G` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J3-G-TOP | OBJ-EX-J3 | `G` (displayed top) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-Y` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J3-G-RIGHT | OBJ-EX-J3 | `G` (displayed right) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-Y` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J3-G-BOTTOM | OBJ-EX-J3 | `G` (displayed bottom) | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | `R-Y` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-C15L-T11 | OBJ-EX-C15-LIGHT | `11` / `T` | p. 191, PDF index 186, location 4, P191-R2 | `LG-R` | `T` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C15L-EL10 | OBJ-EX-C15-LIGHT | `10` / `EL` | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | `EL` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C15L-H4 | OBJ-EX-C15-LIGHT | `4` / `H` | p. 191, PDF index 186, location 4, P191-R2 | `R-W`; `R-B` | `H` | AMB-CON-004; AMB-BOUND-001 | clear junction at printed contact; boundary review pending |
| TERM-EX-C15D-HF12 | OBJ-EX-C15-DIMMER | `12` / `HF` | p. 191, PDF index 186, location 4, P191-R2 | `R-W` | `HF` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C15D-HL6 | OBJ-EX-C15-DIMMER | `6` / `HL` | p. 191, PDF index 186, location 4, P191-R2 | `R-G` | `HL` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C15D-HU5 | OBJ-EX-C15-DIMMER | `5` / `HU` | p. 191, PDF index 186, location 4, P191-R2 | `R-Y` | `HU` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C15D-ED13 | OBJ-EX-C15-DIMMER | `13` / `ED` | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | `ED` | AMB-CON-004 | clear printed contact candidate; review pending |
| TERM-EX-C13-10 | OBJ-EX-C13 | `10` | p. 191, PDF index 186, location 4, P191-R2 | `R-G` | — | — | clear candidate; review pending |
| TERM-EX-C13-13 | OBJ-EX-C13 | `13` | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | — | clear candidate; review pending |
| TERM-EX-J1-A-LEFT | OBJ-EX-J1 | `A` (displayed left) | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J1-A-RIGHT | OBJ-EX-J1 | `A` (displayed right) | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J1-A-BOTTOM | OBJ-EX-J1 | `A` (displayed bottom) | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J1-B-TOP | OBJ-EX-J1 | `B` (displayed top) | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-J1-B-BOTTOM | OBJ-EX-J1 | `B` (displayed bottom) | p. 191, PDF index 186, location 4, P191-R2 | `W-B` | — | AMB-CON-001 | distinct visible connection candidate; semantic review pending |
| TERM-EX-D10-1 | OBJ-EX-D10 | `1` | p. 191, PDF index 186, location 4, P191-R2 | `R-W` | — | AMB-BOUND-001 | clear candidate; boundary review pending |
| TERM-EX-D10-2 | OBJ-EX-D10 | `2` | p. 191, PDF index 186, location 4, P191-R2 | `R-B` | — | AMB-BOUND-001 | clear candidate; boundary review pending |
| TERM-EX-D10-3 | OBJ-EX-D10 | `3` | p. 191, PDF index 186, location 4, P191-R2 | `R-L` | — | AMB-BOUND-001 | clear candidate; boundary review pending |

### Conductor Segment Candidates

One segment ends at each visible connection point, branch, or continuation
boundary. Wire-color codes retain Toyota's printed notation.

| Provisional segment ID | From endpoint | To endpoint | Exact printed wire-color code | Source location or region | Joins or branches encountered | Continuation reference | Applicability | Confidence/status | Ambiguity reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEG-EX-001 | CONT-EX-B | TERM-EX-RELAY-4 | `R` | p. 191, PDF index 186, location 4, P191-R1 | J-EX-B-4; inline marker `1` | `B` | Headlight (Ex. Europe) | clear candidate; review pending | — |
| SEG-EX-002 | CONT-EX-B | TERM-EX-RELAY-1 | `R` | p. 191, PDF index 186, location 4, P191-R1 | J-EX-B-1; inline marker `1` | `B` | Headlight (Ex. Europe) | clear candidate; review pending | — |
| SEG-EX-003 | TERM-EX-RELAY-2 | TERM-EX-FB1-1 | `R-G` | p. 191, PDF index 186, location 4, P191-R1 | inline marker `1`; J-EX-FB1 | — | Headlight (Ex. Europe) | clear candidate; review pending | — |
| SEG-EX-004 | TERM-EX-FB1-3 | TERM-EX-H5-3 | `R-L` | p. 191, PDF index 186, location 4, P191-R1 | none depicted | — | Headlight (Ex. Europe) | clear candidate; review pending | — |
| SEG-EX-005 | TERM-EX-FB1-2 | TERM-EX-H6-3 | `R-B` | p. 191, PDF index 186, location 4, P191-R1 | none depicted | — | Headlight (Ex. Europe) | clear candidate; review pending | — |
| SEG-EX-006 | TERM-EX-H5-1 | TERM-EX-J3-H-TOP | `R-G` | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | J-EX-J3-H | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-007 | TERM-EX-H6-1 | TERM-EX-J3-H-RIGHT | `R-G` | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | J-EX-J3-H | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-008 | TERM-EX-J3-H-BOTTOM | J-EX-RG | `R-G` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-J3-H; J-EX-RG | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-009 | J-EX-RG | TERM-EX-C15D-HL6 | `R-G` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-RG | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-002 |
| SEG-EX-010 | J-EX-RG | TERM-EX-C13-10 | `R-G` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-RG | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-002 |
| SEG-EX-011 | TERM-EX-H5-2 | TERM-EX-J3-G-TOP | `R-Y` | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | J-EX-J3-G | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-012 | TERM-EX-H6-2 | TERM-EX-J3-G-RIGHT | `R-Y` | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | J-EX-J3-G | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-013 | TERM-EX-J3-G-BOTTOM | TERM-EX-C15D-HU5 | `R-Y` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-J3-G | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-014 | TERM-EX-RELAY-3 | J-EX-RW-UP | `R-W` | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | inline marker `1`; J-EX-RW-UP | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-BOUND-001 |
| SEG-EX-015 | J-EX-RW-UP | TERM-EX-D10-1 | `R-W` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-RW-UP | — | Headlight (Ex. Europe) boundary; D10 scope unresolved | clear path; boundary review pending | AMB-BOUND-001 |
| SEG-EX-016 | J-EX-RW-UP | TERM-EX-C15L-H4 | `R-W` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-H4 | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-002; AMB-BOUND-001 |
| SEG-EX-017 | TERM-EX-D10-2 | TERM-EX-C15L-H4 | `R-B` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-H4 | — | Headlight (Ex. Europe) boundary; D10 scope unresolved | clear path; boundary review pending | AMB-BOUND-001 |
| SEG-EX-018 | CONT-EX-REAR-FOG | TERM-EX-D10-3 | `R-L` | p. 191, PDF index 186, location 4, P191-R2 | none depicted | `From Rear Fog Light SW (2-8)` | Equipment scope unresolved | clear path; boundary review pending | AMB-BOUND-001 |
| SEG-EX-019 | TERM-EX-C15L-H4 | TERM-EX-C15D-HF12 | `R-W` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-H4 | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-004; AMB-BOUND-001 |
| SEG-EX-020 | CONT-EX-TAILLIGHT | TERM-EX-C15L-T11 | `LG-R` | p. 191, PDF index 186, location 4, P191-R2 | none depicted | `From Taillight Relay (4-1)` | Headlight (Ex. Europe) boundary | clear candidate; review pending | AMB-BOUND-001 |
| SEG-EX-021 | TERM-EX-C15L-EL10 | TERM-EX-J1-A-LEFT | `W-B` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-J1-A | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001; AMB-CON-004 |
| SEG-EX-022 | TERM-EX-C15D-ED13 | TERM-EX-J1-A-RIGHT | `W-B` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-J1-A | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001; AMB-CON-004 |
| SEG-EX-023 | TERM-EX-J1-A-BOTTOM | J-EX-WB-LHD | `W-B` | p. 191, PDF index 186, location 4, P191-R2/P191-R5 | J-EX-J1-A; J-EX-WB-LHD | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |
| SEG-EX-024 | J-EX-WB-LHD | CONT-EX-BH | `W-B` | p. 191, PDF index 186, location 4, P191-R5 | J-EX-WB-LHD | `BH`; source line marked `(LHD)` | Headlight (Ex. Europe), LHD | clear page-191 mapping; continuation review pending | AMB-GND-001 |
| SEG-EX-025 | J-EX-WB-LHD | J-EX-WB-RHD | `W-B` | p. 191, PDF index 186, location 4, P191-R2/P191-R5 | J-EX-WB-LHD; J-EX-WB-RHD | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-002 |
| SEG-EX-026 | J-EX-WB-RHD | CONT-EX-BI | `W-B` | p. 191, PDF index 186, location 4, P191-R5 | J-EX-WB-RHD | `BI`; source line marked `(RHD)` | Headlight (Ex. Europe), RHD | clear page-191 mapping; continuation review pending | AMB-GND-001 |
| SEG-EX-027 | J-EX-WB-RHD | TERM-EX-J1-B-BOTTOM | `W-B` | p. 191, PDF index 186, location 4, P191-R2/P191-R5 | J-EX-WB-RHD; J-EX-J1-B | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001; AMB-CON-002 |
| SEG-EX-028 | TERM-EX-J1-B-TOP | TERM-EX-C13-13 | `W-B` | p. 191, PDF index 186, location 4, P191-R2 | J-EX-J1-B | — | Headlight (Ex. Europe) | clear candidate; review pending | AMB-CON-001 |

### C15 Switch Contact Candidates

The following rows reproduce only the continuity circles and lines depicted in
the two source tables. They do not describe behavior beyond those depictions.

| Exact source function label | Printed terminal/contact labels | Printed switch position or state label | Source-depicted continuity only | Source location | Ambiguity/status |
| --- | --- | --- | --- | --- | --- |
| `C15 LIGHT CONTROL SW [COMB. SW]` | `T`/`11`, `EL`/`10`, `H`/`4` | `OFF` | no continuity depicted | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |
| `C15 LIGHT CONTROL SW [COMB. SW]` | `T`/`11`, `EL`/`10`, `H`/`4` | `TAIL` | `T`—`EL` | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |
| `C15 LIGHT CONTROL SW [COMB. SW]` | `T`/`11`, `EL`/`10`, `H`/`4` | `HEAD` | `T`—`EL`—`H` | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |
| `C15 DIMMER SW [COMB. SW]` | `HF`/`12`, `HL`/`6`, `HU`/`5`, `ED`/`13` | `FLASH` | `HF`—`HU`—`ED` | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |
| `C15 DIMMER SW [COMB. SW]` | `HF`/`12`, `HL`/`6`, `HU`/`5`, `ED`/`13` | `LOW` | `HL`—`ED` | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |
| `C15 DIMMER SW [COMB. SW]` | `HF`/`12`, `HL`/`6`, `HU`/`5`, `ED`/`13` | `HIGH` | `HU`—`ED` | p. 191, PDF index 186, location 4, P191-R2 | AMB-CON-004; candidate transcribed; review pending |

### Headlight Relay Internal Candidate

| Source object | Printed terminal numbers | Coil endpoints | Contact endpoints | Normal depicted contact state | Source location | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `HEADLIGHT RELAY` | `1`, `2`, `3`, `4` | `4`—`3` | `1`—`2` | open | p. 191, PDF index 186, location 4, P191-R1 | candidate transcribed; review pending; no voltage, polarity, or energized behavior asserted |

### Fuse Candidates

| Exact printed fuse label | Printed rating | Upstream endpoint | Downstream endpoint | Source location | Applicability | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `HEAD LH` | `10A` | TERM-EX-FB1-1 | TERM-EX-FB1-3 | p. 191, PDF index 186, location 4, P191-R1 | Headlight (Ex. Europe) | candidate transcribed; review pending |
| `HEAD RH` | `10A` | TERM-EX-FB1-1 | TERM-EX-FB1-2 | p. 191, PDF index 186, location 4, P191-R1 | Headlight (Ex. Europe) | candidate transcribed; review pending |

### Junction and Branch Candidates

| Provisional junction ID | Exact source code | Displayed terminal/group label | Connected candidate segments | Source location | Unresolved semantic question | Ambiguity reference | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| J-EX-B-4 | `B` | black-dot branch to relay terminal `4` | SEG-EX-001 | p. 191, PDF index 186, location 4, P191-R1 | None; exact source code `B` is retained without expansion. | — | candidate branch transcribed; review pending |
| J-EX-B-1 | `B` | black-dot branch to relay terminal `1` | SEG-EX-002 | p. 191, PDF index 186, location 4, P191-R1 | None; exact source code `B` is retained without expansion. | — | candidate branch transcribed; review pending |
| J-EX-FB1 | `FUSE BLOCK NO. 1` | common terminal `1` | SEG-EX-003 | p. 191, PDF index 186, location 4, P191-R1 | None; terminal `1` visibly joins the two depicted fuse inputs, not their downstream segments. | — | candidate junction transcribed; review pending |
| J-EX-J3-H | `J3` | `H` | SEG-EX-006, SEG-EX-007, SEG-EX-008 | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | What does group `H` mean beyond the depicted connections? | AMB-CON-001 | visible mapping transcribed; semantic review pending |
| J-EX-J3-G | `J3` | `G` | SEG-EX-011, SEG-EX-012, SEG-EX-013 | p. 191, PDF index 186, location 4, P191-R1/P191-R2 | What does group `G` mean beyond the depicted connections? | AMB-CON-001 | visible mapping transcribed; semantic review pending |
| J-EX-RG | — | black-dot `R-G` branch | SEG-EX-008, SEG-EX-009, SEG-EX-010 | p. 191, PDF index 186, location 4, P191-R2 | Independent review must confirm the three-way join. | AMB-CON-002 | candidate branch transcribed; review pending |
| J-EX-RW-UP | — | visible `R-W` split below inline marker `1` | SEG-EX-014, SEG-EX-015, SEG-EX-016 | p. 191, PDF index 186, location 4, P191-R2 | Does the D10 branch remain inside the final headlight boundary? | AMB-BOUND-001 | candidate branch transcribed; boundary review pending |
| J-EX-H4 | `C15` | black-dot branch at `H`/`4` | SEG-EX-016, SEG-EX-017, SEG-EX-019 | p. 191, PDF index 186, location 4, P191-R2 | How should the D10 connection be bounded, and how should the C15 source function be represented? | AMB-BOUND-001; AMB-CON-004 | candidate branch transcribed; review pending |
| J-EX-J1-A | `J1` | `A` | SEG-EX-021, SEG-EX-022, SEG-EX-023 | p. 191, PDF index 186, location 4, P191-R2 | What does group `A` mean beyond the depicted connections? | AMB-CON-001 | visible mapping transcribed; semantic review pending |
| J-EX-WB-LHD | — | black-dot branch marked `W-B (LHD)` | SEG-EX-023, SEG-EX-024, SEG-EX-025 | p. 191, PDF index 186, location 4, P191-R2/P191-R5 | How does BH map to the relevant supporting page? | AMB-GND-001 | candidate branch transcribed; continuation review pending |
| J-EX-WB-RHD | — | black-dot branch marked `W-B (RHD)` | SEG-EX-025, SEG-EX-026, SEG-EX-027 | p. 191, PDF index 186, location 4, P191-R2/P191-R5 | How does BI map to the relevant supporting page? | AMB-GND-001 | candidate branch transcribed; continuation review pending |
| J-EX-J1-B | `J1` | `B` | SEG-EX-027, SEG-EX-028 | p. 191, PDF index 186, location 4, P191-R2 | What does group `B` mean beyond the depicted connections? | AMB-CON-001 | visible mapping transcribed; semantic review pending |

### Continuation Candidates

| Provisional continuation ID | Exact printed identifier or label | Connected candidate segment | Source location | Candidate description | Ambiguity reference | Status |
| --- | --- | --- | --- | --- | --- | --- |
| CONT-EX-B | `B` | SEG-EX-001, SEG-EX-002 | p. 191, PDF index 186, location 4, P191-R1 | shared top source continuation line; meaning not expanded | — | candidate transcribed; review pending |
| CONT-EX-REAR-FOG | `From Rear Fog Light SW (2-8)` | SEG-EX-018 | p. 191, PDF index 186, location 4, P191-R2 | incoming source reference | AMB-BOUND-001 | candidate transcribed; boundary review pending |
| CONT-EX-TAILLIGHT | `From Taillight Relay (4-1)` | SEG-EX-020 | p. 191, PDF index 186, location 4, P191-R2 | incoming source reference | AMB-BOUND-001 | candidate transcribed; boundary review pending |
| CONT-EX-BH | `BH` | SEG-EX-024 | p. 191, PDF index 186, location 4, P191-R5 | lower continuation reached by source line marked `W-B (LHD)`; page legend says `Located on lower back panel inner` | AMB-GND-001 | page-191 mapping clear; referenced-page review pending |
| CONT-EX-BI | `BI` | SEG-EX-026 | p. 191, PDF index 186, location 4, P191-R5 | lower continuation reached by source line marked `W-B (RHD)`; page legend says `Located on cross member frame` | AMB-GND-001 | page-191 mapping clear; referenced-page review pending |

### Transcription Summary

- Visible object candidates: **12**
- Terminal/contact candidates: **36**
- Conductor-segment candidates: **28**
- Fuse candidates: **2**
- Junction/branch candidates: **12**
- Continuation candidates: **5**
- Unresolved ambiguity records: **9** open in the ambiguity log; **7** directly
  affect this transcription (`AMB-APP-001`, `AMB-APP-002`, `AMB-GND-001`,
  `AMB-CON-001`, `AMB-CON-002`, `AMB-CON-004`, `AMB-BOUND-001`)
- Unreadable source regions inside the selected Except-Europe boundary: **none**
  at the resolution reviewed. All candidates still require independent review.
