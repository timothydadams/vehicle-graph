# Agent Guidance

The purpose of this repository is to preserve engineering knowledge in a structured, auditable form without losing the context or provenance of the original source material.

This repository is currently in a documentation-first phase. Preserve that
boundary unless a human explicitly changes it.

## Project invariants

- JSON is canonical. Other representations are derived views.
- Git is the system of record for canonical data and documentation.
- Factory information is immutable. Corrections supersede facts; they do not
  silently rewrite history.
- Knowledge accumulates; it is not replaced. New information should add context rather than erase prior evidence.
- Vehicle-specific knowledge is represented only as an overlay on factory
  knowledge.
- Every fact requires provenance sufficient for a reviewer to trace it to its
  source.
- Applicability must be explicit. Never assume a fact applies to every vehicle.
- Prefer the simplest design that preserves these invariants.
- This is an engineering knowledge project, not an AI project. AI may assist with extraction, organization, validation, and reasoning, but every canonical fact must ultimately trace to documented evidence or an explicitly identified vehicle observation.

## Current scope

The initial milestone is **One Diagram**: one accurate, useful diagram for one
clearly identified vehicle application, produced from traceable knowledge.

Until implementation is explicitly requested:

- edit documentation only;
- do not create schemas, sample data, application code, generators, services,
  databases, build systems, or deployment configuration;
- do not add dependencies or infrastructure;
- do not turn future ideas into present commitments.

## Working style

Keep changes small and reviewable. State assumptions. Preserve source wording
where precision matters, while clearly separating quotation, transcription,
interpretation, and vehicle observation. Update or add an ADR when changing a
project invariant or a consequential architectural decision.

## Decision rule

When faced with multiple valid designs, prefer the simpler one unless the
additional complexity solves a demonstrated problem in the current milestone.

Avoid designing for hypothetical future products, manufacturers, or use cases. 
Generality should emerge naturally from solving real problems.

## Repository philosophy

If a contributor cannot understand a change by reviewing a Git diff,
the change is probably too large.

When in doubt, preserve information rather than discard it.