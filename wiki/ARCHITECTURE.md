# Architecture

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

## 현재 기반

```text
Obsidian/Wiki <-> GitHub main -> Archify
사람의 편집       공식 원본       commit 기반 시각화
```

GitHub `main`이 공식 원본입니다. Obsidian은 같은 Markdown을 읽고 편집하는 인터페이스이며 Archify는 원본이 아니라 특정 commit에서 만들어지는 파생 결과입니다.

## V2 Core 구조

```text
사용자
  | 자연어 요청
  v
V2 Core (Zeus) — 유일한 Orchestrator
  | Run ID / Base Commit / 상태
  | Specify / Clarify / 승인 Gate
  | 조건부 Research / Design
  | Plan / Tasks / 승인 Gate
  v
Manual Agent Adapter
  | Antigravity 작업 지시서
  | 사용자 전달 및 권한 승인
  | 구현 결과 회수
  v
V2 Core Gate 전이
  | Codex 독립 검증
  | 사용자 실물 확인과 최종 승인
  | Result Commit
  | 별도 worktree Rollback / Restore
  v
Run 종료와 승인된 Wiki 갱신
```

V2 Core는 모든 Run, Gate와 상태를 소유하는 유일한 Orchestrator입니다. `Zeus`는 사용자에게 보이는 V2 Core의 이름이며 별도 AI 모델이 아닙니다. Spec Kit은 Workflow 엔진 대신 개별 Skill과 Markdown Artifact(`spec.md`, 체크리스트, `plan.md`)를 제공합니다.

Codex는 내부 설정, Core, Run, Gate, Git, Skill 연결과 기술 검증을 담당합니다. Antigravity는 M4부터 승인된 계획을 기준으로 실제 웹·앱·화면·기능을 구현합니다. 동일 Run에는 한 시점에 쓰기 담당자 한 명만 허용합니다.

## 사용자에게 보이는 흐름

기술 단계를 그대로 노출하지 않고 다음 세 단계로 표현합니다.

1. 원하는 것을 말하기
2. 추천 결과 또는 시안 고르기
3. 실제 결과를 확인하고 완료 또는 수정 말하기

기존 프로젝트를 가져오면 V2가 실제 상태와 부족한 부분을 분석하고 `추천대로 진행` 또는 `직접 선택`을 제시합니다. 사용자는 코드, 명령어와 내부 Agent 연결을 직접 관리하지 않으며 Run ID, SHA, Spec·Plan·Tasks와 기술 로그는 필요할 때만 자세히 봅니다.

## 제작 파이프라인

1. **Intake**: 자연어 요구, 참고 URL과 대상 Project를 받습니다.
2. **Specify/Clarify**: 사용자 원문을 보존한 채 요구사항, 제외 범위와 완료 조건을 정리하고 사용자가 승인합니다.
3. **Target Environment**: Web, Android, iOS, Desktop, CLI, API, Server 또는 기타 대상 환경을 확정합니다.
4. **Conditional Research**: 승인된 요구를 구현하는 데 외부 근거가 필요할 때만 공식 문서, GitHub, Web과 실사용 자료를 조사합니다. 조사로 요구가 달라지면 Spec을 갱신하고 다시 승인받습니다.
5. **Conditional Design**: UI/UX가 필요한 경우에만 디자인 도구를 선택하고 사용자가 결과를 승인합니다.
6. **Plan/Tasks**: 승인된 Spec, Research와 Design을 작은 구현 작업으로 변환하고 사용자가 계획을 승인합니다.
7. **Reuse Decision**: 기존 제품·OSS·Skill·MCP·서비스를 비교하고 필요한 부품만 선택합니다.
8. **Handoff**: Codex가 변경 파일, 허용 명령, 금지 범위, 검증 방법과 복구점을 포함한 구현 지시서를 만듭니다.
9. **Implement**: Antigravity가 승인된 Task를 한 개씩 구현합니다.
10. **Verify**: Codex가 Target Environment에서 구현 Agent와 독립적으로 검증하고 증거를 기록합니다.
11. **Accept**: 사용자가 실제 결과를 확인하고 승인하거나 수정을 요청합니다.
12. **Save**: 승인된 결과를 Run Branch의 Result Project Commit으로 저장합니다.
13. **Recover**: 별도 worktree에서 이전 Commit과 Result Commit을 각각 실행해 복구 가능성을 확인합니다.
14. **Promote**: 검증·복구가 끝난 Result Commit을 `main`에 반영할지는 별도 사용자 승인으로 결정합니다.

각 단계는 `running`, `waiting_user`, `waiting_agent`, `blocked`, `failed`, `completed`, `cancelled` 중 하나의 실제 상태를 가집니다. 실패하거나 중단된 Run은 원인과 재개 지점을 남깁니다.

## V2 화면 뼈대 — Core MVP 이후 후보

Dashboard를 구현할 때는 M1~M7에서 검증된 실제 Run 상태만 읽습니다. Dashboard는 현재 Core MVP의 필수 마일스톤이 아닙니다.

얇은 UI의 구현 경계, Run 표시 우선순위, Project Registry, 허용 Action과 장애 격리 기준은 [[THIN_UI_MVP_CONTRACT]] · [GitHub 링크](THIN_UI_MVP_CONTRACT.md)를 단일 기준으로 사용합니다.

```text
┌─────────────────────────┬──────────────────────────────────┐
│ 프로젝트 / Run          │                                  │
│ 현재 단계와 상태         │          실제 결과 영역          │
│ Milestone / Tasks       │                                  │
│ 막힌 문제 / 승인 대기    │   Spec · Design · Preview · 증거 │
│                         │                                  │
│ 자연어 입력              │                                  │
│ 승인 / 수정 요청         │                                  │
│ 저장 / 되돌리기 상태     │                                  │
└─────────────────────────┴──────────────────────────────────┘
```

- 결과와 사용자가 판단할 내용을 먼저 보여주고 기술 로그는 필요할 때만 펼칩니다.
- 진행률은 `검증 완료 Tasks / 승인된 전체 Tasks`로 계산합니다.
- 승인 버튼은 화면 상태만 바꾸지 않고 같은 V2 Run의 실제 Gate 상태를 변경해야 합니다.
- 웹 Live Preview는 사용자 승인 `localhost` 또는 `127.0.0.1` 개발 서버를 사용합니다.
- CLI, API와 Server 프로젝트는 Live Preview 대신 해당 환경의 실제 실행 결과를 표시합니다.
- Commit과 Rollback 상태는 실제 SHA와 검증 결과가 없으면 완료로 표시하지 않습니다.
- 각 마일스톤은 `Core 검증`과 `사용자가 직접 확인할 흐름`을 나란히 보여줍니다. 사용자 확인 항목은 `대기`, `확인 가능`, `PASS`, `FAIL`로 구분하며 Codex나 UI가 사용자를 대신해 PASS 처리하지 않습니다.
- 사용자 흐름 항목은 해당 마일스톤 범위에만 둡니다. 예를 들어 M2는 자연어 Spec과 승인 Gate를 확인하며 파일 업로드 같은 제품 기능은 승인된 Feature Run 범위가 생기는 M4 이후에 확인합니다.

## Run 기록 경계

- V2 저장소는 공식 기억과 Core·Run·Gate·Skill 연결 정의를 보관합니다.
- 제작 프로젝트 저장소는 실제 소프트웨어와 Result Commit을 보관합니다.
- Spec Kit 산출물은 원본 경로를 참조하고 Run 기록에 복제하지 않습니다.
- 첫 MVP는 활성 Run 하나만 지원하고 DB를 사용하지 않습니다.
- `Result Project Commit`은 Run Branch의 검증된 결과이며 자동으로 `main` 반영을 의미하지 않습니다.
- 실패·취소 시 실행 중인 개발 서버, 임시 worktree와 잠금을 정리하되 원인, 마지막 성공 단계와 재개점은 보존합니다.
- 검증 증거는 최소한 실행 명령, 종료 코드, 실행 시각, 대상 Commit SHA와 산출물 경로를 기록합니다.

## User Scenario 기록과 계산

각 마일스톤의 사용자 확인과 Codex 기술 검증은 같은 Scenario ID 아래 별도 결과로 저장합니다. Scenario는 최소한 `scenario_id`, `scenario_version`, `milestone`, `run_id`, `surface`, 필수 여부, 사용자 확인 항목, Codex 확인 항목, 두 결과, 메모, 증거와 검증 시각을 가집니다.

```yaml
target:
  repository: hospital-web
  core_commit_sha: core123
  project_commit_sha: web456
  environment: web
  url: http://127.0.0.1:5173
```

제작 프로젝트가 아직 없는 단계에서는 `project_commit_sha: null`로 기록합니다. 종합 상태는 별도로 편집하지 않고 다음 규칙으로 계산합니다.

- 현재 Commit과 Scenario 버전이 같고 `user_result: pass`, `codex_result: pass`이면 `PASS`
- 필수 결과가 아직 없으면 `pending`
- 사용자 또는 Codex 결과가 실패이면 `FAIL`
- Commit 또는 `scenario_version`이 달라지면 이전 결과를 보존한 채 `stale` 및 재검증 필요

실제 Run·Gate·Task 상태는 V2 Core, 기술 검증과 증거는 Codex, 사용자 판정은 사용자가 소유합니다. Codex가 현황판을 갱신할 때도 이 원본 상태를 임의로 추측하거나 대신 판정하지 않습니다.

## 구현 마일스톤

1. **M1 — Run·Git 안전 기반**: V2 Run ID, Project, 두 Base Commit, Branch, 상태·중단·재개와 nullable `workflow_run_id` 호환 필드를 연결합니다.
2. **M2 — Spec과 승인 Gate**: `run-05dbfc27`에서 Spec Kit Skill, Artifact, 승인 전 차단과 승인 후 Plan 생성을 같은 V2 Run으로 검증했습니다.
3. **M3 — 조건부 Design과 Plan/Tasks — ✅ 완료**: `run-05dbfc27`에서 Option C v2, 공식 Tasks 47개와 5개 최소 실행 묶음 Handoff를 생성했습니다.
4. **M4 — Feature Run 완성 — ✅ 완료**: Antigravity 구현, Codex 독립 검증, 사용자 승인, Result Commit `c970352`와 임시 worktree Rollback/Restore를 병원 웹에서 검증했습니다.
5. **M5 — 수집·분석·레시피 선택 Core — ✅ 완료**: 새 프로젝트 또는 기존 프로젝트의 실제 상태를 수집하고 부족한 부분과 완료 수준을 분석하여 검증된 제작 레시피 하나와 다음 한 작업을 추천합니다. 자동 크롤러·별도 DB·Dashboard는 만들지 않습니다.
6. **M6 — 기존 프로젝트 Change Run — ✅ 완료**: `run-fa8b4386`에서 병원 프로젝트 `HERO-01`만 수정하고 영향 범위 검증, 사용자 확인, Result Commit `e2625bb`과 별도 worktree Rollback/Restore를 완료했습니다. 이는 AI 부분 수정 검증이며 직접 시각 편집 기능을 포함하지 않습니다.
7. **M7 — PDF 도면 스탬프 MVP E2E — ✅ 완료**: M5에서 선택한 레시피로 모바일에서 다중 페이지 PDF 선택·이동, 페이지별 복수 기호 배치·속성·크기 조절, 원본 보존과 새 PDF 내보내기를 구현했습니다. 사용자 확인, Result Commit `3b592c8`과 별도 worktree Rollback/Restore까지 통과했습니다.

각 마일스톤이 PASS하면 V2 Core가 `CURRENT_STATE.md` 갱신안을 생성합니다. 사용자가 승인한 갱신만 Commit/Push하며 Obsidian은 같은 로컬 Wiki를 즉시 표시합니다. Archify 자동 갱신은 현재 구현된 것으로 간주하지 않습니다.

## 증거 규칙

- 아이디어나 화면 예시는 실제 구현과 분리하여 표시합니다.
- 실제 파일 또는 설정이 있어야 `🔨 구현됨`입니다.
- 해당 기능을 직접 실행한 증거가 있어야 `✅ 검증됨`입니다.
- 구현 Agent의 보고만으로 PASS 처리하지 않습니다.
- 실행 검증에는 명령, 종료 코드, 실행 시각, 대상 Commit SHA와 산출물 경로를 남깁니다.
- 조사 결과에는 원문 URL, 확인 날짜와 채택/탈락 이유를 남깁니다.

## 현재 부품 상태

| 역할 | 부품 | 상태 |
|---|---|---|
| 공식 기억과 버전 | GitHub + Wiki | ✅ 연결 검증 기록 존재 |
| 사람용 편집 | Obsidian | ✅ 연결 검증 기록 존재 |
| 구조 시각화 | Archify | M3 기준점 Commit에서 재생성·검증, M4 상태 반영은 별도 갱신 필요 |
| 자연어 명세 및 계획 | Spec Kit Skills | ✅ 구조 A Skills 직접 호출 및 Plan 성공 검증 |
| 디자인 시스템 제안 | UI UX Pro Max | ✅ M3 설치·직접 호출·Artifact 생성 검증 |
| 설계·독립 검증 | Codex | 사용 중 |
| 실제 구현 | Antigravity | ✅ M4 병원 웹 & M7 PDF 스탬프 구현 완료 |
| 구현 최소화 규칙 | Ponytail | 🔨 `main` 설치, 실제 Task 미검증 |
| 환경별 검증 | 프로젝트별 도구 | 💡 Target Environment에 따라 선택 |
| Core Workflow | V2 Core Orchestrator | ✅ 단독 Run/Gate/상태 소유 검증 완료 (구조 A) |
| V2 UI | 없음 | PM1 계약 확정, Preview v1 시각 충실도 실패, 제품 구현 전 |
| 자동 AI 호출 | 없음 | MVP 필수 아님, Manual Agent Adapter 사용 |

Kernel, Planner, 별도 Collector 서버, Multi-Agent와 자체 실행 엔진은 현재 아키텍처의 필수 구성요소가 아닙니다. M5의 수집·분석은 기존 파일 검색, 실행 확인과 공식 자료 조사로 검증하며 Dashboard는 검증된 Core 흐름을 나중에 감싸는 인터페이스입니다.

## MVP 이후 연결

M7이 PASS하면 Core는 완료 상태만 표시하고 멈추지 않고 `wiki/POST_MVP_ROADMAP.md`의 최우선 미검증 후보를 읽습니다. 이 자동 연결은 `상태 조회 → 후보 로드 → 수집 → 분석 → 추천 → Preview 준비`까지만 허용하며 구현 Gate를 자동 통과하지 않습니다.

Post-MVP는 사용자 기능을 기준으로 `PM1 최소 조립식 기반 + 얇은 UI → PM2 직접 부분 수정 → PM3 조사·자료 수집·병목 진단 → PM4 AI 의도 정합성` 순서로 확정합니다. PM1은 고정 Core 위에 정적 Project·Module Registry, 고정 UI Slot, Design Recipe와 Adapter 경계를 두고 실제 Run 상태를 읽는 얇은 UI를 제공합니다. Module은 Core 상태를 직접 수정하지 않으며 실패는 해당 Module에 격리합니다.

PM1 UI는 `V2 Core → ui-state(JSON) → UI → ui-action → V2 Core` 경계를 유지합니다. PM3 Source Adapter는 새 프로젝트 조사와 기존 프로젝트 병목 진단을 같은 수집 구조로 처리하고 실패를 Core·다른 프로젝트와 격리합니다. PM4는 Planner·Implementer·Verifier의 Intent 정합성 계약을 분리하지만 새로운 Multi-Agent Orchestrator나 Provider 자동 교체를 구현하지 않습니다.

PM1의 디자인은 Hybrid H를 사용합니다. Reference Mix와 이미지 탐색은 방향 결정에만 사용하고, 화면·핵심 상태별 승인 `visual_target`을 Image-to-Code에 직접 입력해 `1440×950`, `430px`, `390px`에서 Fidelity를 확인합니다. PASS 이후 코드가 디자인 원본이며 Design Recipe는 Core CSS와 분리합니다.
