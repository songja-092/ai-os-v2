# Decisions

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다. 이 문서와 충돌하면 표준 흐름을 우선하고 충돌을 보고합니다.

- GitHub 저장소와 Git commit을 공식 기록으로 사용합니다.
- Obsidian은 Wiki를 읽고 편집하는 인터페이스로 사용합니다.
- Archify 결과는 Source of Truth가 아닌 commit 기반 파생 시각화로 취급합니다.
- 연결 검증이 끝나기 전까지 V2 기능을 개발하지 않습니다.

## 조립 우선 원칙

AI OS V2는 개발 기능을 새로 만드는 OS가 아니라, 검증된 기존 도구·오픈소스·Skill·MCP·서비스를 조립하여 개발자 역할을 수행하게 만드는 OS로 설계합니다. 직접 구현은 적합한 기존 대안이 없을 때만 최소한으로 합니다.

기능마다 부품 종류의 우선순위를 미리 고정하지 않고 다음 순서로 판단합니다.

`필요한 기능 → 기존 제품·오픈소스·Skill·MCP 조사 → 실제 검증 → 채택 또는 탈락 → 부족한 연결부만 최소 제작`

## 프로젝트 완성 OS와 사용자 경험

- 📝 승인됨: V2는 웹사이트 제작기에 한정하지 않고, 초보자가 자연어 요청 또는 기존 바이브코딩 프로젝트를 입력하면 부족한 부분을 분석해 디자인·기능·검증·복구·유지보수까지 이어 주는 `프로젝트 완성 OS`를 목표로 합니다.
- 사용자에게 보이는 기본 흐름은 `원하는 것을 말한다 → 추천 결과 또는 시안을 고른다 → 실제 결과를 확인하고 완료 또는 수정을 말한다` 세 단계입니다.
- Run ID, Commit SHA, 기술 스택, Spec·Plan·Tasks, Skill·Plugin·MCP 선택, Git 명령, 로그와 Agent 역할은 기본 화면에서 숨기고 필요할 때만 `자세히 보기`로 제공합니다.
- 사용자에게는 한 번에 질문 하나만 제시합니다. 디자인·결과 방향, 데이터 저장, 위험 권한, 실제 배포와 최종 결과 판정만 질문하고 Framework, 도구, 경로, Git과 기술적 복구 방법은 내부에서 결정합니다.
- 기본 선택지는 가능한 경우 `[추천대로 진행]`과 `[직접 선택]`으로 통일합니다.

## 수집·분석·레시피 경계

- 프로젝트 레시피, 내부 작업 역할과 실행 도구를 구분합니다. 전자명함·소개 웹·캘린더 같은 유형마다 별도 Agent를 만들지 않습니다.
- 수집기는 사용자 원문, 실제 프로젝트 파일과 실행 상태, 기존 Artifact·오류·Commit, 설치된 도구와 공식 성공사례를 모으는 내부 기능입니다. MVP에는 자동 크롤러, 별도 수집 서버와 DB를 만들지 않습니다.
- 분석기는 수집된 사실에서 `현재 가능한 것`, `부족하거나 깨진 것`, `원하는 완료 수준`, `적합한 레시피`, `다음 한 작업`만 판정합니다. 학습기와 자동 Pattern Library는 MVP 이후 후보입니다.
- 완료 수준은 내부적으로 `prototype → local_product → data_product → deployable → deployed`로 구분하되, 사용자에게는 `화면 확인`, `내 컴퓨터에서 사용`, `데이터 저장`, `실제 배포`처럼 설명합니다.
- M5 이후 완료 수준 표기는 `preview`, `local_product`, `deployable_candidate`, `deployed_product` 네 단계로 단순화하며 M5는 앞의 두 단계만 제안합니다.
- 레시피 검색 우선순위는 `V2 검증 레시피 → 설치·검증된 기능 → 공식 표준·도구 → 유지관리되는 GitHub OSS → 검증된 실제 사례 → 얇은 연결 코드 → 자체 신규 구현`입니다.
- 분석 결과는 최소 기능·제외 범위, 후보 레시피 최대 2개, 모바일·데이터·권한·개인정보 위험, 예상 실패점, Preview와 검증 시나리오 및 다음 한 작업을 포함합니다.

## MVP 이후 연속 실행과 안전 Gate

- M7 PASS 후 V2는 `wiki/POST_MVP_ROADMAP.md`를 읽고 다음 미검증 후보 하나의 상태 조회, 공식 자료 수집, 분석과 추천 보고서 준비까지 이어갑니다.
- 읽기 전용 저장소·상태 확인, 공식 문서·GitHub 조사, 기존 레시피 검색과 분석 보고는 사용자 승인 없이 허용합니다.
- 기존 자료를 건드리지 않는 임시 디렉터리·새 Preview Version·가짜 데이터 기반의 가역적 파일럿만 자동 후보가 될 수 있으며 자동 재시도하지 않습니다.
- 외부 패키지 설치, 기존 제품 변경, 실제 데이터, 로그인·권한·DB·개인정보·결제·배포·비밀키·삭제·마이그레이션은 반드시 사용자 승인 후 진행합니다.
- 후보 상태는 `proposed`, `researched`, `pilot_ready`, `implemented`, `verified`, `reusable_recipe`, `deferred`, `rejected` 중 하나만 사용합니다.
- `reusable_recipe`는 실제 프로젝트·환경 실행, 실패 처리, 사용자 확인, Commit과 Rollback/Restore를 모두 통과해야 합니다.
- 별도 학습 모델·Vector DB·Fine-tuning은 만들지 않고 검증 Run의 성공·실패 이유와 Recipe 상태를 기록 기반 학습으로 먼저 재사용합니다.

## 검증된 제작 레시피 후보

- 현재 설치된 Product Design의 `ideate`, `image-to-code`, `audit` 및 `frontend-app-builder`를 디자인 탐색·Preview·구현의 우선 재사용 경로로 둡니다.
- `Leonxlnx/taste-skill`의 `imagegen-frontend-web`, `image-to-code`, `stitch-design-taste`는 이미지 우선 디자인과 Taste 규칙을 제공하는 미설치 후보입니다. v2는 실험 버전으로 표시되어 있으므로 실제 도입 시 안정 버전과 다시 비교합니다.
- Google Labs의 `stitch-skills`는 Stitch MCP, 디자인 변형과 `DESIGN.md` 추출·반복 흐름을 제공하는 미설치 후보입니다. Figma는 이 공식 흐름의 필수 구성으로 확정하지 않습니다.
- Supabase 공식 Auth·Postgres·CRUD·RLS·Migration·Testing·Production Checklist 흐름은 데이터가 필요한 프로젝트의 조건부 Full-stack 레시피 후보입니다. 현재 병원 파일럿에는 적용하지 않습니다.
- 후보의 라이선스 최종 판정은 배포 직전에 수행합니다. 그 전에는 이름, 공식 출처, 확인 버전과 채택 상태를 기록하며 `설치 가능`, `설치됨`, `호출됨`, `검증됨`을 구분합니다.

## Spec Kit 도입

- 📝 승인됨: 자연어 요구사항을 구조화하는 기본 절차로 GitHub Spec Kit을 채택합니다.
- 사용자에게 보이는 기본 절차는 `Specify/Clarify → 요구사항 승인 → Plan/Tasks → 계획 승인 → Implement`로 사용합니다.
- `Analyze`, `Converge` 등은 필요할 때 사용하는 내부 검증 수단이며 사용자 흐름의 고정 단계로 만들지 않습니다.
- Spec Kit `v0.16.1` 기반과 Codex 통합을 사용합니다. M2 기본 경로는 Spec Kit Workflow가 아니라 공식 Skill과 Artifact 형식을 직접 재사용합니다.
- Codex를 현재 Spec Kit 기본 통합으로 사용합니다.
- Antigravity는 Spec Kit을 직접 실행할 필요 없이 승인된 Markdown 산출물과 Codex 작업 지시서를 전달받아 수동으로 구현합니다.
- 도입 전 복구 기준은 Git 태그 `rollback/before-spec-kit-20260809`입니다.

## V1 사용 경계

- 기존 `/home/user/바탕화면/ai_os`는 요구사항, UX 흐름과 실패 원인을 분석하는 참고 자료로만 사용합니다.
- V1의 Kernel, Collector, Truth Guard, UI와 테스트 코드는 V2로 자동 이식하지 않습니다.
- V1에 존재한다는 사실만으로 V2에 적용되었거나 검증된 것으로 기록하지 않습니다.

## Agent 역할과 권한

- 웹 ChatGPT는 아이디어 조사와 정리를 담당하며 구현 완료를 판정하지 않습니다.
- V2 Core는 Run, Gate와 상태를 소유하는 유일한 Orchestrator입니다. 사용자 표시명 `Zeus`는 V2 Core를 가리키며 별도 AI 모델이 아닙니다.
- Codex는 내부 설정, Core, Run, Gate, Git, Skill 연결, 저장소 기반 설계와 기술 검증을 담당합니다.
- Antigravity는 승인된 지시서를 기준으로 실제 웹·앱·화면·기능을 구현하며 M4 전까지 V2 내부 작업에서 대기합니다.
- 동일 Run에는 한 번에 쓰기 담당자 한 명만 허용합니다.
- Antigravity의 파일 변경, 명령 실행, 설치, 외부 연결, 배포 및 Commit은 사용자가 범위를 확인할 수 있어야 합니다.
- V2는 특정 구현 Agent에 종속되지 않으며 Antigravity를 Codex 또는 다른 Agent로 교체할 수 있는 Markdown 작업 지시서를 사용합니다.

## 저장과 복구

- 사용자에게 보이는 `저장`의 공식 의미는 승인된 변경의 Git Commit입니다.
- 새 부품을 도입하기 전 기준 Commit 또는 복구 태그를 남깁니다.
- 파일럿은 별도 브랜치에서 수행하고 검증 실패 시 `main`을 변경하지 않습니다.
- AI OS V2 Wiki의 확정 SHA를 `Base Memory Commit`으로 기록하고, 실제 프로젝트 구현 결과의 `Result Commit`과 구분합니다.
- 실제 프로젝트의 Result Commit은 Codex 검증과 사용자 실물 최종 승인 이후에만 생성합니다.
- Rollback 시험은 `Result Commit → 이전 Commit 정상 확인 → Result Commit 복구 → 결과 재실행 확인`까지 수행합니다.

## 디자인 파일럿

- 📝 승인됨: UI UX Pro Max를 디자인 단계 핵심 파일럿 부품으로 채택합니다.
- 디자인은 UI/UX가 필요한 프로젝트에서만 거치는 조건부 단계입니다.
- 디자인 단계는 특정 도구에 종속되지 않습니다. 현재 기본 파일럿 부품은 UI UX Pro Max이며, 향후 검증된 Skill·오픈소스·MCP로 추가하거나 교체할 수 있습니다.
- UI UX Pro Max는 디자인 스타일, 색상, 글꼴, 레이아웃과 UX 규칙을 제안하며 최종 디자인을 결정하지 않습니다.
- 사용자가 디자인 결과를 직접 확인하고 선택하기 전에는 구현 단계로 넘어가지 않습니다.
- 최초 도입은 별도 브랜치, 고정 버전과 도입 전 복구점으로 수행합니다.
- Antigravity는 승인된 디자인 결과와 Codex 작업 지시서를 전달받아 수동으로 구현합니다.

## 대상 환경과 검증

- 각 프로젝트의 Spec에서 `Target Environment`를 먼저 확정합니다.
- 대상 환경은 Web, Android, iOS, Desktop, CLI, API, Server 또는 기타가 될 수 있습니다.
- Design과 Verification 도구는 Target Environment에 맞게 조건부로 선택합니다.
- Playwright는 웹 프로젝트의 검증 후보이며 V2 전체의 고정 테스트 엔진이 아닙니다.

## 사용자 흐름 검증

- 📝 승인됨: 마일스톤마다 `V2 User Scenario — Given/When/Then 방식`으로 사용자가 직접 확인할 흐름과 Codex 기술 검증을 분리해 기록합니다. Cucumber와 별도 테스트 플랫폼은 설치하지 않습니다.
- `user_result`는 사용자만 판정하고 `codex_result`는 Codex가 실제 기술 증거를 확인한 뒤 기록합니다. Codex와 V2 Core는 사용자 판정을 대신하지 않습니다.
- Scenario 대상은 V2 Core의 `core_commit_sha`와 제작 프로젝트의 `project_commit_sha`를 분리합니다. 제작 프로젝트가 없는 M2·M3에서는 `project_commit_sha: null`을 허용합니다.
- 종합 상태는 별도 원본 값으로 저장하지 않고 현재 Commit, `scenario_version`, `user_result`, `codex_result`에서 계산합니다. Commit 또는 Scenario 버전이 바뀌면 이전 PASS는 삭제하지 않고 `stale`로 표시해 재검증합니다.
- M2·M3에서는 V2 Core Gate와 Artifact를 검증하고 Playwright를 사용하지 않습니다. M4 이후 웹 프로젝트에서 먼저 기존 Codex 브라우저 검증 기능을 사용하며, 반복 자동검증 가치가 확인될 때만 해당 제작 프로젝트에 Playwright를 검토합니다.
- Playwright Codegen은 테스트 초안에만 사용하며 생성 결과 자체를 PASS 증거로 사용하지 않습니다. 외부 `webapp-testing` Skill은 현재 Codex 기능과 중복되므로 설치하지 않습니다.

## V2 Core와 Run

- ✅ 검증됨: V2 Core(Zeus)는 AI 모델이나 새 Kernel이 아니라 Run, Gate, 상태, 결과 참조와 Git 복구점을 소유하는 유일한 Orchestrator입니다.
- Spec Kit은 공식 Skill과 Artifact 형식을 제공하며 Run이나 Gate 상태를 소유하지 않습니다. Spec Kit Workflow는 M2 기본 실행 경로에서 제외합니다.
- `workflow_run_id`는 과거 증거 호환을 위한 nullable 선택 필드입니다.
- 첫 MVP는 `Feature Run`과 `Change Run` 두 종류 및 활성 Run 하나만 지원합니다.
- Run에는 Spec·Design·Plan 본문을 복제하지 않고 실제 산출물 경로와 Commit SHA를 참조합니다.
- `Base Memory Commit`, `Base Project Commit`, `Result Project Commit`, 검증된 Run을 Wiki에 반영한 `V2 State Commit`을 구분합니다.
- 외부 AI 유료 API는 MVP 필수 조건으로 사용하지 않습니다. 기존 도구의 로컬 CLI, 파일과 프로세스 연결은 허용합니다.

## Manual Agent Adapter

- Antigravity 자동 호출은 현재 검증되지 않았으므로 초기 V2는 수동 전달을 공식 상태로 지원합니다.
- 전달 자료에는 Run ID, 프로젝트 경로, 작업 Branch, Base Project Commit, 승인된 Tasks, 수정 허용·금지 범위, 허용 명령과 검증 방법을 포함합니다.
- 회수 자료에는 Run ID, 변경 파일, 실행 명령과 결과, 미해결 문제와 Git diff를 포함합니다.
- Antigravity 보고만으로 Task를 `✅ 검증됨`으로 바꾸지 않습니다.

## UI와 복구 안전

- M1~M4에서는 전용 V2 UI를 구현하지 않고 Spec Kit 상태와 Obsidian의 Run 기록으로 Core를 검증합니다.
- Dashboard UI는 Core MVP 이후 후보입니다. 먼저 M5~M7에서 수집·분석·레시피 선택, Change Run과 전체 제작 사이클을 실제 상태로 검증합니다.
- MVP 웹 Preview는 사용자가 승인한 `localhost` 또는 `127.0.0.1` 개발 서버 하나만 지원합니다. Phone·Tablet·Desktop 전환은 MVP 범위에서 제외합니다.
- Rollback/Restore 검증은 사용자의 현재 작업 폴더를 변경하지 않도록 별도 임시 `git worktree`에서 수행합니다.
- 마일스톤 진행 중 임시 상태를 Wiki의 확정 사실로 자동 저장하지 않습니다. 실제 PASS 증거가 생기면 V2 Core가 `CURRENT_STATE.md` 갱신안을 만들고, 사용자 승인 후 Commit/Push하여 공식 기억으로 확정합니다.
- Obsidian은 V2 저장소의 동일한 Wiki 파일을 Vault에서 읽으므로 별도 동기화 프로그램 없이 로컬 변경을 즉시 표시합니다. GitHub와 Archify 반영은 각각 Push와 별도 갱신 검증 후 확정합니다.
- 실제 Run·Gate·Task 상태는 V2 Core, 기술 검증 결과와 증거는 Codex, 사용자 확인 결과는 사용자가 소유합니다. 현황판은 이 원본을 읽어 표시하며 승인 없이 상태를 만들거나 변경하지 않습니다.
- Sandbox·권한·외부 연결·설치·배포처럼 위험하거나 되돌리기 어려운 행동은 사용자 승인을 요구합니다. 자동 검토가 가능한 변경도 실제 검증과 Git 복구점 없이 완료로 확정하지 않습니다.

## UI·관리자 화면 제작 후보

- 📝 승인됨: `shadcn/ui`, `Storybook`, `Refine`을 조건부 제작 후보로 등록합니다. 세 후보 모두 현재 미설치·미구현·미검증이며 현재 마일스톤 상태를 변경하지 않습니다.
- `shadcn/ui`는 사용자 디자인 승인 후 Button, Input, Form, Dialog, Calendar 등 승인된 화면에 필요한 부품만 실제 프로젝트 코드로 가져와 조립하는 웹 UI 1순위 후보입니다. 전체 세트를 미리 설치하지 않고 프로젝트 기술 스택과 라이선스가 맞을 때 M3 설계 결과 및 M4 작은 화면에서 검증합니다.
- `Storybook`은 공용 UI 부품을 완성 웹과 분리해 상태별로 확인하는 작업대 후보입니다. M4 병원 웹에서는 보류하며, 여러 프로젝트가 부품을 재사용하거나 로딩·오류·빈 상태 등 상태 조합 관리가 어려워질 때 재검토합니다.
- `Refine`은 예약·회원·상품·주문처럼 실제 데이터의 목록·검색·추가·수정·삭제가 필요한 관리자·CRUD 화면 1순위 후보입니다. 일반 사용자 화면 제작 도구로 사용하지 않으며 데이터 저장 방식과 관리자 요구사항이 먼저 승인된 프로젝트에서만 검증합니다.
- 한 번에 하나의 후보만 작은 실제 화면에서 시험하며 기존 방식보다 명확한 효용이 증명될 때만 기본 부품으로 승격합니다. 효용이 없거나 충돌하면 제거하고 도입 전 Git 복구점으로 돌아갑니다.
- Galaxy Preview가 실제 설치·검증되기 전에는 실제 기기 확인을 이 후보들의 필수 PASS 조건으로 만들지 않습니다.

## 직접 부분 수정 패널 후보

- 💡 MVP 이후 최우선 UI 후보: `Direct Partial Edit Panel`입니다. M7 완료 전에는 구현하거나 패키지를 설치하지 않습니다.
- 검증된 기반은 안정적인 영역 라벨 `HERO-01`, M6 AI 부분 수정, 변경 범위 제한, 회귀검증, Commit과 Rollback/Restore입니다. AI 부분 수정과 사용자의 직접 시각 편집을 같은 기능으로 기록하지 않습니다.
- 첫 파일럿은 `HERO-01` 하나에서 글자 크기, 콘텐츠 폭, 자연스러운 줄바꿈과 배경색만 조절합니다. 버튼은 `원래대로`, `미리보기`, `적용`으로 제한합니다.
- 직접 조절은 글자·색상·간격·모서리·그림자와 제한된 움직임 설정, AI 수정은 메뉴 구조·섹션 순서·카드 정보 순서·반응형 구조, 새 Change Run은 새 화면·기능·로그인·저장·관리자·결제를 담당합니다.
- 기술 파일럿 1순위 후보는 `Tweakpane`이며 미설치·미구현·미검증입니다. `AutoAnimate`, `React Grab`, `Agentation`은 조건부 후보이고 `Puck`, Drag & Drop, 자유 Resize와 범용 페이지 편집기는 보류합니다.
- 자유 CSS 입력은 금지하고 허용된 CSS 변수 또는 제한 설정값만 사용합니다. 적용 전 Version을 보존하고 390px·430px·1440px, 가로 넘침과 Console을 검증하며 실패 시 원본을 유지합니다.

## 실제 Galaxy Preview 후보

- 📝 승인됨: 웹/PWA 구현 결과를 실제 Galaxy에서 확인하는 선택형 Verification Adapter를 후속 후보로 둡니다. 현재는 미설치·미구현·미검증입니다.
- 1차 후보 조합은 `scrcpy + adb reverse + Chrome DevTools Remote Debugging`입니다. scrcpy는 실제 기기 화면과 PC 제어, Chrome DevTools는 DOM·Console·Network 검증을 담당합니다.
- 최초 도입은 V2 내부 화면 삽입이 아니라 별도 scrcpy 창을 사용합니다. Tango/ya-webadb 기반 내부 패널은 반복 필요성이 실제로 확인될 때만 후속 검토합니다.
- M1·M2·M3 범위에는 포함하지 않습니다. M4에서 실제 웹 결과물이 생긴 뒤 별도 기술 실험을 수행하고, 성공한 외부 실행 방식만 M5 Preview 선택지와 M7 실기기 승인 검증 후보로 사용합니다.
- 최초 대상은 웹/PWA로 제한하며 Android 네이티브 앱 지원은 실제 요구가 생길 때 별도 판단합니다.
- USB 연결과 `adb reverse`를 기본으로 검토하고, Vite 개발 서버의 LAN 공개 및 무선 ADB 외부 노출은 기본값으로 사용하지 않습니다.
- 연결 실패 시 기존 Mock Preview를 계속 사용할 수 있어야 하며, 설치·연결 실험이 PASS되기 전에는 V2에 적용된 것으로 기록하지 않습니다.

## Ponytail 파일럿

- 📝 승인됨: 불필요한 코드와 의존성을 줄이는 구현 규칙으로 Ponytail을 파일럿 채택합니다.
- 첫 적용 수준은 `lite`이며 프로젝트마다 필요성을 다시 판단할 수 있습니다.
- 판단 순서는 `필요성 → 기존 코드 → 표준 라이브러리 → 플랫폼 기본 기능 → 설치된 의존성 → 최소 코드`입니다.
- 최소화를 이유로 입력 검증, 데이터 손실 방지 오류 처리, 보안, 접근성, 사용자가 승인한 요구사항과 필요한 실행 검증을 생략하지 않습니다.
- Ponytail 제작자의 LOC·토큰·비용·시간 벤치마크는 참고자료이며 V2의 독립 검증 결과가 아닙니다.
- 공식 저장소 Commit `2ed6c52c9d7e5e56942508591085fd45dea277d3`을 고정해 `main`에 설치했으며 실제 Task 품질은 M4에서 검증합니다.
- 도입 전 복구 기준은 `main` Commit `c53a10e6e29da2b270d3cde1df532035efcb4722`입니다.

## 모바일 우선 제작 원칙 (Mobile-First Principle)

- 📝 승인됨: UI 및 레이아웃을 개발할 때는 항상 **모바일 화면 규격(예: 390px, 430px)을 최우선 기준으로 먼저 설계하고 제작**합니다. PC/데스크톱 규격(예: 1440px)은 모바일 레이아웃이 완전히 정착되고 검증된 후, 이에 맞춰 다단 그리드로 유동 확장하는 보조 해상도로 대응합니다. 앞으로의 모든 UI 마일스톤에 이 모바일 우선 원칙을 철저히 고정하여 적용합니다.

## 공통 상태 언어

- 💡 제안: 아이디어일 뿐이며 아직 구현되지 않은 상태입니다.
- 📝 승인됨: 사용자가 채택했지만 아직 구현되지 않은 상태입니다.
- 🔨 구현됨: 실제 코드 또는 설정이 존재하지만 작동은 아직 검증되지 않은 상태입니다.
- ✅ 검증됨: 실제 동작을 확인했고 그 증거가 존재하는 상태입니다.

구현 전에는 구현됐다고 표현하지 않습니다. 실제 검증 전에는 `PASS`, `완료`, `검증됨`이라고 표현하지 않습니다. 직접 확인하지 못한 내용은 `확인 필요`라고 표현합니다.

## M2 요구사항 정리 및 승인 Gate (M2.0)

- ✅ 검증됨: 공식 Run `run-05dbfc27`에서 `execution_mode: skills`, `workflow_run_id: null`로 `speckit-specify`와 `speckit-plan`을 직접 호출했습니다.
- ✅ 검증됨: 승인 전 Plan 차단, Spec 본문 수정, Version `1 → 2`, 승인 초기화와 현재 Version 승인, 승인 후 Plan Artifact 생성과 새 프로세스 재조회를 확인했습니다.
- `run-3b0ffae8`은 다른 Agent 변경이 섞인 `diagnostic_failed` 기록이며 M2 PASS 증거로 사용하지 않습니다.

## M3 Design·Plan·Tasks 완료

- ✅ 검증됨: 공식 Run `run-05dbfc27`에서 UI UX Pro Max와 `frontend-app-builder`를 실제 호출하여 구조가 다른 디자인 탐색 v1과 모바일 우선 Option C v2를 생성했습니다.
- ✅ 검증됨: Option C v2는 390px·430px·1440px, 화면 이동, 오류·완료 상태와 Console 기준 Browser 기술 검증을 통과했습니다.
- 사용자 디자인 만족은 `needs_improvement`이며 Option C v2는 `approved_for_m4_pipeline_test`로만 승인합니다. 상업 디자인 승인이나 Reference 승격으로 해석하지 않습니다.
- 미완성 v3는 `aborted_draft` 참고자료이며 공식 디자인 증거가 아닙니다.
- ✅ 검증됨: 공식 `speckit-tasks` Skill을 같은 Run에서 한 번 호출해 T001~T047을 생성했고 새 Run·Workflow·자동 재시도는 사용하지 않았습니다.
- ✅ 검증됨: 47개 Task를 정확히 한 번씩 포함하는 6개 작업 묶음과 수정 허용·금지 경계를 가진 M4 Handoff를 작성했습니다.
- M4 Handoff Gate는 `ready_for_antigravity`, 구현 상태는 `not_started`입니다. Handoff 준비만으로 Antigravity를 자동 실행하지 않습니다.
- 제작 프로젝트 M3 기준점 Commit은 `2554340`이며 Push는 별도 승인 전까지 수행하지 않습니다.
