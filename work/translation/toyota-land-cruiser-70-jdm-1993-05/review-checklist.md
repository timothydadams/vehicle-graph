# Translation Pilot Review Checklist

## Status

This checklist records the Milestone 6 machine-assisted review status. It does
not define an implementation schema, accept a translation, or claim human
Japanese-language verification.

Evidence mapping is complete for `PILOT-TGT-001` through `PILOT-TGT-008` and
the five active dependencies `PILOT-DEP-002` through `PILOT-DEP-006`. The
missing dependency ID is deliberate. Before review, re-run the fingerprint
commands in [pilot-capture-manifest.md](pilot-capture-manifest.md). Mapping is
not language-fidelity review, and no item below is complete merely because its
page was located.

## Source-Language Fidelity (machine-assisted)

- [x] Every frozen target and active dependency was directly inspected.
- [x] Identifiers, printed pages, grids, punctuation, and qualifiers have
  explicit preservation rules.
- [x] Legibility was assessed without inventing unreadable content.
- [x] Candidate-specific ambiguities and one blocked full-page prose target are
  recorded.
- [x] Machine assistance is described and is not mislabeled as human review.
- [ ] Full transcription and literal translation (Milestone 7 work).
- [ ] Qualified human Japanese-language fidelity review.

## Engineering-Terminology Review

- [ ] Normalized engineering wording matches cited, relevant Toyota usage.
- [ ] Literal wording remains visible beside normalized wording.
- [ ] Normalization adds no unsupported engineering meaning.
- [ ] Parallel English sources are used only as terminology evidence and retain
  their own identity, location, and applicability.
- [ ] Original-publication applicability remains separate from supporting-source
  and target-vehicle applicability.
- [ ] No cross-manual component, connector, terminal, or entity identity is
  inferred from matching terminology or identifiers.
- [ ] Harness and component naming is internally consistent within the reviewed
  boundary.
- [ ] Connector and other source-local identifiers are preserved exactly.
- [ ] The engineering reviewer's role and review scope are recorded separately
  from language-fidelity review.

Milestone 6 did not perform engineering-terminology acceptance. Provisional
glosses remain distinct from normalized wording.

## Applicability, Graph, and Independent Review

- [x] Source model families, production start, and publication date remain
  distinct.
- [x] Destination, 1990 PZJ70 applicability, and EWD168F identity are not
  inferred.
- [ ] Target-vehicle selection remains future work.
- [ ] No graph extraction was performed.
- [ ] No independent translation review or translation acceptance occurred.

## Overall Pilot Disposition

All eight exact dispositions are recorded in
[pilot-review-matrix.md](pilot-review-matrix.md): three
`cleared_for_pilot_translation`, four `cleared_with_recorded_ambiguity`, and one
`blocked_pending_human_language_review`. No boundary revision is proposed.

An overall disposition does not accept translation wording, graph candidates,
or factory facts. Translation acceptance and graph acceptance remain separate.
