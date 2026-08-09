# Decisions

- GitHub 저장소와 Git commit을 공식 기록으로 사용합니다.
- Obsidian은 Wiki를 읽고 편집하는 인터페이스로 사용합니다.
- Archify 결과는 Source of Truth가 아닌 commit 기반 파생 시각화로 취급합니다.
- 연결 검증이 끝나기 전까지 V2 기능을 개발하지 않습니다.

## 조립 우선 원칙

AI OS V2는 개발 기능을 새로 만드는 OS가 아니라, 검증된 기존 도구·오픈소스·Skill·MCP·서비스를 조립하여 개발자 역할을 수행하게 만드는 OS로 설계합니다. 직접 구현은 적합한 기존 대안이 없을 때만 최소한으로 합니다.

기능마다 부품 종류의 우선순위를 미리 고정하지 않고 다음 순서로 판단합니다.

`필요한 기능 → 기존 제품·오픈소스·Skill·MCP 조사 → 실제 검증 → 채택 또는 탈락 → 부족한 연결부만 최소 제작`

## Spec Kit 도입

- 📝 승인됨: 자연어 요구사항을 구조화하는 기본 절차로 GitHub Spec Kit을 채택합니다.
- 사용자에게 보이는 기본 절차는 `Specify/Clarify → 요구사항 승인 → Plan/Tasks → 계획 승인 → Implement`로 사용합니다.
- `Analyze`, `Converge` 등은 필요할 때 사용하는 내부 검증 수단이며 사용자 흐름의 고정 단계로 만들지 않습니다.
- Spec Kit `v0.16.1` 기반과 Codex 통합은 현재 `main`에 반영되어 있습니다. V2 전체 Workflow 연결과 실제 Feature Run은 아직 미구현·미검증입니다.
- Codex를 현재 Spec Kit 기본 통합으로 사용합니다.
- Antigravity는 Spec Kit을 직접 실행할 필요 없이 승인된 Markdown 산출물과 Codex 작업 지시서를 전달받아 수동으로 구현합니다.
- 도입 전 복구 기준은 Git 태그 `rollback/before-spec-kit-20260809`입니다.

## V1 사용 경계

- 기존 `/home/user/바탕화면/ai_os`는 요구사항, UX 흐름과 실패 원인을 분석하는 참고 자료로만 사용합니다.
- V1의 Kernel, Collector, Truth Guard, UI와 테스트 코드는 V2로 자동 이식하지 않습니다.
- V1에 존재한다는 사실만으로 V2에 적용되었거나 검증된 것으로 기록하지 않습니다.

## Agent 역할과 권한

- 웹 ChatGPT는 아이디어 조사와 정리를 담당하며 구현 완료를 판정하지 않습니다.
- Codex는 저장소 기반 설계, 작업 범위 작성과 독립 검증을 담당합니다.
- Antigravity는 기본적으로 수동 구현 Agent로 사용합니다.
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

## V2 Core와 Run

- 📝 승인됨: V2 Core는 AI 모델이나 새 Kernel이 아니라 기존 도구의 실행 순서, 승인 Gate, 결과 참조, 증거와 Git 복구점을 한 Run으로 연결하는 Workflow입니다.
- 가능한 경우 Spec Kit Workflow의 Run ID, Status, Resume와 Gate를 그대로 사용합니다. 별도 Run 엔진이나 ID 생성기를 먼저 만들지 않습니다.
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
- V2 UI는 M5에서 실제 Core Workflow 상태를 읽고 승인 시 같은 Run을 Resume하는 얇은 인터페이스로 구현합니다.
- MVP 웹 Preview는 사용자가 승인한 `localhost` 또는 `127.0.0.1` 개발 서버 하나만 지원합니다. Phone·Tablet·Desktop 전환은 MVP 범위에서 제외합니다.
- Rollback/Restore 검증은 사용자의 현재 작업 폴더를 변경하지 않도록 별도 임시 `git worktree`에서 수행합니다.

## Ponytail 파일럿

- 📝 승인됨: 불필요한 코드와 의존성을 줄이는 구현 규칙으로 Ponytail을 파일럿 채택합니다.
- 첫 적용 수준은 `lite`이며 프로젝트마다 필요성을 다시 판단할 수 있습니다.
- 판단 순서는 `필요성 → 기존 코드 → 표준 라이브러리 → 플랫폼 기본 기능 → 설치된 의존성 → 최소 코드`입니다.
- 최소화를 이유로 입력 검증, 데이터 손실 방지 오류 처리, 보안, 접근성, 사용자가 승인한 요구사항과 필요한 실행 검증을 생략하지 않습니다.
- Ponytail 제작자의 LOC·토큰·비용·시간 벤치마크는 참고자료이며 V2의 독립 검증 결과가 아닙니다.
- 공식 저장소 Commit `2ed6c52c9d7e5e56942508591085fd45dea277d3`을 고정하여 별도 브랜치에서 먼저 검증합니다.
- 도입 전 복구 기준은 `main` Commit `c53a10e6e29da2b270d3cde1df532035efcb4722`입니다.

## 공통 상태 언어

- 💡 제안: 아이디어일 뿐이며 아직 구현되지 않은 상태입니다.
- 📝 승인됨: 사용자가 채택했지만 아직 구현되지 않은 상태입니다.
- 🔨 구현됨: 실제 코드 또는 설정이 존재하지만 작동은 아직 검증되지 않은 상태입니다.
- ✅ 검증됨: 실제 동작을 확인했고 그 증거가 존재하는 상태입니다.

구현 전에는 구현됐다고 표현하지 않습니다. 실제 검증 전에는 `PASS`, `완료`, `검증됨`이라고 표현하지 않습니다. 직접 확인하지 못한 내용은 `확인 필요`라고 표현합니다.
