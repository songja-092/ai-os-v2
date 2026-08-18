#!/usr/bin/env python3
"""Collect public design capabilities and present a three-action review queue."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PLUGIN_ROOT.parents[1]
DEFAULT_ROOT = REPO_ROOT / "pm1-artifacts" / "design-intelligence"
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
CATALOG = [
    {
        "id": "shadcn-ui",
        "repo": "shadcn-ui/ui",
        "role": "verified_component_and_block_registry",
        "category": "implementation-block",
        "reason": "Official Registry supports view, dry-run, diff, schema validation and Commit pinning.",
    },
    {
        "id": "kokonut-ui",
        "repo": "kokonut-labs/kokonutui",
        "role": "animated_shadcn_component_reference",
        "category": "visual-and-motion-block",
        "reason": "Public shadcn registry with Motion-based components and an MIT license.",
    },
    {
        "id": "impeccable",
        "repo": "pbakaus/impeccable",
        "role": "design_finish_second_opinion",
        "category": "design-skill",
        "reason": "Bounded critique and finish playbooks plus deterministic anti-pattern checks.",
    },
    {
        "id": "taste-skill-v1",
        "repo": "Leonxlnx/taste-skill",
        "role": "design_variance_and_anti_slop_candidate",
        "category": "design-skill",
        "reason": "Stable v1 is preserved while v2 remains experimental; requires isolated comparison.",
    },
    {
        "id": "stitch-skills",
        "repo": "google-labs-code/stitch-skills",
        "role": "stitch_design_workflow_candidate",
        "category": "external-design-workflow",
        "reason": "Large public skill suite, but it depends on the external Stitch workflow.",
    },
    {
        "id": "motion",
        "repo": "motiondivision/motion",
        "role": "react_motion_engine",
        "category": "animation-engine",
        "reason": "Production-oriented React and JavaScript motion library with extensive examples.",
    },
    {
        "id": "auto-animate",
        "repo": "formkit/auto-animate",
        "role": "low_configuration_reorder_animation",
        "category": "animation-engine",
        "reason": "Small-purpose animation candidate for add, remove and reorder transitions.",
    },
    {
        "id": "storybook",
        "repo": "storybookjs/storybook",
        "role": "component_state_catalog_and_test_workshop",
        "category": "verification-environment",
        "reason": "Established isolated component development and test environment.",
    },
]


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def github_json(path: str) -> dict:
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "ai-os-v2-design-intelligence/0.1"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.load(response)


def freshness(pushed_at: str | None) -> str:
    if not pushed_at:
        return "unknown"
    pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    age = (dt.datetime.now(dt.timezone.utc) - pushed).days
    if age <= 365:
        return "active_within_1y"
    if age <= 730:
        return "quiet_1_to_2y"
    return "stale_over_2y"


def enrich(item: dict) -> dict:
    result = dict(item)
    result.update({
        "url": f"https://github.com/{item['repo']}",
        "checked_at": now(),
        "status": "candidate",
        "decision": None,
        "actions": ["adopt", "hold", "discard"],
    })
    try:
        metadata = github_json(f"/repos/{item['repo']}")
        result.update({
            "stars": metadata.get("stargazers_count"),
            "archived": metadata.get("archived"),
            "pushed_at": metadata.get("pushed_at"),
            "freshness": freshness(metadata.get("pushed_at")),
            "license": (metadata.get("license") or {}).get("spdx_id") or "unknown",
            "default_branch": metadata.get("default_branch"),
        })
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        result.update({"metadata_error": str(exc), "freshness": "unknown", "license": "unknown"})
    return result


def cmd_collect(args: argparse.Namespace) -> None:
    root = Path(args.root).resolve()
    collection_id = args.collection_id
    if not ID_RE.fullmatch(collection_id):
        raise ValueError("collection id must be lower-case kebab-case")
    selected = [item for item in CATALOG if args.category == "all" or item["category"] == args.category]
    candidates = [enrich(item) for item in selected]
    record = {
        "schema_version": "1.0",
        "collection_id": collection_id,
        "created_at": now(),
        "source_policy": "public_only_no_private_project_input",
        "category": args.category,
        "candidate_count": len(candidates),
        "candidates": candidates,
        "user_actions": ["adopt", "hold", "discard"],
        "automatic_install": False,
        "note": "Adopt selects a candidate for isolated trial; it does not activate it in Core.",
    }
    path = root / "collections" / collection_id / "collection.json"
    if path.exists() and not args.refresh:
        raise FileExistsError(f"collection exists; use --refresh: {path}")
    write_json(path, record)
    print(json.dumps({
        "collection_id": collection_id,
        "path": str(path),
        "candidates": [
            {k: c.get(k) for k in ("id", "role", "stars", "freshness", "license", "url", "actions")}
            for c in candidates
        ],
    }, ensure_ascii=False, indent=2))


def cmd_decide(args: argparse.Namespace) -> None:
    if not args.approved_by_user:
        raise PermissionError("a user decision requires --approved-by-user")
    root = Path(args.root).resolve()
    path = root / "collections" / args.collection_id / "collection.json"
    if not path.exists():
        raise FileNotFoundError(path)
    record = read_json(path)
    candidate = next((c for c in record["candidates"] if c["id"] == args.candidate_id), None)
    if not candidate:
        raise ValueError("candidate not found")
    candidate["decision"] = args.decision
    candidate["decided_at"] = now()
    if args.decision == "adopt":
        candidate["status"] = "selected_for_isolated_trial"
        candidate["next_action"] = f"capability_lab.py prepare --id {candidate['id']} --source {candidate['url']}"
    elif args.decision == "hold":
        candidate["status"] = "held"
        candidate["next_action"] = "none"
    else:
        candidate["status"] = "discarded_from_collection"
        candidate["next_action"] = "none"
    write_json(path, record)
    print(json.dumps({k: candidate.get(k) for k in ("id", "decision", "status", "next_action")}, ensure_ascii=False, indent=2))


def cmd_review(args: argparse.Namespace) -> None:
    path = Path(args.root).resolve() / "collections" / args.collection_id / "collection.json"
    record = read_json(path)
    print(json.dumps({
        "collection_id": record["collection_id"],
        "decision_needed": [
            {k: c.get(k) for k in ("id", "role", "reason", "stars", "freshness", "license", "url", "status", "actions")}
            for c in record["candidates"] if c.get("decision") is None
        ],
    }, ensure_ascii=False, indent=2))


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    root.add_argument("--root", default=str(DEFAULT_ROOT))
    commands = root.add_subparsers(dest="action", required=True)
    collect = commands.add_parser("collect")
    collect.add_argument("--collection-id", required=True)
    collect.add_argument("--category", choices=("all", "implementation-block", "visual-and-motion-block", "design-skill", "external-design-workflow", "animation-engine", "verification-environment"), default="all")
    collect.add_argument("--refresh", action="store_true")
    collect.set_defaults(func=cmd_collect)
    decide = commands.add_parser("decide")
    decide.add_argument("--collection-id", required=True)
    decide.add_argument("--candidate-id", required=True)
    decide.add_argument("--decision", choices=("adopt", "hold", "discard"), required=True)
    decide.add_argument("--approved-by-user", action="store_true")
    decide.set_defaults(func=cmd_decide)
    review = commands.add_parser("review")
    review.add_argument("--collection-id", required=True)
    review.set_defaults(func=cmd_review)
    return root


def main() -> int:
    args = parser().parse_args()
    try:
        args.func(args)
        return 0
    except (ValueError, PermissionError, FileNotFoundError, FileExistsError, urllib.error.URLError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
