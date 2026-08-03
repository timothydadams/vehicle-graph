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

Reviewed translation is specialized source processing between source evidence
and extraction, not a sixth knowledge layer. It produces a derived interpretive
representation that remains subordinate to the original-language publication.
The original publication remains primary evidence; translation acceptance does
not establish a factory fact. Any English Markdown, HTML, or PDF edition
rendered from accepted translation material is a derived view.

The finer ownership boundaries within that path are defined in
[Translation Semantic Layers and Artifact Ownership](TRANSLATION_SEMANTIC_LAYERS.md).
They define dependency edges, contextual authority levels, mutability, and the
rule that higher layers augment rather than replace lower-layer evidence. They
are a semantic contract, not a claim that every layer has a separate schema.

Within the Source-visible Structure layer, the
[Source Page Object Taxonomy](SOURCE_PAGE_OBJECT_TAXONOMY.md) defines the
language-independent vocabulary for visible page occurrences. It defines
neither storage nor hierarchy and does not promote a page object into an
engineering entity or graph fact.

## Canonical state

JSON is the canonical representation of structured knowledge. Git stores its
history, review context, and accepted state. Generated diagrams, indexes,
databases, search structures, and user interfaces are consumers or projections;
none becomes a competing source of truth.

## Information flow

Source evidence is reviewed and transcribed into facts with provenance and
applicability. Factory facts are append-only in meaning: a newly discovered
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
