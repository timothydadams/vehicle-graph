# Issue 44 Phase 2 bounded pilot

These JSON records implement one experimental, pilot-bounded transformation for
publication `toyota-land-cruiser-70-jdm-1993-05`, PDF page 40 / printed page
`3-2` / `PILOT-TGT-008`. They are derived, versioned review artifacts. They are
not canonical factory knowledge and no record in this directory can write to
accepted graph data.

The records deliberately remain separate:

1. `verification.json` reverifies the frozen source inputs;
2. `publication-representation.json` records only relied-upon visible
   occurrences and structure;
3. `translation-binding.json` binds one Japanese label for identification;
4. `applicability.json` preserves the unresolved production dimension;
5. `candidate.json` owns the proposed electrical interpretation;
6. `review/` freezes and records independent extraction review;
7. `eligibility.json` records a non-dispositive eligibility decision; and
8. `lifecycle-test.json` records the controlled synthetic staleness exercise.

The candidate is an immutable proposal, so its intrinsic lifecycle state stays
`proposed`. Review completion and eligibility are derived from the separately
versioned review and eligibility artifacts; they do not mutate or silently
retarget the candidate.

The source artifact and all renders remain below `.evidence/` and are ignored.
Run `python3 scripts/validate-publication-graph-pilot.py` to validate the
package. The validator is intentionally specific to this experiment; it is not
a general publication-representation schema or production tool.

Canonical disposition is blocked pending approved authority. Ineligibility is
not rejection, PR merge is not disposition, and Issue #44 remains open.
