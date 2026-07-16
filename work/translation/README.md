# Translation Working Material

This directory defines the reusable pre-canonical workspace for preparing a
bounded translation of an original-language factory publication. Files under
`work/translation/` are working records, not accepted translations or factory
knowledge. Committing a translation work file makes its history reviewable; it
does not make any wording accepted.

Private source evidence and local derivatives remain under `.evidence/` and are
not committed. The original publication remains primary evidence throughout
transcription, translation, review, rendering, and any later graph extraction.
A reviewed translation may later become a derived **reviewed translation aid**,
but it is not an independent factory source or an interpretive dependency.
Interpretive dependencies remain explanatory locations within the same
original-language publication.

Language-fidelity review and engineering-terminology review are separate gates.
Translation acceptance accepts neither graph candidates nor factory facts.
Translation-record implementation, schemas, renderers, and generated English
views remain deferred until explicitly authorized.

## Relationship to Other Material

```text
source catalog
    ↓
translation workspace
    ↓
future translation records
    ↓
future rendered English views
    ↓
optional graph extraction
```

The source catalog identifies the publication and private evidence convention.
A document workspace then records its pilot boundary, source-language gate,
evidence needs, provisional terminology, ambiguities, and review preparation.
Future translation records may be proposed only after that preparation. Any
future English Markdown, HTML, or PDF is a derived view. Optional graph
extraction remains a separate workflow with independent review and canonical
acceptance.

## Current Pilot

- [Reviewed Source Translation Workflow](../../docs/TRANSLATION_WORKFLOW.md)
- [ADR 0006: Reviewed Source Translation](../../adr/0006-reviewed-source-translation.md)
- [Japanese Land Cruiser 70 EWD source catalog](../../sources/toyota/land-cruiser-70-jdm-1993-05/README.md)
- [Japanese Land Cruiser 70 EWD translation workspace](toyota-land-cruiser-70-jdm-1993-05/README.md)
