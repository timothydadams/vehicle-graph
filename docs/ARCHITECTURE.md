# Architecture

Vehicle Graph is file-first and repository-centered.

## Knowledge layers

1. **Sources** are original evidence, including factory publications,
   photographs, measurements, service records, and direct vehicle observations.

2. **Extraction** transforms source evidence into structured candidate knowledge.
   Extraction may involve human transcription, OCR, AI assistance, or other
   tooling, but it never establishes canonical truth on its own.

3. **Factory knowledge** records accepted facts stated by authoritative factory
   sources. These records are immutable in meaning and evolve only through
   explicit supersession.

4. **Vehicle overlays** record confirmations, measurements, observations,
   modifications, and deviations for a specific identified vehicle without
   changing factory knowledge.

5. **Derived views** combine applicable graph knowledge to produce diagrams,
   reports, search indexes, databases, user interfaces, AI context, or other
   useful representations.

These are conceptual knowledge boundaries, not a proposed directory layout,
schema, or software architecture.

## Publication representation

**Publication representation** is the shared, language-independent capability
for recording what an engineering publication visibly contains and how its
content is organized. It sits between factory publication evidence and several
possible downstream interpretations or uses.

Publication representation includes, or may later include, source-visible page
objects, page decomposition, page-local structure, visual organization,
structural associations, source-evidence bindings, and preserved text
occurrences that do not require translation. Linguistic interpretations may
bind to those occurrences, but do not create them.

Publication representation does not own accepted engineering identity, graph
topology, canonical component relationships, normalized terminology,
translation acceptance, or publication rendering as evidence. A precisely
represented label, line, enclosure, or visible association does not become an
engineering entity, connection, or graph fact merely because a contributor or
agent understands it.

```text
Factory publication evidence
            │
            ▼
Publication representation
            │
            ├────────► Linguistic interpretation
            │              ├── source transcription
            │              ├── literal translation
            │              └── reviewed language representation
            │
            ├────────► Engineering normalization
            │
            ├────────► Search / accessibility / rendering / diffing
            │
            └────────► Graph extraction
                           │
                           ▼
                  Accepted knowledge graph
```

Arrows show permitted dependencies, not automatic transformation, acceptance,
or promotion. The listed consumers are architectural consumers or future
possibilities unless another document identifies an implemented capability.
Rendering remains a derived view and never becomes controlling factory
evidence.

Reviewed translation is specialized linguistic interpretation between source
evidence and extraction, not a sixth knowledge layer and not the owner of
publication representation. It produces a derived interpretive representation
that remains subordinate to the original-language publication. The original
publication remains primary evidence; translation acceptance does not establish
a factory fact. Any English Markdown, HTML, or PDF edition rendered from
accepted translation material is a derived view.

The finer ownership boundaries within that path are defined in
[Translation Semantic Layers and Artifact Ownership](TRANSLATION_SEMANTIC_LAYERS.md).
They define dependency edges, contextual authority levels, mutability, and the
rule that higher layers augment rather than replace lower-layer evidence. They
are a semantic contract, not a claim that every layer has a separate schema.

Within the Source-visible Structure layer, the
[Source Page Object Taxonomy](SOURCE_PAGE_OBJECT_TAXONOMY.md) defines a
pilot-grounded, language-independent candidate vocabulary for visible,
page-scoped occurrences. It defines neither publication-wide structure,
storage, nor hierarchy; does not promote a page object into an engineering
entity or graph fact; and remains subject to validation across other
publication families.

The candidate [Page Decomposition](PAGE_DECOMPOSITION.md) model organizes
instances of that vocabulary within a verified page or declared page boundary.
It recommends a containment hierarchy for page organization plus explicit
non-hierarchical structural relationships for visible associations. The model
is conceptual: it defines no canonical artifact or engineering topology.

The [Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md)
separates source-visible occurrences and values, repository-assigned structural
identity, candidate engineering identity, and accepted graph identity. Matching
spelling never promotes identity or equivalence, and exact source form remains
preserved.

## Architectural principles

- **Language-independent foundation.** A publication can be structurally
  represented whether or not its text is understood or translated.
- **Optional linguistic interpretation.** Language understanding is often
  necessary downstream—for example, to classify a page as a starting-system
  diagram—but it is not a prerequisite for faithfully recording visible
  objects and material structural relationships.
- **English is derived.** English wording never replaces the controlling
  source-language occurrence or acquires factory authorship.
- **Agent capability is not evidence.** Multilingual model understanding may
  assist interpretation, but durable repository claims still require explicit
  provenance, uncertainty, review scope, and reviewable linguistic artifacts.
- **Shared foundation.** Translation, graph extraction, rendering, search,
  accessibility, and revision comparison may consume publication
  representation without owning it.
- **No direct promotion.** A source page object or structural relation does not
  become an engineering entity or graph fact merely because its label is
  understood.

These principles were discovered through successful vertical pilots. One
Diagram tested a direct evidence-to-graph slice; the Japanese translation
feature then exposed page-organization limits. Milestone 7 validated translation
records, Issues #28 and #34 defined the shared semantic boundaries and page-
object vocabulary, and Issue #27 now investigates their candidate page-level
composition. This evolution does not invalidate One Diagram or the Milestone 7
results.

## Canonical state

JSON is the canonical representation of structured knowledge. Git stores its
history, review context, and accepted state. Generated diagrams, indexes,
databases, search structures, and user interfaces are consumers or projections;
none becomes a competing source of truth.

## Information flow

Source evidence may first be represented structurally, then interpreted and
reviewed into candidate claims with provenance and applicability. Factory facts
are append-only in meaning: a newly discovered
correction supersedes prior knowledge explicitly rather than erasing it. A
vehicle overlay may add an observation or identify a difference, but it never
mutates the factory layer. Tools read, validate, query, and combine applicable facts to produce derived views.

## Simplicity

The default architecture is files plus small, replaceable tools. Add a database,
service, queue, cache, or hosted component only when a demonstrated requirement
cannot be met clearly with repository-local files. Convenience alone is not a
reason to introduce infrastructure. Infrastructure should emerge from demonstrated need rather than anticipated scale.

The first architectural proof is **One Diagram**, not a generalized platform.

The repository preserves knowledge.

Tools preserve nothing.
