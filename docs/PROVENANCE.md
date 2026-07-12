# Provenance

Every fact in Vehicle Graph must be traceable to evidence. Provenance is part of
the fact's meaning, not optional metadata.

## What provenance must establish

For factory knowledge, a reviewer should be able to determine:

- the publication or source artifact;
- its edition, revision, date, or other available identity;
- the precise page, section, figure, table, or equivalent location;
- whether the fact is quoted, transcribed, normalized, or interpreted;
- the extraction method (human, AI-assisted, OCR, or other), who performed or supervised the extraction, and who reviewed and accepted it;
- any ambiguity, conflict, or limitation in the source.

For a vehicle-specific observation, provenance should additionally identify the
vehicle unambiguously, the observation method, the date, and supporting evidence
such as measurements or photographs when appropriate and any tools or instruments used when they materially affect the observation.

## Authority and confidence

Factory publications are authoritative descriptions, but sources may conflict,
contain revisions, or cover different applications. Provenance preserves those
differences. Confidence labels, if later adopted, cannot replace evidence.

AI-generated content, conversational memory, community consensus, and uncited summaries are not primary
sources. They may help locate evidence, but they cannot satisfy provenance on
their own.

## Corrections

Accepted factory facts are not silently edited into a new meaning. A correction
must preserve the prior record and state why newer evidence supersedes or narrows
it. Git provides history; explicit provenance provides the semantic explanation.

## Provenance is never inherited

Derived views, reports, diagrams, and query results inherit provenance from the
facts they present. They do not become new sources of truth or replace the
underlying evidence.