# Current State

현재 단계는 `M1 — Run·Git 안전 기반`의 M1.1 범위를 구현하고 독립 검증한 뒤 M2 착수를 준비하는 단계입니다. M1.1 필수 확인 12개 항목은 격리 환경의 실제 실행에서 PASS했고, 검증된 구현은 Branch `antigravity/v2-m1-run-core`의 Commit `28af3fff7eb9bd9b809218cf6bb70e548a759661`에 저장했습니다. Kernel, Planner, Collector, Multi-Agent 및 자체 실행 엔진은 구현하지 않습니다.

V2 Core 현황판의 M1 상태는 실제 검증 결과를 근거로 `completed`이며 M2~M7은 `pending`입니다. 이 상태와 후속 Wiki 보완 Commit은 아직 GitHub `main`에 반영되지 않았습니다.

## Spec Kit 도입 상태

- 🔨 구현됨: GitHub Spec Kit `v0.16.1` 기반이 현재 `main`에 설치되어 있습니다.
- 🔨 구현됨: 기존 V2 원칙을 `.specify/memory/constitution.md`에 연결했습니다.
- ✅ 검증됨: Spec Kit Codex 통합의 관리 파일 상태 검사가 오류와 누락 없이 통과했습니다.
- ✅ 검증됨: 현재 설치된 Workflow가 Run, Status, Resume, 승인 Gate와 `Specify → Plan → Tasks → Implement` 단계를 제공함을 실제 CLI와 Workflow 정의에서 확인했습니다.
- 확인 필요: Clarify, 조건부 Design, Manual Agent 대기, 독립 검증과 Git 복구 단계를 하나의 V2 Workflow로 연결하는 최소 설정.

## 공식 기억 동기화 상태

- 확인한 공식 원격 `origin/main`은 `7674debbe3f22c16df1e3ef81af25fa4052c91ca`입니다.
- 로컬 작업 Branch는 M1 구현·검증 및 후보 문서 Commit을 포함해 `origin/main`보다 앞서 있으며 아직 원격에 Push되지 않았습니다.
- V2 Run의 공식 기억은 `memory.official_commit`, 로컬 구현 기준은 `v2_workspace.head`로 분리해 기록합니다.

## 디자인 파일럿 상태

- 📝 승인됨: UI UX Pro Max를 디자인 단계 핵심 파일럿 부품으로 채택했습니다.
- 미설치: 별도 파일럿 브랜치와 도입 전 복구점을 확인한 뒤 고정 버전으로 시험합니다.
- 확인 필요: 실제 설치·출처·버전·라이선스와 디자인 시스템 결과 검증. Product Design + ImageGen으로 만든 기존 병원 웹 이미지는 비교 참고자료이며 UI UX Pro Max 검증 결과가 아닙니다.

## Ponytail 도입 상태

- 🔨 구현됨: 공식 Ponytail Skill이 현재 `main`에 프로젝트 단위로 설치되어 있습니다.
- 설치 기준: `DietrichGebert/ponytail` Commit `2ed6c52c9d7e5e56942508591085fd45dea277d3`.
- 적용 수준: 첫 파일럿은 `lite`로 사용합니다.
- 확인 필요: 새로운 Codex 작업에서 프로젝트 Skill 자동 인식과 실제 코드 변경 품질 검증.
- 제작자 자체 벤치마크 수치는 V2에서 독립 검증된 사실로 취급하지 않습니다.

## 현재 확정된 운영 방식

- 웹 ChatGPT는 아이디어 대화와 외부 자료 조사·정리를 담당합니다.
- Codex는 실제 저장소를 기준으로 구조 조사, 설계, 작업 지시서 작성과 독립 검증을 담당합니다.
- Antigravity는 사용자가 전달한 승인된 지시서에 따라 수동으로 구현합니다. 파일 수정, 명령 실행과 보안 권한은 사용자 확인을 거칩니다.
- 구현 Agent가 보고한 완료를 그대로 공식 사실로 저장하지 않습니다. 실제 결과와 검증 증거를 확인한 뒤 승인된 변경만 Git에 저장합니다.
- 기존 `ai_os`는 참고 자료이며 V2 코드 재사용 원본이 아닙니다.

## 확정된 다음 단계

- M1 결과와 승인된 Wiki 보완 Commit을 원격 Branch에 Push하여 다른 AI가 같은 기준을 읽을 수 있게 합니다.
- M2에서 실제 Spec Kit Specify/Clarify Workflow Run ID를 기존 V2 Run의 `integrations.spec_kit.workflow_run_id`에 연결합니다.
- 사용자 승인 전 Plan을 차단하고, 승인·거절·수정 요청 뒤 같은 V2 Run을 Resume하는 흐름을 검증합니다.
- 첫 MVP는 활성 Run 하나만 지원하며 별도 DB와 전용 UI를 만들지 않습니다.
- M1~M4에서 실제 Core Workflow를 먼저 검증하고, M5에서 그 실제 상태만 읽는 얇은 V2 UI를 구현합니다.
- 병원 웹은 M4 Feature Run의 실제 결과물로 사용하고, 예약 버튼 수정은 M6 Change Run에서 검증합니다.
- 각 마일스톤은 실제 PASS 증거가 생긴 뒤 `CURRENT_STATE.md` 갱신안을 만들고 사용자 승인 후 Commit/Push합니다. Obsidian은 같은 로컬 파일을 사용하므로 승인된 변경을 즉시 표시합니다.
