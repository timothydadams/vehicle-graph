# Page Decomposition

## Status and purpose

This document recommends a candidate page-decomposition model for Issue #27.
It is an architecture investigation, not a canonical artifact, schema, or
implementation decision.

**Page decomposition** is a reviewable structural representation of
source-visible object occurrences and material visible associations on a
verified publication page or declared page boundary. Every represented
occurrence and association remains locatable in the controlling source evidence
and bound to the verified source artifact. The representation does not require
translation or engineering interpretation.

Page decomposition belongs to the language-independent publication-
representation capability described in [Architecture](ARCHITECTURE.md). It is
evidence-bound, source-visible, reviewable, versioned and revisable, explicit
about uncertainty, and below linguistic or engineering interpretation.

It is not OCR output, plain-text extraction, a translated page, graph
extraction, a canonical engineering model, a rendering, or a pixel-perfect
recreation. It does not assert that every visible line is an engineering
connection.

## Governing principles

1. **Occurrence before meaning.** Record what visibly occurs and where before
   assigning linguistic or engineering meaning.
2. **Evidence before convenience.** Every object instance and relationship must
   have a locatable, reviewable basis in the verified source artifact.
3. **Structure is not engineering.** Visual organization never establishes
   physical membership, electrical connectivity, canonical identity,
   applicability, or graph topology.
4. **Language is optional.** Visible text and placement may be represented
   without reading or translating it. Wording does not supply structural
   identity.
5. **Uncertainty stays local.** Uncertainty attaches to the assertion it could
   materially change.
6. **Coverage is source-boundary based.** Review of all recorded objects does
   not prove that all visible content was recorded.
7. **Simple concepts first.** Use the candidate vocabulary in the
   [Source Page Object Taxonomy](SOURCE_PAGE_OBJECT_TAXONOMY.md), not an
   engineering ontology hidden inside decomposition.

## Terminology

- **Page surface:** one verified PDF page as presented by a specific source
  artifact, including factory-authored publication content, visible non-factory
  capture content, and visible content whose authorship remains uncertain.
- **Decomposition boundary:** the complete page surface or an explicitly
  declared, locatable subset against which coverage is assessed.
- **Region:** a locatable organizational area for navigation, review, and
  coverage. A region is not a graph subgraph.
- **Object class:** a candidate source-visible class from the page-object
  taxonomy.
- **Object instance:** one locatable occurrence of an object class.
- **Structural relationship:** a reviewed source-visible association among
  object instances, not an engineering relationship.
- **Evidence location:** source coordinates and a visual extent or locator
  sufficient for a reviewer to find an occurrence or association.
- **Composite object:** one occurrence whose visible parts cooperate as a
  single document form, such as a callout.
- **Distributed occurrence:** one occurrence occupying multiple noncontiguous
  extents.
- **Repeated motif:** visibly repeated presentation forms; repetition alone
  does not establish shared identity.

## Decomposition unit and boundaries

### Candidate unit

Recommend one decomposition for one verified **page surface**, while allowing
work to declare a frozen boundary containing one or more locatable regions on
that surface. The page remains the navigation and identity anchor; the declared
boundary remains the unit of completeness review.

This supports complete-page work, a bounded page region, multiple linked
regions, and partial decomposition of a frozen boundary. It does not detach a
region from its controlling page surface.

A complete page is identified by publication identity, verified artifact
identity or fingerprint, PDF page, and printed page when present. Printed page
alone is insufficient because numbering may repeat or restart. A partial
boundary must locate every included region, state why the boundary is coherent,
and account for excluded, unreadable, clipped, damaged, and unresolved areas.
Coverage claims apply only to that boundary.

A decomposition proves both its positive scope and its limits by identifying
the controlling page, locating its reviewed boundary, inventorying represented
content, and accounting for visible content outside or unresolved within that
boundary. Foldouts and page spreads require evidence not present in the pilot
and remain deferred.

The verified source artifact controls what is visible and where it is located.
The source publication remains factory evidence for content established as
factory-authored, while a donor watermark, scan or handling mark, or other
capture content is artifact-surface evidence without factory authorship.
Authorship and source role are classified separately from location; precise
decomposition does not grant factory authorship, and uncertain authorship
remains explicit.

### Page and region composition

The page surface is the top organizational container. Candidate region roles
may include heading, legend, diagram, table, notes, footer, inset, annotation,
and repeated page-margin areas. These roles organize navigation and review;
they are not universal classes and require validation in Issue #31.

Regions may nest or overlap where visible layout requires it. An object may be
inside one organizational region, cross a boundary, participate in several
groups, or be referenced from elsewhere. Region labels may require later
linguistic interpretation; the visible region exists without it. Regions
neither own translation nor establish graph membership.

## Object instances

The conceptual progression is:

```text
Semantic layer
    -> candidate object class
        -> source-visible object instance

Source-visible structure
    -> connector depiction
        -> the depiction at a reviewed location on printed page 2-7
```

Each candidate instance conceptually has a stable structural identity, object
class, locatable source-evidence reference, occurrence scope, review status,
specific uncertainty, and optional structural associations. It has no
automatic engineering identity.

Two similar depictions remain separate instances. A reviewed structural
reference or repetition relation may associate them, but does not make them the
same connector, component, terminal, or graph node.

## Locatable evidence bindings

Every location begins with verified publication and artifact identity plus PDF
page; printed page, named boundary, and page grid may supplement it. The visible
extent or locator may use one or more of:

- named region or source-local grid coordinate;
- relative visual description anchored to other visible objects;
- rectangular or polygonal area;
- path or polyline extent;
- point location;
- multiple extents for a distributed occurrence; or
- reference to another located visible object.

Bounding rectangles suit compact labels and symbols but are not universal.
Paths, fuzzy groups, distributed callouts, page grids, repeated motifs, and
objects crossing regions may require other forms. A relationship also requires
evidence: its own visible extent, such as a leader line, or references to the
involved occurrences and the visible cue supporting the association.

Automated detection coordinates are proposals, not reviewed evidence
locations. They acquire review standing only when checked against controlling
evidence and recorded with actual review scope.

Interpretive dependencies remain distinct from primary evidence. Guidance may
define how a grid, symbol, color, or continuation is read, but the target-page
occurrence remains primary evidence for its presence and placement. Attach only
dependencies that materially support the reviewed classification or relation.

## Structural relationship vocabulary

Use a small, conservative vocabulary. Every relationship records its
source-visible basis, involved occurrences, evidence location or cue, review
state, and relationship-specific uncertainty.

| Relationship | Permitted source-visible assertion | Must not imply | Pilot example |
| --- | --- | --- | --- |
| **Containment** | One occurrence is visibly inside a boundary, or document organization places it within a page, region, table, cell, legend, or entry. | Physical or electrical membership, engineering containment, or graph hierarchy. | Relay symbols appear inside `R/B NO.1` on `3-2`; entries appear in the legend on `2-3`. |
| **Visible attachment** | A leader, touching placement, or source-defined cue attaches a label, qualifier, callout, mark, or depiction to another occurrence. | Canonical identity, accepted applicability, endpoint identity, or connectivity. | Connector-callout leaders attach callouts to visible target locations on `2-7`. |
| **Grouping** | Boundary, bracket, alignment, spacing, repeated styling, or whitespace visibly groups occurrences. | Engineering membership or identity; semantic similarity alone is insufficient. | Bracketed connector depictions form groups on `2-3`. |
| **Adjacency** | Proximity is materially relevant to locating or reviewing an occurrence; direction or anchor is stated. | Connectivity, attachment, correspondence, or sequence. | A terminal mark is adjacent to a symbol when no touching cue is clear. |
| **Overlap** | Reviewed extents intersect without necessary containment or attachment. | Grouping, identity, or engineering interaction. | Grid, leaders, subject drawing, and colored paths intersect spatially on `2-3`. |
| **Alignment** | Rows, columns, baselines, grid positions, or repeated layout align occurrences. | Reading order or grouping unless separately supported. | Legend keys, labels, and swatches align on `2-7`; lower connectors align on `3-2`. |
| **Reference** | A visible key, cross-reference, callout, or reviewed publication convention refers to another occurrence or presentation rule. | Engineering equivalence or resolved entity identity. | A harness legend refers to path styling on `2-3`; the production legend refers to distant marks on `3-2`. |
| **Sequence** | Visible numbering, table structure, ordered-list presentation, or reviewed convention supports structural order. | Universal linguistic order, circuit flow, or contributor workflow. | Legend entries may be ordered; the `3-2` circuit has no single page order. |
| **Continuation** | A visible marker points beyond the local extent or page. | Resolved cross-page continuity, shared identity, or topology. | Not required on the pilot targets; resolution remains provisional. |

Uncertainty is relationship-specific. An object may be reviewed while its
attachment endpoint remains ambiguous. A relationship may be challenged
without reclassifying unrelated objects.

### Four meanings of containment

- **Visual containment:** a visible extent lies inside a drawn or apparent
  boundary.
- **Document-structural containment:** organization places an entry in a
  legend, cell in a table, or object in a page region.
- **Engineering containment:** a claim that an item belongs to a physical,
  functional, or electrical assembly.
- **Graph containment:** hierarchy or membership in accepted graph knowledge.

Page decomposition owns only the first two when source-visible and reviewed. A
fuse label inside a block is visually contained; whether the fuse is part of a
canonical fuse-block entity is extraction. A connector depiction in a region
is structurally contained; whether it belongs to a harness is not established.

### Multiple parents and overlap

The source pages are not strict trees. Use primary containment organization for
page, regions, legends, tables, entries, and blocks, supplemented by explicit
non-hierarchical relationships. An occurrence may participate in multiple
groups, overlap several regions, attach visibly to multiple objects, or be
referenced more than once when the evidence shows it. Exact cardinalities
belong to later schema work.

## Reading and traversal order

Keep linguistic reading order, table order, visual inspection order, circuit-
flow direction, document navigation order, and contributor review order
distinct.

Decomposition may record structural order supported by visible organization or
reviewed convention. A table may have ordered rows and columns and a legend an
ordered list. A circuit diagram may have no single valid order. Left-to-right
placement does not establish electrical flow. Japanese text orientation may
influence later reading without altering structural identity. Issue #30 owns
translation bindings and any required linguistic order.

## Composite, distributed, and repeated forms

The pilot supports treating composition as a review decision rather than
prescribing one geometry:

- A **composite object** has parts reviewed as one document occurrence: for
  example, a callout with label, leader, depiction, cavities, and qualifier.
  Its parts may also remain locatable instances.
- A **visual group** records grouping without claiming one object.
- A **structural relationship** connects independent instances.
- A **distributed occurrence** uses multiple extents when one occurrence is
  noncontiguous, such as a grid formed by distant row and column markers.
- A **repeated motif** records repeated presentation while each occurrence
  keeps its identity.

Other examples include a legend entry made of key, swatch, and label; a
connector depiction with separate cavity and identifier marks; a production
legend referring to distant qualifiers; and a path crossing blocks or regions.
Default to separate locatable instances plus explicit composition when that
makes review more granular. Use a distributed instance only when the source
supports one occurrence rather than similar separate occurrences.

## Stable structural identity

A stable identity identifies a source occurrence, not an engineering entity.
It must remain independent of translated and normalized wording; be scoped to
publication, verified artifact, page, and boundary; distinguish occurrences
sharing one printed identifier; survive ordinary class or location corrections
when the occurrence remains the same; avoid page label as the sole page
identity; and establish no cross-page or cross-publication equivalence.

Candidate inputs are publication ID, artifact fingerprint, PDF page, printed
page, page or boundary identity, and a locally assigned occurrence ID. This
document selects no syntax or namespace; the
[Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md) defines
conceptual roles, scopes, stability, and collision rules while likewise
deferring syntax and schema.

## Completeness and omission handling

Completeness is assessed against the controlling boundary, not the recorded
object list. Conceptually distinguish:

- complete page and complete declared-region coverage;
- partial decomposition;
- excluded regions or content;
- unreadable, clipped, damaged, or low-resolution content;
- observed but unclassified objects;
- classified objects with unresolved extent;
- unresolved relationships;
- visibly present but intentionally unrepresented content;
- non-factory capture or watermark marks; and
- content not detected during decomposition.

For each excluded or unresolved area, preserve a location, reason, and effect
on completeness. Source damage differs from contributor omission. Non-factory
marks are visible on the page surface and must be located or explicitly
excluded; they must not be treated as factory-authored content. No numeric
confidence score is recommended.

## Uncertainty and failure states

Candidate descriptive states include observed, provisionally classified,
reviewed, ambiguous class, ambiguous extent, ambiguous attachment, unreadable,
excluded, blocked, and not applicable. They are conceptual review results, not
a schema vocabulary selected here.

Track uncertainty separately for object existence, class, evidence location,
extent, containment, attachment, grouping, reading order, cross-reference, and
boundary completeness. A page summary must not erase local ambiguity.
Downstream layers preserve unresolved structural uncertainty where material.

Decomposition stops or narrows the affected object, association, region, or
boundary when ambiguous, unreadable, clipped, damaged, or otherwise
insufficient source evidence prevents choosing among materially different
structural representations. Such evidence problems include unclear linework,
symbols, cavity marks, leader endpoints, overlaps, path continuity, or region
boundaries. Source-language uncertainty is a structural blocker only when it
materially changes the decomposition.

An unreadable label may remain a locatable unreadable text occurrence when its
existence, extent, and structural associations remain supportable. Uncertainty
confined to later linguistic meaning, engineering interpretation, identity,
applicability, or graph topology is not by itself a structural blocker and
belongs to its downstream layer. Graph-extraction uncertainty likewise does
not retroactively make the source structure unreadable.

## Reviewability and reversible traceability

A reviewer must be able to locate every represented object; inspect its
proposed class and each relationship's visible basis; identify omissions and
unresolved areas; distinguish direct observation from publication-guidance
interpretation; challenge one relationship without rewriting unrelated
objects; and trace later translation or extraction to the source instance.

“Reversible” means reviewable correspondence to evidence. It does not mean
automatic regeneration, pixel-perfect reconstruction, or a required renderer.

## Pilot demonstrations

These demonstrations describe candidate composition; they do not create
decomposition records or rewrite the Milestone 7 translations.

### Printed page 2-3 — engine harness layout

The complete page surface is PDF page 15, printed page `2-3`, within the
verified publication artifact. Candidate composition includes:

- page heading and engine qualifier;
- framed diagram region and page-navigation grid;
- distributed row markers `A`-`D` and column markers `1`-`6`;
- right-side harness legend with ordered entries, uppercase and lowercase
  keys, labels, and color swatches;
- central subject depiction and colored harness-path depictions;
- perimeter connector callouts, source-local labels, connector depictions,
  cavity marks, brackets, production qualifiers, and leader lines;
- factory footer and publication marks; and
- a visible non-factory donation/capture watermark, classified as non-factory
  page-surface content.

Containment organizes regions, legend entries, callouts, depictions, and
cavities. Alignment organizes legend rows and grid markers. Attachment links
leaders to callouts and targets. Reference associates legend keys and swatches
with path styles under the reviewed convention. Grid, leaders, subject, and
paths overlap without becoming one object.

Legend key `A` is not grid row `A`. A harness-path depiction is not a conductor
or graph edge. A connector depiction is not a connector entity. Visible label
attachment does not establish canonical identity. A region is not a subgraph.

### Printed page 2-7 — instrument-panel harness layout

The complete page surface is PDF page 19, printed page `2-7`. Candidate
composition includes:

- heading with `1HZ`, `1PZ`, and source-visible left-side qualifier;
- instrument-panel diagram region and page grid;
- harness legend with case-sensitive keys, labels, and swatches;
- subject depiction and colored path depictions;
- connector groups, source-local labels, connector depictions, cavities,
  brackets, LH/RH and production-date qualifiers, and leader lines;
- factory footer and publication marks; and
- the visible non-factory watermark.

Containment relates entries to the legend and cavities to depictions. Grouping
captures bracketed connector sets. Attachment records leaders and qualifiers.
Alignment captures rows and callouts. Reference associates keys with path
styling. Overlap preserves the dense grid, leaders, paths, and subject drawing.

The heading's left-side qualifier scopes the visible occurrence; it does not
prove a separate canonical harness entity. Matching labels or similar connector
drawings do not establish identity.

### Printed page 3-2 — power-source circuit

The complete page surface is PDF page 40, printed page `3-2`. Candidate
composition includes:

- page heading and engine qualifiers;
- upper-right production legend;
- main circuit-diagram region;
- `R/B NO.1` relay-block and `F/B NO.1` fuse-block boundaries;
- relay and fuse symbols visibly contained in those blocks;
- ignition-switch, battery, alternator, and combination-meter depictions;
- combination-meter and charge-indicator labels;
- wire-color labels, circuit-path depictions, junction dots, terminal marks, connector
  depictions, cavities, and source-local identifiers;
- aligned lower connector strip; and
- factory marks plus the visible non-factory watermark.

Labels attach or sit adjacent to depictions. Symbols are visually contained in
blocks. Paths visibly meet at depicted dots; terminal marks attach to or sit
adjacent to symbols. The production legend references distant circle and square
qualifiers. Lower connector depictions align and group without becoming one
engineering assembly.

A path meeting at a dot is source-visible structure; electrical connectivity
remains a later candidate claim. Translated wording does not establish
engineering identity. Structural completeness does not establish graph
completeness.

## Page-local and publication-level structure

The page-local model can record headings, section marks, continuation markers,
cross-references, printed-page identifiers, margin motifs, and the visible
portion of a table or diagram. Reviewed continuations, multi-page tables, and
document-wide legend references require links among page decompositions. Such
links remain structural and do not assert engineering continuity.

Chapter and section hierarchy, page spreads, foldouts, cross-page identity,
page-number restarts, appendices, and document-wide legends require a future
publication-level design. Issue #27 creates no universal publication schema. A
follow-up may be justified after Issue #31 supplies broader evidence.

## Alternatives considered

### Strict hierarchy or tree

A tree offers simple traversal and natural containers for pages, regions,
tables, legends, entries, and blocks. It fails on overlap, labels and leaders,
distributed grids, multiple groups, paths crossing boundaries, and references.

### Flat object list with relationships

A flat list handles overlap, multiple associations, and distributed forms. It
makes navigation, bounded completeness review, and region/table traversal
harder and repeats basic containment context.

### Hybrid containment hierarchy plus structural relation graph

The hybrid uses an organizational hierarchy for page, regions, legends,
tables, entries, callouts, and blocks, while explicit relationships represent
attachment, grouping, overlap, alignment, reference, sequence, and
continuation. All three pilots require both aspects. This is the recommendation.

## Relationship to sibling issues and existing work

The [Page-to-Translation Binding Model](PAGE_TRANSLATION_BINDING_MODEL.md)
consumes the occurrence and region identities proposed here. It permits
occurrence, source-supported composite, explicit occurrence-set, and bounded
region targets while leaving decomposition valid when no translation exists.
Binding lifecycle does not redefine the structural relationships in this
document.

- Issue #28 defines semantic layers below linguistic and engineering meaning.
- Issue #34 defines the candidate object vocabulary; this document defines
  composition without redesigning it.
- Issue #29 owns identifier roles, scopes, preservation, stability, and
  collision handling; see the
  [Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md).
- Issue #30 owns translation bindings to page objects or regions.
- Issue #31 evaluates the model across publication families.
- Issue #32 owns the downstream contract into graph extraction.

The Milestone 7 translation records remain valid, review-ready, and unchanged.
They are not page decompositions, do not need to capture topology, and require
no migration here. Issue #30 may later recommend structural bindings without
changing their present review status.

One Diagram remains a valid vertical extraction pilot. Future extraction may
use reviewed decomposition as an additional input, but this investigation
changes no One Diagram candidate or accepted fact. Issue #32 owns that contract.

## Explicit non-goals

This recommendation does not:

- define JSON fields, schemas, records, fixtures, validators, or identifier
  syntax;
- decompose pilot pages into canonical data;
- migrate or characterize existing translation records as defective;
- define translation binding, publication-family sufficiency, or extraction
  rules owned by Issues #30-#32;
- create engineering entities, topology, nodes, edges, conductors, or facts;
- require OCR, rendering, pixel-perfect reconstruction, or committed source
  derivatives; or
- authorize implementation, dependencies, infrastructure, or publishing.

## Open questions

- What evidence distinguishes one composite occurrence from a group?
- When is a path one distributed instance versus several segments?
- Which region roles survive validation across other publication families?
- Which evidence-location forms are required in practice?
- How should identity survive reviewed instance splits or merges?
- Which page-local continuations can be linked before publication-level design?
- Does Issue #31 justify a publication-level follow-up investigation?

## Recommendation and next decision gate

Recommend one candidate decomposition per verified page surface or declared
bounded page surface, with:

- containment hierarchy for the page and organizational regions;
- object instances from the candidate taxonomy;
- explicit relationships for attachment, grouping, adjacency, overlap,
  alignment, reference, supported sequence, and continuation;
- flexible reviewed evidence locations;
- stable occurrence identities independent of wording and engineering entities;
- boundary-based completeness, explicit omissions, and granular uncertainty;
  and
- preserved evidence and review history with no engineering or graph promotion.

This conceptual model is ready for architectural review. Canonical artifact
shape and implementation remain blocked pending identifier taxonomy (#29),
translation binding (#30), publication-family evaluation (#31), and the graph-
extraction contract (#32).

No ADR is recommended yet. Defer an ADR until Issues #29-#32 establish whether
the candidate should become a canonical publication-representation artifact
and which parts require a durable architectural decision.
