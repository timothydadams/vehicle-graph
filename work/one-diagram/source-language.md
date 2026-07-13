# EWD168F Source-Language Record

## Status

This is a pre-canonical interpretation aid for the One Diagram milestone. It
records the publication's explanatory dependencies; committing it does not make
the record or any candidate claim accepted factory knowledge.

## Publication

- Publication number: **EWD168F**
- Title: **Toyota Land Cruiser Electrical Wiring Diagram**
- Relevant language: **English**

## Required explanatory sections

### Section A

Section A establishes the publication structure. Its section descriptions help
locate the relationship among System Circuits, Relay Locations, Electrical
Wiring Routing, and System Circuit Connectors. These different views must not be
treated as interchangeable: circuit depiction, physical location, and connector
view each have a distinct publication role.

### Section B

Section B, **How to Use This Manual**, is mandatory reading before interpreting
any Section F system circuit.

EWD168F pages 4–6 establish these concepts:

- system-circuit numbering;
- system-section numbering;
- system title;
- wire-color notation, including base color and stripe notation;
- the source depiction and position of parts;
- connector pin numbering, including different female and male numbering;
- relay-block notation;
- junction-block notation and connector codes;
- shared connector naming;
- related-system references;
- wiring-harness and harness-connector notation;
- model, engine, connector, or specification variation notation;
- ground-point notation;
- shielded-cable notation;
- System Circuit Connectors page organization;
- connector color;
- connector shape and cavity depiction; and
- page-location cross-references between a connector view and a system circuit.

Page 5 states that the circled numeral shown beside relay connections identifies
a Relay Block. A circled `1` on page 191 therefore means **Relay Block No. 1**;
it must not be described as a generic inline marker. Page 29 provides supporting
physical and layout context for Relay Block No. 1, including the Headlight Relay
position.

### Section C

Section C defines abbreviations used by the publication. Page 7 also states that
titles printed inside components are terminal names or terminal codes, not
abbreviations.

## Interpretation rules for page 191

Page 191 must be read using pages 4–7 before any detailed transcription begins.

- Preserve Toyota wire-color codes exactly as printed.
- Preserve terminal numbers separately from terminal codes.
- Distinguish relay-block references from connectors and junctions.
- Distinguish black-dot joins from simple line crossings.
- Preserve source-depicted contact-state tables without explaining behavior
  beyond the depiction.
- Use related-system references as boundary references unless the supporting
  system is intentionally brought into scope.
- Do not assign current direction, power direction, polarity, or diagnostic
  meaning unless explicitly established by the source or a later derived
  analysis.

Any candidate extracted from page 191 must cite the applicable explanatory page
or pages as interpretive dependencies as well as citing the target circuit
evidence.

## Hard versus Soft Questions for Page 191

Hard questions are those whose answers are needed to choose a faithful
transcription. For page 191 these include:

- the meaning of circled Relay Block numerals;
- the distinction between a black-dot join and a line crossing;
- Toyota wire-color notation;
- terminal-number notation; and
- how Toyota depicts continuity in the printed contact tables.

These questions must be understood wherever the selected boundary uses them.
An unreadable mark or unresolved convention is a hard blocker only for the
portion whose transcription it could materially change.

Soft questions preserve uncertainty that does not prevent neutral copying. The
current page-191 soft questions include:

- what J1/J3 grouped letters mean beyond the visible grouped connections;
- how the printed C15 functions will later be modeled;
- whether D10 remains inside the final derived headlight boundary;
- target-vehicle applicability; and
- market and equipment scope.

Soft questions are not resolved by permitting transcription. They must be cited
on affected candidates, and no broader meaning may be supplied without evidence.

## Remaining source-language questions

- `AMB-CON-001`: the meaning of J1 and J3 grouped letters beyond what is visibly
  depicted remains unresolved.
- `AMB-CON-002`: page-191 joins, crossings, and continuations still require
  source-guided review.
- `AMB-CON-004`: the separately named C15 functions must remain distinct without
  unsupported internal semantics.

These questions remain in the [ambiguity log](ambiguity-log.md). Detailed
transcription must stop only where an unresolved convention would force a
choice between materially different source transcriptions.
