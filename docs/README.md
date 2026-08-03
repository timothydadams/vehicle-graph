# Documentation Guide

This repository is intentionally documentation-first. Contributors should read
the documents in the following order to understand the project's purpose,
decisions, and working constraints.

## Recommended Reading Sequence

1. [VISION.md](VISION.md) — Why the project exists.
2. [ARCHITECTURE.md](ARCHITECTURE.md) — How engineering knowledge flows through
   the repository, including publication representation as the shared,
   language-independent foundation for downstream interpretation and use.
3. [adr/](../adr/) — The accepted architectural decisions that govern the project.
4. [AGENTS.md](../AGENTS.md) — Rules for humans and AI contributors.
5. [PROVENANCE.md](PROVENANCE.md) — How engineering facts become trustworthy.
6. [APPLICABILITY.md](APPLICABILITY.md) — How scope and vehicle applicability
   are represented.
7. [SOURCE_LANGUAGE.md](SOURCE_LANGUAGE.md) — How a publication's own technical
   language governs interpretation.
8. [TRANSLATION_WORKFLOW.md](TRANSLATION_WORKFLOW.md) — How non-English source
   material becomes a reviewed English interpretive representation.
9. [EXTRACTION_WORKFLOW.md](EXTRACTION_WORKFLOW.md) — The process for converting
   source material into accepted graph knowledge.
10. [TRANSLATION_SEMANTIC_LAYERS.md](TRANSLATION_SEMANTIC_LAYERS.md) — Semantic
    ownership, dependency, authority-level, mutability, and promotion boundaries
    from factory evidence through source-visible structure, linguistic
    interpretation, graph acceptance, and publishing.
11. [SOURCE_PAGE_OBJECT_TAXONOMY.md](SOURCE_PAGE_OBJECT_TAXONOMY.md) —
    Pilot-grounded, language-independent candidate vocabulary for page-scoped
    source-visible objects, without engineering or graph promotion; broader
    publication-family validation remains deferred.
12. [PAGE_DECOMPOSITION.md](PAGE_DECOMPOSITION.md) — Candidate composition model
    for source-visible occurrences and material visible associations within a
    reviewable page boundary.
13. [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md) — How a fresh reviewer tests
    the evidence-to-claim transformation before canonical acceptance.
14. [SCHEMA_PRINCIPLES.md](SCHEMA_PRINCIPLES.md) — Constraints that future schemas
    must satisfy.
15. [NON_GOALS.md](NON_GOALS.md) — What the project intentionally avoids.
16. [ONE_DIAGRAM.md](ONE_DIAGRAM.md) — Scope and completion criteria for the
    current milestone.
17. [One Diagram working material](../work/one-diagram/README.md) —
    Pre-canonical inventories, candidates, boundaries, and unresolved questions
    for the current milestone.
18. [Independent review working material](../work/independent-review/README.md) —
    Reusable pre-canonical review-package convention and preparation command.
19. [FUTURE_IDEAS.md](FUTURE_IDEAS.md) — Parking lot for ideas that are
    intentionally deferred.

Publication representation provides the language-independent foundation that
translation and extraction can consume now and that search, accessibility,
rendering, and revision comparison may consume in future work. Listing a
consumer here describes an architectural relationship, not an implemented
feature.

## Planning and Status

- [Reviewed source translation roadmap](roadmaps/reviewed-source-translation.md)
  — Evolving milestone plan and work-tracking links for the reviewed translation
  feature. Governing ADRs and workflows take precedence.

## Current Milestone

Current milestone: One Diagram

The goal is to model one trustworthy wiring diagram for one explicitly identified
vehicle application. Every future architectural decision should support this
milestone before expanding the project's scope.
