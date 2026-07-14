# Independent Review Findings: IR-001

## Review identity

- Review revision: `R0`
- Frozen candidate commit: `381c3e936108ee3d63920adbe3830595f667de4d`
- Review completed: `2026-07-14T16:38:27Z`
- Finding status: all findings open; remediation was not performed during review

## IR-001-F001 - Europe half of the frozen boundary is omitted

- Class: `candidate_defect`
- Severity: review-blocking
- Earliest failed workflow layer: candidate extraction
- Primary evidence: EWD168F printed page 191, `Headlight (Europe)`, locations
  `5-6` through `5-8`
- Governing boundary: `work/one-diagram/extraction-boundary.md`, which includes
  both Headlight (Except Europe) and Headlight (Europe)
- Affected candidate set: the source-to-candidate pass for the complete frozen
  boundary

The detailed ledger transcribes only Headlight (Except Europe), and its
related-system section explicitly says the Europe circuit is not extracted.
Printed page 191 visibly contains a separate Europe arrangement with fuses,
H5/H6, C13, C15, J1, the Dimmer Relay, D2, conductors, geographic qualifiers,
continuations, and boundary references. The delayed source inventory confirms
that both heavy-duty variants must remain represented until vehicle
applicability is resolved. `AMB-APP-001`, `AMB-DEP-001`, and `AMB-DEP-002`
preserve scope questions; they do not preserve the absent source claims.

Required remediation: transcribe the in-scope Europe material under the same
source-language and candidate-specific ambiguity rules. Alternatively, a human
may revise and refreeze the extraction boundary through the boundary workflow,
but unresolved target-vehicle selection is not evidence for selecting the
Except-Europe variant.

Re-review scope: repeat source-to-candidate review over the complete revised
boundary, then candidate-to-source review of every new or changed candidate and
its ambiguity attachments.

## IR-001-F002 - Descriptive kinds assert unsupported internal semantics

- Class: `unsupported_interpretation_or_derivation`
- Severity: review-blocking
- Earliest failed workflow layer: candidate extraction
- Primary evidence: EWD168F printed pages 188 and 191
- Interpretive dependency checked: printed page 5, common-connector naming rule
- Supporting evidence checked: printed pages 100-101 physical-location view and
  code table
- Affected candidates: summary-ledger H5/H6 `part/load` kinds;
  `OBJ-EX-C15-LIGHT`, `OBJ-EX-C15-DIMMER`, and `OBJ-EX-C13-HIGH`; corresponding
  summary-ledger kinds

The source supports the exact labels and codes and page 5 explains bracketed
common connector naming. It does not directly state the ledger's broader
`load`, `switch function within part`, or `indicator function within part`
ontology. The physical-location material names Combination SW and Combination
Meter but is not cited by the detailed object candidates and, in any case,
does not turn the modeling relationship into a literal page-191 transcription.
For C15, `AMB-CON-004` properly preserves the unresolved representation question
but does not make the current internal-semantic classification source-stated.
C13 has the same classification issue without an attached ambiguity.

Required remediation: retain exact source labels and codes, replace the kinds
with neutral source-supported descriptions, or label and support the additional
classification as interpretation. Do not resolve the C15 representation
question merely to remove the finding.

Re-review scope: affected object candidates and every claim that depends on
their asserted classification.

## IR-001-F003 - `AMB-CON-004` is over-attached to structural C15 claims

- Class: `incorrect_ambiguity_attachment`
- Severity: review-blocking
- Earliest failed workflow layer: candidate extraction / ambiguity attachment
- Primary evidence: EWD168F printed page 191, C15 contact-state tables and the
  visible R-W connection from Light Control SW `H / 4` to Dimmer SW `HF / 12`
- Affected candidates: the six C15 switch-contact rows and `SEG-EX-019`

`AMB-CON-004` asks how the separately printed C15 functions should later be
distinguished without unsupported internal semantics. The six table rows copy
visible contact marks under visible function headings. `SEG-EX-019` copies a
visible conductor and its printed endpoints. Resolving the representation
question cannot change those rows' printed terminal codes, states, continuity
marks, or the segment's endpoints and wire color. Under the semantic-versus-
structural attachment test, these attachments are broader than the claims they
qualify. The ambiguity remains material to the C15 object-classification or
representation assertions identified in IR-001-F002.

Required remediation: remove `AMB-CON-004` from the six direct contact-table
transcriptions and `SEG-EX-019`; retain it only on the narrowest representation
or function-distinction assertion that can materially change.

Re-review scope: every `AMB-CON-004` attachment and any candidate whose status
or wording changes as a result.

## IR-001-F004 - `AMB-GND-001` is over-attached to legible neutral references

- Class: `incorrect_ambiguity_attachment`
- Severity: review-blocking
- Earliest failed workflow layer: candidate extraction / ambiguity attachment
- Primary evidence: EWD168F printed page 191, lower Except-Europe continuations
- Affected candidates: `SEG-EX-024`, `SEG-EX-026`, `CONT-EX-BH`, and
  `CONT-EX-BI`

The reviewed capture legibly shows `BH` with W-B and LHD and `BI` with W-B and
RHD, together with the printed page-191 location legend. The candidates copy
those visible identifiers and do not assert a mapping to a separate ground or
continuation page. `AMB-GND-001` states that the identifiers are visible and
that their referenced endpoints and meaning still require confirmation.
Resolving that later mapping cannot change these neutral page-191
transcriptions. If a future claim maps BH or BI to external evidence, the
ambiguity may attach to that mapping claim.

Required remediation: remove `AMB-GND-001` from the four neutral page-191
candidates. Preserve the open external-endpoint/mapping question separately.

Re-review scope: every `AMB-GND-001` attachment and any later ground-mapping
candidate.

## IR-001-F005 - Listed page-165 evidence is absent from the supplied artifact

- Class: `evidence_inventory_defect`
- Severity: material evidence limitation; review-blocking for page-165-dependent
  assertions
- Earliest failed workflow layer: evidence inventory
- Evidence artifact: `.evidence/toyota/ewd168f/EWD168F.pdf`, SHA-256
  `44914602b067327a5ecf02bdc8667a31eac7de89915824f7744019f2249d7c48`
- Affected records: page index, evidence manifest, extraction-boundary support,
  source-inventory system-index findings, and any assertion relying on printed
  page 165

The fingerprinted PDF's printed-page sequence jumps from 155 to 173; printed
page 165 is not present. The package nevertheless lists page 165 as
system-index and variant-selection support and the delayed inventory records
specific page-165 findings. Those findings cannot be independently
reconstructed from the supplied private artifact. Printed page 191 itself
legibly labels both variants and their locations, so this absence does not
block neutral transcription of the two page-191 circuits; it does block review
of page-165-dependent support.

Required remediation: preserve and fingerprint an adequate page-165 image tied
to the publication, or correct the inventory/status and remove unsupported
reliance on the unavailable page.

Re-review scope: the corrected evidence inventory and every boundary,
applicability, or candidate assertion that cites or relies on printed page 165.

## Review-significant determinations without separate findings

- The target vehicle's Europe versus Except-Europe selection remains properly
  unresolved under `AMB-APP-001`; no target-vehicle applicability claim was
  accepted or inferred.
- `AMB-APP-002`, `AMB-DEP-001`, `AMB-DEP-002`, `AMB-CON-001`,
  `AMB-CON-003`, and `AMB-BOUND-001` preserve material questions in their
  stated scopes. Their presence does not cure IR-001-F001.
- `AMB-CON-002` is correctly unattached to the reviewed Except-Europe
  candidates because no specific selected crossing remained indeterminate in
  the legible capture. It must attach only if a particular competing
  transcription is identified later.
- The Except-Europe exact labels, fuse values, H5/H6 terminal numbers, relay
  depiction, C15 contact marks, and conductor transcriptions reviewed were
  generally reconstructable from printed page 191, subject to the findings
  above.
- These are review determinations only. No canonical acceptance was performed,
  implied, or recorded.
