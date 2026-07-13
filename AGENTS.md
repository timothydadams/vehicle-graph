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

## Source-Language-First Extraction Rule

Before detailed extraction from any factory publication, every contributor or
agent MUST:

- identify all sections within the same publication that define the notation,
  symbols, abbreviations, terminology, connector numbering, relay and junction
  conventions, continuation rules, page organization, state/contact tables,
  applicability notation, and interpretation guidance used by the target
  material;
- review those explanatory sections before interpreting the target diagram,
  table, figure, or procedure;
- record the required explanatory sections in the working source inventory,
  source-language record, or extraction boundary;
- apply the publication's own definitions before applying generic domain
  knowledge or contextual inference;
- search the publication for an explicit definition before opening an
  ambiguity about a symbol or convention;
- preserve the distinction between source-defined meaning, normalized wording,
  contributor interpretation, and derived conclusion; and
- stop detailed extraction when a required notation or convention remains
  unknown and could materially alter the transcription.

No source symbol or convention may be interpreted from context when the same
publication defines it elsewhere.

Source-language guidance is evidence for interpretation, but working notes
about that guidance are not automatically canonical factory facts.

### Hard and Soft Preconditions

A source-language uncertainty blocks candidate extraction only when it prevents
a faithful transcription of the selected boundary.

Hard preconditions block extraction because their absence makes faithful
transcription materially unreliable. Soft preconditions do not block direct
transcription when the source marks, labels, and relationships can still be
copied faithfully; they must remain explicit ambiguities attached to affected
candidate claims.

Classify an unresolved issue by asking:

> Would this uncertainty force a choice between materially different source
> transcriptions?

If yes, it is a hard blocker for the affected boundary. If no, it is soft and
must be preserved as ambiguity. Uncertainty about later schema design or
engineering interpretation is not a hard blocker when the source can still be
copied faithfully.

Extraction must stop for unreadable or undefined source language, not merely
for incomplete engineering understanding.

## Decision rule

When faced with multiple valid designs, prefer the simpler one unless the
additional complexity solves a demonstrated problem in the current milestone.

Avoid designing for hypothetical future products, manufacturers, or use cases. 
Generality should emerge naturally from solving real problems.

## Repository philosophy

If a contributor cannot understand a change by reviewing a Git diff,
the change is probably too large.

When in doubt, preserve information rather than discard it.
