# Source Page Object Taxonomy

## Purpose and status

This document defines a pilot-grounded, language-independent **candidate
taxonomy** for source-visible objects on engineering-publication pages. It is
initially supported by the diagram-heavy Milestone 7 Toyota EWD pages `2-3`,
`2-7`, and `3-2` and provides a stable starting vocabulary for the design
investigation in Issue
[#34](https://github.com/timothydadams/vehicle-graph/issues/34) and is limited
to the **Source-visible Structure** layer defined by
[Translation Semantic Layers and Artifact Ownership](TRANSLATION_SEMANTIC_LAYERS.md).

Broader adequacy across publication families is unproven. Issue
[#31](https://github.com/timothydadams/vehicle-graph/issues/31) owns that
evaluation. Later evidence may add, refine, merge, or retire classes; no class
becomes canonical merely by appearing here. This is a conceptual vocabulary,
not a schema. It does not choose JSON fields, identifiers, geometry,
containment rules, reading order, decomposition artifacts, translation
bindings, or graph transformations.

## Governing test

> A source page object is a locatable occurrence of visible content or visible
> organization that a reviewer can identify on the controlling publication
> evidence without first deciding what engineering entity or graph fact it
> means.

An occurrence may be text-bearing, graphical, or organizational. It may have
fuzzy or overlapping extents, distributed or linked visible parts, no explicit
enclosure, or a long course across several regions. It qualifies when a
reviewer can point to its visible parts and association in traceable evidence.
Locatable does not mean OCR-detected, automatically segmented, or already
assigned a bounding box. Issue #27 owns any future boundaries, geometry, or
extents. Publication-defined guidance may be needed to name a visible form
precisely, but the guidance must not promote that form into an engineering
identity or relationship.

The page itself is the outer source-visible surface. A publication is evidence
context, not a page object: no single page occurrence is the publication.
Likewise, a section is represented here only by a visible section indicator,
heading, boundary, or other page occurrence; an inferred document hierarchy is
deferred to Issue #27.

## Page scope and publication-level structure

This candidate taxonomy covers occurrences locatable on one publication page
or visible page surface. Publication identity remains Factory Evidence context,
not a page object. A page-local heading, section indicator, printed page number,
or continuation marker may be a page object because a reviewer can locate it
on that page; the publication hierarchy or resolved cross-page relationship it
suggests is not defined here.

The taxonomy does not define a publication, volume, chapter, section hierarchy,
appendix structure, multi-page table, multi-page figure, foldout, spread,
document-wide motif identity, cross-page reading order, resolved continuation,
or cross-page object identity. A continuation marker is a page object; resolving
where it leads and what persists across pages is separate work. A multi-page
engineering object must not be forced into unrelated page-local identities
before that relationship is designed.

Issue #27 owns page-decomposition design, page hierarchy, overlap, geometry,
stable structural identity, reading order, and related structural organization
questions. Whether a later investigation must own publication-level hierarchy
remains open.

## What a page object is not

A source page object is not:

- an engineering component, connector, harness, conductor, terminal, or
  electrical relationship;
- a graph node, edge, subgraph, accepted fact, or candidate claim;
- a translation unit, translation record, normalized term, or English view;
- an OCR token, computer-vision detection, bounding box, or extraction result;
- proof that nearby, touching, nested, repeated, or similarly labeled forms
  have an engineering relationship; or
- proof of applicability beyond the qualifier visibly attached or associated
  under a reviewed publication convention.

Page objects exist independently of translation because non-textual forms,
source-language text occurrences, layout, exact case, and source-local marks
exist before any English wording is proposed. They exist independently of
graph extraction because the page can be described faithfully even when the
identity, topology, applicability, or engineering meaning of every depicted
form remains unresolved.

## Definition template

Every type below uses the same conceptual template:

- **Purpose** explains why the visible type is distinguished.
- **Observable characteristics** describe how a reviewer can locate it without
  asserting engineering meaning.
- **Typical examples** illustrate the candidate concept without claiming that
  it is sufficient across publication families.
- **May contain / May be contained by** record possible visual organization,
  not a decided hierarchy.
- **Owns / Does not own** state semantic responsibility.
- **May reference** records a visible source reference, not a graph reference.
- **Must not imply** names the most likely unsupported promotion.
- **Pilot examples** point to direct observations on printed pages `2-3`,
  `2-7`, and `3-2` of the verified pilot publication.
- **Open questions** defer unresolved classification or decomposition choices.

“May contain” and “may be contained by” are vocabulary constraints only. They
do not answer Issue #27's questions about page hierarchy, overlap, nesting,
reading order, or stable structural identity. “Owns” describes meaning, not
storage.

## Candidate-class status

Classes have evidence status, not schema status:

| Status | Meaning | Examples in this document |
| --- | --- | --- |
| Pilot-supported | Directly visible on at least one of the three pilot pages | page grid, legend key, text label, connector depiction, path depiction, junction dot |
| Publication-guidance-supported | Classification also depends on reviewed guidance from the same Toyota publication | harness-path depiction, circuit-path depiction, connector cavity, terminal mark |
| Provisional candidate | Plausible vocabulary retained without direct support from the three pilot pages | paragraph, warning, inset |
| Retained for future-family validation | A cautious class whose adequacy or distinctness requires Issue #31 evidence | table subdivisions, continuation reference, splice depiction |

These descriptions are review aids, not implemented status fields. A
pilot-supported class is supported only for the observed pilot forms; it is not
automatically sufficient for another publication family.

## Document objects

### Page

- **Purpose:** identify the complete visible publication surface on which
  occurrences can be located.
- **Observable characteristics:** a bounded sheet or image with printed
  content and page edges; its evidence coordinates are established separately.
- **Typical examples:** a wiring-diagram page or harness-layout page.
- **May contain:** any page object. **May be contained by:** no page object.
- **Owns:** visible page extent and page-local occurrence context. **Does not
  own:** publication identity, artifact fingerprint, or document hierarchy.
- **May reference:** another printed page through visible text.
- **Must not imply:** a graph subgraph or a complete engineering boundary.
- **Pilot examples:** the full visible surfaces of `2-3`, `2-7`, and `3-2`.
- **Open questions:** whether a future decomposition represents the page itself
  as an object or only as evidence context.

### Page region

- **Purpose:** name a visibly distinguishable area without deciding its
  internal hierarchy.
- **Observable characteristics:** separation by whitespace, rule, background,
  alignment, boundary, or coherent visual treatment.
- **Typical examples:** title band, legend area, drawing area, footer strip.
- **May contain:** any occurrence visually within the area. **May be contained
  by:** page or another visibly bounded region.
- **Owns:** the observed area and its visual extent. **Does not own:** reading
  order, semantic hierarchy, or engineering scope.
- **May reference:** nothing solely by being a region.
- **Must not imply:** a graph subgraph or electrical containment.
- **Pilot examples:** the right-side harness legends on `2-3` and `2-7`; the
  lower connector strip on `3-2`.
- **Open questions:** whether page regions are objects, containers, or both.

### Page heading

- **Purpose:** distinguish prominent text that visibly identifies or
  introduces page content.
- **Observable characteristics:** prominent placement or typography, commonly
  near the page top.
- **Typical examples:** page title, diagram title, visible section heading.
- **May contain:** text and qualifiers. **May be contained by:** page or heading
  region.
- **Owns:** exact visible text occurrence, styling, and placement. **Does not
  own:** canonical document title metadata or normalized terminology.
- **May reference:** a visible section or subject only as printed wording.
- **Must not imply:** publication title metadata or engineering identity.
- **Pilot examples:** the Japanese headings with `(1HZ, 1PZ)` on all three
  pages, including the left-side qualifier on `2-7`.
- **Open questions:** when a heading is one composite occurrence versus text
  plus separate qualifier objects.

### Footer

- **Purpose:** distinguish a recurring or page-bottom publication area.
- **Observable characteristics:** content aligned near the lower page edge,
  often separated from the main content.
- **Typical examples:** page code, issue mark, publication mark, donor mark.
- **May contain:** printed page number, publication marks, capture marks, or
  revision marks. **May be contained by:** page.
- **Owns:** visible footer organization. **Does not own:** the truth of
  publication metadata or capture provenance.
- **May reference:** a publication identifier or date exactly as visible.
- **Must not imply:** that all content in the footer is factory-authored.
- **Pilot examples:** the bottom marks and non-factory donor watermark visible
  on `2-3`, `2-7`, and `3-2`.
- **Open questions:** whether repeated footer layouts reuse one class or remain
  page-local motifs.

### Publication mark

- **Purpose:** preserve a visible mark that identifies or characterizes the
  publication.
- **Observable characteristics:** printed code, item number, logo, issue text,
  or publisher mark.
- **Typical examples:** publication item number or publisher imprint.
- **May contain:** text, date marks, or logo forms. **May be contained by:**
  footer, heading, or page.
- **Owns:** the exact visible mark. **Does not own:** verified publication
  identity, edition, or artifact fingerprint.
- **May reference:** publication metadata as visible source text.
- **Must not imply:** that the occurrence alone resolves publication identity.
- **Pilot examples:** `品番6742601` in the footer of all three pages.
- **Open questions:** when a compound date-and-item-number mark is decomposed.

### Revision mark

- **Purpose:** preserve a visible mark presented as a revision, issue, change,
  or dated variant mark without interpreting its effect.
- **Observable characteristics:** date-like, revision-like, or change notation
  positioned with publication content.
- **Typical examples:** issue date, changed-item marker, revision code.
- **May contain:** text or symbols. **May be contained by:** footer, heading,
  note, or page.
- **Owns:** exact visible notation. **Does not own:** supersession, effective
  applicability, or publication-version conclusions.
- **May reference:** another visible revision or date notation.
- **Must not imply:** that marked content applies to a particular vehicle.
- **Pilot examples:** the `('95/01 ...)` footer occurrence on all pilot pages.
- **Open questions:** how to distinguish a revision mark from a production
  qualifier when source guidance is incomplete.

### Capture mark or watermark

- **Purpose:** separate visible non-factory capture context from factory page
  content.
- **Observable characteristics:** overlaid, stamped, or added text or graphics
  attributable to scanning, donation, hosting, or later handling.
- **Typical examples:** donor credit or website watermark.
- **May contain:** text or graphical marks. **May be contained by:** page or
  footer area.
- **Owns:** the visible capture occurrence and its non-factory classification
  when supported. **Does not own:** factory content or publication identity.
- **May reference:** a donor or site exactly as displayed.
- **Must not imply:** factory authorship or engineering meaning.
- **Pilot examples:** `Donated by Paul Stockhoff, cruisercult.com` on all three
  pages.
- **Open questions:** whether crop marks, punch holes, stains, and scan defects
  belong to this type or to evidence-quality observations.

## Navigation objects

### Page grid

- **Purpose:** preserve a visible page-navigation lattice.
- **Observable characteristics:** repeated horizontal and vertical divisions
  with edge identifiers.
- **Typical examples:** alphanumeric location grid.
- **May contain:** row and column identifiers and visually overlaid content.
  **May be contained by:** page or drawing region.
- **Owns:** visible grid lines and organization. **Does not own:** legend keys,
  connector identities, or page-object coordinates chosen by a repository.
- **May reference:** page-local locations through visible row/column marks.
- **Must not imply:** geometry for a future schema or graph position.
- **Pilot examples:** rows `A`-`D` and columns `1`-`6` on `2-3` and `2-7`.
- **Open questions:** whether grid cells are first-class objects.

### Row identifier

- **Purpose:** preserve a visible identifier associated with a page-grid row.
- **Observable characteristics:** repeated or edge-aligned mark corresponding
  to a horizontal grid band.
- **Typical examples:** `A`, `B`, `C`, `D`.
- **May contain:** text mark. **May be contained by:** page grid or page edge.
- **Owns:** exact visible value, case, and occurrence. **Does not own:** a
  legend-entry identity or repository coordinate.
- **May reference:** a page-grid row under the visible convention.
- **Must not imply:** that an identical legend key has the same role.
- **Pilot examples:** `A`-`D` at both edges of `2-3` and `2-7`.
- **Open questions:** whether duplicated edge marks are separate occurrences.

### Column identifier

- **Purpose:** preserve a visible identifier associated with a page-grid
  column.
- **Observable characteristics:** edge-aligned mark corresponding to a vertical
  grid band.
- **Typical examples:** `1` through `6`.
- **May contain:** text mark. **May be contained by:** page grid or page edge.
- **Owns:** exact visible value and occurrence. **Does not own:** terminal,
  cavity, or connector numbering.
- **May reference:** a page-grid column under the visible convention.
- **Must not imply:** engineering numbering.
- **Pilot examples:** `1`-`6` across the top of `2-3` and `2-7`.
- **Open questions:** whether a grid coordinate is derived from a row and
  column occurrence or represented separately.

### Printed page number

- **Purpose:** distinguish a visible publication page label from PDF or capture
  coordinates.
- **Observable characteristics:** page-local number or compound section-page
  mark in a conventional margin location.
- **Typical examples:** `2-3`, `2-7`, `3-2`.
- **May contain:** text mark. **May be contained by:** heading, footer, or page.
- **Owns:** exact visible value and placement. **Does not own:** PDF page index
  or evidence mapping.
- **May reference:** the visibly labeled page.
- **Must not imply:** a repository identifier.
- **Pilot examples:** the printed numbers on each named pilot page.
- **Open questions:** none raised by the pilot.

### Continuation reference

- **Purpose:** distinguish a visible mark that directs reading beyond the
  current bounded depiction.
- **Observable characteristics:** continuation arrow, destination mark, or
  page/grid reference placed at an interrupted path or content boundary.
- **Typical examples:** off-page continuation marker.
- **May contain:** symbol, label, or cross-reference. **May be contained by:**
  diagram or table region.
- **Owns:** visible continuation form and printed destination. **Does not own:**
  resolved connectivity or destination identity.
- **May reference:** another visible page, grid location, or labeled occurrence.
- **Must not imply:** a graph edge across pages.
- **Pilot examples:** no page-to-page circuit continuation was observed on
  `3-2`; the type is retained because the publication guidance addresses such
  navigation.
- **Open questions:** whether the marker and its destination text are one
  object.

### Cross-reference

- **Purpose:** preserve visible text or a mark that points to another source
  location or labeled occurrence.
- **Observable characteristics:** a source-local page, grid, figure, table, or
  label reference.
- **Typical examples:** page-and-grid citation or referenced identifier.
- **May contain:** text, identifier, or navigation symbol. **May be contained
  by:** note, table cell, callout, or diagram.
- **Owns:** exact visible reference. **Does not own:** successful resolution,
  identity equivalence, or engineering relationship.
- **May reference:** only the source target denoted visibly.
- **Must not imply:** that matching marks identify the same engineering entity.
- **Pilot examples:** source-local connector and location marks are visible on
  the layout pages; their identifier classes are deferred to Issue #29.
- **Open questions:** the boundary between a cross-reference, identifier, and
  label occurrence.

## Textual objects

### Text block

- **Purpose:** provide a language-independent parent type for visibly grouped
  lines or runs of text.
- **Observable characteristics:** glyphs organized by baseline, spacing,
  alignment, punctuation, or shared styling.
- **Typical examples:** heading, paragraph, note, warning, or label.
- **May contain:** text runs, inline qualifiers, and marks. **May be contained
  by:** any visible region or graphical form.
- **Owns:** exact source-visible occurrence, order, case, punctuation, and
  placement. **Does not own:** translation or normalized wording.
- **May reference:** another visible occurrence through its printed content.
- **Must not imply:** an engineering object merely because it names one.
- **Pilot examples:** headings, legend wording, wire-color labels, and block
  labels across the three pages.
- **Open questions:** whether individual glyphs or lines ever need identity.

### Paragraph

- **Purpose:** distinguish visibly continuous prose from labels and tabular
  text.
- **Observable characteristics:** one or more flowing text lines with prose
  spacing and punctuation.
- **Typical examples:** explanatory instructions or descriptive prose.
- **May contain:** inline marks and qualifiers. **May be contained by:** note,
  warning, callout, or text region.
- **Owns:** visible prose organization. **Does not own:** translation units or
  propositions.
- **May reference:** other source locations as printed.
- **Must not imply:** one paragraph equals one translation unit or claim.
- **Pilot examples:** the selected pilot pages are diagram-dominant and do not
  provide a substantial paragraph example.
- **Open questions:** how paragraph boundaries survive multi-column layouts.

### Note

- **Purpose:** distinguish supplemental visible text set apart from primary
  labels or body prose.
- **Observable characteristics:** note marker, offset block, smaller type, or
  visibly separate explanatory text.
- **Typical examples:** diagram note or footnote.
- **May contain:** paragraphs, labels, qualifiers, or cross-references. **May be
  contained by:** page, region, table, or callout.
- **Owns:** visible note occurrence. **Does not own:** truth, applicability, or
  engineering normalization.
- **May reference:** objects or source locations through visible notation.
- **Must not imply:** scope beyond its visible association.
- **Pilot examples:** production-date explanations on `3-2` are better treated
  as a legend, not automatically as a note.
- **Open questions:** the observable threshold between note, legend, and
  qualifier.

### Warning

- **Purpose:** distinguish visibly emphasized cautionary content.
- **Observable characteristics:** warning word, icon, box, color, or typographic
  emphasis presented as caution.
- **Typical examples:** caution or safety warning.
- **May contain:** heading, paragraph, symbol, or qualifier. **May be contained
  by:** page or region.
- **Owns:** visible warning treatment. **Does not own:** hazard classification
  beyond what is printed.
- **May reference:** visibly identified procedures or objects.
- **Must not imply:** a repository risk rating.
- **Pilot examples:** none observed on the three pilot pages.
- **Open questions:** whether caution, notice, and warning require distinct
  source-visible subtypes.

### Text label

- **Purpose:** preserve a compact text occurrence visually associated with a
  nearby form, path, group, or region.
- **Observable characteristics:** short text positioned within, beside, or
  visibly attached by a publication-defined convention.
- **Typical examples:** component wording, wire-color word, connector mark,
  block abbreviation.
- **May contain:** identifier, qualifier, or value text. **May be contained by:**
  symbol, block, legend entry, table cell, or page region.
- **Owns:** exact visible wording and observed association. **Does not own:**
  the object it labels, translation, engineering identity, or topology.
- **May reference:** a nearby depiction only when attachment is visible or
  defined by reviewed source guidance.
- **Must not imply:** text label = engineering component.
- **Pilot examples:** connector callout labels on `2-3` and `2-7`; relay, fuse,
  wire-color, and `コンビネーションメーター` labels on `3-2`.
- **Open questions:** whether every repeated label occurrence needs separate
  identity.

### Qualifier

- **Purpose:** preserve visible wording or notation that narrows another
  occurrence.
- **Observable characteristics:** parenthetical, adjacent, prefixed, suffixed,
  or legend-mediated limiting text or mark.
- **Typical examples:** engine, side, model, market, or production qualifier.
- **May contain:** text, identifier, date, or symbol. **May be contained by:**
  heading, label, legend entry, or note.
- **Owns:** exact visible qualifier and observed scope association. **Does not
  own:** accepted applicability or engineering scope.
- **May reference:** the occurrence it visibly qualifies.
- **Must not imply:** graph applicability.
- **Pilot examples:** `(1HZ, 1PZ)` on all pages; `左側`, `(LH)`, `(RH)`,
  `(~'95.1)`, and `('95.1~)` on the applicable layout occurrences.
- **Open questions:** when a qualifier is an independent object versus part of
  a larger text occurrence.

### Legend

- **Purpose:** distinguish a visible key-to-explanation or mark-to-meaning
  presentation.
- **Observable characteristics:** repeated aligned entries pairing marks,
  swatches, symbols, or keys with text.
- **Typical examples:** harness legend, production legend, symbol legend.
- **May contain:** legend entries, heading, note, and qualifiers. **May be
  contained by:** page region, inset, or table-like area.
- **Owns:** visible legend organization. **Does not own:** engineering entities,
  identifier taxonomy, or applicability conclusions.
- **May reference:** page occurrences through its visible keys or marks.
- **Must not imply:** that a legend key is a page coordinate or graph ID.
- **Pilot examples:** harness legends on `2-3` and `2-7`; circle/square
  production legend on `3-2`.
- **Open questions:** whether production legends require a specialized type.

### Legend entry

- **Purpose:** preserve one visibly grouped correspondence inside a legend.
- **Observable characteristics:** aligned key or symbol, explanatory text, and
  optional swatch or qualifier.
- **Typical examples:** key-label-color row or symbol-date row.
- **May contain:** legend key, label, swatch, symbol, and qualifier. **May be
  contained by:** legend.
- **Owns:** visible correspondence among its displayed parts. **Does not own:**
  identity or meaning beyond the page convention.
- **May reference:** page occurrences bearing the same visible mark.
- **Must not imply:** entity equivalence or accepted applicability.
- **Pilot examples:** `A` through `I` and lowercase entries on `2-3`; uppercase
  and lowercase entries including `H`, `J`, `K`, `k`, `p`, `q` on `2-7`.
- **Open questions:** whether a multi-line entry is one occurrence.

### Legend key

- **Purpose:** distinguish the visible mark used on one side of a legend
  correspondence.
- **Observable characteristics:** compact case-sensitive letter, number,
  symbol, or compound mark aligned with an entry.
- **Typical examples:** boxed uppercase or lowercase letter; circle or square.
- **May contain:** a text or graphical mark. **May be contained by:** legend
  entry.
- **Owns:** exact visible value, case, shape, and occurrence. **Does not own:**
  page-grid coordinates, repository identifiers, or engineering identity.
- **May reference:** matching page marks only under the visible legend
  convention.
- **Must not imply:** legend key = page coordinate.
- **Pilot examples:** uppercase `A`-`I` and lowercase `f`, `g`, `i`, `ℓ` on
  `2-3`; uppercase and lowercase keys on `2-7`; circle and square on `3-2`.
- **Open questions:** identifier classification and scope belong to Issue #29.

### Table, row, column, and table cell

- **Purpose:** distinguish visibly tabular organization and its four common
  structural levels without defining a data model.
- **Observable characteristics:** repeated alignment, rules, headers, or a
  matrix of intersecting bands.
- **Typical examples:** specification table, connector index, state table.
- **May contain:** a table may contain visible rows and columns; their
  intersections may contain cells; cells may contain text, symbols, or marks.
  **May be contained by:** page region, inset, note, or legend-like area.
- **Owns:** visible tabular alignment; a row owns its horizontal occurrence, a
  column its vertical occurrence, and a cell its visible intersection. **Does
  not own:** database records, logical field names, or translated row meaning.
- **May reference:** other source locations through visible cell content.
- **Must not imply:** a schema, record hierarchy, or graph relationship.
- **Pilot examples:** no primary pilot page is a conventional table; the
  repeated fuse listings inside the `3-2` boundary remain diagram labels and
  paths unless a reviewer can point to a visibly tabular structure.
- **Open questions:** where embedded tables fit and whether rows, columns, and
  cells are always individually represented.

## Graphical objects

### Graphical symbol

- **Purpose:** provide a language-independent parent type for a discrete
  conventional drawn mark.
- **Observable characteristics:** repeatable bounded shape distinguishable from
  prose, path, or background illustration.
- **Typical examples:** ground, fuse, battery, contact, or coil form.
- **May contain:** marks or labels. **May be contained by:** block, diagram,
  legend entry, or another composite depiction.
- **Owns:** visible geometry and attached marks. **Does not own:** engineering
  identity, behavior, or connectivity.
- **May reference:** a legend entry or label through a visible convention.
- **Must not imply:** graph node or accepted engineering class.
- **Pilot examples:** the many conventional forms on `3-2`.
- **Open questions:** whether every visible symbol is represented individually.

### Color swatch

- **Purpose:** preserve a bounded sample of visible color used in a legend or
  annotation without deciding what the color denotes.
- **Observable characteristics:** filled rectangle, line sample, or other
  compact color patch aligned with text or a key.
- **Typical examples:** harness-legend color rectangle.
- **May contain:** color fill and border. **May be contained by:** legend entry,
  callout, or annotation region.
- **Owns:** visible color appearance and occurrence. **Does not own:** harness
  identity, wire-color code, rendering value, or engineering classification.
- **May reference:** similarly colored page forms only through a visible legend
  convention.
- **Must not imply:** that color match alone establishes identity.
- **Pilot examples:** the colored rectangles aligned with harness entries on
  `2-3` and `2-7`.
- **Open questions:** how color is described or measured and how scan variance
  is preserved without defining storage.

### Subject illustration

- **Purpose:** distinguish a large contextual drawing over or around which
  callouts and other depictions are arranged.
- **Observable characteristics:** continuous pictorial outline or shaded form
  recognizable as the visual subject of a layout page.
- **Typical examples:** engine-compartment or instrument-panel illustration.
- **May contain:** no semantic children by definition, though other page
  objects may visibly overlap it. **May be contained by:** diagram region.
- **Owns:** visible pictorial form and extent. **Does not own:** vehicle,
  component, location, mounting, or routing facts.
- **May reference:** nothing solely through visible overlap.
- **Must not imply:** that an overlaid path is physically attached to or routed
  through the depicted subject.
- **Pilot examples:** the central engine-compartment drawing on `2-3` and the
  instrument-panel drawing on `2-7`.
- **Open questions:** when a subject illustration is one object versus multiple
  graphical forms, and whether it is background context rather than a
  decomposed object.

### Component symbol

- **Purpose:** distinguish a graphical symbol visibly presented as a bounded
  component-like depiction while remaining below engineering identity.
- **Observable characteristics:** conventional outline or internal marks, often
  with terminal marks or a label.
- **Typical examples:** ignition-switch, battery, alternator, fuse, ground,
  relay-contact, relay-coil, or switch depiction.
- **May contain:** terminal marks, labels, contacts, coils, or other symbols.
  **May be contained by:** diagram, block, or visual group.
- **Owns:** visible composite depiction. **Does not own:** canonical component
  entity, function, state, or topology.
- **May reference:** labels and paths visibly attached to it.
- **Must not imply:** component symbol = engineering component.
- **Pilot examples:** the ignition-switch, two battery, alternator, fuse,
  ground, relay-contact, and relay-coil forms visible on `3-2`.
- **Open questions:** whether those named forms are stable subtypes or
  publication-specific specializations; source guidance controls their naming.

### Connector depiction

- **Purpose:** preserve a visible connector-like outline independently of any
  connector entity.
- **Observable characteristics:** bounded face or profile drawing, often with
  repeated internal positions and a nearby source-local mark.
- **Typical examples:** connector face, inline connector profile, grouped pair.
- **May contain:** cavities, terminal marks, labels, and graphical detail. **May
  be contained by:** callout, group, block, or diagram region.
- **Owns:** visible outline and internal visual arrangement. **Does not own:**
  canonical connector identity, mating relation, pinout, or applicability.
- **May reference:** a nearby label or callout under visible/source-defined
  association.
- **Must not imply:** connector depiction = connector entity.
- **Pilot examples:** numerous labeled connector drawings around `2-3` and
  `2-7`; the lower connector strip and in-diagram depictions on `3-2`.
- **Open questions:** how profile and face views are distinguished without
  asserting identity.

### Connector cavity

- **Purpose:** preserve one visible position inside a connector depiction.
- **Observable characteristics:** repeated bounded position, optionally bearing
  a number, mark, fill, or terminal graphic.
- **Typical examples:** numbered rectangle or circle in a connector face.
- **May contain:** cavity label or terminal mark. **May be contained by:**
  connector depiction.
- **Owns:** visible position, shape, and mark. **Does not own:** canonical
  cavity identity, terminal endpoint, occupancy, or numbering semantics.
- **May reference:** a visible cavity mark.
- **Must not imply:** an electrical endpoint.
- **Pilot examples:** numbered positions within the connector drawings on all
  three pages.
- **Open questions:** whether connector cavity drawings should always be
  decomposed and how positional correspondence is represented.

### Terminal mark

- **Purpose:** distinguish a visible terminal number, letter, circle, or other
  position mark from an engineering terminal.
- **Observable characteristics:** compact mark placed at or within a symbol,
  cavity, path endpoint, or boundary.
- **Typical examples:** numbered terminal or circled letter.
- **May contain:** text or shape. **May be contained by:** symbol, connector
  cavity, block, or path endpoint.
- **Owns:** exact visible mark and placement. **Does not own:** terminal entity,
  endpoint mapping, or connectivity.
- **May reference:** a labeled position under source-defined convention.
- **Must not imply:** canonical terminal identity.
- **Pilot examples:** numbers around the ignition switch, relay depictions,
  fuses, batteries, alternator, meter, and lower connector drawings on `3-2`.
- **Open questions:** identifier class and scope belong to Issue #29.

### Path depiction

- **Purpose:** preserve a visible continuous or segmented line-like route
  without deciding what kind of thing, if any, it depicts.
- **Observable characteristics:** locatable course with styling, color, width,
  bends, interruptions, labels, dots, or boundary intersections.
- **Typical examples:** colored routed form on a layout page or linework in a
  circuit diagram.
- **May contain:** path segments, junction dots, labels, and continuation marks.
  **May be contained by:** diagram, block, or visual group.
- **Owns:** source-visible geometry, styling, color, and extent. **Does not own:**
  a physical conductor, harness, fluid line, data flow, continuity, endpoints,
  or graph topology.
- **May reference:** visibly intersected or attached marks.
- **Must not imply:** path depiction = graph edge or physical route.
- **Pilot examples:** the target-specific harness-path depictions on `2-3` and
  `2-7`; circuit-path depictions on `3-2`.
- **Open questions:** which source-supported roles remain useful across the
  publication families evaluated by Issue #31.

### Harness-path depiction

- **Purpose:** specialize a path depiction when same-publication guidance and
  a target-local legend support its visible harness-layout role.
- **Observable characteristics:** colored routed form visibly associated with a
  named harness legend entry and color swatch under the reviewed convention.
- **Typical examples:** one colored route-like form on a harness-layout page.
- **May contain:** path segments or visible inline marks. **May be contained by:**
  harness-layout diagram or visual group.
- **Owns:** visible route-like form and target-local legend association. **Does
  not own:** an accepted harness entity, individual conductor, physical routing,
  attachment, continuity, or topology.
- **May reference:** its legend entry under the reviewed page convention.
- **Must not imply:** that the depiction is one conductor or proves a physical
  harness route.
- **Pilot examples:** colored harness-layout path depictions on `2-3` and
  instrument-panel harness-layout path depictions on `2-7`.
- **Open questions:** whether later decomposition records one colored form, a
  grouped route, or smaller visual parts.

### Circuit-path depiction

- **Purpose:** specialize a path depiction that occurs in a circuit-diagram
  context without accepting electrical connectivity.
- **Observable characteristics:** circuit linework with visible course, labels,
  intersections, dots, terminal marks, or symbol contacts.
- **Typical examples:** line-like path across the circuit field on `3-2`.
- **May contain:** path segments, junction dots, labels, and terminal marks.
  **May be contained by:** circuit diagram or block.
- **Owns:** visible circuit-path form and its source-defined presentation. **Does
  not own:** one wire, a conductor entity, accepted continuity, or graph edge.
- **May reference:** visibly associated dots, symbols, labels, and terminals.
- **Must not imply:** that visibly connected linework is already an accepted
  connectivity claim.
- **Pilot examples:** the circuit-path depictions across `3-2`.
- **Open questions:** Issue #32 will determine how these observations may
  support candidate connectivity extraction.

### Path segment

- **Purpose:** retain a candidate visual subdivision of a path depiction
  without asserting electrical or physical segmentation.
- **Observable characteristics:** a locatable path portion between bends, joins,
  labels, symbols, boundaries, or other possible visual cues.
- **Typical examples:** one straight or curved portion of circuit linework.
- **May contain:** label or inline mark. **May be contained by:** path depiction
  or block.
- **Owns:** visible local geometry. **Does not own:** wire identity, conductor
  identity, continuity, gauge, color meaning, or graph edge.
- **May reference:** adjacent visible marks.
- **Must not imply:** an independently meaningful conductor or electrical edge.
- **Pilot examples:** possible visual subdivisions between dots, symbols, and
  block boundaries on `3-2`; no segment-level representation is selected.
- **Open questions:** Issues #27 and #32 will determine whether segment-level
  representation is useful.

### Leader line

- **Purpose:** distinguish a line that visibly associates a callout or label
  with another occurrence from a path depiction.
- **Observable characteristics:** thin association line terminating at a label,
  drawing, or callout, without being colored or styled like the depicted
  harness-path depictions on the same page.
- **Typical examples:** connector-to-location association line.
- **May contain:** no required child. **May be contained by:** callout, diagram,
  or page region.
- **Owns:** visible association line. **Does not own:** electrical connectivity
  or engineering relationship.
- **May reference:** its visibly associated endpoint occurrences.
- **Must not imply:** graph edge or conductor.
- **Pilot examples:** the many thin lines from connector/cavity drawings into
  the engine-compartment and instrument-panel illustrations on `2-3` and
  `2-7`.
- **Open questions:** whether leader lines should be first-class objects and how
  ambiguous endpoints are recorded.

### Junction dot

- **Purpose:** preserve a visible dot placed at a path intersection or branch.
- **Observable characteristics:** filled or outlined point aligned with two or
  more path portions.
- **Typical examples:** black dot at a T or crossing.
- **May contain:** no required child. **May be contained by:** path depiction,
  block, or diagram.
- **Owns:** dot shape and exact visible placement. **Does not own:** accepted
  electrical join, splice entity, or graph branching.
- **May reference:** intersecting visible path portions.
- **Must not imply:** accepted connectivity.
- **Pilot examples:** filled junction dots along the circuit-path depictions on
  `3-2`.
- **Open questions:** how a dot differs from a splice symbol under each
  publication's definitions.

### Splice depiction

- **Purpose:** preserve a discrete visible form identified by the publication's
  own guidance as a splice depiction.
- **Observable characteristics:** publication-defined mark at or around path
  portions.
- **Typical examples:** splice mark distinct from an ordinary junction dot.
- **May contain:** label or terminal-like mark. **May be contained by:** path
  depiction or diagram.
- **Owns:** visible form and source-defined classification. **Does not own:**
  splice entity, electrical equivalence, or topology.
- **May reference:** associated visible paths or labels.
- **Must not imply:** graph junction.
- **Pilot examples:** no separate splice subtype is asserted from the pilot
  pages without applying the publication's definitions.
- **Open questions:** which visibly distinct forms the source classifies as
  splices.

### Block boundary

- **Purpose:** preserve a visible enclosure used to group diagram content.
- **Observable characteristics:** rectangle, outline, bracket, or other closed
  or partial boundary around visible forms.
- **Typical examples:** relay block, fuse block, meter boundary.
- **May contain:** symbols, paths, labels, terminal marks, or sub-boundaries.
  **May be contained by:** diagram region or another visible boundary.
- **Owns:** visible enclosure and visual containment. **Does not own:** physical
  assembly, engineering containment, electrical membership, or graph subgraph.
- **May reference:** its visible label.
- **Must not imply:** visual containment = electrical containment.
- **Pilot examples:** the relay-block and fuse-block rectangles and the
  combination-meter enclosure on `3-2`.
- **Open questions:** whether relay-block and fuse-block internal depictions are
  specialized block types or combinations of primitives.

## Structural objects

### Visual group

- **Purpose:** name an evident grouping that lacks or does not require a closed
  boundary.
- **Observable characteristics:** shared alignment, spacing, bracket, styling,
  repetition, or surrounding whitespace.
- **Typical examples:** connector group or repeated symbol cluster.
- **May contain:** any page objects. **May be contained by:** page region,
  inset, callout, block, or another visible group.
- **Owns:** observed grouping cue. **Does not own:** engineering membership,
  hierarchy, or entity identity.
- **May reference:** nothing solely through grouping.
- **Must not imply:** graphical proximity = engineering relationship.
- **Pilot examples:** bracketed connector pairs around `2-3` and `2-7`; the
  repeated lower connector drawings on `3-2`.
- **Open questions:** the minimum visual evidence required to recognize a
  group.

### Diagram boundary

- **Purpose:** distinguish the visible extent of a diagram from surrounding
  page material.
- **Observable characteristics:** rule, frame, whitespace, heading, or other
  visible separation enclosing a coherent graphic presentation.
- **Typical examples:** circuit field or harness-layout field.
- **May contain:** graphical, textual, navigation, and structural objects. **May
  be contained by:** page region or page.
- **Owns:** visible diagram extent. **Does not own:** extraction boundary,
  circuit completeness, or graph subgraph.
- **May reference:** continuation or cross-reference marks within it.
- **Must not imply:** a complete engineering system.
- **Pilot examples:** the framed layout fields on `2-3` and `2-7`; the main
  circuit field above the lower connector strip on `3-2`.
- **Open questions:** whether open whitespace alone can define the boundary.

### Block

- **Purpose:** describe visibly grouped content whose presentation functions as
  a block without requiring an engineering classification.
- **Observable characteristics:** boundary, title, repeated internal layout, or
  coherent enclosure.
- **Typical examples:** labeled relay-like block, fuse-like listing block, or
  text block.
- **May contain:** boundaries, symbols, text, paths, and nested groups. **May be
  contained by:** diagram, page region, or inset.
- **Owns:** visual block organization. **Does not own:** physical assembly,
  electrical containment, or schema hierarchy.
- **May reference:** visible labels or source references.
- **Must not imply:** graph subgraph.
- **Pilot examples:** the visibly labeled `R/B NO.1` and `F/B NO.1` areas on
  `3-2`, named only by their source-visible labels here.
- **Open questions:** overlap with page region and block boundary.

### Inset

- **Purpose:** distinguish a visibly separated subsidiary presentation within
  or beside a main presentation.
- **Observable characteristics:** framed, scaled, offset, or independently
  titled subview.
- **Typical examples:** detail view, alternate view, or supplementary diagram.
- **May contain:** any objects used by the subsidiary presentation. **May be
  contained by:** page, diagram region, or block.
- **Owns:** visible inset treatment. **Does not own:** identity correspondence
  between main and inset forms.
- **May reference:** main-view occurrences through visible callouts.
- **Must not imply:** that similar drawings represent the same entity.
- **Pilot examples:** no unambiguous inset is required to describe the pilot
  pages.
- **Open questions:** how to distinguish insets from adjacent visual groups.

### Annotation region

- **Purpose:** distinguish an area visibly devoted to explanatory annotation.
- **Observable characteristics:** notes, labels, symbols, or leaders arranged
  apart from the main depicted subject.
- **Typical examples:** annotation band or explanatory margin.
- **May contain:** notes, labels, callouts, leaders, or legends. **May be
  contained by:** page or diagram region.
- **Owns:** visible annotation organization. **Does not own:** translated
  wording or graph claims.
- **May reference:** visibly annotated occurrences.
- **Must not imply:** engineering relationship.
- **Pilot examples:** the perimeter connector/callout areas around the central
  drawings on `2-3` and `2-7`.
- **Open questions:** whether annotation region is distinct from page region.

### Callout region

- **Purpose:** distinguish a visibly localized annotation combining one or
  more labels, drawings, brackets, and leader lines.
- **Observable characteristics:** compact group offset from the depicted subject
  and linked by a leader or shared label.
- **Typical examples:** connector/cavity callout.
- **May contain:** label, connector depiction, cavities, bracket, qualifier,
  and leader line. **May be contained by:** annotation region, diagram, or page.
- **Owns:** visible callout grouping. **Does not own:** connector identity,
  endpoint mapping, or engineering association.
- **May reference:** its visibly indicated target occurrence.
- **Must not imply:** identity between depiction and target beyond the visible
  source association.
- **Pilot examples:** connector and cavity callouts around `2-3` and `2-7`.
- **Open questions:** whether each callout is first-class and how overlapping
  callouts are bounded.

## Metadata-bearing objects

Metadata-bearing objects are still page occurrences. They do not own repository
metadata or accepted applicability. A production, engine, model, market, or
publication qualifier is specialized only when the visible wording or a
reviewed publication convention supports that classification; otherwise it
remains a generic qualifier or mark.

### Production qualifier

- **Purpose:** preserve a visible production-date or production-range
  qualification.
- **Observable characteristics:** date-like range text or legend symbol visibly
  associated with another occurrence.
- **Typical examples:** before/after date notation.
- **May contain:** date text, range marks, or legend key. **May be contained by:**
  heading, label, legend entry, callout, or diagram.
- **Owns:** exact visible mark and observed scope. **Does not own:** decoded
  vehicle applicability or effective-date conclusion.
- **May reference:** the occurrence it visibly qualifies.
- **Must not imply:** production qualifier = graph applicability.
- **Pilot examples:** `(~'95.1)` and `('95.1~)` on `2-3` and `2-7`; the
  circle/square production legend and square/circle marks on `3-2`.
- **Open questions:** whether production legends become specialized legends.

### Applicability qualifier

- **Purpose:** provide a parent type for visible source scope limitations.
- **Observable characteristics:** wording or marks visibly narrowing model,
  engine, side, market, equipment, or production scope.
- **Typical examples:** parenthetical model/engine list or variant mark.
- **May contain:** engine, model, market, side, equipment, or production
  qualifier occurrences. **May be contained by:** heading, label, legend, note,
  or table cell.
- **Owns:** exact visible limitation and observed association. **Does not own:**
  accepted claim applicability.
- **May reference:** the visibly qualified occurrence.
- **Must not imply:** universal or vehicle-specific applicability.
- **Pilot examples:** `(1HZ, 1PZ)` on all pages and `左側` on `2-7`.
- **Open questions:** whether this remains a role of qualifier rather than a
  separate object type.

### Engine, model, and market qualifier

- **Purpose:** distinguish visible qualifier subtypes only when the publication
  wording or reviewed guidance identifies their source-local role.
- **Observable characteristics:** compact source wording, code, or list visibly
  associated with a heading, label, or entry.
- **Typical examples:** engine code list, model code, or destination mark.
- **May contain:** text and source-local identifiers. **May be contained by:**
  applicability qualifier, heading, label, legend entry, or table cell.
- **Owns:** exact visible occurrence and source-supported subtype. **Does not
  own:** canonical engine/model/market entity or applicability assertion.
- **May reference:** the occurrence it visibly qualifies.
- **Must not imply:** cross-publication identity or scope transfer.
- **Pilot examples:** `(1HZ, 1PZ)` is visible on all pages; no market qualifier
  is asserted from the pilot pages.
- **Open questions:** identifier meaning and namespace belong to Issue #29.

### Publication identifier occurrence

- **Purpose:** distinguish a visible identifier-like mark presented as
  publication information.
- **Observable characteristics:** item number, document code, or edition mark
  in publication context.
- **Typical examples:** publisher item number.
- **May contain:** text and punctuation. **May be contained by:** publication
  mark, footer, title area, or page.
- **Owns:** exact source-visible occurrence. **Does not own:** canonical source
  identity or repository identifier.
- **May reference:** publication context exactly as printed.
- **Must not imply:** that one visible occurrence proves artifact identity.
- **Pilot examples:** `6742601` within `品番6742601` on all three pages.
- **Open questions:** identifier classification belongs to Issue #29.

## Pilot-page demonstrations

### Printed page 2-3

The page is a framed engine-compartment layout overlaid with a navigation grid.
The rows `A`-`D` and columns `1`-`6` are row and column identifiers belonging to
the page grid. The uppercase and lowercase characters in the right-side harness
legend are legend keys belonging to legend entries. Identical-looking letters
in those two roles must not be conflated.

Around the perimeter, text labels, connector depictions, cavity drawings,
brackets, and leader lines form callouts. The central engine-compartment drawing
is a graphical background or subject depiction. The colored forms laid over it
are harness-layout path depictions: the target-local legend and reviewed
publication convention visibly associate their colors with named harness
entries. They do not thereby become accepted harness entities, individual
conductors, physical routing or attachment facts, or graph edges. The page grid
remains distinct from the case-sensitive legend keys. The footer combines
factory publication marks with a non-factory capture watermark, which remain
distinct object types despite sharing an area.

### Printed page 2-7

The instrument-panel illustration, colored instrument-panel harness-layout path
depictions, perimeter callouts, connector groups, and leader lines are distinct
graphical and structural occurrences. The right-side harness legend contains
uppercase and lowercase keys, text labels, and color swatches. `H`, `J`, `K`,
`k`, `p`, and `q` retain their exact case and occurrence context; their
identifier taxonomy is not decided here. Route-like presentation does not
establish accepted physical routing, attachment, continuity, or topology.

The page heading includes engine and side qualifiers. Individual connector
callouts also display production qualifiers such as `(~'95.1)` and `('95.1~)`.
Those marks are page objects associated with visible occurrences, not accepted
vehicle applicability. The grid remains navigation structure, not a coordinate
system for future decomposition.

### Printed page 3-2

The page visibly contains block boundaries labeled `R/B NO.1` and `F/B NO.1`,
component-like symbols, an ignition-switch depiction, battery and alternator
depictions, circuit-path depictions, wire-color labels, junction dots,
fuse-like forms,
connector depictions, cavity drawings, and terminal marks. The right-side
combination-meter label is a text label adjacent to a visibly enclosed
depiction; the label does not create a component entity.

The circuit-path depictions, path portions, junction dots, symbols, terminal
marks, and symbol boundaries can all be recorded as source-visible structure.
Later extraction may propose connectivity claims from this evidence, but no
claim is accepted merely because the page visibly connects lines. This taxonomy
does not assert that a circuit-path depiction is one wire or conductor entity,
that a dot is accepted electrical connectivity, that a terminal mark is an
endpoint, or that a labeled block is a physical assembly. The circle/square
production legend, its entries, and matching page marks are visible correspondences;
applicability conclusions remain downstream.

## Required distinctions

| Source-visible concept | Must remain distinct from | Reason |
| --- | --- | --- |
| Text label | Engineering component | Wording and its visible association do not establish identity |
| Connector depiction | Connector entity | A drawn view does not establish canonical identity, mating, or applicability |
| Path depiction or path segment | Graph edge | Visible linework is not accepted connectivity or topology |
| Legend key | Page-grid coordinate | Role and occurrence context differ even when glyphs match |
| Page region | Graph subgraph | Visual extent is not an engineering boundary |
| Graphical proximity | Engineering relationship | Nearness is observation, not a claim |
| Page heading | Document-title metadata | A visible heading does not own verified publication identity |
| Production qualifier | Graph applicability | Source-visible scope still requires downstream claim binding and review |
| Translation unit | Page object | Translation owns linguistic representation; structure owns visible occurrence |
| Translation record | Page decomposition | Existing records group translation coverage but do not enumerate page structure |
| Visual containment | Electrical containment | A boundary or enclosure does not establish membership or connectivity |

## Semantic-layer and provenance relationship

This taxonomy belongs entirely to **Source-visible Structure**. Factory
evidence owns the artifact, fingerprint, publication identity, and PDF-to-
printed-page mapping. A future page decomposition may use this vocabulary to
describe visible occurrences, but each occurrence must retain a locatable
reference to that evidence. Same-publication interpretive dependencies are
attached only when their conventions are materially required to classify or
read a visible object.

The taxonomy does not define translation, engineering terminology, graph
entities, graph relationships, candidate claims, accepted knowledge, or
publishing views. Text-bearing objects may later bind to translation records,
but Issue #30 owns that relationship. Graphical objects retain provenance even
when they contain no translatable language. Nothing in the taxonomy increases
authority merely because a page has been decomposed precisely.

## Relationship to future page decomposition

This pilot-grounded vocabulary supplies candidate primitive types for a future
decomposition.
It does not determine whether every occurrence is represented, whether objects
nest or overlap, how regions are bounded, whether reading order is captured, or
which identities are stable. Issue #27 addresses those page-decomposition
design questions with its own evidence and review; it does not declare a
canonical artifact.

## Boundaries with sibling issues

Issue #30's [Page-to-Translation Binding Model](PAGE_TRANSLATION_BINDING_MODEL.md)
references occurrences of the candidate classes defined here. A binding to a
text label does not become a binding to the depicted object it visibly labels,
and nonlinguistic page objects remain valid without bindings.

- Issue [#28](https://github.com/timothydadams/vehicle-graph/issues/28)
  defines semantic ownership and constrains this taxonomy to Source-visible
  Structure.
- Issue [#34](https://github.com/timothydadams/vehicle-graph/issues/34)
  defines page-visible primitive object vocabulary.
- Issue [#27](https://github.com/timothydadams/vehicle-graph/issues/27) will
  define regions, hierarchy, overlap, reading order, and decomposition using
  the vocabulary; this document does not begin that work.
- Issue [#29](https://github.com/timothydadams/vehicle-graph/issues/29) defines
  identifier occurrences, values, classes, references, targets, scope, and
  identity boundaries in the
  [Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md).
- Issue [#30](https://github.com/timothydadams/vehicle-graph/issues/30) will
  define how translation records bind to page objects or regions.
- Issue [#31](https://github.com/timothydadams/vehicle-graph/issues/31) will
  evaluate these candidates across other publication families and determine
  where they require extension or revision.
- Issue [#32](https://github.com/timothydadams/vehicle-graph/issues/32) will
  define how reviewed upstream material supports candidate graph claims.

## Publication families not yet validated

The diagram-heavy pilot does not validate the taxonomy for the following
coverage candidates:

| Unvalidated family | Candidate forms requiring evidence |
| --- | --- |
| Photographs | image areas, captions, overlays, scales, and callouts |
| Charts and plots | axes, scales, series, data points, and chart legends |
| Numbered prose structure | sections, subsections, lists, and list items |
| Mathematics | equations, formula blocks, variables, and equation labels |
| Procedures | ordered steps, prerequisites, outcomes, cautions, and branching |
| Exploded views | part depictions, balloons, leader lines, and parts lists |
| Maps and spatial diagrams | mapped regions, scales, keys, and spatial legends |
| Multi-page structures | tables, figures, foldouts, spreads, continuations, and repeated motifs |
| Engineering change material | revision clouds, strikeouts, stamps, and change markup |

These are coverage candidates, not object classes defined by this document.
Issue #31 will test whether the current primitives describe them or whether the
taxonomy needs additions, refinements, mergers, or retirements. This PR does not
invent unreviewed classes to simulate completeness.

## Non-goals

This investigation does not define or modify schemas, JSON, fields, canonical
hierarchy, stable object IDs, geometry, extraction algorithms, graph topology,
rendering, OCR, NLP, computer vision, translation, engineering normalization,
page-decomposition records, translation records, graph records, validators,
services, or dependencies. It does not decompose the pilot pages, create graph
entities, infer connectivity, or begin Issue #27.

## Open questions

The following questions are deliberately unresolved:

- Should page regions be objects, containers, or both?
- Should every visible symbol be individually represented?
- How should overlapping graphical objects be modeled?
- Should leader lines be first-class objects?
- Should connector cavity drawings always be decomposed?
- Should production legends be specialized objects?
- Should repeated page motifs reuse object classes?
- Where should embedded tables fit?
- When are background illustrations page objects rather than undifferentiated
  graphical context?
- Are grid cells, color swatches, brackets, and path endpoints first-class
  primitives?
- Which named graphical specializations are truly language-independent across
  publication families?
- How should visible damage, punch holes, crop boundaries, and scan defects be
  separated from page content?

No answer is selected here. Unresolved categories must not be forced into a
generic bucket merely to make a future representation appear complete.
