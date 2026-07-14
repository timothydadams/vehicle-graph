# Independent Review

## Purpose

Independent review evaluates the transformation from evidence into candidate
claims. Mechanical review preparation freezes and packages the extraction
before review begins:

```text
Source → source-language review → evidence inventory → extraction boundary
       → candidate extraction → review preparation → independent review
       → canonical acceptance
```

The governing question is:

> Can another careful reader reconstruct this candidate from the cited
> evidence, using only the publication's documented language, without relying
> on the extractor's private reasoning?

Review tests evidence sufficiency, use of publication-specific source language,
claim discipline, extraction-boundary integrity, applicability, provenance,
and ambiguity completeness and attachment accuracy. A technically plausible
candidate still fails when the source does not support it.

## Scope

Independent review covers one identified, frozen extraction package. It checks
candidate material; it does not make that material canonical. It does not
complete a source with domain knowledge, design a preferred graph shape, test a
vehicle observation against factory material, or broaden the agreed extraction
boundary for convenience.

The rules in [PROVENANCE.md](PROVENANCE.md),
[APPLICABILITY.md](APPLICABILITY.md), [SOURCE_LANGUAGE.md](SOURCE_LANGUAGE.md),
and [EXTRACTION_WORKFLOW.md](EXTRACTION_WORKFLOW.md) govern the review. This
document defines how a reviewer applies them independently.

## Review Preparation

Review preparation is a mechanical lifecycle stage, not another evidence
interpretation stage. From the repository root, inspect the proposed package
without writing files:

```shell
scripts/prepare-independent-review one-diagram --check
```

When the dry run is correct, create the package with:

```shell
scripts/prepare-independent-review one-diagram
```

The command discovers extraction artifacts from the workspace's small
declarative mapping, validates required paths and the explicit readiness signal,
and freezes the complete repository-backed input set at one commit. That set
includes the extraction artifacts, review-preparation configuration, readiness
signal, repository source and disclosure materials, governing documentation,
reviewer prompt, and package templates. Section-qualified disclosures freeze
their underlying files. The command refuses any uncommitted input or existing
target package, records the full commit and configuration path, assigns the next
`IR-NNN` ID unless `--review-id` is supplied, instantiates the templates, and
writes `REVIEW_TASK.md`.

Private evidence remains outside Git only when publication metadata identifies
it as a configured local source and records the SHA-256 that binds it. The
command verifies the actual file before continuing and records the verified
fingerprint. Without that binding, a source material is treated as a repository
input and must be committed; if it has no recorded hash, preparation reports
that its fingerprint was not verified. Generation is validated before output
is written and completed through an atomic directory rename.

The mapping may name exact sections when a working file combines neutral source
material with candidate rationale. Such disclosure choices and unavoidable
exposure remain explicit repository decisions; the command does not infer or
rewrite section boundaries. It does not assess semantic completeness, perform
review, modify extraction conclusions, resolve ambiguity, or perform canonical
acceptance. Commit the prepared package explicitly before launching review.

## Reviewer Independence

The reviewer should not have participated in the extraction under review. When
that is impractical, use a separate session with a clean task context and the
staged-disclosure procedure below. Operational context may identify the
repository, review package, frozen commit, and output path. It must not convey
extractor conclusions, suspected defects, preferred answers, disputed
interpretations, desired graph structure, or a belief that the extraction is
correct.

Independence reduces anchoring; it is not security-grade blindness. Repository
history and delayed files may remain discoverable. The reviewer must follow the
disclosure stages and record any premature exposure that could affect the
review.

The reviewer does not assume bad faith. The reviewer does assume that:

- a plausible candidate may be unsupported;
- a relevant citation may not prove the assertion;
- normalization may have changed source meaning;
- interpretive dependencies may be absent or over-attached;
- ambiguities may be missing, misclassified, or attached too broadly;
- the extraction boundary may be incoherent; and
- the source-language record may itself require correction.

## Evidence Authority

Keep the provenance roles distinct:

- **Primary evidence** directly shows or states the candidate claim.
- **Interpretive dependencies** define publication notation or conventions
  materially required to read that primary evidence.
- **Supporting evidence** establishes context such as identity, layout,
  applicability, or location without directly stating the engineering claim.

A notation page does not become primary evidence for an engineering claim
merely because it explains how to read the claim. A supporting page may be
relevant without proving the candidate. Each role must be accurate and no
required interpretive dependency may be omitted or irrelevant one attached.

The following material may locate evidence, challenge a reading, or suggest a
question, but cannot establish a claim on its own:

- generic engineering or automotive convention;
- physical or electrical plausibility;
- similar diagrams or another manufacturer's conventions;
- conversation history or extractor rationale;
- AI-generated summaries or confidence labels;
- derived diagrams; and
- agreement between extractor and reviewer.

## Review Prerequisites

Before review starts, the preparer must create a review package from the
[package template](../work/independent-review/template/) and identify:

- a stable review ID and extraction or milestone ID;
- the exact commit that freezes the candidate material;
- publication identity and applicability records;
- the evidence inventory and accessible primary source artifacts;
- the publication-specific source-language record and its source material;
- the frozen extraction boundary;
- the candidate ledger and ambiguity log;
- which materials are initially disclosed and intentionally delayed; and
- every required output path.

The reviewer must confirm that the frozen commit and each path resolve, that the
evidence needed for the boundary is available and legible, and that the
manifest does not substitute a local path for source identity or provenance.
Private source artifacts may remain outside Git, but the manifest must identify
their reviewed fingerprint or other binding and disclose their status.

If publication identity, boundary, required source language, or necessary
evidence is missing, the reviewer records the blocker rather than reconstructing
the package from extractor assumptions.

## Staged Disclosure

The general reading sequence in [docs/README.md](README.md) remains the normal
orientation path outside an active staged review. During an active review, the
reviewer reads repository-wide governing documentation but does not follow
index links into milestone- or extraction-specific working material unless the
manifest lists the exact artifact or section for the current disclosure stage.
For extraction-specific material, the review manifest controls disclosure even
when a broader repository index links to that material.

### Stage 1 — Independent source account

Initially disclose only:

- repository governing documentation;
- the review-package manifest;
- publication identity and applicability records;
- evidence inventory;
- frozen extraction boundary;
- relevant source artifacts; and
- publication-specific source-language material.

Where practical, delay the candidate ledger, candidate-attached ambiguity IDs,
the ambiguity log, extractor rationale, prior conclusions, downstream graph
shape, and vehicle-specific engineering expectations.

An existing working file may contain more than one role. In that case, the
manifest may disclose exact neutral sections during Stage 1 and delay sections
that contain candidate-specific rationale. Do not rewrite or omit publication
definitions merely to improve blindness. Record the section-level split and any
unavoidable exposure in the disclosure log.

The reviewer inspects the complete frozen source boundary and writes the
independent source account before opening delayed material. The account records
visible source constructs, expected independently meaningful claims, source
conventions actually used, unresolved readings, natural claim boundaries,
exclusions, boundary references, and evidence limitations. It is a concise
comparison baseline, not a second candidate ledger.

### Stage 2 — Candidate comparison

After saving the source account, disclose the candidate ledger. Perform both
review directions below without opening extractor rationale or the ambiguity
log merely to explain away a discrepancy.

### Stage 3 — Ambiguity and rationale check

After recording possible discrepancies, disclose the ambiguity log and only
the working rationale relevant to those discrepancies. Determine whether an
existing ambiguity properly preserves the issue, whether a new ambiguity is
needed, and whether each attachment passes the candidate-specific tests.

Record the time or commit at which each stage was completed. If delayed material
was seen early, disclose that in the review summary and assess whether a fresh
source account is required.

## Pass One: Source to Candidate

Begin with the frozen extraction boundary, not the ledger. Independently inspect
all primary evidence and the source-language and supporting material needed to
read it. Then compare the saved source account to the candidate set.

Check that:

1. every independently meaningful visible claim inside the boundary is present
   or explicitly unresolved, deferred, or excluded;
2. natural claim boundaries have not been fragmented until meaning is lost or
   combined so that assertions cannot be reviewed independently;
3. source constructs and boundary references have not been silently omitted;
4. excluded material has not entered merely through page proximity or domain
   expectation; and
5. the boundary remains the smallest coherent source area for the stated
   extraction.

This pass detects omissions and boundary defects that ledger-only review cannot
reliably find. Fidelity takes priority over apparent completeness.

## Pass Two: Candidate to Source

For each candidate, test every field and assertion against its evidence:

1. Locate the primary evidence and reconstruct the assertion from it.
2. Verify whether the transformation is transcription, normalization,
   interpretation, or derivation and that the label matches the work performed.
3. Verify every cited evidence role and reject citations that are merely
   relevant rather than probative.
4. Apply the publication's own source language before generic knowledge.
5. Confirm every necessary interpretive dependency and remove irrelevant ones.
6. Confirm the narrowest source-supported applicability; unknown scope must
   remain unknown.
7. Verify that source wording and normalized wording remain distinguishable
   wherever normalization could alter meaning.
8. Check attached ambiguities and look for missing ones.

An assertion that cannot be reconstructed is incorrect, unsupported, or
properly unresolved. Do not turn those three states into one another without
evidence.

## Ambiguity Review

Apply the ambiguity-attachment tests in [AGENTS.md](../AGENTS.md) and the
sequence in [EXTRACTION_WORKFLOW.md](EXTRACTION_WORKFLOW.md). Ask separately:

> Does the unresolved issue prevent faithful transcription?

and:

> What exactly could change in this candidate if the ambiguity were resolved?

The first question classifies a hard or soft precondition for the affected
boundary. The second determines candidate attachment. Attach an ambiguity only
when resolution could materially change a named candidate field or assertion.
Do not propagate it by category, object association, shared page, shared
connector, circuit membership, or structural adjacency.

Review must detect both missing and excessive attachments. Semantic uncertainty
does not automatically attach to structural claims; group meaning does not
automatically attach to visible correspondence; endpoint uncertainty belongs on
endpoint claims; boundary uncertainty belongs where treatment could change;
and applicability uncertainty belongs where scope could change.

## Finding Taxonomy

Classify a finding at the earliest failed workflow layer. A downstream symptom
does not become a candidate-only defect when its cause is a defective evidence
inventory, source-language record, boundary, or applicability decision.

`findings.md` is primarily for defects, blockers, disputed determinations, and
review-significant decisions. The reviewer does not ordinarily create one
finding for every successful candidate. Acceptance-ready candidates may be
listed in the review summary or a referenced inventory, and properly unresolved
claims may be listed there, through ambiguity-log references, or in a referenced
inventory. An individual `acceptance_ready_candidate` or
`properly_unresolved_claim` finding is optional and is used only when preserving
that verification decision is materially useful. Review output must not
duplicate the candidate ledger merely to record successful review.

| Finding class | Meaning and example | Required remediation | Scope and re-review |
| --- | --- | --- | --- |
| `candidate_defect` | A candidate misquotes, omits, combines, fragments, or mislabels otherwise adequate evidence; for example, a transcribed terminal differs from a legible label. | Correct the candidate and preserve the review finding and resolution. | Candidate-level plus directly dependent candidates. |
| `missing_ambiguity` | Evidence permits materially different readings or leaves material scope unresolved, but no ambiguity preserves the issue. | Add the narrowest ambiguity and attach it only to assertions it could change; adjust status if needed. | Affected candidates and attachment audit. Broader review only if the uncertainty crosses the boundary. |
| `incorrect_ambiguity_attachment` | An attachment cannot name a candidate field that could change, or a material ambiguity is attached to the wrong claim. | Remove or move the attachment; do not resolve the ambiguity merely to remove it. | Candidate-level and any other attachments created by the same rationale. |
| `source_language_defect` | Required publication guidance is missing, misread, or normalized incorrectly; for example, a connector convention was inferred rather than found in the publication. | Revisit the publication's explanatory material and correct the source-language record. Stop affected transcription if the issue is hard. | Re-review every candidate that uses the convention. |
| `evidence_inventory_defect` | Evidence is absent, misidentified, assigned the wrong role, or insufficiently bound to the publication. | Correct the inventory or preserve adequate evidence; do not repair candidates from memory. | Re-review every claim relying on the affected evidence or identity. |
| `extraction_boundary_defect` | The boundary omits necessary context, includes unrelated material, or is not coherently transcribable. | Narrow or redefine and freeze the boundary again; preserve explicit exclusions and references. | Repeat source-to-candidate review for the revised boundary, then affected candidate review. |
| `applicability_defect` | Scope is broadened, unsupported, conflated with target-vehicle context, or assigned at the wrong level. | Narrow or correct applicability and keep source-stated, inferred, and unresolved scope distinct. | Re-review every candidate inheriting or asserting the affected scope. |
| `unsupported_interpretation_or_derivation` | A claim depends on plausibility, domain expectation, or a derived conclusion not stated by the evidence. | Remove or relabel the assertion, or leave it unresolved until evidence supports it. | Candidate and all dependent claims; broader review if the inference shaped extraction. |
| `acceptance_ready_candidate` | The candidate is reconstructable, correctly scoped, fully traceable, and has only properly preserved ambiguities. | No extraction change; include it in the review disposition for human acceptance consideration. | No additional review unless a dependency changes. |
| `properly_unresolved_claim` | Evidence does not support a unique claim, and the candidate or ambiguity accurately preserves that limitation without guessing. | Leave unresolved and state what evidence could change the status. | Re-review only when relevant evidence, boundary, or source-language guidance changes. |

## Escalation and Remediation

Route remediation to the failed layer:

- Correct a candidate when adequate evidence and governing records support a
  different transcription, transformation label, evidence role, or field.
- Open a new ambiguity when uncertainty could materially change a claim and is
  not already preserved.
- Remove an ambiguity attachment when resolving it could change nothing in that
  candidate; leave the ambiguity open if it still matters elsewhere.
- Revisit source-language documentation when a publication-defined convention
  is missing, misread, or required to choose between transcriptions.
- Correct the evidence inventory when an artifact, source location, role,
  quality limitation, or source binding is wrong or absent.
- Narrow or redefine the extraction boundary when faithful review requires
  missing context or current inclusions are incoherent. Freeze the revision
  before review resumes.
- Narrow applicability whenever evidence supports less scope than the candidate
  claims. Never widen scope because no exception is known.
- Leave a claim unresolved when evidence cannot choose among material readings.
- Mark a candidate acceptance-ready immediately when both passes find no defect
  and any uncertainty is properly preserved.
- Require human adjudication for disputed evidence authority, a consequential
  boundary or applicability choice not resolved by repository rules, acceptance
  of an interpretation rather than a transcription, or any proposed exception
  to a project invariant.

Remediation belongs to the extractor or another designated contributor, not to
the independent reviewer during the review run. The reviewer records findings
and later verifies resolutions. This preserves a reviewable separation between
detection and correction.

## Re-review Rules

Each resolved finding records its resolution commit and required re-review
scope. Use the narrowest sufficient re-review:

- Candidate-only corrections require candidate-to-source review of that
  candidate and directly dependent claims.
- Ambiguity changes require rechecking every changed attachment and any claim
  whose status or confidence could change.
- Source-language changes require re-review of all candidates using the changed
  convention.
- Evidence identity, quality, or role changes require re-review of all claims
  that depend on that evidence.
- Applicability changes require re-review of all facts sharing or inheriting
  the affected scope.
- Boundary changes require a new source-to-candidate pass over the revised
  boundary, followed by candidate review for affected material.

Any change to the frozen candidate commit must be identified as a new review
revision. The package manifest and review summary must distinguish the original
reviewed candidate commit, the remediated candidate commit frozen for re-review,
the review revision, and the basis and scope of that re-review. Do not silently
continue against moving candidate content. A focused re-review may reuse the
earlier source account only when the relevant evidence and extraction boundary
remain unchanged; record `yes` or `no` and an explicit reason. Otherwise write
a new account.

## Review Dispositions

Package lifecycle state and review disposition are separate audit fields. The
manifest's `Package state` uses only:

- `draft`
- `frozen`
- `in_review`
- `findings_issued`
- `remediation`
- `re_review`
- `review_complete`
- `closed`

The review summary's `Disposition` uses only:

- `accepted` — every in-scope candidate is acceptance-ready and no unresolved
  ambiguity materially limits the reviewed claims.
- `accepted_with_unresolved_ambiguities` — candidates are faithful and
  review-complete, with properly recorded non-blocking ambiguities.
- `changes_required` — one or more remediable findings prevent an
  acceptance-ready result.
- `blocked_by_source_language` — required publication language is unknown or
  unreadable and faithful transcription cannot proceed for the boundary.
- `blocked_by_evidence` — required evidence is absent, inadequately identified,
  or too poor to support review.
- `boundary_revision_required` — the frozen boundary is not coherent enough to
  review faithfully.

Never combine package state and review disposition into one free-text field.
`review_complete` means the reviewer finished both review passes and ambiguity
review, recorded method validity, issued a disposition, completed the reviewer
declaration, and recorded the final timestamp. Findings may remain open.
`review_complete` does not mean accepted, remediated, closed, or canonically
accepted. Conversely, `accepted` is a review disposition only and does not mean
canonical acceptance. A package may also record applicability findings, but
narrowing applicability is ordinarily `changes_required`; if it makes the
selected boundary incoherent, use `boundary_revision_required`.

## Invalid Review

A candidate may fail a valid review. Separately, the review itself is invalid
when the method cannot support its conclusion. Every summary must explicitly
record `Method validity: valid` or `Method validity: invalid — <reason>`;
narrative compliance notes do not substitute for this field. An operative
review disposition may be recorded only when method validity is `valid`.

When validity is `invalid`, record the reason and explain whether a fresh or
corrected review is required. Do not move the package to `review_complete` or
invent a new disposition. A review is invalid when the reviewer:

- relies on engineering expectation or plausibility as evidence;
- inspects only the ledger without independently inspecting the frozen source
  boundary;
- resolves ambiguity without evidence;
- expands scope during review;
- silently rewrites source terminology;
- guesses away unresolved knowledge;
- performs the source account after exposure to delayed candidate conclusions;
  or
- reviews moving candidate content without freezing a new revision.

Premature disclosure is not automatically fatal, but the summary must explain
why independence remains adequate or require a fresh review.

## Completing the Review Record

After both review passes and ambiguity review, the reviewer:

1. records reviewer identity in the independent source account and summary;
2. records the review date and explicit method validity;
3. records one established review disposition when validity is `valid`;
4. completes the reviewer declaration and its final timestamp; and
5. moves the manifest package state to `review_complete`.

Run `scripts/check-independent-review <package-path>` to check these audit
fields. This validation checks record completeness and vocabulary, not the
substantive correctness of findings. Open findings and a `changes_required`
disposition are compatible with `review_complete`.

## Relationship to Canonical Acceptance

Independent review produces a review record and recommendation. It never writes
candidate claims into canonical state and never makes an acceptance decision on
behalf of the repository owner. For the One Diagram milestone, canonical
acceptance remains an explicit human-controlled act recorded separately from
the review disposition and linked to the exact reviewed and remediated commits.

The human acceptor verifies that required findings are resolved, reviewer
verification is complete, the accepted scope is explicit, and unresolved
ambiguities are knowingly retained. Rejection or deferral is valid; review does
not force uncertain material into the graph.

## Agent-Use Constraints

An agent reviewer must:

- use a fresh session where practical and receive only operational context;
- work on one identified frozen review package;
- follow staged disclosure and save the source account before opening delayed
  materials;
- inspect source evidence directly rather than trusting summaries;
- record explicit reviewer identity in both reviewer-owned outputs;
- avoid modifying extraction, ambiguity, boundary, applicability, or
  source-language artifacts during the review run;
- record structured findings and cite exact evidence;
- record explicit method validity, disposition, reviewer declaration, and final
  timestamp before marking the package `review_complete`;
- distinguish incorrect, unsupported, and unresolved claims;
- stop or narrow only where a hard precondition prevents faithful transcription;
  and
- refrain from canonical acceptance.

Automation may check completeness or consistency of the package, but it cannot
turn unsupported inference into accepted knowledge. A human or agent reviewer
who cannot access required source material records a blocker instead of relying
on the extractor's description of it.
