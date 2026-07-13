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
   source claims with provenance and applicability. Keep transcription,
   normalization, interpretation, and derivation distinct, and preserve
   soft ambiguity explicitly on affected candidates. Candidate extraction may
   begin once all hard preconditions for the selected boundary are satisfied.
7. **Independent review.** Check candidates against the complete evidence
   boundary, the cited source-language guidance, and the stated applicability.
   Verify that soft ambiguities were not silently resolved. A reviewer must
   reject unsupported completion or interpretation.
8. **Canonical acceptance.** Accept reviewed claims through the repository's
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

Use this decision test:

> Does the unresolved issue prevent faithful transcription?

- **Yes:** stop or narrow the boundary.
- **No:** record ambiguity and continue.

For the initial milestone, follow this workflow only as far as needed to produce
**One Diagram**. Automation may assist transcription or review, but generated
claims are not facts until supported by evidence and accepted through the same
process.

Extraction favors fidelity over completeness. An incomplete but accurate graph
is preferable to a complete graph containing unsupported assumptions.
