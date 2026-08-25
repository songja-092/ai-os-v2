# AI OS V2 — PC 운영 UI 구성 및 PM1 시각 설계 인수인계 보고서

작성일: 2026-08-16  
상태: 기존 PC Visual Target 방향 채택·수정 중 / 실제 UI 구현 전

## 1. 이번에 확정한 플랫폼 기준

- **AI OS V2 운영 UI**는 PC 전용으로 완성한다.
- V2 운영 UI 자체의 390px·430px 모바일 화면은 만들지 않는다.
- **V2가 제작하는 고객용 웹·앱 결과물**은 390px·430px 모바일 결과를 필수로 만든다.
- V2 PC 작업실에서는 고객 결과물의 390px·430px 화면을 크게 비교·검토할 수 있어야 한다.
- 고객 결과물의 PC 화면은 해당 프로젝트 요구사항에 따라 추가한다.

이 구분은 V2 운영 도구와 V2가 만드는 제품을 혼동하지 않기 위한 공식 설계 기준이다.

## 2. PM0과 현재 작업의 관계

PM0은 실제 PM 기능 구현을 시작하기 위한 운영환경 Gate다. PM0이 PASS되기 전에도 PM1 시각 설계와 Visual Target 비교는 가능하지만, 선택되지 않은 시안을 제품 코드로 변환하거나 Core와 연결하지 않는다.

현재 PM0 상태:

- 설계: 완료
- 운영환경 Gate: 미완료
- 남은 핵심 검증: Antigravity Sandbox, 병원 웹·PDF 제품의 독립 Worktree와 고정 Port, Preview 장애 격리, 외부 백업·복원, 새 세션 재현
- PM1 실제 구현 허용: 아직 아님

## 3. V2 PC 운영 UI 구성

### 3.1 전역 Navigation

- 대시보드
- 프로젝트
- 자료 조사
- 스킬·기능
- Docker
- 작업 기록
- 설정

`디자인`은 전역 메뉴로 두지 않는다. 디자인은 각 프로젝트의 제작 단계 안에서 다룬다. 개인 Avatar나 `HJ` 표시는 현재 단독 사용자 환경에서 제거한다. 향후 다중 사용자 기능이 실제로 생길 때 계정 영역으로 추가한다.

### 3.2 대시보드

목적은 전체 프로젝트 상태와 사용자가 지금 해야 할 행동 하나를 빠르게 확인하는 것이다.

권장 Section ID:

- `dashboard.next-action`
- `dashboard.core-flow`
- `dashboard.project-list`
- `dashboard.background-jobs`
- `dashboard.blockers`
- `dashboard.recent-completions`

구성:

1. 지금 할 일
2. Core 제작 흐름
3. 프로젝트 목록
4. 백그라운드 작업
5. 문제 있는 작업 — 문제가 있을 때만 확장
6. 최근 완료

프로젝트가 10개·50개 이상으로 늘어나는 상황을 고려해 큰 카드보다 밀도 높은 목록을 기본으로 사용한다. 검색, 유형 필터, 상태 필터, 최근 변경 정렬, 보관됨 분리를 제공한다.

프로젝트 유형 예시:

- 웹사이트
- 기능 도구
- 업무 OS
- 시스템 — 개발 모드에서만 표시
- 보관됨

### 3.3 프로젝트 작업실

목적은 선택한 프로젝트의 요청, 현재 단계, 디자인 후보와 실제 Preview를 한 화면에서 검토하는 것이다.

권장 Section ID:

- `workspace.project-header`
- `workspace.intent-receipt`
- `workspace.stage-flow`
- `workspace.mobile-preview`
- `workspace.design-candidates`
- `workspace.reference-evidence`
- `workspace.allowed-actions`
- `workspace.technical-details`

PC 기본 구조:

- 왼쪽: 사용자 요청, 현재 단계, AI가 이해한 내용
- 중앙: 고객 결과물의 큰 390px·430px 모바일 Preview
- 오른쪽: Reference, 사용 Skill·도구, 검증 근거
- 하단 또는 보조 Rail: 구조가 다른 Design DNA 후보

주요 행동은 `통과`, `수정 요청`, `중단`이며 Core가 제공한 `allowed_actions`에 포함될 때만 표시한다. Run ID, Commit SHA, Port, PID, 내부 Gate와 Agent 로그는 `기술 상세` 안에 접어 둔다.

### 3.4 자료 조사

- 공개 웹·공식 문서·GitHub·Reddit 조사 결과
- 사용자가 제공한 Threads·PDF·Markdown·Text·Screenshot
- 출처, 수집 시점, 라이선스·사용 조건
- 프로젝트별 Reference Mix와 선택 이유
- 자료 부족과 수집 실패 상태

수집 결과를 디자인 후보와 연결하되, 수집 실패가 기존 제작 기능 전체를 차단하지 않게 한다.

### 3.5 스킬·기능

- 사용 가능한 Skill과 실제 연결 상태
- Skill의 역할: 수집, 분석, 디자인 규칙, 구현, 검증
- 설치 출처와 버전 또는 Source Commit
- 프로젝트별 사용 기록
- 실패 시 대체 경로

Skill 이름을 장식용으로 표시하지 않는다. 실제 사용 증거가 있는 Skill만 결과 Provenance에 남긴다.

### 3.6 Docker

Docker는 제품 기능이 아니라 개발·실행 환경 상태를 확인하는 전역 진입점이다.

- 사용 중인 프로젝트와 Container
- 실행·중지 상태
- Port 충돌
- Health 또는 Preview 접근 상태
- 로그와 재시작은 기술 상세에서 제공

실제로 Docker를 쓰지 않는 프로젝트에는 상태를 추정해 표시하지 않는다.

## 4. Core 정합성 계약

V2 UI는 다음 Core 계약을 읽고 행동을 요청하는 얇은 UI다.

- `ui-state`: 현재 단계, 상태, Preview, 오류, 활성 Run
- `ui-action`: 사용자가 요청한 행동 전달
- `allowed_actions`: 현재 상태에서 허용된 버튼 목록

UI가 직접 추정하거나 임의로 PASS 처리하면 안 되는 항목:

- 현재 단계와 PASS
- 다음 행동
- 활성 Run과 정상 Result Run
- Preview·Module·오류 상태

UI는 YAML, 제품 파일, Git 상태를 직접 수정하지 않는다. 모든 변경은 Core 계약과 검증된 실행 경로를 통한다.

## 5. 고객 결과물의 모바일 계약

- 필수 Viewport: 390px, 430px
- 좌우 가로 넘침 금지
- 핵심 Touch Target 44px 이상
- 상태를 색상만으로 표현하지 않음
- 긴 기술정보 기본 숨김
- 동일 기능의 두 모바일 폭 회귀검증
- V2 PC 작업실에서 두 Viewport를 동시에 또는 빠르게 전환해 비교

이 모바일 계약은 V2 운영 UI가 아니라 V2가 제작하는 고객 결과물에 적용한다.

## 6. 이번 Visual Target 제작 기록

### 입력 Reference

- `/home/user/바탕화면/V2_UI/PM1_visual_targets_v2/01-dashboard-pc-v2.png`
- `/home/user/바탕화면/V2_UI/PM1_visual_targets_v2/02-workspace-pc-v2.png`

### 실제 사용 도구·Skill

- 이미지 생성 도구: **OpenAI built-in ImageGen**
- 설계 문맥 확인: `product-design:get-context`
- 구조적으로 다른 방향 탐색: `product-design:ideate`
- 이미지 생성 절차: `imagegen`
- 향후 선택안 구현 준비 기준: `build-web-apps:frontend-app-builder`

이번 제작에 사용하지 않은 도구:

- UI UX Pro Max: 사용하지 않음
- Figma: 사용하지 않음
- Penpot: 사용하지 않음
- Storybook: 사용하지 않음

### 생성 결과

1. `01-project-command-center-1440.png`
   - 방향: 프로젝트 Command Center
   - 핵심: 많은 프로젝트 관리, 다음 행동, 390·430 모바일 결과 동시 비교
   - SHA-256: `465f4e8c0cb43a49638a554dd1b53831495490fa452f69fa9facc01195bf2bb3`

2. `02-mobile-preview-studio-1440.png`
   - 방향: 몰입형 Mobile Preview Studio
   - 핵심: 사용자 요청, 큰 단일 모바일 Preview, Reference·검증 Inspector
   - SHA-256: `70603dde104c0e8402165fdac9653764712d783bc522f020c7c6eec564e720e8`

3. `03-workflow-review-stage-1440.png`
   - 방향: Workflow Board + Review Stage
   - 핵심: Core 단계와 프로젝트 목록, 390·430 비교, 증거 Rail의 균형
   - SHA-256: `9f116a69298c024e1657745dd8768ac2e8f29e0cf7fca77741a128454d6fb862`

보관 위치:

`/home/user/바탕화면/V2_UI/PM1_PC_ONLY_V2_UI_OPTIONS/`

기존 V2 모바일 시안은 삭제하지 않고 `rejected_wrong_platform_scope` 디자인 증거로 보존한다.

## 7. 시각안 해석 주의사항

생성 이미지에 보이는 Docker 정상, PASS, 도구 버전과 같은 상태 문구는 레이아웃을 확인하기 위한 시각 Placeholder다. 공식 Core 상태나 구현 완료 증거가 아니다. 실제 구현에서는 `ui-state`, `allowed_actions`, Provenance Artifact가 제공하는 값만 표시한다.

## 8. 현재 판정과 다음 Gate

### 8.1 2026-08-16 사용자 방향 결정

사용자는 새로 탐색한 3개 방향보다 기존의 다음 두 PC Visual Target 방향이 더 적합하다고 판단했다.

- `/home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target.png`
- `/home/user/바탕화면/v2_ui_images/프로젝트 작업실 PC Visual Target.png`

따라서 이후 디자인 수정은 새로운 전체 화면 탐색이 아니라 이 두 화면을 기준으로 한 부분 수정으로 진행한다.

수정 시간 단축 Workflow:

1. 기준 Visual Target 원본 보존
2. 문제를 Section ID에 연결
3. 한 번에 한두 Section만 수정
4. 동일 Viewport 전후 비교
5. 사용자 확인 후 기준 Version 승격
6. Prompt·도구·입력 이미지·SHA-256 기록

첫 수정본:

- `/home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target v2.png`
  - Docker 메뉴 추가
  - 프로젝트 목록과 우측 Rail의 글 밀도 축소
  - `지금 할 일` 영역 축소와 단일 CTA 유지
  - SHA-256: `fb9a4e1899e74ee478aa1f2e7f4ab06ddb0a26ff20b94099f0b06feeb0369b65`
- `/home/user/바탕화면/v2_ui_images/프로젝트 작업실 PC Visual Target v2.png`
  - Docker 메뉴 추가
  - 고객 결과물 390·430 Preview를 중앙 핵심 영역으로 확대
  - 고객 PC 결과는 보조 Control로 이동
  - 요청·후보·근거 영역의 글 밀도 축소
  - SHA-256: `316d3b8b7782778186160a7f32f04aaa9e3fae11f498a986928cea7a3b6dbe24`

수정본 제작 도구는 **OpenAI built-in ImageGen**이며 UI UX Pro Max·Figma는 사용하지 않았다.

### 8.2 Dashboard v3 부분 수정

사용자 피드백에 따라 Dashboard에서 `지금 할 일`과 노출형 `Core 제작 흐름`을 제거했다. 첫 화면은 빠른 실행과 프로젝트 관리에 집중한다.

- 결과: `/home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target v3.png`
- `dashboard.next-action`: 제거
- `dashboard.core-flow`: Dashboard에서 숨김
- `dashboard.quick-actions`: 새 프로젝트, 기존 프로젝트 등록, 최근 프로젝트 열기, 자료 조사 시작
- `dashboard.project-list`: 하나의 큰 통합 Panel로 확대
- `dashboard.background-jobs`와 `dashboard.recent-completions`: 좁은 보조 Rail 유지
- SHA-256: `927eb3121080ea0d9770f0a1f533bdf60cf0a826f64053c49e4a88ff72eea0e2`

휴대폰 연결·동기화 판정:

- 390·430 Preview 자체는 PC 내부 Viewport 검증이다.
- 별도로 승인된 PM1 Thin UI 계약에 프로젝트 작업실의 휴대폰 연결·동기화 Panel이 포함된다.
- Core `allowed_actions`의 `open_on_phone`만 표시·실행한다.
- 기본 연결은 USB + `adb reverse`이며 `scrcpy`는 선택 기능이다.
- 연결 상태와 실제 기기 Preview 상태를 Panel에서 표시하되, 연결 실패 시 PC Preview와 다른 프로젝트는 계속 동작한다.
- 이것은 계정 기반 Cloud Sync나 LAN 공개가 아니다. Cloud Sync와 무선 ADB 외부 공개는 제외한다.
- 현재 상태는 승인된 설계 계약이며 아직 설치·구현·검증 완료 상태가 아니다.

### 8.3 Dashboard v4와 PM1 누락 감사

- 결과: `/home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target v4.png`
- Sidebar: 어두운 Navy 면을 밝은 Ice Blue 계열로 변경
- `dashboard.core-flow`: 기본 숨김, `제작 흐름 보기` Disclosure로만 표시
- SHA-256: `1131958609e616f5d7c301efe6d8157d3d924cc0f9722f3726d3882744e0d387`

현재 시안에 반영됨:

- 프로젝트 검색·유형 Filter·목록
- 프로젝트 상태·다음 행동·최근 변경·열기
- 빠른 실행
- 백그라운드 작업·최근 완료
- Docker 진입점
- 390·430 고객 결과물 비교
- 통과·수정 요청·중단
- Reference·실제 사용 Skill·도구 표시
- 기술 상세 접기

아직 Visual Target이 필요한 항목:

- 작업실 휴대폰 연결·동기화 Panel: USB + `adb reverse`, 선택 `scrcpy`, `open_on_phone`
- 저장되지 않은 변경 표시
- 마지막 검증 시점
- 결과물·전달 준비 상태
- 최소 오류 보고서와 Preview 장애 상태
- `제작 흐름 보기`의 펼친 상태
- 프로젝트별 자식 작업 보드 또는 작업 기록 진입 상태
- `allowed_actions`에 따른 Action 노출·비활성 상태

범위 주의:

- `새 프로젝트`와 `기존 프로젝트 등록`은 PM2 기능이다. PM1 Dashboard에 빠른 실행 진입점은 둘 수 있지만 PM2 구현 전에는 실제 동작 완료처럼 표시하지 않는다.
- 빠른 실행도 Core `allowed_actions` 또는 Capability 상태가 제공한 항목만 활성화한다.

### 8.4 Dashboard v5와 프로젝트 작업실 v3

Dashboard 확정 후보:

- 파일: `/home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target v5.png`
- 빠른 실행 높이 축소
- `제작 흐름 보기`를 프로젝트 Panel Header로 이동
- PM2 기능인 `새 프로젝트`·`기존 프로젝트 등록`을 `PM2 준비 중` 비활성 상태로 표현
- SHA-256: `967c29566be638ac96d33cd5326cbf6f27ea103d54ae63c0b2efb9ae1270bb0e`

프로젝트 작업실 수정 후보:

- 파일: `/home/user/바탕화면/v2_ui_images/프로젝트 작업실 PC Visual Target v3.png`
- Sidebar 이후 전체를 하나의 큰 통합 작업 Panel로 구성
- 내부 Divider로 요청·후보, 390·430 Preview, 연결·근거·검증 Inspector 구분
- 휴대폰 연결: USB, `adb reverse`, Galaxy 후보, `연결 확인`, 선택 `scrcpy`
- 증거 없는 연결 성공 표시를 제거하고 `확인 전`으로 정정
- 저장되지 않은 변경 `없음`, 마지막 검증 `확인 전`, 전달 준비 `준비 전`
- 기술 상세와 오류 상세 기본 접힘
- SHA-256: `c45a8f8f632ccba140b18fdc8e1791dc0e9c82e75cb5afb7aff57870b5a45c1c`

두 시안은 **OpenAI built-in ImageGen**으로 기존 Visual Target을 부분 수정했다. UI UX Pro Max·Figma는 사용하지 않았다.

### 8.5 단일 Mobile Preview와 부분 수정 Panel

- 파일: `/home/user/바탕화면/v2_ui_images/프로젝트 작업실 PC Visual Target v4 부분수정.png`
- SHA-256: `65d1541a0b3f74e3dc27ac33e55d9cb6bb814ddc0222119e856613d2aadb709f`
- 390·430 두 Preview를 하나의 Preview Panel로 통합
- 기본 Viewport는 430px이며 390px Button은 같은 결과의 폭만 전환
- Viewport 전환 시 Scroll·선택·Draft 상태 유지
- 화면에는 하나만 표시하지만 적용 전 390·430 자동 회귀검사 유지

부분 수정 Workflow:

1. Preview에서 안정적인 Section ID 선택
2. 오른쪽 `부분 수정` Panel에서 허용 속성만 변경
3. Draft 상태로 보존
4. `미리보기`로 제품 파일을 덮어쓰지 않고 결과 확인
5. 390·430·Console·가로 넘침 회귀검사
6. PASS 후에만 `적용`
7. `원래대로`로 선택 Version 복구

첫 허용 속성:

- Section 순서
- 콘텐츠 폭
- Padding
- Text 크기
- 배경색
- 표시·숨김

금지:

- 자유 Canvas Drag & Drop
- 임의 Resize
- Raw CSS 입력
- 검증 없는 즉시 덮어쓰기
- Section ID가 없는 영역 수정

오른쪽 Inspector는 `부분 수정`, `휴대폰 연결`, `근거` Tab으로 통합한다. 부분 수정의 `적용`과 전체 결과의 `통과`는 서로 다른 Action이다.

### 8.6 Core 경유 여부 정정

이번 PM1 UI는 **V2 Core를 활용한 디자인 생성·채택·적용·부분 수정의 첫 통합 테스트**다.

현재까지 생성한 Dashboard·Workspace 수정 이미지는 Core Run을 거치지 않고 **OpenAI built-in ImageGen**으로 직접 생성했다. 따라서 `external_direction_evidence`이며 공식 Visual Target이나 구현 입력이 아니다.

저장소에서 확인한 실제 Core 기능:

- `design generate`: Run 안에서 UI UX Pro Max → frontend-app-builder → Browser 검증을 실행하지만 현재 병원 웹 A/B와 mobile-first 요구가 코드에 고정되어 PM1 V2 운영 UI에 그대로 사용할 수 없음
- `design import`: 외부 이미지를 수동 Reference Artifact로 보존
- `design direction select`: 사용자 방향 선택과 구현 차단 Gate 기록
- `design visual-target register/verify/approve`: Run 내부 생성 이미지·Prompt·Reference·도구 증거·SHA-256 검증과 승인
- `design fidelity record/promote`: 승인 Visual Target과 구현 Fidelity PASS 후 코드 Source of Truth 승격
- M6 Quick Change: 자연어 기반 AI 부분 수정·회귀·Rollback/Restore 검증 완료
- 직접 시각 조절 Panel: 아직 미구현

이후 테두리 강화, Layout 순서 변경, 여백 조절과 디자인 수정은 다음 Core 경로로 검증한다.

1. PM1 V2 UI 전용 Core Design Run 준비
2. 현재 방향 이미지를 Reference Evidence로 Import
3. 사용자 요청을 Intent·Design Change 요구사항으로 기록
4. Core가 Run 안에서 새 Visual Target 생성
5. `visual-target register → verify`
6. 사용자 시각 승인
7. 승인 후 Image-to-Code
8. Section ID 기반 Change Run으로 테두리·순서·여백 수정
9. 390·430 자동 회귀와 Rollback/Restore 검증

```yaml
current_images:
  role: external_direction_evidence
  generated_through_v2_core: false
  official_visual_target: false
  implementation_input_allowed: false
```

```yaml
v2_operator_ui:
  target: desktop_only
  required_viewport: 1440
  mobile_variant_required: false

produced_customer_results:
  mobile_required: true
  required_viewports: [390, 430]

pm0:
  design: completed
  operational_gate: not_completed

pm1:
  baseline_direction: existing_dashboard_and_workspace_pc_targets
  revision_version: v2
  visual_target_approved: false
  image_to_code_started: false
  implementation_started: false

repository_changes:
  core_or_product_code_changed: false
  run_changed: false
  commit_created: false
  push_performed: false
```

다음 Gate는 사용자가 1·2·3 중 하나를 선택하거나 혼합 방향을 지정하는 것이다. 선택 전에는 Image-to-Code, PM1 실제 구현, 새 Run, Commit, Push를 수행하지 않는다. PM1이 완료된 뒤 PM1 변경만 별도 Commit한다.
