#!/usr/bin/env python3
"""Validate the deliberately bounded Issue 44 experimental pilot package."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "work/publication-graph-pilot/issue-44/phase-2"
PUB = "toyota-land-cruiser-70-jdm-1993-05"
HASH = "sha256:1345fc0bd9601411b7b7f3b43c477d5119fd08d0c2b2672ca835ff55061627c6"
V1 = "I44-SR-PATH-CONTINUITY-001-v1"
V2 = "I44-SR-PATH-CONTINUITY-001-v2-synthetic"
REQUIRED = (
    "verification.json",
    "publication-representation.json",
    "translation-binding.json",
    "applicability.json",
    "candidate.json",
    "review/REVIEW_TASK.md",
    "review/manifest.json",
    "review/independent-source-account.md",
    "review/result.json",
    "eligibility.json",
    "lifecycle-relationship-v2.json",
    "lifecycle-test.json",
)


def load(package, name):
    return json.loads((package / name).read_text(encoding="utf-8"))


def derive_dependency_states(candidate, review, eligibility, active_relationship):
    """Derive freshness transitively; never read expected lifecycle states."""
    candidate_fresh = candidate.get("relationship", {}).get("source_structure_dependency") == active_relationship
    review_fresh = candidate_fresh and review.get("candidate_id") == candidate.get("candidate_id")
    eligibility_fresh = (
        review_fresh
        and eligibility.get("reviewed_candidate_id") == candidate.get("candidate_id")
        and eligibility.get("extraction_review_id") == review.get("review_id")
    )
    disposition_fresh = eligibility_fresh
    return {
        "candidate": "fresh" if candidate_fresh else "stale",
        "extraction_review": "fresh" if review_fresh else "review_required",
        "eligibility": "fresh" if eligibility_fresh else "review_required",
        "disposition_reference": "fresh" if disposition_fresh else "review_required",
    }


def validate(package=DEFAULT):
    errors = []
    missing = [name for name in REQUIRED if not (package / name).is_file()]
    if missing:
        return [f"missing {name}" for name in missing]

    verification = load(package, "verification.json")
    representation = load(package, "publication-representation.json")
    binding = load(package, "translation-binding.json")
    applicability = load(package, "applicability.json")
    candidate = load(package, "candidate.json")
    manifest = load(package, "review/manifest.json")
    result = load(package, "review/result.json")
    eligibility = load(package, "eligibility.json")
    synthetic = load(package, "lifecycle-relationship-v2.json")
    lifecycle = load(package, "lifecycle-test.json")

    if not (package / "review/REVIEW_TASK.md").read_text(encoding="utf-8").strip():
        errors.append("review task must not be empty")
    if not (package / "review/independent-source-account.md").read_text(encoding="utf-8").strip():
        errors.append("independent source account must not be empty")

    for name, record in (("verification", verification), ("representation", representation)):
        if record.get("publication_id") != PUB:
            errors.append(f"{name}: wrong publication")
        if record.get("artifact_fingerprint") != HASH:
            errors.append(f"{name}: wrong artifact fingerprint")
        location = record.get("source_location", {})
        if (location.get("pdf_page"), location.get("printed_page"), location.get("region_id")) != (40, "3-2", "PILOT-TGT-008"):
            errors.append(f"{name}: wrong frozen page mapping")
    if verification.get("status") != "passed":
        errors.append("verification gate did not pass")

    occurrences = representation.get("occurrences", [])
    occurrence_ids = [item.get("occurrence_id") for item in occurrences]
    if len(occurrence_ids) != len(set(occurrence_ids)):
        errors.append("source occurrence identities are not unique")
    relationship_ids = [item.get("relationship_id") for item in representation.get("relationships", [])]
    if len(relationship_ids) != len(set(relationship_ids)):
        errors.append("source relationship identities are not unique")
    selected = representation.get("selected_ground_occurrence_id")
    grounds = [item for item in occurrences if item.get("kind") == "ground_symbol_occurrence"]
    if len([item for item in grounds if item.get("occurrence_id") == selected]) != 1:
        errors.append("exactly one existing ground occurrence must be selected")
    if len([item for item in grounds if item.get("candidate_role") != "explicitly_not_selected"]) != 1:
        errors.append("exactly one ground occurrence may remain in candidate scope")

    candidate_records = []
    for path in package.rglob("*.json"):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append(f"invalid JSON: {path.relative_to(package)}")
            continue
        if record.get("record_type") == "experimental_engineering_candidate":
            candidate_records.append(record)
        record_type = record.get("record_type", "")
        if "disposition" in record_type and record_type != "graph_acceptance_eligibility_review":
            errors.append(f"canonical disposition artifact is prohibited: {path.relative_to(package)}")
        if record_type.startswith("canonical_") or record_type in {"accepted_graph_fact", "accepted_graph_relationship"}:
            errors.append(f"canonical graph artifact is prohibited: {path.relative_to(package)}")
    if len(candidate_records) != 1:
        errors.append("Phase 2 package must contain exactly one engineering candidate record")
    candidate_relationships = [record.get("relationship") for record in candidate_records if record.get("relationship")]
    if len(candidate_relationships) != 1:
        errors.append("Phase 2 package must contain exactly one candidate relationship")
    if any(record.get("relationships") for record in candidate_records):
        errors.append("Phase 2 package must not introduce a second candidate relationship")

    if binding.get("source_occurrence_id") not in occurrence_ids:
        errors.append("translation binding must target a source occurrence")
    if binding.get("is_primary_evidence") is not False or binding.get("role") != "linguistic_identification_only":
        errors.append("translation binding must remain non-primary identification support")
    if binding.get("status") != "review_ready" or binding.get("language_review") != "incomplete":
        errors.append("translation binding must retain actual review-ready/incomplete review state")

    ambiguity = applicability.get("ambiguity", {})
    if applicability.get("status") != "unresolved_material" or applicability.get("candidate_specific_production_scope") is not None:
        errors.append("candidate-specific production applicability must remain explicitly unresolved")
    if applicability.get("canonical_acceptance_prohibited") is not True:
        errors.append("unresolved applicability must prohibit acceptance")
    prohibited = " ".join(applicability.get("prohibited_derivations", [])).lower()
    for phrase in ("default scope", "union", "common to both", "1990 pzj70"):
        if phrase not in prohibited:
            errors.append(f"missing prohibited applicability derivation: {phrase}")

    candidate_id = candidate.get("candidate_id")
    if candidate_id in occurrence_ids or candidate_id in relationship_ids:
        errors.append("candidate identity must remain separate from source identities")
    if candidate.get("lifecycle_state") != "proposed":
        errors.append("candidate intrinsic lifecycle state must remain immutable 'proposed'")
    if len(candidate.get("endpoints", [])) != 2:
        errors.append("candidate must have exactly two endpoints")
    if candidate.get("relationship", {}).get("kind") != "electrically_connected_to":
        errors.append("package must contain exactly one candidate relationship")
    if candidate.get("applicability", {}).get("ambiguity_id") != ambiguity.get("ambiguity_id"):
        errors.append("material applicability ambiguity must attach to candidate")
    if candidate.get("canonical_acceptance_prohibited") is not True or candidate.get("canonical_graph_write") is not False:
        errors.append("candidate must prohibit acceptance and canonical graph writes")
    if "visible_continuity" not in json.dumps(representation) or "electrically_connected_to" in json.dumps(representation):
        errors.append("source-visible path must remain distinct from candidate connectivity")

    frozen = manifest.get("frozen_commit", "")
    if manifest.get("status") != "complete":
        errors.append("review manifest must be complete")
    if result.get("status") != "complete":
        errors.append("review result must be complete")
    if manifest.get("candidate_id") != candidate_id or result.get("candidate_id") != candidate_id:
        errors.append("review manifest, result, and candidate must use the same candidate ID")
    if manifest.get("review_id") != result.get("review_id"):
        errors.append("review manifest and result must use the same review ID")
    expected_outputs = {
        "work/publication-graph-pilot/issue-44/phase-2/review/independent-source-account.md",
        "work/publication-graph-pilot/issue-44/phase-2/review/result.json",
    }
    if set(manifest.get("outputs", [])) != expected_outputs:
        errors.append("review manifest must identify the complete review outputs")
    if not re.fullmatch(r"[0-9a-f]{40}", frozen):
        errors.append("review frozen commit must be a full 40-character Git commit")
    if result.get("frozen_commit") != frozen:
        errors.append("review manifest and result frozen commits disagree")
    if manifest.get("artifact_fingerprint") != HASH or result.get("artifact_fingerprint_reviewed") != HASH:
        errors.append("review artifact fingerprint must match controlling evidence")
    reviewer = result.get("reviewer", {})
    if reviewer.get("role") != "independent_extraction_reviewer" or not reviewer.get("independence_statement") or not reviewer.get("limitations"):
        errors.append("review result must record the independent procedure and disclosed limitations")
    if reviewer.get("independent_from_proposal") is not True:
        errors.append("review result must preserve its recorded independence assertion")
    if manifest.get("canonical_graph_write") is not False or result.get("canonical_graph_write") is not False:
        errors.append("review package may not mutate canonical graph data")
    if result.get("outcome") not in manifest.get("permitted_outcomes", []):
        errors.append("review outcome is outside manifest permitted outcomes")
    if result.get("outcome") != "supported_as_proposed":
        errors.append("committed extraction review outcome must remain supported_as_proposed")
    misleading = re.compile(r"acceptance[_ -]?ready|ready[_ -]?for[_ -]?acceptance|acceptance candidate", re.IGNORECASE)
    if misleading.search(json.dumps(result, ensure_ascii=False)):
        errors.append("extraction review must not classify a candidate as acceptance-ready")

    review_id = result.get("review_id")
    if eligibility.get("status") != "complete":
        errors.append("eligibility review must be complete")
    if eligibility.get("reviewed_candidate_id") != candidate_id:
        errors.append("eligibility must reference the exact candidate")
    if eligibility.get("extraction_review_id") != review_id:
        errors.append("eligibility must reference the exact extraction review")
    if eligibility.get("extraction_review_outcome") != result.get("outcome"):
        errors.append("eligibility must preserve the extraction review outcome")
    eligibility_dependencies = eligibility.get("dependency_fingerprints", {})
    expected_eligibility_dependencies = {
        "candidate": candidate_id,
        "representation": representation.get("record_id"),
        "path_relationship": candidate.get("relationship", {}).get("source_structure_dependency"),
        "applicability": applicability.get("record_id"),
        "extraction_review": result.get("review_id"),
    }
    if eligibility_dependencies != expected_eligibility_dependencies:
        errors.append("eligibility dependency fingerprints must match the exact baseline package")
    if applicability.get("status") == "unresolved_material" and eligibility.get("decision") != "ineligible":
        errors.append("unresolved material applicability requires ineligible")
    if eligibility.get("canonical_acceptance_allowed") is not False:
        errors.append("ineligible candidate cannot be canonically accepted")
    if eligibility.get("rejected") is not False:
        errors.append("ineligible is not rejected")
    if eligibility.get("performs_canonical_disposition") is not False:
        errors.append("eligibility may not perform canonical disposition")
    if eligibility.get("canonical_disposition") != "blocked_pending_approved_authority":
        errors.append("eligibility must leave canonical disposition blocked pending approved authority")
    if eligibility.get("canonical_graph_write") is not False or eligibility.get("canonical_data_changed") is not False:
        errors.append("eligibility may not mutate canonical graph data")

    active_v1 = candidate.get("relationship", {}).get("source_structure_dependency")
    active_relationship_ids = {item.get("relationship_id") for item in representation.get("relationships", [])}
    synthetic_relationship = synthetic.get("synthetic_relationship", {})
    synthetic_id = synthetic_relationship.get("relationship_id")
    if active_v1 != V1 or V1 not in active_relationship_ids:
        errors.append("committed baseline must bind candidate and representation to path relationship v1")
    if synthetic_id != V2 or synthetic_id == V1:
        errors.append("synthetic lifecycle v2 must be distinct from v1")
    if synthetic.get("test_only") is not True or synthetic.get("record_type") != "synthetic_lifecycle_test_input":
        errors.append("synthetic lifecycle relationship must be explicitly test-only")
    if synthetic.get("supersedes_relationship_id") != V1:
        errors.append("synthetic lifecycle relationship must explicitly supersede v1")
    if synthetic.get("factory_evidence") != "unchanged" or synthetic.get("factory_artifact_fingerprint") != HASH:
        errors.append("synthetic lifecycle transition must preserve factory evidence identity")
    if synthetic.get("meaning_changed") is not False or synthetic.get("source_occurrences_changed") is not False:
        errors.append("synthetic lifecycle transition may not invent source meaning")
    if synthetic.get("committed_active_representation_changed") is not False:
        errors.append("synthetic lifecycle test may not replace the committed active representation")

    transitions = lifecycle.get("transitions", [])
    sequence = [item.get("active_relationship") for item in transitions]
    if lifecycle.get("baseline_active_relationship") != V1 or sequence != [V1, V2, V1]:
        errors.append("lifecycle must record explicit baseline, isolated v2 activation, and v1 restoration")
    else:
        for index, transition in enumerate(transitions):
            derived = derive_dependency_states(candidate, result, eligibility, transition["active_relationship"])
            if transition.get("expected_states") != derived:
                errors.append(f"lifecycle transition {index} expected states disagree with derived dependency freshness")
    if lifecycle.get("test_input") != V2 or lifecycle.get("superseded_test_dependency") != V1:
        errors.append("lifecycle report must identify the exact isolated dependency transition")
    if lifecycle.get("factory_evidence_changed") is not False or lifecycle.get("canonical_data_changed") is not False:
        errors.append("lifecycle test must preserve factory and canonical data")
    if lifecycle.get("prior_versions_preserved") is not True or lifecycle.get("review_history_preserved") is not True:
        errors.append("lifecycle test must preserve prior versions and review history")
    if lifecycle.get("silent_retargeting_prevented") is not True:
        errors.append("lifecycle test must prevent silent retargeting")
    if lifecycle.get("active_artifacts_restored_after_test") is not True or lifecycle.get("restored_active_dependency") != V1:
        errors.append("lifecycle test must explicitly restore active dependency v1")
    baseline = derive_dependency_states(candidate, result, eligibility, V1)
    if set(baseline.values()) != {"fresh"}:
        errors.append("committed baseline candidate, review, and eligibility dependencies must be fresh")

    tracked = subprocess.run(["git", "ls-files", ".evidence"], cwd=ROOT, text=True, capture_output=True, check=False).stdout.strip()
    if tracked:
        errors.append("private evidence is tracked")
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
