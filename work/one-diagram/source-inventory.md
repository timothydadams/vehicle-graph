# EWD168F Headlight Source Inventory

## Status

Working source inventory for the **One Diagram** milestone. This document defines the proposed evidence boundary; it does not establish accepted canonical factory facts.

## Source artifact

- Manufacturer: Toyota Motor Corporation
- Title: **Toyota Land Cruiser Electrical Wiring Diagram**
- Publication number: **EWD168F**
- Date printed on cover: **August 1992**
- Destination printed on cover: **Europe & General**
- Extraction language: **English**
- Foreword applicability:
  - FZJ 70, 73, 75 Series
  - HZJ 70, 73, 75 Series
  - PZJ 70, 73, 75 Series
  - LJ 70, 72, 73, 77, 79 Series
  - RJ 70, 73, 77 Series

## Target context

The intended target is the identified 1990 PZJ70 with 1PZ engine and right-hand drive. Those details guide source selection but do not prove whether the Europe or Except-Europe headlight circuit applies. That remains unresolved.

## Manual structure

| Section | Title | One Diagram role |
| --- | --- | --- |
| A | Introduction | Manual structure |
| B | How to Use This Manual | Toyota diagram notation |
| C | Abbreviations | Source terminology |
| D | Relay Locations | Relay and fuse-block locations |
| E | Electrical Wiring Routing | Physical part and connector locations |
| F | Electrical Wiring Diagram | System index, circuits, connector views |

## Evidence ledger

| Evidence ID | Printed page | Description | Role |
| --- | ---: | --- | --- |
| EWD168F-COVER | cover | Publication cover | identity |
| EWD168F-FOREWORD | unnumbered | Foreword and applicable models | identity/scope |
| EWD168F-P001 | 1 | Contents | navigation |
| EWD168F-P003 | 3 | Section descriptions | source structure |
| EWD168F-P004 | 4 | Example system circuit | notation |
| EWD168F-P005 | 5 | Circuit notation definitions | notation |
| EWD168F-P006 | 6 | System Circuit Connectors explanation | connector interpretation |
| EWD168F-P007 | 7 | Abbreviations | terminology |
| EWD168F-P026 | 26 | Engine-compartment relay locations | location support |
| EWD168F-P027 | 27 | Heavy-duty instrument-panel relay locations | location support |
| EWD168F-P028 | 28 | Light-duty instrument-panel relay locations | comparison |
| EWD168F-P029 | 29 | Relay Block No. 1 | headlight-relay support |
| EWD168F-P030 | 30 | Fuse Block No. 1, Europe | Europe fuse support |
| EWD168F-P031 | 31 | Fuse Block No. 1, Except Europe | Except-Europe fuse support |
| EWD168F-P084 | 84 | RHD 1PZ engine-compartment positions | target location support |
| EWD168F-P085 | 85 | Engine-compartment code table | code definitions |
| EWD168F-P100 | 100 | RHD instrument-panel positions | target location support |
| EWD168F-P101 | 101 | Instrument-panel code table | code definitions |
| EWD168F-P165 | 165 | System-circuit index | system/variant selection |
| EWD168F-P188 | 188 | System Circuit Connectors (5) | connector detail |
| EWD168F-P189 | 189 | System Circuit Connectors (5), continuation | junction detail |
| EWD168F-P190 | 190 | System Circuit Connectors (5), continuation | boundary context |
| EWD168F-P191 | 191 | Heavy-Duty System Circuits 5 | primary circuit spread |

## System-index findings

Page 165 lists, for heavy-duty vehicles:

- `HEADLIGHT (Ex. Europe)` at `5-4`
- `HEADLIGHT (Europe)` at `5-6`

For light-duty vehicles it separately lists Except-Europe, Europe, and beam-level-control circuits. The One Diagram target is heavy-duty. Both heavy-duty variants must remain represented until vehicle applicability is resolved.

## Proposed primary boundary

Page 191 contains Headlight Cleaner, Winch, Back-Up Light, Headlight (Except Europe), and Headlight (Europe). The proposed logical extraction boundary is the headlight material at locations `5-4` through `5-8`, including shared conductors and references necessary to interpret both variants.

Non-headlight systems on the same spread remain outside scope unless a shared element is necessary to understand the headlight circuit.

## Required supporting evidence

### Interpretation

- pp. 4–5: system-circuit notation
- p. 6: connector-view interpretation
- p. 7: abbreviations
- p. 165: system index and variant mapping

### Circuit detail

- p. 191: heavy-duty headlight circuits
- pp. 188–189: connector shapes, colors, cavities, and location references
- p. 190: retained as same-group boundary context until the connector inventory is complete

### Physical location

- p. 29: Headlight Relay in Relay Block No. 1
- p. 30: Europe fuse-block arrangement
- p. 31: Except-Europe fuse-block arrangement
- pp. 84–85: RHD 1PZ engine-compartment locations, including H5 and H6
- pp. 100–101: RHD instrument-panel locations, including C15, J1, and J3 where applicable

## Candidate source-described objects

This is an inventory, not an accepted schema:

- Headlight LH — H5
- Headlight RH — H6
- Headlight Relay
- Light Control SW [Comb. SW] — C15
- Dimmer SW [Comb. SW] — C15
- High Beam Indicator Light [Comb. Meter] — C13
- Junction Connector No. 1 — J1
- Junction Connector No. 3 — J3
- Fuse Block No. 1
- Europe headlight fuses
- Except-Europe headlight fuses
- source-depicted grounds
- related-system continuations

## Connector-view findings

Page 188 shows:

- C13, High Beam Indicator Light [Comb. Meter], blue connector, locations 5-5 and 5-8
- C15, Dimmer SW [Comb. SW], black connector, locations 5-4 and 5-6
- C15, Light Control SW [Comb. SW], black connector, locations 5-4 and 5-6
- H5, Headlight LH, locations 5-4 and 5-7
- H6, Headlight RH, locations 5-4 and 5-8

Page 189 shows:

- J1, Junction Connector No. 1, orange connector, locations 5-4, 5-5, 5-6, and 5-8
- J3, Junction Connector No. 3, blue connector, location 5-4

Connector views establish source-depicted housing shape, cavity display, connector color, and cross-reference. Electrical connectivity must still be traced from page 191.

## Physical-location findings

For the RHD 1PZ engine-compartment view:

- H5 is Headlight LH
- H6 is Headlight RH

For the RHD instrument-panel view:

- C13 is Combination Meter
- C15 is Combination SW
- J1 is Junction Connector No. 1
- J3 is Junction Connector No. 3

Physical location is separate knowledge from electrical connectivity.

## Applicability

### Source-stated

- publication covers Europe & General
- PZJ 70, 73, and 75 Series are included
- heavy-duty and light-duty are distinguished
- Europe and Except-Europe headlight variants are distinguished
- p. 84 is explicitly RHD: 1PZ
- p. 100 is explicitly RHD
- pp. 30–31 distinguish Europe from Except Europe fuse layouts

### Unresolved

- Europe versus Except-Europe applicability for the target vehicle
- whether the 1990 vehicle matches all August 1992 source details
- production-date or serial-number limitations
- market-specific equipment differences
- relevance of factory headlight-cleaner equipment

## Evidence quality

The material is adequate for inventory and boundary discovery. Overlapping
high-resolution working captures of page 191 have now been reviewed and are
adequate for candidate conductor-level transcription. Several later pages are
watermarked scans from a third-party copy, while the user's physical EWD168F
remains the preferred primary artifact.

The page-191 working captures are not currently repository evidence assets, and
their relationship to the user's physical source still needs to be recorded.
Candidate transcription from them is not accepted factory knowledge.

Before accepting conductor-level facts:

- preserve direct scans/photos tied to the physical source
- catalog watermarked pages as working derivatives or secondary evidence
- review candidate transcriptions against adequately identified evidence

## Include

- publication identity and scope
- Toyota notation needed to interpret the circuit
- both heavy-duty headlight variants until applicability is resolved
- relevant connector views
- relay and fuse-block references
- RHD 1PZ and RHD instrument-panel location facts
- explicit ambiguity and variant statements

## Exclude for now

- Headlight Cleaner as a separate system
- Winch
- Back-Up Light
- body-routing pages 104–105
- light-duty headlight circuits
- beam-level control
- service part numbers
- inferred operating behavior

## Page-191 working captures

The reviewed overlapping high-resolution captures cover:

1. Except-Europe fuse/headlamp area
2. Except-Europe switching and junction area
3. Europe switching and junction area
4. Europe fuse/headlamp and high-beam-indicator area
5. lower grounds and continuation references

These working captures are adequate for candidate conductor-level transcription.
They do not replace preserved evidence tied to the user's physical source, and
claims transcribed from them remain candidates until reviewed and accepted.
