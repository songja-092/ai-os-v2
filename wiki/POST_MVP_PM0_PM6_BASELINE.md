# AI OS V2 Post-MVP PM0~PM6 공식 기준

작성일: 2026-08-17
상태: 사용자 승인 완료·설계 완료
적용 범위: Post-MVP 계획만
보존 범위: Core MVP M1~M7, 기존 Run·Artifact·Commit

## 1. 공식 순서

```text
PM0 운영환경 준비
→ PM1 디자인 탐색·채택
→ PM2 조립식 V2 보드
→ PM3 부분 수정
→ PM4 자료 조사
→ PM5 사용자 의도 정합성
→ PM6 전체 통합·최종 검증
```

이 문서는 과거 Post-MVP PM0~PM7 번호 체계를 대체합니다. 기능을 삭제한 것이 아니라 이동·통합해 중복을 제거했습니다. Core MVP M1~M7의 완료 판정과 증거에는 영향을 주지 않습니다.

## 2. PM별 책임과 PASS

### PM0 — 운영환경 준비

목적: 기존 프로젝트를 손상하지 않고 실제 구현을 반복 실행·복구할 수 있는 환경을 만듭니다.

구현 범위:

- 격리 Worktree와 고정 Runtime·실행 명령
- 고정 Port와 `strictPort` 충돌 차단
- Antigravity 안전 실행
- Preview 장애 격리
- 외부 Backup·Rollback·Restore
- 새 Codex 세션 재현

PASS:

- 새 세션에서 같은 환경을 재현합니다.
- 병원 웹과 PDF Preview를 독립 실행합니다.
- Preview 실패가 Core와 다른 프로젝트에 전파되지 않습니다.
- Backup 표본의 Restore를 확인합니다.

### PM1 — 디자인 탐색·채택

목적: AI 생성안만 반복하지 않고 사용자가 더 다양하고 좋은 디자인을 눈으로 선택하게 합니다.

후보 구성:

- 검증된 외부 Block 조합 A
- 구조가 다른 외부 Block 조합 B
- 현재 디자인 유지안
- 필요한 경우에만 AI 보완안

구현 범위:

- 검색 전 `Reference Brief` 작성: 화면 목적, 사용자, 필수 정보, 핵심 행동, 정보 밀도, PC·모바일 기준, 유지할 V2 규칙, 제외할 디자인
- 공식 Registry, 라이선스가 확인된 OSS와 검증된 디자인 시스템 우선 조사
- 출처·라이선스·의존성·기술 호환성 확인
- 실제 Reference 10개 이상을 `Reference Board`에 공개하고 구조가 겹치는 후보를 제거
- 같은 평가 기준으로 분석한 추천 방향 3~5개와 현재안 비교
- 전체 구조·특정 Section·Design DNA를 마우스와 간단한 선택 버튼으로 선택
- V2 기본 Typography·Color·Button 규칙으로 시각 통일
- 선택 출처·Section ID·Design Recipe 기록
- 저비용 구조 Preview 1~2개 뒤 실제 데이터 Code Preview 1개만 제작
- 승인된 Visual Target 등록과 승인 전 구현 차단

입력 우선순위와 채택 방식:

```yaml
pm1_input_priority:
  primary: mouse_selection
  secondary: simple_choice_buttons
  fallback: natural_language

adoption_methods:
  recommended:
    description: V2가 Reference 10개 이상을 조사하고 추천 3개를 표시
  bring_reference:
    description: 사용자가 URL 또는 Screenshot을 제공하고 사용할 부분을 선택
  direct_assembly:
    description: 검증된 Block·Section 보관함에서 선택해 저비용 구조 Draft로 원하는 순서를 조합
```

- 어느 방식에서도 현재안을 유지할 수 있습니다.
- 방식을 전환해도 이미 고른 Reference는 해당 Draft의 임시 후보로 보존합니다.
- 추천 3개를 먼저 표시하되 전체 Reference 목록을 열람할 수 있습니다.
- 최종 실제 데이터 Code Preview는 하나만 제작합니다.
- 사용자가 중단하면 제품·Recipe·Registry를 변경하지 않습니다.
- PM1은 특정 디자인의 채택뿐 아니라 채택 방식 자체가 편한지 시험합니다. 불편하다고 판정한 방식은 기본 Workflow로 승격하지 않고 다른 방식으로 전환합니다.
- PM1의 직접 조립형은 이미지·구조 Draft와 격리 Code Preview 수준입니다. 실제 Module Registry 등록·장착·상태 저장·장애 격리는 PM2에서만 구현하며 PM1이 PM2 Gate를 우회하지 않습니다.

Reference는 두 종류를 구분합니다.

- `visual_reference`: 구조·분위기만 참고하며 코드를 복사하지 않습니다.
- `reusable_code_block`: 라이선스·의존성·코드를 확인한 뒤 실제 재사용 후보로 다룹니다.

평가 항목은 `task_fit`, `information_hierarchy`, `implementation_feasibility`, `responsive_quality`, `accessibility`, `license_clarity`, `v2_design_system_fit`, `section_reusability`이며 각 0~5점입니다. 점수는 추천 근거일 뿐 자동 선택 근거가 아니며 최종 선택은 사용자가 합니다. `UI UX Pro`는 사용성·구조 분석 보조 도구이고 `Taste Skill`은 미검증 평가 후보입니다.

PASS — 디자인 품질:

- 출처와 라이선스를 확인한 구조적으로 다른 후보가 존재합니다.
- Reference 10개 이상과 추천 방향 3~5개가 사용자에게 공개됩니다.
- 모든 후보를 같은 데이터와 Viewport로 비교합니다.
- 사용자가 현재안보다 나은 방향 또는 현재안 유지를 명시적으로 선택합니다.
- 선택 결과가 Visual Target·Section ID·Design Recipe에 연결됩니다.
- 사용자 승인 전 PM2 구현을 시작하지 않습니다.

PASS — 채택 편의성:

- 전문용어와 자연어 입력 없이 선택 흐름을 완료합니다.
- 현재안·추천형·Reference 가져오기·직접 조립형 사이를 전환할 수 있습니다.
- 전체 화면과 특정 Section을 각각 선택할 수 있습니다.
- 실제 V2 데이터 Preview를 확인합니다.
- 채택·다른 방식·중단 중 하나를 선택할 수 있습니다.
- 사용자가 채택 방식이 편하다고 명시적으로 판정합니다.
- 중단 시 제품·Recipe·Registry 변경이 없습니다.

제외: 대규모 자동 수집기, 새 DB, 자동 Template 혼합, 출처 없는 복제.

### PM2 — 조립식 V2 보드

목적: PM1에서 승인한 디자인을 실제로 조립·격리·복원 가능한 보드로 작동시킵니다.

구현 범위:

- PC 전용 V2 UI Shell과 Project Registry
- Slot Renderer
- 검증 가능한 Module Manifest와 정적 Module Registry
- `project_home`, `workspace_preview`, `workspace_tools`, `background_capability` Slot
- 기존 기능 Module 2개 장착
- Module 순서 이동과 활성화·비활성화
- Module 오류·Preview 장애 격리
- 순서·활성 상태 복원
- 실제 `V2 Core → ui-state → UI → ui-action → V2 Core`
- 로컬 프로젝트 등록·전환·이름 변경·보관·복원

PASS — 조립 기능:

- 유효한 Manifest의 Module만 장착됩니다.
- Module 2개를 이동하고 하나를 비활성화할 수 있습니다.
- 한 Module 실패가 Core·다른 Module·다른 프로젝트에 전파되지 않습니다.
- 이전 순서와 활성 상태를 복원합니다.
- Core가 허용하지 않은 Action은 표시하거나 실행하지 않습니다.
- 프로젝트별 Run·Preview·결과가 섞이지 않습니다.

예쁜 화면만으로 조립 기능을 PASS하지 않고, Module 동작만으로 PM1 디자인 품질을 PASS하지 않습니다.

### PM3 — 부분 수정

목적: 승인된 보드와 고객 결과물을 제한된 범위에서 안전하게 수정합니다.

구현 범위:

- 마우스로 Section·Module Card 선택
- Card Drag & Drop, 위·아래 이동 버튼과 허용된 Slot 간 이동
- Property Panel에서 여백·크기·순서·표현·표시 상태 변경
- Manifest가 허용한 Module 인스턴스 복제와 Draft 배치에서 제거
- 변경 전후 Preview
- 새 Design Version
- 적용·폐기·이전 Version 복구
- 고객 결과물 390px·430px 모바일 회귀검증
- 조건부 Visual Editor Adapter를 통한 Module·Section 이동, 제한된 Resize, 표시·숨김과 허용 속성 편집

입력과 제한값:

```yaml
pm3_input_priority:
  primary: [drag_and_drop, up_down_buttons, property_panel]
  accessibility_alternative: [keyboard_control, move_buttons]
  fallback: [natural_language]

size_presets:
  width: [small, medium, large, full]
  height: [compact, normal, expanded]
spacing: [small, medium, large]
font_size: [small, medium, large]
```

직접 편집도 항상 Recipe Diff를 만듭니다. Drag와 이동 버튼은 같은 이동 명령을 생성하고 같은 Slot 또는 Manifest가 허용한 Slot으로만 이동합니다. `Undo·Redo`는 현재 Draft 안에서 작동하며 적용 뒤 복구는 Core Version Restore를 사용합니다. 변경 전후 비교 전에는 적용할 수 없고 사용자 승인 전 실제 제품을 변경하지 않습니다.

복제·삭제 경계:

- `duplicate`는 Manifest의 `max_instances`와 복제 권한이 허용한 Module 인스턴스에만 적용합니다.
- `remove_from_draft`는 코드·Manifest·Registry 삭제가 아니라 현재 Draft 배치에서만 제거합니다.
- 제거한 Section은 현재 Draft에서 Undo할 수 있습니다.
- Core 필수 Module은 제거할 수 없습니다.
- Module 오류는 해당 Card의 Error Boundary에만 격리합니다.

PASS:

- 선택한 Section 이외의 변경이 없습니다.
- 변경 전후를 확인하고 취소·적용할 수 있습니다.
- 새 Version과 Restore 지점이 존재합니다.
- 모바일 핵심 흐름이 깨지지 않습니다.
- Card 순서 변경, 허용 Slot 이동, 제한 Resize, 복제·Draft 제거와 Undo가 동일 Recipe Diff·Version 규칙으로 재현됩니다.

기존 M6 Quick Change 증거는 자연어 국소 수정의 선행 증거로 보존하지만 직접 보드 편집 완료 증거로 확대하지 않습니다.

`Puck`은 PM1 기능이 아니라 PM3의 제거 가능한 Visual Editor Adapter 후보입니다. PM2 PASS와 별도 승인 전에는 설치하지 않습니다. `React Grid Layout`은 Puck만으로 승인된 Panel Resize를 충족하지 못한다는 증거가 생길 때만 보조 후보로 검토하며, 현재 `Craft.js`로 전환할 근거는 없습니다.

## 2-1. PM1~PM3 설계 계약

### Design Recipe

V2는 디자인 원본으로 Versioned Design Recipe를 소유합니다. 최소 필드는 다음과 같습니다.

```yaml
recipe_id: string
schema_version: "1.0"
project_id: string
target_surface: v2_board | customer_product
version: integer
base_version: integer | null
status: draft | approved | applied | discarded | restored
sections:
  - section_id: string
    module_id: string
    slot_id: string
    order: integer
    visible: boolean
    layout: {column, row, width, height, min_width, max_width, min_height, max_height}
    style: {spacing_token, font_token, color_token, typography_scale}
    reference_ids: [string]
references:
  - reference_id: string
    type: visual_reference | reusable_code_block
    name: string
    url: string
    used_part: string
    applied_section_ids: [string]
    license: string
    access_status: verified | inaccessible | user_screenshot
    adoption_status: candidate | selected | verified | reusable
changes:
  - change_id: string
    command: string
    target_section_id: string
    target_viewport: shared | desktop | mobile
    property: string
    before: any
    after: any
    source: direct_edit | natural_language | restore
```

직접 편집과 자연어 편집은 같은 `changes[]`를 생성합니다. 기존 Version을 덮어쓰지 않고 항상 새 Draft를 만들며 사용자 승인 후 `approved`, Core 검증 후 `applied`로 전환합니다. 취소는 `discarded`, Restore는 과거 Version을 복사한 새 Draft입니다. Puck JSON은 Recipe에 저장하지 않습니다.

반응형 계약:

```yaml
responsive:
  shared:
    spacing_tokens: {}
    typography_tokens: {}
    component_rules: {}
  desktop:
    required_for: [v2_board]
    layout: {}
    order_overrides: []
    hidden_section_ids: []
  mobile:
    required_for: [customer_product]
    breakpoint: 430
    validation_widths: [390, 430]
    layout: {}
    order_overrides: []
    hidden_section_ids: []
```

`v2_board`는 PC Recipe가 필수이고 모바일은 선택입니다. `customer_product`는 모바일 Recipe가 필수입니다. 공통 속성과 Viewport Override를 분리하고 PC 변경은 모바일 Override를 자동 변경하지 않습니다. 390·430은 별도 디자인이 아니라 하나의 모바일 규칙을 검증하는 Viewport입니다. Restore는 공통 속성과 Override를 함께 복원합니다.

### Module Manifest와 Slot Renderer

Manifest는 `manifest_version`, `module_id`, `display_name`, `module_version`, `adapter_type`, `allowed_slots`, `required_state`, `emitted_actions`, `permissions`, `health`, `status`를 포함합니다. Slot Renderer는 다음 순서를 지킵니다.

```text
Manifest Schema 확인 → Registry 등록 확인 → Slot 허용 확인
→ Core 권한 확인 → Module별 Error Boundary에서 Render
→ 실패한 Module만 Fallback
```

Registry에 없거나 허용되지 않은 Module·Slot·Action은 거부합니다. Module은 Core 상태를 직접 수정하지 못합니다. 배치 변경은 새 Recipe Version으로 저장하며 비활성화와 실패 뒤에도 Recipe·Artifact·이전 배치를 복원할 수 있어야 합니다.

### Puck Adapter

```text
V2 Design Recipe → RecipeToPuckAdapter → 임시 Puck Config·Data
→ 사용자 편집 → PuckToRecipeDiffAdapter → Core Schema·권한 검증
→ Draft Preview → 사용자 승인 → 새 Recipe Version
```

Puck은 Version이나 Core Action을 소유하지 않고 Puck Data와 전용 Component ID를 Source of Truth로 사용하지 않습니다. 제거할 때 Editor Route와 Adapter 연결을 끊고 Package를 제거해도 일반 Slot Renderer가 Recipe를 Render해야 하며 Design Recipe, Version, Reference, Diff, 승인 기록, Preview, 적용 코드와 Artifact가 유지되어야 합니다.

### PM4 — 자료 조사

목적: 프로젝트 제작과 병목 해결에 필요한 출처가 확인된 자료를 확보합니다.

구현 범위:

- 공식 웹·문서와 GitHub 조사
- Reddit 조사
- 사용자가 제공한 Threads 자료
- PDF·Markdown·Text·Screenshot
- 프로젝트 병목 조사
- Source·수집 시점·공식 자료와 보조 의견 구분
- `Collection Request → Collector → Analyzer → 사용자 선택 → 격리 검증 → 채택` 상태 분리
- Source Adapter별 Timeout·후보 수 제한과 수동 URL·파일 입력 대체 경로

최소 계약:

```yaml
collection_request:
  request_id: string
  project_id: string
  research_question: string
  purpose: string
  allowed_source_types: [official_web, github, reddit, user_file, user_screenshot, user_provided_text]
  exclusion_rules: []
  maximum_candidates: integer
collector_output:
  collection_id: string
  status: collected | partial | inaccessible | failed
  sources: []
analyzer_output:
  analysis_id: string
  claims: []
  candidates: []
  beginner_summary:
    recommended_count: 3
    next_single_action: string
```

Collector는 수집 사실만 기록하고 사실 판정·추천·채택을 하지 않습니다. 주요 주장은 Source ID와 연결하며 증거를 `official | primary | secondary | community_opinion`으로 구분합니다. 접근하지 못한 내용 추정, Star·조회수만으로 채택, License 불명확 후보 설치를 금지합니다. 상태는 `collected → analyzed → candidate → user_selected → isolated_verified → adopted → reusable`로 분리합니다.

PASS:

- 주장과 출처가 연결됩니다.
- 공식 자료와 보조 의견이 구분됩니다.
- 조사 실패가 Core와 기존 제작 기능을 막지 않습니다.
- 승인 전 제품을 변경하지 않습니다.

제외: 로그인·유료 제한 우회, 무단 대량 Scraping, 상시 수집 Agent, 별도 Queue·Worker·DB.

### PM5 — 사용자 의도 정합성

목적: AI가 요청을 잘못 이해한 상태로 구현을 시작하지 못하게 합니다.

구현 범위:

- 사용자 원문과 Intent Packet
- AI Intent Receipt
- 변경·비변경 범위
- Acceptance Checks
- 구현 전 불일치 차단과 구현 후 원문 비교

최소 계약:

```yaml
intent_packet:
  packet_id: string
  packet_version: integer
  project_id: string
  original_request: string
  clarified_request: string
  target_environment: string
  build_scope: []
  preserve_scope: []
  excluded_scope: []
  acceptance_checks: []
  constraints: []
  unresolved_questions: []
  risk_classification: string
scope_lock:
  intent_packet_version: integer
  scope_hash: string
  approved_by_user: boolean
  approved_at: string
  editable_targets: []
  protected_targets: []
```

초보자에게는 `만들 것`, `유지할 것`, `건드리지 않을 것`, `완료 확인 방법`과 `맞아요`, `수정할게요`만 기본 표시합니다. 사용자 원문 충돌, 미해결 질문, 범위 초과, 보호 대상 변경, Acceptance 누락 또는 Target Environment 불일치 시 구현을 차단합니다. 구현 뒤 최초 원문·승인 Intent Version·실제 변경·보존 범위·Acceptance 결과를 다시 비교하고 불일치하면 완료·Commit을 차단합니다.

PM5 구현 전 임시 Gate:

- 공식 순서상 PM5는 의도 정합성 기능을 Core 일반 기능으로 완성하는 단계입니다.
- PM1~PM4에서도 구현·Preview 제작 전에 동일 필드의 수동 Intent Receipt와 Scope Lock을 문서로 사용합니다.
- 수동 계약은 PM5 완료 증거가 아니며, PM5 PASS 뒤 Versioned Core 계약으로 교체합니다.
- 따라서 PM5가 뒤 번호라는 이유로 앞 단계가 사용자 의도 확인 없이 진행되지 않습니다.

PASS:

- 구현 전 사용자 요청과 AI 이해가 일치합니다.
- 범위 충돌이나 누락이 있으면 구현을 차단합니다.
- 구현 결과를 최초 요청과 다시 비교합니다.

### PM6 — 전체 통합·최종 검증

목적: PM0~PM5가 하나의 안전하고 복구 가능한 제작 흐름으로 작동하는지 확인합니다.

통합 흐름:

```text
프로젝트 등록 → 의도 확인 → 자료 조사 → 디자인 탐색·선택
→ 보드 조립 → 부분 수정 → 최종 Preview → 승인
→ Commit·Rollback·Restore → 결과 전달
```

PASS:

- 초보자가 마우스 선택·간단한 버튼·Preview 중심으로 전체 과정을 완료하며 자연어는 보조 입력으로만 사용합니다.
- 프로젝트와 Run이 섞이지 않습니다.
- 실패 단계에서 중단·재개할 수 있습니다.
- 승인 결과를 저장하고 이전 상태로 복구합니다.
- 최종 Preview·검증 보고서·실행 방법·제한사항을 함께 전달합니다.

중단·재개 계약은 `project_id`, 공식 PM 순서, PM별 상태, Evidence Version, stale 증거, 현재 Blocker와 다음 행동 하나를 보존합니다. 재개 시 Core·제품 Commit, Intent·Recipe Version, Port·Worktree와 stale 증거를 다시 확인합니다. 기술 PASS와 사용자 PASS는 분리합니다.

Capability 제거 시험은 `비활성화 → 진행 작업 안전 중단 → Manifest·Adapter 연결 해제 → 전용 Package 제거 → 수동 Workflow 복귀 → Build·Core 회귀 → 과거 Artifact·Recipe 조회 → removed 상태·이유 기록`을 따릅니다.

## 2-2. Beginner Assistance Layer

Beginner Assistance Layer는 새 Core나 별도 상태 저장소가 아니라 `Core ui-state`를 쉬운 표시와 선택으로 바꾸는 제거 가능한 Adapter입니다.

```text
V2 Core ui-state → Beginner Assistance Adapter
→ 쉬운 상태 설명·다음 행동 하나·최대 3개 선택지
→ allowed_actions 안의 사용자 선택 → V2 Core
```

Core는 상태, `allowed_actions`, 승인, Run, Version, Artifact, Commit·Rollback·Restore, 검증 결과와 공식 Project Memory를 소유합니다. Layer는 쉬운 문장, 선택지, 접힌 기술정보, 문제 신고와 사용자용 Version 이름만 담당합니다. Core 상태 추측·직접 수정, 사용자 대신 PASS, 추천 자동 실행, Git·Shell 직접 실행과 별도 공식 기억 저장을 금지합니다.

공통 행동은 `추천대로 진행`, `직접 선택`, `문제 있어요`, `이전 상태로`이며 항상 네 개를 표시하지 않고 현재 `allowed_actions`에 있는 최대 3개만 보여줍니다. Action은 `expected_state_version`을 포함하고 Core가 다시 권한과 상태를 검증합니다. Layer를 제거해도 표준 UI 또는 CLI Workflow, Run·Version·Artifact·Memory와 Restore가 유지되어야 합니다.

## 2-3. 실제 휴대폰 Preview Adapter

휴대폰 연결은 Cloud Sync가 아니라 고객 결과물의 실제 기기 검증을 위한 선택형 Adapter입니다.

- 기본 후보는 USB와 `adb reverse`, 선택 후보는 `scrcpy`입니다.
- 계정 기반 Cloud Sync, 개인 파일 동기화, 프로젝트 복사, 무선 ADB 외부 공개와 자동 업로드는 제외합니다.
- PM0은 `adb` 가용성·Port·프로세스 정리와 실패 격리 가능성을 확인하되 실제 기기가 없으면 `optional_adapter_ready`로 기록하고 PM 전체를 차단하지 않습니다.
- PM1은 `휴대폰에서 보기`, `화면 미리보기만 보기`, `나중에 하기`를 제공하며 실패 시 390·430 Browser Preview로 전환합니다.
- PM3은 Card 순서·크기·여백 변경 뒤 휴대폰 Preview 갱신과 모바일 Override를 검증합니다.
- PM6은 실제 기기 터치·스크롤·입력, 연결 해제 뒤 PC 작업 지속, `adb reverse` 정리와 Browser Preview 대체를 통합 검증합니다.
- 기본 화면에는 `ADB`, Port, IP, PID와 `scrcpy`를 숨기고 `자세히`에서만 표시합니다.

## 3. 고정 Gate

```text
PM0 FAIL → 실제 Post-MVP 구현 금지
PM1 디자인 품질 FAIL → PM2 구현 금지
PM2 조립 기능 FAIL → PM3 및 영상·3D Adapter 추가 금지
PM3 FAIL → 부분 수정 완료 선언 금지
PM4·PM5 FAIL → 해당 프로젝트 구현 진행 금지
PM6 FAIL → Post-MVP 완료 선언 금지
```

모든 PM의 실제 변경 전에는 승인된 Intent Receipt와 Scope Lock이 필요합니다. PM5 PASS 전에는 수동 문서 Gate를 사용하고 PM5 이후에는 Core가 Version·Hash·stale 상태를 검증합니다.

영상·3D 같은 새 기능은 PM2 조립식 보드 PASS 이후 별도 Adapter·Preview Module 후보로 검토합니다.

## 4. 기존 PM 기능·증거 매핑

| 이전 Post-MVP 기능 | 새 위치 | 판정 | 기존 증거 |
|---|---|---|---|
| PM0 운영환경 | PM0 | 유지 | 원본 ID·경로로 보존 |
| PM1 대시보드·작업실 | PM2 | 조립식 보드로 이동 | Preview는 당시 판정 그대로 보존 |
| PM2 로컬 프로젝트 관리 | PM2 | Project Registry에 통합 | 보존 |
| PM3 디자인 Reference | PM1 | 디자인 탐색으로 이동 | Reference 출처·Artifact 보존 |
| PM3 일반 자료·병목 조사 | PM4 | 유지 | Run·분석 Artifact 보존 |
| PM4 사용자 의도 확인 | PM5 | 이동 | 계약·검증 증거 보존 |
| PM5 디자인 다양성 | PM1 | 디자인 탐색과 통합 | 후보·선택 증거 보존 |
| PM6 최신 디자인 조사 | PM1 | 후보 조사와 통합 | 출처 증거 보존 |
| PM6 부분 수정 | PM3 | 이동 | M6 Quick Change 증거 보존 |
| PM7 전체 통합 | PM6 | 번호 이동 | 원래 Run·Commit·Artifact 보존 |

증거 보존 원칙:

- 기존 `run_id`, Commit SHA, Artifact 경로와 SHA-256을 변경하지 않습니다.
- 당시 PASS·FAIL·rejected 판정을 그대로 유지합니다.
- 새 PM 번호는 별도 매핑으로만 연결합니다.
- 과거 증거가 검증하지 않은 새 기능까지 PASS한 것으로 확대하지 않습니다.
- Core MVP M1~M7 파일과 완료 기록을 수정하지 않습니다.

## 5. 현재 상태

```yaml
core_mvp_m1_m7: completed_and_frozen
post_mvp_design: completed
design_completion_scope: contracts_only
official_post_mvp_sequence: PM0_to_PM6
active_gate: PM0
pm1_design_exploration: not_started_under_new_baseline
pm2_modular_board: not_started
pm3_to_pm6: not_started
pm1_adoption_method: test_not_finalized
pm0_operational_readiness: blocked
```

Post-MVP 설계 계약은 완료됐습니다. 이는 구현·도구 채택·사용 방식 승격 완료를 뜻하지 않습니다. 다음 구현 작업은 PM0 Gate를 완료하는 것입니다. PM0 PASS 후 PM1에서 추천형·Reference 가져오기·직접 조립형을 실제로 비교하고 사용자가 편하다고 판정한 방식만 기본 Workflow 후보로 승격합니다.

생산 배포·운영 관찰과 10년차 전문가 수준 판정은 PM0~PM6 완료만으로 선언하지 않습니다. 배포 가능한 프로젝트에서 별도 승인된 Deployment·Monitoring Adapter와 여러 프로젝트 재현 증거를 축적하는 `Professional Capability Program`의 후속 범위입니다.
