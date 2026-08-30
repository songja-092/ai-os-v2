#!/usr/bin/env python3
"""Discover visual-reference seeds from a confirmed PM4 request.

The first provider is Behance public search. The adapter records discovery
evidence only; it does not copy a design or claim a reusable license.
"""

import argparse
import html
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


PROJECT_TERMS = {
    "electronic_business_card": [
        "digital vcard mobile app UI",
        "contact card mobile profile UI",
        "NFC digital business card mobile UI",
    ],
    "interior_community": ["interior design community website", "interior social platform", "home design community"],
}

PROJECT_ADJACENT_TERMS = {
    "electronic_business_card": [
        "professional mobile profile",
        "personal link page portfolio",
        "digital vcard profile",
        "contact profile landing page",
        "professional bio link page",
        "NFC profile page",
    ],
    "interior_community": [
        "interior inspiration social feed",
        "home renovation community",
        "interior creator profile",
        "room design sharing platform",
    ],
}

GENERIC_TRAITS = {"검색어와 연결된 시각 구성", "실제 프로젝트 Cover", "방향 비교 후보"}

PROJECT_TITLE_SIGNALS = {
    "electronic_business_card": {
        "positive": {"digital", "nfc", "mobile", "profile", "vcard", "app", "website", "web", "contact", "bio"},
        "negative": {"print", "printable", "stationery", "letterhead", "mockup", "template"},
    },
    "interior_community": {
        "positive": {"interior", "community", "social", "home", "room", "renovation", "platform", "app", "web"},
        "negative": {"print", "brochure", "catalog", "stationery"},
    },
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def request_text(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AI-OS-V2-PM4 visual research)"})
    with urllib.request.urlopen(request, timeout=25) as response:
        return response.read(2_000_000).decode("utf-8", errors="replace")


def request_terms(receipt, refill_round=0, preferred_traits=None, rejected_traits=None):
    explicit = receipt.get("reference_search_terms") or receipt.get("answers", {}).get("reference_search_terms")
    if explicit:
        base_terms = [str(value).strip() for value in explicit if str(value).strip()]
    else:
        project_type = receipt.get("project_type")
        if project_type in PROJECT_TERMS:
            base_terms = list(PROJECT_TERMS[project_type])
        else:
            original = re.sub(r"[^0-9A-Za-z가-힣 ]+", " ", receipt.get("original_request", "")).strip()
            if not original:
                raise ValueError("검색어를 만들 수 있는 요청 내용이 없습니다.")
            base_terms = [original + " web design", original + " mobile UI", original + " website"]

    if refill_round <= 0:
        return base_terms[:3]

    project_type = receipt.get("project_type")
    adjacent = PROJECT_ADJACENT_TERMS.get(project_type, [])
    start = ((refill_round - 1) * 3) % max(len(adjacent), 1)
    rotated = adjacent[start:] + adjacent[:start]
    preferred = [str(value).strip() for value in (preferred_traits or []) if str(value).strip()]
    rejected_tokens = {
        token.lower()
        for value in (rejected_traits or [])
        for token in re.findall(r"[0-9A-Za-z가-힣]+", str(value))
        if len(token) > 1
    }
    expanded = preferred[:2] + rotated + base_terms
    unique = []
    for term in expanded:
        normalized = term.strip()
        if not normalized or normalized in unique:
            continue
        if rejected_tokens and rejected_tokens.issuperset(
            token.lower() for token in re.findall(r"[0-9A-Za-z가-힣]+", normalized)
        ):
            continue
        unique.append(normalized)
    return unique[:5]


def behance_results(term):
    url = "https://www.behance.net/search/projects?" + urllib.parse.urlencode({"search": term})
    page = request_text(url)
    images = {}
    for tag in re.findall(r"<img\b[^>]+>", page, flags=re.I):
        src = re.search(r'\bsrc="(https://mir-s3-cdn-cf\.behance\.net/[^\"]+)"', tag)
        alt = re.search(r'\balt="([^\"]+)"', tag)
        if src and alt:
            images[html.unescape(alt.group(1)).strip()] = html.unescape(src.group(1))
    records = []
    for tag in re.findall(r"<a\b[^>]+>", page, flags=re.I):
        href = re.search(r'\bhref="((?:https://www\.behance\.net)?/gallery/[^\"]+)"', tag)
        title = re.search(r'\btitle="Link to project - ([^\"]+)"', tag)
        if not href or not title:
            continue
        name = html.unescape(title.group(1)).strip()
        image_url = images.get(name)
        if not image_url:
            continue
        source_url = html.unescape(href.group(1)).split("?", 1)[0]
        if source_url.startswith("/"):
            source_url = "https://www.behance.net" + source_url
        useful = {token for token in re.findall(r"[a-z0-9]+", term.lower()) if token not in {"design", "web", "website", "mobile"}}
        title_tokens = set(re.findall(r"[a-z0-9]+", name.lower()))
        score = len(useful & title_tokens)
        records.append({"title": name, "source_url": source_url, "image_url": image_url, "query": term, "search_url": url, "relevance_score": score})
    unique = {item["source_url"]: item for item in records}
    return sorted(unique.values(), key=lambda item: (-item["relevance_score"], item["title"]))


def project_relevance(item, project_type):
    """Keep a visual candidate only when its title exposes the requested surface intent."""
    title = item["title"].lower()
    if project_type == "electronic_business_card":
        if any(phrase in title for phrase in ("company profile", "print ready", "printable", "stationery", "letterhead")):
            return -1
        business_card_surface = "business card" in title and any(
            token in title for token in ("digital", "nfc", "mobile", "web", "site")
        )
        profile_surface = any(
            phrase in title for phrase in ("mobile profile", "digital profile", "vcard", "contact profile", "bio link")
        )
        if not (business_card_surface or profile_surface):
            return -1
        surface_bonus = 0
        if "ui/ux" in title or "application" in title:
            surface_bonus += 6
        if "app" in title:
            surface_bonus += 3
        if "case study" in title:
            surface_bonus += 2
        if "website" in title or "web-site" in title:
            surface_bonus -= 3
        if title.startswith("nfc digital business card - mobile app"):
            surface_bonus -= 20
        item["surface_bonus"] = surface_bonus
    signals = PROJECT_TITLE_SIGNALS.get(project_type)
    if not signals:
        return item["relevance_score"]
    title_tokens = set(re.findall(r"[a-z0-9]+", item["title"].lower()))
    positive = title_tokens & signals["positive"]
    negative = title_tokens & signals["negative"]
    if not positive or negative:
        return -1
    return item["relevance_score"] + len(positive) * 3 + item.get("surface_bonus", 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--regional-seed-file")
    parser.add_argument("--exclude-file")
    parser.add_argument("--refill-round", type=int, default=0)
    args = parser.parse_args()
    receipt = read_json(args.receipt)
    if not receipt.get("user_confirmed") or receipt.get("status") != "user_confirmed":
        raise SystemExit("확정된 인터뷰 명세가 필요합니다.")
    excluded_urls = set()
    preferred_traits = []
    rejected_traits = []
    if args.exclude_file:
        previous = read_json(args.exclude_file)
        if previous.get("request_id") != receipt["request_id"]:
            raise SystemExit("기존 Reference 상태와 인터뷰 명세가 일치하지 않습니다.")
        decisions = previous.get("decisions", {})
        for item in previous.get("items", []):
            excluded_urls.add(item.get("source_url"))
            decision = decisions.get(item.get("reference_id"))
            if decision == "adopt":
                preferred_traits.append(item.get("source_name", ""))
                preferred_traits.extend(trait for trait in item.get("traits", []) if trait not in GENERIC_TRAITS)
            elif decision == "discard":
                rejected_traits.extend(trait for trait in item.get("traits", []) if trait not in GENERIC_TRAITS)
                rejected_traits.append(item.get("source_name", ""))
    terms = request_terms(receipt, args.refill_round, preferred_traits, rejected_traits)
    found, failures = {}, []
    for term in terms:
        try:
            for item in behance_results(term):
                if item["source_url"] not in excluded_urls:
                    found[item["source_url"]] = item
        except Exception as exc:
            failures.append({"provider": "behance_public_search", "query": term, "reason": type(exc).__name__})
    for item in found.values():
        item["project_relevance_score"] = project_relevance(item, receipt.get("project_type"))
    ranked = sorted(found.values(), key=lambda item: (-item["project_relevance_score"], item["title"]))
    selected = [item for item in ranked if item["project_relevance_score"] >= 0][: args.limit]
    references = []
    for index, item in enumerate(selected, 1):
        references.append({
            "reference_id": (
                f"ref-refill-r{args.refill_round:02d}-{index:02d}"
                if args.refill_round > 0 else f"ref-discovered-{index:02d}"
            ),
            "source_name": item["title"],
            "source_url": item["source_url"],
            "image_url": item["image_url"],
            "source_type": "design_gallery",
            "region": "global",
            "natural_summary_ko": f"‘{item['query']}’ 검색에서 발견한 실제 공개 디자인 프로젝트입니다. 화면 방향 참고용이며 구현 가능성과 라이선스는 별도 확인이 필요합니다.",
            "traits": ["검색어와 연결된 시각 구성", "실제 프로젝트 Cover", "방향 비교 후보"],
            "do_not_copy": ["원본 브랜드", "원본 문구", "원본 이미지", "고유 레이아웃 전체"],
            "discovery_evidence": {"provider": "behance_public_search", "query": item["query"], "search_url": item["search_url"]},
        })
    if args.regional_seed_file:
        regional = read_json(args.regional_seed_file)
        if regional.get("request_id") != receipt["request_id"]:
            raise SystemExit("한국 공급원 목록과 인터뷰 명세가 일치하지 않습니다.")
        existing_urls = excluded_urls | {item["source_url"] for item in references}
        ordered_regional = sorted(
            regional.get("references", []),
            key=lambda item: (item.get("source_type") != "user_provided", item.get("region") != "korea"),
        )
        for item in ordered_regional:
            if item.get("source_url") in existing_urls:
                continue
            enriched = dict(item)
            enriched["discovery_evidence"] = {
                "provider": (
                    "user_provided_source" if item.get("source_type") == "user_provided"
                    else "registered_korean_actual_source" if item.get("region") == "korea"
                    else "registered_global_actual_source"
                ),
                "query": receipt.get("project_type"),
                "search_url": item["source_url"],
            }
            references.append(enriched)
            existing_urls.add(item["source_url"])
            if len(references) >= args.limit:
                break
    output = {
        "schema_version": "1.0",
        "request_id": receipt["request_id"],
        "discovery_mode": "request_terms_to_public_visual_gallery",
        "queries": terms,
        "refill_round": args.refill_round,
        "previous_decision_influence": {
            "adopted_traits": preferred_traits,
            "discarded_traits": rejected_traits,
            "excluded_url_count": len(excluded_urls),
        },
        "references": references,
        "source_failures": failures,
        "discovered_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "automatic_selection": False,
        "implementation_allowed": False,
        "limitations": [
            "현재 무료 Runtime 공급원은 Behance 공개 검색 한 곳입니다.",
            "한국 실제 서비스는 접근 확인된 등록 공급원을 요청 유형에 맞을 때만 보충합니다.",
            "검색 결과는 시각 방향 참고용이며 구현 가능성이나 재사용 라이선스를 증명하지 않습니다.",
            "검색어 생성은 확정된 인터뷰 명세와 명시된 Reference 검색어를 사용합니다.",
            "요청 화면을 제목에서 확인할 수 없는 인쇄물·일반 회사소개 후보는 사용자 Gallery 전에 제외합니다.",
        ],
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"request_id": receipt["request_id"], "queries": len(terms), "references": len(references), "failures": len(failures)}, ensure_ascii=False))
    return 0 if len(references) >= 5 else 2


if __name__ == "__main__":
    raise SystemExit(main())
