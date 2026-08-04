# Reviewed Source Translation Roadmap

## Planning Status

This is an evolving planning document. It may be revised through normal review
as implementation teaches the project more. It does not override the governing
[reviewed source translation ADR](../../adr/0006-reviewed-source-translation.md),
[translation workflow](../TRANSLATION_WORKFLOW.md), or other architectural and
workflow documents.

## 1. Purpose

The reviewed source translation feature aims to produce:

- provenance-backed English representations of original-language factory
  publications;
- terminology normalized to evidenced Toyota engineering usage;
- independently reviewable translation records;
- generated English reference views; and
- eventual translation-aware graph extraction.

The Japanese publication remains primary evidence. Generated English output is
repository-created derived material and is not Toyota-authored.

Reviewed-source translation depends on the shared, language-independent
[publication-representation architecture](../ARCHITECTURE.md#publication-representation).
Publication representation is not owned by translation: it also supports graph
extraction directly and may support structured search, accessibility,
rendering, publishing, and revision comparison through later, separately
authorized work.

## 2. Governing Constraints

The [translation workflow](../TRANSLATION_WORKFLOW.md),
[extraction workflow](../EXTRACTION_WORKFLOW.md), and
[ADR 0006](../../adr/0006-reviewed-source-translation.md) govern this work:

- The original-language publication remains primary evidence. Translation
  records are derived interpretive representations.
- Reviewed translations are reviewed translation aids, not interpretive
  dependencies. Same-publication explanatory locations may be interpretive
  dependencies when they materially define how primary evidence is read.
- Source transcription, literal translation, normalized wording,
  interpretation, and derivation remain distinct.
- Language-fidelity and engineering-terminology reviews remain independent.
  Translation acceptance does not accept graph facts.
- Matching identifiers across publications do not establish entity equivalence
  or transfer applicability without explicit evidence.
- The publication identified by source-labeled part number `6742601` does not
  establish applicability to a 1990 PZJ70.
- Private factory evidence remains gitignored.
- JSON is canonical for implemented translation records. Rendered Markdown,
  HTML, indexes, and PDFs are derived views.

## 3. Branch and Delivery Model

`feature/translation` is the integration branch for the complete feature. Each
remaining translation PR branches from and targets `feature/translation`;
translation PRs must not target `main`. The completed feature branch will later
be merged into `main` when the planned feature work is sufficiently complete.

PR numbers used while planning are sequence labels only and may not match final
GitHub PR numbers. Milestone names are the durable references.

## 4. Status Summary

| Phase | Status | Completed work | Next action |
| --- | --- | --- | --- |
| Foundation | Complete | Architecture, source catalog, and workspace | Preserve governing boundaries |
| Record model | Complete | Translation record schema, supplemental validator, synthetic fixtures, and tests merged in PR #7 | Prepare and freeze pilot evidence |
| Pilot evidence preparation | Complete | Artifact and frozen mappings merged in PR #23 | Preserve frozen evidence boundary |
| Source-language review | Complete | All targets and dependencies reviewed; dispositions merged in PR #24 | Preserve the reviewed boundary and dispositions |
| Pilot translation | Complete | Three review-ready records merged in PR #25; schema, provenance, review separation, and dependency handling validated | Independently review the pilot records |
| Publication representation architecture | In progress | Semantic-layer and artifact ownership from Issue #28 and the pilot-grounded candidate source-page vocabulary from Issue #34 are complete | Design page decomposition in Issue #27, then complete the remaining Epic #26 investigations before expanding production translation |
| Independent review | Planned | Review dimensions defined | Prepare and run reproducible review |
| Terminology promotion | Planned | Provisional ledger seeded | Promote proven recurring terms |
| Publishing | Planned | Derived-view role defined | Build renderer, indexes, and companion PDF |
| Batch translation | Blocked | Bounded-work principle defined | Wait for the page-decomposition investigation before adding production-scale tooling or campaigns |
| Graph integration | Planned | Provenance roles defined | Define the page-decomposition-to-extraction contract before implementation |

## 5. Completed Milestones

### Milestone 1 — Architecture and workflow

Established translation architecture, provenance roles, review separation, and
implementation boundaries in [ADR 0006](../../adr/0006-reviewed-source-translation.md)
and the [translation workflow](../TRANSLATION_WORKFLOW.md). Completed by
[PR #4](https://github.com/timothydadams/vehicle-graph/pull/4).

### Milestone 2 — Source catalog

Cataloged the Japanese Toyota publication `トヨタ ランドクルーザー70 配線図集`,
source-labeled part number `6742601`, while preserving private evidence and
cautious applicability wording. See the
[source catalog](../../sources/toyota/land-cruiser-70-jdm-1993-05/README.md) and
[PR #5](https://github.com/timothydadams/vehicle-graph/pull/5).

### Milestone 3 — Translation workspace

Established the pilot boundary, evidence inventory, source-language review
gate, terminology ledger, ambiguity log, page inventory, and review preparation.
See the [pilot workspace](../../work/translation/toyota-land-cruiser-70-jdm-1993-05/README.md)
and [PR #6](https://github.com/timothydadams/vehicle-graph/pull/6).

### Milestone 4 — Translation record schema and validation ([issue](https://github.com/timothydadams/vehicle-graph/issues/8))

Completed by [PR #7](https://github.com/timothydadams/vehicle-graph/pull/7).
The repository now has a canonical JSON schema for page- or bounded-region
translation records, a supplemental provenance and consistency validator,
synthetic valid and invalid fixtures, and tests. Validation includes
coverage-to-content reconciliation, substantive text-state checks, independent
review dimensions, and enforceable `fully_reviewed` semantics. No real Toyota
source page was translated in this milestone.

### Milestone 5 — Pilot evidence preparation and page mapping ([issue](https://github.com/timothydadams/vehicle-graph/issues/9))

Complete, merged in [PR #23](https://github.com/timothydadams/vehicle-graph/pull/23).
The artifact fingerprint, mappings, targets, dependencies, and evidence
boundary are frozen.

### Milestone 6 — Pilot source-language review ([issue](https://github.com/timothydadams/vehicle-graph/issues/10))

Completed by [PR #24](https://github.com/timothydadams/vehicle-graph/pull/24).
The machine-assisted review assigned every frozen target a disposition and
reviewed all five active dependencies. The prose-heavy target remains blocked
pending qualified human language review; documented blockage was a valid
review outcome, not an incomplete convention inventory.

### Milestone 7 — Pilot translation records ([issue](https://github.com/timothydadams/vehicle-graph/issues/11))

Completed by [PR #25](https://github.com/timothydadams/vehicle-graph/pull/25).
The three targets cleared without material ambiguity—printed pages `2-3`,
`2-7`, and `3-2`—now have canonical, review-ready JSON records. The pilot
validated the translation-record schema, provenance model, independent review
dimensions, interpretive-dependency handling, and separation of provisional
literal English from engineering terminology. It did not accept translations,
normalize Toyota terminology, or extract graph facts.

## 6. Planned Milestones

### Milestone 7A — Publication representation architecture ([epic](https://github.com/timothydadams/vehicle-graph/issues/26))

Investigate a shared, language-independent representation of the source
publication's visual and semantic page structure. Review of the three pilot
records demonstrated that linguistic fidelity and provenance are practical,
while headings, legends, blocks, connector illustrations, harness drawings,
tables, identifiers, and graphical notation need clearer structural ownership
before translation expands.

This milestone is a successful architectural discovery from the One Diagram
vertical slice and Milestone 7 translation pilot, not a correction to either.
It changes no schema, translation record, validator, or graph model. Its seven
investigations will define proposed semantic layers and
artifact ownership, a source page-object taxonomy, page decomposition and
hierarchy, identifier taxonomy, page-object or region bindings to translation,
coverage across publication families, and the downstream graph-extraction
contract. These are investigations and design recommendations, not authorization
for a schema or implementation decision. Further production-page translation
and batch campaigns are gated on their completion; independent review of the
existing pilot records may continue.

Issue [#28](https://github.com/timothydadams/vehicle-graph/issues/28) defined
semantic layers and artifact ownership in
[Translation Semantic Layers and Artifact Ownership](../TRANSLATION_SEMANTIC_LAYERS.md).
Issue [#34](https://github.com/timothydadams/vehicle-graph/issues/34) defined the
pilot-grounded, page-scoped candidate vocabulary in
the [Source Page Object Taxonomy](../SOURCE_PAGE_OBJECT_TAXONOMY.md); it remains
subject to broader publication-family validation in Issue #31. Both completed
investigations establish publication representation below translation. Issue
#27's candidate [Page Decomposition](../PAGE_DECOMPOSITION.md) design and Issue
#29's [Publication Identifier Taxonomy](../PUBLICATION_IDENTIFIER_TAXONOMY.md)
are also complete. Issue #30's completed
[Page-to-Translation Binding Model](../PAGE_TRANSLATION_BINDING_MODEL.md) defines
how linguistic artifacts may reference stable source-visible occurrences or
declared regions without owning publication structure and was delivered by
[PR #40](https://github.com/timothydadams/vehicle-graph/pull/40). Issue #31's
[Publication Family Evaluation](../PUBLICATION_FAMILY_EVALUATION.md) now
stress-tests those completed concepts against all seven required families. It
recommends that Issue #32 may proceed after review with documented evidence
limitations; Issue #32 remains a separate, open, unstarted investigation.

Current Epic #26 status: #27, #28, #29, #30, and #34 complete; #31 under review;
#32 open and unstarted.

Completing publication representation will unblock production translation and
translation binding, and will establish shared inputs for structured search,
future publishing, and graph extraction. This roadmap does not claim that all
of those consumers will be implemented on `feature/translation`.

### Milestone 8 — Independent-review preparation ([issue](https://github.com/timothydadams/vehicle-graph/issues/12))

Deliver frozen review inputs, source-fingerprint verification, a review
manifest, hard-blocker checks, stale-input detection, reproducibility tests, and
separate language and engineering review packages.

### Milestone 9 — Pilot independent review and correction ([issue](https://github.com/timothydadams/vehicle-graph/issues/13))

Review transcription completeness, literal fidelity, terminology normalization,
qualifiers, applicability, table and diagram coverage, unsupported
interpretation, supporting-source roles, ambiguity attachment, and review-status
accuracy. Preserve reviewer outputs and corrections as reviewable artifacts.

### Milestone 10 — Structured terminology store ([issue](https://github.com/timothydadams/vehicle-graph/issues/14))

Promote recurring terminology only after the pilot proves the representation.
Store the Japanese term, literal meaning, normalized Toyota English, scope,
normalization evidence, proposal lifecycle, language-fidelity status,
engineering-terminology status, and ambiguity and rejection history.

### Milestone 11 — Review renderer ([issue](https://github.com/timothydadams/vehicle-graph/issues/15))

Generate auditable Markdown or HTML from canonical JSON, prioritizing Japanese
source text, literal English, normalized engineering wording, source
identifiers, provenance, ambiguity, and review status. Do not prioritize
factory-layout imitation yet.

### Milestone 12 — Translation-derived indexes ([issue](https://github.com/timothydadams/vehicle-graph/issues/16))

Generate publication/page, component, connector or source-local-identifier,
harness, system, terminology, and unresolved-ambiguity indexes. The provisional
source-catalog page index remains a lightweight navigation scaffold, not the
finished translated index.

### Milestone 13 — English companion PDF ([issue](https://github.com/timothydadams/vehicle-graph/issues/17))

Generate a clearly disclosed repository-created reference edition, prioritizing
page correlation and provenance over visual imitation.

### Milestone 14 — Batch preparation tooling ([issue](https://github.com/timothydadams/vehicle-graph/issues/18))

Add local tools for page rendering, draft-record initialization, text-layer
extraction where available, repeated-string detection, terminology suggestions,
batch validation, and unreadable-region reporting. No tool may automatically
accept translation work. Production-scale tooling must follow the page
decomposition architecture rather than hard-code the pilot's grouped units.

### Milestone 15 — Full-publication translation campaign ([issue](https://github.com/timothydadams/vehicle-graph/issues/19))

Translate the publication in bounded, reviewable batches. This is not one PR;
use chapter- or page-type-oriented campaigns as evidence and review capacity
support. Do not begin the campaign until the page decomposition investigation
defines the canonical intermediate structure.

### Milestone 16 — Translation-aware graph extraction ([issue](https://github.com/timothydadams/vehicle-graph/issues/20))

Allow extraction to cite the original publication as primary evidence,
same-publication explanatory locations as interpretive dependencies, an
accepted translation record as a reviewed translation aid, and parallel
English Toyota material as supporting terminology evidence. Graph acceptance
remains independent.

## 7. Dependencies and Decision Gates

- Prove the schema before real records scale.
- Fingerprint and map the local PDF before reproducible page work.
- Review required source-language conventions before translating affected
  pages.
- Complete the publication representation architecture investigation before expanding
  production translation beyond the current pilot records.
- Require successful pilot review before full-publication scaling.
- Promote terminology only after repeated real usage demonstrates the need.
- Begin renderer and publishing work after translation records stabilize.
- Define the page-decomposition-to-graph-extraction contract before graph
  integration and begin implementation only after the translation workflow is
  accepted.

These are gates, not artificial serialization: local artifact preparation may
proceed independently where it does not require record binding, and other safe
preparation work may proceed in parallel.

## 8. Explicit Non-Goals

- A hosted translation service or database.
- A generic universal multilingual platform.
- Automatic acceptance or replacement of factory evidence.
- Claims of Toyota authorship for repository-created output.
- Connector equivalence based on matching identifiers.
- Retroactive applicability to the user's 1990 PZJ70.
- Graph extraction during translation.
- Layout-faithful reconstruction before content fidelity is proven.

## 9. Definition of Pilot Success

The pilot succeeds when representative page types have structured records;
each record remains traceable to original evidence; transcription, literal
translation, and normalization are distinct; coverage and omissions are
explicit; language and engineering review remain separate; hard ambiguities
block only affected boundaries; supporting English publications remain
properly scoped; independent review can reproduce and challenge the work;
generated English views can be rebuilt from JSON; and no graph fact is accepted
implicitly.

## 10. Roadmap Maintenance

Update this roadmap when milestone sequencing changes materially. Completed
milestones should link to merged PRs, and active work should link to GitHub
issues. Issue closure does not change architectural rules. ADRs and governing
workflow documents take precedence. Issue details may evolve without rewriting
historical completed milestones; material scope changes should be reflected in
both the roadmap and the affected issues.

Tracking: [Epic: Reviewed source translation feature](https://github.com/timothydadams/vehicle-graph/issues/21)
