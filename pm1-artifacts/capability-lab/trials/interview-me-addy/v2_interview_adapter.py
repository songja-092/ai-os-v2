#!/usr/bin/env python3
"""Project-blind contract test for the V2 Interview Me adapter."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def route(signals: set[str], policy: dict) -> str:
    if "user_stop" in signals:
        return "stop_without_implementation"
    if signals.intersection(policy["activation"]["skip_when"]):
        return "skip"
    if signals.intersection(policy["activation"]["run_when"]):
        return "interview"
    return "skip"


def receipt(case: dict, result: str) -> dict:
    status = {
        "skip": "not_required",
        "interview": "needs_user_answers",
        "stop_without_implementation": "stopped_unconfirmed",
    }[result]
    scope_lock_present = "scope_lock_present" in case["signals"]
    return {
        "packet_id": f"fixture-{case['id']}",
        "packet_version": 1,
        "project_id": "generated-fixture-project",
        "original_request": case["request"],
        "clarified_request": case["request"] if result == "skip" else None,
        "target_environment": "fixture-only" if result == "skip" else None,
        "build_scope": ["selected_text_style"] if result == "skip" else [],
        "preserve_scope": ["all_unselected_sections"] if result == "skip" else [],
        "excluded_scope": ["layout", "content", "behavior"] if result == "skip" else [],
        "acceptance_checks": ["selected H3 text is one approved size step smaller"] if result == "skip" else [],
        "constraints": ["existing scope lock required"],
        "unresolved_questions": [] if result == "skip" else ["outcome", "user", "success"],
        "risk_classification": "low" if result == "skip" else "unclassified",
        "why_now": None,
        "status": status,
        "scope_lock_present": scope_lock_present,
        "implementation_allowed": result == "skip" and scope_lock_present
    }


def validate_source(skill_text: str) -> dict:
    required = {
        "one_question_at_a_time": "one question at a time" in skill_text.lower(),
        "explicit_confirmation": "explicit yes" in skill_text.lower(),
        "out_of_scope": "out of scope" in skill_text.lower(),
        "no_premature_spec": "producing a spec, plan, or task list before" in skill_text.lower(),
        "clear_request_skip": "mechanical operations" in skill_text.lower(),
        "live_user_required": "live, responsive user" in skill_text.lower(),
    }
    return {"checks": required, "pass": all(required.values())}


def main() -> int:
    policy = load(ROOT / "v2-policy.json")
    cases = load(ROOT / "scenarios.json")["cases"]
    skill_path = ROOT / "isolated-install" / "interview-me" / "SKILL.md"
    source = validate_source(skill_path.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        actual = route(set(case["signals"]), policy)
        results.append({
            "id": case["id"],
            "expected": case["expected"],
            "actual": actual,
            "pass": actual == case["expected"],
            "receipt": receipt(case, actual),
        })
    required_pm5_fields = set(policy["output"]["fields"])
    schema_checks = [
        required_pm5_fields.issubset(item["receipt"].keys()) for item in results
    ]
    report = {
        "verdict": "PASS" if source["pass"] and all(item["pass"] for item in results) and all(schema_checks) else "FAIL",
        "source_contract": source,
        "pm5_schema_checks": schema_checks,
        "scenario_results": results,
        "limits": [
            "This proves deterministic routing and receipt boundaries, not LLM answer quality.",
            "The upstream skill has no hard question cap; V2 adds a three-question pause, not a forced completion.",
            "No Core or product write is performed."
        ]
    }
    (ROOT / "v2-adapter-verification.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
