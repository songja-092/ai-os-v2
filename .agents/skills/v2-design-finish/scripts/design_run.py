#!/usr/bin/env python3
"""Initialize and validate a V2 design-finish artifact without external packages."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


DESIGN_GATES = [
    "information_priority",
    "spacing_consistency",
    "typography_hierarchy",
    "component_state_completeness",
    "border_and_surface_clarity",
    "responsive_quality",
    "motion_purpose",
    "reference_fidelity",
    "visual_target_fidelity",
    "user_task_completion",
    "user_visual_approval",
]

TECHNICAL_GATES = [
    "build_and_types",
    "rendered_route",
    "primary_interactions",
    "fatal_console_errors",
    "keyboard_focus",
    "contrast_and_names",
    "scope_preservation",
    "rollback_available",
]

ALLOWED_GATE_VALUES = {"pending", "pass", "fail", "not_required"}

UI_UX_PRO_PATHS = [
    Path("/home/user/바탕화면/test_project/.agents/skills/ui-ux-pro-max"),
    Path("/home/user/바탕화면/ai_os/.agents/skills/ui-ux-pro-max"),
]


def new_manifest(project_id: str, surface: str) -> dict[str, Any]:
    return {
        "artifact_version": "1.0",
        "project_id": project_id,
        "target_surface": surface,
        "status": "draft",
        "viewport": {
            "width": 1600 if surface == "v2_board" else 430,
            "height": 1000 if surface == "v2_board" else 932,
            "theme": "light",
            "motion_state": "initial",
        },
        "brief": {
            "purpose": "",
            "primary_task": "",
            "required_information": [],
            "untouched_areas": [],
            "prohibited_patterns": [],
        },
        "references": [],
        "tools": [],
        "implementation_candidates": [],
        "visual_target": {
            "image_path": "",
            "sha256": "",
            "prompt_record": "",
            "user_approved": False,
        },
        "changes": [],
        "verification": {
            "design": {name: "pending" for name in DESIGN_GATES},
            "technical": {name: "pending" for name in TECHNICAL_GATES},
        },
    }


def init_manifest(args: argparse.Namespace) -> int:
    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "design-finish-manifest.json"
    if destination.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing manifest: {destination}")
    destination.write_text(
        json.dumps(new_manifest(args.project_id, args.surface), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(destination)
    return 0


def check_manifest(args: argparse.Namespace) -> int:
    path = Path(args.manifest).expanduser().resolve()
    data = json.loads(path.read_text(encoding="utf-8"))
    problems: list[str] = []

    for key in ("artifact_version", "project_id", "target_surface", "status", "viewport", "brief", "tools", "visual_target", "verification"):
        if key not in data:
            problems.append(f"missing field: {key}")

    surface = data.get("target_surface")
    if surface not in {"v2_board", "customer_product"}:
        problems.append("target_surface must be v2_board or customer_product")

    verification = data.get("verification", {})
    for group, names in (("design", DESIGN_GATES), ("technical", TECHNICAL_GATES)):
        values = verification.get(group, {})
        for name in names:
            value = values.get(name)
            if value not in ALLOWED_GATE_VALUES:
                problems.append(f"verification.{group}.{name} has invalid or missing value")

    approved = bool(data.get("visual_target", {}).get("user_approved"))
    status = data.get("status")
    if status in {"approved", "implemented", "verified"} and not approved:
        problems.append("approved/implemented/verified status requires visual_target.user_approved=true")

    if status == "verified":
        for group in ("design", "technical"):
            pending = [key for key, value in verification.get(group, {}).items() if value not in {"pass", "not_required"}]
            if pending:
                problems.append(f"verified status has incomplete {group} gates: {', '.join(pending)}")

    result = {"manifest": str(path), "valid": not problems, "problems": problems}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not problems else 1


def doctor_environment(args: argparse.Namespace) -> int:
    repo = Path(args.repo).expanduser().resolve()
    required = {
        "python3": shutil.which("python3") is not None,
        "v2_repo": (repo / "AGENTS.md").is_file(),
        "pm1_brief": (repo / "wiki" / "PM1_REFERENCE_BRIEF.md").is_file(),
        "artifact_root": (repo / "pm1-artifacts").is_dir(),
        "ui_ux_pro_max": any((path / "SKILL.md").is_file() for path in UI_UX_PRO_PATHS),
        "image_output_root": Path("/home/user/바탕화면/v2_ui_images").is_dir(),
    }
    optional = {
        "node": shutil.which("node") is not None,
        "npm": shutil.which("npm") is not None,
        "dembrandt": shutil.which("dembrandt") is not None,
    }
    result = {
        "repo": str(repo),
        "required": required,
        "optional": optional,
        "ready": all(required.values()),
        "note": "Optional tools are not PM1 blockers and must not be auto-installed.",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ready"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create a non-overwriting design artifact manifest")
    init.add_argument("--output", required=True)
    init.add_argument("--project-id", required=True)
    init.add_argument("--surface", choices=("v2_board", "customer_product"), required=True)
    init.add_argument("--force", action="store_true", help="explicitly replace an existing manifest")
    init.set_defaults(func=init_manifest)

    check = sub.add_parser("check", help="validate a design artifact manifest")
    check.add_argument("manifest")
    check.set_defaults(func=check_manifest)

    doctor = sub.add_parser("doctor", help="check the local design-finish environment without installing tools")
    doctor.add_argument("--repo", required=True)
    doctor.set_defaults(func=doctor_environment)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
