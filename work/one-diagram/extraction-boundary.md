# EWD168F Headlight Extraction Boundary

## Status

This document records the currently proposed pre-canonical boundary. It is based
on the [source inventory](source-inventory.md) and remains subject to review
against preserved evidence.

## Proposed Boundary

- Publication: **EWD168F**
- Circuit group: **Heavy-Duty System Circuits 5**
- Variant: **Headlight (Except Europe)**, beginning at location `5-4`
- Variant: **Headlight (Europe)**, beginning at location `5-6`
- Primary logical span: the headlight material at locations `5-4` through `5-8`
  on printed page 191, including shared conductors and references necessary to
  interpret the two variants

Both heavy-duty variants remain in the proposed boundary until applicability to
the identified target vehicle is resolved.

## Source-Language Review Gate

### Hard gate

Detailed extraction is blocked only by missing definitions or evidence that
prevent faithful transcription of the selected boundary. The
[source-language review checklist](source-language-review-checklist.md) records
these hard preconditions. A hard blocker may apply to only part of the page; the
boundary may be narrowed around it only without losing source meaning.

For EWD168F page 191:

- printed pages 4–7 must be reviewed;
- the circled Relay Block notation must be understood;
- wire-color and terminal-number conventions must be understood where used;
- black-dot joins must be distinguishable from line crossings; and
- contact-table and continuation notation must be readable wherever required to
  distinguish the source-depicted relationships.

### Soft gate

Applicability, object semantics, extraction-boundary treatment, or future
representation questions may remain open when the source can still be
transcribed neutrally. Each soft ambiguity must remain in the
[ambiguity log](ambiguity-log.md), be cited on affected candidates, and be
reviewed before canonical acceptance.

J1/J3 meaning beyond their visible grouped connections does not block
transcription when those groups and connections can be copied exactly. C15
representation questions do not block transcription of its printed tables.
Applicability questions remain soft unless they affect which source variant is
selected as the extraction boundary; the Except-Europe boundary itself is
explicitly identified above without asserting target-vehicle applicability.

The publication-specific definitions and classifications are recorded in the
[source-language record](source-language.md).

Within the selected boundary, interpretive dependencies and ambiguity
attachments are evaluated per candidate. A reviewed explanatory page is not a
dependency of every candidate, and an open ambiguity does not attach where its
resolution could not materially change the candidate. Attachments do not
propagate through structural adjacency or a shared object.

## Primary Circuit Evidence

- Page 191: Heavy-Duty System Circuits 5, limited to the electrically meaningful
  headlight material for the Except-Europe and Europe variants.

Other systems printed on page 191 do not enter the boundary merely because they
share the spread.

## Notation Dependencies

- Pages 4–5: mandatory example system circuit and circuit notation definitions.
- Page 7: mandatory abbreviations and source terminology.
- Page 165: system-index and variant mapping context.

## Connector Dependencies

- Page 6: mandatory explanation of System Circuit Connectors.
- Page 188: connector detail for C13, C15, H5, and H6.
- Page 189: junction detail for J1 and J3.
- Page 190: same-group boundary context, retained until the connector inventory
  is complete.

## Relay and Fuse-Block Support

- Page 26: engine-compartment relay locations.
- Page 27: heavy-duty instrument-panel relay locations.
- Page 29: Headlight Relay in Relay Block No. 1.
- Page 30: Fuse Block No. 1, Europe.
- Page 31: Fuse Block No. 1, Except Europe.

Page 28 is retained only as light-duty comparison material; it does not bring
the light-duty circuit into scope.

## Physical-Location Support

- Pages 84–85: RHD 1PZ engine-compartment positions and code definitions,
  including H5 and H6.
- Pages 100–101: RHD instrument-panel positions and code definitions, including
  C13, C15, J1, and J3 where applicable.

These pages support physical-location claims. They do not establish electrical
connectivity.

## Publication and Applicability Support

- Publication cover and unnumbered foreword: publication identity, destination,
  and listed models.
- Pages 1 and 3: contents and source structure.
- Page 165: heavy-duty system selection and Europe/Except-Europe distinctions.

## Currently Excluded

- Headlight Cleaner as a separate system, except a source reference necessary
  to interpret the selected headlight circuit;
- Winch;
- Back-Up Light;
- body-routing pages 104–105;
- light-duty headlight circuits;
- beam-level control;
- service part numbers;
- inferred operating behavior or current flow.

## Unresolved Applicability

The target context is the identified 1990 PZJ70 with 1PZ engine and right-hand
drive. That context does not establish whether the Europe or Except-Europe
headlight circuit applies. The August 1992 publication date, production scope,
market, and equipment distinctions also require evidence before either variant
can be selected for the target vehicle.
