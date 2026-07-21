# Toyota Land Cruiser 70 Translation Records

This directory contains canonical JSON translation records derived from the
Japanese Toyota publication `toyota-land-cruiser-70-jdm-1993-05`. The original
publication remains primary evidence. These records are repository-created
translation aids, not Toyota-authored English, factory facts, or graph facts.

The first production set covers only the Milestone 7 targets cleared without
material ambiguity:

- `pages/2-3.json` — `PILOT-TGT-005`, PDF 15;
- `pages/2-7.json` — `PILOT-TGT-006`, PDF 19; and
- `pages/3-2.json` — `PILOT-TGT-008`, PDF 40.

All three records are `review_ready`, not accepted. Their source readings were
machine-cross-checked, their English is provisional literal wording, and no
engineering normalization has been accepted. Qualified language-fidelity and
engineering-terminology review remain separate future gates.

Validate the records with:

```sh
python3 scripts/validate-translation-records.py \
  translations/toyota/land-cruiser-70-jdm-1993-05/pages/*.json
```

The frozen boundary, evidence mappings, dependency attachments, and ambiguity
dispositions remain in the corresponding
[`work/translation`](../../../work/translation/toyota-land-cruiser-70-jdm-1993-05/README.md)
workspace.
