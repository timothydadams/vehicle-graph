# Schema Principles

This document defines constraints for repository schemas. The first implemented
schema covers reviewed translation records only; graph identifiers and graph
relationship taxonomy remain deferred.

## Principles

1. **Canonical JSON.** Structured knowledge is authored and reviewed as JSON.
   Alternate formats are generated or imported at a boundary.
2. **Facts are addressable.** Every accepted fact must have a stable identity so
it can be cited, reviewed, superseded, referenced, and consumed independently.
3. **Provenance is required.** A fact without traceable evidence is incomplete,
   not merely lower quality.
4. **Applicability is explicit.** The graph must express what a fact applies to
   and must preserve uncertainty instead of silently broadening scope.
5. **Factory facts are immutable.** Corrections create explicit new knowledge
   and relationships to earlier facts.
6. **Overlays are separate.** Vehicle-specific facts reference factory context
   but never rewrite it.
7. **Meaning precedes convenience.** Do not distort the model to suit one
   renderer, database, library, or extraction tool.
8. **Prefer boring structures.** Use straightforward JSON concepts and the
   smallest vocabulary that faithfully represents the milestone.
9. **Extension must be earned.** AAdd concepts only in response to reviewed source material or demonstrated
engineering needs, beginning with **One Diagram**.
10. **Validation assists review.** It detects structural and consistency violations but
never invents missing knowledge or silently resolves ambiguity.
11. **Schemas describe knowledge, not tools.** The canonical model should remain
independent of any particular query engine, visualization, database, or AI
system.

## Deferred decisions

Graph identifiers and relationship taxonomy remain intentionally undecided
until multiple representative diagrams have been modeled. Translation records
use JSON Schema plus narrow supplemental validation because their pilot page
types and provenance requirements have now been examined. That decision does
not pre-commit the graph schema to the same field names or file layout.
