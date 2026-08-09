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

### M1 — Run·Git 안전 기반

- 실제 Spec Kit Workflow Run ID가 생성됩니다.
- 대상 Project, Run 전용 Branch, `Base Memory Commit`과 `Base Project Commit`이 연결됩니다.
- `running`, 대기, 실패, 취소와 재개 상태를 실제 Run에서 구분할 수 있습니다.
- 사용자 작업 폴더와 `main`을 임의로 변경하지 않습니다.
- PASS 증거를 기준으로 `CURRENT_STATE.md` 갱신안을 만들 수 있고 Obsidian에서 로컬 변경을 확인할 수 있습니다.

### M2 — Spec과 승인 Gate

- 사용자의 자연어 원문으로 실제 Spec Kit Specify/Clarify 산출물을 생성합니다.
- Spec과 완료 조건이 같은 Run ID에 연결됩니다.
- 사용자 승인 전 Plan이 실행되지 않습니다.
- 승인 후 새 Run을 만들지 않고 기존 Run을 Resume합니다.

### M3 — 조건부 Design과 Plan/Tasks

- Research와 Design 필요 여부를 판정하고 사용자에게 범위를 보여줍니다.
- 필요하지 않은 조건부 단계는 실행하지 않습니다.
- UI/UX가 필요하면 검증된 디자인 도구의 결과와 사용자 선택 증거가 존재합니다.
- 승인된 Spec과 Design을 참조하는 Plan/Tasks가 생성됩니다.
- 진행 상태는 실제 승인된 Tasks 수와 검증 완료 수를 사용합니다.

### M4 — Feature Run 완성

- Antigravity 전달 자료와 회수 결과가 같은 Run ID와 Base Project Commit을 가리킵니다.
- 구현 결과가 실제 대상 환경에서 실행됩니다.
- Codex가 구현 Agent 보고와 별도로 검증 증거를 남깁니다.
- 사용자 실물 승인 후에만 Result Project Commit을 생성합니다.
- 별도 임시 worktree에서 이전 Commit과 Result Commit을 각각 실행해 Rollback/Restore를 확인합니다.

### M5 — 얇은 V2 UI

- UI의 Project, Run, 단계, Task, 승인, 검증과 Commit 상태가 실제 Core 상태와 일치합니다.
- 승인과 수정 요청이 실제 Workflow Gate와 Run 상태에 반영됩니다.
- 웹 프로젝트는 승인된 로컬 개발 서버의 실제 Live Preview를 표시합니다.
- UI가 임의 진행률, PASS 또는 Commit SHA를 생성하지 않습니다.

### M6 — Change Run

- 기존 Result Project Commit에서 별도 Change Run을 생성합니다.
- 변경 영향 범위를 사용자에게 보여주고 승인받습니다.
- 영향받지 않은 Feature Run 전체 단계를 반복하지 않습니다.
- 수정 대상 검증과 필요한 최소 회귀 검증을 통과합니다.
- 새 Result Project Commit과 안전한 Rollback/Restore 증거가 존재합니다.

### M7 — MVP E2E

- V2 UI에서 시작한 병원 웹 Feature Run이 실제 결과물과 Commit까지 완료됩니다.
- V2 UI에서 시작한 예약 버튼 Change Run이 필요한 단계만 실행해 새 Commit까지 완료됩니다.
- 두 Run 모두 승인 Gate, 독립 검증, 사용자 실물 승인과 Rollback/Restore 증거를 가집니다.
- UI, Core, 제작 프로젝트 Git과 승인된 Wiki 상태가 서로 일치합니다.
- 위 항목을 모두 확인한 경우에만 `AI OS V2 MVP = ✅ 검증됨`으로 판정합니다.
