# Verification

## Required checks

- Obsidian에서 변경한 Markdown이 GitHub의 동일 commit에 존재하는가
- GitHub에서 변경한 Markdown이 Git pull 후 Obsidian에 표시되는가
- 외부 AI가 GitHub의 `wiki/CURRENT_STATE.md`를 동일하게 읽는가
- Archify 결과가 사용한 Repository와 commit SHA를 식별하는가

GitHub to Obsidian Reverse Connection Test - PASS

## V2 시작 준비 판정 기준

다음 조건을 모두 직접 확인하면 최초 실제 프로젝트 파일럿을 시작할 수 있습니다.

- [ ] 연결 검증 네 항목의 Repository, Branch, Commit SHA와 실제 결과가 한 보고서에서 확인됨
- [ ] 세 AI가 동일한 Wiki SHA를 읽고 이를 `Base Memory Commit`으로 기록함
- [ ] Spec Kit 기반 V2 Workflow에서 실제 기능 하나의 Spec과 완료 조건을 생성함
- [ ] 프로젝트의 `Target Environment`가 Spec에 기록됨
- [ ] UI/UX가 필요한 프로젝트라면 UI UX Pro Max 디자인 시스템 제안과 사용자 디자인 선택 증거가 존재함
- [ ] Design을 수행했다면 선택한 Design Tokens와 대표 결과의 완료 조건이 고정됨
- [ ] Antigravity 수동 작업 지시서에 수정 범위, 보안 승인, 테스트와 Commit 전 승인 규칙이 포함됨
- [ ] 파일럿으로 사용할 작고 복구 가능한 프로젝트가 지정됨
- [ ] 파일럿 시작 전 기준 Commit 또는 복구 태그가 존재함
- [ ] 구현과 독립 검증을 서로 다른 단계로 수행할 수 있음
- [ ] 사용자에게 실제 화면 또는 실행 결과를 보여줄 방법이 정해짐
- [ ] Target Environment에서 승인된 결과와 동작을 검증할 방법이 정해짐
- [ ] 실패 시 `main`을 훼손하지 않고 되돌릴 수 있음

체크되지 않은 항목을 추측으로 PASS 처리하지 않습니다. 최초 파일럿은 Kernel이나 V2 UI 제작이 아니라 작고 복구 가능한 파일럿 프로젝트의 한 가지 작업을 끝까지 검증하는 것으로 제한합니다.

## 최초 파일럿 Rollback PASS 기준

1. Codex 검증과 사용자 실물 최종 승인 후 프로젝트 `Result Commit A`를 생성합니다.
2. 이전 Commit으로 되돌려 이전 버전의 Build와 실행이 정상인지 확인합니다.
3. `Result Commit A`로 다시 복구합니다.
4. 결과 버전의 Build와 실행이 다시 정상인지 확인합니다.

Rollback과 Restore는 현재 작업 폴더가 아닌 별도 임시 `git worktree`에서 검증합니다. V2 Wiki의 `Base Memory Commit`과 실제 프로젝트의 `Base Project Commit`, `Result Project Commit`을 서로 다른 증거로 기록합니다.

## V2 Core MVP PASS 기준

각 마일스톤은 아래 기술 PASS 기준과 함께 사용자가 직접 수행할 흐름을 제공합니다. 사용자 확인 전에는 해당 항목을 자동 PASS 처리하지 않으며, 기술 검증과 필수 사용자 흐름 확인이 모두 끝나야 마일스톤을 완료로 기록합니다.

### 공통 User Scenario 판정 규칙

- 사용자 확인과 Codex 기술 검증을 별도 결과로 보존합니다.
- V2 Core Commit과 제작 프로젝트 Commit을 분리해 기록합니다. 제작 프로젝트가 없는 M2·M3의 `project_commit_sha`는 `null`입니다.
- 종합 PASS는 현재 Commit 및 Scenario 버전 일치, 필수 `user_result: pass`, `codex_result: pass`를 모두 만족할 때 계산합니다.
- Commit 또는 `scenario_version`이 바뀌면 이전 결과를 삭제하지 않고 `stale`로 표시하고 재검증합니다.
- 실패 후 수정했으면 같은 목적의 Scenario를 새 대상 Commit에서 다시 실행합니다.
- 테스트에는 개인정보 대신 가짜 데이터를 사용합니다.

### M1 — Run·Git 안전 기반

- V2 Run ID가 생성되고 대상 Project, Run 전용 Branch, `Base Memory Commit`과 `Base Project Commit`이 연결됩니다.
- `integrations.spec_kit.workflow_run_id`는 과거 Workflow 증거 호환을 위한 nullable 선택 필드이며 skills 기본 경로에서는 `null`입니다.
- 공식 원격 `origin/main` SHA는 `memory.official_commit`, 현재 로컬 V2 HEAD는 `v2_workspace.head`에 서로 분리되어 기록됩니다.
- `running`, 대기, 실패, 취소와 재개 상태를 실제 Run에서 구분할 수 있습니다.
- 프로세스를 종료하고 다시 실행해도 저장된 Run 상태와 재개점을 읽을 수 있습니다.
- 사용자 작업 폴더와 `main`을 임의로 변경하지 않습니다.
- PASS 증거를 기준으로 `CURRENT_STATE.md` 갱신안을 만들 수 있습니다.

사용자 Scenario는 새 규칙을 소급해 만들지 않습니다. 기존 승인 범위의 CLI·상태 파일 재조회, 재개와 상태 전이는 Codex가 기술적으로 검증합니다.

### M2 — Spec과 승인 Gate (구조 A 전환)

- 공식 검증 Run: `run-05dbfc27`
- ✅ `execution_mode: skills`, `workflow_run_id: null`
- ✅ `speckit-specify` 직접 호출로 `spec.md`와 요구사항 체크리스트 생성
- ✅ 승인 전 `v2 plan` 종료코드 `1`로 차단
- ✅ `v2 spec modify`가 Spec 본문을 실제로 변경하고 Version을 `1 → 2`로 증가시킨 후 승인을 `pending`으로 초기화
- ✅ `v2 spec approve`가 현재 Version `2`만 승인하고 외부 Workflow를 Resume하지 않음
- ✅ 승인만으로 Plan이 자동 시작되지 않음
- ✅ `v2 plan`이 `speckit-plan` Skill을 직접 호출하고 비어 있지 않은 `plan.md`를 같은 Run에 연결
- ✅ 새 프로세스에서 같은 Run을 재조회하고 `git diff --check` 통과

`run-3b0ffae8`은 다른 Agent 변경이 섞인 `diagnostic_failed` 기록이며 M2 PASS 증거가 아닙니다. 다른 기존 실패 Run도 M2 PASS 증거로 사용하지 않습니다.

사용자는 정리된 요구사항의 수정 요청, 승인 전 차단, 승인 후 plan.md 생성 완료를 확인합니다. Codex는 V2 Run 과 생성된 Markdown Artifact 들의 실물 정합성을 검증합니다. Playwright는 사용하지 않습니다.

### M3 — 조건부 Research·Design과 Plan/Tasks

- Research와 Design 필요 여부, 실행 이유와 생략 이유를 사용자에게 보여줍니다.
- 필요하지 않은 조건부 단계는 실행하지 않습니다.
- 조사로 요구사항이 달라지면 Spec 갱신과 재승인을 거칩니다.
- UI/UX가 필요하면 검증된 디자인 도구의 결과와 사용자 선택 증거가 존재합니다.
- 승인된 Spec과 Design을 참조하는 Plan/Tasks가 생성됩니다.
- 사용자가 계획을 승인하기 전에는 Handoff 또는 Implement 단계로 진입하지 않습니다.
- 진행률은 승인된 Task 집합의 검증 완료 수를 기준으로 계산합니다.

사용자는 디자인 선택지와 Plan을 확인하고 승인 또는 수정 요청을 수행합니다. Codex는 선택한 Design 결과가 같은 Run의 Plan과 Tasks에 실제로 연결됐는지 파일과 상태로 검증합니다. Playwright는 사용하지 않습니다.

### M4 — Feature Run 완성

- Antigravity 전달 자료와 회수 결과가 같은 Run ID, Run Branch와 Base Project Commit을 가리킵니다.
- 승인된 Task 범위 밖의 변경이 없는지 Git diff로 확인합니다.
- 구현 결과가 실제 대상 환경에서 실행됩니다.
- Codex가 구현 Agent 보고와 별도로 실행 명령, 종료 코드, 대상 SHA와 산출물 경로가 포함된 검증 증거를 남깁니다.
- 사용자가 실제 결과를 승인한 뒤 Run Branch에 Result Project Commit을 생성합니다.
- 별도 임시 worktree에서 이전 Commit과 Result Commit을 각각 실행해 Rollback/Restore를 확인합니다.
- Result Project Commit의 `main` 반영은 자동 수행하지 않으며 별도 사용자 승인을 요구합니다.
- 실패·취소 시 임시 서버, worktree와 잠금을 정리하고 재개점을 보존합니다.

사용자는 병원 웹의 승인된 핵심 흐름을 직접 사용하고 `통과` 또는 `문제 있음`을 판정합니다. Codex는 기존 브라우저 검증 기능으로 실제 상호작용, Console 오류, Spec 일치와 대상 Commit을 확인합니다. 반복 가치가 확인된 흐름만 추후 Playwright 자동검증 후보로 전환합니다.

### M5 — 얇은 V2 UI

- UI의 Project, Run, 단계, Task, 승인, 검증과 Commit 상태가 실제 Core 상태와 일치합니다.
- 승인과 수정 요청이 실제 V2 Core Gate와 Run 상태에 반영됩니다.
- 웹 프로젝트는 승인된 로컬 개발 서버의 실제 Live Preview와 연결 실패 상태를 표시합니다.
- 새로고침 또는 V2 UI 재시작 후에도 Core의 저장된 상태를 다시 표시합니다.
- UI가 임의 진행률, PASS, 증거 또는 Commit SHA를 생성하지 않습니다.
- 기술 로그를 숨겨도 실패 원인, 사용자 선택과 다음 행동은 확인할 수 있습니다.

사용자는 현황판, 승인·수정 버튼과 Preview를 직접 사용합니다. Codex는 UI 표시가 실제 Core 원본 상태와 일치하는지 기존 브라우저 검증 기능으로 확인합니다. Driver.js는 사용 안내가 실제로 필요할 때만 별도 후보로 검토합니다.

### M6 — Change Run

- 기존 Result Project Commit을 Base Project Commit으로 사용하는 별도 Change Run을 생성합니다.
- 변경 영향 범위와 수행·생략할 단계를 사용자에게 보여주고 승인받습니다.
- 영향받지 않은 Feature Run 전체 단계를 반복하지 않습니다.
- 수정 대상 검증과 승인된 최소 회귀 검증을 통과합니다.
- 기존 Feature Run의 증거를 새 증거처럼 복제하지 않고 Change Run의 새 증거를 남깁니다.
- 새 Result Project Commit과 안전한 Rollback/Restore 증거가 존재합니다.
- `main` 반영은 별도 사용자 승인을 요구합니다.

사용자는 요청한 부분만 바뀌고 기존 기능이 유지되는지 확인합니다. Codex는 영향받는 기존 Scenario를 새 Project Commit에서 재실행하며, 반복 회귀검증이 필요할 때만 제작 프로젝트 단위 Playwright 도입을 검토합니다.

### M7 — MVP E2E

- V2 UI에서 시작한 병원 웹 Feature Run이 실제 결과물과 Result Project Commit까지 완료됩니다.
- V2 UI에서 시작한 예약 버튼 Change Run이 필요한 단계만 실행해 새 Result Project Commit까지 완료됩니다.
- 두 Run 모두 승인 Gate, 독립 검증, 사용자 실물 승인과 Rollback/Restore 증거를 가집니다.
- V2 UI와 Core를 종료한 뒤 새 세션에서 공식 Wiki와 저장된 Run을 다시 읽고 완료 상태와 증거를 동일하게 표시합니다.
- 새 세션에서 완료된 프로젝트를 기준으로 추가 Change Run을 시작할 수 있습니다.
- UI, Core, 제작 프로젝트 Git과 승인된 Wiki 상태가 서로 일치합니다.
- M7 PASS는 `AI OS V2 MVP` 검증을 의미하며 상업 배포·다중 사용자·무인 운영 완료를 의미하지 않습니다.
- 위 항목을 모두 확인한 경우에만 `AI OS V2 MVP = ✅ 검증됨`으로 판정합니다.

사용자는 자연어 요청부터 결과 확인, 저장과 복구까지 전체 흐름을 직접 수행합니다. Codex는 Core와 제작 프로젝트 Commit, E2E 결과, Rollback과 Restore 증거가 모두 같은 Run 기록과 일치하는지 확인합니다.
