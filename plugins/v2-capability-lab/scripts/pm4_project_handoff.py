#!/usr/bin/env python3
"""Create a non-executing PM4 handoff from the user's selected direction."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--output-md", required=True)
    args = parser.parse_args()
    state = json.loads(Path(args.state).read_text(encoding="utf-8"))
    receipt = json.loads(Path(args.receipt).read_text(encoding="utf-8"))
    selected_id = state.get("selected_candidate_id")
    selected = next((item for item in state.get("items", []) if item.get("candidate_id") == selected_id), None)
    record = state.get("selection_record") or {}
    if not selected or record.get("selected_by") != "user":
        raise SystemExit("a recorded user selection is required")
    handoff = {
        "schema_version": "1.0",
        "request_id": state["request_id"],
        "status": "user_selected_ready_for_next_stage",
        "selected_direction": {
            "candidate_id": selected["candidate_id"],
            "label": selected["direction_label"],
            "summary_ko": selected["direction_summary_ko"],
            "evidence_links": selected["evidence_links"],
        },
        "implementation_evidence": {
            "repository": selected["name"],
            "url": selected["url"],
            "license": selected["license"],
            "capabilities": selected["capabilities"],
            "adoption_status": "not_installed_not_adopted",
        },
        "confirmed_scope": receipt["answers"],
        "preserved_candidate_ids": [item["candidate_id"] for item in state["items"] if item["candidate_id"] != selected_id],
        "unverified": ["Instagram authenticated collection", "actual preview", "implementation", "deployment"],
        "forbidden_before_next_approval": ["install", "implement", "apply_to_product", "deploy"],
        "product_changed": False,
    }
    Path(args.output_json).write_text(json.dumps(handoff, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# PM4 선택 결과 제작 가능 확인서", "",
        f"- 선택 방향: {selected['direction_label']}",
        f"- 선택 방식: {record['input_method']}",
        f"- 선택 시각: {record['selected_at']}",
        f"- 구현 참고: {selected['name']} ({selected['license']})", "",
        "## 선택 근거", "",
    ]
    lines += [f"- [{item['source']}]({item['url']}): {item['summary_ko']}" for item in selected["evidence_links"]]
    lines += ["", "## 현재 경계", "", "- 실제 설치·구현·제품 적용·배포는 하지 않았습니다.", "- 나머지 네 방향은 비교 후보로 보존합니다.", "- Instagram 로그인 수집과 실제 Preview는 아직 검증되지 않았습니다.", ""]
    Path(args.output_md).write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"status": handoff["status"], "selected": selected_id}, ensure_ascii=False))


if __name__ == "__main__":
    main()
