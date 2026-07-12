# Vision

Engineering knowledge contained in factory service information is valuable but
often difficult to preserve, navigate, and apply. It may be scattered across manuals, diagrams, tables, bulletins, and
vehicle-specific observations. Vehicle Graph will turn that information into a
structured engineering graph without losing its source, scope, or meaning.

The graph should answer practical questions such as:

- What does the factory say?
- Which vehicles does that statement apply to?
- Where did the statement come from?
- How does this particular vehicle differ from the factory description?
- What trustworthy diagram or other view can be produced from those facts?
- Why do we believe this statement?

The repository favors durability and auditability over novelty. Canonical JSON
files live in Git. Factory facts remain immutable. Knowledge about an individual
vehicle is expressed as a separate overlay. Every fact points back to evidence.

## Initial milestone: One Diagram

Success is demonstrated by one useful diagram for one explicitly identified vehicle
application. The diagram must be reproducible from traceable facts and must make
factory knowledge and vehicle-specific differences distinguishable.

This deliberately small milestone is a test of the whole philosophy. It is not
permission to design a universal platform in advance.

## Design philosophy

Vehicle Graph preserves engineering knowledge before it preserves software.

Every implementation decision should make the underlying knowledge easier to
understand, review, and reuse. Infrastructure exists to serve the knowledge
model, never the reverse.

## Long-term character

Vehicle Graph should remain understandable from the repository itself. A new
contributor should be able to inspect files, follow provenance, review changes,
and reconstruct derived outputs without access to hidden services. Tools may
improve extraction and presentation, but the knowledge must outlive any tool.
