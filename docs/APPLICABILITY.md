# Applicability

A fact is meaningful only when its applicability is understood.Similar-looking vehicles can
differ by model year, market, body, powertrain, equipment, production date,
option, revision, or prior modification.

## Applicability and confidence are independent.

A fact may apply to a very specific configuration with high confidence, or to
a broad configuration with low confidence. Neither property implies the other.

## Principles

- Applicability is explicit and reviewable.
- Unknown scope remains unknown; it is never widened by convenience.
- The absence of a known exception does not prove universal applicability.
- Source-stated scope and inferred scope must be distinguishable.
- Conflicting applicability claims coexist with provenance until resolved.
- A derived view must disclose the vehicle context used to select facts.

## Factory scope and vehicle identity

Factory knowledge describes a class of vehicles or configurations. A
vehicle-specific overlay describes one identified vehicle. The overlay may
confirm a factory condition, add a measured detail, or record a deviation, but
it does not change what the factory source states for the broader class.

The future model should support the narrowest identifiers justified by evidence
without assuming that any one identifier, including model year or VIN, always
captures every relevant production distinction.

For the **One Diagram** milestone, every extracted fact should use the narrowest applicability supported by the source evidence.

Applicability is a property of facts, not of tools.

Tools may filter or project facts based on applicability, but they do not infer
or broaden applicability unless explicitly directed to do so.
