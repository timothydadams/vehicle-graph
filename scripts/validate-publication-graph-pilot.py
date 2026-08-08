#!/usr/bin/env python3
"""Validate the deliberately bounded Issue 44 experimental pilot package."""

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "work/publication-graph-pilot/issue-44/phase-2"
PUB = "toyota-land-cruiser-70-jdm-1993-05"
HASH = "sha256:1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6"


def load(package, name):
    return json.loads((package / name).read_text(encoding="utf-8"))


def validate(package=DEFAULT):
    errors = []
    required = ["verification.json", "publication-representation.json", "translation-binding.json", "applicability.json", "candidate.json", "review/manifest.json"]
    for name in required:
        if not (package / name).is_file(): errors.append(f"missing {name}")
    if errors: return errors
    verification, representation, binding, applicability, candidate, manifest = (load(package, name) for name in required)

    for name, record in (("verification", verification), ("representation", representation)):
        if record.get("publication_id") != PUB: errors.append(f"{name}: wrong publication")
        if record.get("artifact_fingerprint") != HASH: errors.append(f"{name}: wrong artifact fingerprint")
        location = record.get("source_location", {})
        if (location.get("pdf_page"), location.get("printed_page"), location.get("region_id")) != (40, "3-2", "PILOT-TGT-008"):
            errors.append(f"{name}: wrong frozen page mapping")
    if verification.get("status") != "passed": errors.append("verification gate did not pass")

    occurrences = representation.get("occurrences", [])
    occurrence_ids = [item.get("occurrence_id") for item in occurrences]
    if len(occurrence_ids) != len(set(occurrence_ids)): errors.append("source occurrence identities are not unique")
    relationship_ids = [item.get("relationship_id") for item in representation.get("relationships", [])]
    if len(relationship_ids) != len(set(relationship_ids)): errors.append("source relationship identities are not unique")
    selected = representation.get("selected_ground_occurrence_id")
    grounds = [item for item in occurrences if item.get("kind") == "ground_symbol_occurrence"]
    if len([item for item in grounds if item.get("occurrence_id") == selected]) != 1: errors.append("exactly one existing ground occurrence must be selected")
    if len([item for item in grounds if item.get("candidate_role") != "explicitly_not_selected"]) != 1: errors.append("exactly one ground occurrence may remain in candidate scope")

    if binding.get("source_occurrence_id") not in occurrence_ids: errors.append("translation binding must target a source occurrence")
    if binding.get("is_primary_evidence") is not False or binding.get("role") != "linguistic_identification_only": errors.append("translation binding must remain non-primary identification support")
    if binding.get("status") != "review_ready" or binding.get("language_review") != "incomplete": errors.append("translation binding must retain actual review-ready/incomplete review state")

    ambiguity = applicability.get("ambiguity", {})
    if applicability.get("status") != "unresolved_material" or applicability.get("candidate_specific_production_scope") is not None: errors.append("candidate-specific production applicability must remain explicitly unresolved")
    if applicability.get("canonical_acceptance_prohibited") is not True: errors.append("unresolved applicability must prohibit acceptance")
    prohibited = " ".join(applicability.get("prohibited_derivations", [])).lower()
    for phrase in ("default scope", "union", "common to both", "1990 pzj70"):
        if phrase not in prohibited: errors.append(f"missing prohibited applicability derivation: {phrase}")

    if candidate.get("candidate_id") in occurrence_ids or candidate.get("candidate_id") in relationship_ids: errors.append("candidate identity must remain separate from source identities")
    if len(candidate.get("endpoints", [])) != 2: errors.append("candidate must have exactly two endpoints")
    if candidate.get("relationship", {}).get("kind") != "electrically_connected_to": errors.append("package must contain exactly one candidate relationship")
    if candidate.get("applicability", {}).get("ambiguity_id") != ambiguity.get("ambiguity_id"): errors.append("material applicability ambiguity must attach to candidate")
    if candidate.get("canonical_acceptance_prohibited") is not True or candidate.get("canonical_graph_write") is not False: errors.append("candidate must prohibit acceptance and canonical graph writes")
    if "visible_continuity" not in json.dumps(representation) or "electrically_connected_to" in json.dumps(representation): errors.append("source-visible path must remain distinct from candidate connectivity")

    if manifest.get("candidate_id") != candidate.get("candidate_id"): errors.append("review package targets wrong candidate")
    if manifest.get("canonical_graph_write") is not False: errors.append("review package may not mutate canonical graph data")
    if manifest.get("status") == "complete":
        result = load(package, "review/result.json")
        if result.get("reviewer", {}).get("independent_from_proposal") is not True: errors.append("completed extraction review must be independent")
    eligibility_path = package / "eligibility.json"
    if eligibility_path.exists():
        eligibility = load(package, "eligibility.json")
        if eligibility.get("decision") != "ineligible": errors.append("unresolved material applicability requires ineligible")
        if eligibility.get("canonical_disposition") != "blocked_pending_approved_authority": errors.append("eligibility must remain separate from disposition")
        if eligibility.get("rejected") is not False: errors.append("ineligible is not rejected")
        if eligibility.get("canonical_graph_write") is not False: errors.append("eligibility may not mutate canonical graph data")
    lifecycle_path = package / "lifecycle-test.json"
    if lifecycle_path.exists():
        lifecycle = load(package, "lifecycle-test.json")
        if lifecycle.get("factory_evidence_changed") is not False or lifecycle.get("prior_versions_preserved") is not True: errors.append("lifecycle test must preserve evidence and prior versions")
        expected = {"candidate": "stale", "extraction_review": "review_required", "eligibility": "review_required", "disposition_reference": "review_required"}
        if lifecycle.get("dependent_states") != expected: errors.append("lifecycle staleness did not propagate to every required dependent")

    tracked = subprocess.run(["git", "ls-files", ".evidence"], cwd=ROOT, text=True, capture_output=True, check=False).stdout.strip()
    if tracked: errors.append("private evidence is tracked")
    canonical_candidates = list((ROOT / "data").rglob("*.json")) if (ROOT / "data").exists() else []
    if canonical_candidates: errors.append("pilot unexpectedly introduced canonical data files")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("package", nargs="?", type=Path, default=DEFAULT)
    args = parser.parse_args()
    errors = validate(args.package)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Issue 44 bounded pilot package validates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
