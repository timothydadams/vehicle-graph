# ADR 0006: Reviewed Source Translation Is a Derived Interpretive Representation

- Status: Accepted
- Date: 2026-07-15

## Context

Vehicle Graph needs to work from factory publications whose language is not
English. The first demonstrated case is a Japanese Toyota electrical wiring
diagram that may later support an English representation normalized to Toyota
engineering terminology. Translation can make review and downstream extraction
more accessible, but it also introduces interpretive choices that must not be
confused with factory authorship or independent evidence.

The repository therefore needs a reviewable boundary between the
original-language publication, translation work, accepted graph knowledge, and
rendered outputs. That boundary must preserve the existing decisions that JSON
is canonical for structured knowledge, Git records reviewed state, every fact
requires provenance, applicability is explicit, and tools do not establish
truth.

## Decision

The original-language factory publication remains the authoritative source
evidence. A reviewed translation is a committed, reviewable **derived
interpretive representation**. It is not an independent factory source, must
not be presented as factory-authored English material, and does not replace the
original publication.

Translation occurs as specialized source processing before normal graph
extraction. A graph claim extracted through a reviewed translation must cite the
original publication location as primary evidence. Explanatory locations within
that publication remain interpretive dependencies when they define source
language materially required to read the primary evidence. The reviewed
translation may be cited separately as a **reviewed translation aid** or
supporting review artifact according to its actual role, but it must never be
the claim's sole provenance.

A reviewed translation aid is a repository-created, reviewed English
representation used to support accessibility, review, or downstream extraction.
It does not define the publication's source language, independently state a
factory claim, establish factory authorship or source meaning, prove entity
identity, or transfer applicability.

Translation work must keep these transformations distinct:

- source transcription;
- literal translation;
- normalized engineering wording;
- translator or contributor interpretation; and
- derived conclusions.

Source-local identifiers, page references, connector IDs, grid references,
qualifiers, and applicability marks are preserved exactly. Matching identifiers
or terminology across publications do not establish entity equivalence or
shared applicability. Another factory publication may provide explicitly
identified terminology evidence, but it cannot silently alter the source being
translated.

Language-fidelity review and engineering-terminology review are separate review
dimensions. Machine cross-checking may assist either review, but agreement
between tools or outputs is not human language verification and must not be
recorded as such.

Accepted translation records may later produce English Markdown, HTML, or PDF
editions. Those editions are noncanonical derived views, not factory-authored
publications. Acceptance of a translation does not accept any downstream graph
fact.

## Alternatives Considered

### Treat the English translation as an independent factory source

Rejected because the translation was not published by the factory and would
obscure where wording, interpretation, and applicability originated.

### Translate only while extracting graph candidates

Rejected because combining translation and extraction would make it difficult
to review language fidelity separately from engineering claim construction.

### Use another English publication as the translation authority

Rejected because another publication has its own identity, applicability, and
source language. It may support terminology normalization only when its role is
explicit, and matching labels do not prove cross-publication identity.

### Add translation as a new canonical knowledge layer

Rejected because translation is source processing that supports extraction,
not accepted factory knowledge or a competing canonical representation.

## Consequences

Translation requires an explicit boundary, original-source provenance, staged
review, and preservation of unresolved language or terminology questions.
Contributors may review engineering terminology without claiming competence in
the source language, while language-fidelity conclusions remain limited to
reviewers qualified to make them.

This separation adds review work, but it keeps the original publication
auditable, prevents translated wording from acquiring unsupported authority,
and permits downstream extraction to reuse an accepted reviewed translation aid
without bypassing normal candidate review and canonical acceptance.

## Scope Limits

This decision initially governs a small, representative Japanese Toyota EWD
pilot. It does not broaden the One Diagram milestone, authorize implementation
or bulk translation, define schemas or translation records, create services or
general multilingual infrastructure, or permit direct graph extraction during
translation. Source-catalog metadata and evidence setup for the Japanese
publication belong to later work.
