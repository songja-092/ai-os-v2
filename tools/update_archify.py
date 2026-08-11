#!/usr/bin/env python3
"""Regenerate the local Archify artifact from committed V2 state."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


REPO_ROOT = Path(__file__).resolve().parents[1]
ARCHIFY_DIR = Path(
    os.environ.get("AI_OS_V2_ARCHIFY_DIR", "/home/user/바탕화면/ai_os_v2_archify")
)
SPEC_PATH = ARCHIFY_DIR / "ai-os-v2-current-ko.architecture.json"
HTML_PATH = ARCHIFY_DIR / "ai-os-v2-current-ko.html"
ARCHIFY_CLI = Path(
    os.environ.get(
        "ARCHIFY_CLI",
        "/home/user/.codex/skills/archify/bin/archify.mjs",
    )
)


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def committed_file(path: str) -> str:
    return run("git", "show", f"HEAD:{path}")


def next_steps(markdown: str) -> list[str]:
    lines = markdown.splitlines()
    collecting = False
    items: list[str] = []
    for line in lines:
        if line.strip() in {"## 다음 단계", "## 확정된 다음 단계"}:
            collecting = True
            continue
        if collecting and line.startswith("## "):
            break
        if collecting and line.startswith("- "):
            text = line[2:].strip().replace("`", "")
            items.append(text if len(text) <= 64 else f"{text[:61]}...")
    return items[:5]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    if not SPEC_PATH.exists():
        raise SystemExit(f"Archify specification not found: {SPEC_PATH}")
    if not ARCHIFY_CLI.exists():
        raise SystemExit(f"Archify CLI not found: {ARCHIFY_CLI}")

    revision = run("git", "rev-parse", "HEAD")
    branch = run("git", "branch", "--show-current") or "detached"
    milestones = json.loads(committed_file("state/milestones.json"))
    current_state = committed_file("wiki/CURRENT_STATE.md")
    completed = sum(item.get("status") == "completed" for item in milestones)

    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    spec["meta"]["repository"]["revision"] = revision
    spec["meta"]["subtitle"] = (
        f"Commit {revision[:7]} · {branch} · M1~M7 {completed}/{len(milestones)} 완료"
    )

    components = {item["id"]: item for item in spec["components"]}
    if "github" in components:
        components["github"]["sublabel"] = f"공식 기억 · 현재 기준 {revision[:7]}"
    if "archify" in components:
        components["archify"]["sublabel"] = f"Commit {revision[:7]}에서 자동 재생성"
        components["archify"]["tag"] = "자동 갱신"

    milestone_items = [
        f"{item['id']} · {item['name']} · {item['status']}" for item in milestones
    ]
    plan_items = next_steps(current_state) or ["확정된 다음 단계가 없습니다."]
    spec["cards"] = [
        {"dot": "emerald", "title": "M1~M7 진행 상태", "items": milestone_items},
        {"dot": "cyan", "title": "확정된 다음 단계", "items": plan_items},
    ]

    ARCHIFY_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=ARCHIFY_DIR, delete=False, suffix=".json"
    ) as handle:
        json.dump(spec, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        candidate = Path(handle.name)
    candidate.replace(SPEC_PATH)

    validate = run(
        "node",
        str(ARCHIFY_CLI),
        "validate",
        "architecture",
        str(SPEC_PATH),
        "--quality",
        "showcase",
        "--json",
        "--repo-root",
        str(REPO_ROOT),
    )
    receipt = run(
        "node",
        str(ARCHIFY_CLI),
        "deliver",
        "architecture",
        str(SPEC_PATH),
        str(HTML_PATH),
        "--quality",
        "showcase",
        "--json",
        "--repo-root",
        str(REPO_ROOT),
    )

    if not args.quiet:
        print(f"Archify Updated: {revision}")
        print(validate)
        print(receipt)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        if error.stdout:
            print(error.stdout, file=sys.stderr)
        if error.stderr:
            print(error.stderr, file=sys.stderr)
        raise SystemExit(error.returncode)
