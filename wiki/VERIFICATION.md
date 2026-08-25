# Verification

> Post-MVP 최신 PM0~PM6 PASS 기준은 [[POST_MVP_PM0_PM6_BASELINE]]을 사용합니다. 아래 PM1~PM4 연속 실행 문구는 이전 설계 기록이며 최신 Roadmap을 덮어쓰지 않습니다.

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다. Gate와 완료 판정은 이 표준을 기준으로 검증합니다.

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

#### M3 실제 검증 결과

- ✅ Run ID 유지: `run-05dbfc27`
- ✅ UI UX Pro Max `v2.14.1`과 `frontend-app-builder` 직접 호출 증거 존재
- ✅ Option C v2 모바일 우선 Preview와 Browser 검증 Artifact 존재
- ✅ 기술 검증 PASS와 사용자 `needs_improvement` 판정을 분리 보존
- ✅ M4 파이프라인 시험 승인만 기록하고 상업 디자인·Reference 승인은 `false` 유지
- ✅ Spec Kit `v0.16.1` Codex integration 복구 후 Missing/Modified managed files 0
- ✅ 공식 `speckit-tasks` Skill 호출 1회, 자동 재시도·새 Run·Workflow 사용 없음
- ✅ `tasks.md` T001~T047 순차 생성 및 Spec·Plan·Option C 범위 정합성 확인
- ✅ M4 Handoff의 6개 묶음에 47개 Task 누락 0·중복 0
- ✅ 승인된 Spec·Plan·Preview v1·v2·v3 해시 불변
- ✅ 제작 프로젝트 기준점 Commit: `2554340`

M3 판정은 `✅ 검증됨`입니다. 이후 M4 Handoff를 5개 최소 실행 묶음으로 정리해 실제 구현에 사용했습니다.

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

#### M4 실제 검증 결과

- ✅ Run ID 유지: `run-05dbfc27`
- ✅ 구현 Agent: Antigravity
- ✅ 기준 Project Commit: `25543402bacf1e57dac797a8a66abad4498d97f0`
- ✅ Result Project Commit: `c9703520ff9a7a6ce95f64918ada4ce08160175d`
- ✅ `npm run typecheck`, `npm run build`, `git diff --check`
- ✅ Codex 인앱 Browser에서 390px·430px·1440px, 메뉴·의료진·예약 오류·완료·메인 복귀 검증
- ✅ 애플리케이션 Console 오류와 깨진 이미지 없음
- ✅ 코드에서 외부 전송·브라우저 저장 API 부재, 제출 후 초기화와 새로고침 후 입력 미복원 확인
- ✅ 사용자의 M4 파이프라인 테스트 승인
- ✅ 별도 임시 worktree에서 기준 Commit의 제품 부재와 Result Commit의 설치·Typecheck·Build 재현 확인
- 비차단 이슈: `HERO-01`의 390px 한국어 제목 줄바꿈
- 상업 디자인 승인: `false`
- Reference 승인: `false`

M4 판정은 `✅ 검증됨`이며 다음 단계는 M5입니다.

### M5 — 수집·분석·레시피 선택 Core

#### 현재 검증 상태

- ✅ 자연어 요청 기반 수집·분석: `run-78f0af7d`
- ✅ V2 Core 내부 Codex 호출 1회와 자동 재시도 없음
- ✅ `research.md`, `analysis.md`, `user-summary.md` 생성·비어 있지 않음·출처 URL 확인
- ✅ `recipe_status: researched`, 사용자 확인 전 Preview Gate 차단과 새 프로세스 재조회
- ✅ 사용자 제공 URL·본문·파일 선택 입력과 `analysis_kind: user_provided_source`
- ✅ 임시 Git 격리 작업공간에서 하위 Codex 실행 후 검증된 Artifact만 공식 Run으로 회수
- ✅ 접근 불가 자료의 실제 확인·미확인 범위를 분리하고 `needs_more_source`로 정상 종료: `run-7bc24e97`
- ✅ 자연어 분석 프로필 회귀검증과 기존 `run-78f0af7d` Artifact 해시 불변
- ✅ 사용자 확인 전 Preview Gate 차단, 후보 Wiki 자동 등록 없음, 새 프로세스 재조회
- 전체 판정: `M5 ✅ 검증됨`

- 새 프로젝트 또는 기존 바이브코딩 프로젝트의 실제 파일, 실행 가능 여부, 기존 Artifact·오류·Commit과 설치 도구를 읽습니다.
- 확인한 사실과 확인하지 못한 항목을 구분하고, 화면·기능·데이터·검증·배포 중 부족하거나 깨진 영역을 판정합니다.
- 사용자가 원하는 완료 수준을 확인하고 현재 단계에 맞는 검증된 제작 레시피 하나와 다음 한 작업만 추천합니다.
- 프로젝트 레시피, 내부 역할과 실행 도구를 혼동하지 않으며 설치되지 않은 후보를 적용됨으로 표시하지 않습니다.
- 자동 인터넷 크롤러, 별도 수집 서버·DB, 학습기, Dashboard UI와 새 Multi-Agent를 만들지 않습니다.
- 새 프로세스에서도 같은 입력과 기준 Commit에서 동일한 분석 근거와 추천을 재조회할 수 있습니다.
- 공식 입력은 기존 `test_project`와 PDF 도면 스탬프 자연어 요청입니다.
- PDF.js, pdf-lib, Konva/Fabric.js를 공식 근거·유지관리·모바일 조작·좌표 변환·대용량 PDF 위험 기준으로 비교하고 후보를 최대 2개로 제한합니다.
- 결과에는 `local_product` 목표, 포함·제외 기능과 다음 실행 작업 하나가 명시되며 패키지 설치와 PDF 구현은 발생하지 않습니다.

사용자는 분석 결과의 쉬운 요약과 `[추천대로 진행]` 또는 `[직접 선택]`만 확인합니다. Codex는 추천이 실제 프로젝트 상태와 공식 근거에 연결되는지 검증합니다.

### M6 — 기존 프로젝트 Change Run

- 기존 Result Project Commit 또는 가져온 기존 프로젝트의 확인된 Commit을 Base Project Commit으로 사용하는 Change Run을 생성합니다.
- 부족한 영역 하나와 변경 영향 범위를 식별하고 필요한 단계만 실행하며 전체 Feature Run을 반복하지 않습니다.
- 요청한 부분 수정과 영향받는 기존 기능의 최소 회귀 검증을 통과합니다.
- 기존 증거를 새 증거처럼 복제하지 않고 현재 대상 Commit의 새 증거를 남깁니다.
- 사용자 확인 뒤 새 Result Project Commit과 별도 worktree Rollback/Restore 증거를 만듭니다.
- `main` 반영은 별도 사용자 승인을 요구합니다.

사용자는 요청한 부분만 바뀌고 기존 기능이 유지되는지 확인합니다. Codex는 변경 전후 Commit, 영향 범위와 회귀 결과를 독립 검증합니다.

공식 검증 대상은 병원 프로젝트 `HERO-01`의 390px·430px 모바일 한국어 줄바꿈입니다. 해당 영역만 수정하고 메뉴·예약·완료 흐름을 회귀검증합니다. PDF 기능은 M6에서 구현하지 않습니다.

검증 결과: `run-fa8b4386`에서 Quick Change 분기, `HERO-01` 국소 CSS 수정, 390px·430px 단어 내부 분리 방지, 1440px 회귀 없음, 메뉴·의료진·예약 오류·완료·복귀, Typecheck·Build·Diff, 사용자 `pass`, Result Commit `e2625bb`, 기준/결과 Commit의 별도 worktree Rollback·Restore를 모두 확인했습니다. `partial_change_by_ai: pass`이며 직접 시각 편집 패널은 M6 범위 밖입니다.

### M7 — PDF 도면 스탬프 MVP E2E

- PDF 도면 스탬프 자연어 요청으로 시작하고 M5에서 선택한 레시피와 실제 사용 도구가 일치합니다.
- 실제 상태 수집, 부족한 부분 분석, 레시피 선택, 조건부 디자인, 계획, 구현, 독립 검증과 사용자 확인을 한 Run 계보에서 완료합니다.
- 모바일에서 실제 PDF 한 페이지를 표시하고 스탬프 한 종류를 터치로 배치·이동·크기 조절할 수 있습니다.
- 원본 PDF는 불변이며 좌표가 맞게 반영된 새 PDF를 다운로드할 수 있습니다.
- 사용자에게는 한 번에 질문 하나와 쉬운 선택지만 제공하며 내부 Run·SHA·도구 선택은 기본 흐름에서 숨깁니다.
- 작업을 중단하고 새 프로세스에서 같은 공식 기억, Run과 재개점을 불러와 이어서 완료할 수 있습니다.
- Result Commit 생성 후 별도 worktree에서 Rollback/Restore를 재현합니다.
- Core, 제작 프로젝트 Git과 승인된 Wiki 상태가 서로 일치하며 Dashboard UI 없이도 전체 사이클이 성립합니다.
- M7 PASS는 `AI OS V2 Core MVP` 검증을 의미하며 상업 배포·다중 사용자·무인 운영·학습기·Dashboard 완료를 의미하지 않습니다.
- 위 항목을 모두 확인한 경우에만 `AI OS V2 Core MVP = ✅ 검증됨`으로 판정합니다.

사용자는 말하기, 추천 선택, 실제 결과 확인과 수정·완료 판단만 수행합니다. Codex는 Run, Artifact, Commit, E2E와 복구 증거의 정합성을 확인합니다.

M7에서는 로그인, Backend, 클라우드 저장, 다중 사용자, 서명 인증, OCR, 기존 PDF 문장 편집, 복잡한 도면 측정과 실제 배포를 제외합니다.

#### M7 실제 검증 결과

- ✅ 공식 Run ID: `run-c0a968f3`
- ✅ 구현 Agent: Antigravity
- ✅ 구현 라이브러리: `pdfjs-dist` (PDF 한 페이지 표시 및 썸네일바 생성용), `pdf-lib` (좌표 변환 및 새 PDF 다운로드용)
- ✅ 모바일 반응형 뷰포트(390px, 430px) 및 PC(1440px) 가로 넘침 차단 및 시인성(텍스트 15~20% 스케일링) 최적화 완료
- ✅ 퀵 문자 프리셋 동적 관리(`localStorage` 영구 보존, Rename/Delete 분리), 도면 여백 클릭 시 선택 해제, 스탬프 선택 시 dashed blue bounding box 활성화 시각 표시 검증 완료
- ✅ 우측 속성 설정 패널 340px 및 상시 노출(선택 유무에 따라 사전 설정으로 자동 분기 변경) 검증 완료
- ✅ 최초 공식 intake 입력(1페이지) SHA256: `c5573243ac74e0ad0ea4170e6289e571056f1faf189ea477c8e987442a58d20e`
- ✅ 다중 페이지 최종 검증 입력(2페이지) SHA256: `bb59d68049892ad24f5442f138c4098aacea37ad33ac8644d83ffd05a888927e`
- ✅ 기호 합성 출력(2페이지) SHA256: `d40efdb91344c6c1a75f19049e39c92c980504ffd6d590871308bde81e699e44`
- ✅ SHA 차이는 원본 변조가 아니라 1페이지 intake 입력과 별도로 생성한 2페이지 검증 입력 및 새 출력 PDF의 역할 차이에서 발생합니다.
- ✅ `npx tsc --noEmit` & `npm run lint` & `npm run build` 모두 성공 (종료코드 0)
- ✅ PDF.js Worker가 입력 버퍼를 분리하는 오류를 `App.tsx`의 렌더링용·내보내기용 `ArrayBuffer` 복사로 국소 수정했습니다.
- ✅ 제품 Result Commit `3b592c8`; 별도 worktree에서 기준 Commit과 Result Commit Build 및 Rollback/Restore PASS
- ✅ 사용자의 최종 확인 PASS

M7 판정은 `✅ 검증됨`이며, 이에 따라 V2 Core MVP 검증이 공식적으로 통과되었습니다.

### POST-MVP 연속 실행

#### PM1~PM6 결정 흐름 검증 계약

- PM5 인터뷰·Spec Lite/Full·Scope Lock 없이 새 제작 또는 범위 확장 구현을 시작하지 않습니다.
- PM4는 기존 Recipe·DNA·Block·Skill을 먼저 검색하고 부족할 때만 외부 조사합니다.
- PM1은 같은 목적·데이터·Viewport에서 구조적으로 다른 낮은 비용의 방향 3개를 보여주고, 선택된 후보·부분에서만 7축 Design DNA를 추출합니다.
- 완성 Code Preview와 Visual Target은 선택 조합 하나만 제작하며 사용자가 디자인을 승인하기 전 구현하지 않습니다.
- 승인 Design Recipe의 Reference·DNA·Section·Component·Hash가 Antigravity Handoff와 실제 결과까지 이어지는지 확인합니다.
- PM3 편집은 마우스 이동·Inline/Panel 글자·자유 Resize·이미지 교체/크기·Viewport Override를 같은 Recipe Diff에 기록하고 Core 승인·Version·Restore를 우회하지 않습니다.
- PM6은 디자인 방향을 새로 결정하지 않고 Intent→조사→방향 선택→DNA→Visual Target→Recipe→구현→부분 수정→마감→최종 승인→복구의 증거 계보를 재검증합니다.
- PM3의 사용자 조건부 통과는 기술 완료가 아니며 실제 고객 결과물·390/430·Undo·Draft 폐기·원본 보존·프로젝트 격리·접근성·회귀를 PM6에서 다시 확인합니다.

- M7 PASS 후 `wiki/POST_MVP_ROADMAP.md`를 실제로 읽고 첫 미검증 후보 `direct_partial_edit_panel`을 선택합니다. `web_camera_capture`는 기능 후보로 유지합니다.
- 기존 레시피·설치 도구·공식 문서·GitHub 사례를 조사하고 구현 가능성·위험·다음 선택지를 기록합니다.
- 사용자에게 `[진행]`, `[나중에]`, `[다른 후보 보기]`를 제시하지만 구현을 자동 시작하지 않습니다.
- 외부 설치·기존 제품 변경·실제 데이터·권한·DB·배포·삭제는 Gate 없이 실행되지 않습니다.
- 후보가 실제 환경 검증, 사용자 확인, Commit과 Rollback/Restore를 통과하기 전에는 `verified` 또는 `reusable_recipe`가 될 수 없습니다.

### 이전 PM1 최소 조립식 기반·Hybrid H Gate

- [ ] 병원 웹과 PDF 프로젝트가 정적 Project Registry로 각각 열림
- [ ] PDF Module 비활성화 후에도 Core와 병원 웹이 정상 동작함
- [ ] 잘못된 Module Manifest가 해당 Module에만 격리됨
- [ ] Module 복구 후 기존 Artifact를 재사용할 수 있음
- [ ] 새 프로젝트 등록과 Design Recipe 교체가 Run·Gate·Rollback 경계를 우회하지 않음
- [ ] 화면·핵심 상태별 승인 `visual_target`과 SHA256이 존재함
- [ ] Image-to-Code 입력과 도구 실행 증거가 존재함
- [ ] `1440×950`, `430px`, `390px` 동일 Viewport Fidelity가 PASS함
- [ ] Fidelity PASS 이후에만 코드가 `design_source_of_truth`로 승격됨

`run-ef4986d7` Preview v1은 기능적 상호작용과 반응형 구조는 통과했지만 시각 충실도는 실패했습니다. Artifact는 `rejected_visual_fidelity` 증거로 보존하며 PM1 구현 입력으로 사용할 수 없습니다.
