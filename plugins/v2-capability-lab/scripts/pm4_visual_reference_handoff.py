#!/usr/bin/env python3
"""Create a non-executing handoff from user-adopted visual references."""

import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json_atomic(path, payload):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as target:
        json.dump(payload, target, ensure_ascii=False, indent=2)
        target.write("\n")
        temp_path = target.name
    os.replace(temp_path, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--approved-at", required=True)
    args = parser.parse_args()

    state_path = Path(args.state)
    state = read_json(state_path)
    decisions = state.get("decisions", {})
    adopted = [item for item in state.get("items", []) if decisions.get(item.get("reference_id")) == "adopt"]
    if not adopted:
        raise SystemExit("사용자가 채택한 시각 Reference가 없습니다.")
    selected = []
    for item in adopted:
        selected.append({
            "reference_id": item["reference_id"],
            "source_name": item["source_name"],
            "source_url": item["source_url"],
            "region": item["region"],
            "source_type": item["source_type"],
            "traits": item["traits"],
            "do_not_copy": item["do_not_copy"],
            "local_image_path": item["local_image_path"],
            "sha256": item["sha256"],
        })
    payload = {
        "schema_version": "1.0",
        "request_id": state["request_id"],
        "status": "user_visual_reference_selection_confirmed",
        "selected_count": len(selected),
        "selected_references": selected,
        "user_approval": {
            "decision": "채택완료",
            "approved_at": args.approved_at,
            "source": "current_user_conversation",
        },
        "source_state": {
            "path": str(state_path.resolve()),
            "sha256": hashlib.sha256(state_path.read_bytes()).hexdigest(),
            "refill_round": state.get("refill", {}).get("round", 0),
        },
        "next_stage": "pm1_design_direction_grouping",
        "next_stage_input": "selected_references_only",
        "design_dna_extracted": False,
        "visual_target_created": False,
        "product_changed": False,
        "implementation_allowed": False,
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    write_json_atomic(args.output, payload)
    print(json.dumps({"selected": len(selected), "output": args.output}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
