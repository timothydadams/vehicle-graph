# Issue 44 Phase 1 Evidence Verification

## Status

`blocked_pending_evidence_or_interpretation`

## Scope

- Publication ID: `toyota-land-cruiser-70-jdm-1993-05`
- Verified artifact: `sha256:1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6`
- PDF page: 40
- Printed page: `3-2`
- Frozen target: `PILOT-TGT-008`
- Inspected same-publication dependencies: `PILOT-DEP-003`,
  `PILOT-DEP-004`, and `PILOT-DEP-005`
- Inspection date: 2026-08-05
- Contributor: Codex (OpenAI), acting as an assisted repository contributor
- Tool assistance: `shasum`, `stat`, Poppler `pdfinfo` and `pdftoppm`,
  ImageMagick crop preparation, direct high-resolution visual inspection, and
  comparison with the committed inventory, source-language review, ambiguity
  ledger, and review-ready translation record

This is an evidence-verification and planning-refinement report. It is not an
independent extraction review, a language-fidelity review, a translation
acceptance, an engineering-candidate record, or a canonical disposition.

The report-local labels below have no identity outside this report and are not
stable repository-assigned source-object identities.

## Candidate hypothesis

Issue 44 provisionally asks whether, for the exact source-supported engine and
production scope, the terminal occurrence visibly marked `1` on the depiction
associated with `バッテリーNO.1` may be proposed as electrically connected to
the depicted ground reference, based on the material circuit-path depiction and
source-defined notation.

That statement was tested as a hypothesis. It is not accepted by this report.

## Artifact verification

The expected local PDF was found at the repository's private-evidence path. Its
SHA-256 matches the expected fingerprint exactly. The file is 101,456,077 bytes
and contains 90 PDF pages. The file was not modified.

Direct inspection verified that PDF page 40 visibly bears printed page `3-2`,
the centered title `電源(1HZ,1PZ)`, and the lower publication mark containing
`品番6742601`. These observations agree with the frozen mapping of PDF page 40
to `PILOT-TGT-008` in the Milestone 7 inventory and evidence manifest. A donor
watermark is also visible at the lower page edge; it was treated as a scan or
donor artifact, not as factory content or evidence for the candidate.

The `.evidence/` boundary and every working-render path were verified with
`git check-ignore` before rendering. `.gitignore` ignores the entire boundary,
and no parent rule re-includes it. Before and after inspection, Git reported no
tracked or staged private evidence. The full page was inspected before a
private battery-region crop was made for closer review.

## Source-visible findings

The following labels are local to this report:

- `observed-label-a`: the exact visible string `バッテリーNO.1`.
- `observed-depiction-a`: the adjacent rectangular battery-symbol depiction.
- `observed-terminal-mark-a`: the lower occurrence shown as `1` with circled
  source-local letter `D`.
- `observed-path-a`: the path portions leaving that lower occurrence.
- `observed-ground-a`: the ground-symbol occurrence directly below the lower
  terminal occurrence.
- `observed-ground-b`: the second ground-symbol occurrence reached by the
  right-hand branch.

### Label occurrence and depiction

`バッテリーNO.1` is exact and legible. It is placed vertically immediately to
the right of `observed-depiction-a`; no enclosure or leader joins the label to
the depiction. The visible association is by close adjacency and placement.
The neighboring `バッテリーNO.2` label and depiction use the same arrangement
to the left, but their spacing and separate depiction boundaries do not create
a plausible alternate target for `observed-label-a` at the inspected
resolution.

Identifying the exact occurrence does not require accepting an English
translation. The review-ready translation record preserves the exact Japanese
label and provisionally groups it with the page's circuit labels. That broad
grouping neither contradicts nor independently proves the more specific
label-to-depiction association recorded here.

### Terminal marks

`observed-depiction-a` has two distinct visible occurrences of `1`: an upper
`1` beside circled letter `C`, and a lower `1` beside circled letter `D`.
Consequently, the hypothesis's phrase “the terminal occurrence visibly marked
`1`” is not independently locatable without further qualification.

`PILOT-DEP-004` defines the applicable page convention for connector and
terminal presentation: the number at the connection is the terminal number,
while the circled letter relates the occurrence to the lower connector strip.
Under that source convention, `observed-terminal-mark-a` is the lower terminal
number `1` associated with source-local connector occurrence `D`, whose lower
strip entry is `F1`. The mark is legible; scan wear, bleed-through, and line
overlap do not affect this reading. The upper `1 (C)` is the nearby occurrence
that could be confused with it if `D` and lower position are omitted.

This report does not promote `D`, `F1`, or `1` into a stable engineering
terminal identity.

### Circuit-path depiction

Starting at `observed-terminal-mark-a`, a visible path portion proceeds
downward without crossing a component, connector, relay, junction-block,
continuation, or page boundary. It directly reaches `observed-ground-a`.
At the same lower terminal occurrence, a second path portion branches down and
right and directly reaches `observed-ground-b`.

No junction dot is printed at the branch origin. The two path portions visibly
share the same endpoint at the circled `D` occurrence rather than crossing at
an intermediate point. No crossing, hidden internal relationship, line-style
change, production mark, label, switch state, continuation mark, or unresolved
structural interruption appears on either portion. There is no off-page
continuation within the inspected complete-page boundary.

The path is therefore visibly continuous from lower terminal occurrence
`1 (D)` to each of the two ground-symbol occurrences. This is a source-visible
structural observation, not an accepted electrical edge, conductor entity,
canonical topology, or graph fact.

### Ground-symbol occurrences

`observed-ground-a` and `observed-ground-b` both have the geometry identified
as an earth-point symbol by `PILOT-DEP-003`. Each is directly reached by a path
portion from `observed-terminal-mark-a`. Neither occurrence carries a visible
alphabetic ground-point name, qualifier, or other identifier on PDF page 40.

The inspected source guidance establishes the symbol category but does not
establish a broader named ground identity for either occurrence. A later
candidate needs only one precisely selected depicted ground reference, not a
canonical ground node. Because two occurrences are present, the hypothesis's
singular “the depicted ground reference” is under-specified.

### Engine qualifier

The exact title occurrence is `電源(1HZ,1PZ)`. It is centered above the complete
circuit and is the page-wide heading. The candidate-supporting battery and
ground region lies inside that page-wide circuit boundary. The narrow visible
engine qualifier is therefore `1HZ,1PZ` for this page; it does not establish
applicability to every PZJ70 or to the user's 1990 PZJ70.

### Production marks and legend

The upper-right page legend visibly reads `○: ～'95.1` and `□: '95.1～`.
The existing translation record gives the provisional literal readings
“through January 1995” and “January 1995 onward”; those readings remain
unreviewed linguistic interpretation rather than accepted translation.

Both `○` and `□` occur elsewhere on PDF page 40 near other circuit material.
Neither mark occurs on, within, immediately adjacent to, or by a leader from
`observed-label-a`, `observed-depiction-a`, either of its `1` occurrences,
`observed-path-a`, `observed-ground-a`, or `observed-ground-b`. No source-visible
mark-to-candidate-support association can therefore be recorded.

The reviewed dependencies define ground, terminal, connector, block, path, and
wire-color conventions. They do not define whether unmarked material on this
page is common to both legend ranges, belongs to one range, or has another
production scope. The target-local legend defines the two marks' ranges but
does not visibly state the meaning of absence of a mark. Inferring “common to
both” from layout would exceed the reviewed source-language evidence.

The publication-wide title material separately bounds listed `KZJ7#`, `PZJ7#`,
and `HZJ7#` series from May 1993 onward. That boundary cannot supply the missing
candidate-specific relationship to the page's January 1995 legend and cannot
broaden the candidate to the user's 1990 PZJ70.

## Guidance findings

### `PILOT-DEP-003`

- Location: PDF page 7 / printed page `1-4`, right-side power/ground region.
- Role for this verification: notation interpretation.
- Material convention: defines the earth-point symbol category and the
  presentation of ground-load information.
- Existing review status: machine-assisted source-convention review; no human
  Japanese-language verification or accepted translation.
- Downstream requirement: required to identify `observed-ground-a` and
  `observed-ground-b` narrowly as depicted ground references.

### `PILOT-DEP-004`

- Location: PDF page 8 / printed page `1-5`, full page.
- Role for this verification: notation and source-structure interpretation.
- Material convention: defines system-circuit page organization, connector and
  terminal-number presentation, internal-circuit presentation, wire-color
  notation, and related page fields.
- Existing review status: machine-assisted source-convention review; no human
  Japanese-language verification or accepted translation.
- Downstream requirement: required for reading lower occurrence `1 (D)` as a
  terminal-number occurrence and for preserving the visible path/endpoint
  structure. Its wire-color and operating-condition portions are not material
  to this candidate.

### `PILOT-DEP-005`

- Location: PDF page 9 / printed page `1-6`, full page.
- Role reviewed: J/B and R/B internals, block-side and harness-side connector
  shapes, terminal numbers, wire-to-wire shapes, and female/male footnotes.
- Existing review status: machine-assisted source-convention review; no human
  Japanese-language verification or accepted translation.
- Downstream requirement: not required for this candidate. The selected
  battery-to-ground support does not pass through a J/B, R/B, internal block
  circuit, or wire-to-wire connector. It was inspected because it was a
  required verification input, but citing it as candidate support would add an
  irrelevant interpretive dependency.

## Ambiguities

### `issue44-verification-ambiguity-1`: selected endpoint wording

- Description: both the upper `1 (C)` and lower `1 (D)` occur on
  `observed-depiction-a`, and the lower occurrence reaches two visible ground
  symbols.
- Exact effect: the terminal endpoint and ground-symbol endpoint named by the
  provisional hypothesis.
- Classification: soft for the source-visible transcription; hard only if a
  candidate repeats the under-specified endpoint wording.
- `AGENTS.md` test: Test C applies. Resolving the ambiguity changes which
  terminal occurrence and which visible ground endpoint the candidate maps to.
- Candidate effect: it does not block a deliberately narrowed candidate, but
  it requires explicit revision before candidate creation.
- Resolution: name lower terminal occurrence `1 (D)` and select either the
  directly-below ground-symbol occurrence or the right-hand branch occurrence
  by an independently reviewable location description.

### `issue44-verification-ambiguity-2`: production applicability

- Description: the candidate-supporting region carries neither `○` nor `□`,
  and no reviewed same-publication rule defines the candidate applicability of
  unmarked material.
- Exact effect: the production-scope property of the proposed engineering
  candidate and whether the observed structure supports pre-January-1995,
  January-1995-onward, both, or another scope.
- Classification: hard for candidate creation.
- `AGENTS.md` test: Test E applies. Resolving the ambiguity could select
  materially different production scopes. The uncertainty forces a choice
  between different candidate transcriptions even though the visible path can
  itself be copied faithfully.
- Candidate effect: blocks Phase 2 candidate creation; attaching a broad soft
  ambiguity would not satisfy Issue 44's exact production-scope gate.
- Resolution: locate and review a same-publication convention that explicitly
  defines the production applicability of unmarked circuit material, or obtain
  an approved planning revision that changes the gate while preserving the
  unresolved candidate scope. A convention from EWD168F or another publication
  cannot resolve this ambiguity.

## Applicability conclusion

The source visibly supports only the following without further interpretation:

- the complete circuit page is headed for `1HZ,1PZ`;
- the selected structural occurrences lie within that page-wide circuit;
- the publication's separately reviewed title material lists `KZJ7#`, `PZJ7#`,
  and `HZJ7#` series beginning May 1993; and
- the page legend defines visible `○` and `□` date strings, but neither mark is
  associated with this candidate-supporting region.

The evidence does not presently establish whether the proposed candidate is
pre-January-1995 only, January-1995-onward only, or common to both. It does not
support applicability to the user's 1990 PZJ70.

## Candidate disposition for the next phase

Remain blocked.

The evidence supports planning a narrower terminal and ground endpoint, but an
engineering-candidate record must not be created until the production scope of
unmarked material is established or Issue 44 is explicitly replanned. No
replacement candidate was selected.

## Recommended candidate wording

No candidate wording is recommended while the production-applicability hard
precondition remains unresolved.

If that precondition is later resolved, the structural portion should at least
identify the lower terminal occurrence `1 (D)` and one selected ground-symbol
occurrence, rather than using the current singular and under-specified endpoint
phrasing. That planning note is not a candidate proposal.

## Hidden-disqualifier check

Within the complete inspected page and candidate-supporting region:

- no off-page continuation, connector boundary, block boundary, switch-state
  dependency, internal battery path choice, path crossing, junction dot,
  alternative non-ground endpoint, footnote, or page-wide note interrupts the
  selected visible path;
- two ground endpoints, rather than one, are visibly reached from lower
  terminal occurrence `1 (D)`;
- no production-dependent branch or source-visible production mark is attached
  to the selected region;
- minor scan wear and bleed-through do not change the relevant transcription;
- the donor watermark is not factory content;
- the review-ready translation record does not contradict the visible labels,
  title, page mapping, or notation, but it does not prove topology or
  candidate-specific applicability; and
- the existing ambiguity ledger contains no ambiguity that resolves or
  supersedes the candidate-specific production question recorded here.

These are bounded absence observations, not universal claims about the
publication.

## Explicit omissions

This report does not represent or decide:

- the upper `1 (C)` path beyond noting it as a disambiguating occurrence;
- the `バッテリーNO.2` circuit beyond checking label-association ambiguity;
- alternator, fuse-block, relay-block, ignition-switch, combination-meter, fuse,
  or unrelated circuit content;
- wire-color identities outside what was needed to rule out a material path
  change;
- a stable source-object identity, source-local identity reconciliation,
  physical battery identity, named ground point, canonical ground node,
  electrical edge, graph topology, engineering candidate, eligibility result,
  acceptance, or rejection; or
- any applicability derived from EWD168F, another publication, or a specific
  vehicle observation.

## Private-evidence statement

No factory page image, crop, screenshot, OCR derivative, or other private
factory-content bytes were committed. Working full-page renders and the
battery-region crop remain under the verified gitignored `.evidence/` boundary.
