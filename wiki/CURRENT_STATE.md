# Current State

현재 `M4 — Feature Run 완성`까지 검증을 마쳤으며 다음 단계는 `M5 — 얇은 V2 UI`입니다.

M2 공식 검증 Run은 `run-05dbfc27`입니다. `execution_mode: skills`, `workflow_run_id: null`인 동일 Run에서 Specify, 승인 전 Plan 차단, Spec 본문 수정과 Version 증가, 승인, Plan Artifact 생성과 새 프로세스 재조회를 확인했습니다.

M3에서도 같은 `run-05dbfc27`을 유지했습니다. UI UX Pro Max와 frontend-app-builder로 모바일 우선 Option C v2를 생성하고 Browser 기술 검증을 통과했습니다. 사용자는 디자인 마감에 `needs_improvement`를 남겼지만 M4 파이프라인 시험 입력으로 승인했습니다. 상업 디자인과 Reference 승인은 아닙니다.

공식 `speckit-tasks` Skill로 T001~T047의 `tasks.md`를 한 번 생성했고 Spec·Plan·Option C 정합성을 확인했습니다. Antigravity용 M4 Handoff는 실제 실행 범위를 5개 최소 묶음으로 정리했습니다. 제작 프로젝트 M3 기준점은 Commit `2554340`입니다.

M4에서는 Antigravity가 Vite·TypeScript 병원 웹을 구현하고 Codex가 390px·430px·1440px Browser 흐름, Typecheck, Build, Console, 비저장 동작을 독립 검증했습니다. 사용자가 파이프라인 테스트를 승인한 뒤 Result Commit `c970352`를 생성했고 별도 임시 worktree에서 기준 Commit `2554340`과 Result Commit의 Rollback·Restore를 재현했습니다. 390px 제목 줄바꿈은 비차단 후속 개선으로 남겼으며 상업 디자인과 Reference 승인은 계속 `false`입니다.

`run-3b0ffae8`은 다른 Agent의 변경이 섞인 `diagnostic_failed` 기록이며 M2 PASS 증거로 사용하지 않습니다. 기존 실패 Run도 M2 PASS 증거가 아닙니다.

## Spec Kit 및 Core 상태

- ✅ 검증됨: V2 Core가 Run, Gate와 상태를 소유하는 단일 Orchestrator로 동작합니다. 사용자 표시명은 `Zeus`이며 별도 AI 모델이 아닙니다.
- ✅ 검증됨: Spec Kit은 `speckit-specify`, `speckit-plan`, `speckit-tasks` Skill과 Markdown Artifact 생성을 담당합니다.
- ✅ 검증됨: `specify integration upgrade codex`로 누락된 공식 관리 Skill 7개를 복구했고 integration status의 Missing/Modified managed files가 모두 0입니다.
- ✅ 검증됨: Spec Kit Workflow Run, Gate Resume와 상태 동기화는 M2 기본 실행 경로에서 제외됐습니다.
- ✅ 검증됨: Artifact가 없으면 Agent 종료코드가 `0`이어도 실패로 판정합니다.
- `workflow_run_id`는 과거 Workflow 증거를 보존하기 위한 nullable 선택 필드입니다.

## 역할과 단독 쓰기 규칙

- Codex는 M2부터 내부 설정, Core, Run, Gate, Git, Skill 연결과 기술 검증을 담당합니다.
- Antigravity는 실제 웹·앱·화면·기능 구현을 담당하며 M4 병원 웹 구현을 완료했습니다.
- 동일 Run은 한 시점에 쓰기 담당자 한 명만 허용합니다.
- 구현 Agent의 완료 보고는 공식 사실이 아니며, Codex 검증과 사용자 승인을 거친 변경만 Git에 저장합니다.

## 공식 기억 상태

- 현재 기준 원격 `origin/main`은 `7674debbe3f22c16df1e3ef81af25fa4052c91ca`입니다.
- V2 Run의 공식 기억은 `memory.official_commit`, 로컬 구현 기준은 `v2_workspace.head`로 분리해 기록합니다.
- 제작 프로젝트의 M3 기준점은 `2554340`, M4 Result Commit은 `c970352`이며 둘 다 Push되지 않았습니다.
- 이 Wiki 갱신도 로컬 기준점 Commit으로 저장하고 Push는 별도 승인 전까지 수행하지 않습니다.

## 다음 단계

- M5에서는 M1~M4의 실제 Core·Run·Gate·Artifact·Commit 상태를 읽는 얇은 V2 UI를 설계합니다.
- 초보 사용자에게는 프로젝트 선택, 현재 단계, 결과 Preview, 승인·수정 요청, 저장·복구 상태만 우선 표시합니다.
- M5 UI는 실제 원본 상태를 읽고 변경할 뿐 임의의 진행률·PASS·SHA를 생성하지 않습니다.
