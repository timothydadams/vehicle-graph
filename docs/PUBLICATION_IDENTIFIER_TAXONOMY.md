# Publication Identifier Taxonomy

## Purpose and scope

This document defines identifier concepts across factory evidence, publication
representation, linguistic interpretation, engineering normalization, graph
extraction, and accepted graph knowledge. It assigns meaning, ownership, scope,
preservation, stability, collision handling, and review responsibility without
defining JSON fields, syntax, or a schema.

The design is grounded in Milestone 7 printed pages `2-3`, `2-7`, and `3-2`.
It prevents values such as `A`, `H8`, `A-9`, `30`, and `2-3` from being
mistaken for structural occurrence identity, engineering entity identity,
graph identity, equivalence, applicability, or canonical repository identity.

> An identifier is evidence of a visible or publication-defined designation
> within its documented scope. It does not establish the engineering identity
> of the thing designated.

## Governing principles

- **Spelling is not identity.** Equal values do not establish equal
  occurrences, roles, targets, entities, or graph nodes.
- **Occurrence and value are distinct.** Each locatable appearance is separate
  from the value it displays.
- **Scope controls meaning.** Identical values may coexist in different
  objects, callouts, legends, grids, pages, sections, artifacts, or
  publications.
- **Source form is evidence.** Preserve case, punctuation, spacing, prefixes,
  suffixes, separators, and material typography. Case is significant unless
  same-publication evidence proves otherwise.
- **Reference and target are distinct.** A reference does not prove its target;
  a resolved publication reference does not establish engineering identity.
- **Repository identity is disclosed.** Structural occurrence IDs are
  repository-assigned review aids, never factory identifiers.
- **Identity is promoted only by review.** Candidate engineering and accepted
  graph identities belong downstream and require their own evidence and gates.
- **Translation preserves identifiers.** Translation must not rewrite source
  values. Normalization may classify a value but must retain its exact form.
- **Ambiguity remains local.** Unknown readings, classes, scopes, attachments,
  or targets remain explicit at the narrowest place they can materially change.

## Core terminology

### Identifier occurrence

An **identifier occurrence** is one locatable source-visible occurrence that
contains or presents an identifier. The `H8` beside one connector depiction is
one occurrence; another `H8` elsewhere is another occurrence.

It owns visible presence, exact source form, evidence location, and reviewed
visual attachment or structural context. It does not own canonical connector
identity, graph identity, applicability, or cross-publication equivalence.

### Identifier value

An **identifier value** is the character sequence or symbolic value presented
by an occurrence, such as `H8`, `A`, `a`, `A-9`, `2-3`, `30`, or
`R/B NO.1`. A value may recur and serve different roles. A transcription
correction changes the recorded reading of an occurrence; it does not silently
substitute a normalized value.

### Identifier class

An **identifier class** is the publication role under which a value is used,
such as printed page identifier, grid-row marker, legend key, connector
reference, terminal identifier, or block designation. Classification may need
notation guidance from the same publication. It does not establish engineering
identity.

Not all alphanumeric text is an identifier. A label names or describes visible
content; terminology expresses a linguistic or engineering concept; a
measurement combines a value with measured meaning; descriptive prose states
content. Text is an identifier when the publication visibly or through its own
guidance uses it to designate, locate, key, number, or refer. One text object
may carry both descriptive wording and an identifier.

### Identifier scope

**Identifier scope** is the narrowest evidenced boundary within which a class
and value have reviewable meaning. Pilot-supported conceptual scopes are:

- object-local or callout-local;
- legend-local;
- page-grid-local;
- page-local or declared-boundary-local;
- section-local where publication guidance establishes it;
- publication-local only where evidence establishes publication-wide use;
- artifact-local for exact captured evidence; and
- engineering-model-local or repository-local only downstream.

Region-local and publication-family-local scope remain possible investigation
outcomes, not defaults. Never infer publication uniqueness from the pilot.

**Source-local** means a designation is controlled by its identified
publication, artifact, source location, and applicable publication conventions
unless evidence expands that scope. Within one publication it may be unique
only within an index, diagram family, page, legend, callout, harness, component,
or variant.

### Identifier reference and target

An **identifier reference** is an occurrence or structural object that points
to another occurrence, publication-defined designation, or unresolved target.
It remains distinct from its displayed value, target occurrence, proposed
engineering entity, and accepted graph node.

An **identifier target** is the occurrence, designation, or later engineering
entity proposed as the target. Resolution can be directly visible,
same-publication-guidance-resolved, provisional, ambiguous, unresolved,
conflicting, or rejected. Visible attachment is structural evidence. Guidance
may establish how a reference is read. Neither proves physical identity with
another same-valued depiction. Translation may assist review but cannot resolve
identity by itself.

### Structural occurrence identity

A **structural occurrence identity** is a stable repository identity for one
source-visible occurrence or decomposition object. It must be scoped to the
verified artifact and page or boundary; remain independent of translated and
normalized wording, identifier value, identifier class, engineering entity
identity, and graph identity; distinguish same-valued occurrences; and survive
ordinary review corrections while the underlying occurrence remains the same.

Publication identity, artifact fingerprint, PDF page, printed page, boundary,
and a locally assigned occurrence component are conceptual inputs. This
document selects no syntax, namespace, mandatory components, or schema.
Printed page labels, identifier values, translated wording, and normalized
wording must not be the sole durable identity basis. Identifier class must not
determine durable identity.

Identifier class may support description, indexing, validation, review,
collision analysis, a human-readable alias, or diagnostic output, but it must
not determine the durable structural identity of an occurrence that is expected
to survive class correction. Two occurrences require distinct structural IDs
whether they display the same value or have different classes. Correcting a
grid marker that was classified as a legend key preserves its structural ID
when the visible occurrence remains the same; the class correction remains
versioned and reviewable.

### Engineering and graph identity

A **candidate engineering entity identity** belongs to graph extraction and
represents a proposed component, connector, harness, terminal, or other
engineering entity. Page decomposition and identifier classification do not
create it.

An **accepted graph identity** is assigned only through reviewed extraction and
canonical acceptance. It must not be copied directly from a source value merely
because that value appears stable. A source value may become a graph property
or alias only through an explicit, evidenced extraction claim.

## Identifier categories

These are concepts, not fields or a closed vocabulary.

| Category | Primary semantic owner | Meaning and default scope | Must remain distinct from |
| --- | --- | --- | --- |
| Publication identifier | Source-visible structure / publication representation | Factory-visible designation for a publication or edition | Repository publication key, fingerprint, abstract-work identity |
| Publication part or document number | Source-visible structure / publication representation | Factory-visible number such as the value following `品番` | Component part identity unless explicitly assigned that role |
| Artifact fingerprint | Factory evidence inventory | Repository-recorded digest of exact evidence bytes | Factory-visible identifier or abstract publication identity |
| PDF page identity | Factory evidence inventory | Page position in one exact artifact | Printed page and page-content identity |
| Printed page identifier | Source-visible structure / publication representation | Factory-visible label such as `2-3` | Globally unique page or PDF-page identity |
| Section or chapter reference | Source-visible structure / publication representation | Publication navigation designation | Engineering system identity |
| Grid row marker | Source-visible structure / publication representation | `A` within one page grid | Legend key `A` or repository coordinate |
| Grid column marker | Source-visible structure / publication representation | `1` within one page grid | Terminal or cavity `1` |
| Combined grid coordinate | Source-visible structure / publication representation | Publication-defined combination such as `A-9` | Occurrence identity or global location |
| Legend key | Source-visible structure / publication representation | Key interpreted through one legend | Grid coordinate, harness entity, graph ID |
| Production-legend key | Source-visible structure / publication representation | Mark such as `○` or `□` referring to a visible convention | Resolved applicability by itself |
| Connector identifier or reference | Source-visible structure / publication representation | Source-visible connector designation | Physical connector identity |
| Inter-harness connector identifier | Source-visible structure / publication representation | Publication-defined inter-harness designation | Cross-publication equivalence |
| Component reference | Source-visible structure / publication representation | Designation associated with a component presentation | Canonical component identity |
| Harness reference | Source-visible structure / publication representation | Designation associated with a harness presentation | Physical harness identity or applicability |
| Block designation | Source-visible structure / publication representation | `R/B NO.1` or `F/B NO.1` | Accepted block entity identity |
| Terminal identifier | Source-visible structure / publication representation | Mark associated with a depicted terminal/contact context | Occurrence ID or accepted terminal identity |
| Connector-cavity identifier | Source-visible structure / publication representation | Mark for a depicted connector position | Terminal identity, occupancy, endpoint identity |
| Fuse or relay designation | Source-visible structure / publication representation | Source-visible rating/name/number | Accepted fuse or relay identity |
| Wire-color label | Source-visible structure / publication representation | Source notation such as `青-白` | Wire identity, conductor identity, graph edge |
| Continuation reference | Source-visible structure / publication representation | Marker pointing beyond local extent | Resolved continuity or topology |
| Cross-page reference | Source-visible structure / publication representation | Visible page, grid, figure, or table reference | Cross-page engineering identity |
| Callout-local identifier | Source-visible structure / publication representation | Designation meaningful within one callout | Page- or publication-unique identity |
| Structural occurrence identity | Page decomposition | Repository identity for one visible occurrence | Source identifier, entity, graph identity |
| Candidate engineering entity identity | Graph extraction | Provisional downstream identity | Source occurrence and accepted identity |
| Accepted graph identity | Accepted graph knowledge | Governed canonical repository identity | Factory designation or candidate identity |

Issue #31 must test which categories generalize to other publication families.

Semantic ownership identifies the layer responsible for the represented
concept; it does not replace evidentiary authority. The factory publication is
evidence for a printed value. Source-visible structure owns the reviewed
occurrence and proposed source-role classification. Page decomposition owns the
repository-assigned structural occurrence identity. Graph extraction owns a
candidate engineering identity, and accepted graph knowledge owns a governed
graph identity after acceptance. These are conceptual responsibilities, not
file, object, field, or storage ownership.

## Semantic-layer ownership audit

| Concept | Example | Owner | Scope | Authority and stability | May reference | Must not imply |
| --- | --- | --- | --- | --- | --- | --- |
| Printed publication identifier | `6742601` after `品番` | Source-visible structure / publication representation | Publication/artifact location | Factory evidence is authoritative for the visible value; source form is preserved and corrections are reviewed | Publication context | Repository or component identity |
| Artifact fingerprint | `sha256:…` | Factory-evidence inventory | Exact bytes | Stable only for those bytes | Artifact and pages | Abstract-publication identity |
| Page-grid coordinate | row `A`, column `1` | Source-visible structure | One page grid | Reviewed structural interpretation; marks preserved | Grid location | Legend, terminal, global coordinate |
| Legend key | `A`, `k`, `q` | Source-visible structure | One legend/convention | Exact form preserved | Entry and matching page marks | Harness identity or applicability |
| Visible connector label | `H8` | Source-visible structure | Supported source-local scope | Exact form preserved | Attached depiction/designation | Physical or cross-publication identity |
| Structural occurrence ID | repository assigned | Page decomposition | Artifact + boundary + occurrence | Stable through ordinary corrections; superseded for identity change | Evidence occurrence and relations | Factory or engineering identity |
| Translation binding reference | future occurrence reference | Linguistic interpretation, constrained by #30 | Reviewed occurrence/region | Should survive wording change | One or more occurrences | Unique-by-value binding |
| Candidate engineering ID | proposed connector | Graph extraction | Candidate model/applicability | Reviewable and changeable | Evidence and occurrences | Acceptance |
| Accepted graph ID | governed connector node | Accepted graph | Repository/applicability | Governed, supersession-preserving | Reviewed candidate/provenance | Factory designation or universal scope |

## Artifact fingerprint distinction

A SHA-256 fingerprint identifies exact artifact bytes. It is repository
recorded, not factory printed, and does not identify the abstract publication
by itself. A rescan of the same physical book may differ; different artifacts
or editions may display the same publication identifier. Page locations and
structural identities retain controlling artifact context. No fingerprinting
implementation is changed here.

## Stability, correction, and supersession

Preserve an identifier's exact source form. Transcription corrections retain
review history. Unreadable characters remain explicit rather than conveniently
normalized.

Keep structural occurrence identity stable when translation or normalization
changes, classification is corrected or refined, reviewed geometry is adjusted,
or ambiguity status changes without changing the occurrence. Identifier class
may change as a versioned review correction without changing the structural ID.
Explicit supersession may be required when an occurrence is split or merged,
page mapping or artifact changes, or the occurrence was identified incorrectly.
Migration mechanics remain deferred.

Candidate engineering identity may change during review without rewriting
source occurrences. Accepted graph identity evolves only through governance,
with provenance and supersession history preserved.

## Collisions and ambiguity

Collision classes include the same value across object classes, case, pages,
sections, publications, artifacts, or visible occurrences; one occurrence with
several readings; several references with one target; and one reference with
several targets.

> Preserve both occurrences and their scopes. Do not merge merely to eliminate
> a collision.

A collision is expected reuse when scope separates occurrences; unresolved
ambiguity when reading, class, scope, attachment, or target is unknown; possible
misclassification when context contradicts a proposed class; or a later
equivalence candidate only after an explicit claim is supported and reviewed.

An uncertain target does not invalidate a readable occurrence. Attach
uncertainty only where resolution could materially change value, class, scope,
attachment, target, status, or downstream claim. Page or object association
alone is insufficient.

## Cross-publication controls

```text
toyota-land-cruiser-70-jdm-1993-05 :: H8
!=
toyota-ewd168f :: H8
```

Matching connector identifiers, component names, terminal numbers, page
numbers, or harness names do not establish physical identity. Names may support
terminology comparison only. Another Toyota English publication may support
normalization, but cannot broaden identifier scope, transfer market/date/
engine/equipment applicability, or become primary evidence for the Japanese
publication. Equivalence belongs to a later reviewed claim citing the original
occurrences.

## Provenance and review

Every occurrence remains traceable to controlling publication, artifact
fingerprint, PDF page, printed page when present, and locatable occurrence or
boundary. Preserve exact form, proposed class and scope with review status,
material visible attachment, and same-publication dependencies needed to read
it. Reference resolution separately records the reference, proposed target, and
supporting convention. Later engineering claims retain the source occurrences
and their own applicability evidence.

Review asks whether the occurrence is correctly located and transcribed; case,
punctuation, spacing, and typography are preserved; class and scope are
supported; attachment is visible; target resolution is direct, guidance-based,
provisional, ambiguous, unresolved, conflicting, or rejected; source identity
has been confused with structural, engineering, or graph identity; or matching
text has incorrectly implied equivalence or applicability. Use granular
uncertainties and descriptive states, not numeric confidence scores.

## Pilot examples

These examples do not create decompositions or graph facts.

### Printed page `2-3`

PDF page 15 displays `2-3`, grid columns `1`-`6` and rows `A`-`D`, harness
legend keys `A`-`I`, `f`, `g`, `i`, and `ℓ`, connector callout identifiers,
`1HZ`/`1PZ` qualifiers, production marks, and publication marks.

```text
grid row A != legend key A
```

The two `A` occurrences differ in occurrence, class, scope, and reference role;
structural IDs distinguish them. Upper/lowercase keys remain distinct. A legend
key is a presentation reference, not automatically a harness entity. A
connector label remains source-local. `2-3` needs publication, artifact, and
PDF-page context.

### Printed page `2-7`

PDF page 19 displays grid coordinates, connector callouts, case-sensitive keys
including `H`, `J`, `K`, `k`, `p`, and `q`, LH/RH qualifiers, `1HZ`/`1PZ`
qualifiers, and production-date qualifiers. Identifiers and qualifiers have
different roles: `p` remains a key while `(LH)` limits associated wording.
Translation may render the harness name but cannot replace `p`. Similar
connector depictions keep separate occurrence identities; matching labels do
not establish physical identity.

### Printed page `3-2`

PDF page 40 displays `R/B NO.1`, `F/B NO.1`, fuse and relay designations,
terminal marks `ACC`, `AM1`, `IG`, `ST1`, `B`, `S`, and `L`, connector labels
including `i1`, `E1`, `H70`, and `H127`, cavity marks, wire-color labels such
as `青-白`, production keys `○` and `□`, page `3-2`, and component text.

A block designation is not canonical block identity. A terminal marked `30`
would not become graph terminal `30` without a reviewed claim establishing its
owner and context. Cavity number is not terminal identity. Wire-color label is
not wire identity. A production mark is not resolved applicability. A component
label is not canonical component identity.

## Relationships and sibling boundaries

The Milestone 7 records remain valid, review-ready, unchanged, and canonical
only for their translation-artifact role. They are not decompositions, graph
extractions, accepted translations, factory facts, or graph facts. Their
grouped units are not defective.

Issue #30 must bind translation to stable occurrences or regions without using
displayed values as unique keys: source identifiers remain verbatim, repeated
values remain distinguishable, one translation may relate to several
occurrences, and translated wording never becomes the identifier. No binding
model or migration is defined here.

Issue #32 will define graph-extraction contracts. Here, source identifiers
remain evidence, structural IDs locate source objects, candidate entity IDs
belong downstream, accepted graph IDs require governance, and equivalence is an
evidenced claim. No candidate record or graph schema is defined.

- #28 owns semantic layers and authority.
- #34 owns source-visible object classes.
- #27 owns page decomposition, relationships, and structural identity needs.
- #29 owns identifier roles, scopes, stability, collisions, and preservation.
- #30 owns translation bindings.
- #31 validates across publication families.
- #32 owns extraction contracts and engineering identity claims.

Completed Issues #27, #28, and #34 are not redesigned; Issues #30-#32 are not
started.

## Alternatives considered

- **Visible values as unique keys — rejected.** Values collide even within one
  pilot page and across roles, pages, artifacts, and publications.
- **One global namespace — rejected.** It collapses factory designation,
  structural review identity, candidate identity, and accepted identity.
- **Opaque IDs only — rejected.** Opaque structural identity is useful but
  cannot replace preserved source designation.
- **Scoped occurrence identity — recommended conceptually.** Use verified
  publication, artifact, and page-or-boundary context plus a locally assigned
  stable occurrence component. Identifier value and class may support indexing,
  review, aliases, and diagnostics, but do not determine durable occurrence
  identity. Exact syntax and mandatory components remain open.
- **Delay until schema — rejected.** Issues #30 and #32 need ownership and scope
  boundaries before binding and extraction design, though syntax stays deferred.

## Unresolved questions

- Which structural occurrence identity components are mandatory?
- Are structural IDs stable across rescans?
- How should identity survive page remapping, splits, and merges?
- Should publication-family scope exist?
- Which source identifiers are publication-unique?
- How should one occurrence with multiple readings be represented?
- When is a reference sufficiently resolved for extraction?
- How should equivalence claims cite original occurrences?
- Which answers require Issue #31 evidence?
- Which decisions require an ADR after Issues #30-#32?

## Explicit non-goals

This investigation does not define JSON, schemas, syntax, validators,
migrations, or canonical structural IDs; create graph IDs or entities; modify
or normalize source identifiers; resolve equivalence; establish applicability;
decompose pages; modify translations; create bindings; implement extraction;
add dependencies; or authorize production-scale translation.

## Design recommendation and ADR decision

Adopt source-visible occurrence plus exact value, reviewed class and narrowest
supported scope, separate reference and target, artifact-bound structural
occurrence identity, and strictly downstream engineering and graph identity.
Preserve collisions instead of merging them. Require explicit evidence and
review for every scope expansion or equivalence claim. Durable structural
identity follows the occurrence and its verified evidence context, not mutable
identifier class or displayed value; classification corrections therefore do
not replace the occurrence identity.

No invariant changes, so no immediate ADR is needed. Keep the design
provisional and defer a focused ADR until Issues #30-#32 establish the binding
and extraction contracts that consume these identifiers.
