# ADR 0007: Publication Representation Precedes Candidate-First Graph Extraction

- Status: Accepted
- Date: 2026-08-05

## Context

One Diagram successfully tested direct engineering extraction as a vertical
slice. The reviewed Japanese translation pilot then exposed a shared need that
was not owned by translation: the publication's visible content and structure
must be preservable separately from language and engineering interpretation.

Epic #26 investigated that need through separate work on semantic ownership,
source-visible page objects, page decomposition, identifiers, translation
bindings, publication-family coverage, and the downstream extraction handoff.
It established publication representation as a language-independent foundation.
Translation is one optional consumer of that foundation, and graph extraction
is another; neither owns or replaces it.

The repository needs this stable boundary before implementing canonical page
decomposition or candidate-extraction artifacts. This evolution preserves One
Diagram and Milestone 7 as successful pilots that revealed the missing shared
abstraction. Detailed operational rules remain in the
[semantic-layer contract](../docs/TRANSLATION_SEMANTIC_LAYERS.md),
[page-decomposition model](../docs/PAGE_DECOMPOSITION.md), and
[publication-to-graph extraction contract](../docs/PUBLICATION_GRAPH_EXTRACTION_CONTRACT.md).

## Decision

### Factory evidence remains primary

Original factory publication evidence is authoritative for what a publication
visibly contains. After verification and fingerprinting it remains immutable,
private and gitignored where repository policy requires, distinct from every
derived representation, and the ultimate evidentiary anchor for claims derived
from that publication.

Publication representation, transcription, translation, normalization, graph
candidates, accepted graph knowledge, and publishing views do not replace
factory publication evidence. Every accepted graph fact derived from a factory
publication remains traceable to its exact controlling publication location and
verified artifact.

Accepted knowledge may use other evidence classes under their own governance;
vehicle observations and overlays retain their own controlling evidence and do
not silently exchange authority with factory publications.

### Publication representation is language-independent

Publication representation records source-visible content and organization
without requiring English translation or complete linguistic understanding. It
may preserve page surfaces and declared boundaries, object occurrences, visual
organization, structural relationships, source-local identifiers, qualifiers,
locatable evidence, coverage, omissions, uncertainty, and review state.

It does not establish engineering identity, physical membership, electrical
topology, applicability acceptance, canonical graph relationships, or
factory-authored English. Translation, search, accessibility, rendering,
revision comparison, engineering normalization, and graph extraction may
consume it without owning it; this architectural permission does not claim
that those consumers are implemented.

### Linguistic interpretation is optional and separately owned

English translation is an optional, reviewable linguistic representation.
Graph extraction may instead use reviewed source-language understanding,
preserved transcription, directly supportable nonlinguistic evidence, or other
reviewed linguistic artifacts. A model's unrecorded multilingual understanding
is not durable repository evidence.

When linguistic meaning materially supports a claim, the repository preserves
the original-language occurrence, interpretation or translation, provenance,
uncertainty, review scope, and qualifications of the review. Translation
acceptance does not accept an engineering or graph claim.

### Extraction emits engineering candidates

Graph extraction consumes lower-layer observations and structural
relationships but does not duplicate source transcription, visible label
occurrences, visible attachment, containment, grouping, path geometry, or
page-object identity as graph candidates. It adds an explicit engineering
interpretation and emits the smallest independently reviewable candidate
engineering assertion supported by its stated inputs.

For example, observing `H8` is lower-layer evidence; proposing that a candidate
connector retains source-local designation `H8` is an engineering candidate.
A visible leader attachment is lower-layer structure; proposing that connector
X is at candidate vehicle location Y is an engineering candidate. Rejecting an
engineering interpretation does not invalidate an accurate lower-layer
observation or relationship.

### Candidate review and canonical acceptance remain separate

The required direction is:

```text
factory evidence
→ publication representation
→ optional linguistic and engineering interpretation
→ candidate engineering claim
→ independent extraction review
→ graph-acceptance eligibility review
→ explicit canonical acceptance
→ accepted graph knowledge
```

No arrow represents automatic promotion. Extraction never writes canonical
graph knowledge directly. Favorable candidate review is not canonical
acceptance. Eligibility review checks whether a candidate may be accepted but
does not silently mutate canonical data. Canonical acceptance is a separate,
explicit, reviewable decision. Proposal, review, eligibility, and acceptance
authorities remain distinguishable.

No tool, model, renderer, or polished English output establishes truth.
Accepted knowledge remains governed, revisable through explicit supersession,
and fully provenance-backed.

### Evidence roles remain distinct

Candidate support preserves at least these conceptual roles: primary factory
evidence, direct source observation, source-structure support, linguistic
interpretation, engineering terminology support, notation interpretation,
applicability support, corroborating factory evidence, conflicting factory
evidence, contextual accepted knowledge, derived-claim dependency, and
publishing or review aid.

One artifact may play different roles for different claims, but each use names
its role. Terminology support cannot silently become topology evidence;
applicability support cannot silently become identity evidence. A publishing or
review aid cannot replace primary evidence, satisfy a required review gate, or
confer canonical acceptance.

### Applicability composition follows the evidence relationship

There is no blanket intersection or union rule. **Applicability composition
follows the evidentiary relationship.** Conjunctive or complementary support
cannot exceed the justified intersection. Independently supported variants
remain separate candidates. Overlapping corroboration strengthens support
without automatically broadening scope. A union requires an explicit reviewed
derivation from independently accepted constituent facts.

Terminology-only and notation-only aids do not alter applicability unless they
independently provide controlling applicability evidence in that role.
Conflicts may narrow scope, preserve variants, remain unresolved, or block
acceptance. Later publication date alone does not establish supersession. In
particular, the January 1995 Japanese publication is not automatically
applicable to the user's 1990 PZJ70.

### Source-local identity remains local

Matching identifiers, labels, spelling, terminology, connector geometry, pin
counts, visual proximity, or publication date does not establish cross-page or
cross-publication identity. For example, `Japanese publication :: H8` and
`EWD168F :: H8` remain separate source-local occurrences until an explicit
engineering-equivalence candidate is supported, reviewed, and accepted. This
decision does not assert that those occurrences are equivalent.

### Ambiguity and provenance survive promotion

Every higher layer preserves unresolved lower-layer uncertainty that could
materially change its claim. The repository does not collapse confidence into
one page-level number, silently suppress alternatives, resolve conflicts
without a record, retarget claims after source changes, or end provenance at an
English translation or rendered page.

A publication-derived accepted graph fact retains a chain to its accepted
candidate, acceptance decision, engineering interpretation, material supporting
artifacts, exact controlling publication location, and verified source
artifact. Canonical page decomposition is not yet a universal prerequisite:
direct, precise source-location provenance remains valid where canonical
decomposition does not exist. When a candidate materially relies on a
structural occurrence or relationship, that support must be preserved and
reviewed.

### Demonstrated coverage remains limited

The general invariants are supported by Epic #26, but demonstrated
publication-family coverage is limited to circuit diagrams, harness layouts,
connector views, and tables within two Toyota EWD publications. Extraction
support has not been validated for specifications, maintenance procedures,
exploded diagrams, general multi-page structures, photographs, charts or plots,
equations, maps, or revision markup. Future support requires bounded evidence
and review.

### Relationship to ADR 0006

[ADR 0006](0006-reviewed-source-translation.md) remains valid and governs
reviewed translation as a derived interpretive representation. This decision
generalizes the lower architectural foundation discovered through the
translation work while preserving ADR 0006's translation-specific constraints.
Translation remains an optional consumer of publication representation; it is
not factory evidence and cannot accept graph facts. This ADR adds the
candidate-first extraction and explicit canonical-acceptance boundary.

## Alternatives Considered

### Continue extracting directly from undifferentiated PDFs

Rejected because it collapses observation, structure, interpretation,
extraction, and acceptance, making provenance and correction difficult to
isolate.

### Make translation the owner of page decomposition

Rejected because publication representation is language-independent and also
serves publications already in English.

### Require English before graph extraction

Rejected because reviewed source-language understanding and nonlinguistic
evidence may support engineering candidates directly.

### Treat page objects as engineering entities

Rejected because visible structure does not establish physical or graph
identity.

### Let extraction write canonical graph facts directly

Rejected because candidate creation, independent review, eligibility review,
and canonical acceptance must remain separate.

### Treat all supporting artifacts as equal evidence

Rejected because evidence roles have different authority and scope.

### Merge matching identifiers automatically

Rejected because identifiers remain source-local until reviewed equivalence.

### Require canonical decomposition before any extraction

Not adopted as an immediate universal requirement. Precise primary provenance
remains mandatory, and materially relied-upon structural support must be
preserved. Canonical decomposition is the preferred future foundation, but
current One Diagram work remains valid. Implementation planning will determine
when decomposition becomes required for new claims.

### Candidate-first, separately accepted extraction

Accepted because it creates an auditable, independently reviewable
transformation without prematurely choosing schemas or implementation.

## Consequences

Publication structure becomes reusable by multiple consumers, while translation
and extraction can evolve independently. Lower-layer corrections need not
rewrite unrelated graph knowledge, and rejected candidates do not erase
accurate observations. Cross-publication identity, applicability, and ambiguity
become explicit and reviewable. Accepted facts retain complete provenance, and
rendering or search cannot acquire unsupported authority.

The cost is more intermediate artifacts, explicit provenance, and separate
review boundaries. Implementations will need staleness and supersession
handling; some useful interpretations will remain candidates longer. Schemas,
lifecycle mechanics, and unsupported publication-family behavior remain future
work rather than completed capabilities.

## Scope Limits

This ADR does not define JSON, schemas, IDs, namespaces, geometry,
cardinalities, exact statuses, graph node or edge serialization, or lifecycle
mechanics. It creates no decomposition, translation, candidate, evidence,
vehicle-overlay, or canonical graph record; changes no graph data; implements
no validator, extraction, acceptance automation, downstream consumer, or
bounded pilot; translates no page; asserts no `H8` equivalence; broadens no
applicability; and authorizes neither production-scale translation nor bulk
extraction.

This ADR governs extraction from engineering publications; it does not redefine
the evidence rules for direct vehicle observations, measurements, service
records, photographs, or vehicle overlays.

After acceptance it authorizes planning one bounded architecture pilot, not
production extraction. The recommended pilot uses one demonstrated Toyota EWD
page, one reviewed page decomposition, one translation binding where
applicable, one explicit engineering candidate, complete evidence-role
provenance, one independent extraction review, one graph-acceptance eligibility
review, one explicit acceptance or deliberate rejection, and recorded
ambiguity, applicability, and supersession behavior. Page selection and exact
implementation mechanics remain planning decisions.
