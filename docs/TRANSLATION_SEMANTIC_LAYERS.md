# Translation Semantic Layers and Artifact Ownership

## Purpose and scope

This document defines the semantic boundaries between original-language
factory evidence, reviewed translation work, graph knowledge, and generated
English outputs. It assigns ownership, authority, provenance, transformations,
review gates, and uncertainty to each layer.

The layers are a semantic contract, not a proposed directory layout, JSON
schema, state machine, or implementation plan. Existing artifacts may carry
information from more than one layer while preserving these distinctions.
Later investigations may propose artifacts and bindings, but must not collapse
the meanings defined here.

This contract specializes the repository's broader source, extraction,
accepted-knowledge, and derived-view boundaries. It is demonstrated with the
Milestone 7 records for printed pages `2-3`, `2-7`, and `3-2`. Those records
remain valid and unchanged.

## Layer diagram

```text
1. Factory evidence
        v
2. Source-visible structure
        v
3. Linguistic translation
        v
4. Engineering normalization
        v
5. Graph extraction / candidate claims
        v
6. Accepted knowledge graph
        v
7. Derived presentation and publishing
```

Arrows mean that a downstream layer may consume reviewed upstream material.
They do not mean automatic promotion, acceptance, or replacement. Graph
extraction may consult source structure, translation, and normalization
directly. Every derived layer retains provenance to original evidence.

## Primary audit view

| Layer | Owns | Artifact and evidence status | Review gate | May reference | Must not assert |
| --- | --- | --- | --- | --- | --- |
| Factory evidence | Publication artifact, page image, fingerprint, publication and page coordinates | Preserved evidence plus committed identity and inventory | Artifact and source-location verification | Publication metadata and capture context | Translation, engineering identity, or topology |
| Source-visible structure | Regions, text objects, symbols, labels, layout, paths, depicted joins, and source-local notation | Candidate decomposition; implementation undecided; direct source observation | Location and publication-convention review | Factory evidence and material interpretive dependencies | Canonical entities, inferred connectivity, or identifier equivalence |
| Linguistic translation | Original-language transcription and literal English | Existing translation record or candidate translation unit; derived interpretation | Source-language and qualified human language-fidelity review | Visible text or region and primary evidence | Normalization, component identity, topology, or widened scope |
| Engineering normalization | Explicit engineering terminology that retains source and literal wording | Candidate normalized wording; derived interpretation | Terminology and applicability review | Reviewed translation and separately identified terminology evidence | Silent qualifier removal, equivalence, or graph facts |
| Graph extraction / candidate claims | Candidate entities, relationships, applicability, evidence roles, and claim-specific ambiguity | Candidate artifact; exact shape undecided | Extraction and independent graph review | Evidence, structure, translation aid, normalization, and dependencies | Acceptance, factory-authored English, or unsupported topology |
| Accepted knowledge graph | Explicitly accepted nodes, edges, facts, provenance, applicability, and supersession | Canonical graph JSON; schema undecided | Human-controlled canonical acceptance after independent review | Exact reviewed candidates and retained evidence | Silent mutation, unreviewed inference, or view authority |
| Derived presentation and publishing | Rendered pages, PDFs, diagrams, indexes, search structures, and disclosures | Generated noncanonical output | Publishing QA | Accepted upstream artifacts and disclosed provisional material | Factory evidence, factory authorship, canonical state, or new facts |

## 1. Factory evidence

- **Purpose:** preserve the artifact against which every later observation and
  claim can be audited.
- **Owns:** the source PDF or other publication artifact; faithful page images;
  artifact fingerprint; publication identity; PDF-page and printed-page
  coordinates; edition, date, source-stated scope, and capture limitations.
- **Does not own:** transcription, translation, normalized terms, page-object
  classes, engineering entities, graph facts, or English editions.
- **Input and output:** consumes a lawfully obtained factory publication and
  produces preserved evidence plus a committed identity and inventory. The
  private artifact need not be committed for its binding to be reviewable.
- **Provenance:** artifact identity and fingerprint remain bound to exact source
  locations; captures disclose their relationship to the original.
- **Allowed transformations:** verification, fingerprinting, faithful capture,
  page mapping, and recording source-stated identity or scope.
- **Forbidden transformations:** translation, interpretation of visual
  relationships, engineering identification, inferred applicability, or
  presenting repository output as the factory artifact.
- **Claims emitted:** evidence-identity and location claims, such as the mapping
  between a PDF page and a printed page.
- **Review or acceptance gate:** artifact verification and source-location
  verification.
- **Uncertainty handling:** uncertain identity, mapping, damage, or legibility
  remains explicit and blocks only affected later work.
- **Mutability:** preserved evidence is immutable. Corrections to committed
  identity records preserve review history rather than silently rebinding work.

## 2. Source-visible structure

- **Purpose:** describe what is visibly placed on a page without turning it into
  translated prose or engineering topology.
- **Owns:** candidate visible-region and object identity; page layout and
  hierarchy; text occurrences; graphical symbols; visible label attachment;
  legend keys; page-grid coordinates; connector depictions and identifiers;
  terminal marks and cavity numbers; wire-color labels; conductor paths;
  junction dots; leader lines; visible grouping; and exact case, punctuation,
  placement, and source-local marks. A line or dot is a depiction here, not yet
  accepted electrical connectivity.
- **Does not own:** literal English, normalized Toyota terminology, canonical
  connector or component identity, inferred connectivity, candidate entities,
  or accepted graph facts.
- **Input and output:** consumes factory evidence and the publication's notation
  guidance; may produce a candidate page decomposition. Canonical status,
  taxonomy, hierarchy, and geometry remain open.
- **Provenance:** every object remains locatable in the fingerprinted artifact.
  Same-publication guidance is attached only when materially required to read
  that object.
- **Allowed transformations:** segment, order, group, and describe visible
  content; preserve coordinates and hierarchy; transcribe source marks; bind a
  visibly attached label under the publication's convention.
- **Forbidden transformations:** infer topology from proximity; treat a legend
  key as an entity ID; equate repeated identifiers; turn a depiction into a
  canonical entity; or assign an unseen engineering role.
- **Claims emitted:** direct observations, such as “lower-case `k` appears” or
  “this path has a depicted junction dot.”
- **Review or acceptance gate:** source-location verification plus review of
  every materially used publication convention.
- **Uncertainty handling:** uncertain object boundaries, label associations,
  case, legibility, joins, or coordinates remain structural ambiguities. A hard
  issue blocks only the structure it prevents recording faithfully.
- **Mutability:** reviewable derived work unless a later decision defines a
  canonical structural artifact.

## 3. Linguistic translation

- **Purpose:** preserve visible original-language text and provide the closest
  supportable English wording without importing engineering normalization.
- **Owns:** Japanese source transcription, literal English, translation-unit
  coverage, language and grammar questions, and separate source-reading and
  literal-translation review states.
- **Does not own:** page geometry except through a structural binding;
  normalized Toyota terminology; canonical identifiers; engineering entities;
  connectivity; or graph acceptance.
- **Input and output:** consumes a visible text object or bounded region plus
  primary evidence; produces a translation unit or current page record. Binding
  granularity remains for Issue #30.
- **Provenance:** retains original text, publication identity, location,
  fingerprint, qualifiers, identifiers, review history, and lower-layer
  ambiguity. The original location remains primary evidence.
- **Allowed transformations:** exact transcription; literal English;
  disclosed reordering required by English; explicit alternate readings.
- **Forbidden transformations:** derive connectivity from proximity; silently
  normalize; erase case, qualifiers, or identifiers; claim human verification
  from machine agreement; or establish entity identity or broader scope.
- **Claims emitted:** transcription claims and provisional or reviewed
  language-equivalence claims. Translating `コンビネーションメーター` as
  provisional “Combination meter” does not identify a component node.
- **Review or acceptance gate:** source-location and source-language review,
  then qualified human language-fidelity review before full acceptance. The
  pilot does not claim that qualified human review occurred.
- **Uncertainty handling:** unreadable characters and ambiguous grammar attach
  to affected units. Materially different readings block that boundary.
- **Mutability:** translation records are canonical for their implemented
  reviewed-translation artifact role, but are reviewable derived
  representations rather than factory facts.

## 4. Engineering normalization

- **Purpose:** express source-supported concepts in consistent engineering
  terminology while retaining source transcription and literal English.
- **Owns:** proposed or reviewed normalized wording, terminology evidence and
  scope, terminology-review state, and uncertainty about a terminology choice.
- **Does not own:** source wording, canonical component identity,
  cross-publication equivalence, topology, candidate graph claims, or accepted
  knowledge.
- **Input and output:** consumes transcription and reviewed or explicitly
  provisional translation, with separately identified terminology evidence;
  produces candidate normalized wording. Terminology-store shape and scope
  remain open.
- **Provenance:** retains original and literal wording, terminology-source
  identity and applicability, rationale, review history, qualifiers, and
  ambiguity.
- **Allowed transformations:** choose a documented engineering term, reorder for
  engineering clarity, and record a scoped terminology mapping.
- **Forbidden transformations:** silently replace prior wording; suppress
  qualifiers; transfer applicability; use matching words to prove identity;
  resolve structural ambiguity; or emit topology.
- **Claims emitted:** scoped terminology claims, not component-identity or
  relationship claims.
- **Review or acceptance gate:** engineering-terminology and applicability
  review, separate from language-fidelity review.
- **Uncertainty handling:** a normalized term may remain absent or provisional
  without changing transcription or literal translation.
- **Mutability:** reviewable derived work; no pilot terminology is accepted by
  this investigation.

## 5. Graph extraction / candidate claims

- **Purpose:** convert source-supported observations into the smallest
  independently reviewable engineering claims without asserting canonical
  truth.
- **Owns:** candidate entities and relationships; components, terminals,
  conductor segments, junctions, connectors, harnesses, and locations;
  inferred electrical connectivity; candidate applicability; evidence-role
  assignments; claim-specific ambiguity; and extraction status.
- **Does not own:** factory evidence, translation acceptance, accepted nodes or
  edges, silent equivalence, or publishing state.
- **Input and output:** consumes original evidence, source structure, reviewed
  translation aids, useful normalization, and material interpretive
  dependencies; produces candidate claims in an artifact deferred to Issue #32.
- **Provenance:** cites original publication primary evidence, dependencies,
  translation aids, and supporting evidence in distinct roles; retains explicit
  applicability and only ambiguities that could change that candidate.
- **Allowed transformations:** propose entities; infer relationships from
  reviewed depictions and conventions; combine evidence explicitly; and record
  a derived claim as derived.
- **Forbidden transformations:** use an English rendering as primary evidence;
  treat proximity as accepted topology; accept its own claims; infer identity
  from repeated cross-publication identifiers; broaden scope; or propagate
  ambiguity by object association.
- **Claims emitted:** candidate engineering claims. A source-visible line and a
  proposed electrical connection remain distinct statements.
- **Review or acceptance gate:** extraction review followed by independent graph
  review against frozen evidence. Favorable review is not acceptance.
- **Uncertainty handling:** endpoint, identity, applicability, and connectivity
  uncertainty attaches only to candidates it could change. A hard issue blocks
  the affected candidate; faithful unresolved candidates may be reviewed.
- **Mutability:** mutable candidate work, frozen by revision for review.

## 6. Accepted knowledge graph

- **Purpose:** preserve engineering facts that passed independent review and an
  explicit canonical-acceptance decision.
- **Owns:** accepted nodes, edges, facts, provenance, applicability, retained
  ambiguity, review and acceptance history, and explicit supersession.
- **Does not own:** evidence, source layout, translation as factory authorship,
  unreviewed candidates, or presentation choices.
- **Input and output:** consumes exact independently reviewed candidates and an
  acceptance record; produces canonical graph JSON. Schema, identifiers, and
  layout remain undecided.
- **Provenance:** keeps original evidence reachable and translation,
  normalization, applicability, ambiguity, findings, and acceptance distinct.
- **Allowed transformations:** identify accepted facts; link them; explicitly
  supersede, correct, or qualify prior knowledge.
- **Forbidden transformations:** silent mutation; dropping prior
  representations; accepting translation as a graph fact; erasing ambiguity;
  or letting a tool or renderer define truth.
- **Claims emitted:** accepted graph facts with explicit scope. Acceptance does
  not imply infallibility or universal applicability.
- **Review or acceptance gate:** independent review plus a separate,
  human-controlled acceptance act. Qualified reviewers may not yet exist for
  every future claim.
- **Uncertainty handling:** accepted facts may retain acknowledged non-blocking
  ambiguity.
- **Mutability:** immutable in meaning; correction or narrowing creates explicit
  superseding knowledge.

## 7. Derived presentation and publishing

- **Purpose:** make accepted knowledge and reviewed translation material
  accessible without creating a competing source of truth.
- **Owns:** rendered English pages, companion PDFs, annotated diagrams,
  searchable indexes, databases, interfaces, layout and styling, generation
  metadata, and provisional-status disclosures.
- **Does not own:** factory evidence or authorship, translation or graph
  acceptance, canonical facts, or new applicability conclusions.
- **Input and output:** consumes accepted upstream artifacts and may include
  unresolved material only when visibly provisional; produces reproducible,
  noncanonical views.
- **Provenance:** retains publication identity, upstream artifact and review
  state, applicability context, and references sufficient to reach evidence and
  accepted facts.
- **Allowed transformations:** reformat, annotate, index, filter, arrange,
  highlight, and render accepted content; disclose provisional content.
- **Forbidden transformations:** become primary evidence; imply Toyota
  authorship; hide uncertainty; create facts through layout; widen scope; or
  become canonical because it is polished or searchable.
- **Claims emitted:** presentation and generation claims. Displayed engineering
  statements retain upstream authority.
- **Review or acceptance gate:** publishing QA for source correlation,
  disclosure, coverage, links, and accurate upstream status.
- **Uncertainty handling:** provisional material must be conspicuously labeled;
  otherwise an ambiguity that makes a view misleading blocks that portion.
- **Mutability:** freely regenerable derived output.

## Information ownership details

| Information | Owning layer | Boundary note |
| --- | --- | --- |
| Source PDF and page image | Factory evidence | A page image is evidence only when faithfully bound to the artifact |
| Artifact fingerprint | Factory evidence | Binds downstream locations to reviewed evidence |
| PDF and printed page coordinates | Factory evidence | Structure references but does not redefine the mapping |
| Source-visible region identity | Source-visible structure | Artifact form and canonical status remain open |
| Japanese transcription | Linguistic translation | Bound to visible text or a bounded region |
| Literal English | Linguistic translation | Never silently normalized |
| Normalized Toyota terminology | Engineering normalization | Requires scoped evidence and review |
| Page layout and hierarchy | Source-visible structure | Issue #27 defines decomposition details |
| Symbols and visible label attachment | Source-visible structure | Translation owns wording; extraction owns engineering claims |
| Legend keys and page-grid coordinates | Source-visible structure | Neither is automatically an entity ID or topology |
| Connector depictions and identifiers | Source-visible structure | Identifier classes are deferred to Issue #29 |
| Terminal labels and cavity numbers | Source-visible structure | Preserve marks before endpoint claims |
| Wire-color labels and conductor paths | Source-visible structure | Words may be translated; a path is not automatically an edge |
| Inferred electrical connectivity | Graph extraction | Accepted only after independent review and acceptance |
| Applicability qualifiers | Layer where stated | Every later claim must retain source scope without widening it |
| Candidate entities and relationships | Graph extraction | Intermediate shape is deferred |
| Accepted nodes and edges | Accepted knowledge graph | Canonical only after explicit acceptance |
| Ambiguity records | Narrowest affected layer | Storage may be shared; ownership follows what could change |
| Review status | Layer reviewed | Never promotes another layer automatically |
| Rendered English page and PDF | Publishing | Noncanonical and not factory-authored |
| Searchable indexes | Publishing | Reproducible projections |

## Cross-layer reference model

References have distinct meanings:

- A **provenance reference** traces a derived artifact or claim to evidence and
  prior representations.
- A **structural binding** connects a translation or later record to a visible
  object or region without claiming engineering identity.
- An **interpretive dependency** points to a same-publication location defining
  a convention materially required to read primary evidence.
- **Candidate-claim support** identifies primary evidence, translation aids,
  normalization, dependencies, and supporting evidence for one candidate while
  preserving each role.
- An **accepted graph reference** points to accepted knowledge and its history;
  it never turns a lower-layer object into a graph entity.

Allowed references include a translation unit binding to a visible text
object; normalization citing reviewed or explicitly provisional translation;
extraction citing structure, translation, normalization, and evidence in their
actual roles; accepted facts retaining all provenance; and publishing views
referencing accepted upstream artifacts and review states.

Forbidden references and promotions include:

- translation using visual proximity to assert connectivity;
- source structure asserting canonical connector or component identity;
- extraction treating translation or English rendering as primary evidence;
- publishing output becoming factory evidence or canonical knowledge;
- repeated identifiers across publications establishing equivalence;
- normalization silently erasing qualifiers or ambiguity;
- page layout becoming topology without an explicit candidate and review; and
- status at one layer becoming acceptance at another.

## Claim authority and semantic promotion

Authority categories are: **factory evidence**, **direct source observation**,
**source transcription**, **provisional or reviewed translation**, **normalized
engineering terminology**, **candidate engineering claim**, **accepted graph
fact**, and **derived presentation**. English wording or attractive rendering
does not increase authority.

```text
observed -> transcribed -> translated -> normalized
         -> extracted as a candidate claim -> independently reviewed
         -> accepted as a graph fact -> rendered as a derived view
```

These are not automatic transitions, and not every claim needs a populated
artifact at every stage. Each promotion is an explicit representation or
review outcome. It preserves original evidence, prior representation, review
history, ambiguity, applicability, and source-publication identity. A higher
layer never silently replaces lower-layer content.

## Review and acceptance gates

| Review | Applies to | Establishes | Does not establish |
| --- | --- | --- | --- |
| Artifact verification | Factory evidence | Artifact identity and fingerprint | Content meaning |
| Source-location verification | Evidence and structure | Correct page and visible location | Translation or identity |
| Source-language review | Structure and translation | Material publication conventions were found and applied | Human language fidelity by itself |
| Qualified human language-fidelity review | Transcription and literal English | Human-qualified fidelity for stated scope | Normalization or graph truth |
| Engineering-terminology review | Normalization | Scoped normalized wording | Entity identity or topology |
| Applicability review | Any scoped claim | No broader scope than evidence supports | Universal applicability |
| Extraction review | Candidates | Claim discipline and evidence roles | Independence or acceptance |
| Independent graph review | Frozen candidates | Independent evidence-to-claim review | Canonical acceptance |
| Canonical acceptance | Accepted graph | Exact reviewed claims become canonical | Infallibility |
| Publishing QA | Derived views | Accurate rendering, disclosure, links, and coverage | New engineering authority |

The actual reviewer and scope must be recorded. The repository does not claim
to have qualified reviewers available for every gate.

## Uncertainty and ambiguity propagation

Ambiguity lives at the narrowest layer and assertion it could materially
change. A shared log may store records, but storage does not change ownership.
An unreadable character belongs to transcription; ambiguous grammar to
translation; uncertain terminology to normalization; uncertain visible
object-label association to structure; uncertain connector identity or
electrical relationship to affected candidates; and uncertain applicability to
every claim whose scope could change.

A higher layer retains unresolved lower-layer ambiguity and may add narrower
downstream ambiguity. It must not suppress or spread it by category.

An ambiguity blocks translation when materially different readings remain;
normalization when no source-faithful term can be chosen; extraction when
faithful candidate endpoints, content, or scope require a choice; acceptance
when support or preserved uncertainty is inadequate; and publishing when the
view would mislead even with disclosure. Otherwise publishing may show it only
with visible provisional labeling.

## Pilot examples

### Printed page 2-3 — engine harness layout

- **Factory evidence:** fingerprinted scan, PDF page 15, printed page `2-3`.
- **Source-visible structure:** heading; rows `A`-`D`; columns `1`-`6`; harness
  legend; case-sensitive keys; connector and ground callouts; cavities; leader
  lines; swatches; and colored harness paths.
- **Linguistic translation:** Japanese harness labels and provisional literal
  English.
- **Engineering normalization:** possible future Toyota-supported harness
  names; none accepted here.
- **Graph extraction:** candidate harness, connector, location, and relationship
  claims.
- **Accepted graph:** only independently reviewed and explicitly accepted
  identities and relationships.
- **Publishing:** a disclosed English legend or annotated page.

A legend key is not automatically a harness entity ID. A drawn path is not
automatically a graph edge.

### Printed page 2-7 — instrument-panel harness layout

Factory evidence is PDF page 19 / printed page `2-7`. Structure owns the grid,
visual grouping, legend, swatches, connector callouts, exact-case identifiers,
text-label occurrences, and production qualifiers `('95.1~)` and `(~'95.1)`.
Translation owns Japanese wording and literal English while retaining engine,
side, and date qualifiers.

`H`, `J`, `K`, `k`, `p`, and `q` may have different roles as legend keys,
callout prefixes, or other source-local marks. Case and occurrence context must
survive. Issue #34 defines page-object types and Issue #29 identifier classes;
this document decides neither. Translation establishes neither connector
identity nor applicability beyond the source qualifier.

### Printed page 3-2 — power circuit diagram

- **Factory evidence:** fingerprinted artifact, PDF page 40 / printed `3-2`.
- **Source-visible structure:** fuse and relay blocks, ignition switch,
  batteries, alternator, combination meter, charge indicator, labels,
  wire-color words, junction dots, paths, connector depictions, terminal marks.
- **Linguistic translation:** provisional `コンビネーションメーター` to
  “Combination meter,” plus fuse, relay, component, and color wording.
- **Engineering normalization:** future Toyota-standard terminology; none
  accepted here.
- **Graph extraction:** candidate components, terminals, conductor segments,
  junctions, and electrical relationships.
- **Accepted graph:** independently reviewed and explicitly accepted topology.
- **Publishing:** a disclosed English rendering or searchable view.

A translated label is not a component entity. A drawn line is source structure;
connectivity is an extraction claim. `complete_bounded` means the declared
translation boundary is reconciled, not that every graphic object was
decomposed or that graph coverage is complete.

## Relationship to current translation records

The Milestone 7 records remain valid, unchanged, canonical for their current
reviewed-translation artifact role, and review-ready derived interpretive
representations. They are not source-page decompositions, graph extractions,
accepted translations, accepted factory facts, or accepted graph facts.
Grouped layout notes preserve nonlinguistic coverage without pre-empting a
future page-object model.

## Boundaries with sibling issues

- #34 defines primitive source-visible page objects.
- #27 defines page regions, hierarchy, and decomposition.
- #29 defines identifier classes and namespaces.
- #30 defines structural bindings between source objects or regions and
  translation records.
- #31 tests the model across publication families.
- #32 defines the downstream extraction contract and candidate boundary.
- #28 defines semantic layers and ownership constraining all of them.

This document does not choose sibling-issue schemas, taxonomies, identifiers,
geometry, binding granularity, or extraction-record shape.

## Open design questions

- Does page decomposition become canonical JSON?
- Are bounding boxes required?
- Does translation bind to regions, individual text objects, or both?
- Do candidate claims live in graph-shaped intermediate records?
- How can multiple publications support one accepted fact while retaining
  identity, applicability, and evidence roles?
- How do rendered pages reference upstream review states?
- Is accepted terminology global or publication-family-specific?

## Explicit non-goals

This investigation does not define or modify schemas, validators, migrations,
page-decomposition records, graph records, renderers, indexes, services, or
databases. It does not redesign or accept translation records; translate more
pages; normalize Toyota terminology; define object or identifier taxonomies;
define JSON fields; infer applicability to a 1990 PZJ70; establish equivalence
across publications; convert visible objects directly into graph entities; or
infer topology from proximity.

## ADR recommendation

No immediate ADR is recommended. Defer an ADR until Issues #27, #29, #30, #31,
#32, and #34 provide enough evidence to choose canonical artifacts and
contracts. Existing ADRs already govern evidence authority, translation's
derived role, provenance, immutability, overlays, and derived views; this
investigation refines their semantic boundaries without changing an invariant.
