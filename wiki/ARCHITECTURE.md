# Architecture

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
Spec Kit Workflow 기반 V2 Core
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
V2 Core Resume
  | Codex 독립 검증
  | 사용자 실물 확인과 최종 승인
  | Result Commit
  | 별도 worktree Rollback / Restore
  v
Run 종료와 승인된 Wiki 갱신
```

V2 Core는 AI를 직접 호출하는 새 오케스트레이터가 아닙니다. Spec Kit의 기존 Workflow 엔진을 우선 사용하고, 빠진 단계의 순서·Gate·외부 결과 참조만 최소 연결합니다.

## 사용자에게 보이는 흐름

기술 단계를 그대로 노출하지 않고 다음 다섯 단계로 표현합니다.

1. 원하는 결과 말하기
2. 조사 결과와 선택지 보기
3. 시안과 작업 계획 승인하기
4. 구현 결과를 실제 화면에서 사용해 보기
5. 저장하거나 이전 상태로 되돌리기

사용자는 코드, 명령어와 내부 Agent 연결을 직접 관리하지 않습니다. 사용자가 직접 판단하는 지점은 요구사항, 조건부 디자인, 작업 계획, 보안·실행 권한과 최종 결과 승인입니다.

## 제작 파이프라인

1. **Intake**: 자연어 요구와 참고 URL을 받습니다.
2. **Research**: 필요한 근거를 공식 문서, GitHub, Web과 실사용 자료에서 조사하고 출처를 남깁니다.
3. **Specify/Clarify**: Spec Kit으로 요구사항, 제외 범위와 완료 조건을 정리하고 사용자가 승인합니다.
4. **Target Environment**: Web, Android, iOS, Desktop, CLI, API, Server 또는 기타 대상 환경을 확정합니다.
5. **Conditional Design**: UI/UX가 필요한 경우에만 디자인 도구를 선택합니다. 현재 기본 파일럿은 UI UX Pro Max이며 사용자가 결과를 승인합니다.
6. **Plan/Tasks**: 승인된 요구사항과 디자인을 실제 구현 계획과 작은 작업으로 변환합니다.
7. **Reuse Decision**: 기존 제품·OSS·Skill·MCP·서비스를 비교 검증합니다.
8. **Handoff**: Codex가 변경 파일, 허용 명령, 금지 범위, 검증 방법과 복구점을 포함한 구현 지시서를 만듭니다.
9. **Implement**: Antigravity가 사용자 승인 아래 한 Task씩 구현합니다.
10. **Verify**: Target Environment에 맞는 실제 실행 검증을 수행합니다. 웹이면 Playwright, CLI면 명령/출력, API면 요청/응답 검증처럼 도구를 조건부로 선택합니다.
11. **Accept**: 사용자가 실제 결과를 확인하고 승인하거나 수정을 요청합니다.
12. **Save**: 승인된 한 변경을 Commit/Push하고 Wiki와 시각화가 해당 SHA를 가리키게 합니다.
13. **Recover**: 이전 Commit을 확인한 뒤 결과 Commit으로 복구하고 재실행합니다.

각 단계는 `running`, `waiting_user`, `waiting_agent`, `blocked`, `failed`, `completed`, `cancelled` 중 하나의 실제 상태를 가집니다. 실패하거나 중단된 Run은 원인과 재개 지점을 남깁니다.

## V2 화면 뼈대

M5에서 구현할 화면은 M1~M4의 실제 Run 상태만 읽습니다.

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
- 승인 버튼은 화면 상태만 바꾸지 않고 실제 Workflow Gate를 Resume해야 합니다.
- 웹 Live Preview는 사용자 승인 `localhost` 또는 `127.0.0.1` 개발 서버를 사용합니다.
- CLI, API와 Server 프로젝트는 Live Preview 대신 해당 환경의 실제 실행 결과를 표시합니다.
- Commit과 Rollback 상태는 실제 SHA와 검증 결과가 없으면 완료로 표시하지 않습니다.

## Run 기록 경계

- V2 저장소는 공식 기억과 Workflow 연결 정의를 보관합니다.
- 제작 프로젝트 저장소는 실제 소프트웨어와 Result Commit을 보관합니다.
- Spec Kit 산출물은 원본 경로를 참조하고 Run 기록에 복제하지 않습니다.
- 첫 MVP는 활성 Run 하나만 지원하고 DB를 사용하지 않습니다.

## 구현 마일스톤

1. **M1 — Run·Git 안전 기반**: Workflow Run ID, Project, 두 Base Commit, Branch, 상태·중단·재개를 연결합니다.
2. **M2 — Spec과 승인 Gate**: 실제 Specify/Clarify 결과가 승인 전 멈추고 승인 후 같은 Run에서 재개되는지 검증합니다.
3. **M3 — 조건부 Design과 Plan/Tasks**: 필요한 단계만 실행하고 승인된 Tasks를 생성합니다.
4. **M4 — Feature Run 완성**: Manual Agent Handoff, 구현 결과 회수, 독립 검증, 사용자 승인, Result Commit과 안전한 Rollback/Restore를 병원 웹에서 검증합니다.
5. **M5 — 얇은 V2 UI**: M1~M4의 실제 상태와 산출물을 읽고 승인·Resume와 웹 Live Preview를 제공합니다.
6. **M6 — Change Run**: 기존 결과의 작은 수정에서 필요한 단계만 실행하고 회귀 검증과 새 Commit을 만듭니다.
7. **M7 — MVP E2E**: V2 UI에서 병원 웹 Feature Run과 예약 버튼 Change Run을 실제로 완료합니다.

각 마일스톤이 PASS하면 V2 Core가 `CURRENT_STATE.md` 갱신안을 생성합니다. 사용자가 승인한 갱신만 Commit/Push하며 Obsidian은 같은 로컬 Wiki를 즉시 표시합니다. Archify 자동 갱신은 현재 구현된 것으로 간주하지 않습니다.

## 증거 규칙

- 아이디어나 화면 예시는 실제 구현과 분리하여 표시합니다.
- 실제 파일 또는 설정이 있어야 `🔨 구현됨`입니다.
- 해당 기능을 직접 실행한 증거가 있어야 `✅ 검증됨`입니다.
- 구현 Agent의 보고만으로 PASS 처리하지 않습니다.
- 조사 결과에는 원문 URL, 확인 날짜와 채택/탈락 이유를 남깁니다.

## 현재 부품 상태

| 역할 | 부품 | 상태 |
|---|---|---|
| 공식 기억과 버전 | GitHub + Wiki | ✅ 연결 검증 기록 존재 |
| 사람용 편집 | Obsidian | ✅ 연결 검증 기록 존재 |
| 구조 시각화 | Archify | 연결 검증 증거 재확인 필요 |
| 자연어 명세 | Spec Kit | 🔨 `main` 적용, 실제 Feature Run 미검증 |
| 디자인 시스템 제안 | UI UX Pro Max | 📝 승인됨, 미설치 |
| 설계·독립 검증 | Codex | 사용 중 |
| 실제 구현 | Antigravity | 수동 운영 방식 확정 |
| 구현 최소화 규칙 | Ponytail | 🔨 `main` 설치, 실제 Task 미검증 |
| 환경별 검증 | 프로젝트별 도구 | 💡 Target Environment에 따라 선택 |
| Core Workflow | Spec Kit Workflow | 🔨 기본 Run/Gate/Resume 존재, V2 전체 연결 미구현 |
| V2 UI | 없음 | M5 이전에는 구현하지 않음 |
| 자동 AI 호출 | 없음 | MVP 필수 아님, Manual Agent Adapter 사용 |

Kernel, Planner, Collector, Multi-Agent와 자체 실행 엔진은 현재 아키텍처의 필수 구성요소가 아닙니다. V2 UI는 Core를 대신하지 않으며 M1~M4에서 검증된 실제 상태를 M5에서 보여주는 인터페이스입니다.
