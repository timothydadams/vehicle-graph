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
  Poppler `pdftotext`, ImageMagick contact-sheet and crop preparation, direct
  high-resolution visual inspection, repository-wide text search, and
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

## Publication-wide production-convention search

### Search boundary and methods

The search used the reverified artifact identified above and included all 90
PDF pages. No page was excluded. Working text, renders, thumbnails, contact
sheets, and crops remained under the verified gitignored `.evidence/` boundary.

The following complementary methods were used:

1. `pdftotext -layout` attempted a complete text-layer extraction. The result
   contained 91 lines / 3,961 bytes and only the repeated donor watermark, so
   the artifact has no usable factory-text layer for this search.
2. `rg` searched that extraction and committed repository material for `○`,
   `□`, `○:`, `□:`, `～'95.1`, `'95.1～`, `95.1`, `○印`, `□印`, `無印`,
   `印のない`, `記号`, `生産`, `適用`, `変更`, and the English navigation
   terms `production` and `unmarked`. Repository hits were used only for
   navigation and were checked against the verified PDF where material.
3. `pdftoppm` rendered all pages at navigation resolution. Six ordered contact
   sheets covering PDF pages 1–90 were visually reviewed for explanatory
   pages, repeated legends, notes, headers, footers, marked diagrams, and
   direct production qualifiers.
4. Chapter 1 and the opening material at PDF pages 2–10 were rendered and
   reviewed at higher resolution. This included publication scope and revision
   material, contents, all “how to read” pages, and the active diagram
   dependencies.
5. The system-circuit chapter at PDF pages 39–69 was reviewed page by page.
   PDF pages 40–69 were rerendered at higher resolution, and their header and
   legend regions were compared. Potential production/date hits and unrelated
   uses of similar glyphs were then inspected directly.
6. The direct parenthetical date qualifiers on representative layout pages 15
   / `2-3` and 19 / `2-7` were rerendered at high resolution and compared with
   their committed machine transcriptions.

The visual pass covered page surfaces, margins, headers, footers, legends,
footnotes, and the Chapter 1 explanatory material. It can establish the
completed search boundary and the inspected results, but it is not a
mathematical proof that no faint or unrecognized wording exists. Scan wear,
the absent factory-text layer, and the absence of installed Japanese OCR meant
that visual inspection, rather than OCR term matching, controlled the result.

### Relevant and potentially relevant occurrences

| PDF page(s) | Printed page(s) | Region and minimal visible content | Evaluation for this candidate |
| --- | --- | --- | --- |
| 2 | none visible | Opening applicability includes `1993-5～` with the listed model families. | Defines the publication-wide production start already recorded in the repository. It does not define `○`, `□`, their attachment, or unmarked circuit material. |
| 15, 19 | `2-3`, `2-7` | Individual layout callouts carry direct parenthetical date strings such as `(95.1～)` and `(～95.1)`. | Demonstrates occurrence-local date qualifiers without a circle/square legend. It supplies no default or unmarked-material rule for system circuits. |
| 40, 41, 44–47, 50 | `3-2`, `3-3`, `3-6`–`3-9`, `3-12` | Page legends pair `○` with `～'95.1` and `□` with `'95.1～`. | Directly defines those two marks' date strings on each page. None of the legends states the meaning or scope of unmarked material. PDF page 40 remains the primary occurrence for the proposed candidate. |
| 42 | `3-4` | A page-specific legend combines square variants with body/date scope and circle/triangle marks with engine scope. | Confirms that glyph meaning can be page-specific and composite. It does not define unmarked content or govern page `3-2`. |
| 49 | `3-11` | Two different square forms are paired with the two January 1995 ranges. | A page-specific production legend, but neither a general rule nor an explanation of unmarked content. It does not govern page `3-2`. |
| 51 | `3-13` | Open and filled square forms are paired with body/date scope. | Page-specific mark definitions only; no unmarked-material rule and no material relationship to the selected page-40 region. |
| 55 | `3-17` | A single `○` entry is paired with `～'95.1`. | Defines only the visible mark on that page. It does not say what the absence of that mark means. |
| 58, 59, 66, 67 | `3-20`, `3-21`, `3-28`, `3-29` | Composite legends combine circles, squares, divided or filled forms, and other glyphs with engine, body, equipment, and date scopes. | Inconclusive for the candidate. They show that each page's legend must be read locally, but none visibly supplies a general default or unmarked-material convention for page `3-2`. |
| 63, 68 | `3-25`, `3-30` | Circle/triangle entries identify engine categories without defining the January 1995 pair. | False positives for a production-date-rule search. Same glyph family, unrelated local role. |

Circled connector-reference letters, ground-point symbols, circular diagram
geometry, table marks, and body/engine glyphs elsewhere in the publication were
also false positives unless their local legend explicitly gave them a
production role. No such unrelated occurrence was promoted into candidate
support.

### Search result and dependency assessment

Search completed across all 90 pages using text-layer extraction, exact and
likely-term searches, committed-record navigation, complete visual contact
sheets, page-by-page system-circuit review, and high-resolution inspection of
every potentially explanatory location listed above.

No inspected occurrence explicitly defined the applicability of unmarked
circuit material, stated that absence of `○` or `□` means common to both date
ranges, established a default scope, or defined how a nearby mark expands to an
otherwise unmarked component, path, branch, block, or page region. The repeated
legends define visible glyphs and, on several pages, visibly demonstrate
page-local composite meanings; repetition alone cannot supply the missing
rule.

The search discovered no new material interpretive dependency for this
candidate. PDF pages 41, 42, 44–47, 49–51, 55, 58, 59, 66, and 67 are
comparison occurrences only. They neither define unmarked content nor govern
page `3-2`, so attaching them downstream would obscure provenance. The frozen
Milestone 7 dependency inventory therefore remains unchanged.

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
both” from layout would exceed the reviewed source-language evidence. The
publication-wide search documented above found repeated page-local legends but
no explicit same-publication rule that closes this gap.

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
- Classification: hard gate for engineering-candidate creation under Issue
  #44's exact-applicability requirement; not a hard blocker for transcription
  of the visible source structure.
- `AGENTS.md` test: Test E applies. Resolving the ambiguity could select
  materially different candidate production scopes. The label, depiction,
  lower `1 (D)`, two path branches, two ground-symbol occurrences, and visible
  absence of a nearby production mark can all be transcribed faithfully and do
  not change with this ambiguity.
- Candidate effect: blocks Phase 2 candidate creation; attaching a broad soft
  ambiguity would not satisfy Issue 44's exact production-scope gate.
- Search result: the complete bounded publication search found visible absence
  of a mark at the selected region and repeated definitions of visible marks,
  but no explicit rule defining the meaning of that absence. Absence of a mark,
  failure to find a rule for absence, and a prohibited inference that absence
  means “both” remain distinct.
- Resolution: the legitimate next options are explicit replanning of Issue #44
  while preserving the unresolved scope, or later user-approved planning of a
  different candidate. If qualified source-language review identifies wording
  overlooked in the completed visual boundary, that exact location must be
  reviewed before use. No candidate may be created under the current gate, and
  EWD168F or another publication cannot supply the missing convention.

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
support applicability to the user's 1990 PZJ70. This conclusion remains after
the complete bounded 90-page search; it does not convert failure to find an
explicit unmarked-material rule into evidence for any one scope.

## Candidate disposition for the next phase

Remain blocked.

The evidence supports planning a narrower terminal and ground endpoint, but an
engineering-candidate record must not be created until the production scope of
unmarked material is established or Issue 44 is explicitly replanned. The
publication-wide search did not establish that scope. No replacement candidate
was selected.

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
battery-region crop, extracted watermark-only text, all-page thumbnails,
contact sheets, and production-legend crops remain under the verified
gitignored `.evidence/` boundary.
