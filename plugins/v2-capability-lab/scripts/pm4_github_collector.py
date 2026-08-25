#!/usr/bin/env python3
"""Collect recent, directly testable GitHub candidates for PM4."""
from __future__ import annotations
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import urllib.parse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
parser.add_argument("--limit", type=int, default=10)
args = parser.parse_args()

since = (datetime.now(timezone.utc) - timedelta(days=30)).date().isoformat()
queries = [f'"vibe coding" pushed:>={since}', f'codex claude pushed:>={since}', f'AI web design pushed:>={since}']
records = {}
for query in queries:
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({"q": query, "sort": "stars", "order": "desc", "per_page": 10})
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "AI-OS-V2-PM4/0.1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        payload = json.load(response)
    for item in payload.get("items", []):
        records[item["html_url"]] = {
            "platform": "github",
            "channel_name": item["owner"]["login"],
            "channel_url": item["owner"]["html_url"],
            "title": item["full_name"],
            "url": item["html_url"],
            "short_summary": item.get("description") or "설명 없음",
            "published_at": item.get("created_at"),
            "updated_at": item.get("pushed_at"),
            "public_metrics": {"stars": item.get("stargazers_count"), "forks": item.get("forks_count"), "open_issues": item.get("open_issues_count")},
            "license": (item.get("license") or {}).get("spdx_id"),
            "cost": "open_source_or_repository_specific",
            "project_ready_evidence": {"clone_url": item.get("clone_url"), "default_branch": item.get("default_branch")},
        }

items = sorted(records.values(), key=lambda item: item["public_metrics"]["stars"] or 0, reverse=True)[:args.limit]
result = {
    "schema_version": "1.0",
    "platform": "github",
    "collected_at": datetime.now(timezone.utc).isoformat(),
    "period_days": 30,
    "queries": queries,
    "role": "collection_only",
    "items": items,
    "adoption_decision": None,
}
output = Path(args.output).resolve()
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "collected", "items": len(items), "output": str(output)}, ensure_ascii=False))
