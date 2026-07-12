# ADR 0005: Tools Consume the Graph

- Status: Accepted
- Date: 2026-07-11

## Context

Renderers, databases, search systems, extraction helpers, and AI systems change
more quickly than preserved engineering knowledge. Allowing a tool to own the
model would make the repository dependent on that tool.
Engineering knowledge has a much longer lifespan than any individual implementation technology.

## Decision

Tools may read, transform, validate, search, visualize, or propose modifications to canonical graph knowledge, but they never become the canonical representation themselves. They do
not define truth, own canonical state, or bypass provenance and applicability.
Generated artifacts remain reproducible projections.

## Consequences

Tools must adapt to the graph's documented meaning and remain replaceable. Some
tool-specific optimizations may be less convenient, but the knowledge stays
portable, inspectable, and independent of unnecessary infrastructure.
