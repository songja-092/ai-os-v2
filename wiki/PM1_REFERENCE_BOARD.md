# PM1 Reference Board v1

작성일: 2026-08-17  
접근 확인일: 2026-08-17  
상태: 사용자 선택 대기  
대상: PC 전용 `v2_board` 대시보드·프로젝트 작업실  
고객 결과물 기준: 모바일 우선, 390px·430px 회귀검증

이 문서는 조사 근거와 계약 기록입니다. 사용자가 실제로 보는 화면은 V2 Core의 `./v2 dashboard --port 8200` 실행 후 `http://127.0.0.1:8200/reference-board`에서 제공합니다. Core는 `pm1-artifacts/reference-board/manifest.json`을 검증하고, 사용자가 마우스로 선택한 경우에만 `selection.json` Draft를 기록합니다.

## 1. 사용자가 선택할 것

각 후보에서 다음 네 가지 중 하나만 선택합니다.

- `전체 구조 사용`
- `이 부분만 사용`
- `현재안 유지`
- `다른 후보 보기`

Motion은 별도로 `없음`, `절제`, `표현적` 중 하나를 선택합니다. 선택 전에는 Library를 설치하거나 Code Preview를 만들지 않습니다.

## 2. 구조적으로 다른 추천 3개

### 추천 A — 밀도 높은 전문 작업실

사용할 Reference Mix:

- [shadcn Dashboard Block](https://ui.shadcn.com/blocks?category=dashboard): 접히는 Sidebar, 검색, Project Navigation
- [Tremor Blocks](https://blocks.tremor.so/blocks): 상태 Monitoring, Filterbar, Table, Empty State
- [Plane](https://plane.so/open-source): 여러 Project·Module을 빠르게 전환하는 밀도와 점진적 복잡성

V2 적용 예상:

```text
밝은 Sidebar
→ 빠른 실행·검색
→ 프로젝트 목록과 상태를 한 화면에 밀도 있게 표시
→ 오른쪽에 Background 작업·문제 상태
→ 필요할 때만 Core 제작 흐름 펼치기
```

- 적합: 프로젝트 10~50개 관리, 상태 비교, 운영 중심
- 주의: 처음 보는 사용자가 정보량에 압도되지 않도록 기본 필터와 접기를 사용
- Motion 강도 권장: `절제`
- Section ID: `dashboard.navigation`, `dashboard.quick-actions`, `dashboard.project-list`, `dashboard.background-jobs`

### 추천 B — Preview 중심 작업 공간

사용할 Reference Mix:

- [Storybook Browse Stories](https://storybook.js.org/docs/get-started/browse-stories): 검색 가능한 Sidebar, 격리 Preview Canvas, Toolbar, 상세 Panel
- [현재 프로젝트 작업실 Visual Target](/home/user/바탕화면/v2_ui_images/프로젝트%20작업실%20PC%20Visual%20Target.png): 사용자 요청과 큰 Preview의 기존 방향
- [Motion Examples](https://motion.dev/examples): Modal·Layout·상태 전환의 절제된 Feedback

V2 적용 예상:

```text
왼쪽 20% 요청·단계·후보
→ 오른쪽 80% 큰 실제 Preview
→ 필요하면 왼쪽을 접어 10:90 집중 모드
→ 아래 또는 오른쪽 상세 Panel은 기본 숨김
```

- 적합: 결과를 직접 보고 통과·수정하는 초보자 중심 흐름
- 주의: 대시보드 기능까지 작업실에 섞지 않음
- Motion 강도 권장: `절제`
- Section ID: `workspace.context-panel`, `workspace.preview`, `workspace.preview-toolbar`, `workspace.actions`, `workspace.details`

### 추천 C — 조립식 Module 보드

사용할 Reference Mix:

- [Puck Demo](https://demo.puckeditor.com/edit): Component Palette, 큰 Canvas, Property Panel
- [Puck GitHub](https://github.com/puckeditor/puck): React Component 기반 조립 구조와 MIT 계약
- [shadcn Sidebar](https://ui.shadcn.com/docs/components/aria/sidebar): 접히는 Navigation과 Panel 구조
- [Animate UI](https://animate-ui.com/docs): 이동·열기·상태 변화의 접근 가능한 Motion Pattern

V2 적용 예상:

```text
Module 후보 Panel
→ 중앙 보드 Canvas
→ 선택한 Module 속성 Panel
→ 순서·표시 상태를 Draft로 변경
→ Preview 후 적용 또는 복구
```

- 적합: 미래 Module·영상·3D Adapter를 같은 Slot에 추가하는 구조
- 주의: PM1에서는 구조 Draft만 비교하며 실제 Registry·Drag & Drop은 PM2·PM3까지 금지
- Motion 강도 권장: `절제`
- Section ID: `workspace.module-library`, `workspace.module-canvas`, `workspace.property-panel`, `workspace.version-actions`

## 3. 전체 Reference 목록

### CURRENT-01 — 현재 V2 대시보드·작업실

```yaml
reference_type: 화면 참고용
url:
  - /home/user/바탕화면/v2_ui_images/대시보드 PC Visual Target.png
  - /home/user/바탕화면/v2_ui_images/프로젝트 작업실 PC Visual Target.png
access_checked_at: 2026-08-17
license_status: 사용자 제공 자산
section_id: [dashboard.shell, dashboard.project-list, workspace.preview]
dependencies: [none_static_image]
responsive: V2_PC만_대상; 고객_모바일은_별도_Recipe
motion_level: 없음
do_not_copy: [작은_모바일_Preview, 과도한_설명, 약한_Panel_테두리, 대시보드와_작업실_혼합]
current_design: true
```

사용할 부분: Navy 계열의 신뢰감, 프로젝트 목록, 큰 Preview 작업실 방향. 비교의 기준점으로 삭제하지 않습니다.

### LAYOUT-01 — shadcn Dashboard Block

```yaml
reference_type: 코드 재사용 가능
url: https://ui.shadcn.com/blocks?category=dashboard
access_checked_at: 2026-08-17
license_status: 확인_MIT
section_id: [dashboard.navigation, dashboard.project-list, dashboard.filters]
dependencies: [React, Tailwind_CSS, shadcn_ui, Radix_or_Base_UI]
responsive: PC_확인; 공식_responsive_명시; 390_430_실행검증_전
motion_level: 절제
do_not_copy: [사용자_Profile_기본노출, 불필요한_Chart, 팀_전환기]
current_design: false
```

사용할 부분: 접히는 Sidebar, Container Query 기반 Dashboard Shell, 검색·Table·Card의 명확한 구분.

### LAYOUT-02 — Tremor Blocks

```yaml
reference_type: 코드 재사용 가능
url: https://blocks.tremor.so/blocks
access_checked_at: 2026-08-17
license_status: 확인_MIT
section_id: [dashboard.background-jobs, dashboard.problem-state, dashboard.project-list]
dependencies: [React, Tailwind_CSS, Tremor_or_Tremor_Raw]
responsive: PC_확인; 390_430_개별_Block_실행검증_전
motion_level: 없음
do_not_copy: [금융_KPI_내용, 불필요한_Chart, 유료_Template_고유자산]
current_design: false
```

사용할 부분: Status Monitoring, Filterbar, Table Action, Empty State와 높은 정보 밀도.

### LAYOUT-03 — Plane

```yaml
reference_type: 화면 참고용
url: https://plane.so/open-source
access_checked_at: 2026-08-17
license_status: 확인_AGPL_코드재사용금지
section_id: [dashboard.project-list, dashboard.navigation, dashboard.module-summary]
dependencies: [visual_reference_only]
responsive: PC_화면_참고; 390_430_미확인
motion_level: 절제
do_not_copy: [브랜드, Icon, 문구, AGPL_Code, 팀_협업_UI]
current_design: false
```

사용할 부분: 프로젝트가 많을 때의 다중 View, Module 개념, 처음에는 단순하고 필요할 때 복잡성을 여는 방식.

### WORKSPACE-01 — Storybook UI

```yaml
reference_type: 화면 참고용
url: https://storybook.js.org/docs/get-started/browse-stories
access_checked_at: 2026-08-17
license_status: 확인_MIT
section_id: [workspace.navigation, workspace.preview, workspace.preview-toolbar, workspace.details]
dependencies: [React_optional, isolated_iframe_preview, Storybook]
responsive: PC_확인; 공식_mobile_active_panel_지원; V2는_PC만_사용
motion_level: 절제
do_not_copy: [개발자용_Story용어, Addon_전문용어, Source_Code_기본노출]
current_design: false
```

사용할 부분: 검색 가능한 좌측 목록, 중앙 격리 Canvas, Toolbar, 필요할 때만 여는 상세 Panel.

### WORKSPACE-02 — Puck Editor Demo

```yaml
reference_type: 화면 참고용
url: https://demo.puckeditor.com/edit
access_checked_at: 2026-08-17
license_status: 확인_MIT
section_id: [workspace.module-library, workspace.module-canvas, workspace.property-panel]
dependencies: [React, puckeditor_core]
responsive: PC_Editor_확인; 390_430_고객_Preview는_별도검증
motion_level: 절제
do_not_copy: [Puck_Data를_Source_of_Truth로_사용, 무제한_Field, 자유로운_제품_직접덮어쓰기]
current_design: false
```

사용할 부분: Palette·Canvas·Property Panel의 공간 분리. PM3 Adapter 후보일 뿐 PM1 설치 대상이 아닙니다.

### MOTION-01 — Kokonut UI

```yaml
reference_type: 코드 재사용 가능
url: https://kokonutui.com/docs
access_checked_at: 2026-08-17
license_status: 확인_MIT_GitHub
section_id: [shared.buttons, workspace.status-feedback, dashboard.quick-actions]
dependencies: [React_or_Next, Tailwind_CSS_v4, shadcn_ui, Motion_component_specific, lucide]
responsive: component_specific; 390_430_실행검증_전
motion_level: 절제_to_표현적
do_not_copy: [Pro_유료_Component, Particle_남용, 전체_색상체계, 불필요한_장식]
current_design: false
```

사용할 부분: 상태 Button, Card Feedback, AI·Navigation Component의 작은 상호작용.

### MOTION-02 — Magic UI

```yaml
reference_type: 코드 재사용 가능
url: https://magicui.design/docs
access_checked_at: 2026-08-17
license_status: 확인_MIT_무료_Registry만
section_id: [dashboard.background-jobs, workspace.reference-summary, customer_product.hero]
dependencies: [React, Tailwind_CSS, shadcn_ui, Motion_component_specific]
responsive: component_specific; 390_430_실행검증_전
motion_level: 표현적
do_not_copy: [Pro_Template, 과도한_Particle, Cursor_Effect, 지속_반복_배경]
current_design: false
```

사용할 부분: Animated List·Progress·Video Dialog처럼 상태나 콘텐츠 이해에 도움되는 효과만 후보로 사용.

### MOTION-03 — Animate UI

```yaml
reference_type: 코드 재사용 가능
url: https://animate-ui.com/docs
access_checked_at: 2026-08-17
license_status: 확인_오픈소스_개별원본라이선스재확인
section_id: [shared.dialog, shared.tabs, shared.icons, workspace.property-panel]
dependencies: [React, Tailwind_CSS, Motion, shadcn_registry, Radix_or_Base_or_Headless_UI]
responsive: component_specific; 390_430_실행검증_전
motion_level: 절제
do_not_copy: [모든_Primitive_일괄도입, 중복_shadcn_Component, 목적없는_Icon_Animation]
current_design: false
```

사용할 부분: 접근성과 유지보수를 고려한 Dialog·Tabs·Icon의 작은 상태 전환.

### MOTION-04 — React Bits

```yaml
reference_type: 화면 참고용_코드는_조건부
url: https://reactbits.dev/
access_checked_at: 2026-08-17
license_status: 확인_조건부_MIT_plus_Commons_Clause
section_id: [customer_product.hero, customer_product.background, customer_product.text]
dependencies: [React, CSS_or_Tailwind, component_specific_animation_dependency]
responsive: component_specific; 390_430_실행검증_전
motion_level: 표현적
do_not_copy: [Library_재판매, V2_운영_UI_과도한_효과, 무거운_WebGL_기본사용]
current_design: false
```

사용할 부분: 고객 Landing Page의 Text·Background·Hero 방향을 눈으로 비교하는 용도. V2 운영 UI에는 기본 적용하지 않습니다.

### MOTION-05 — Motion Examples

```yaml
reference_type: 코드 재사용 가능
url: https://motion.dev/examples
access_checked_at: 2026-08-17
license_status: 확인_MIT_Core; MotionPlus_유료예제_제외
section_id: [shared.layout-transition, shared.dialog, shared.reorder, shared.feedback]
dependencies: [React, Motion]
responsive: cross_device_gesture_지원; 후보별_390_430_실행검증_전
motion_level: 절제_to_표현적
do_not_copy: [MotionPlus, Experimental, Cursor_Trail, 큰_Parallax, 기능과_무관한_효과]
current_design: false
```

사용할 부분: Reorder, Shared Layout, Modal, Toast, Hold-to-confirm 같은 기능 목적이 분명한 예제.

### MOTION-06 — Anime.js

```yaml
reference_type: 코드 재사용 가능
url: https://animejs.com/documentation/
access_checked_at: 2026-08-17
license_status: 확인_MIT
section_id: [customer_product.svg, customer_product.timeline, customer_product.three_adapter]
dependencies: [JavaScript_or_React, Anime_js, optional_Three_js]
responsive: Scope와_Media_Query_설계가능; 후보별_390_430_실행검증_전
motion_level: 표현적
do_not_copy: [일반_Button에_복잡한_Timeline, 무한_Loop, Core상태_직접변경, 3D_기본설치]
current_design: false
```

사용할 부분: SVG 도면 기호, 순차 Text, 복잡한 Timeline과 향후 3D Module. 일반 V2 UI 기본 엔진은 아닙니다.

## 4. 현재 비교 요약

| 후보 | 프로젝트 증가 대응 | Preview 집중 | 미래 조립성 | 초보자 용이성 | 코드 재사용 위험 | 추천 Motion |
|---|---:|---:|---:|---:|---:|---|
| A 전문 작업실 | 높음 | 중간 | 중간 | 중간 | 낮음~중간 | 절제 |
| B Preview 중심 | 중간 | 매우 높음 | 중간 | 높음 | 낮음 | 절제 |
| C 조립식 보드 | 높음 | 높음 | 매우 높음 | 검증 필요 | 중간 | 절제 |
| 현재안 | 중간 | 높음 | 낮음 | 중간 | 없음 | 없음 |

이 표는 자동 선택 점수가 아닙니다. 추천 순위가 아니라 구조적 차이를 설명합니다.

## 5. 라이선스·접근 위험

- Plane은 AGPL이므로 구조와 정보 밀도만 보고 코드·브랜드·문구를 복제하지 않습니다.
- React Bits는 Commons Clause가 포함되어 Reference 용도는 가능하지만 실제 코드 채택 전 배포·재판매 조건을 다시 검토합니다.
- Magic UI·Kokonut UI의 Pro 자산은 후보에서 제외합니다.
- Motion Examples의 Motion+ 표시 예제는 무료 후보에서 제외합니다.
- Animate UI는 Component가 다른 Primitive에서 Port된 경우 원본 라이선스까지 다시 확인합니다.
- `responsive`가 `실행검증_전`인 후보는 지원한다고 추정하지 않습니다.

## 6. 사용자 선택 Gate

아래 네 항목만 답하면 다음 단계로 진행할 수 있습니다.

```yaml
selected_direction: A | B | C | current | none
selected_sections: []
motion_level: none | restrained | expressive
adoption_action: whole_structure | selected_parts | keep_current | show_others
```

선택 후에도 바로 제품을 구현하지 않습니다. 선택한 방향으로 구조 Draft 1~2개만 만들고, 사용자가 방향을 확인한 뒤 실제 V2 데이터 Code Preview 하나를 제작합니다.

## 7. 현재 상태

```yaml
reference_count_external: 11
current_design_preserved: true
recommended_directions: 3
actual_access_checked: true
library_installed: false
code_preview_created: false
product_code_changed: false
pm1_status: awaiting_user_direction_selection
```
