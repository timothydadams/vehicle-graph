# ADR 0001: JSON Is Canonical

- Status: Accepted
- Date: 2026-07-11

## Context

The project needs one durable, inspectable representation for structured
engineering knowledge. Multiple editable representations would create ambiguity
about which one is authoritative.

The canonical representation must be human-readable, version-controlled, auditable, and independent of any specific software implementation.

## Decision

JSON is the canonical representation of structured graph knowledge. Diagrams,
tables, databases, indexes, and other formats are derived views or boundary
formats and must be reproducible from canonical JSON.

## Consequences

JSON changes can be reviewed directly in Git, and tools remain replaceable. The
project accepts that JSON is not the best authoring or query format for every
task; convenience may justify additional derived representations, but never an additional canonical representation..
