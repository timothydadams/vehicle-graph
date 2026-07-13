# EWD168F Source Catalog

EWD168F is the selected source artifact for the
[One Diagram milestone](../../../docs/ONE_DIAGRAM.md). This directory contains
committed source-catalog records, not the publication itself and not accepted
factory facts.

The actual PDF is intentionally not committed. A contributor with a lawfully
obtained copy should place it at:

```text
.evidence/toyota/ewd168f/EWD168F.pdf
```

Working crops or rendered pages may be placed under:

```text
.evidence/toyota/ewd168f/working/
```

Preserved direct captures may be placed under:

```text
.evidence/toyota/ewd168f/captures/
```

Everything under `.evidence/` is private, contributor-supplied local material
and is ignored by Git. The [metadata record](metadata.json) describes the
expected location; it must not be read as confirmation that the PDF or any
working image is present. The [page index](page-index.md) maps provisional
evidence references to expected local forms under the same constraint.

Extracted claims must cite publication number `EWD168F` and the printed page,
figure, table, or other source location. A machine-specific local file path is
not sufficient provenance.

## Fingerprinting the Local Artifact

After supplying the PDF, run this command from the repository root:

```shell
python3 scripts/fingerprint-source.py \
  .evidence/toyota/ewd168f/EWD168F.pdf
```

Review the reported path, byte size, and SHA-256. Then copy the SHA-256 manually
into `metadata.json` and update `fingerprint_status` in a separate reviewable
change. The helper does not modify metadata automatically.
