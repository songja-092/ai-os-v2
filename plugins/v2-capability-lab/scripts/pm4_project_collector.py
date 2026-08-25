#!/usr/bin/env python3
"""Collect open-source project references from GitHub using a confirmed PM4 receipt."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request


API = "https://api.github.com"
ALLOWED_LICENSES = {"MIT", "Apache-2.0", "AGPL-3.0", "GPL-3.0"}
REQUIRED_TERMS = ("business card", "digital card", "vcard", "名片", "전자명함")


def request_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "AI-OS-V2-PM4/1.0 (personal research)",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request, timeout=8) as response:
        return json.load(response)


def request_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-OS-V2-PM4/1.0 (personal research)"})
    with urllib.request.urlopen(request, timeout=8) as response:
        return response.read(300_000).decode("utf-8", errors="replace")


def detected_license(repo: dict) -> tuple[str | None, str]:
    api_value = (repo.get("license") or {}).get("spdx_id")
    if api_value in ALLOWED_LICENSES:
        return api_value, "github_repository_metadata"
    full_name = repo["full_name"]
    branch = repo.get("default_branch") or "main"
    for filename in ("LICENSE", "LICENSE.md", "LICENSE.txt"):
        try:
            content = request_text(f"https://raw.githubusercontent.com/{full_name}/{branch}/{filename}").lower()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            continue
        if "gnu affero general public license" in content:
            return "AGPL-3.0", f"repository_file:{filename}"
        if "apache license" in content and "version 2.0" in content:
            return "Apache-2.0", f"repository_file:{filename}"
        if "mit license" in content:
            return "MIT", f"repository_file:{filename}"
        if "gnu general public license" in content and "version 3" in content:
            return "GPL-3.0", f"repository_file:{filename}"
    return None, "not_verified"


def capabilities(text: str) -> list[str]:
    checks = {
        "qr": ("qr", "qrcode"),
        "vcard_contact_save": ("vcard", ".vcf", "save contact"),
        "call_or_message_links": ("tel:", "sms:", "whatsapp", "social"),
        "theme_customization": ("theme", "template", "customiz", "design token"),
        "privacy_or_local_processing": ("privacy", "no tracking", "browser", "self-host"),
        "pwa_or_offline": ("pwa", "offline", "progressive web app"),
        "team_or_crm": ("team", "crm", "analytics", "admin"),
    }
    lower = text.lower()
    return [name for name, terms in checks.items() if any(term in lower for term in terms)]


def archetype(caps: list[str]) -> str:
    if "team_or_crm" in caps:
        return "team_or_management"
    if "pwa_or_offline" in caps:
        return "installable_self_hosted"
    if "privacy_or_local_processing" in caps:
        return "privacy_first_static"
    if "theme_customization" in caps:
        return "visual_customization"
    return "simple_contact_card"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--seed-file")
    parser.add_argument("--output", required=True)
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    if receipt.get("status") != "user_confirmed" or not receipt.get("user_confirmed"):
        raise SystemExit("confirmed PM4 interview receipt required")
    if receipt.get("project_type") != "electronic_business_card":
        raise SystemExit("this MVP adapter only supports electronic_business_card")

    queries = [
        'topic:digital-business-card',
        '"digital business card" QR vCard license:mit',
        '电子名片 QR CRM license:mit',
    ]
    if args.seed_file:
        queries = queries[:1]
    repos: dict[str, dict] = {}
    failures: list[dict] = []
    for query in queries:
        url = API + "/search/repositories?" + urllib.parse.urlencode(
            {"q": query, "sort": "stars", "order": "desc", "per_page": 20}
        )
        try:
            data = request_json(url)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            failures.append({"source": "github", "query": query, "error": type(exc).__name__})
            continue
        for repo in data.get("items", []):
            license_id = (repo.get("license") or {}).get("spdx_id")
            haystack = " ".join(
                [repo.get("name") or "", repo.get("description") or "", " ".join(repo.get("topics") or [])]
            ).lower()
            if license_id not in ALLOWED_LICENSES or not any(term in haystack for term in REQUIRED_TERMS):
                continue
            repos[repo["html_url"]] = repo

    if args.seed_file:
        seed_data = json.loads(Path(args.seed_file).read_text(encoding="utf-8"))
        if seed_data.get("request_id") != receipt["request_id"]:
            raise SystemExit("discovery seed request does not match receipt")
        for full_name in seed_data.get("repositories", []):
            try:
                repo = request_json(API + "/repos/" + urllib.parse.quote(full_name, safe="/"))
                repos[repo["html_url"]] = repo
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                failures.append({"source": "github", "repository": full_name, "error": type(exc).__name__})

    candidates = []
    for repo in repos.values():
        description = repo.get("description") or ""
        readme = ""
        try:
            readme = request_text(
                f"https://raw.githubusercontent.com/{repo['full_name']}/{repo.get('default_branch') or 'main'}/README.md"
            )
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            pass
        license_id, license_evidence = detected_license(repo)
        if license_id not in ALLOWED_LICENSES:
            continue
        caps = capabilities(" ".join([repo.get("name") or "", description, " ".join(repo.get("topics") or []), readme]))
        if "qr" not in caps and "vcard_contact_save" not in caps:
            continue
        candidates.append(
            {
                "candidate_id": "project-" + hashlib.sha256(repo["html_url"].encode()).hexdigest()[:12],
                "name": repo["full_name"],
                "url": repo["html_url"],
                "preview_url": repo.get("homepage") or None,
                "description": description,
                "license": license_id,
                "license_evidence": license_evidence,
                "stars": repo.get("stargazers_count", 0),
                "updated_at": repo.get("updated_at"),
                "capabilities": caps,
                "direction": archetype(caps),
                "selection_reason": "전자명함·QR 또는 연락처 저장 근거와 공개 라이선스가 확인된 저장소",
                "source_region": "asia" if any(x in (repo.get("language") or "").lower() for x in ("vue",)) and "名片" in description else "global",
                "adoption_status": "candidate_not_adopted",
            }
        )
    candidates.sort(key=lambda item: (-len(item["capabilities"]), -item["stars"], item["name"]))
    selected: list[dict] = []
    used_directions: set[str] = set()
    for item in candidates:
        if item["direction"] in used_directions:
            continue
        selected.append(item)
        used_directions.add(item["direction"])
        if len(selected) == args.limit:
            break
    if len(selected) < args.limit:
        for item in candidates:
            if item in selected:
                continue
            selected.append(item)
            if len(selected) == args.limit:
                break

    output = {
        "schema_version": "1.0",
        "request_id": receipt["request_id"],
        "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": "spec_based_project_collection",
        "source": "github_public_api",
        "queries": queries,
        "deduplicated_repository_count": len(repos),
        "eligible_candidate_count": len(candidates),
        "source_failures": failures,
        "items": selected,
        "user_decisions": {},
        "product_changed": False,
        "installation_performed": False,
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "collected", "items": len(selected), "failures": len(failures)}, ensure_ascii=False))
    return 0 if len(selected) == args.limit else 2


if __name__ == "__main__":
    raise SystemExit(main())
