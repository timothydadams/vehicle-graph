# ADR 0002: Factory Records Are Immutable

- Status: Accepted
- Date: 2026-07-11

## Context

Factory publications may be revised, contradicted, or later understood more
precisely. Silently changing an accepted fact would erase what was previously
recorded and weaken auditability.

## Decision

Accepted factory information is immutable in meaning. New evidence may
supersede, correct, qualify, or narrow an earlier fact through an explicit new
record and relationship. It must not overwrite history as though the earlier
record never existed.

Vehicle-specific observations, community knowledge, and later factory publications must never modify an existing factory record; they must reference it through explicit relationships.

## Consequences

Tools and consumers must account for supersession and revision. The graph retains a
faithful history, while Git records the repository changes that introduced it.
Clerical corrections that do not alter meaning may be handled separately by a
future documented policy.
