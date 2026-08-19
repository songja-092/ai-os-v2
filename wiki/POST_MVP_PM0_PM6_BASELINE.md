# AI OS V2 Post-MVP PM0~PM6 공식 기준

작성일: 2026-08-17
최종 갱신: 2026-08-18
상태: 사용자 승인 완료·설계 완료
적용 범위: Post-MVP 계획만
보존 범위: Core MVP M1~M7, 기존 Run·Artifact·Commit

## 1. 공식 순서

```text
PM0 운영환경·Capability Lab 준비
→ PM1 디자인 전략·탐색·채택
→ PM2 조립식 제작 보드
→ PM3 부분 수정·Motion Adapter
→ PM4 조사·Design Intelligence
→ PM5 사용자 의도·범위·자산 정합성
→ PM6 전체 통합·품질·복구 검증
```

이 문서는 과거 Post-MVP PM0~PM7 번호 체계를 대체합니다. 기능을 삭제한 것이 아니라 이동·통합해 중복을 제거했습니다. Core MVP M1~M7의 완료 판정과 증거에는 영향을 주지 않습니다.

### 1-1. 2026-08-18 최종 제작 흐름

```text
쉬운 사용자 요청
→ PM5 수동 Intent·Scope Lock 선행 적용
→ 기존 성공 Recipe·Block으로 해결 가능한지 확인
→ 부족할 때만 PM4 V2 Collector가 제한 조사
→ PM1에서 업종·사용자·핵심 행동에 맞는 Brief·Block·Visual Target 1개 승인
→ PM2에서 승인된 Recipe·Block을 실제 Module로 조립
→ PM3에서 마우스로 순서·크기·여백·표현을 부분 수정하고 필요할 때만 Motion·3D Adapter 적용
→ PM5에서 최초 요청·변경 범위·공용/맞춤/고객 전용 자산 재확인
→ PM6에서 디자인·기능·접근성·성능·회귀·복구 통합 검증
→ 사용자 최종 승인
→ 성공한 Recipe·Block·Adapter만 재사용 자산으로 승격
```

사용자가 보는 표준 행동은 `추천대로 진행`, `직접 선택`, `문제 있어요`,
`이전 상태로`를 기본으로 하고 현재 `allowed_actions`에 있는 행동만 표시합니다.

### 1-2. 다양성과 도구 확장 원칙

- 다양성은 반복 ImageGen이 아니라 `Verified Code Block + Layout Recipe + Style Pack + Industry Pattern + Motion·3D Module`의 조합으로 만듭니다.
- 같은 업종 100개를 제작해도 색상만 바꾸지 않고 고객·진료·사업 전략에 따라 정보 우선순위·Layout·Navigation·Media·기능을 다르게 합니다.
- 기본형·성장형·프리미엄형 가격은 PM 기능 상태가 아닌 사업 운영 정책입니다. 다만 PM5는 현재 계약에서 재사용·맞춤·고객 전용으로 확정된 자산 경계를 보존합니다.
- 새 도구는 `발견 → 라이선스·최신성·의존성 감사 → Capability Lab 격리 시험 → 사용자 채택·보류·폐기 → 비활성 Adapter 등록 → 해당 PM의 실제 검증 → 활성`으로 추가합니다.
- 모든 외부 도구는 Feature Flag로 끄고 Adapter·Package를 제거해도 Design Recipe·Version·Reference·승인·Artifact가 남아야 합니다.
- 3D·Rive·dotLottie·영상 도구는 실제 고객 요구가 생긴 뒤 하나만 시험하며 PM2 조립 기능 PASS 전에는 V2에 장착하지 않습니다.

## 2. PM별 책임과 PASS

### PM0 — 운영환경·Capability Lab 준비

목적: 기존 프로젝트를 손상하지 않고 실제 구현을 반복 실행·복구할 수 있는 환경을 만듭니다.

구현 범위:

- 격리 Worktree와 고정 Runtime·실행 명령
- 고정 Port와 `strictPort` 충돌 차단
- Antigravity 안전 실행
- Preview 장애 격리
- 외부 Backup·Rollback·Restore
- 새 Codex 세션 재현
- 후보 Skill·Plugin·Library의 Repo-local 격리 폴더·가짜 Fixture·실행 증거·제거 경로
- 후보 Process의 비공개 Project·Git 기록·Secret 접근 차단

PASS:

- 새 세션에서 같은 환경을 재현합니다.
- 병원 웹과 PDF Preview를 독립 실행합니다.
- Preview 실패가 Core와 다른 프로젝트에 전파되지 않습니다.
- Backup 표본의 Restore를 확인합니다.

### PM1 — 디자인 전략·탐색·채택

목적: 사용자가 복잡한 디자인 탐색을 직접 수행하지 않고도 완성도 높은 실제 화면 하나를 빠르게 확인하고 승인·수정·거절하게 합니다.

기본 Workflow:

- 사용자가 쉬운 말로 원하는 화면을 요청합니다.
- V2는 필요한 경우에만 같은 화면 종류의 검증 가능한 Reference를 내부적으로 제한 조사합니다.
- `UI UX Pro`는 화면 유형·정보 우선순위·색상·Typography·Spacing·접근성 규칙과 금지 Pattern을 제안하고 최종 결과를 검사합니다.
- 기존 V2 결정과 실제 프로젝트 데이터를 사용해 Visual Target 하나만 제작합니다.
- 사용자는 실제 화면에서 `이 방향으로 진행`, `이 부분만 수정`, `다른 방향 보기`, `현재안 유지`, `중단`, `이전 상태로` 중 하나를 선택합니다.
- 첫 결과가 거절된 경우에만 거절 이유를 반영한 구조적으로 다른 대안 하나를 제작합니다.
- 사용자 최종 승인 전 PM2 구현·제품 적용·Design Recipe 승격을 차단합니다.

구현 범위:

- 간단한 `Reference Brief`: 화면 목적, 사용자, 필수 정보, 핵심 행동, 정보 밀도, 대상 Viewport, 유지할 V2 규칙, 제외할 디자인
- Reference가 필요하면 공식 자료·라이선스가 확인된 OSS·검증된 디자인 시스템을 우선하고 출처·접근 시점·라이선스·사용 Section·의존성을 기록
- `visual_reference`와 `reusable_code_block`을 구분하고 문구·Logo·브랜드 자산은 기본적으로 복제하지 않음
- 실제 V2 데이터와 동일한 Viewport·화면 상태·Theme·확대 비율·Motion 시점으로 Visual Target 하나를 제공
- Section ID를 유지한 부분 수정, 변경 전후 확인, 선택하지 않은 영역 보존
- 사용자가 요청할 때만 Reference 전체 목록·구역 선택·속성 선택 같은 상세 탐색 기능 제공
- 승인된 Visual Target 기록과 승인 전 구현 차단
- 기존 성공 Recipe·Block 우선 검색과 재사용 불가 사유 기록
- 업종·핵심 고객·핵심 진료/업무·핵심 행동을 디자인 차별화 축으로 고정
- 실제 구현 재료를 `Verified Code Block`, 배치를 `Layout Recipe`, 시각 규칙을 `Style Pack`으로 분리

입력 우선순위:

```yaml
pm1_input_priority:
  request: easy_natural_language
  review: actual_visual_preview
  primary_actions: simple_choice_buttons
  revision: section_selection_or_short_request
```

Reference Board·구역/속성 선택형 Visual Companion·Google Stitch는 사용자 Pilot에서 기존 방식보다 빠르거나 좋은 결과를 증명하지 못했으므로 기본 Workflow에서 제외하고 실패 증거로 보존합니다. `UI Remix` 연구는 실제 사례의 전체·부분 선택이 비전문가에게 도움이 될 수 있다는 외부 근거로 유지하지만, V2 사용자가 탐색과 선택을 부담스럽다고 판정했으므로 요청 시 선택 기능으로만 사용합니다. 자동 Reference Collector·대형 Database·Vector 검색·별도 Art Director Agent는 같은 제한 작업이 실제 프로젝트에서 3회 이상 성공하고 자동화 가치가 증명되기 전에는 만들지 않습니다.

PASS — 디자인 품질:

- 실제 V2 데이터로 Visual Target 하나가 만들어지고 사용한 UI UX Pro 규칙과 Reference가 있다면 출처가 기록됩니다.
- 사용자가 실제 화면을 눈으로 확인하고 디자인 품질을 명시적으로 승인합니다.
- Section 단위 수정이 가능하고 선택하지 않은 영역이 보존됩니다.
- 첫 결과가 거절되면 색상만 바꾼 복제안이 아니라 거절 이유를 반영한 구조적으로 다른 대안 하나만 제공합니다.
- 승인 전 제품·Recipe·Registry를 변경하지 않고 실패·중단 시 이전 상태를 보존합니다.

PASS — 채택 편의성:

- 사용자가 Reference 목록이나 디자인 전문용어를 다루지 않고 요청부터 결과 확인까지 완료합니다.
- 쉬운 버튼으로 진행·부분 수정·다른 방향·현재안 유지·중단·복구를 선택합니다.
- 사용자가 거절된 Pilot보다 이 방식이 빠르고 편하다고 명시적으로 판정합니다.
- 중단 시 제품·Recipe·Registry 변경이 없습니다.

제외: Reference 10개 강제 노출, 반복 ImageGen A/B/C, 후보별 Code Preview, 대규모 자동 수집기, 새 DB, 자동 Template 혼합, 출처 없는 복제.

### PM2 — 조립식 제작 보드

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
- 출처·Commit/Hash·License·의존성·수정 내역을 고정한 Verified Code Block 등록
- Layout Recipe·Style Pack을 Module·Slot에 적용하는 결정형 Renderer
- 향후 Motion·3D·Illustration Module을 Core 변경 없이 연결할 Adapter Slot

PASS — 조립 기능:

- 유효한 Manifest의 Module만 장착됩니다.
- Module 2개를 이동하고 하나를 비활성화할 수 있습니다.
- 한 Module 실패가 Core·다른 Module·다른 프로젝트에 전파되지 않습니다.
- 이전 순서와 활성 상태를 복원합니다.
- Core가 허용하지 않은 Action은 표시하거나 실행하지 않습니다.
- 프로젝트별 Run·Preview·결과가 섞이지 않습니다.

예쁜 화면만으로 조립 기능을 PASS하지 않고, Module 동작만으로 PM1 디자인 품질을 PASS하지 않습니다.

### PM3 — 부분 수정·Motion Adapter

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
selections:
  - reference_id: string
    region_label: string
    normalized_bounds: {x, y, width, height}
    target_section_id: string
    selected_properties: [layout | spacing | color | typography | content | branding | motion]
    apply:
      layout: boolean
      spacing: boolean
      color: boolean
      typography: boolean
      content: boolean
      branding: boolean
      motion: boolean
comparison_context:
  viewport: {width, height}
  zoom: number
  data_fixture_id: string
  screen_state: string
  color_mode: light | dark
  motion_capture: paused | timestamp_ms
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

Screenshot 좌표만으로 구역을 식별하지 않습니다. `normalized_bounds`와 `region_label`, 실제 적용 대상인 `target_section_id`를 함께 기록합니다. `apply`에서 선택하지 않은 속성은 잠기며 원본의 문구·Logo·브랜드 자산은 기본값 `false`입니다. Reference와 Preview의 비교는 `comparison_context`가 일치할 때만 유효합니다.

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

### PM4 — 조사·Design Intelligence

목적: 프로젝트 제작과 병목 해결에 필요한 출처가 확인된 자료를 확보합니다.

2026-08-18 사용자는 Design Intelligence·디자인 다양성·구현 도구 확장을 반영하기 위한 Post-MVP PM 수정을 명시적으로 승인했습니다. PM4를 수정하거나 기능을 이동할 때는 중복·누락 표와 선행 Gate를 함께 갱신하고, Core MVP M1~M7과 과거 증거는 보존합니다.

구현 범위:

- 공식 웹·문서와 GitHub 조사
- Reddit 조사
- 사용자가 제공한 Threads 자료
- PDF·Markdown·Text·Screenshot
- 프로젝트 병목 조사
- Source·수집 시점·공식 자료와 보조 의견 구분
- `Collection Request → Collector → Analyzer → 사용자 선택 → 격리 검증 → 채택` 상태 분리
- Source Adapter별 Timeout·후보 수 제한과 수동 URL·파일 입력 대체 경로
- 공개 Capability 후보를 `발견 → 정적 감사 → 가짜 Fixture 격리 시험 → 사용자 판정
  → 채택·보류·폐기`로 처리하는 제거 가능한 Capability Lab
- 디자인 Reference, 구현 Block, 디자인 Skill, Motion과 검증 도구를 구분하는
  `Design Intelligence` Collection
- 기존 V2 Artifact·Design Recipe·Module Registry·Reference Evidence를 검색하는 성공 Recipe 우선 경로
- `Visual Reference | Verified Code Block | Layout Recipe | Style Pack | Motion Module | Illustration Module | 3D Module | Industry Pattern | Rejected Example` 분류
- 사용자가 채택한 후보 1개만 Capability Lab으로 전달하고 시험 결과를 같은 후보에 연결
- 최종 채택된 후보를 Core Write 권한이 없는 비활성 Adapter로 등록하고 해당 PM PASS 후에만 활성

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

사용자에게는 후보별 `채택`, `보류`, `폐기`만 표시합니다. `채택`은 미검증 코드를
Core에 즉시 연결한다는 뜻이 아니라 다음 격리 시험을 승인한다는 뜻입니다. 격리 시험
PASS 뒤 다시 채택된 후보만 비활성 Adapter 상태로 Registry에 기록할 수 있습니다.

데이터 정책:

```yaml
public_source:
  examples: [public_url, public_github, public_registry]
  external_network: allowed_when_declared
generated_fixture:
  external_network: allowed_when_declared
private_project:
  candidate_access: prohibited
secret:
  examples: [token, cookie, password, ssh_key, dotenv]
  candidate_access: prohibited
```

외부 Network 사용 자체를 금지하지 않습니다. 대신 후보 Sandbox에는 V2·제품 저장소,
Git 기록, `.env`, Browser Profile과 Secret을 Mount하거나 전달하지 않습니다. 기본 시험은
Network를 끄고, 공개 Network가 필요한 시험은 사용자의 명시적 승인을 요구합니다.

PASS:

- 주장과 출처가 연결됩니다.
- 공식 자료와 보조 의견이 구분됩니다.
- 조사 실패가 Core와 기존 제작 기능을 막지 않습니다.
- 승인 전 제품을 변경하지 않습니다.

제외: 로그인·유료 제한 우회, 무단 대량 Scraping, 상시 수집 Agent, 별도 Queue·Worker·DB,
후보의 비공개 프로젝트 직접 접근, 승인 없는 Package Install Script·전역 Skill 설치.

### PM5 — 사용자 의도·범위·자산 정합성

목적: AI가 요청을 잘못 이해한 상태로 구현을 시작하지 못하게 합니다.

구현 범위:

- 사용자 원문과 Intent Packet
- AI Intent Receipt
- 변경·비변경 범위
- Acceptance Checks
- 구현 전 불일치 차단과 구현 후 원문 비교
- 공용 재사용·고객 맞춤·고객 전용 자산 경계와 재사용 금지 조건
- 외부 도구·계정·Network·프로젝트 전송 범위와 사용자 승인

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

### PM6 — 전체 통합·품질·복구 검증

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
active_gate: PM3
pm1_design_exploration: pass
pm2_modular_board: completed_and_locked
pm3_to_pm6: not_started
pm1_adoption_method: single_visual_target_with_ui_ux_pro_guard
pm0_operational_readiness: pass_with_user_deferred_backup
```

Post-MVP 설계 계약은 완료됐습니다. PM0는 사용자가 외부 Backup·표본 Restore를 후속으로 유예한 조건으로 통과했습니다. PM1에서는 실패 Pilot을 보존한 상태로 `single_visual_target_with_ui_ux_pro_guard`와 PC 운영 UI를 검증했고 사용자가 PASS했습니다. PM2는 두 프로젝트 결과 Module과 단일 선택 Preview, 프로젝트별 기능 목록, Module 격리·복원을 사용자·기술 검증으로 완료했습니다. 현재 활성 단계는 PM3이며 PM2 PASS를 PM3 직접 편집 구현 완료로 확대하지 않습니다.

생산 배포·운영 관찰과 10년차 전문가 수준 판정은 PM0~PM6 완료만으로 선언하지 않습니다. 배포 가능한 프로젝트에서 별도 승인된 Deployment·Monitoring Adapter와 여러 프로젝트 재현 증거를 축적하는 `Professional Capability Program`의 후속 범위입니다.
