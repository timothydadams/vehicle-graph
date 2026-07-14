# Independent Review Summary: IR-001

- Review ID: `IR-001`
- Frozen candidate commit for this revision: `381c3e936108ee3d63920adbe3830595f667de4d`
- Reviewer: `Codex — fresh independent-review session`
- Review date: `2026-07-14`
- Method validity: `valid`
- Disposition: `changes_required`

This is an independent-review recommendation for frozen candidate commit
`381c3e936108ee3d63920adbe3830595f667de4d`. It is not canonical acceptance.

## Result

Five open findings require remediation before the candidates can receive an
acceptance-ready disposition:

1. the Europe half of the frozen extraction boundary has no detailed candidate
   transcription;
2. several descriptive kinds add unsupported internal or load semantics;
3. `AMB-CON-004` is over-attached to direct C15 structural transcriptions;
4. `AMB-GND-001` is over-attached to legible neutral BH/BI references; and
5. printed page 165 is listed as support but is absent from the supplied,
   fingerprinted PDF.

The Except-Europe detailed transcription is otherwise substantially
reconstructable from the direct source for exact labels, fuses, headlamp and
relay terminals, C15 contact marks, visible joins, and conductor colors. That
partial result cannot support an accepted review disposition because the
frozen boundary is only half represented and the open attachment and
classification findings remain.

## Review method and independence

- Stage 1 used only the manifest-authorized initial materials and the direct
  source. `independent-source-account.md` was saved at
  `2026-07-14T16:33:37Z` before the candidate ledger was opened.
- Stage 2 opened only the candidate ledger. Possible discrepancies were saved
  in `findings.md` at `2026-07-14T16:36:14Z` before Stage 3 material was opened.
- Stage 3 then opened the ambiguity log and the exact delayed sections listed
  by the manifest. Final review completed at `2026-07-14T16:38:27Z`.
- No delayed material or existing review-output content was opened prematurely.
  The ledger's embedded ambiguity IDs, extraction rationale, and extractor
  review conclusions were unavoidable exposure already disclosed by the
  manifest.
- Both source-to-candidate and candidate-to-source passes were performed.
- No electrical plausibility, generic automotive expectation, conversation
  history, desired graph shape, or extractor conclusion was used as evidence.

## Evidence and scope limitations

The 276-page local PDF matches the recorded SHA-256, and printed pages 4-7,
188-191, and the selected supporting pages reviewed are legible. The PDF omits
printed page 165, and its relationship to the user's physical EWD168F remains
unrecorded. Those limitations are preserved in `IR-001-F005` and the independent
source account rather than guessed away.

Target-vehicle applicability remains unresolved. Both page-191 variants can be
transcribed neutrally, but neither may be asserted to apply to the identified
1990 RHD 1PZ PZJ70 without additional evidence.

## Required next review revision

After remediation, freeze the changed candidate inputs at a new remediated
commit and record a new review revision. The source account may be reused only
if the page-191 evidence and extraction boundary remain unchanged; page-165
evidence changes must be explicitly recorded and its dependent assertions
re-reviewed. The narrowest sufficient scopes are listed in
`finding-resolutions.md`.

No extraction artifact was modified, and no canonical acceptance was
performed, implied, or recorded.

## Reviewer Declaration

I evaluated evidence-to-claim fidelity and did not use engineering plausibility,
extractor conclusions, or a desired graph shape as evidence. This disposition
is not canonical acceptance.

- Reviewer: `Codex — fresh independent-review session`
- Recorded at: `2026-07-14T16:38:27Z`
