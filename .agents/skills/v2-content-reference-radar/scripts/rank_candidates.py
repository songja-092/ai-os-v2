#!/usr/bin/env python3
"""Rank V2 content references without inventing unavailable social metrics."""

import argparse
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def parse_time(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (TypeError, ValueError):
        return None


def number(value):
    return float(value) if isinstance(value, (int, float)) and math.isfinite(value) and value >= 0 else None


def percentile(values, value):
    ordered = sorted(v for v in values if v is not None)
    if value is None or not ordered:
        return None
    if len(ordered) == 1:
        return 1.0
    return sum(candidate <= value for candidate in ordered) / len(ordered)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if not 1 <= args.limit <= 10:
        raise SystemExit("--limit must be 1..10")

    source = json.loads(Path(args.input).read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    seen = set()
    groups = defaultdict(list)
    for raw in source.get("items", []):
        url = raw.get("url")
        platform = raw.get("platform")
        if not url or not platform or url in seen:
            continue
        seen.add(url)
        published = parse_time(raw.get("published_at"))
        age_days = max((now - published).total_seconds() / 86400, 1.0) if published else None
        metrics = raw.get("metrics") or {}
        views, likes = number(metrics.get("views")), number(metrics.get("likes"))
        comments, reposts = number(metrics.get("comments")), number(metrics.get("reposts"))
        primary = views if views is not None else likes
        velocity = primary / age_days if primary is not None and age_days is not None else None
        item = dict(raw)
        item["_velocity"] = velocity
        item["_engagement"] = ((comments or 0) + (reposts or 0) * 2) / max(primary or 0, 1) if primary is not None else None
        groups[platform].append(item)

    ranked = []
    for platform, items in groups.items():
        velocities = [item["_velocity"] for item in items]
        engagements = [item["_engagement"] for item in items]
        for item in items:
            pv = percentile(velocities, item["_velocity"])
            pe = percentile(engagements, item["_engagement"])
            relevance = number(item.get("relevance"))
            if pv is None:
                score = None
                status = "NOT_PROVEN"
                basis = []
            else:
                reaction = pv * 0.8 + (pe or 0) * 0.2
                score = round((reaction * 0.7 + ((relevance / 100) if relevance is not None else 0.5) * 0.3) * 100)
                status = "RANKED_WITHIN_PLATFORM"
                basis = ["public_primary_metric_per_day", "public_engagement"]
                if relevance is not None:
                    basis.append("spec_relevance")
            item.pop("_velocity", None)
            item.pop("_engagement", None)
            item["ranking"] = {
                "score": score,
                "status": status,
                "scope": f"{platform}_items_only",
                "basis": basis,
                "warning": "플랫폼 내부 공개 수치 비교이며 콘텐츠 품질이나 성공을 보장하지 않음",
            }
            item["user_decision"] = None
        items.sort(key=lambda value: (value["ranking"]["score"] is not None, value["ranking"]["score"] or -1), reverse=True)
        ranked.extend(items[:4])

    ranked.sort(key=lambda value: (value["ranking"]["score"] is not None, value["ranking"]["score"] or -1), reverse=True)
    output = {
        "schema_version": "1.0",
        "request": source.get("request"),
        "ranking_policy": "within_platform_velocity_then_spec_relevance",
        "items": ranked[: args.limit],
        "allowed_decisions": ["adopt", "hold", "discard"],
        "final_decision_owner": "user",
        "automatic_product_application": False,
    }
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ranked", "items": len(output["items"]), "output": str(target)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
