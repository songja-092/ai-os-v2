# Current State

현재 단계는 `M2 — 요구사항 정리 및 승인 Gate` 기술 검증을 PASS하고 `M3 — 조건부 Research·Design과 Plan/Tasks`를 준비하는 상태입니다.

M2 공식 검증 Run은 `run-05dbfc27`입니다. `execution_mode: skills`, `workflow_run_id: null`인 동일 Run에서 Specify, 승인 전 Plan 차단, Spec 본문 수정과 Version 증가, 승인, Plan Artifact 생성과 새 프로세스 재조회를 확인했습니다.

`run-3b0ffae8`은 다른 Agent의 변경이 섞인 `diagnostic_failed` 기록이며 M2 PASS 증거로 사용하지 않습니다. 기존 실패 Run도 M2 PASS 증거가 아닙니다.

## Spec Kit 및 Core 상태

- ✅ 검증됨: V2 Core가 Run, Gate와 상태를 소유하는 단일 Orchestrator로 동작합니다. 사용자 표시명은 `Zeus`이며 별도 AI 모델이 아닙니다.
- ✅ 검증됨: Spec Kit은 `speckit-specify`, `speckit-plan` Skill과 Markdown Artifact 생성을 담당합니다.
- ✅ 검증됨: Spec Kit Workflow Run, Gate Resume와 상태 동기화는 M2 기본 실행 경로에서 제외됐습니다.
- ✅ 검증됨: Artifact가 없으면 Agent 종료코드가 `0`이어도 실패로 판정합니다.
- `workflow_run_id`는 과거 Workflow 증거를 보존하기 위한 nullable 선택 필드입니다.

## 역할과 단독 쓰기 규칙

- Codex는 M2부터 내부 설정, Core, Run, Gate, Git, Skill 연결과 기술 검증을 담당합니다.
- Antigravity는 실제 웹·앱·화면·기능 구현을 담당하며, M4 실제 구현 전까지 V2 내부 작업에서 대기합니다.
- 동일 Run은 한 시점에 쓰기 담당자 한 명만 허용합니다.
- 구현 Agent의 완료 보고는 공식 사실이 아니며, Codex 검증과 사용자 승인을 거친 변경만 Git에 저장합니다.

## 공식 기억 상태

- 현재 기준 원격 `origin/main`은 `7674debbe3f22c16df1e3ef81af25fa4052c91ca`입니다.
- V2 Run의 공식 기억은 `memory.official_commit`, 로컬 구현 기준은 `v2_workspace.head`로 분리해 기록합니다.
- 이 문서와 M2 기준점 Commit은 아직 Push되지 않았습니다.

## 다음 단계

- M3에서 조건부 Research·Design, Plan·Tasks와 사용자 계획 승인을 검증합니다.
- UI/UX가 필요한 병원 웹에서 UI UX Pro Max는 M3 디자인 후보로만 시험합니다.
- M4에서 승인된 Plan·Tasks를 기준으로 Antigravity에게 실제 웹 구현을 전달합니다.
- M5 전에는 전용 V2 UI를 구현하지 않습니다.
