#!/usr/bin/env python3
"""Compile and verify a traceable V2 reference-adoption recipe."""

from __future__ import annotations

import argparse
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path


ADOPTED = {"adopted", "adopted_design_direction", "adopted_with_adjustment"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_adopted(trial: dict) -> bool:
    if trial.get("status") in ADOPTED:
        return True
    decision = trial.get("user_decision")
    if isinstance(decision, dict):
        decision = decision.get("decision")
    return decision == "adopt"


class TraceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = {}

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        section = values.get("data-v2-section")
        if section:
            sources = values.get("data-v2-sources", "")
            self.sections[section] = {item.strip() for item in sources.split(",") if item.strip()}


def compile_recipe(selection_path: Path, output_path: Path) -> dict:
    selection = load_json(selection_path)
    base = selection_path.parent
    compiled_sources = []
    for source in selection["sources"]:
        trial_path = (base / source["trial_path"]).resolve()
        trial = load_json(trial_path)
        if not is_adopted(trial):
            raise SystemExit(f"BLOCKED: {source['source_id']} is not user-adopted")
        compiled_sources.append({
            **source,
            "trial_path": str(trial_path),
            "trial_sha256": sha256(trial_path),
            "trial_status": trial.get("status", "unknown"),
        })
    preview_path = (base / selection["preview_path"]).resolve()
    recipe = {
        "schema_version": "1.0",
        "recipe_id": "ondam-home-community-reference-adoption-v1",
        "project_id": selection["project_id"],
        "target_surface": selection["target_surface"],
        "version": 1,
        "status": "draft",
        "preview": {"path": str(preview_path), "sha256": sha256(preview_path)},
        "sources": compiled_sources,
        "rules": {
            "source_of_truth": "design_recipe",
            "user_approval_required_before_apply": True,
            "unselected_brand_assets_copy": False,
            "reference_trace_required": True
        }
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(recipe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return recipe


def verify(recipe_path: Path) -> dict:
    recipe = load_json(recipe_path)
    preview = Path(recipe["preview"]["path"])
    if sha256(preview) != recipe["preview"]["sha256"]:
        raise SystemExit("FAIL: preview hash differs from compiled recipe")
    parser = TraceParser()
    parser.feed(preview.read_text(encoding="utf-8"))
    failures = []
    for source in recipe["sources"]:
        for section in source["applied_section_ids"]:
            if section not in parser.sections:
                failures.append(f"missing section: {section}")
            elif source["source_id"] not in parser.sections[section]:
                failures.append(f"{section} missing source: {source['source_id']}")
    result = {
        "verdict": "PASS" if not failures else "FAIL",
        "recipe_id": recipe["recipe_id"],
        "verified_sources": len(recipe["sources"]),
        "verified_sections": sorted(parser.sections),
        "failures": failures,
        "limits": [
            "This verifies traceability and deterministic recipe compilation, not visual quality.",
            "Core automatic source selection and product application remain outside this pilot."
        ]
    }
    if failures:
        raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection", type=Path, nargs="?")
    parser.add_argument("--recipe", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if not args.verify_only:
        if args.selection is None:
            parser.error("selection is required unless --verify-only is used")
        compile_recipe(args.selection.resolve(), args.recipe.resolve())
    result = verify(args.recipe.resolve())
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
