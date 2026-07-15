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

### Translated Sources

When working from a non-English factory publication, every contributor or agent
MUST:

- preserve original-language source text where it is captured;
- keep source transcription, literal translation, and normalized engineering
  wording distinct;
- preserve source-local identifiers, page and grid references, qualifiers, and
  applicability marks exactly;
- avoid claiming human language-fidelity review unless a qualified human
  reviewer performed it;
- avoid using matching terms or identifiers from another publication to
  establish cross-publication entity identity or applicability;
- cite the original publication location as primary evidence for downstream
  factory claims; and
- treat rendered English Markdown, HTML, or PDF editions as derived views, not
  factory-authored or canonical records.

A reviewed translation may serve as a reviewed translation aid or supporting
review artifact according to its actual role. Interpretive dependencies remain
source-language locations within the original publication. Contributors and
agents must not collapse these roles. A reviewed translation is never an
independent factory source and does not replace normal extraction, review, or
acceptance. See [TRANSLATION_WORKFLOW.md](docs/TRANSLATION_WORKFLOW.md).

### Interpretive Dependencies

Candidate claims must cite primary evidence separately from interpretive
dependencies. Primary evidence is the source location that visibly states or
depicts the candidate. An interpretive dependency is a source location within
the same publication that defines how required notation, symbols, conventions,
abbreviations, page structure, connector numbering, relay or junction notation,
state tables, continuations, or applicability marks must be read.

Attach only interpretive dependencies that materially support how the candidate
is read. Do not cite every explanatory page merely because it was reviewed, and
do not describe a source-language page as though it directly contains the
engineering claim shown elsewhere. Omitting a necessary interpretive dependency
is a review failure. Adding an irrelevant dependency is also a review failure
because it obscures provenance.

> Provenance must explain both where a candidate is shown and, when necessary,
> how the publication tells us to read it.

### Candidate-Specific Ambiguity Attachment

Ambiguities attach at claim level. Attach an ambiguity only when resolving it
could materially change that candidate's text, endpoints, applicability,
boundary treatment, status, confidence, or interpretation. Broad propagation by
category, page proximity, or generic shorthand is prohibited. An ambiguity may
remain open without attaching to candidates it does not affect.

Conditionally hard ambiguities attach only at source locations where the hard
condition actually exists. If a crossing is clearly depicted, for example, an
open ambiguity about other indeterminate crossings does not belong on that
candidate.

> An ambiguity belongs on a candidate only when resolving it could materially
> change that candidate.

#### Ambiguity Attachment Application Tests

Before attaching an ambiguity, apply the relevant tests:

- **Test A — Semantic versus structural claim:** If the ambiguity concerns an
  object's broader meaning, classification, or later modeling while the
  candidate only records a visible terminal, label, wire, or endpoint, do not
  attach it unless resolving the ambiguity could materially change that
  structural claim.
- **Test B — Group meaning versus visible correspondence:** Attach uncertainty
  about a junction or connector group's broader meaning to the grouped-meaning
  claim when appropriate. Do not propagate it to a clearly visible label,
  position, terminal, or conductor whose correspondence would remain unchanged.
- **Test C — Positional or endpoint uncertainty:** Attach the ambiguity when
  resolving it could change which visible position, terminal, group, or endpoint
  the candidate maps to; otherwise, do not attach it.
- **Test D — Boundary ambiguity:** Attach the ambiguity when resolving it could
  move the candidate into or out of the extraction boundary or change whether
  it is an internal claim or boundary reference.
- **Test E — Applicability ambiguity:** Attach the ambiguity when resolving it
  could change the candidate's stated scope. Do not attach a later
  vehicle-selection question to a candidate already scoped neutrally to an
  explicit source variant unless that candidate asserts vehicle applicability.
- **Test F — Legibility or transcription ambiguity:** Attach the ambiguity when
  resolving it could change literal source text, wire color, terminal number,
  join status, or recorded connection, and adjust status or confidence as
  appropriate.

Touching the same object, appearing on the same page, using the same connector,
belonging to the same circuit, or being structurally adjacent is not sufficient
reason for attachment.

The following invariants apply:

- Semantic ambiguity does not automatically propagate to structural claims.
- Object association alone is not a sufficient attachment reason.
- Endpoint uncertainty belongs on endpoint claims; modeling uncertainty belongs
  on modeling claims.
- Attach the narrowest ambiguity that can materially change the candidate.

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
