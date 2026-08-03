# Vehicle Graph

Vehicle Graph is a structured engineering knowledge repository for preserving
factory engineering information in a machine-readable, auditable form.

The project transforms service documentation into canonical JSON while
preserving provenance, applicability, and the distinction between factory
knowledge and vehicle-specific observations.

## Publication Representation

Vehicle Graph does not promote an undifferentiated PDF directly into graph
facts. It first preserves a language-independent representation of what the
publication visibly contains and how that content is organized. Translation is
one optional consumer of that shared foundation; it does not own page
decomposition.

The intended path is: publication evidence → source-visible representation →
optional linguistic interpretation → engineering interpretation → candidate
claims → accepted graph knowledge. Each transition remains reviewable and does
not imply automatic promotion. See the [architecture overview](docs/ARCHITECTURE.md),
[semantic-layer contract](docs/TRANSLATION_SEMANTIC_LAYERS.md), and
[source page-object taxonomy](docs/SOURCE_PAGE_OBJECT_TAXONOMY.md). The
candidate [page-decomposition model](docs/PAGE_DECOMPOSITION.md) describes how
those source-visible occurrences may be organized for review, and the
[page-to-translation binding model](docs/PAGE_TRANSLATION_BINDING_MODEL.md)
defines how linguistic artifacts may reference that structure without owning
it.

## Current Status

🚧 Documentation complete
⏳ Schema design in progress
🎯 Current milestone: One Diagram

## Start Here

1. docs/VISION.md
2. docs/ARCHITECTURE.md
3. docs/README.md
4. AGENTS.md

## Guiding Principles

- JSON is canonical.
- Git is the system of record.
- Every fact requires provenance.
- Factory knowledge is immutable.
- Vehicle-specific knowledge uses overlays.
