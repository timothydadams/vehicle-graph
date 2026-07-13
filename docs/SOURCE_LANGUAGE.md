# Source Language

## Meaning

“Source language” is the technical language a publication uses to communicate
meaning. It includes not only prose, but also the publication's symbols,
notation, terminology, layout rules, cross-references, and applicability
qualifiers. A factory publication must be treated as a self-describing technical
language because familiar-looking marks may have publisher-specific meanings.

Source-language material may include:

- “how to use this manual” sections and interpretation instructions;
- symbol legends and abbreviations;
- connector numbering and cavity-depiction rules;
- relay-block, junction-block, and junction-connector notation;
- wire-color notation, including base-color and stripe conventions;
- continuation and related-system references;
- state/contact tables;
- applicability qualifiers and variation notation; and
- page, section, figure, table, and location cross-references.

Before detailed extraction, contributors must locate and review the explanatory
material within the same publication that governs the selected target. The
required pages or sections must be recorded in the source inventory,
publication-specific source-language record, or extraction boundary and cited
during extraction and independent review.

## Knowledge Boundaries

Source-language evidence defines how the publication communicates. Extracted
engineering claims are statements taken from a specific target diagram, table,
figure, or procedure using that language. Contributor interpretation explains
meaning not directly stated by the source and must be labeled as interpretation.
Derived knowledge is a conclusion produced from one or more accepted claims; it
does not become a new source statement.

Normalized wording may accompany source wording, but it must not erase or
silently replace publisher terminology when that terminology carries meaning.
Toyota terminology and the terminology of every other publisher must be
preserved under the same rule.

No source symbol or convention may be interpreted from context when the same
publication defines it elsewhere. Generic engineering assumptions must not
replace source-defined semantics, even when the generic interpretation appears
familiar or likely.

## Recording Interpretive Dependencies

A source-language page becomes a candidate-level interpretive dependency only
when it defines notation or a convention materially required to read that
candidate's primary evidence. Dependencies should be as narrow as practical and
should identify the specific convention being applied.

Do not attach an explanatory page when the candidate is a directly readable
label or statement that does not use the page's convention. Copying every
notation page onto every candidate is bad provenance: it hides which guidance
actually supports the reading and can misrepresent explanatory material as the
source of the engineering claim.

For example, in an EWD-style publication:

- a striped wire-color code may depend on the publication's color-code rule;
- a circled relay-block number may depend on the relay-block legend;
- a connector cavity mapping may depend on the connector numbering convention;
- a title printed inside a component may depend on the publication's statement
  that such titles are terminal names or codes; and
- a plain component label needs no notation dependency merely because it appears
  on the same diagram.

These examples are publication-pattern examples, not Toyota-only rules. Each
publication must supply its own definitions. Independent review checks that
every recorded dependency is necessary and accurate and that no required
dependency is missing.

## Blocking and Non-Blocking Source-Language Uncertainty

Source-language uncertainty concerns whether the publication's marks and
conventions can be read and applied faithfully. Object or application
uncertainty concerns broader meaning, scope, or later representation. The first
may block transcription; the second does not automatically do so.

Hard blockers include an unreadable symbol, an undefined convention needed to
distinguish two possible connections, unknown terminal-numbering rules when
mapping terminals, or inadequate evidence quality for the selected claim. A
hard blocker applies only to the affected boundary. Extraction may proceed
around it only when the boundary can be narrowed without losing source meaning.

Soft ambiguities include unresolved target applicability, incomplete knowledge
of an object's broader engineering role, uncertainty about future canonical
representation, or an unknown meaning beyond a visible source label or
relationship. A visible label or relationship may be transcribed neutrally
while its broader meaning remains unresolved.

Source-language review must enable faithful transcription; it does not require
complete engineering interpretation. Ambiguity is acceptable in candidate
extraction when it is recorded and cited on affected claims. Unsupported
completion is not acceptable.

Use this decision test:

> Does the unresolved issue prevent faithful transcription?

- **Yes:** stop or narrow the affected boundary.
- **No:** record the ambiguity and continue.

## Unresolved Source Language

Search the publication for an explicit definition before recording a symbol or
convention as ambiguous. If the publication's guidance is missing, incomplete,
illegible, or genuinely ambiguous, record:

- the unresolved symbol, term, or convention;
- the affected target and explanatory source locations;
- why the uncertainty could change the extraction;
- the evidence needed to resolve it; and
- whether detailed extraction must stop for the affected boundary.

Working notes about source-language guidance remain pre-canonical unless they
pass the repository's acceptance process. The guidance may be evidence for an
interpretation without making the working note an accepted factory fact.

## Use Across Publications

The rule applies to each publication on its own terms. Different publishers,
publication families, languages, revisions, diagram types, parts catalogs,
service procedures, and tabular references may define different technical
languages. Contributors must identify the relevant explanatory material anew
for each source rather than carrying one publisher's conventions into another.
