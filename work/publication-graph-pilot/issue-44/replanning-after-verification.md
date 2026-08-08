# Issue 44 Replanning After Evidence Verification

## Status

Planning decision. Phase 2 has not begun.

Phase 1 is complete in PR #46. Its
[report](evidence-verification.md) remains
`blocked_pending_evidence_or_interpretation`: the page and source-visible
structure were verified, but the original exact-applicability gate prevented
candidate creation.

## Architectural question

Can the pilot preserve the original one-page engineering hypothesis as a
candidate with explicitly unresolved production applicability, review it, find
it ineligible, and deliberately reject it through approved authority without
weakening the applicability requirements for accepted knowledge?

## Decision

Yes. [ADR 0007](../../../adr/0007-publication-representation-and-candidate-first-extraction.md)
and the
[publication-to-graph extraction contract](../../../docs/PUBLICATION_GRAPH_EXTRACTION_CONTRACT.md)
distinguish a reviewable candidate from eligibility and canonical acceptance.
They require
material ambiguity to survive promotion, permit provisional extraction while
ambiguity blocks acceptance, and preserve rejected candidates and accurate
lower-layer observations. The independent-review method likewise permits
faithful candidates with properly recorded unresolved ambiguity. The
[applicability rules](../../../docs/APPLICABILITY.md) still require unknown
scope to remain unknown and prohibit widening by convenience.

Issue #44 may therefore create one candidate whose January 1995 production
scope remains explicitly unresolved, provided the controls below are met. The
candidate must be ineligible for canonical acceptance while that material
ambiguity remains. The intended end-to-end disposition is governed rejection,
unless new reviewed evidence resolves applicability and the issue first returns
to planning review.

This decision does not relax the rule for accepted knowledge. It changes only
the pilot's candidate-creation gate so the repository can test ambiguity
propagation, ineligibility, preservation, and deliberate rejection.

```text
engineering candidate
→ independent extraction review
→ graph-acceptance eligibility review
→ approved canonical-disposition authority
    ├── may accept only if eligible
    └── may deliberately reject whether eligible or ineligible
```

Extraction review determines evidentiary support. Eligibility review determines
whether acceptance prerequisites are satisfied. The approved authority makes
the explicit, attributable disposition. No earlier gate mutates canonical
data, an `ineligible` result is not itself a rejection, and PR merge is not a
canonical disposition unless repository governance separately designates and
approves it as such.

## Scope separation

The implementation must keep three applicability scopes distinct:

1. **Publication envelope:** the publication identity, Japanese-market
   context, listed model families, and production beginning May 1993.
2. **Page-visible engine scope:** the page `3-2` heading `電源(1HZ,1PZ)`, at
   its actual review status.
3. **Candidate-specific production scope:** the January 1995 variant applicable
   to the selected unmarked region. This remains unresolved because neither
   `○` nor `□` is associated with the region and the publication-wide search
   found no rule for unmarked material.

The first two scopes do not supply the third. Absence of a production mark is
not evidence that both ranges apply.

## Replanned candidate boundary

The one planning hypothesis is:

> Within the verified page `3-2` evidence boundary and page-visible `1HZ,1PZ`
> context, propose that lower terminal occurrence `1 (D)` on the depiction
> associated with `バッテリーNO.1` is electrically connected through the
> selected circuit-path depiction to one explicitly selected ground-symbol
> occurrence. Candidate-specific January 1995 production applicability remains
> unresolved because the region is unmarked and the publication defines no
> unmarked-material convention.

Phase 2 must select either the directly below ground-symbol occurrence or the
right-hand branch ground-symbol occurrence using an independently reviewable
source-location description and later stable occurrence identity. It must not
guess, create two relationships, or broaden the candidate to both grounds.

## Candidate-creation gate

Candidate creation may proceed only when:

- the verified artifact fingerprint, PDF page 40, printed page `3-2`, and
  `PILOT-TGT-008` mapping remain unchanged;
- lower terminal occurrence `1 (D)` is preserved exactly;
- one ground-symbol occurrence is selected explicitly and locatably;
- the material circuit-path depiction is represented neutrally and separately
  from proposed electrical connectivity;
- the page-visible `1HZ,1PZ` context is preserved at its actual review status;
- absence of a candidate-associated production mark is recorded as direct
  observation;
- the failed publication-wide search for an unmarked-material convention is
  cited without converting absence into a default;
- candidate-specific production applicability is explicitly unresolved;
- the material applicability ambiguity is attached to the candidate and every
  downstream stage it could change;
- candidate lifecycle state clearly prohibits canonical acceptance; and
- no default, union, transfer from another publication, or inference of “both
  production ranges” is introduced.

This gate authorizes proposal and review only. It does not establish
eligibility.

## Unresolved-applicability requirements

The candidate may record known dimensions alongside the unresolved production
dimension. The required unresolved-applicability record must preserve the
visible absence of `○` or `□` association with the selected region; the exact
page-local legend occurrence and ranges it defines for visible marks; PR #46's
complete bounded publication-wide search result; the publication envelope;
the page-visible `1HZ,1PZ` context; the unresolved candidate-specific January
1995 production dimension and reason it remains unresolved; the applicability
ambiguity identifier or later stable reference; its review state; the hard
prohibition on canonical acceptance; and downstream dependency and staleness
behavior. Translation cannot resolve or broaden the scope, and EWD168F or
general Toyota convention cannot transfer applicability.

The record must describe absence and uncertainty. It must not create a
synthetic mark, inferred mark attachment, default scope, “common to both”
scope, transferred applicability, or a candidate-specific legend relationship
that Phase 1 did not observe.

The Phase 1 negative finding remains historical evidence. New evidence may be
added through normal provenance and review, but it cannot silently mutate the
candidate or this plan.

## Independent extraction review

Independent review remains genuine and asks whether the proposed electrical
connectivity is faithfully supported by the frozen inputs. It separately
evaluates the label-to-depiction association, lower terminal `1 (D)`, selected
ground occurrence, circuit-path interpretation, material notation
dependencies, page engine scope, applicability-ambiguity attachment, and
evidence completeness.

Possible outcomes remain supported as proposed, correction required,
unsupported, or blocked. The plan does not instruct the reviewer to approve
connectivity merely to reach eligibility review. A favorable extraction review
does not resolve production applicability or confer eligibility.

## Eligibility blocker

A candidate with unresolved material production applicability is not eligible
for canonical acceptance. Eligibility review must confirm that:

- the ambiguity remains unresolved and correctly attached;
- no later artifact silently supplies a default scope;
- translation has not altered applicability;
- another publication has not transferred applicability;
- the publication envelope has not replaced candidate-specific scope;
- the candidate has not been broadened to the user's 1990 PZJ70; and
- every dependency remains fresh.

The expected result is `ineligible` if the ambiguity remains. Eligibility
review cannot resolve it by policy convenience and does not perform canonical
disposition.

## Governed rejection

An approved canonical-disposition authority may accept only an eligible
candidate and may deliberately reject a reviewed candidate whether eligible or
ineligible. The existing Issue #44 authority gate remains unchanged: the
authority must be proposed, explicitly approved by a human maintainer, and the
attributable decision, inputs, rationale, separate disposition, conflicts or
recusals, and preserved history must be recorded. Eligibility review does not
automatically reject a candidate; deliberate rejection is a separate governed
disposition.

The rejection must explain that the electrical interpretation may be
structurally supportable, but candidate-specific production applicability is
unresolved and the claim cannot enter accepted factory knowledge. It must
preserve the candidate, accurate lower-layer observations, ambiguity,
independent-review findings, eligibility result, and rationale.

Rejection is not evidence that the depicted structure is electrically false or
inapplicable to every vehicle. It means the repository lacks sufficient
support to accept the claim at the required scope.

## Lifecycle implications

The planned lifecycle test remains required. A controlled synthetic upstream
change must make dependent candidate, review, eligibility, and disposition
state explicitly stale or review-required without rewriting factory evidence.
Rejected state and prior dependencies remain recoverable. If reviewed evidence
later resolves production scope, it creates a planning and supersession event;
it does not retarget or erase the rejected record.

## Alternatives considered

### A. Preserve the candidate with unresolved applicability — selected

This tests ambiguity propagation, independent review, ineligibility, governed
rejection, and preservation while retaining the original page and engineering
question. It cannot produce an accepted graph fact and depends on approved
rejection authority, which are intentional constraints rather than defects.

### B. Replace it with an explicitly marked relationship on page `3-2`

This might exercise acceptance, but it substitutes a second candidate after
the first gate failed, requires a new evidence-verification boundary, and
optimizes away the result this pilot should test. It is not authorized.

### C. Treat unmarked material as common

Rejected. PR #46 found no same-publication evidence for that default.

### D. Use EWD168F or general Toyota convention

Rejected. Neither can supply candidate-specific applicability for this
publication.

### E. Close Issue #44 as blocked

Not selected. Existing doctrine permits a candidate to preserve ambiguity
while acceptance remains blocked, and deliberate rejection is an expressly
supported pilot outcome.

## Changes required to Issue 44

Issue #44 must record the completed Phase 1 result and this replanning PR,
preserve the original gate as history, narrow the candidate endpoints, replace
the obsolete exact-mark creation gate with the controlled gate above, make the
eligibility blocker explicit, preserve genuine independent review, and define
the meaning and governance of deliberate rejection. It remains open and Phase
2 remains not started.

## Phase 2 entry criteria

Phase 2 may begin only after this planning decision merges and Issue #44
reflects it. At entry:

- the Phase 1 report remains unchanged and blocked as historical evidence;
- the revised one-page, one-candidate boundary controls;
- Phase 2 must select exactly one ground-symbol occurrence;
- candidate-specific production applicability remains explicitly unresolved;
- the applicability ambiguity is mandatory and material;
- canonical acceptance is prohibited while it remains unresolved;
- independent extraction review remains genuine and eligibility remains a
  separate non-mutating decision;
- canonical-disposition authority still requires explicit maintainer approval;
- governed rejection is the intended disposition unless new reviewed
  same-publication evidence triggers planning review; and
- no new evidence silently changes the candidate or plan.

## Explicit non-goals

This decision does not implement Phase 2, select the ground occurrence, create
stable source-object identities, decompose the page, bind translation, create a
candidate or graph artifact, define schemas or fields, add candidate validators
or tests, perform extraction or eligibility review, propose or approve
authority, create a rejection artifact, modify private evidence, infer
unmarked applicability, select a replacement candidate, begin production work,
or validate another publication family.
