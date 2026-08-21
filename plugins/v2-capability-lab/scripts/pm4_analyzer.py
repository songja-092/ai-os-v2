#!/usr/bin/env python3
"""Analyze collected PM4 facts without selecting or adopting a candidate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request-file", required=True)
    parser.add_argument("--collection-file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        request = json.loads(Path(args.request_file).resolve().read_text(encoding="utf-8"))
        collection = json.loads(Path(args.collection_file).resolve().read_text(encoding="utf-8"))
        matches = collection.get("local_collection", {}).get("items", [])
        minimum = int(request.get("minimum_local_matches", 3))
        required_terms = set(request.get("required_terms") or [])
        strong = [item for item in matches if item.get("score", 0) >= 3]
        covered = {term for item in strong for term in item.get("matched_terms", [])}
        required_met = not required_terms or required_terms <= covered
        sufficient = len(strong) >= minimum and required_met
        gaps = list(request.get("research_gaps") or ([] if sufficient else ["구현 가능성", "유지관리", "라이선스"]))
        original = request["original_request"]
        queries = [] if sufficient else [f"{original} {gap}" for gap in gaps]
        result = {
            "schema_version": "1.0",
            "request_id": request.get("request_id"),
            "role": "fact_analysis_not_collection_not_adoption",
            "coverage": "sufficient" if sufficient else ("partial" if matches else "insufficient"),
            "facts": {
                "collected_count": len(matches),
                "strong_match_count": len(strong),
                "minimum_required": minimum,
                "required_terms": sorted(required_terms),
                "required_terms_met": required_met,
            },
            "external_research_needed": not sufficient,
            "research_gaps": gaps,
            "external_queries": queries,
            "recommendation": None,
            "adoption_decision": None,
            "next_owner": "collector" if not sufficient else "v2_ai_or_director",
        }
        Path(args.output).resolve().write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
