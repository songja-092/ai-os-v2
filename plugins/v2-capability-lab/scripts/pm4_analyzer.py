#!/usr/bin/env python3
"""Summarize collected PM4 facts and ask the user whether to continue."""

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
        strong = [item for item in matches if item.get("score", 0) >= 3]
        covered = sorted({term for item in matches for term in item.get("matched_terms", [])})
        summaries = [
            {
                "source_id": item["source_id"],
                "title": item["title"],
                "link": item.get("url") or item.get("path"),
                "short_summary": f"{', '.join(item.get('matched_terms', [])[:5])} 관련 자료",
                "source_type": item["source_type"],
            }
            for item in matches
        ]
        result = {
            "schema_version": "1.0",
            "request_id": request.get("request_id"),
            "role": "fact_summary_not_sufficiency_not_adoption",
            "facts": {
                "collected_count": len(matches),
                "strong_match_count": len(strong),
                "covered_terms": covered,
            },
            "results": summaries,
            "sufficiency_judgment": None,
            "recommendation": None,
            "adoption_decision": None,
            "user_review": {
                "question": "현재 수집된 자료와 짧은 요약을 확인했습니다. 이 정도면 충분한가요?",
                "choices": ["자료 더 찾기", "이 정도면 충분", "조사 방향 수정"],
                "decision": None,
            },
            "next_owner": "user",
        }
        Path(args.output).resolve().write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
