# AI OS V2 표준 사용자 제작 흐름

Status: Official

Scope: All V2 Feature Runs and Change Runs

Owner: V2 Core (Zeus)

Priority: Highest

이 문서는 V2 제작 흐름의 최상위 기준입니다. 다른 문서와 충돌하면 충돌을 보고하고 사용자 승인 없이 이 문서의 핵심 흐름을 바꾸지 않습니다.

## 사용자에게 보이는 흐름

`요청하기 → 만들 내용 확인 → 미리보기 선택 → 제작 및 확인 → 완료`

사용자가 판단할 때만 `[이대로 진행]`, `[수정 요청]`, `[중단]`을 표시합니다. Run ID, Commit SHA, 기술 스택, 패키지명과 테스트 로그는 기본 화면에서 숨기고 상세 보기에서만 제공합니다. 가짜 진행률과 예상 완료 시간은 표시하지 않습니다.

## V2 내부 표준 흐름

`자연어 요청 → 수집·분석 → 요구사항 확인 → Preview → 사용자 선택 → 구현 → Codex 독립 검증 → 사용자 확인 → Commit·복구점`

### 1. 자연어 요청

V2 Core가 사용자 원문, 대상 프로젝트, 기준 Commit, 요청 시각, Run 종류, 임시 실행 경로와 허용·금지 범위 초안을 기록합니다. 사용자가 Run ID나 Commit을 입력하지 않습니다.

### 2. 수집·분석

현재 코드·Git·실행 상태, V2 검증 레시피, 설치된 Skill·CLI·MCP, 공식 API·문서, 유지관리되는 GitHub OSS, 성공·실패 사례, 재사용 코드와 모바일·PC·브라우저 제약을 수집합니다.

분석 결과는 최소 기능·제외 범위, 후보 레시피 최대 2개, 위험도와 예상 실패점, Preview·검증 방법 및 완료 수준을 포함합니다. 검색 순서는 `V2 검증 레시피 → 설치·검증 기능 → 공식 표준·도구 → 유지관리 OSS → 실제 사례 → 얇은 연결 → 자체 구현`입니다.

### 3. 요구사항 확인

사용자에게 `만들 것`, `이번에는 만들지 않을 것`과 선택지만 보여줍니다. 수정 시 요구사항 Version을 올리고 기존 승인을 무효화하며 Diff를 보존합니다. 현재 Version 승인 전에는 구현을 시작하지 않습니다.

### 4. Preview

Preview는 실제 제품과 분리된 가역적 검토 Artifact입니다. 가짜 데이터를 사용하고 원본 프로젝트를 보호하며 모바일 우선으로 핵심 동작을 직접 확인할 수 있어야 합니다. 정적인 그림으로 기능을 확인할 수 없으면 동작형 Preview를 사용합니다. 자동 재시도하지 않고 실패 증거를 남깁니다.

### 5. 사용자 선택

선택은 `승인`, `수정 요청`, `다른 안 보기`, `나중에`, `중단`입니다. 다음 의미를 구분합니다.

- `approved_for_implementation`: 구현 입력으로 사용 가능
- `needs_improvement`: 개선 필요, 파이프라인 시험 가능
- `commercially_approved`: 실제 상업 결과 승인
- `reference_approved`: 다른 프로젝트에서 재사용 승인

파이프라인 시험 승인을 상업·Reference 승인으로 해석하지 않습니다.

### 6. 구현

Antigravity는 승인된 제품·기능 구현, Codex는 환경·설정과 독립 검증, V2 Core는 Run·상태·Gate·증거를 담당합니다. Handoff에는 목표, 기준 Commit, 허용·금지 범위, 검증 방법과 보고 형식을 포함합니다. Preview를 제품 완료물로 간주하지 않으며 동일 Run에는 쓰기 담당자 한 명만 허용합니다.

### 7. Codex 독립 검증

구현 Agent의 보고와 별도로 실행, Typecheck·Build, 주요 사용자 흐름, 모바일·PC, Console, 깨진 자산, 요구 누락, 범위 밖 기능, 저장·전송, Git diff, 허용 경로와 원본 Artifact를 확인합니다. 기능별 검사를 추가하며 종료코드가 `0`이어도 실제 Artifact가 없으면 실패입니다.

### 8. 사용자 확인

기술 로그 대신 사용자가 실제 결과에서 수행할 행동만 안내합니다. 사용자는 `[문제없음]`, `[수정 필요]`, `[중단]`을 선택합니다. 사용자 `문제없음` 전에는 최종 완료로 처리하지 않습니다. 비차단 개선은 별도 후속 후보로 보존할 수 있습니다.

### 9. Commit·복구점

사용자 확인 PASS 후 변경 파일과 Git diff를 확인하고 Result Commit을 생성합니다. 기준 Commit, Artifact, 검증 결과, 사용자 판정, 남은 개선, Rollback 방법과 Restore 결과를 기록하고 새 프로세스에서 재조회합니다. Commit과 검증된 복구점이 없으면 `completed`가 아닙니다.

## 실행 경로

- `quick`: 문구·색상·간격·작은 버그처럼 제한된 한 영역. 영향 분석 후 수정·검증·사용자 확인·Commit/복구를 수행합니다.
- `standard`: 새 화면·일반 기능·Preview가 필요한 제작. 전체 표준 흐름을 사용합니다.
- `high_risk`: 로그인·권한·DB·개인정보·결제·삭제·마이그레이션·배포·비밀키·대규모 구조·불명확 라이선스. 추가 조사와 사용자 승인 Gate를 사용합니다.

위험도는 `quick → standard → high_risk`로 자동 상향할 수 있지만 자동 하향하지 않습니다.

## 내부 상태와 사용자 표시

| 내부 상태 | 사용자 표시 |
|---|---|
| `requested`, `collecting`, `analyzing` | 요청을 확인하고 있습니다 |
| `awaiting_requirements_review` | 만들 내용 확인 |
| `preview_in_progress` | 미리보기 제작 중 |
| `awaiting_preview_review` | 미리보기 선택 |
| `ready_for_implementation`, `implementing` | 제작 중 |
| `verifying` | 결과 확인 중 |
| `awaiting_user_confirmation` | 사용자 확인 대기 |
| `committing`, `completed` | 완료 처리 중 / 완료 |
| `blocked`, `failed` | 문제 확인 필요 |
| `cancelled` | 중단됨 |

## Gate 규칙

- 요구사항 승인 전 구현 차단
- Preview가 필요한 Standard Run은 Preview 선택 전 구현 차단
- 구현 Artifact가 없으면 검증 완료 차단
- Codex 검증 실패 시 사용자 최종 승인 차단
- 사용자 확인이 없으면 최종 Commit 차단
- Commit·복구점이 없으면 `completed` 차단
- 공식 활성 Run은 하나만 허용
- 사용자 승인 없이 별도 Run이나 구현 단계를 자동 생성하지 않음

## MVP 이후 자동 연결

최종 Run 완료 후 [Post-MVP Roadmap](POST_MVP_ROADMAP.md)을 읽고 미검증 후보와 기존 레시피·공식 자료·실제 사례를 조사해 최대 3개를 추천할 수 있습니다. 사용자는 `[다음 후보 진행]`, `[다른 후보]`, `[나중에]`만 선택합니다.

읽기 전용 조사·분석은 자동 허용하지만 기존 제품 수정, 외부 설치, DB, 로그인·권한, 개인정보, 결제, 배포와 삭제·마이그레이션은 사용자 승인 없이 실행하지 않습니다.

## Core 소유권

새 Workflow 엔진을 만들지 않습니다. V2 Core는 Run, 상태, Gate, Artifact 경로, 사용자 판정, Commit·복구점과 다음 작업 표시만 소유합니다. Spec Kit은 요구사항·Plan·Tasks Artifact를 생성하며 Codex와 Antigravity는 별도 Run 상태를 소유하지 않습니다.
