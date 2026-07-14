# Independent Source Account: IR-001

## Review basis

- Review revision: `R0`
- Frozen candidate commit: `381c3e936108ee3d63920adbe3830595f667de4d`
- Reviewer: `Codex — fresh independent-review session`
- Account saved: `2026-07-14T16:33:37Z`
- Disclosure stage: Stage 1 initial-review materials only

This account is a source-first comparison baseline, not a candidate ledger and
not canonical acceptance. I had not opened the candidate ledger, ambiguity log,
delayed source-language sections, delayed source-inventory sections, or any
existing review-output content when I wrote it.

## Publication, scope, and evidence status

The reviewed source is Toyota publication `EWD168F`, *Toyota Land Cruiser
Electrical Wiring Diagram*, dated August 1992, English, destination stated as
Europe & General. The foreword lists PZJ 70, 73, and 75 Series among the
applicable models. The selected source boundary is the heavy-duty Headlight
(Ex. Europe) and Headlight (Europe) material at locations `5-4` through `5-8`
on printed page 191. The identified 1990 RHD 1PZ PZJ70 is target context only;
the source material reviewed in Stage 1 does not select Europe or Except-Europe
for that vehicle.

The local PDF contains 276 PDF pages and matches the recorded SHA-256
`44914602b067327a5ecf02bdc8667a31eac7de89915824f7744019f2249d7c48`.
Its relationship to the user's physical source remains unrecorded. Printed page
191 and the required printed pages 4-7 are legible at the level needed for
source-first review. Printed pages 188-190 are also present and legible.

The PDF's internal page sequence omits some printed pages. In particular,
printed page 165, listed as system-index and variant-selection support, is not
present between printed pages 155 and 173 in the local PDF. I therefore did not
independently verify any claim that depends on page 165. This does not prevent
literal review of the two explicitly titled page-191 source variants, but it is
an evidence limitation for any candidate that uses page 165 to establish
system selection or applicability.

## Publication language used

Printed pages 4-7 establish the conventions needed here:

- alphabetic wire-color codes, with the first letter denoting base color and
  the second letter denoting stripe color;
- connector pin numbering, including different female and male orientations;
- the circled numeral convention for a Relay Block number;
- junction-block and connector notation, related-system references, variation
  qualifiers, ground points, and connector-page organization;
- the rule that titles printed inside components are terminal names or terminal
  codes rather than abbreviations.

Page 191 visibly uses wire-color codes, circled `1` Relay Block references,
terminal numbers, component terminal codes, contact-state tables, black-dot
joins, continuation arrows, related-system references, geographic qualifiers,
connector/junction codes, and ground-point continuations. Those constructs
must be transcribed without adding current direction, behavior, polarity, or
generic electrical meaning.

## Visible constructs and natural claim boundaries

The page divides naturally into two source-labeled variants:

- `Headlight (Ex. Europe)`, beginning at `5-4` and extending through the shared
  material around `5-5`; and
- `Headlight (Europe)`, beginning at `5-6` and extending through `5-8`.

Within those variants, independently reviewable source constructs include:

- labeled objects and source codes: Fuse Block No. 1, Headlight Relay, Dimmer
  Relay, H5 Headlight LH, H6 Headlight RH, C15 Light Control SW [Comb. SW], C15
  Dimmer SW [Comb. SW], C13 High Beam Indicator Light [Comb. Meter], J1 Junction
  Connector No. 1, J3 Junction Connector No. 3, D10 Diode (for Rear Fog Light),
  and D2 Daytime Running Light Relay where variant-qualified;
- fuse labels, terminal numbers, terminal codes, and the printed contact-state
  tables for the C15 switch functions;
- conductor segments with their printed wire-color codes and explicit
  geographic or variant qualifiers;
- terminal-to-conductor and conductor-to-object endpoint relationships;
- black-dot joins and clearly unjoined crossings as distinct visible claims;
- J1 and J3 grouped correspondences where page 191 shows the group letters and
  page 189 supplies the connector view;
- continuation and related-system references, which are boundary references
  rather than implicit inclusion of the referenced systems; and
- bottom-of-page ground-point continuations, which may be recorded as boundary
  endpoints without inferring chassis behavior.

The source depicts different fuse and control arrangements for the two
variants. Shared names or adjacent conductors do not justify merging their
variant-specific claims. Contact-state rows and terminal correspondences should
remain reviewable separately from behavioral interpretations.

## Supporting views checked

- Printed page 188 supplies connector views and location references for C13,
  C15, H5, and H6.
- Printed page 189 supplies the connector views for J1 and J3. Its visible J1
  cavities are grouped `A` and `B`; its visible J3 populated cavities are
  grouped `G` and `H`.
- Printed page 190 is continuation context for System Circuit Connectors (5)
  but contains no additional selected headlight connector entry.
- Printed pages 26-27 and 29-31 provide relay/fuse layout or location context;
  page 29 visibly identifies the Headlight Relay position in Relay Block No. 1.
- Printed pages 84-85 and 100-101 provide RHD physical-location diagrams and
  code tables. They support physical location or code identification, not page-
  191 electrical connectivity.

## Unresolved readings and evidence limits

- Europe versus Except-Europe applicability to the target vehicle remains
  unresolved.
- The source publication is August 1992 while the target context is a 1990
  vehicle; the reviewed evidence does not establish production-date fit.
- Printed page 165 is unavailable in the fingerprinted PDF, so its asserted
  index mapping cannot be independently checked in this review state.
- The PDF is a contributor-local scan with a visible donor watermark, and its
  relationship to the user's physical EWD168F remains unrecorded.
- The broader engineering meaning or later representation of J1/J3 grouping is
  not established merely by the visible group correspondence.
- Geographic qualifiers such as Iceland, Denmark, Middle East, and exclusions
  must remain exactly scoped to the conductors or objects beside which they are
  printed; proximity alone does not propagate them.

## Boundary exclusions

Headlight Cleaner, Winch, and Back-Up Light material elsewhere on page 191 is
outside the selected boundary except for explicit continuation references
needed to preserve a selected conductor's boundary treatment. Light-duty
circuits, inferred operating behavior, current flow, diagnostics, service part
numbers, and vehicle-specific applicability conclusions are also outside this
source account.
