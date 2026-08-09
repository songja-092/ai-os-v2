# Current State

현재 단계는 V2 MVP 설계를 닫고 `M1 — Run·Git 안전 기반` 구현을 시작하기 직전입니다. Kernel, Planner, Collector, Multi-Agent 및 자체 실행 엔진은 구현하지 않습니다.

이전 지식 연결 시험 기록은 존재하지만, 파일럿 시작 기준인 네 연결의 Repository, Branch, Commit SHA와 실제 증거를 한 보고서에서 최종 확인해야 합니다.

## Spec Kit 도입 상태

- 🔨 구현됨: GitHub Spec Kit `v0.16.1` 기반이 현재 `main`에 설치되어 있습니다.
- 🔨 구현됨: 기존 V2 원칙을 `.specify/memory/constitution.md`에 연결했습니다.
- ✅ 검증됨: Spec Kit Codex 통합의 관리 파일 상태 검사가 오류와 누락 없이 통과했습니다.
- ✅ 검증됨: 현재 설치된 Workflow가 Run, Status, Resume, 승인 Gate와 `Specify → Plan → Tasks → Implement` 단계를 제공함을 실제 CLI와 Workflow 정의에서 확인했습니다.
- 확인 필요: Clarify, 조건부 Design, Manual Agent 대기, 독립 검증과 Git 복구 단계를 하나의 V2 Workflow로 연결하는 최소 설정.

## 공식 기억 동기화 상태

- 현재 설계 기준 `main`은 `d85c9482c14b6bda70cea4dda3b5dae9df883aed`이며 로컬 HEAD와 `origin/main`이 일치함을 확인했습니다.
- 이번 문서 보완 Commit/Push 후 새 SHA를 다음 M1 작업의 `Base Memory Commit`으로 사용합니다.

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

- M1에서 Spec Kit Workflow Run ID를 우선 재사용하여 Run, 대상 Project, `Base Memory Commit`, `Base Project Commit`, 상태와 재개 지점을 연결합니다.
- 첫 MVP는 활성 Run 하나만 지원하며 별도 DB와 전용 UI를 만들지 않습니다.
- M1~M4에서 실제 Core Workflow를 먼저 검증하고, M5에서 그 실제 상태만 읽는 얇은 V2 UI를 구현합니다.
- 병원 웹은 M4 Feature Run의 실제 결과물로 사용하고, 예약 버튼 수정은 M6 Change Run에서 검증합니다.
- 각 마일스톤은 실제 PASS 증거가 생긴 뒤 `CURRENT_STATE.md` 갱신안을 만들고 사용자 승인 후 Commit/Push합니다. Obsidian은 같은 로컬 파일을 사용하므로 승인된 변경을 즉시 표시합니다.
