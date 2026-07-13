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

EWD168F pages 4–7 are mandatory source-language dependencies. Page 191 may not
be interpreted without applying those definitions, and any future Except-Europe
or Europe detailed transcription must cite the relevant source-language
guidance recorded in [source-language.md](source-language.md).

The previous detailed extraction commit was reverted. No detailed conductor
transcription should be recreated as part of this policy task. Future detailed
transcription may proceed when the
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
