#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
from pathlib import Path

EXCLUDED_NAMES = {".git", ".env", ".ssh", "cookies", "tokens", "node_modules"}


def safe_files(root):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part.lower() in EXCLUDED_NAMES for part in path.parts):
            continue
        yield path


def digest(root, files):
    value = hashlib.sha256()
    for path in files:
        relative = path.relative_to(root).as_posix()
        value.update(relative.encode("utf-8"))
        value.update(str(path.stat().st_size).encode("ascii"))
    return value.hexdigest()


def inspect(args):
    root = Path(args.source).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit("source must be an existing directory")
    files = list(safe_files(root))
    suffixes = sorted({path.suffix.lower() for path in files if path.suffix})
    entry_candidates = [path.relative_to(root).as_posix() for path in files if path.name in {"index.html", "package.json"}]
    payload = {
        "packaging_version": "1.0",
        "status": "candidate_draft",
        "source": {
            "path": str(root),
            "file_count": len(files),
            "structure_sha256": digest(root, files),
            "excluded_sensitive_names": sorted(EXCLUDED_NAMES),
        },
        "project": {"project_id": args.project_id, "display_name": args.display_name},
        "detected": {"file_types": suffixes, "entry_candidates": entry_candidates},
        "features": [],
        "overlap": [],
        "verification": {"preview": "not_run", "interaction": "not_run", "isolation": "not_run", "restore": "not_run"},
        "decision": "candidate",
        "warning": "이 파일은 정적 분석 초안이며 기능 구현 또는 작동 증거가 아닙니다.",
    }
    output = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output, end="")


parser = argparse.ArgumentParser(description="Create a read-only V2 project packaging draft")
subparsers = parser.add_subparsers(dest="command", required=True)
inspect_parser = subparsers.add_parser("inspect")
inspect_parser.add_argument("source")
inspect_parser.add_argument("--project-id", required=True)
inspect_parser.add_argument("--display-name", required=True)
inspect_parser.add_argument("--output")
inspect_parser.set_defaults(handler=inspect)
arguments = parser.parse_args()
arguments.handler(arguments)
