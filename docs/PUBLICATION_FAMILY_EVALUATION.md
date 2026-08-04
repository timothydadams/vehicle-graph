# Publication Family Evaluation

## Purpose and scope

This report evaluates the publication-representation architecture developed by
Issues #27–#30 and #34 against the seven engineering-publication families named
by Issue #31. It asks whether the current concepts can preserve inspected,
source-visible organization before linguistic or engineering interpretation.

This is an architecture stress test, not a universal document model. It does
not create decomposition records, translation records, engineering claims,
graph facts, schemas, or implementation requirements. A result of insufficient
evidence is a valid result and is not converted into presumed support.

## Outcome vocabulary

Each family uses one of these outcomes:

- `supported as currently described` — inspected evidence fits the existing
  vocabulary and composition model without a family-specific extension;
- `supported with a publication-specific composition` — existing primitives
  and relationships work, but their composition has a source-supported role
  specific to that publication family;
- `supported provisionally` — inspected evidence supports the main design, but
  a material case remains untested or an existing distinction needs design;
- `architecture gap demonstrated` — inspected evidence cannot be represented
  faithfully by the concepts currently described;
- `publication-level question deferred` — the example exposes structure beyond
  a page, and the current milestone does not safely resolve it; and
- `insufficient evidence` — approved local evidence does not contain a suitable
  inspectable example.

## Evidence inventory

The evaluation used only committed catalogs and working records plus the two
already-authorized, ignored local PDFs they identify. Availability was verified
on 2026-08-03. Local paths are navigation aids, not publication provenance.

| Evidence | Directly inspectable | Locations used | Families supported |
| --- | --- | --- | --- |
| Toyota *Land Cruiser Electrical Wiring Diagram*, EWD168F, August 1992, Europe & General | yes, local PDF fingerprinted by the catalog; later pages visibly carry a third-party capture watermark | printed pp. 4–6, 84–85, 100–101, 165, 188–191; especially system-circuit spread and System Circuit Connectors (5) | circuit diagrams, connector views, tables, supporting layout comparison |
| Toyota `トヨタ ランドクルーザー70 配線図集`, source-labeled `品番 6742601`, January 1995 | yes, local PDF fingerprint matches the cataloged pilot artifact | PDF p. 15 / printed `2-3`; PDF p. 18 / `2-6`; PDF p. 19 / `2-7`; PDF p. 40 / `3-2`; PDF p. 80 / `5-2`; explanatory PDF pp. 6–10 | circuit diagrams, harness layouts, connector depictions, tables |
| Committed source catalogs and bounded work | yes, as repository records rather than substitutes for page inspection | `sources/toyota/**`; `work/translation/toyota-land-cruiser-70-jdm-1993-05/**`; `work/one-diagram/**` | source identity, page mapping, boundaries, interpretive dependencies, known limitations |

No approved evidence outside those electrical-wiring publications was found.
The catalogs identify each local artifact and constrain its use; they do not
expand the evidence boundary. Neither filename, publication family, nor page
metadata was used to infer unseen content.

The Japanese explanatory pages were located and reviewed as required source-
language dependencies before structural observations were made. Their language
review remains incomplete, so this report records only visible organization and
does not assign engineering meanings to untranslated marks. EWD168F's English
explanatory pp. 4–6 were likewise reviewed before its circuit and connector
conventions were considered.

## Evaluation method

For every example the reviewer:

1. identified the publication and exact PDF and printed-page coordinates where
   both were available;
2. confirmed that the source page itself was directly inspectable;
3. described visible marks, boundaries, text occurrences, and organization
   without converting them into engineering claims;
4. mapped visible material to candidate classes in the
   [Source Page Object Taxonomy](SOURCE_PAGE_OBJECT_TAXONOMY.md);
5. tested containment composition and material non-hierarchical relationships
   from [Page Decomposition](PAGE_DECOMPOSITION.md);
6. recorded printed identifier occurrences and apparent structural scope under
   the [Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md),
   without assigning engineering identity;
7. separated linguistic occurrences from graphical and structural content;
8. tested whether decomposition could proceed before translation;
9. recorded ambiguity, overlap, repeated form, distributed extent, and page-
   versus publication-level concerns;
10. tested semantic ownership, evidence traceability, completeness, omission
    handling, and downstream neutrality; and
11. classified shortcomings as evidence, vocabulary, decomposition, identifier,
    binding, publication-level, downstream-extraction, or implementation
    questions.

## Common criteria

The same questions governed every family:

- **Source visibility:** can each object be pointed to without deciding what
  engineering entity it means?
- **Composition:** can primitives and composites preserve material organization
  without a family-specific schema?
- **Relationships:** can containment, visible attachment, grouping, adjacency,
  overlap, alignment, reference, sequence, and continuation be recorded without
  asserting engineering topology?
- **Identity:** can structural occurrence identity remain separate from printed,
  engineering, and graph identity?
- **Traceability:** can every object and relationship cite a reviewable source
  extent?
- **Language independence:** can decomposition precede complete translation?
- **Linguistic binding:** can text artifacts bind to visible occurrences without
  owning structure?
- **Completeness:** can boundaries, exclusions, omissions, uncertainty, and
  undetected-content risk remain explicit?
- **Applicability:** can visible qualifiers remain occurrences rather than
  prematurely accepted vehicle applicability?
- **Multi-page behavior:** does the example require publication-level structure
  that page-local objects cannot safely settle?
- **Downstream neutrality:** is the result useful beyond graph extraction?

## Family evaluations

### 1. Circuit diagrams

**Evidence.** The Japanese publication's PDF p. 40 / printed `3-2` was inspected
with its explanatory PDF pp. 7–9 / printed `1-4` through `1-6`. EWD168F's
printed p. 191 system-circuit spread was inspected with its pp. 4–6 notation
guidance and p. 165 index context.

**Visible structure.** The examples contain diagram boundaries and regions,
graphical and component symbols, block boundaries, labels embedded in or near
symbols, circuit-path depictions and segments, junction dots, terminal marks,
wire-color text labels, fuse and relay depictions, connector depictions, notes,
qualifiers, grid-like location marks, and references. The EWD168F spread also
shows visually continued horizontal paths across several labeled system regions
and lower visible references to paths.

**Composition and identity.** A page or declared spread region contains diagram
regions, blocks, symbols, labels, and path depictions. Containment, visible
attachment, grouping, overlap, reference, sequence where visibly supported,
and continuation preserve the material structure. Two path extents may visibly
cross; their recorded extents and overlap preserve that geometry without adding
a `crossing` relationship. A path may have distributed segments; a block may be
composite. Printed labels and codes remain identifier occurrences with page- or
publication-local scope. Similar labels across the two publications do not
establish shared engineering identity.

**Language and bindings.** Graphical decomposition is useful before Japanese
translation. Text labels, notes, wire-color occurrences, and qualifiers can be
binding subjects later. Linguistic understanding may be required for reviewed
source-language or engineering interpretation, but English translation is not
required. Translation is one optional, reviewable linguistic representation
that may support downstream interpretation. Source transcription, direct
source-language understanding, literal translation, engineering normalization,
engineering interpretation, and graph extraction remain distinct.

**Limitations.** The EWD168F foldout-like spread demonstrates fuzzy page-versus-
spread boundaries and paths that cross regions. The current model can preserve
a declared evidence boundary and distributed object, but publication-wide
continuation resolution remains deferred. That does not prevent faithful
page-boundary representation.

**Outcome:** `supported with a publication-specific composition`.

Circuit paths remain source-visible objects, not accepted graph edges. A visible
junction may later support a connectivity candidate but accepts nothing.
Translated component wording does not establish canonical component identity.

### 2. Harness layouts

**Evidence.** Japanese PDF p. 15 / printed `2-3` and PDF p. 19 / printed `2-7`
were inspected with PDF p. 6 / printed `1-3`. PDF p. 18 / printed `2-6`
provided the visibly paired component-list context.

**Visible structure.** Both layout pages contain a page grid, row and column
identifiers, a large vehicle or panel subject illustration, colored harness-
path depictions, dense connector depictions and callouts around the perimeter,
leader lines, labels, a color legend, legend keys, headings, printed page
numbers, engine qualifiers, and publication/capture marks. Uppercase and
lowercase forms are visibly distinct and are preserved exactly.

**Composition and identity.** The subject illustration, route-like paths, and
callouts are overlapping composites rather than one tree. Paths cross grid and
region boundaries; leader lines visibly attach callouts containing labels or
connector depictions to locations. Legend keys, grid coordinates, connector
codes, and structural occurrence IDs require distinct roles even where characters
collide. `LH`, `RH`, engine, model, and production text must remain source-
visible qualifiers until interpreted and accepted downstream.

**Language and bindings.** The illustration, colored paths, grids, leaders, and
connector motifs remain decomposable before translation. The publication's own
`1-3` explanation is necessary before assigning meanings to those marks; unknown
meaning does not erase their visible form. Translation may bind to headings,
legends, and labels without owning their placement or visible attachment.

**Limitations.** The paired `2-6` list and `2-7` layout demonstrate a publication-
level correspondence that page-local proximity cannot resolve. The pages can be
represented independently, but a durable cross-page reference requires later
publication-level design and source-language review.

**Outcome:** `supported with a publication-specific composition`, with the
paired-list relationship a `publication-level question deferred`.

Harness paths are not individual conductor paths. Route-like appearance does
not establish accepted physical routing, and visible organization remains
useful without translation.

### 3. Connector views

**Evidence.** EWD168F printed pp. 188–190, headed System Circuit Connectors (5),
were inspected with p. 6 connector guidance and the bounded One Diagram source
inventory. Connector motifs on Japanese printed `2-3`, `2-7`, and `3-2` were
also inspected as comparison, not as proof of equivalence.

**Visible structure.** EWD168F shows table-like repeated cells containing parts
codes, component-label text, connector-body outlines, cavity divisions, cavity
characters or numbers, connector-color labels, location references, and
occasionally alternate motifs for the same printed parts code. Surrounding
headings, multilingual reference tables, blank cells, and capture watermarks are
also visible. Japanese pages show repeated connector-body and cavity motifs in
different compositions.

**Composition and identity.** A connector depiction is a composite containing a
body outline, cavities, terminal or cavity marks, and visibly attached labels.
It may sit within a table cell or callout. Decomposition is preferable where a
mark's extent and independent review matter; the composite remains useful as a
parent.
Cavity numbers are visible text/identifier occurrences contained by or visibly
attached to cavity depictions. Their later role as terminal or cavity
engineering identifiers is not decided here. View orientation must be
represented only when an orientation
mark or qualifier is visible; geometry alone cannot supply it.

**Language and bindings.** Body geometry, cavity partitions, and repeated motifs
do not require translation. Labels and view-side qualifiers, where visibly
present, can receive linguistic bindings. The absence of a translated qualifier
must not be filled from generic connector convention.

**Limitations.** Similar drawings, repeated parts codes, and similar cavity
geometry do not establish identity within or across publications. No inspected
example proves a general orientation vocabulary beyond visible marks and text.

**Outcome:** `supported with a publication-specific composition`.

A connector drawing remains distinct from a connector entity, and this report
does not solve connector equivalence.

### 4. Tables

**Evidence.** Japanese PDF p. 80 / printed `5-2` (component-name index), PDF
p. 18 / printed `2-6` (layout component list), and EWD168F System Circuit
Connectors (5) tables were inspected. Japanese PDF p. 10 / printed `1-7` was
reviewed as the publication-defined explanation for index fields.

**Visible structure.** The examples show table boundaries, headings, columns,
header and body cells, repeated side-by-side column groups, blank cells,
qualifier text, identifier occurrences, page/location references, connector
drawings embedded in cells, and multilingual reference rows. Geometric reading
order is not always sufficient: the Japanese `5-2` page has two major vertical
groups, while the connector tables repeat composite entries down columns.

**Concrete composition test.** On Japanese printed `5-2`, one body cell in the
left major column group can be recorded as a stable table-cell occurrence with
its own visible extent. The table, horizontal row occurrence, vertical column
occurrence, and cell occurrence are separately typed and locatable. The cell is
document-structurally contained by the table; grouping and alignment relate it
to the typed row and column occurrences; and sequence preserves the visibly
supported order of rows and columns. The same cell may participate in both
groups because Issue #27 expressly permits multiple group participation. A
printed code or page reference inside the cell remains a separate contained
identifier occurrence rather than row identity or engineering identity.

This composition preserves the visible row and column roles through typed
relationship endpoints without new `row-membership` or `column-membership`
relationship types. Exact representation and cardinality remain implementation
questions. A future schema may add convenience relations without making them
architectural prerequisites. Header scope remains provisional: the inspected
examples support header-cell occurrences, alignment, grouping, and sequence,
but do not demonstrate that every apparent spanning or inherited header has a
reliably source-visible scope beyond those cues. Visible ditto or inheritance
marks, if encountered, would remain text occurrences with only the grouping,
alignment, reference, or sequence supported by the source; none was relied on
in these examples.

**Language and bindings.** Cell boundaries and order can be represented before
translation. Text may bind per occurrence or at a declared group where the
binding model's coverage rules are satisfied. Blank cells remain visible
structure, not missing translations.

**Outcome:** `supported with a publication-specific composition`; header scope
remains `supported provisionally` where the visible cue is incomplete.

Visible tabular organization, an interpreted record structure, and extracted
engineering facts are three separate stages. A row is not automatically a
record or claim.

### 5. Specifications

**Evidence available.** The inspected publications contain tables and labeled
electrical values within diagrams, but the approved bounded evidence does not
provide a suitable specification page whose governing role can be established
without inference.

**Missing evidence.** No directly inspectable bounded example was identified
that tests property labels, values, units, tolerances, conditions, variants,
exceptions, footnotes, repeated measurement patterns, or multi-page
specification continuation as a specification family.

**Unproven conclusion.** It remains unproven that separate value and unit
occurrences, visible grouping or attachment without property normalization,
conditions, and prose-versus-table specification compositions are sufficient across real
specification pages. Existing text, qualifier, table, and relationship concepts
are plausible candidates, not validation.

**Outcome:** `insufficient evidence`.

Issue #32 may proceed with limited demonstrated coverage. Its contract may
define general evidence-preservation and review invariants, but it must keep
those separate from family-specific inputs demonstrated only by the inspected
circuit, harness-layout, connector-view, and table pages. Specifications remain
unvalidated, and no extraction capability for them is authorized.
A future bounded factory specification page with values, units, ranges,
tolerances, conditions, variants, and footnotes would be useful.

### 6. Maintenance procedures

**Evidence available.** The approved publications include explanatory prose and
notes about reading diagrams, but those are not maintenance procedures and must
not be repurposed as procedural evidence.

**Missing evidence.** No directly inspectable bounded example tests ordered
steps, prerequisites, warnings scoped across steps, tool and part references,
figures, acceptance criteria, branches, optional instructions, or procedure-
level continuation.

**Unproven conclusion.** Page-local sequence and text-to-figure reference or
visible attachment are conceptually representable, but procedure-level scope,
shared warnings, and branching remain unvalidated publication-level questions.

**Outcome:** `insufficient evidence`.

Issue #32 may proceed with limited demonstrated coverage, but maintenance
procedures remain unvalidated and no extraction capability for them is
authorized. Its general contract must distinguish evidence-role and review
invariants from untested procedure inputs. Issue #32 does not define a procedure
execution model, but that fact does not narrow its architectural ownership to
circuits. Future evidence should include a bounded, authorized factory
procedure with at least one warning, ordered steps, a referenced figure, and a
conditional or continued step.

### 7. Exploded diagrams

**Evidence available.** The publications contain subject illustrations,
connector drawings, and circuit symbols, but no bounded example is established
as an exploded view or parts diagram.

**Missing evidence.** No directly inspectable example tests depicted parts,
balloons, item numbers, leaders, quantity tables, assembly grouping, insets,
variants, or repeated views.

**Unproven conclusion.** Existing illustration, leader, label, table, group, and
relationship concepts are plausible, but balloon-to-depiction visible
attachment or reference and parts-table composition have not been validated.
Spatial separation must not be presumed to encode assembly relationships.

**Outcome:** `insufficient evidence`.

Issue #32 may proceed with limited demonstrated coverage, but exploded diagrams
remain unvalidated and no extraction capability for them is authorized. Its
general contract must distinguish evidence-role and review invariants from
untested exploded-diagram inputs. Future bounded evidence should pair an
exploded illustration with balloons, leaders, and its parts table.

## Cross-family findings

### Common structural concepts

Inspected evidence supports reuse of page or declared boundary, region,
heading, text occurrence, label, qualifier, note, legend and entry, table and
cell, graphical depiction, path depiction and segment, leader line, visible
boundary, visible attachment, grouping, and reference, publication or
capture mark, and printed identifier occurrence. Stable repository structural
identity and locatable evidence extents are supported across four inspected
page families within two Toyota EWD publications in one broad electrical-wiring
publication domain.

These are reusable because reviewers can point to them before deciding their
engineering meaning. Reuse does not imply identical downstream semantics.

### Publication-specific variants

- circuit-path depiction: a specialized visible path role, not a graph edge;
- harness-path depiction: a specialized visible path role, not a conductor or
  accepted physical route;
- connector cavity and terminal mark: source-visible children of a connector
  depiction whose engineering identity remains downstream;
- page grid and legend key: distinct navigation roles despite visual similarity
  to other short codes;
- table header/body, row, column, and cell roles: visible organizational roles
  preserved through typed occurrences, grouping, alignment, and sequence;
- specification value, procedure step, and parts balloon: proposed specialized
  roles that remain unsupported until evidence exists.

A similar line, enclosure, short code, or repeated motif is not enough to share
a specialized role. Engineering meaning belongs downstream.

## Stress test of prior concepts

| Prior concept | Finding |
| --- | --- |
| Semantic ownership (#28) | Supported: source-visible structure remained useful in Japanese and English without promotion into engineering identity, translation, or graph facts. |
| Page-object vocabulary (#34) | Supported across four inspected page families within two Toyota EWD publications; proposed specification, procedure, and exploded-view roles remain unvalidated. |
| Composition and hierarchy (#27) | Supported by containment plus explicit relationships; a table cell can participate in typed row and column groups without requiring a strict tree. |
| Structural relationships (#27) | Containment, visible attachment, grouping, adjacency, overlap, alignment, reference, sequence, and continuation are sufficient for the inspected examples. Geometric path crossings are preserved by extents and overlap, not a new relationship type. |
| Structural identity (#27) | Supported: repeated motifs and identical printed values still require distinct occurrence identity. |
| Identifier classification (#29) | Supported: grid coordinates, legend keys, parts codes, cavity marks, page references, and structural IDs remain distinct. |
| Translation bindings (#30) | Supported: linguistic occurrences can bind without owning diagrams, tables, or graphical objects; blank cells and graphical marks need no translation. |
| Coverage and omission handling (#27/#30) | Supported conceptually for bounded pages; untested families must be declared absent rather than counted as covered. |
| Evidence traceability | Supported: every observation can cite a publication coordinate and locatable extent; local filenames alone are insufficient. |
| Page-local versus publication-level scope | Partly supported: paired lists/layouts and spread continuations expose deferred cross-page composition, but page-local decomposition remains coherent. |

No inspected finding contradicts the semantic layers, identifier separation, or
translation-binding direction. Foundational documents are therefore not
rewritten in this evaluation PR. Table convenience relations, exact
cardinalities, and incompletely cued header scope remain implementation or
provisional questions rather than demonstrated architecture gaps.

## Hard cases

### Inspected

- labels and numerous leader lines overlap on Japanese `2-3` and `2-7`;
- one dense layout region contains paths crossing several grid cells and visual
  groups;
- reading order on Japanese `5-2` differs from a simple geometric scan because
  major column groups repeat;
- labels are embedded inside circuit and connector symbols;
- identical or similar connector motifs recur without proven shared identity;
- EWD168F's wide system-circuit material has paths and references crossing
  multiple labeled regions;
- tables embed graphical connector depictions inside cells;
- capture watermarks overlap source content and must remain capture marks rather
  than factory publication objects;
- the Japanese `2-6`/`2-7` correspondence is distributed across pages;
- some visible extents are fuzzy or crowded enough that decomposition would
  need uncertainty and undetected-content risk.

### Conceptual only; not tested

Multi-page specification tables, procedure branches, warnings spanning several
steps, exploded-view balloons, photographs with annotations, foldout coordinate
normalization, duplicated item numbers in separate parts-table scopes, charts,
equations, maps, and revision markup were not tested. They remain deferred and
must not be cited as supported outcomes.

## Evidence gaps

| Family | Available | Missing | Unproven conclusion | Issue #32 impact | Useful future bounded evidence |
| --- | --- | --- | --- | --- | --- |
| Specifications | diagram labels and general tables only | controlling specification page and conventions | value/unit/condition/tolerance and prose/table compositions | may proceed with general invariants separated from unvalidated inputs; no capability authorized | one specification table plus prose specification with variants and footnotes |
| Maintenance procedures | explanatory prose, not a procedure | steps, warnings, figures, branches, continuation | sequence, shared scope, and procedure-level structure | may proceed with general invariants separated from unvalidated inputs; no capability authorized | one bounded procedure with warning, figure, branch, and acceptance criterion |
| Exploded diagrams | illustrations and connector drawings, not exploded views | balloons, parts table, quantities, assembly groups | depiction/balloon/table composition and scope | may proceed with general invariants separated from unvalidated inputs; no capability authorized | one exploded figure and its paired parts table |
| Multi-page structures generally | one paired list/layout and wide circuit material | a fully reviewed continuation or spanning table | publication-level identity, sequence, and completeness | distinguish general invariants from untested inputs | one bounded continued diagram or table with publication-defined continuation rules |

## Implications for the architecture

The evidence supports the architecture's central separation: publication
representation can preserve visible structure independently of English,
translation, engineering identity, and graph acceptance. The hybrid containment
plus relationship model handles diagrams and layouts better than either a strict
tree or a flat list. The identifier taxonomy prevents repeated short codes from
collapsing into identity. Translation bindings remain optional and directional.

The concrete table retest demonstrates no missing structural relationship.
Typed row, column, and cell occurrences plus containment, grouping, alignment,
and sequence preserve the inspected organization. Exact cardinalities,
convenience relations, fields, and storage remain implementation questions;
header scope remains provisional when no reliable source-visible cue establishes
it.

Publication-level composition remains a design boundary, not a demonstrated
failure of page decomposition. Paired pages and wide spreads can be represented
locally while their durable cross-page relationship remains explicit and
unresolved.

## Readiness for Issue #32

**Recommendation: ready with documented limitations.**

Issue #32 may begin after this evaluation is reviewed because the corrected
analysis supports investigation of general evidence-role separation, provenance
retention, optional linguistic dependencies, candidate-versus-accepted claims,
review boundaries, applicability preservation, and ambiguity propagation. The
table retest found no missing architectural relationship; exact representation
and cardinality are implementation questions.

Issue #32 remains a general downstream-contract investigation, not a circuit-
only investigation. Its demonstrated family coverage is limited to four page
families within two Toyota EWD publications. It must distinguish general
architectural invariants, demonstrated family-specific inputs, and untested
future inputs; must not claim that specifications, procedures, exploded
diagrams, or general multi-page structures are validated; and authorizes no
extraction capability for those families. It must preserve distinct primary
evidence, interpretive dependencies, optional linguistic artifacts,
applicability evidence, and candidate engineering interpretation. It remains
responsible for defining the handoff; this report defines no inputs, graph
schema, node or edge types, acceptance automation, or canonical fields.

## Recommendations

### Required before Issue #32

None. No demonstrated defect makes the extraction-boundary investigation unsafe
or incoherent.

### Recommended before implementation

- decide implementation representation and cardinality for table compositions
  without treating convenience relations as architectural prerequisites;
- decide how publication-level compositions reference page-local occurrences
  without replacing their structural identity;
- require evidence-bound declarations for spread/foldout boundaries and
  coordinate systems;
- retain explicit decomposition coverage, omission, uncertainty, and
  undetected-content risk for dense pages.

### Deferred until evidence exists

- specification value/unit/condition compositions;
- maintenance-procedure sequence, shared warning scope, and branching;
- exploded-view balloon, depiction, and parts-table composition;
- generic multi-page table and diagram continuation;
- photographs, charts, plots, equations, maps, and revision markup.

### Consumer-specific

- graph connectivity and engineering entity resolution belong to extraction;
- translated terminology and acceptance belong to linguistic interpretation;
- search indexing, accessibility reading order, rendering fidelity, and revision
  comparison belong to their consumers unless shared evidence later proves a
  representation requirement.

## Deferred questions

- Should a future schema add convenience relations for table composition, or
  use typed row/column endpoints with grouping and alignment directly?
- What publication-level object, if any, should connect page-local occurrences
  across a spread, continuation, or paired list and layout?
- When a visible label applies to several depictions, are multiple visible
  attachments sufficient, or is an explicit scoped group required?
- Which orientation concepts are source-visible across connector publication
  families rather than conventions inferred by a reader?
- What completeness declaration is adequate for extremely dense or partially
  obscured pages?

## ADR recommendation

Defer any new ADR until Issue #32 defines the downstream extraction contract and
the epic's combined findings can be evaluated together. The table retest found
no independent decision that changes a project invariant or requires an ADR
before the extraction-boundary investigation.

## Explicit non-goals

This evaluation does not translate or decompose a publication; build a
universal document model; add or commit factory evidence; create schemas,
canonical decomposition or translation records, graph candidates, graph facts,
or topology; modify pilot records; establish connector or depicted-part
identity; implement OCR, computer vision, translation, rendering, search, or
accessibility; define Issue #32's extraction contract; or retarget work to
`main`.
