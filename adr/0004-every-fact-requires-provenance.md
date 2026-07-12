# ADR 0004: Every Fact Requires Provenance

- Status: Accepted
- Date: 2026-07-11

## Context

Engineering claims without traceable evidence cannot be independently verified,
scoped, corrected, or safely reused.

## Decision

Every fact must carry provenance sufficient to locate and evaluate its evidence.
This applies to factory facts and vehicle-specific overlay facts. A candidate
claim lacking provenance is not accepted graph knowledge.
Provenance may reference factory documentation, vehicle observations, service records, measurements, photographs, or other explicitly identified evidence.

## Consequences

Extraction requires more care, and some seemingly useful claims will remain
outside the graph until supported. In return, consumers can expose sources,
reviewers can audit decisions, and disagreements can be represented without
discarding evidence.
