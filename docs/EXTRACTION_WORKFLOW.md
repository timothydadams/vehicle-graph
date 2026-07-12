# Extraction Workflow

Extraction is an evidence-preserving engineering activity. It is not bulk text
conversion and it is not an invitation to infer undocumented facts.

## Proposed workflow

1. **Identify the source.** Record the publication, edition or revision, and the
   specific location being examined.
2. **Define the target application.** State the vehicle, configuration, and
   other applicability constraints known before extraction.
3. **Preserve evidence.** Retain enough source context for an independent
   reviewer to locate and interpret the material.
4. **Define the extraction boundary.** Identify exactly what portion of the
source is being extracted during this review. Prefer small, coherent units over
large sections.
5. **Extract atomic facts.** Record the smallest independently meaningful claims rather
than summarizing a larger section.
6. **Attach provenance and applicability.** Neither is optional or deferred.
7. **Distinguish transcription from interpretation.** Record ambiguity and
   uncertainty; do not silently resolve them.
8. **Review against the source.** A reviewer verifies the extracted facts against the source before they become
accepted graph knowledge.
9. **Resolve outstanding ambiguity.** Unresolved ambiguity is preserved explicitly rather than silently resolved.
10. **Commit through Git.** The reviewable change becomes part of the system of
   record.
11. **Generate a derived view.** Tools consume accepted facts without modifying
   them.
12. **Validate the derived view.** Check the result against both the source and the
    stated vehicle application.

For the initial milestone, follow this workflow only as far as needed to produce
**One Diagram**. Automation may assist transcription or review, but generated
claims are not facts until supported by source evidence and accepted through the
same process.

Extraction favors fidelity over completeness.

An incomplete but accurate graph is preferable to a complete graph containing
unsupported assumptions.