# Extraction Workflow

Extraction is an evidence-preserving engineering activity. It is not bulk text
conversion and it is not an invitation to infer undocumented facts.

## Ordered Workflow

1. **Publication identity and scope review.** Identify the publication,
   edition or revision, language, source artifact, and the specific material
   being considered. Record limitations in the available evidence.
2. **Applicability review.** Record the publication's stated scope and the
   narrowest known vehicle, model, market, equipment, date, or other qualifiers.
   Preserve unresolved applicability rather than broadening it.
3. **Source-language review.** Identify and review the exact explanatory pages
   or sections that define the notation, symbols, abbreviations, terminology,
   connector and junction conventions, continuation rules, state/contact
   tables, page organization, and applicability notation needed to interpret
   the target source. Cite those dependencies in the working record, classify
   unresolved issues as hard or soft for the selected boundary, and stop only
   where a hard issue prevents faithful transcription.
4. **Evidence inventory.** Inventory the primary material and every supporting
   page needed to identify, interpret, and independently review it. Distinguish
   preserved evidence from working derivatives and unavailable material.
5. **Extraction-boundary definition.** State the smallest coherent source area
   being extracted and distinguish primary evidence, interpretive dependencies,
   related-system references, applicability support, and exclusions.
6. **Candidate extraction.** Record the smallest independently meaningful
   source claims. Each candidate records primary evidence; material interpretive
   dependencies when needed; supporting evidence when used; applicability;
   ambiguity IDs that directly affect the claim; and status or confidence. Keep
   transcription, normalization, interpretation, and derivation distinct.
   Apply the ambiguity-attachment review sequence below before adding each ID.
   Candidate extraction may begin once all hard preconditions for the selected
   boundary are satisfied.
7. **Review preparation.** Validate and mechanically package the committed
   extraction with `scripts/prepare-independent-review`. Record the frozen full
   Git commit, instantiate the review outputs, and make staged disclosure
   explicit. Preparation does not interpret evidence, change candidates, or
   perform review. Use `--check` first to inspect the proposed package without
   writing it.
8. **Independent review.** Follow the detailed
   [independent-review methodology](INDEPENDENT_REVIEW.md). Check candidates
   against the complete evidence
   boundary and stated applicability. Verify that each claimed interpretive
   dependency actually defines a convention used by the candidate, no required
   dependency is missing, and supporting evidence is not confused with primary
   evidence. Verify that no ambiguity was attached merely by category or page
   proximity, every attached ambiguity could materially change its candidate,
   and conditionally hard ambiguities are attached only where their hard
   condition exists. Repeat the ambiguity-attachment review sequence and reject
   any attachment that cannot identify a candidate field or assertion that
   could change. A reviewer must reject unsupported completion or interpretation.
9. **Canonical acceptance.** Accept reviewed claims through the repository's
   documented process and commit the reviewable change through Git. Only
   accepted knowledge may supply derived views.

Candidate extraction must not begin until stages 1 through 5 establish all hard
preconditions for the selected boundary. Soft preconditions are recorded and
carried into extraction. The source-language review must identify the exact
explanatory pages or sections used to interpret the target material.

A contributor must not infer the meaning of a source symbol merely from
electrical convention when the publication defines it. If the publication's
own guidance is incomplete or ambiguous, record that limitation explicitly
before proceeding. Detailed extraction must stop when the unresolved meaning
could materially alter the transcription.

A hard blocker may affect only part of a page, circuit, table, or procedure.
Extraction may proceed around it only if the boundary can be narrowed without
losing source meaning.

## Extraction Through a Reviewed Translation

When extraction relies on an accepted translation, the original-language
publication remains primary evidence. The reviewed translation may be cited as
an interpretive dependency when it materially supports how that evidence is
read, but translated wording is not an independent factory statement and must
not become the sole provenance for a candidate.

Translation acceptance and graph-candidate acceptance are separate review
gates. An accepted translation may support candidate extraction, but each graph
candidate still follows this workflow, cites the original source location, and
requires independent review and canonical acceptance. See the
[reviewed source translation workflow](TRANSLATION_WORKFLOW.md).

Use this decision test:

> Does the unresolved issue prevent faithful transcription?

- **Yes:** stop or narrow the boundary.
- **No:** record ambiguity and continue.

For candidate-level ambiguity attachment, use a separate test:

> Could resolving this ambiguity materially change this candidate?

- **Yes:** attach it.
- **No:** leave it in the ambiguity log but do not attach it here.

## Ambiguity-Attachment Review Sequence

For every proposed attachment:

1. Identify the candidate claim.
2. Identify the exact ambiguity.
3. State which candidate field or assertion could change if the ambiguity were
   resolved.
4. Apply the relevant semantic, group-meaning, positional, boundary,
   applicability, or transcription test.
5. Attach the ambiguity only when a material change is possible.

Use this concise decision test:

> What exactly could change in this candidate if the ambiguity were resolved?

If the answer is **nothing**, do not attach it.

For the initial milestone, follow this workflow only as far as needed to produce
**One Diagram**. Automation may assist transcription or review, but generated
claims are not facts until supported by evidence and accepted through the same
process.

Extraction favors fidelity over completeness. An incomplete but accurate graph
is preferable to a complete graph containing unsupported assumptions.
