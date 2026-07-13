# One Diagram Working Material

This directory contains pre-canonical work for the [One Diagram milestone](../../docs/ONE_DIAGRAM.md).
Files here may record candidate claims, incomplete transcriptions, and unresolved
interpretations. Committing a file in this directory does not make any statement
accepted factory knowledge.

The [source inventory](source-inventory.md) identifies EWD168F, the proposed
evidence boundary, supporting pages, applicability, and evidence limitations.
The [headlight extraction ledger](headlight-extraction-ledger.md) organizes
candidate observations and questions within that proposed boundary. The ledger
depends on the inventory and remains subject to evidence review.

Supporting workspace records are:

- [source-language record](source-language.md), which identifies the EWD168F
  explanatory sections that govern interpretation;
- [source-language review checklist](source-language-review-checklist.md), which
  records completion of the required pre-extraction review gate;
- [evidence manifest](evidence-manifest.md), which tracks the provisional
  evidence set and capture status;
- [extraction boundary](extraction-boundary.md), which separates the proposed
  circuit boundary from its supporting dependencies and exclusions;
- [ambiguity log](ambiguity-log.md), which preserves unresolved questions
  without silently deciding them.

## Local Evidence Convention

The [EWD168F source catalog](../../sources/toyota/ewd168f/README.md) records the
expected private local evidence paths. Working files in this directory may
reference artifacts or derivatives under `.evidence/`, but ignored local files
must not be treated as committed repository state or accepted factory knowledge.

## Extraction Gate

Source-language review precedes candidate extraction. The checklist separates
hard blockers from soft ambiguities, and extraction authorization depends only
on the hard preconditions for the selected boundary. Soft ambiguities do not
block faithful transcription, but they must be attached to affected candidates
and reviewed before canonical acceptance. See the
[extraction boundary gate](extraction-boundary.md#source-language-review-gate).

## Next Work Sequence

1. Preserve and identify evidence.
2. Review the publication's source language and complete the applicable
   checklist items.
3. Finalize the extraction boundary and satisfy its review gate.
4. Transcribe visible source claims.
5. Review candidate claims against preserved evidence and cited source-language
   guidance.
6. Only then propose the minimum canonical schema required by the reviewed
   source material.
