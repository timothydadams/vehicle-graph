# One Diagram

## Purpose

**One Diagram** is the first working milestone for Vehicle Graph.

The milestone will preserve and model the factory headlight wiring information contained in the electric wiring diagram material included with Toyota repair manual EWD168F. The result will be one trustworthy, reproducible view for one explicitly stated vehicle application.

This milestone is intentionally narrow. Its purpose is to test the repository's documentation, provenance, applicability, extraction, review, canonical-data, validation, and derived-view principles against real factory material before a broader model is designed.

The source material remains authoritative. Vehicle Graph will preserve structured claims extracted from that material; it will not replace, rewrite, or present itself as the factory publication.

## Milestone question

The milestone should answer:

> Can Vehicle Graph reproduce the electrically meaningful content of the applicable EWD168F headlight wiring diagram from reviewed, traceable, repository-local facts without losing source meaning, applicability, ambiguity, or provenance?

Everything added during this milestone must directly support answering that question.

## Selected source

The initial source artifact is the user's physical copy of:

* Toyota repair manual identifier: **EWD168F**
* source area: the electric wiring diagram material included with the manual;
* initial system: **headlights**.

The complete publication identity must be recorded from the physical artifact before extraction begins. This includes, when available:

* exact publication title;
* publication number as printed;
* edition or revision;
* publication date;
* copyright or issue information;
* volume, appendix, or section identity;
* language;
* any notices that limit or qualify application.

The repository must not assume that an electric wiring diagram identifier, edition, or applicability is established merely because it has been discussed previously. The physical source must establish its own identity.

Until the source has been inspected, the following remain unresolved:

* the exact diagram title used by Toyota;
* the page or page range containing the headlight circuit;
* whether the complete circuit appears on one page or multiple pages;
* whether related pages, connector views, location diagrams, legends, or tables are required;
* whether EWD168F includes more than one applicable headlight circuit;
* whether light-duty and heavy-duty variants are distinguished;
* the source-stated model, market, production-date, equipment, or other applicability limits.

These are extraction questions, not assumptions to resolve in advance.

## Target vehicle application

The intended vehicle context is the identified 1990 Toyota Land Cruiser PZJ70 that motivated this repository.

Known vehicle details may guide source review, but they do not determine factory applicability by themselves. The source must first state or support the configuration to which each extracted fact applies.

Before canonical factory facts are accepted, the milestone must document the narrowest source-supported application using whatever distinctions EWD168F provides, which may include:

* model or model code;
* chassis series;
* engine;
* electrical-system voltage;
* body configuration;
* market or destination;
* light-duty or heavy-duty classification;
* production date or serial-number range;
* installed equipment or option;
* publication revision.

Unknown applicability remains unknown. Similarity to the target vehicle does not establish applicability.

Vehicle-specific observations, confirmations, modifications, or deviations are outside the factory knowledge layer. If later needed to validate the derived diagram against the identified vehicle, they must be recorded separately as a vehicle overlay with their own evidence.

## Extraction target

The initial extraction target is the factory circuit Toyota identifies as the headlight or headlamp system within the EWD168F electric wiring diagram material.

The extraction boundary will be finalized only after the relevant source pages have been located and reviewed.

The target boundary should include the smallest coherent set of source material needed to understand and reproduce the selected circuit. Depending on the publication, that may include:

* the primary headlight wiring diagram;
* continuation pages;
* source legends and symbol definitions;
* connector or terminal references necessary to interpret the circuit;
* junction, splice, relay, fuse, fusible-link, switch, lamp, indicator, power, and ground information shown as part of the circuit;
* variant or applicability notes printed with the diagram;
* referenced tables or explanatory notes required to interpret what is shown.

Material should not be included merely because it concerns lighting generally. Each supporting page must be necessary to interpret, trace, validate, or reproduce the selected headlight circuit.

## Initial boundary rules

The milestone begins with the electrical circuit, not the complete headlight product or vehicle lighting system.

The extraction may include:

* electrically participating components shown by the selected source;
* component identifiers and labels printed by Toyota;
* terminals, connector cavities, junctions, splices, and grounds required to preserve connectivity;
* conductor paths and source-stated conductor attributes;
* switch contacts and internal connections shown by the source;
* fuses, fusible links, relays, power sources, loads, and indicators shown in the circuit;
* off-page references and continuations;
* source-stated operating conditions or variant notes;
* unresolved source ambiguity.

The extraction does not automatically include:

* Toyota service-part numbers;
* complete headlamp assemblies or their non-electrical subcomponents;
* bulbs, housings, brackets, fasteners, trim, or mounting hardware not electrically represented by the selected diagram;
* physical harness routing beyond what is necessary to identify or interpret the circuit;
* repair procedures;
* diagnostic procedures;
* replacement recommendations;
* aftermarket modifications;
* inferred current paths or operating behavior not stated or depicted by the source;
* facts taken from other publications merely to make the first graph more complete.

A concept enters the milestone only when reviewed source material or a demonstrated need to reproduce the selected diagram requires it.

## Pre-scan source handling

No page should be treated as extraction evidence until the physical source has been inventoried.

Before scanning diagram pages:

1. Photograph or scan the manual cover and publication-identification pages.
2. Record the manual's printed publication identity.
3. Locate the electric wiring diagram section and record its structural relationship to EWD168F.
4. Inspect the section index or contents pages.
5. Identify every candidate page associated with the headlight circuit.
6. Identify any legends, symbol keys, applicability tables, connector references, or continuation pages required to read the candidate diagram.
7. Record the apparent page boundaries before choosing the final extraction set.
8. Resolve whether multiple headlight variants are present or preserve that question as explicit ambiguity.

The initial inventory may use reference images or notes, but no extracted claim becomes accepted factory knowledge until reviewed against adequately preserved evidence.

## Evidence capture requirements

Scans must preserve enough context for an independent reviewer to:

* identify the physical publication;
* locate the original page;
* read page numbers, section headings, notes, and applicability statements;
* distinguish printed content from handwritten marks, damage, shadows, or scanning artifacts;
* follow all circuit continuations;
* inspect conductor labels, terminal labels, component labels, junctions, and line intersections;
* determine whether nearby legends or notes alter interpretation.

Scanning should favor fidelity over image cleanup. Original evidence must remain distinguishable from any cropped, rotated, contrast-adjusted, annotated, or otherwise processed derivative.

When processing improves legibility, retain both:

* the preserved source capture; and
* the processed working image.

Processed images are aids to extraction and review. They do not replace the preserved evidence.

## Source inventory deliverable

Before schema discovery begins, the repository should contain a reviewed source inventory describing:

* the EWD168F publication identity;
* the electric wiring diagram section identity;
* the candidate headlight pages;
* each supporting page required for interpretation;
* known source-stated applicability;
* unresolved applicability;
* visible diagram variants;
* page continuations and dependencies;
* scan completeness and quality limitations;
* the proposed final extraction boundary.

The inventory should make it possible to agree on exactly what will be extracted before claims are transcribed.

## Fact discovery

The first diagram will be used to discover the minimum vocabulary needed by the canonical model.

Schema discovery must begin from visible source claims rather than a predefined automotive ontology.

During source review, the team will inventory at least:

* things depicted;
* connection points depicted;
* electrical connections depicted;
* labels and attributes printed;
* internal component relationships depicted;
* variant and applicability statements;
* continuation mechanisms;
* ambiguous symbols or intersections;
* information required by the source but defined elsewhere in the publication.

Candidate entities, relationships, and attributes may be proposed during this inventory, but they do not become general project vocabulary merely because they appear useful.

Every proposed concept must answer:

1. What exact source content requires this concept?
2. Is the concept necessary to preserve meaning or reproduce the selected diagram?
3. Can an existing, simpler structure represent the same claim faithfully?
4. Is the concept factory knowledge, vehicle-overlay knowledge, provenance, applicability, or derived presentation?
5. Are we transcribing something shown, normalizing source terminology, or interpreting engineering meaning?

The smallest faithful vocabulary wins.

## Atomicity

Extraction will record the smallest independently meaningful claims that can be reviewed against the source.

A record should not combine unrelated claims merely because they concern the same component or page.

The appropriate atomic boundary will be discovered through the diagram, but each accepted claim must be independently:

* identifiable;
* reviewable;
* traceable to evidence;
* assigned applicability;
* capable of being superseded or corrected without silently changing other claims;
* consumable by a derived view.

Atomicity must not be pursued so mechanically that source meaning is fragmented or lost. The milestone should use the smallest units that remain independently meaningful.

## Transcription and interpretation

The milestone must distinguish:

* direct transcription of source content;
* normalization of source notation;
* interpretation of depicted meaning;
* derived conclusions produced from accepted facts.

Toyota's printed terminology and notation must be preserved even when normalized values are also recorded.

Interpretations must never be disguised as transcription. When a diagram is unclear, the ambiguity should be recorded rather than resolved through undocumented electrical assumptions.

A derived renderer may trace or arrange accepted connections, but its output does not establish new factory facts.

## Provenance requirements

Every accepted factory fact must identify:

* the EWD168F source artifact;
* the exact page, figure, table, legend, or equivalent source location;
* the preserved evidence asset;
* whether the claim was transcribed, normalized, or interpreted;
* the extraction method;
* the person or process responsible for extraction;
* the review and acceptance state;
* any ambiguity, conflict, damage, or source limitation affecting the claim.

Provenance may be referenced through shared records when many facts rely on the same evidence location, but it must remain possible to trace each fact independently.

A generated diagram inherits provenance from its underlying facts. It is never its own source.

## Applicability requirements

Every accepted fact must carry the narrowest applicability justified by its evidence.

Applicability must distinguish:

* scope printed or otherwise stated by the source;
* scope inferred during review;
* unresolved scope;
* the factory configuration described;
* the identified vehicle used as the target context.

No tool or reviewer may broaden applicability simply because no exception has yet been found.

If different portions of the headlight circuit have different applicability, applicability must be recorded at the fact level rather than assigned only to the diagram as a whole.

## Review requirements

Extraction and review are separate responsibilities even when performed by the same contributor at different times.

A fact is not accepted merely because it has been transcribed into JSON.

Review must verify:

* agreement with the preserved source;
* correct source location;
* correct distinction between transcription and interpretation;
* narrow and supportable applicability;
* explicit preservation of ambiguity;
* structural consistency with related accepted facts;
* absence of unsupported completion or inferred relationships.

Corrections must preserve the prior accepted meaning and explicitly supersede, narrow, or replace it according to the repository's eventual correction mechanism. Git history alone is not a semantic correction record.

## Canonical representation

Canonical structured knowledge produced by this milestone will be stored as straightforward JSON in Git.

The exact identifiers, field names, file layout, relationship vocabulary, JSON Schema, and validation implementation will be decided only after representative headlight source material has been reviewed.

The canonical representation must remain independent of:

* a particular diagram renderer;
* database storage;
* graph-database conventions;
* user-interface requirements;
* extraction software;
* AI context formats.

Source images, working notes, extraction candidates, accepted factory facts, vehicle overlays, and generated outputs must remain conceptually distinguishable even if the final repository layout places some of them near one another.

## Derived diagram

The milestone will produce a derived headlight wiring view from accepted canonical facts.

The derived view must:

* identify the factory source;
* disclose the vehicle application used to select facts;
* remain visibly distinguishable from Toyota factory documentation;
* reproduce the electrically meaningful content within the agreed extraction boundary;
* preserve meaningful component, terminal, conductor, connector, junction, power, ground, switch, protection, and variant information required by the source;
* expose or link to the provenance of the facts it presents;
* disclose unresolved ambiguity or incomplete extraction;
* be reproducible from repository-local canonical data and replaceable tooling.

The renderer may choose a clearer visual arrangement than the source publication, but it must not silently alter the engineering meaning.

Rendered coordinates and presentation choices are derived data, not canonical factory facts.

## Validation

Validation has two separate targets.

### Knowledge validation

Canonical facts must be checked for:

* required identity;
* provenance;
* applicability;
* valid references;
* structural consistency;
* unresolved ambiguity where appropriate;
* accidental duplication or contradiction;
* unsupported claims.

Validation may detect omissions or contradictions. It must not invent missing facts or choose among ambiguous interpretations.

### Diagram validation

The generated view must be reviewed against:

* the complete selected source boundary;
* the accepted canonical facts;
* the stated target application.

Review should confirm that every electrically meaningful source feature inside the agreed boundary is either:

* represented;
* explicitly deferred;
* marked ambiguous; or
* documented as outside scope.

The diagram need not imitate the factory page layout. It must preserve the source's engineering meaning.

## Completion criteria

**One Diagram** is complete when:

1. EWD168F and its included electric wiring diagram material are unambiguously identified.
2. The headlight extraction boundary is documented and reviewed.
3. Required source pages and supporting context are preserved.
4. Source-stated and unresolved applicability are recorded.
5. The minimum necessary canonical vocabulary has been discovered from the source.
6. The selected circuit has been extracted into addressable atomic facts.
7. Every accepted fact has provenance and applicability.
8. Transcription, normalization, interpretation, and derivation remain distinguishable.
9. Factory facts and any vehicle-specific overlay facts remain separate.
10. Canonical JSON passes milestone validation.
11. A headlight wiring view can be generated solely from accepted repository-local knowledge.
12. The generated view has been checked against both the source and the stated application.
13. A contributor can follow repository evidence from the generated view back to each material factory claim.
14. Known omissions and unresolved ambiguities are disclosed.
15. No unsupported engineering relationship has been added merely to make the result appear complete.

Completion does not require:

* complete modeling of EWD168F;
* complete modeling of the vehicle's lighting systems;
* a universal electrical or automotive ontology;
* a database;
* a web application;
* automated extraction;
* support for another vehicle, publication, system, or manufacturer;
* proof that the discovered schema will generalize unchanged.

## Stop conditions

The milestone should pause and document the problem rather than silently proceeding when:

* EWD168F's publication identity cannot be established;
* the headlight diagram cannot be located completely;
* required continuation or legend pages are missing;
* multiple variants exist and the applicable one cannot be distinguished;
* source quality prevents reliable transcription;
* applicability cannot be narrowed enough to support the intended derived view;
* the source contains a contradiction that materially changes circuit meaning;
* a proposed model requires undocumented assumptions to connect the circuit;
* canonical facts cannot reproduce the source without renderer-specific knowledge.

A stop condition is not failure. Explicitly preserving the limitation is more valuable than producing a complete-looking but untrustworthy graph.

## Immediate next step

After this document is accepted, the next task is source identification and inventory—not schema implementation.

The first source-handling session should capture the EWD168F publication-identification material, locate the electric wiring diagram contents and headlight section, and identify the complete candidate page set required for the extraction boundary.
