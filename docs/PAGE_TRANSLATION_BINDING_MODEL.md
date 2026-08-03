# Page-to-Translation Binding Model

## Purpose and status

This document defines a conceptual model for connecting linguistic work to the
shared, source-visible publication representation. It is the design
investigation for Issue #30. It defines relationships, ownership, cardinality,
granularity, coverage, review, and lifecycle behavior; it does not select JSON,
field names, identifier syntax, storage, or migration mechanics.

The model is grounded in the current Milestone 7 records for printed pages
`2-3`, `2-7`, and `3-2`. Those records remain valid and unchanged. The model is
provisional pending the publication-family evaluation in Issue #31 and the
graph-extraction contract in Issue #32.

## Governing principles

1. **Structure exists without translation.** A source-visible occurrence or
   region remains valid with no linguistic content, untranslated content, one
   proposal, competing proposals, a rejected proposal, or no need for
   translation.
2. **Bindings point to structure.** Linguistic artifacts reference stable
   structural occurrence or declared-region identity. Displayed text,
   translated English, unit IDs, printed page values, and source identifier
   values are not source-object identity.
3. **Binding does not transfer ownership.** Page decomposition owns structural
   occurrence identity and relationships. Linguistic interpretation owns
   transcription, literal translation, language ambiguity, and language review.
   Engineering normalization remains later and independently reviewed.
4. **English is derived.** English augments the controlling source-language
   occurrence; it never replaces that occurrence or the original publication.
5. **Exact source form is preserved.** A binding must not silently rewrite
   source text, punctuation, case, qualifiers, identifier values, or notation.
6. **Granularity and coverage are declared.** Reviewers can identify exactly
   which occurrences, parts, composites, sets, or regions a subject covers.
7. **No automatic fact promotion.** Binding does not establish component or
   connector identity, harness membership, topology, applicability,
   equivalence, or accepted graph knowledge.
8. **Review dimensions remain separate.** Structural target, binding
   correctness, source transcription, literal translation, engineering
   terminology, and graph extraction have distinct review gates.
9. **Use the narrowest practical reviewed binding.** Precision is preferred,
   but source-supported composites, explicit occurrence sets, and bounded
   regions are allowed when atomic binding would lose meaning or impair review.
10. **No binding silently retargets itself.** Material changes to target
    correspondence, target membership, or evidence context require explicit
    review and, where needed, supersession.

## Core terminology

### Binding

A **binding** is a reviewed relationship connecting a linguistic artifact or
translation unit to one or more source-visible occurrences or a declared
region. The binding owns the relationship, its declared scope, uncertainty,
and binding-review state. It owns neither endpoint.

### Structural binding target

A **structural binding target** is a stable source-visible occurrence,
source-supported composite occurrence, explicit set of occurrences, or
declared region in the publication representation. A target is referenced by
structural occurrence or region identity within its evidence context, never by
displayed content such as `H8`, `A`, or `2-3` as a supposedly unique key.

### Linguistic binding subject

A **linguistic binding subject** is the linguistic artifact related to source
structure. It may be an exact transcription, literal translation, grouped
translation unit, language ambiguity, omission or not-applicable disposition,
or a future accepted language representation. This list describes conceptual
roles; it does not require a separate stored binding for every subject type.

### Binding role

A **binding role** states why the subject relates to the target. Candidate
conceptual roles include `transcribes`, `literally translates`, `groups for
translation`, `preserves untranslated notation`, `records language ambiguity`,
`records omission`, `records not-applicable linguistic treatment`, and
`supplies reviewed linguistic interpretation`. The vocabulary remains
provisional. It must not include engineering relationships.

### Binding scope

**Binding scope** is the declared structural and linguistic boundary covered by
the relationship: for example, an exact text occurrence, a complete legend
entry, an enumerated set of repeated labels, a table row, a page-heading region,
or a bounded group of callouts. Scope identifies both inclusion and intentional
exclusion where a target contains nonlinguistic structure.

### Binding evidence

**Binding evidence** is the primary publication evidence and reviewed
structural reference that support the correspondence. The original publication
page remains the evidentiary anchor. Page decomposition is a derived reviewed
structural representation; the binding and translation are derived
interpretive artifacts.

### Binding coverage

**Binding coverage** records which represented linguistic occurrences or
declared regions have an explicit linguistic treatment. It is distinct from
whether the structure was completely decomposed and whether a translation or
normalization was completed.

## Ownership, authority, and direction

The conceptual direction is:

```text
linguistic artifact or translation unit
              │
              └── references ──► source-visible occurrence or region
```

This direction expresses dependency and authority, not a storage layout:

- linguistic interpretation depends on publication representation;
- publication representation does not depend on translation;
- revising or deleting a translation cannot delete the source object;
- one occurrence may support competing, revised, or differently scoped
  linguistic artifacts; and
- an index may provide inverse navigation from structure to translations
  without reversing semantic ownership.

The original publication controls what is visible. Publication representation
owns the reviewed structural account and stable occurrence identity. A binding
owns only its correspondence and review state. Linguistic interpretation owns
its proposed reading and wording. Engineering normalization and graph
extraction own later interpretations and claims. No endpoint gains the other's
authority through association.

## Binding subjects and targets

The same structural target may support transcription, translation, ambiguity,
and a not-applicable disposition without requiring those concepts to be
collapsed into one artifact. Conversely, one linguistic subject may address
several explicitly enumerated targets when grouping is justified.

Target kinds are conceptual:

| Target kind | Appropriate use | Required discipline |
| --- | --- | --- |
| Occurrence | One label, qualifier, note, key, terminal mark, or text occurrence | Preserve its independent identity and exact source form |
| Partial occurrence | A mixed occurrence or independently reviewable portion | Declare the covered portion; do not select offset syntax here |
| Composite occurrence | One source-supported legend entry, callout, table cell, or heading with qualifier | Identify which constituent text is linguistic and preserve internal ambiguity |
| Explicit occurrence set | Repeated wording or a reviewed translation group | Enumerate every member and state grouping rationale and order |
| Declared region | Bounded prose or a legacy grouped unit lacking finer reviewed decomposition | State boundary, covered content, omissions, and limitations |

A target may contain or visibly attach to graphical objects. That does not make
those objects linguistic targets unless they independently require a linguistic
treatment.

## Cardinality

### One-to-one

One subject references one occurrence, such as a page heading, component label,
note, legend key, or qualifier. This is the default when the occurrence carries
an independently reviewable reading.

### One-to-many

One subject may intentionally cover several occurrences: repeated identical
labels translated once, a grouped legend translation, or prose visibly split
across structural occurrences. Every occurrence remains individually
referenceable. The binding declares membership, coverage, grouping rationale,
and linguistic order. Repetition does not establish engineering identity.

### Many-to-one

Several subjects may reference one occurrence: exact transcription, provisional
literal translation, alternative reading, correction, terminology proposal, or
reviewed interpretation. Competing artifacts remain reviewable and cannot
overwrite one another without history.

### Many-to-many

Unrestricted many-to-many binding is not recommended. It obscures which
subject covers which occurrence and makes omission and revision review
ambiguous. Where pilot evidence appears many-to-many, use an explicit grouping
subject or occurrence-set target with declared membership and simpler bindings.
If future evidence requires many-to-many directly, Issue #31 must define its
boundary, membership, ordering, and review semantics before adoption.

## Granularity alternatives and recommendation

### One binding per text occurrence

This gives precise provenance, omission detection, ambiguity attachment, and
review. It can also fragment phrases and create poor ergonomics for tables,
legends, and text distributed across visual forms.

### Composite-object binding

Binding a source-supported legend entry, callout, table cell, note, or heading
with qualifier matches visible document forms and keeps related text together.
It risks hiding an independently ambiguous part and must not imply that
non-text constituents are translated.

### Region-level binding

A declared region is practical for bounded prose and compatible with current
grouped records. It is too coarse for dense diagrams when used alone: it weakens
field-level provenance, ambiguity attachment, and omission detection.

### Grouped occurrence binding

An explicitly enumerated occurrence set preserves individual structural
identity while supporting repeated strings and existing translation-review
ergonomics. Its grouping rationale and order require review, and membership
changes can stale only part of the group.

### Hybrid model

Adopt a hybrid model. Prefer occurrence-level targets where practical; use a
source-supported composite when it is the natural visible and linguistic unit;
use an explicit occurrence set for reviewed repetition or grouping; and retain
region binding for bounded prose or legacy grouped records. This is the
smallest model supported by all three pilots. It avoids a universal granularity
while making every departure from occurrence-level binding explicit.

## Source transcription alignment

```text
source-visible text occurrence
          │
          ├── binding ──► exact source transcription
          └── binding ──► literal translation
                                  │
                                  └── later engineering normalization
```

The page object owns the visible occurrence and location; it need not contain
accepted Japanese transcription. The linguistic artifact owns its proposed
reading. A binding associates the reading with the occurrence.

Transcription and literal translation normally reference the same structural
target, but their granularity may differ. Exact transcription can remain
occurrence-level while one literal translation uses an explicit occurrence set
to preserve a coherent phrase or repeated wording. That difference must be
declared and reviewed.

Partial-occurrence or span alignment may be needed when one visible occurrence
contains both an identifier and translatable prose, when punctuation changes
scope, or when only part is readable. The model permits a declared partial
target but does not choose offsets, coordinate syntax, or tokenization. A
qualifier may be a distinct target or part of a reviewed composite. The choice
must preserve its text and attachment.

If a character is unreadable or has several readings, preserve the visible
occurrence, bind the narrowed transcription status or alternative readings,
and attach ambiguity only to affected subjects. Do not guess one reading into
the page structure. Structural ambiguity blocks binding only when the target or
boundary cannot be identified faithfully.

## Text labels and the things they label

```text
text-label occurrence != depicted object
```

A binding to a label does not bind its wording to a connector, component,
harness, relay, or other depiction. A visible-attachment relationship may be
referenced as structural context, but it remains distinct from the linguistic
relationship and from engineering identity.

For example, source text occurrence `H8` may be visibly attached to a connector
depiction and receive a preserve-verbatim or translation-not-applicable
disposition. This does not create a canonical connector named `H8`.

## Grouped translation units and repeated wording

Grouping is a linguistic review choice, not structural identity. A grouped
subject must:

- enumerate every target occurrence or bind to a reviewed composite/region;
- state why the content is grouped;
- preserve target-local qualifiers, punctuation, case, and ordering;
- distinguish source-supported reading order from translator-selected order;
- expose omissions and unreadable members;
- avoid claiming identity among repeated occurrences; and
- narrow or become stale when membership changes materially.

Repeated identical text remains separate occurrences. One subject may translate
the repetitions once through an explicit occurrence set, but a reviewer must be
able to discover every location and determine whether one differs by case,
punctuation, qualifier, or context. Shared wording does not mean shared object,
shared applicability, or shared engineering entity.

## Qualifiers and structural associations

Qualifiers include `1HZ`, `1PZ`, LH/RH, production-date ranges, market or
equipment restrictions, parenthetical text, and production-legend marks. A
qualifier may be its own occurrence, a constituent of a composite, or visibly
attached to a heading, label, entry, or callout.

A binding must preserve both the qualifier and the reviewed structural
association that scopes it. Grouping cannot silently broaden a qualifier from
one entry to a legend, from one label to a group, or from source wording to
vehicle applicability. Translating a production qualifier records linguistic
meaning; applicability acceptance remains governed by
[Applicability](APPLICABILITY.md).

If qualifier attachment is uncertain, attach that uncertainty only to bindings
whose text, membership, boundary, or scope could change. A readable qualifier
can be transcribed while its broader applicability remains unresolved.

## Source-local identifiers and non-translatable notation

Connector identifiers, terminal labels, cavity numbers, page-grid coordinates,
legend keys, wire-color abbreviations, printed page identifiers, production
marks, block designations, and cross-references retain the roles and scopes in
the [Publication Identifier Taxonomy](PUBLICATION_IDENTIFIER_TAXONOMY.md).

Their linguistic treatment may be preserve verbatim, transcription only,
translation not applicable, explanatory annotation, or translated surrounding
wording with the identifier retained. A not-applicable disposition is still
reviewable linguistic coverage; it does not erase the occurrence. Displayed
values never become binding keys.

Mixed content must remain separable. For example, a legend key can be preserved
while its adjacent Japanese harness name is translated. A wire-color label may
be literally translated under a same-publication color convention, while the
nearby path remains a graphical occurrence with no translation binding.

## Reading and traversal order

Keep these orders distinct:

- structural traversal order;
- visually supported reading order;
- source-language reading order;
- table row and column order;
- translator-selected grouping order;
- circuit flow; and
- graph topology.

A binding or grouping subject may record reviewed linguistic order where
translation requires it. This does not redefine page hierarchy, assert a global
order, infer electrical flow, or create topology. Pages without one valid
reading order remain addressable through independent targets and local orders.

## Provenance

Each binding must preserve or reference enough context to identify:

- publication identity and verified artifact fingerprint;
- PDF page and printed page where present;
- declared decomposition boundary;
- structural occurrence, occurrence-set, composite, or region identity;
- linguistic subject and binding role;
- binding scope, membership, and relevant order;
- binding-review status and uncertainty;
- material same-publication interpretive dependencies; and
- revision or supersession state where applicable.

The source page is primary evidence. Decomposition is a reviewed structural
representation. Binding is a derived relationship. Translation is a derived
linguistic representation. None replaces the source page. Interpretive
dependencies explain how required notation is read; attach only those material
to the subject-target correspondence or source reading.

## Completeness and omission handling

Four independent coverage questions precede graph extraction:

| Coverage dimension | Question | Owner |
| --- | --- | --- |
| Structural coverage | Which visible objects and relationships are represented inside the decomposition boundary? | Publication representation |
| Binding coverage | Which represented linguistic occurrences or regions have an explicit treatment? | Binding/review workflow |
| Translation coverage | Which bound content has transcription, literal translation, ambiguity, omission, unreadable status, or not-applicable treatment? | Linguistic interpretation |
| Engineering-normalization coverage | Which translated concepts have reviewed normalized terminology? | Engineering normalization |

Therefore:

```text
complete decomposition
!= complete binding
!= complete translation
!= complete normalization
!= complete graph extraction
```

Excluded, intentionally untranslated, unreadable, omitted, and not-applicable
content remains visible in coverage accounting. A grouped subject cannot claim
complete page coverage merely because a broad region was translated. It must
declare target occurrences and account for linguistic occurrences inside its
boundary that are not members.

Binding review should support both directions: structure-to-binding detects
untreated linguistic occurrences, while binding-to-structure detects missing,
incorrect, or overbroad targets. Fidelity takes priority over superficial
completeness.

## Uncertainty and failure states

Record uncertainty at the narrowest level that could materially change the
relationship. Distinguish uncertainty in target occurrence, target boundary,
group membership, binding role, source reading, linguistic order, literal
meaning, qualifier scope, omission status, and engineering normalization.

Examples include a subject that may correspond to either of two labels; two
readings of one label; a qualifier that may attach to one entry or a group; a
grouped subject that omits a footnote; repeated text that differs by case; or a
target changed after structural review.

A higher-level translation cannot suppress structural ambiguity. Structural
ambiguity blocks binding only where it prevents identifying the target,
boundary, or material membership. A faithful binding can remain valid while
literal meaning or later engineering normalization is unresolved. Engineering
uncertainty alone does not invalidate accurate transcription and binding.

## Review gates

Do not collapse the following into one `approved` state or a numeric confidence
score:

1. **Structural-target review:** Does the occurrence or region exist? Is its
   structural identity stable and its evidence location correct?
2. **Binding-correctness review:** Does the subject address the claimed target?
   Are membership, role, scope, order, qualifiers, and punctuation correct?
3. **Source-transcription review:** Were source text, case, punctuation,
   identifiers, and qualifiers read and preserved correctly?
4. **Literal-translation review:** Is the target-language wording faithful?
5. **Engineering-normalization review:** Is terminology supported and free of
   invented engineering meaning?
6. **Graph-extraction review:** Does a separate candidate faithfully derive
   from its evidence without automatic promotion?

A contributor without Japanese competence may review target existence,
structural correspondence, binding membership, and engineering concerns within
their qualifications. They cannot claim qualified human language verification.

## Revision, staleness, split, and merge behavior

| Change | Conceptual effect |
| --- | --- |
| Source transcription changes | Re-review transcription and dependent translation; structural identity normally remains |
| Literal translation or terminology changes | Update linguistic review history; structural identity and binding target remain |
| Structural reclassification | Binding remains valid if occurrence identity and correspondence remain |
| Geometry correction | Re-review only if target correspondence or boundary changes materially |
| Occurrence split | Review every binding; explicitly supersede or replace coverage with bindings to resulting occurrences |
| Occurrence merge | Review every binding; preserve former identities and explicit supersession rather than silently coalescing |
| Region-boundary change | Re-evaluate inclusion, omission, and coverage claims |
| Page mapping or evidence artifact changes | Revalidate provenance and target correspondence |
| Group member added or removed | Invalidate or narrow the former membership and coverage claim; unaffected occurrence bindings may remain |

No binding silently retargets itself. Translation wording does not alter
structural identity. Structural reclassification or geometry correction does
not create needless staleness when the same occurrence remains identifiable.
Split, merge, material boundary change, artifact replacement, and page
remapping require explicit review. Stale and superseded relationships remain
recoverable through Git and future lifecycle records; migration mechanics are
outside this design.

## Pilot-page analysis

These examples demonstrate conceptual relationships only. They do not create
page decompositions, structural IDs, bindings, accepted translations, or graph
facts.

### Printed page `2-3`

The current `tgt005-heading` unit can remain one linguistic review subject. A
future heading translation could reference the heading text occurrence, while
`1HZ,1PZ` could receive a distinct qualifier disposition or remain inside a
reviewed heading composite. Either choice must preserve the qualifier and its
attachment.

The grouped `tgt005-harness-legend` unit can remain one review unit while a
future explicit occurrence set enumerates each legend-entry text occurrence.
Keys `A`-`I`, `f`, `g`, `i`, and `ℓ` remain separately addressable identifier
occurrences; each Japanese harness label remains separately addressable text.
The color swatches are structural graphical objects and are not translated.
The legend key `A` is not grid row `A`, even though the displayed values match.

The `layout-identifiers` subject currently accounts for grid markers, connector
identifiers, cavity numbers, production qualifiers, shapes, and colors as a
grouped not-applicable treatment. Future binding can narrow this into explicit
preserve-verbatim or not-applicable dispositions for identifier occurrences.
Connector identifiers remain source-local and do not create connector identity.
Production qualifiers preserve their visible association without accepting
applicability.

The printed page, publication date/part mark, and factory content remain
distinct from the non-factory donor watermark. A capture mark can receive an
explicit exclusion or non-factory disposition but must not be grouped into a
factory translation. Current region names such as `harness-legend` remain
pilot-local references, not proof that canonical regions already exist.

Conceptually:

```text
heading translation              -> heading text occurrence
engine-qualifier disposition      -> qualifier occurrence
grouped legend translation        -> enumerated legend-entry text occurrences
identifier-preservation treatment -> legend-key occurrence
not-applicable treatment          -> grid-marker occurrence
```

### Printed page `2-7`

The heading and left-side wording may use a source-supported composite or
separate heading and qualifier occurrences. The harness legend contains
case-sensitive keys including `H`, `J`, `K`, `k`, `p`, and `q`; every
occurrence requires stable structural identity independent of its value.
Translated harness wording cannot replace a key.

`(LH)` and `(RH)` can bind separately or as constituents of reviewed legend
entry composites. Their attachment and scope must survive grouping. Production
qualifiers likewise remain associated with the source-visible items they
qualify and do not accept applicability.

Connector labels and depictions remain distinct. A translated label does not
establish connector or harness identity. Repeated or similar callouts remain
separate occurrences even when one grouped subject improves review ergonomics.
One occurrence's correction must not silently alter another. Current grouped
units can remain unchanged while future bindings enumerate their targets.

### Printed page `3-2`

The page heading and `1HZ,1PZ` qualifiers follow the same occurrence/composite
choice as page `2-3`. Component-bearing labels—relay and fuse labels, block
labels, combination-meter wording, and the charge-indicator label—may receive
literal translations. Their association with depictions is structural context,
not component identity or topology.

Terminal marks, connector identifiers, cavity labels, and block designations
generally receive preserve-verbatim, transcription-only, or not-applicable
treatment. Wire-color labels can receive literal translations under the
same-publication two-color convention, but nearby circuit paths do not thereby
receive bindings. Circuit symbols, conductor paths, joins, relay contacts, and
block boundaries have no translation binding merely because neighboring text
does.

The production legend may use a grouped subject for `○` and `□` explanations
plus explicit structural references to each distant mark. This records how the
legend is read without resolving applicability or electrical meaning. A group
must expose any missing distant mark and preserve the association between mark
and legend entry. Translation coverage does not imply circuit-topology
coverage. Toyota-normalized terminology remains separate from literal wording.

## Compatibility with existing Milestone 7 records

The three records remain valid, review-ready, unchanged, and canonical only for
their current translation-artifact role. They are not page decompositions,
accepted translations, graph extractions, or accepted graph facts.

A future implementation can retain each current content unit as a linguistic
subject and associate structural references externally or through a later
schema revision. Grouped units need not be split merely to gain precise
bindings; their future binding can enumerate occurrences while preserving the
group as a review unit. Current review states carry forward and do not imply
binding approval.

Current `source_region_id` values and names such as `page-heading`,
`harness-legend`, and `diagram-notation` are pilot-local source references.
They do not prove that a future canonical region or structural occurrence
already exists, and they must not be reused as durable structural identity
without later reconciliation. No migration or record change is required in
this investigation.

## Alternatives considered

- **Translation record owns page structure — rejected.** Translation is an
  optional downstream capability and cannot own language-independent source
  representation.
- **Displayed text or source identifier value as binding key — rejected.**
  Values repeat, collide across roles, and change under correction.
- **Page-level binding only — rejected.** It cannot support precise provenance,
  qualifier scope, omission detection, or independent review.
- **Atomic occurrence binding only — not adopted universally.** It is precise
  but fragments source-supported phrases, legends, tables, and distributed
  text.
- **Region binding only — rejected as the general model.** It is compatible
  with current records but too coarse for dense diagrams and tables.
- **Translation embedded in every page object — rejected.** It makes structure
  language-dependent and complicates multiple languages, proposals, and review
  histories.
- **External association model — adopted.** Separately reviewable bindings
  connect independently owned linguistic and structural artifacts.
- **Hybrid target model — adopted provisionally.** Occurrence, composite,
  explicit occurrence-set, and bounded-region targets address demonstrated
  pilot needs without unrestricted many-to-many relationships.

## Sibling-issue boundaries

- Issue #28 owns semantic layers, authority, and artifact ownership.
- Issue #34 owns candidate source-visible object classes.
- Issue #27 owns page decomposition, structural relationships, and stable
  structural occurrence identity.
- Issue #29 owns identifier roles, scopes, preservation, and identity
  constraints.
- Issue #30 owns translation-binding concepts, direction, cardinality,
  granularity, coverage, lifecycle, and review.
- Issue #31 will test the combined model across publication families.
- Issue #32 will define downstream graph-extraction contracts.

This design does not redesign Issues #27-#29 or #34, begin Issue #31 or #32, or
prescribe their conclusions.

## Unresolved questions

- Must every translatable text occurrence receive an explicit binding?
- Can any region-level binding satisfy complete translation review?
- When should repeated text share one linguistic subject?
- Does transcription require finer granularity than literal translation?
- Are substring or span bindings necessary, and how should they be located?
- How should punctuation-only occurrences be treated?
- How should visible text embedded in graphical symbols bind?
- How should qualifiers shared across several entries bind?
- How should grouped bindings survive occurrence splits?
- Can current `source_region_id` values map cleanly to future structural
  identities?
- Which concepts survive Issue #31's publication-family evaluation?
- Which final decisions require an ADR after Issues #31 and #32?
- What implementation and migration milestone should follow Epic #26?

## Explicit non-goals

This investigation does not define JSON, fields, schemas, binding syntax,
structural IDs, storage, validators, migrations, or implementation code; modify
translation records or canonical JSON; create page-decomposition fixtures;
perform OCR or translate pages; accept translations or normalize Toyota
terminology; create engineering entities or graph facts; resolve connector
equivalence; establish or broaden applicability; generate publishing output;
add dependencies or infrastructure; or authorize production-scale translation.

## Design recommendation and ADR decision

Use separately reviewable translation bindings that point from linguistic
artifacts to stable source-visible occurrences or declared regions. Prefer
occurrence-level targets where practical; allow source-supported composites and
explicit occurrence sets where grouping remains enumerated and reviewable; and
retain region-level binding for bounded prose and legacy grouped units. Every
binding preserves structural identity, declared coverage, qualifiers,
uncertainty, provenance, and independent review without transferring ownership
or creating engineering facts.

This design refines the dependency already established by ADR 0006 and the
completed publication-representation investigations; it does not change a
project invariant. Keep it provisional. Defer a focused ADR until Issues #31
and #32 test publication-family coverage and the downstream extraction
contract.
