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

### Feature Run

- 실제 Spec Kit Workflow Run ID가 존재합니다.
- 사용자 원문, Project, `Base Memory Commit`과 `Base Project Commit`이 같은 Run에 연결됩니다.
- Spec과 Plan 승인 전 다음 단계가 실행되지 않습니다.
- 필요한 경우에만 Research와 Design이 실행됩니다.
- Antigravity 전달·회수 결과가 같은 Run ID를 가리킵니다.
- 구현 Agent 보고와 별도로 Target Environment에서 실제 검증합니다.
- 사용자 최종 승인 후에만 `Result Project Commit`을 만듭니다.
- 별도 worktree에서 이전 Commit과 Result Commit의 실행을 모두 확인합니다.

### Change Run

- 기존 Result Commit을 기준으로 부분 수정 범위를 제안하고 사용자가 승인합니다.
- 영향받지 않은 전체 Feature 단계를 반복하지 않습니다.
- 수정 대상 검증과 필요한 최소 회귀 검증을 수행합니다.
- 새 Result Commit과 안전한 Rollback/Restore 증거를 남깁니다.

### 최종 E2E

M7에서 V2 UI에 입력한 병원 웹 Feature Run과 예약 버튼 Change Run이 실제 Core Workflow를 통해 완료되고 UI 상태가 Core 상태와 일치할 때만 `AI OS V2 MVP = ✅ 검증됨`으로 판정합니다.
