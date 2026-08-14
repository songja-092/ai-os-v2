# Current State

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

현재 `M7 — PDF 도면 스탬프 MVP E2E`까지 구현·독립 검증·사용자 승인·Result Commit·Rollback/Restore가 완료됐습니다. M7 공식 Run은 `run-c0a968f3`, 제품 Result Commit은 `3b592c8`입니다. 최초 intake 입력은 1페이지 PDF(`c5573243…`)이며, 다중 페이지 확정 범위의 최종 검증에는 별도의 2페이지 입력(`bb59d680…`)과 기호가 합성된 출력(`d40efdb…`)을 사용했습니다. 최초 입력이 바뀐 것이 아니라 검증 범위가 확장되어 별도 Artifact가 추가된 것입니다. 이로써 `AI OS V2 Core MVP M1~M7`은 검증 완료·동결 상태입니다. Post-MVP `PM1~PM4` 기획과 PM1 Reference Mix는 확정됐고 현재 활성 단계는 `PM1 — 얇은 UI`입니다. 기존 이미지 시안 5장은 참고자료이며 모바일 우선 클릭형 Preview A/B와 실제 PM1 구현은 아직 시작하지 않았습니다.

M2 공식 검증 Run은 `run-05dbfc27`입니다. `execution_mode: skills`, `workflow_run_id: null`인 동일 Run에서 Specify, 승인 전 Plan 차단, Spec 본문 수정과 Version 증가, 승인, Plan Artifact 생성과 새 프로세스 재조회를 확인했습니다.

M3에서도 같은 `run-05dbfc27`을 유지했습니다. UI UX Pro Max와 frontend-app-builder로 모바일 우선 Option C v2를 생성하고 Browser 기술 검증을 통과했습니다. 사용자는 디자인 마감에 `needs_improvement`를 남겼지만 M4 파이프라인 시험 입력으로 승인했습니다. 상업 디자인과 Reference 승인은 아닙니다.

공식 `speckit-tasks` Skill로 T001~T047의 `tasks.md`를 한 번 생성했고 Spec·Plan·Option C 정합성을 확인했습니다. Antigravity용 M4 Handoff는 실제 실행 범위를 5개 최소 묶음으로 정리했습니다. 제작 프로젝트 M3 기준점은 Commit `2554340`입니다.

M4에서는 Antigravity가 Vite·TypeScript 병원 웹을 구현하고 Codex가 390px·430px·1440px Browser 흐름, Typecheck, Build, Console, 비저장 동작을 독립 검증했습니다. 사용자가 파이프라인 테스트를 승인한 뒤 Result Commit `c970352`를 생성했고 별도 임시 worktree에서 기준 Commit `2554340`과 Result Commit의 Rollback·Restore를 재현했습니다. 당시 비차단 후속 개선으로 남긴 390px 제목 줄바꿈은 M6에서 해결했으며 상업 디자인과 Reference 승인은 계속 `false`입니다.

M6에서는 Quick Change Run `run-fa8b4386`으로 `HERO-01`만 수정했습니다. 제품 소스 변경은 `src/styles.css`의 국소 규칙 2개뿐이며 390px·430px 줄바꿈, 1440px 회귀, 메뉴·의료진·예약 오류·완료·복귀 흐름을 확인했습니다. 사용자 판정과 Codex 검증은 모두 `pass`이며 Result Commit은 `e2625bb`입니다. 기준 Commit `c970352`와 Result Commit을 별도 worktree에서 각각 Build하여 Rollback·Restore를 재현했습니다. 이는 자연어를 통한 AI 부분 수정의 검증이며 사용자가 Preview에서 직접 값을 조절하는 편집 패널이 구현됐다는 의미는 아닙니다.

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

- 현재 기준 원격 `origin/main`은 `72db6dc2fa5cde72c78cfd66184d13cc57ffc5aa`입니다.
- V2 Run의 공식 기억은 `memory.official_commit`, 로컬 구현 기준은 `v2_workspace.head`로 분리해 기록합니다.
- 제작 프로젝트의 M3 기준점은 `2554340`, M4 Result Commit은 `c970352`, M6 Result Commit은 `e2625bb`, M7 Result Commit은 `3b592c8`이며 Push되지 않았습니다.
- 이 Wiki 갱신도 로컬 기준점 Commit으로 저장하고 Push는 별도 승인 전까지 수행하지 않습니다.

## 다음 단계

- Post-MVP 공식 순서는 `PM1 얇은 UI → PM2 직접 부분 수정 → PM3 자료 가져오기 → PM4 제작 정확도와 AI 교체 기반`입니다. 후보 판정과 구현 상태를 분리하며 현재 PM1~PM4는 기획 확정, 구현 전 상태입니다.
- PM1은 승인된 계약에 따라 `V2 Core → ui-state(JSON) → UI → ui-action → V2 Core` 경계를 사용합니다. 다음 한 작업은 [[ui-reference-mix]] · [GitHub 링크](ui-reference-mix.md)를 반영한 모바일 우선 클릭형 Preview A/B 제작입니다. 사용자가 `A`, `B` 또는 수정안을 선택하기 전에는 실제 PM1 UI를 구현하지 않습니다.
- M5의 수집·분석·레시피 선택 Core와 M6의 Quick Change Run·AI 부분 수정·회귀·복구 흐름, 그리고 M7 모바일 PDF 도면 스탬프 `local_product` E2E 구현 및 사용자 검증을 완료했습니다.
- 사용자에게는 `원하는 것을 말하기 → 추천 결과 또는 시안 고르기 → 실제 결과를 확인하고 완료 또는 수정 말하기`만 보이며, 기본 행동은 `[추천대로 진행]`과 `[직접 선택]`으로 단순화합니다.
- 자동 인터넷 크롤러, 별도 수집 서버·DB, 학습기, Dashboard UI와 Multi-Agent는 M5 범위에 포함하지 않습니다.
- 디자인 레시피는 현재 설치된 Product Design·frontend-app-builder·UI UX Pro Max를 우선 재사용합니다. Taste와 Google Stitch Skills는 미설치 후보이며 실제 작은 검증 전에는 채택 또는 검증됨으로 기록하지 않습니다.
- Supabase의 Auth·Postgres·RLS·Migration·검증·배포 흐름은 병원 파일럿에 추가하지 않고, 데이터 저장이 승인된 후속 프로젝트의 조건부 Full-stack 레시피 후보로 둡니다.
- M5의 공식 분석 요청은 `PDF 도면 위에 스탬프를 배치·이동·크기 조절하고 원본을 보존한 채 새 PDF로 저장`이며, 구현이나 패키지 설치 없이 최대 두 개의 현실적인 레시피와 다음 작업 하나만 제시합니다.
- M7은 M5에서 선택한 레시피로 모바일 PDF 도면 스탬프 `local_product`를 E2E 검증 및 승인 받았습니다.
- Core MVP 이후 첫 단계는 PM1 얇은 UI이며 프로젝트 홈은 `B — 프로젝트·다음 행동 중심`, 작업실은 `A — Preview 중심`을 클릭형 Preview 기준으로 사용합니다. PM2는 `HERO-01` 직접 부분 수정, PM3는 Reddit·GitHub·Threads·웹·문서 Source Adapter, PM4는 Intent 정합성과 AI 역할 Adapter 경계를 검증합니다.
