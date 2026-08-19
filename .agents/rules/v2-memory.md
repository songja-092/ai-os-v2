# AI OS V2 공용 기억 Load

새 작업 또는 새 세션에서 사용자의 첫 요청을 처리하기 전에 @../../wiki/SESSION_START_CONTRACT.md를 가장 먼저 읽고, 저장소의 `AGENTS.md`에 정의된 공용 기억 Load 절차를 수행한다.

다음 문서를 기억이나 이전 대화가 아닌 실제 파일에서 읽는다.

- @../../wiki/GOAL.md
- @../../wiki/CURRENT_STATE.md
- @../../wiki/DECISIONS.md
- @../../wiki/ARCHITECTURE.md
- @../../wiki/VERIFICATION.md
- @../../wiki/POST_MVP_PM0_PM6_BASELINE.md
- @../../wiki/PM1_PM4_DESIGN_MEETING_2026-08-19.md
- @../../wiki/AI_EVIDENCE_GUARD.md

Wiki 내용을 이 Rule에 복사하지 않는다. 현재 Worktree·GitHub `origin/main`·Obsidian Vault의 HEAD를 각각 확인한다. 서로 다르면 현재 상태를 섞지 않고 불일치를 보고한다. 필수 문서를 모두 읽은 경우에만 현재 HEAD Commit SHA를 기준 기억으로 고정하고 `AI OS V2 Memory Loaded: <Commit SHA>` 형식으로 보고한다.

로컬 미커밋 변경이나 충돌 위험이 있으면 임의로 동기화하거나 덮어쓰지 말고 중단하여 사용자에게 보고한다.
