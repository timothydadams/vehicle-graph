# ADR 0003: Vehicle-Specific Knowledge Uses Overlays

- Status: Accepted
- Date: 2026-07-11

## Context

An individual vehicle may differ from factory documentation because of
production variation, options, repairs, modifications, wear, or incomplete
factory coverage. Editing factory knowledge to match that vehicle would confuse
two different claims.

## Decision

Vehicle-specific information exists only as an overlay. An overlay identifies
the vehicle, references one or more factory records, and records confirmations, observations, measurements, modifications, and deviations
or deviations with its own provenance. It never mutates factory facts.

## Consequences

Tools must combine factory knowledge and a selected overlay when producing a
vehicle-specific view. The separation preserves both the factory record and the
vehicle's actual condition.
