---
description: AI OS V2에서 기능·상태·PASS·동기화·복구를 주장할 때 항상 적용하는 증거 우선 규칙
---

# Evidence First

- 채팅 기억보다 현재 Git Commit의 실제 파일을 우선합니다.
- 작업 전 `wiki/SESSION_START_CONTRACT.md`, `wiki/CODEX_COMMON_EXECUTION_CONTRACT.md`, `AGENTS.md`, `wiki/AI_EVIDENCE_GUARD.md`를 읽습니다.
- 변경 전 승인 범위와 잠긴 PM을 확인하고, 변경 영향에 맞는 기존 검사를 선택합니다.
- 일반 코드 오류는 승인 범위 안에서 수정한 뒤 실패했던 동일 검사를 다시 실행합니다.
- 데이터 손실·권한·로그인·비용·사용자 Dirty·PM 잠금 충돌은 임의로 해결하지 않고 중단해 보고합니다.
- 직접 읽지 못한 파일·실행 결과·웹 내용을 확인했다고 말하지 않습니다.
- 설계, 구현, 검증, 사용자 승인을 서로 다른 상태로 기록합니다.
- 증거가 없으면 `확인 필요` 또는 `not_proven`으로 표현합니다.
- 로컬 Worktree·GitHub `origin/main`·Obsidian Vault의 SHA가 실제로 같을 때만 `동기화됨`이라고 표현합니다.
- Fixture·Pilot·Preview를 Core 연결·PM PASS·제품 완료로 확대하지 않습니다.
- 사용자 PASS는 사용자만 내립니다.
- 같은 Run에서 쓰기 담당자는 한 명만 둡니다.
