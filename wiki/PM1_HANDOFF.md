# PM1 Thin UI Handoff

> 역사적 문서: 이 문서의 PM1~PM4 번호 체계는 [[POST_MVP_FINAL_DESIGN]]의 PM0~PM7 구조로 대체됐습니다. PM1 Thin UI 기술 계약은 참고할 수 있지만 현재 단계·다음 PM·전체 Roadmap 판정에는 사용하지 않습니다. 새 세션은 [[GPT_SESSION_CHANGE_CONTINUATION_HANDOFF]]에서 시작합니다.

작성일: 2026-08-15
목적: 새 Codex 세션이 과거 대화를 다시 읽지 않고 Post-MVP PM1부터 안전하게 이어가기 위한 공식 인수인계입니다.

## 1. 공식 기준점

```yaml
repository: https://github.com/songja-092/ai-os-v2
official_branch: main
core_mvp: M1-M7 completed_and_frozen
post_mvp_planning: PM1-PM4 approved
active_milestone: PM1_minimum_modular_foundation_and_thin_ui
pm1_implementation: not_started
selected_direction: MIX-1
design_method: Hybrid_H
pm1_clickable_preview: rejected_visual_fidelity
```

제품 저장소 `/home/user/바탕화면/test_project`의 완료 기준점은 병원 웹 `c970352`, M6 부분 수정 `e2625bb`, M7 PDF 제품 `3b592c8`입니다. 제품 저장소와 V2 저장소를 하나의 Commit처럼 처리하지 않습니다.

## 2. 반드시 먼저 읽을 문서

1. [[CURRENT_STATE]] · [GitHub 링크](CURRENT_STATE.md)
2. [[POST_MVP_ROADMAP]] · [GitHub 링크](POST_MVP_ROADMAP.md)
3. [[THIN_UI_MVP_CONTRACT]] · [GitHub 링크](THIN_UI_MVP_CONTRACT.md)
4. [[ui-reference-mix]] · [GitHub 링크](ui-reference-mix.md)
5. [[ARCHITECTURE]] · [GitHub 링크](ARCHITECTURE.md)
6. [[DECISIONS]] · [GitHub 링크](DECISIONS.md)

기억이나 과거 대화보다 위 문서와 실제 Git 상태를 우선합니다.

## 3. Post-MVP 공식 순서

### PM1 — 최소 조립식 기반 + 얇은 UI

사용자가 프로젝트를 선택하고 현재 요청·상태와 실제 Preview를 확인한 뒤 `통과`, `수정 요청`, `중단`을 선택하고 다른 프로젝트로 전환합니다.

### PM2 — 직접 부분 수정

사용자가 `HERO-01`의 글자 크기, 콘텐츠 폭, 줄바꿈과 배경색을 제한된 값으로 직접 조절하고 원래대로 또는 적용합니다.

### PM3 — 조사·자료 수집·병목 진단

공통 Source Adapter로 새 프로젝트 조사 1건과 기존 프로젝트 병목 진단 1건만 먼저 검증합니다. 가장 영향이 큰 병목 하나와 해결책 최대 2개를 제시하며 승인 전 제품을 변경하지 않습니다.

### PM4 — AI 의도 정합성

Intent Packet과 구현 AI의 Intent Receipt를 비교해 오해 상태의 구현 시작을 차단합니다. Provider 자동 교체 시스템은 만들지 않고 AI 역할 Adapter 계약 경계만 남깁니다.

## 4. PM1 승인 계약

```text
V2 Core → ui-state(JSON) → UI
UI → ui-action → V2 Core
```

- UI는 Run YAML, Wiki 또는 프로젝트 파일을 직접 읽거나 수정하지 않습니다.
- UI는 임의 Shell 명령을 만들지 않습니다.
- Core가 내려준 `allowed_actions`만 표시합니다.
- Action에는 `state_version`과 `action_id`를 사용해 stale·중복·다른 프로젝트 요청을 차단합니다.
- 프로젝트는 Core Project Registry의 고정 경로·Port·시작 명령만 사용합니다.
- Preview 장애가 Core, 다른 프로젝트와 과거 결과에 전파되면 안 됩니다.
- Project Registry와 Module Registry는 정적 허용 목록으로 제한합니다.
- Module은 `project_home`, `workspace_preview`, `workspace_tools`, `background_capability` 고정 Slot만 사용합니다.
- Module은 Run·Gate·Artifact와 Action 허용 여부를 직접 변경하지 않습니다.

## 5. PM1 Hybrid H 디자인 기준

공식 방향은 MIX-1이며 다음 절차를 사용합니다.

```text
Reference Mix → A/B/C → MIX-1
→ 화면·핵심 상태별 visual_target → 사용자 시각 승인
→ Image-to-Code → 동일 Viewport Fidelity PASS
→ 코드가 디자인 원본
```

검증 Viewport는 `1440×950`, `430px`, `390px`입니다. `design-draft.json`은 구조 계약이며 visual target을 대신하지 않습니다. 기존 Preview v1은 `rejected_visual_fidelity`로 보존하고 구현 입력으로 사용하지 않습니다.

Reference Mix는 Linear, Figma Prototype, ChatGPT Canvas, Home Assistant, SafetyCulture와 Shopify POS의 패턴을 각각 1~2개만 사용합니다. 브랜드·색상·이미지·아이콘·소스 코드를 복제하지 않습니다.

## 6. PM1 최소 범위

- 프로젝트 2개: 병원 웹과 PDF 도면 기호
- 프로젝트 홈과 작업실
- 실제 Preview 실행·중단·전환
- 사용자에게 쉬운 현재 상태와 다음 행동
- 통과·수정 요청·중단
- Preview 서버 종료, Port 충돌, 앱 초기화 실패와 프로젝트 전환 상태
- 최소 오류 보고서

제외: Galaxy, Docker 관리 UI, Skill·AI 관리, 풍부한 작업 기록, 범용 설정, 직접 부분 수정, Source Adapter UI, 자유 Dashboard와 Marketplace.

## 7. 다음 작업 하나

```text
MIX-1 화면·핵심 상태별 visual_target 생성
→ 사용자 시각 승인
→ Image-to-Code 및 동일 Viewport Fidelity 검증
```

visual target 승인과 Fidelity PASS 전에는 실제 PM1 제품 UI, Core API 또는 Registry 프로세스 제어를 구현하지 않습니다.

## 8. 사용할 기존 도구

- Product Design Ideate
- frontend-app-builder
- Product Design Audit
- frontend-testing-debugging
- Browser

새 UI 라이브러리나 패키지를 설치하지 않습니다. UI UX Pro Max는 설치·호출 가능성을 다시 확인한 경우에만 분석 보조로 사용합니다.

## 9. 저장소와 작업 안전

현재 V2 작업 폴더에는 다른 사용자 소유의 미커밋 변경이 존재할 수 있습니다. 시작할 때 `git status`, HEAD, 원격 main과 실행 중인 프로세스를 다시 확인합니다. 다음을 임의 수정·Stage·Commit·삭제하지 않습니다.

- 기존 실패·진단 Run
- 사용자 IDEA_ARCHIVE 변경
- `v2`의 출처가 섞인 미커밋 변경
- `__pycache__`, `tmp`와 기타 캐시

병원 웹과 PDF 제품은 같은 저장소의 서로 다른 Commit이므로 동시에 실행하려면 사용자 승인 후 별도 Git worktree를 사용합니다. 같은 작업 폴더에서 Commit을 전환하며 두 Preview를 실행하지 않습니다.

## 10. 다음 세션 첫 보고

1. GitHub main과 로컬 HEAD 일치 여부
2. 기존 Dirty 변경과 PM1 작업 격리 가능 여부
3. 병원·PDF 독립 worktree 준비 필요성
4. Reference 6개와 A/B 구조 요약
5. 신규 설치 없이 클릭형 Preview 제작 가능 여부
6. 파일을 수정하기 전 실제 변경 예정 경로

PM1 완료 후에는 반드시 PM2를 다음 마일스톤으로 제시합니다.
