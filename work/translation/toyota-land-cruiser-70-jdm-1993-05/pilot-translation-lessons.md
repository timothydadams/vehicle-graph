# Pilot Translation Record Lessons

## Scope and status

Milestone 7 produced review-ready records only for `PILOT-TGT-005`,
`PILOT-TGT-006`, and `PILOT-TGT-008`. It did not translate blocked
`PILOT-TGT-007`, change the frozen evidence boundary, perform human Japanese
review, accept engineering terminology, accept a translation, or extract graph
facts.

## What fit naturally

The current model made the following decisions explicit and reviewable:

- the frozen artifact fingerprint and both PDF and printed coordinates;
- complete bounded coverage with no hidden omission or unreadable region;
- exact source transcription beside provisional literal English;
- source-local qualifiers and identifiers that must not be normalized away;
- same-publication interpretive dependencies attached only to affected units;
- separate proposal, source-reading, literal-translation, and engineering-term
  review states; and
- review-ready status without implying translation or graph acceptance.

The circuit record also demonstrated narrow dependency attachment: the
power/ground convention applies to diagram notation, the two-color rule applies
to wire labels, and block/connector conventions apply only to the notation they
explain.

## Where the schema felt awkward

Full-page harness and circuit diagrams contain both language that can be
translated and dense graphical structure that must be preserved but is not
English prose. The current `content_units` model can represent visible labels,
identifiers, and layout notes, but it has no dedicated structured vocabulary
for connector shapes, cavity arrays, conductor paths, joins, symbol placement,
or the binding between a leader line and its depicted endpoint.

The pilot records therefore group source-local diagram notation and preserve
its graphical role in `layout_notes`. That is auditable at page level, but less
granular than the model is for a heading or table cell. The schema also requires
a literal-translation disposition for entirely nonlinguistic units;
`not_applicable` works, although it is repetitive.

No validation rule was weakened, and the schema was not redesigned to hide
this friction.

## Recommendation after more experience

Keep the current schema for independent review of these records. After more
diagram pages have been authored and reviewed, evaluate whether a small,
diagram-specific content kind or explicit source-structure binding is justified.
Any proposal should be based on repeated review failures or lost provenance,
not authoring convenience alone. Normalized terminology should likewise wait
for evidenced terminology promotion rather than being inferred from plausible
English.

The model appears scalable to hundreds of pages for provenance, status, review,
and textual content. Diagram-heavy scaling will be labor-intensive, and its
practical limit should be reassessed after independent reviewers test whether
the grouped graphical notation can be reconstructed reliably from the cited
page and dependency locations.
