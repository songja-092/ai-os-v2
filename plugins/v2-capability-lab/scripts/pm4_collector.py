#!/usr/bin/env python3
"""PM4 local-first research collector.

Searches approved/local V2 evidence before requesting bounded external research.
It never installs, activates, or adopts a capability.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.parse


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ROOTS = ("wiki", ".agents/skills", "plugins/v2-capability-lab/skills")
TEXT_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".txt"}
STOPWORDS = {
    "관련", "기존", "사용", "위한", "있는", "없는", "더", "및", "또는", "현재",
    "검증", "조사", "만드는", "만들기", "기능", "화면", "프로젝트", "v2", "ai",
}


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON object required: {path}")
    return value


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def tokens(text: str) -> set[str]:
    found = re.findall(r"[가-힣]{2,}|[a-zA-Z][a-zA-Z0-9_-]{2,}", text.lower())
    return {item for item in found if item not in STOPWORDS}


def iter_local_files(repo: Path, roots: list[str]):
    for relative_root in roots:
        root = (repo / relative_root).resolve()
        if repo not in root.parents and root != repo:
            raise ValueError(f"root escapes repository: {relative_root}")
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES and path.stat().st_size <= 1_000_000:
                yield path


def local_search(repo: Path, roots: list[str], request: str, limit: int) -> list[dict]:
    query = tokens(request)
    matches: list[dict] = []
    for path in iter_local_files(repo, roots):
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        path_tokens = tokens(str(path.relative_to(repo)))
        body_tokens = tokens(content[:200_000])
        overlap = query & (path_tokens | body_tokens)
        if not overlap:
            continue
        evidence_bonus = 2 if any(word in content.lower() for word in ("approved", "pass", "채택", "승인", "verified")) else 0
        score = len(overlap) + evidence_bonus
        title = next((line.lstrip("# ").strip() for line in content.splitlines() if line.strip().startswith("#")), path.stem)
        matches.append({
            "source_id": "local-" + hashlib.sha256(str(path.relative_to(repo)).encode()).hexdigest()[:12],
            "source_type": "local_v2_asset",
            "path": str(path.relative_to(repo)),
            "title": title[:140],
            "matched_terms": sorted(overlap),
            "score": score,
            "evidence_hint": "approved_or_verified_term_present" if evidence_bonus else "match_only_not_proven",
        })
    return sorted(matches, key=lambda item: (-item["score"], item["path"]))[:limit]


def canonical_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value.strip())
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"public http(s) URL required: {value}")
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(key, val) for key, val in query if not key.lower().startswith("utm_")]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip("/") or "/", urllib.parse.urlencode(sorted(query)), ""))


def normalize_sources(records: list[dict]) -> list[dict]:
    unique: dict[str, dict] = {}
    for item in records:
        url = canonical_url(str(item.get("url", "")))
        source_id = "web-" + hashlib.sha256(url.encode()).hexdigest()[:12]
        normalized = {
            "source_id": source_id,
            "url": url,
            "source_class": item.get("source_class", "secondary"),
            "title": item.get("title", url),
            "access_status": item.get("access_status", "not_checked"),
            "license_status": item.get("license_status", "unknown"),
            "retrieved_at": item.get("retrieved_at"),
            "used_part": item.get("used_part"),
            "adoption_status": "collected_not_adopted",
        }
        unique[source_id] = normalized
    return list(unique.values())


def external_queries(request: str, gaps: list[str]) -> list[str]:
    suffixes = ["공식 문서", "GitHub open source license", "검증 사례"]
    return [f"{request} {gap} {suffix}".strip() for gap, suffix in zip(gaps or ["자료"], suffixes)]


def cmd_run(args: argparse.Namespace) -> None:
    repo = Path(args.repo).resolve()
    request_file = Path(args.request_file).resolve()
    request = read_json(request_file)
    original = str(request.get("original_request", "")).strip()
    if not original:
        raise ValueError("original_request is required")
    roots = request.get("local_roots") or list(DEFAULT_ROOTS)
    if not isinstance(roots, list) or not all(isinstance(item, str) for item in roots):
        raise ValueError("local_roots must be a list of repository-relative paths")
    matches = local_search(repo, roots, original, args.limit)
    required_matches = int(request.get("minimum_local_matches", 3))
    required_terms = set(request.get("required_terms") or [])
    strong_matches = [item for item in matches if item["score"] >= 3]
    covered_terms = {term for item in strong_matches for term in item["matched_terms"]}
    required_terms_met = not required_terms or required_terms <= covered_terms
    sufficient = len(strong_matches) >= required_matches and required_terms_met
    gaps = list(request.get("research_gaps") or ([] if sufficient else ["구현 가능성", "유지관리", "라이선스"]))
    result = {
        "schema_version": "1.0",
        "run_at": now(),
        "request_id": request.get("request_id"),
        "original_request": original,
        "policy": "local_first_external_only_if_missing",
        "local_search": {
            "roots": roots,
            "match_count": len(matches),
            "strong_match_count": len(strong_matches),
            "minimum_required": required_matches,
            "required_terms": sorted(required_terms),
            "required_terms_met": required_terms_met,
            "matches": matches,
        },
        "coverage": "sufficient" if sufficient else ("partial" if matches else "insufficient"),
        "external_research_needed": not sufficient,
        "external_research": {
            "gaps": gaps,
            "queries": [] if sufficient else external_queries(original, gaps),
            "automatic_network_execution": False,
            "private_project_upload": False,
        },
        "decision": {
            "available_actions": ["adopt", "hold", "discard"],
            "current": None,
            "requires_user": True,
        },
        "side_effects": {"installed": False, "activated": False, "core_changed": False},
    }
    write_json(Path(args.output).resolve(), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_ingest(args: argparse.Namespace) -> None:
    source = read_json(Path(args.sources_file).resolve())
    records = source.get("sources")
    if not isinstance(records, list):
        raise ValueError("sources[] is required")
    output = {
        "schema_version": "1.0",
        "normalized_at": now(),
        "sources": normalize_sources(records),
        "automatic_adoption": False,
    }
    write_json(Path(args.output).resolve(), output)
    print(json.dumps(output, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="action", required=True)
    run = commands.add_parser("run")
    run.add_argument("--repo", default=str(REPO_ROOT))
    run.add_argument("--request-file", required=True)
    run.add_argument("--output", required=True)
    run.add_argument("--limit", type=int, default=8)
    run.set_defaults(func=cmd_run)
    ingest = commands.add_parser("ingest")
    ingest.add_argument("--sources-file", required=True)
    ingest.add_argument("--output", required=True)
    ingest.set_defaults(func=cmd_ingest)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
