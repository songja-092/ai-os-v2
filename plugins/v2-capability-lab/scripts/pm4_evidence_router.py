#!/usr/bin/env python3
"""Route one PM4 topic to existing evidence adapters and merge their artifacts.

This is a thin dispatcher. It does not crawl, install, adopt, or apply anything.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


LANE_LABELS = {
    "visual_reference": "화면과 표현 방식",
    "real_usage": "사람들이 실제로 쓰는 방식과 반응",
    "implementation_material": "실제로 만들 수 있는 코드와 도구",
    "official_fact": "공식 기능과 제한 확인",
}


def classify(topic: str, goal: str) -> list[str]:
    text = f"{topic} {goal}".lower()
    lanes: list[str] = []
    if any(term in text for term in ("디자인", "ui", "ux", "웹", "화면", "reference", "래퍼런스", "이미지")):
        lanes.append("visual_reference")
    if any(term in text for term in ("사례", "활용", "사용", "반응", "reference", "래퍼런스", "바이브")):
        lanes.append("real_usage")
    if any(term in text for term in ("코딩", "개발", "구현", "도구", "앱", "웹", "v2")):
        lanes.append("implementation_material")
    if any(term in text for term in ("ai", "코딩", "도구", "업데이트", "기능", "구현")):
        lanes.append("official_fact")
    return list(dict.fromkeys(lanes or ["real_usage", "official_fact"]))


def extract_items(payload: dict) -> list[dict]:
    if isinstance(payload.get("items"), list):
        return payload["items"]
    if isinstance(payload.get("sample_candidates"), list):
        return payload["sample_candidates"]
    return []


def normalize(item: dict, source: dict, lane: str) -> dict | None:
    url = item.get("url")
    if not url:
        return None
    title = item.get("title") or item.get("summary_ko") or item.get("short_summary") or "제목 확인 필요"
    summary = item.get("summary_ko") or item.get("short_summary") or item.get("public_text") or title
    reference_use = item.get("reference_use")
    if reference_use and reference_use not in str(summary):
        summary = f"{summary} 참고할 부분은 {reference_use}입니다."
    summary = str(summary).strip()[:500]
    has_korean = bool(re.search(r"[가-힣]", summary))
    explains_more_than_title = summary != str(title).strip() and len(summary) >= 28
    review_ready = has_korean and explains_more_than_title
    return {
        "candidate_id": hashlib.sha256(url.encode("utf-8")).hexdigest()[:16],
        "evidence_type": lane,
        "evidence_label_ko": LANE_LABELS[lane],
        "platform": source["platform"],
        "title": str(title).strip(),
        "summary_ko": summary,
        "review_ready": review_ready,
        "review_issue": None if review_ready else "한국어로 내용과 참고 이유를 충분히 설명하지 못함",
        "url": url,
        "author_or_channel": item.get("author") or item.get("channel_name"),
        "published_at": item.get("published_at") or item.get("updated_at"),
        "source_artifact": source["artifact"],
        "user_decision": None,
    }


def diversify_by_platform(items: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = {}
    for item in items:
        groups.setdefault(item["platform"], []).append(item)
    diversified = []
    while any(groups.values()):
        for platform in list(groups):
            if groups[platform]:
                diversified.append(groups[platform].pop(0))
    return diversified


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--request", required=True)
    parser.add_argument("--sources", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    request_path = Path(args.request).resolve()
    sources_path = Path(args.sources).resolve()
    request = json.loads(request_path.read_text(encoding="utf-8"))
    source_manifest = json.loads(sources_path.read_text(encoding="utf-8"))
    topic = str(request.get("topic") or "").strip()
    goal = str(request.get("goal") or "").strip()
    if not topic:
        raise SystemExit("request.topic is required")

    lanes = classify(topic, goal)
    route_status = []
    candidates_by_lane: dict[str, list[dict]] = {lane: [] for lane in lanes}
    for source in source_manifest.get("sources", []):
        relevant_lanes = [lane for lane in source.get("evidence_types", []) if lane in lanes]
        if not relevant_lanes:
            continue
        artifact = (sources_path.parent / source["artifact"]).resolve()
        if not artifact.exists():
            route_status.append({"adapter": source["adapter"], "status": "NOT_PROVEN", "reason": "artifact_missing", "evidence_types": relevant_lanes})
            continue
        payload = json.loads(artifact.read_text(encoding="utf-8"))
        items = extract_items(payload)
        status = "EXECUTED" if items else "NOT_PROVEN"
        route_status.append({"adapter": source["adapter"], "status": status, "artifact": source["artifact"], "item_count": len(items), "evidence_types": relevant_lanes})
        for lane in relevant_lanes:
            for item in items:
                normalized = normalize(item, source, lane)
                if normalized:
                    candidates_by_lane[lane].append(normalized)

    for lane in lanes:
        candidates_by_lane[lane] = diversify_by_platform(candidates_by_lane[lane])

    # Give each proven evidence lane one candidate before filling remaining slots.
    selected = []
    seen = set()
    for lane in lanes:
        while candidates_by_lane[lane] and candidates_by_lane[lane][0]["url"] in seen:
            candidates_by_lane[lane].pop(0)
        if candidates_by_lane[lane]:
            item = candidates_by_lane[lane].pop(0)
            selected.append(item)
            seen.add(item["url"])
    while len(selected) < args.limit and any(candidates_by_lane.values()):
        progressed = False
        for lane in lanes:
            while candidates_by_lane[lane] and candidates_by_lane[lane][0]["url"] in seen:
                candidates_by_lane[lane].pop(0)
            if not candidates_by_lane[lane]:
                continue
            item = candidates_by_lane[lane].pop(0)
            selected.append(item)
            seen.add(item["url"])
            progressed = True
            if len(selected) >= args.limit:
                break
        if not progressed:
            break

    proven_lanes = sorted({item["evidence_type"] for item in selected})
    missing_lanes = [lane for lane in lanes if lane not in proven_lanes]
    result = {
        "schema_version": "1.0",
        "runtime_scope": "single_topic_limited_runtime",
        "request": request,
        "classified_evidence_types": [{"id": lane, "label_ko": LANE_LABELS[lane]} for lane in lanes],
        "freshness_policy": {
            "fast_moving_default_days": 30,
            "fallback_order": ["platform_expansion", "adjacent_query", "older_reference_with_explicit_label"],
            "automatic_one_year_expansion": False,
        },
        "routes": route_status,
        "items": selected,
        "proven_evidence_types": proven_lanes,
        "missing_evidence_types": missing_lanes,
        "automatic_adoption": False,
        "automatic_product_application": False,
        "user_decision": None,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS_WITH_MISSING_EVIDENCE" if missing_lanes else "PASS", "items": len(selected), "proven_evidence_types": proven_lanes, "missing_evidence_types": missing_lanes}, ensure_ascii=False))


if __name__ == "__main__":
    main()
