# Reviewed Source Translation Workflow

## Purpose

This workflow produces a reviewable English representation of a non-English
factory publication while preserving traceability to the original-language
publication. The initial demonstrated use case is a Japanese Toyota electrical
wiring diagram and normalized engineering wording consistent with evidenced
Toyota terminology.

A reviewed translation is a **derived interpretive representation**. It is not
factory-authored English material, an independent factory source, or a
replacement for the original publication. Translation prepares source material
for review and possible later extraction; it does not accept graph knowledge.

## Translation Stages

1. **Publication identity and applicability review.** Identify the publication,
   edition or revision, language, source-stated scope, and unresolved
   applicability without importing scope from another manual.
2. **Local evidence verification and fingerprinting.** Verify the lawfully
   obtained, private artifact under `.evidence/` and bind the work to its
   recorded fingerprint. The ignored artifact is not repository state.
3. **Publication-specific source-language review.** Locate and review the
   publication's definitions for notation, symbols, terminology, page
   organization, cross-references, and applicability marks before translating
   material that uses them.
4. **Translation boundary definition.** State the smallest coherent region to
   translate, its required interpretive dependencies and supporting evidence,
   and its exclusions. This boundary does not become a graph-extraction
   boundary automatically.
5. **Source transcription.** Record the visible source wording and source-local
   marks needed for review without translating or normalizing them.
6. **Literal translation.** Record the closest supportable English rendering of
   the transcribed language, preserving uncertainty and source structure where
   they affect meaning.
7. **Engineering normalization.** Add normalized engineering wording without
   erasing the transcription or literal translation. Identify terminology
   evidence from other publications explicitly.
8. **Ambiguity recording.** Record unresolved readings, translations,
   terminology choices, qualifiers, and boundary questions at the narrowest
   content they could materially change.
9. **Language-fidelity review.** Verify the transcription and literal
   translation against the original-language publication.
10. **Engineering-terminology review.** Verify that normalized wording preserves
    the source-supported engineering meaning and uses terminology evidence
    accurately.
11. **Translation acceptance.** Record the disposition of the bounded
    translation only after the required reviews. Acceptance does not accept a
    graph candidate or fact.
12. **Rendering of derived English views.** Produce English Markdown, HTML, or
    PDF views from accepted translation records when implementation is later
    authorized.
13. **Optional downstream graph extraction.** Apply the normal extraction and
    independent-review workflow, with the original publication as primary
    evidence, applicable same-publication explanatory pages as interpretive
    dependencies, and the accepted translation as a reviewed translation aid.

## Required Distinctions

- **Source transcription** records visible original-language text and marks
  without translating them.
- **Literal translation** expresses the closest supportable English wording
  before engineering terminology is normalized.
- **Normalized engineering translation** adds normalized engineering wording
  while preserving the literal translation and source wording.
- **Translator or contributor interpretation** explains a choice or meaning
  not directly stated by the source and is labeled as interpretation.
- **Derived conclusion** is reasoned from one or more source-supported claims;
  it is neither transcription nor translation.
- **Primary evidence** is the original publication location that visibly states
  or depicts the translated content and any downstream factory claim.
- **Interpretive dependency** is a source location within the original
  publication that defines notation, terminology, layout, or another convention
  materially required to read the primary evidence.
- **Reviewed translation aid** is a repository-created, reviewed English
  representation used to support accessibility, review, or downstream
  extraction. It does not define the publication's source language and does not
  independently state a factory claim.
- **Supporting evidence** establishes identity, context, applicability, layout,
  or review rationale without directly stating the translated engineering
  content.
- **Parallel-factory terminology evidence** is material from another identified
  factory publication used to support a terminology choice. It does not become
  evidence for the translated publication's engineering claim or applicability.

These roles are assigned per use. A relevant artifact does not acquire a
stronger evidentiary role merely because it is useful during review.

## Review Dimensions

Translation review records separate dispositions for:

- source reading and transcription;
- literal translation;
- engineering normalization; and
- the overall bounded translation.

Each disposition must identify what was reviewed, by whom or by what process,
and any unresolved ambiguity. Numeric confidence scores are not required and
must not substitute for evidence or review scope.

A contributor who does not know Japanese may perform
engineering-terminology review when the evidence supports that work. That
contributor cannot claim human language-fidelity review or human verification
of the Japanese reading. Machine comparison can identify questions and provide
a cross-check, but machine agreement does not prove correctness and must not be
recorded as human review.

## Cross-Publication Controls

Another Toyota English publication may provide parallel-factory terminology
evidence for normalized engineering wording. Its publication identity,
location, applicability, and role must be recorded separately.

Cross-publication evidence:

- cannot silently change, complete, or override the Japanese source;
- cannot establish that identically named or numbered connectors, components,
  terminals, or other objects are the same physical entity;
- cannot transfer applicability from one publication to another; and
- cannot become primary evidence for what the Japanese publication states.

Any proposed equivalence requires its own evidence and review outside the
translation decision.

## Provenance

The original publication page, figure, table, region, or equivalent source
location remains the evidentiary anchor throughout transcription, translation,
review, rendering, and downstream extraction. The preserved artifact's identity
and fingerprint bind the work to the reviewed evidence.

A translation must retain the source location and the transformation and review
history needed to reconstruct how its wording arose. A translation record must
never become the sole provenance for a factory engineering claim. Downstream
claims cite the original publication location as primary evidence, applicable
explanatory locations within that publication as interpretive dependencies, the
accepted translation separately as a reviewed translation aid, and other
material as supporting evidence only when that role is accurate.

## Ambiguity and Blocking

Use the repository's existing hard-versus-soft decision test:

> Does the unresolved issue prevent faithful transcription or translation of
> the selected boundary?

- **Yes:** stop or narrow the affected translation boundary without losing
  source meaning.
- **No:** preserve the uncertainty and continue without inventing completion.

An ambiguity attaches only to translated content it could materially change.
Shared page location, terminology category, or object association is not enough.
Terminology uncertainty may affect normalized wording without changing the
source transcription. Engineering-modeling uncertainty may remain open without
changing any translation stage. Keep those questions distinct and attach each
at its actual point of effect.

## Derived English Editions

English Markdown, HTML, or PDF editions are generated derived views of accepted
translation records. They are noncanonical, are not factory-authored, and do
not replace the original-language publication. A rendered edition must retain
enough provenance and disclosure for a reader to identify its source and
derived status.

## Initial Scope

The initial scope is a small, representative pilot using Japanese Toyota EWD
material. This workflow does not authorize bulk manual translation, a generic
multilingual service, a hosted application, translation implementation, or
direct graph extraction within the translation step. It does not alter the One
Diagram boundary. Publication metadata and source-catalog setup for the pilot
belong to later work.

## Implemented Translation Records

Canonical structured translations use page-or-bounded-region JSON records
validated by [`translation-record.schema.json`](../schemas/translation-record.schema.json).
Each record preserves ordered content units, original-publication primary
evidence, explicit coverage, and separate proposal, source-reading,
literal-translation, and engineering-terminology review states. The descriptive
record disposition applies only to the stated translation boundary: it does not
imply human language verification, accept a graph candidate or factory fact, or
make the translation an interpretive dependency.

The disposition vocabulary is descriptive. `working` is incomplete authoring;
`review_ready` declares a bounded record ready for its stated reviews;
`provisionally_accepted` accepts it only for the recorded `acceptance_scope`;
`fully_reviewed` records completion of the separately declared review evidence;
and `blocked` or `changes_required` prevents acceptance. A soft ambiguity may
remain when it is explicitly attached to the content it can change. A hard
source-language blocker prevents acceptance of its affected boundary. Neither
accepted disposition implies any particular review status: the four review
objects remain authoritative for those independent dimensions.

Committed records will live under `translations/<publisher>/<publication>/pages/`.
No real pilot record exists yet. Future English Markdown, HTML, and PDF editions
will be generated derived views of accepted JSON records, not editable or
factory-authored sources.

Run `python3 scripts/validate-translation-records.py <record.json> [...]` to
validate records. JSON Schema handles the stable shape and vocabularies; the
validator additionally checks source-coordinate presence, human-review
qualification, dependency targets, duplicate unit IDs, and coverage consistency.
