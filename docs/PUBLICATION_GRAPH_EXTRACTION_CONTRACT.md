# Publication-to-Graph Extraction Contract

## Status and purpose

This document defines the conceptual handoff from factory publication evidence
and publication representation into candidate engineering claims, independent
review, and accepted canonical graph knowledge. It completes Issue #32, the
final design investigation in Epic #26.

This is an architecture contract, not a storage design. It assigns evidence
roles, responsibilities, review boundaries, provenance requirements,
uncertainty behavior, and acceptance constraints without choosing fields,
syntax, identifiers, cardinalities, or implementation. Demonstrated family
coverage is limited to circuit diagrams, harness layouts, connector views, and
tables inspected in two Toyota EWD publications.

Its durable architectural decisions are recorded by
[ADR 0007](../adr/0007-publication-representation-and-candidate-first-extraction.md).

## Scope and governing principles

The contract governs extraction that may consume controlling factory evidence,
reviewed publication representation, optional linguistic interpretation,
engineering normalization where needed, applicability evidence, material
interpretive dependencies, and limited contextual accepted knowledge.

Graph extraction consumes lower-layer observations and structural
relationships; it does not duplicate them as graph candidates. Its output is
the smallest independently reviewable engineering assertion derived from those
inputs. Transcription remains linguistic or direct-observation work,
structural relationships remain publication representation, normalization
remains terminology work, and canonical acceptance remains separate.

1. **Primary evidence remains primary.** The controlling factory publication
   location is the evidentiary anchor. Decomposition, transcription,
   translation, normalization, extraction, and rendering are derived artifacts
   with distinct roles.
2. **Structure does not equal engineering meaning.** A visible object,
   containment, attachment, path, dot, label, or repeated motif does not by
   itself establish engineering identity, routing, connectivity, behavior,
   applicability, or topology.
3. **Extraction emits candidates.** It never writes accepted graph facts.
4. **Acceptance is independent.** Artifact, structure, transcription,
   language, terminology, applicability, extraction, graph acceptance, and
   publishing reviews are distinct gates.
5. **Translation is optional.** Reviewed source-language understanding or
   directly supportable nonlinguistic evidence may support extraction. When a
   translation is used, its provenance, uncertainty, and review scope remain
   explicit.
6. **Applicability survives every transformation.** Material model, market,
   production-date, engine, equipment, option, destination, and other
   qualifiers remain attached. Applicability composition follows the
   evidentiary relationship: conjunctive support generally narrows to a
   supported intersection, independent variant claims remain separate, and a
   union requires an explicit reviewed derivation.
7. **Ambiguity propagates narrowly.** Unresolved uncertainty remains on every
   candidate it could materially change unless authorized review resolves it.
   Association or proximity alone is not propagation.
8. **Identity is never inferred from label reuse.** Matching identifiers,
   terminology, depictions, or proximity do not prove equivalence.
9. **Evidence roles do not collapse.** A terminology aid cannot silently become
   topology evidence, nor applicability evidence become identity evidence.
10. **Derived views remain downstream.** Publishing, search, reports, and APIs
    do not become primary evidence or acceptance authorities.

## Contract diagram

```text
Verified factory evidence ───────────────────────────────────────────┐
        │                                                           │
        ▼                                                           │
Publication representation                                          │
        │                                                           │
        ├────────► optional linguistic interpretation ────────┐     │
        ├────────► engineering normalization where required ──┤     │
        ├────────► applicability evidence ─────────────────────┤     │
        └────────► explicit interpretive dependencies ─────────┤     │
                                                             ▼     │
Contextual accepted knowledge ────────────────► graph extraction ◄──┘
                                                    │
                                                    ▼
                                      candidate engineering claims
                                                    │
                                                    ▼
                                      independent extraction review
                                                    │
                                                    ▼
                                    explicit graph-acceptance decision
                                                    │
                                                    ▼
                                      accepted canonical knowledge
```

Arrows are permitted dependencies and evidence roles, not automatic promotion.

## Input roles

Each input use declares its role for the particular candidate. One artifact may
play different roles for different claims, but authority is evaluated per use.

### Factory evidence

Factory evidence includes publication identity, verified artifact fingerprint,
PDF and printed-page coordinates, an exact figure, table, region, or other
location, and visible factory-authored content. Visible non-factory capture
content remains identified as such. It controls what the publication visibly
states or depicts, not the repository's engineering interpretation.

### Publication representation

Publication representation may supply a decomposition boundary, source-visible
occurrences, structural identities, locatable extents, visible relationships,
coverage and omission declarations, unreadable content, qualifiers, ambiguity,
and review state. It is a reviewed structural aid, not graph truth. A connector
depiction is not a connector entity; a path is not a graph edge; a leader is not
membership; a structural identity is not an engineering identity.

A canonical decomposition record is not a universal prerequisite for
extraction. Direct, precise source-location provenance remains valid where no
canonical decomposition exists. When an engineering candidate materially
relies on a structural occurrence or relationship, however, that support must
be preserved and reviewed; future implementation should prefer stable
structural references when available.

### Linguistic interpretation

Linguistic inputs may include transcription, source-language reading, literal
translation, bindings, preserve-verbatim or translation-not-applicable
dispositions, uncertainty, and language-review state. An agent's unrecorded
multilingual understanding is not durable evidence. Meaning material to a claim
requires preserved interpretation, original-language provenance, uncertainty,
and actual review scope. Translation is never factory-authored English or sole
provenance for a factory claim.

### Engineering normalization

Normalization may supply engineering wording, its terminology basis, scope,
alternatives, and review state. It can help name a candidate concept but cannot
add source facts, transfer applicability, prove identity, establish topology,
or accept a claim. Source wording, literal meaning, and normalization remain
distinct.

### Applicability evidence

Applicability may come from publication metadata, visible qualifiers,
model-family tables, production boundaries, market or destination statements,
engine designations, equipment conditions, or option notes. It is a distinct
evidence role; terminology or topology similarity does not prove scope.

### Interpretive dependencies

Dependencies explain how controlling evidence must be read. They may include
same-publication notation, symbols, wire colors, continuations, connector-view
orientation, relay and junction conventions, state tables, page organization,
or applicability guidance. Every dependency declares what it supports and what
it does not. The publication's own definitions precede generic knowledge. Only
dependencies material to the candidate attach: omission of a required
dependency and addition of an irrelevant one are both review failures.

### Existing accepted graph knowledge

Accepted facts may provide context, propose a match, expose a conflict, or be
explicit dependencies of a derived candidate. They do not overwrite
contradictory publication evidence and are not primary evidence for a new
factory-observation claim. Circular provenance is prohibited: a candidate
cannot cite itself, its rendering, or a downstream index as support.

## Evidence-role matrix

| Role | May support | Must not support by itself | Controlling? | Provenance and review |
| --- | --- | --- | --- | --- |
| Primary factory evidence | What the source visibly states or depicts | Repository interpretation | Yes for direct observation | Verified artifact and exact location |
| Direct source observation | A visible mark, label, or occurrence | Identity or topology | For observed content | Exact source form, extent, observation review |
| Source-structure support | Visible grouping, attachment, sequence, or path organization | Physical membership, routing, connectivity, or graph identity | No | Occurrences, relationships, structure review |
| Linguistic interpretation | Meaning or literal translation used by the claim | Factory-authored English, topology, identity | No | Original occurrence, uncertainty, language-review scope |
| Terminology support | Scoped normalized wording | Equivalence, applicability transfer, topology | No | Terminology source, scope, rationale, review |
| Notation interpretation | How marks and conventions are read | A claim absent from controlling evidence | Controls interpretation only | Exact guidance and convention review |
| Applicability support | Model, market, date, engine, equipment, or variant scope | Terminology or topology | May control scope | Exact qualifier and applicability review |
| Corroborating factory evidence | Independent agreement or complementary support | Replacement of controlling evidence | Sometimes jointly | Separate verified source, location, and role |
| Conflicting factory evidence | Material incompatible content | Silent selection | Yes as an acceptance constraint | Separate conflict, scope, and disposition |
| Contextual accepted knowledge | Matching help and conflict detection | Primary support for a new direct claim | No | Accepted fact and original provenance |
| Derived-claim dependency | An explicit derivation | A direct factory-observation claim | For the derivation only | Upstream facts, assumptions, and relationship-specific applicability composition |
| Publishing or review aid | Navigation, comparison, inspection, and presentation of disclosed upstream state | Primary evidence, satisfaction of a required review gate, or canonical acceptance | No | Generating inputs, disclosed upstream state, and underlying recorded decisions |

For example, EWD168F may support Toyota English terminology for a Japanese
publication without proving that identically numbered connectors are
equivalent.

A review aid may help a reviewer navigate or compare material, but does not
prove that review occurred and cannot substitute for primary evidence. Visual
polish never promotes a candidate. A generated report may document a decision,
but its authority comes from the underlying recorded decision and provenance,
not its presentation.

## Claim-support profiles

There is no universal minimum input bundle. Required evidence and review depend
on what a candidate asserts.

### Engineering candidate primarily supported by direct source observation

Example: candidate connector X retains source-local identifier `H8` in
publication A. The direct observation that the page visibly contains `H8`
remains owned by source transcription or publication representation; the
engineering candidate references it and explicitly proposes how that
designation relates to candidate X. Minimum support normally includes a
verified artifact, exact location, reviewed observation or transcription,
identifier role and narrowest supported scope, applicable qualifiers,
uncertainty, and review state. Retaining the source-local designation neither
converts `H8` into repository identity nor establishes physical connector
identity or equivalence with another source's `H8`.

### Engineering candidate primarily supported by source-visible structure

Example: candidate connector X is proposed at candidate vehicle location Y
based on a reviewed callout attachment. The visible leader attachment remains
owned by publication representation. Extraction must state the engineering
interpretation it proposes and, when available, cite the exact structural
occurrences and relationship. Minimum support normally includes primary
evidence, a precise source location, the reviewed visible relationship and
extent, qualifiers, coverage context, and structural ambiguity. Visible
attachment does not itself establish vehicle location, physical mounting,
harness ownership or membership, routing, or connector identity.

### Linguistically dependent engineering candidate

Example: the source labels an item “Glow Plug Relay (Main).” Minimum support
normally includes the factory location, source occurrence, reviewed
transcription or durable source-language interpretation, translation when used,
separate terminology evidence when normalized wording is claimed, qualifiers,
ambiguity, and actual language and terminology review states. The graph
candidate must add an engineering interpretation, such as proposing that the
source-labeled occurrence designates candidate relay X; transcription and
normalization remain lower-layer assertions rather than graph candidates.

### Topology or behavior candidate

Example: two candidate terminals are electrically connected under a stated
condition. Minimum support normally includes controlling circuit evidence;
relevant visible paths, symbols, endpoints, junctions or crossings;
publication notation guidance; endpoint interpretation; operating condition;
structural and engineering ambiguity; applicability; and extraction review.
Every endpoint is reviewable. Visible linework and a junction dot are inputs to
interpretation, not automatically a graph edge or accepted connectivity.

### Cross-publication identity candidate

Example: `publication-A::H8` and `publication-B::H8` are the same physical
connector. Each occurrence remains separately identified. Support must extend
beyond label equality and may include geometry, cavity count, keying, component
association, wire colors, harness context, location, mating relationships,
applicability overlap, or an explicit factory cross-reference. No single
attribute, automatic rule, or numeric score establishes equivalence.

### Derived candidate

Example: a conclusion follows from several accepted facts. Minimum support
includes an explicit derivation, every upstream accepted fact, retained original
provenance, assumptions, and applicability composed according to the
dependencies' relationship. Conjunctive dependencies constrain the result to
their supported intersection; an applicability union requires a separately
justified aggregation. A derived claim is identified as derived and revalidated
when a dependency changes. It cannot masquerade as a direct factory fact.

## Extraction and candidate responsibilities

Extraction may propose engineering entities and relationships; interpret
reviewed structure using publication guidance; use optional linguistic
artifacts and separately supported normalized wording; combine several sources
while preserving roles; retain variants; record conflicts; narrow
applicability; and state explicit derivations.

It must declare its boundary and omissions; cite primary evidence; preserve
publication identity and source-local identifiers; retain qualifiers and
material dependencies; distinguish observation, interpretation,
normalization, corroboration, conflict, and derivation; attach ambiguity only
to the narrowest candidate it could change; retain incompatible variants; and
emit independently reviewable candidates.

Extraction consumes accurate lower-layer observations and relationships rather
than re-emitting them as graph candidates. Every output candidate must state the
engineering interpretation added to its support. Source observation,
structural relationship, linguistic interpretation, and normalized terminology
remain independently reviewable assertions in their owning layers.

It must not mutate evidence; replace original wording; treat translation as
factory-authored English; promote page identity into engineering identity;
promote containment into physical containment, visible attachment into
membership, or paths into graph edges; infer equivalence from identifiers;
broaden applicability; suppress conflict; accept its own candidates; or write
canonical knowledge directly.

A candidate is the smallest explicit engineering assertion that can be
reviewed independently. Conceptually it preserves its assertion and kind,
candidate entities or relationships, exact primary evidence, structural inputs,
linguistic and normalization artifacts, applicability, evidence roles,
dependencies, assumptions, ambiguity, conflicts, derivation, extraction
boundary, review state, and staleness or supersession history.

A source observation or structural relationship may be independently reviewed
without becoming a graph candidate. A graph candidate adds an explicit
engineering interpretation and keeps it distinguishable from every supporting
lower-layer assertion. Rejecting that interpretation does not invalidate an
accurate transcription or structural relationship. Correcting a lower-layer
input may stale or supersede its dependent candidates without changing
unrelated work.

```text
Source observation:
The page visibly contains H8.

Structural observation:
A leader visibly attaches the H8 callout to a depicted location.

Engineering candidate:
The source-labeled connector H8 is proposed to be located at candidate vehicle
location X.

Accepted graph fact:
Only after independent review and explicit acceptance.
```

This example is conceptual and defines no record syntax. A candidate is
reviewable, not canonical. One candidate may use several items in different
roles; several candidates may interpret one occurrence; and one occurrence may
support several claims. Rejected and superseded candidates may remain valuable
history. Polished English does not increase authority. Output must remain
separable from evidence, representation, translation, and accepted knowledge
so an interpretation can change without rewriting them.

## Provenance preservation

```text
accepted graph fact
    ↓
accepted extraction candidate and acceptance decision
    ↓
candidate engineering interpretation
    ↓
supporting reviewed artifacts used by the candidate
    ├── source-visible occurrences and structural relationships, when
    │   available or relied upon
    ├── linguistic interpretation, when relied upon
    ├── terminology or notation guidance, when relied upon
    ├── applicability evidence
    └── other declared dependencies
    ↓
exact controlling factory publication location
    ↓
verified source artifact
```

Every candidate reaches exact primary factory evidence. A canonical page-
decomposition record is not universally required at this architecture stage:
direct source-location provenance may support a candidate where no canonical
decomposition exists. This does not authorize vague page-only provenance; the
location must be precise enough for independent review. When extraction relies
on a structural occurrence or relationship, that support must be preserved and
reviewed even before canonical decomposition storage exists. Future
implementation should prefer stable structural references where available.

Translation, terminology, notation guidance, applicability, and corroborating
or conflicting publications participate in their actual roles. Provenance
explains both where support appears and how it was interpreted. It never stops
at a translation, English rendering, search result, or graph record. This
compatibility rule preserves, rather than weakens, publication representation
as the preferred language-independent foundation.

Several pages may jointly support one candidate when each role is declared. One
page may support several separately scoped candidates. Agreeing publications
retain separate provenance; complementary sources identify what each supports;
conflicts retain both sources, scopes, and interpretations. Terminology and
topology may come from different sources only with roles separate. A
translation-dependent candidate reaches through its binding to original
evidence.

If an artifact, page map, decomposition, or lower-layer interpretation changes,
no claim is silently retargeted. Affected work is re-reviewed or superseded,
prior provenance remains recoverable, and downstream derivations are
reevaluated.

## Applicability and identity controls

Extraction evaluates applicability from publication-level scope through page,
region, item, and claim qualifiers. Engine, model, market, destination,
equipment, option, production-date, and operating conditions remain explicit.
Uncertainty stays attached where it could change scope. Applicability
composition follows the evidentiary relationship:

- **Conjunctive or complementary support.** When a candidate depends on several
  evidence items simultaneously, it cannot exceed their justified
  intersection. Conceptually, topology evidence scoped to `1PZ` plus a
  connector view scoped to `1993-on JDM` supports only their demonstrated
  intersection; this is not a claim about the user's vehicle.
- **Independent corroboration over the same scope.** Overlap may strengthen
  support without automatically broadening the candidate.
- **Independent variant-specific support.** Equivalent-looking assertions from
  different variants remain separate candidates rather than being merged.
- **Explicit derived aggregation.** A union is permitted only as a reviewed
  derivation from independently accepted variant facts when equivalence of the
  asserted relationship is justified, union boundaries and exceptions are
  explicit, conflicts remain visible, and provenance reaches every constituent
  fact and original source.
- **Terminology-only or notation-only support.** These sources do not change
  applicability unless they independently provide controlling applicability
  evidence used in that role.
- **Conflicting applicability.** Conflict may narrow a candidate, preserve
  alternatives, remain unresolved, block acceptance, or require more evidence;
  scopes are neither averaged nor silently united.
- **Supersession.** A later publication changes applicability only when an
  explicit revision or supersession relationship and its scope are supported,
  never from publication date alone.

A source outside the target vehicle's range may be a terminology or
interpretive aid but cannot establish target applicability. The January 1995
Japanese publication may provide insight relevant to Land Cruiser 70-series
work, but it does not automatically apply to the user's 1990 PZJ70. Connector
or harness equivalence needs evidence. This contract creates no vehicle overlay.

Factory identifier occurrences and values, identifier classes and scopes,
structural occurrence identities, candidate engineering identities, and
accepted graph identities remain separate. Source values remain verbatim and
narrowly scoped; repeated values remain distinct occurrences. Structural
identity locates evidence but does not confer engineering identity. Candidate
identity is provisional, and accepted identity requires review and explicit
acceptance. No value, spelling, number, geometry, or terminology automatically
merges occurrences or becomes repository identity.

## Ambiguity, uncertainty, and blocking

Uncertainty may concern readability, structural class or relationship,
transcription, literal meaning, normalization, entity identity, topology,
applicability, cross-source equivalence, derivation, or acceptance. These remain
local rather than collapsing into a page score or numeric confidence value.

For source transcription, ask:

> Would this uncertainty force a choice between materially different source
> transcriptions?

If yes, it blocks the affected boundary or requires narrowing. If no, faithful
transcription may continue with explicit ambiguity.

For candidate attachment, ask:

> Could resolving this ambiguity materially change this candidate's assertion,
> endpoints, identity, applicability, boundary, status, or interpretation?

If yes, attach it at the narrowest claim. If no, do not propagate it by object,
page, connector, circuit, or category association. Uncertainty may block one
claim, narrow it, preserve alternatives, permit provisional extraction while
blocking acceptance, require evidence, or propagate through a derivation. A
higher layer never suppresses unresolved lower-layer uncertainty.

## Multi-source corroboration and conflict

Sources may provide independent agreement, complementary support,
terminology-only support, notation-only support, a variant difference,
unresolved conflict, explicitly established supersession, or unrelated
similarity. The relationship is claim-specific and controls how applicability
is composed. Conjunctive evidence narrows to supported overlap; independently
supported variants remain separate; and any union is an explicit derived claim
rather than the default result of citing several sources.

Extraction must not silently select the cleaner diagram, combine incompatible
variants, average conflicts, merge source-local identifiers, presume a later
publication is superior, or treat English wording as stronger topology evidence
than Japanese factory content. A later source supersedes only when evidence
establishes that relationship and scope. Alternatives may remain, scope may be
narrowed, or more evidence requested. Acceptance preserves why an
interpretation was accepted, rejected, or superseded.

## Review gates

Required gates follow the claim-support profile; not every claim needs every
gate.

1. Artifact verification confirms exact source identity and integrity.
2. Source-location verification confirms the cited location or extent.
3. Source-structure review checks objects, relations, coverage, and ambiguity.
4. Source-transcription review checks exact source form and readability.
5. Language-fidelity review checks meaning or translation within the reviewer's
   actual qualifications.
6. Engineering-terminology review checks normalized wording without accepting
   identity or topology.
7. Applicability review checks material qualifiers and combinations.
8. Extraction-candidate review checks the engineering transformation, roles,
   dependencies, assumptions, and claim-local ambiguity.
9. Independent graph-acceptance review checks eligibility of the exact candidate
   for a separate canonical decision.
10. Publishing QA checks rendering and disclosure without changing authority.

An English-only engineering reviewer cannot claim Japanese language-fidelity
review, and machine cross-checking is not human language verification. No score
replaces review evidence. The proposer does not automatically accept their own
candidate, and favorable review is not canonical acceptance.

## Candidate-to-canonical acceptance boundary

A candidate may become canonical only when controlling evidence is verified and
available; its location is independently reviewable; its assertion is explicit;
evidence roles, material interpretation, and assumptions are documented;
source-local identifiers remain preserved; applicability is explicit; material
ambiguities are resolved or retained under documented policy; conflicts are
disclosed; applicability composition is justified for the declared evidence
relationship; required gates passed; an independent acceptance decision is
recorded; and the accepted fact remains traceable to the exact candidate and
evidence.

Acceptance does not rewrite lower-layer artifacts, create factory-authored
English, imply universal applicability, or make a claim infallible. A candidate
may instead be rejected, unresolved, blocked, superseded, stale,
variant-specific, or duplicate. These are concepts, not prescribed status
values. Non-acceptance preserves useful evidence and rationale; a duplicate
does not merge distinct occurrences. Canonical meaning changes only through
governed qualification or supersession with history recoverable.

## Revision and staleness

Artifact or page-map change; decomposition-boundary change; source-object split,
merge, or reidentification; transcription or translation correction;
normalization change; applicability narrowing; candidate-entity split or merge;
new conflict; accepted-fact supersession; or an upstream derivation dependency
change triggers explicit impact review. Nothing is silently retargeted.

Review identifies unaffected, stale, blocked, revised, or superseded claims.
Prior provenance and decisions remain recoverable. Accepted meaning is not
silently mutated, and derived claims are recalculated or revalidated. Migration
mechanics remain implementation work.

## Demonstrated-family examples

These are conceptual walkthroughs, not canonical records or universal support.

### A. Circuit diagram — printed page `3-2`

The factory page controls. Representation may locate symbols, labels, paths,
junction dots, terminal marks, qualifiers, and visible relations. Publication
guidance may define dots, crossings, wire colors, continuations, and state
tables. Linguistic interpretation may preserve `コンビネーションメーター`;
normalization may propose English terminology. Extraction may propose candidate
components, terminals, connectivity, or conditional behavior.

A path is not a graph edge; a junction dot is not automatically accepted
connectivity; and translating `コンビネーションメーター` does not establish
canonical identity. Every endpoint requires review, and engine or production
qualifiers constrain the candidate.

### B. Harness layout — printed pages `2-3` and `2-7`

Representation may preserve page grids, legend keys, harness paths, connector
callouts, leaders, qualifiers, and paired list/layout references. Extraction may
use those lower-layer assertions to propose that a candidate engineering
harness carries a source-local designation, that a candidate connector is at a
candidate vehicle location, or that a depicted context supports a candidate
harness boundary.

Depicted route is not accepted physical routing; attachment is not harness
ownership; grid position is not vehicle geometry; and identifiers remain
source-local. The publication-level paired-page relationship remains unresolved
where prior design left it open.

```text
structural observation
→ a leader visibly attaches a callout to a depicted location

engineering candidate
→ connector X is proposed at candidate vehicle location Y

not established
→ physical mounting, harness ownership, or accepted location
```

### C. Connector view

Representation may locate the body depiction, cavities and numbers, component
label, and visible view qualifier. Extraction may propose geometry, cavity
numbering, terminal correspondence, or a cross-publication comparison. Geometry
is not identity; matching IDs are not equivalence; orientation cannot be
invented; and terminology evidence cannot prove topology. Equivalence is a
separate candidate.

### D. Table

Representation may preserve table, row, column, cell, grouping, alignment,
sequence, identifier, and page reference. Translation may bind to text without
owning the table. A row is not automatically an engineering record, cell text
is not automatically a property value, and blank cells are structure rather
than omitted translation. Exact cardinality remains implementation. A candidate
cites the particular cell or group used.

### E. Multi-source connector label `H8`

```text
Japanese publication :: H8
EWD168F              :: H8
```

These remain separate source-local occurrences. Identifier, wording, geometry,
pin count, wire colors, harness, location, or mating context may contribute to
an equivalence candidate, but no single match proves identity. No actual `H8`
equivalence is asserted here.

The lower-layer and engineering boundaries are:

```text
source observation
→ source-local identifier occurrence H8

engineering candidate
→ candidate connector X retains source-local identifier H8

not established
→ physical connector identity or equivalence with another publication's H8
```

Applicability composition likewise depends on the evidence relationship:

```text
conjunctive support
→ candidate limited to the demonstrated intersection

independent support for variant A and variant B
→ separate variant-specific candidates

explicit derived aggregation after independent acceptance and equivalence review
→ a stated union with boundaries, exceptions, conflicts, and all provenance
```

These are conceptual variants and establish no actual vehicle claim.

## Compatibility with One Diagram

One Diagram was a successful vertical pilot that exposed the missing shared
publication-representation layer. Its inventories, boundary, source-language
record, candidate ledger, ambiguity records, and direct provenance remain valid
for their reviewed artifact roles. They are not invalid because canonical
decomposition does not yet exist.

An existing One Diagram engineering candidate remains reviewable through its
exact page and region provenance even before a canonical decomposition record
exists. Future structural references may enrich that provenance, but the
contract neither retroactively invalidates existing candidates nor authorizes a
migration. Implementation must decide when decomposition is required for new
claims and whether or how legacy candidates gain references while preserving
original evidence and review history. A candidate that materially relies on a
visual relationship must preserve that relationship in reviewable form even
before canonical decomposition storage exists. Existing canonical graph facts,
if any, are not automatically reopened.

## Unsupported-family limitations

Current evidence demonstrates four page families within two Toyota EWDs. The
general invariants above may guide future evaluation, but validated extraction
inputs or transformations are not claimed for specifications, maintenance
procedures, exploded diagrams, general multi-page structures, photographs,
charts or plots, equations, maps, or revision markup.

Support requires bounded inspectable evidence, a family evaluation,
source-language guidance review where applicable, contract stress testing, and
independent review. Plausible similarity is insufficient.

## Sibling-layer boundaries

- #28 owns semantic layers and artifact ownership.
- #34 owns source-visible object vocabulary.
- #27 owns page decomposition, structural relationships, and occurrence
  identity needs.
- #29 owns publication identifier roles, scopes, and collision controls.
- #30 owns translation bindings.
- #31 owns family evaluation and demonstrated coverage limits.
- #32 owns this downstream extraction contract and acceptance boundary.

This contract consumes rather than redesigns those conclusions.

## Alternatives considered

- **Direct PDF-to-canonical extraction — rejected:** it collapses observation,
  interpretation, extraction, review, and acceptance.
- **Mandatory English translation — rejected:** source-language and
  nonlinguistic evidence can support claims directly.
- **Page decomposition as graph extraction — rejected:** structure does not own
  engineering identity or topology.
- **Equal authority for all inputs — rejected:** evidence roles differ.
- **Accepted knowledge replacing publication provenance — rejected:** every
  fact must remain traceable to controlling evidence.
- **Automatic merge of matching identifiers — rejected:** source identifiers
  remain local until equivalence is supported and accepted.
- **One universal input bundle — rejected:** support depends on claim type.
- **Candidate-first, independently reviewed extraction — provisionally
  adopted:** it preserves reversible interpretation and separate acceptance
  without choosing artifact syntax.

## ADR and implementation-readiness recommendations

Recommend one focused ADR after Issue #32 merges. It should capture publication
representation as the language-independent foundation and candidate-first graph
extraction as a separately reviewed downstream transformation, while deferring
storage, schemas, identifiers, and implementation. No ADR is created here so
review of the completed contract can precede the combined Epic #26 decision.

After that ADR is accepted, the architecture is ready for a bounded pilot: one
reviewed page decomposition, one translation binding where applicable, one
extraction candidate, one independent review, one explicit acceptance or
deliberate rejection, and complete provenance. The pilot must use a demonstrated
family and test the contract rather than start production extraction.

## Explicit non-goals

This contract does not define or create schemas, JSON fields, graph node or edge
serialization, IDs, exact statuses, cardinalities, decomposition or translation
records, candidate records, graph data, validators, code, migrations,
acceptance automation, additional translations, evidence, vehicle overlays, or
the post-epic pilot. It does not establish actual `H8` equivalence, broaden
applicability to the user's 1990 PZJ70, redesign sibling work, or claim support
for an unvalidated family.
