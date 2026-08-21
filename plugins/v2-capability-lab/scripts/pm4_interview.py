#!/usr/bin/env python3
"""Create one beginner-friendly PM4 interview question at a time."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


QUESTIONS = (
    ("goal", "무엇을 찾고 싶은가요?", ["디자인 참고", "구현 도구", "사용자 반응", "잘 모르겠어요"]),
    ("target", "어디에 사용할 자료인가요?", ["V2 운영 화면", "고객용 웹", "기능·스킬", "아직 정하지 않음"]),
    ("priority", "무엇을 먼저 볼까요?", ["인기 사례", "검증된 구현", "시각적 다양성", "균형 있게"]),
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request-file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        path = Path(args.request_file).resolve()
        request = json.loads(path.read_text(encoding="utf-8"))
        answers = request.get("interview_answers") or {}
        if not isinstance(answers, dict):
            raise ValueError("interview_answers must be an object")
        next_question = None
        for field, question, choices in QUESTIONS:
            if not answers.get(field):
                next_question = {"field": field, "question": question, "choices": choices, "input": "mouse_first"}
                break
        if next_question is None:
            open_decisions = request.get("open_decisions") or []
            if not isinstance(open_decisions, list):
                raise ValueError("open_decisions must be a list")
            unresolved = next((item for item in open_decisions if isinstance(item, dict) and not answers.get(item.get("field"))), None)
            if unresolved:
                next_question = {
                    "field": unresolved["field"],
                    "question": unresolved["question"],
                    "choices": unresolved.get("choices", []),
                    "input": "mouse_first" if unresolved.get("choices") else "short_text",
                }
        result = {
            "schema_version": "1.0",
            "request_id": request.get("request_id"),
            "status": "confirmed" if next_question is None else "needs_user_answer",
            "answers": answers,
            "next_question": next_question,
            "rule": "ask_one_more_only_when_the_answer_changes_the_result",
        }
        Path(args.output).resolve().write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
