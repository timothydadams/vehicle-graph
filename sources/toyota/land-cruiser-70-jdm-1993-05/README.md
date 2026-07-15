# Japanese Land Cruiser 70 EWD Source Catalog

This directory contains committed source-catalog records only. It catalogs
Toyota publication `6742601`, `トヨタ ランドクルーザー70 配線図集`; it does not
contain the publication itself, a translation, or accepted factory knowledge.

The actual factory PDF is intentionally not committed. A contributor with a
lawfully obtained copy should place it at:

```text
.evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf
```

Working derivatives may be placed under:

```text
.evidence/toyota/land-cruiser-70-jdm-1993-05/working/
```

Preserved direct captures may be placed under:

```text
.evidence/toyota/land-cruiser-70-jdm-1993-05/captures/
```

Everything under `.evidence/` is private, contributor-supplied local material
and is ignored by Git. The [metadata record](metadata.json) describes the
expected location; committed metadata does not prove that the PDF, a working
derivative, or a capture exists in another checkout. The
[page index](page-index.md) is a provisional navigation record under the same
constraint.

A recorded fingerprint identifies the local artifact that was reviewed. It
does not distribute or embed the source or guarantee the artifact's presence in
another checkout.

Source claims must cite publication number `6742601` and the printed page,
figure, table, or other publication location. A local file path alone is
insufficient provenance.

This catalog does not establish applicability to a 1990 PZJ70. The source is a
January 1995 publication stated to apply to `KZJ7#`, `PZJ7#`, and `HZJ7#`
production from May 1993. The publication date and production-applicability
start are separate facts; this is not a 1993 publication. Translation and graph
extraction belong to later, separately reviewable work.

## Fingerprinting the Local Artifact

After supplying the PDF, run this command from the repository root:

```shell
python3 scripts/fingerprint-source.py \
  .evidence/toyota/land-cruiser-70-jdm-1993-05/original.pdf
```

The helper reports the path, byte size, and SHA-256. It does not report a page
count and does not modify `metadata.json` automatically. Record reviewed
fingerprint or page-count values only in a separate reviewable change.
