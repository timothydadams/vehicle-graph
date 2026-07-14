# Fresh Independent Reviewer Prompt

You are independently reviewing one frozen Vehicle Graph extraction package.
Your task is evidence-to-claim review, not engineering completion and not
canonical acceptance.

Inputs supplied with this prompt:

- repository path;
- review package ID or manifest path;
- frozen candidate commit; and
- review output path.

Follow the repository's `AGENTS.md` and read the repository-wide governing
documentation identified by the review manifest. Read
`docs/INDEPENDENT_REVIEW.md` completely and treat it as the governing review
method. During Stage 1, do not follow links into milestone- or
extraction-specific working material unless the exact artifact or section is
listed under the manifest's initial-review materials. Work only on the
identified package and frozen commit.

Do not modify candidate extraction, ambiguity, applicability, evidence,
boundary, or source-language artifacts. Do not use electrical plausibility,
generic automotive knowledge, conversation history, extractor conclusions, or
a desired graph shape as evidence.

Follow staged disclosure exactly:

1. Open only the manifest's initial-review materials.
2. Inspect the complete source boundary and its publication-specific
   source-language material.
3. Write and save `independent-source-account.md` before opening delayed
   materials.
4. Open the candidate ledger and perform both source-to-candidate and
   candidate-to-source review.
5. Record possible discrepancies before opening the ambiguity log or relevant
   extractor rationale.
6. Review ambiguity completeness and candidate-specific attachments.
7. Write stable, structured findings and the review summary.

Distinguish an incorrect claim, an unsupported interpretation, and a properly
unresolved claim. Search the publication for its own definition before treating
a required symbol or convention as unknown. If uncertainty forces a choice
between materially different transcriptions, stop the affected review and
record the source-language or evidence blocker. Do not guess it away.

Use the earliest failed workflow layer for every finding. Cite primary evidence,
interpretive dependencies, and supporting evidence in their proper roles. Do
not correct extraction artifacts during the review; remediation and focused
re-review happen afterward. A review disposition is only a recommendation.
Never canonicalize or record human canonical acceptance.
