# AI OS V2 — PM1 착수 통합 GPT 인수인계 지시서

> [!IMPORTANT]
> 이 문서는 이전 PM1 실험의 인수인계 기록입니다. 2026-08-18 이후 새 작업은
> [[GPT_DESIGN_INTELLIGENCE_CONTINUATION_HANDOFF]]와
> [[POST_MVP_PM0_PM6_BASELINE]]을 우선하며, 실패 Pilot은 증거로만 보존합니다.

작성일: 2026-08-17  
대상: 새 GPT·Codex 세션  
상태: Post-MVP 설계 완료, PM0 조건부 운영 PASS, PM1 진행 중

아래 지시문을 새 세션에 그대로 전달합니다.

---

## 전달 지시문

AI OS V2의 Post-MVP 작업을 이어서 진행해 주세요.

과거 대화의 기억이나 이전 PM 번호를 추정하지 말고 실제 저장소·Worktree·최신 문서를 읽은 뒤 판단하세요. 완료된 Core MVP M1~M7은 변경하지 않습니다.

### 1. 확인 경로

```text
Core 원본 Dirty 작업공간:
/home/user/바탕화면/ai_os_v2

PM0 검증 Worktree:
/home/user/바탕화면/ai_os_v2_or0

PM1 작업 Worktree:
/home/user/바탕화면/ai_os_v2_pm1

과거 정적 PM1 Preview 증거:
/home/user/바탕화면/V2_UI/pm1-clickable-preview

제품 저장소:
/home/user/바탕화면/test_project
```

우선 읽을 문서:

```text
/home/user/바탕화면/ai_os_v2_pm1/wiki/CURRENT_STATE.md
/home/user/바탕화면/ai_os_v2_pm1/wiki/POST_MVP_PM0_PM6_BASELINE.md
/home/user/바탕화면/ai_os_v2_pm1/wiki/POST_MVP_DESIGN_COMPLETION_REPORT.md
/home/user/바탕화면/ai_os_v2_pm1/wiki/PM1_REFERENCE_BRIEF.md
/home/user/바탕화면/ai_os_v2_pm1/wiki/WEB_ANIMATION_RESEARCH_2026-08-17.md
```

### 2. Git과 보존 상태

```yaml
github_origin_main: 83ab8deaa504df6c1baf95a3a49ab1df05345653
post_mvp_design_local_commit: 822a218ee9cd51d0110b55d5cf87eee8ad3c2566
pm0_verification_commit: f03d80cb43a77b2377e7d915a90fda2716fe7d2a
pm1_worktree_head: 3ae7b9842053723d895beb05d685eeaa56b006c7
pm1_branch: codex/pm1-design-adoption
push_status: not_performed
```

- 원본 `/home/user/바탕화면/ai_os_v2`에는 기존 Run·Wiki·Submodule·Cache 등 사용자 Dirty 변경이 남아 있습니다.
- 원본 Dirty 변경을 Reset·Restore·Stash·자동 Commit하지 마세요.
- PM1은 분리된 `/home/user/바탕화면/ai_os_v2_pm1`에서만 진행합니다.
- 현재 PM1의 `CURRENT_STATE.md`, `PM1_REFERENCE_BRIEF.md`, `WEB_ANIMATION_RESEARCH_2026-08-17.md`는 진행 중 변경이며 PM1 PASS 전에는 Result Commit으로 만들지 않습니다.
- 각 PM은 완료·Codex 검증·사용자 PASS 후 별도 Result Commit 하나로 저장합니다.

### 3. 공식 PM 순서

```text
PM0 운영환경 준비
→ PM1 디자인 탐색·채택
→ PM2 조립식 V2 보드
→ PM3 부분 수정
→ PM4 자료 조사
→ PM5 사용자 의도 정합성
→ PM6 전체 통합·최종 검증
```

Post-MVP 설계 계약은 완료됐지만 기능 구현 완료를 뜻하지 않습니다.

### 4. PM0의 정확한 판정

PM0 기술 검증 결과:

```yaml
technical_preflight: PASS
fresh_codex_process_reproduction: PASS
antigravity_isolated_safe_launch: PASS
strict_port_and_path_checks: PASS
external_backup_and_sample_restore: DEFERRED_BY_USER
pm0_gate: PASS_WITH_USER_DEFERRED_BACKUP
pm1_start_allowed: true
```

외부 Backup·표본 Restore는 원래 PM0 필수 조건이지만 사용자가 PM1 시험 동안 명시적으로 유예했습니다. 따라서 다음 두 표현을 구분하세요.

- PM1 착수 Gate: PASS
- 완전한 재해 복구 준비: 미완료

이를 PM0 FAIL로 되돌려 PM1을 다시 차단하지 마세요. 대신 `operational_debt.external_backup_restore`로 보존하고 실제 제품 배포 전에는 반드시 해결해야 합니다.

### 5. 현재 가장 큰 제품 능력 병목

Core는 Run·Gate·승인·증거·복구를 안전하게 관리하지만, Post-MVP 능력은 아직 실제 제품에서 증명되지 않았습니다.

```yaml
core_safety: implemented_and_frozen
post_mvp_design_contract: completed
pm0_for_pm1: pass_with_deferred_backup
design_adoption_quality: not_yet_proven
modular_board: not_implemented
visual_editing: not_implemented
web_quality_profile: not_yet_formalized
production_operation: insufficient
senior_equivalent_capability: not_proven
```

기능을 더 늘리기 전에 다음 순서로 실제 증거를 만들어야 합니다.

```text
PM1에서 디자인 채택 방식 검증
→ PM2에서 조립식 보드 검증
→ PM3에서 초보자 직접 편집 검증
→ PM4·PM5 연결
→ PM6 Web Quality·통합 검증
→ 별도 승인 후 배포·운영 검증
```

### 6. PM1의 정확한 목적

PM1은 특정 디자인이나 도구를 확정 사용하기 위한 단계가 아닙니다.

목적:

- 초보자가 전문용어와 반복 ImageGen 없이 좋은 디자인을 눈으로 선택
- 다음 세 채택 방식의 편의성을 비교
- 디자인 품질과 채택 방식 편의성을 각각 판정

채택 방식:

```text
추천형
→ V2가 실제 Reference 10개 이상 조사
→ 구조적으로 다른 추천 3개 표시

Reference 가져오기
→ 사용자가 URL·Screenshot 제공
→ 전체 또는 사용할 Section 선택

직접 조립형
→ 검증된 Block·Section 후보 선택
→ 저비용 구조 Draft에서 순서 조합
```

입력 우선순위:

```yaml
primary: mouse_selection
secondary: simple_choice_buttons
fallback: natural_language
```

공통 행동:

- 현재안 유지
- 추천대로 진행
- 직접 선택
- 다른 방식
- 중단

사용자가 불편하다고 판정한 방식은 V2 기본 Workflow로 승격하지 않습니다.

### 7. PM1 Reference Workflow

```text
Reference Brief
→ 실제 Reference 10개 이상 수집
→ 출처·접근·라이선스·구현 가능성 검사
→ Visual Reference와 Reusable Code Block 분리
→ Reference Board 전체 공개
→ 구조가 겹치는 후보 제거
→ 추천 3개
→ 전체 또는 Section 선택
→ 구조 Draft 1~2개
→ 방향 확인
→ 실제 V2 데이터 Code Preview 1개
→ 디자인 품질·채택 편의성 사용자 판정
```

- 실제 Code Preview를 여러 개 반복 생성하지 않습니다.
- 여러 Reference 조합을 이해하기 어려울 때만 조합 이미지 한 장을 사용합니다.
- 반복 ImageGen A/B/C는 기본 흐름이 아닙니다.
- Reference를 수집했다는 이유만으로 Registry에 등록하지 않습니다.
- 사용자 승인 후 실제 Preview 적용·검증까지 PASS한 Block·Recipe만 재사용 자산으로 승격합니다.

### 8. 검증된 기본값 우선 정책

사용자는 실험을 선호하지 않습니다. 여러 Library를 동시에 설치해 비교하지 마세요.

```text
현재 Stack과 Browser 기본 기능으로 해결
→ 충족하면 종료
→ 실제 부족함이 증명되면 검증된 도구 하나만 격리 Pilot
→ 성능·접근성·모바일·제거 검증
→ 효과가 없으면 완전 제거
→ 안정적인 기본 방식이 운영된 뒤에만 새 실험
```

자동 조사와 후보 추천은 가능하지만 다음은 사용자 승인 전 금지합니다.

- Package·Skill 설치
- 외부 API·유료 서비스 연결
- 제품 적용
- Run 생성·변경
- Commit·Push

### 9. 웹 애니메이션 방향

애니메이션 엔진 하나를 전역으로 고정하지 않습니다.

```yaml
simple_motion:
  tool: CSS_and_View_Transition_API
  status: recommended_default

react_ui_motion:
  tool: Motion
  status: PM2_React_stack_confirmed_then_single_pilot

reorder_only:
  tool: AutoAnimate
  status: consider_only_if_Motion_not_adopted

complex_svg_timeline_3d:
  tool: Anime.js
  status: deferred_until_real_requirement

animated_component_references:
  tools: [Kokonut_UI, Magic_UI, Animate_UI, React_Bits]
  status: PM1_visual_and_code_candidates

illustration_motion:
  tool: dotLottie
  status: customer_product_candidate

advanced_scroll_motion:
  tool: GSAP
  status: deferred_due_visual_builder_license_boundary
```

도구 역할:

- Kokonut UI는 Engine이 아니라 Motion 기반 완성 UI Block Reference입니다.
- Motion은 React Layout·Card·Panel·Gesture의 기본 후보입니다.
- Anime.js는 SVG·Timeline·Text·Canvas·향후 Three.js용 제거 가능한 Adapter 후보입니다.
- AutoAnimate와 Motion을 같은 목적 때문에 동시에 설치하지 않습니다.
- GSAP은 고객 웹의 특수 연출에는 조건부 사용 가능하지만 V2 Animation Builder의 핵심 엔진으로 채택하지 않습니다.

Motion 필수 규칙:

- 목적: Feedback·Transition·Hierarchy·Storytelling 중 하나 기록
- `prefers-reduced-motion` 지원
- 기본 속성은 `transform`, `opacity`
- 자동 재생·무한 반복·큰 Parallax 기본 금지
- Animation Adapter 제거 후에도 Content·Action·최종 Layout 유지
- 디자인 품질 PASS와 Motion 성능·접근성 PASS 분리

### 10. Beginner Assistance Layer

V2의 내부 Run·Gate·Commit을 초보자가 이해하는 화면으로 번역합니다.

필수 사용자 기능:

- 지금 할 일 하나
- 추천대로 진행 또는 직접 선택
- 쉬운 요청 정리 확인
- 변경 범위 잠금
- 문제 있어요
- 적용 전 실제 Preview
- 쉬운 이전 상태 복구
- 검증 결과 요약
- 막혔을 때 선택지 하나

사용자가 선택하지 않은 값을 AI가 확정하지 않습니다. 추천값은 추천으로 표시하고 사용자 확인 전 제품을 변경하지 않습니다.

### 11. 조립식 보드·편집기의 미구현 상태

다음은 계약만 존재하며 구현 완료로 표현하면 안 됩니다.

- Module Manifest
- Module Registry
- Slot Renderer
- Module 이동·비활성화·장애 격리·복원
- Drag & Drop
- 크기·순서·여백·글자 조절
- Undo·Redo
- Draft·Version·Restore 편집 흐름
- Puck Adapter

PM1의 직접 조립은 구조 Draft일 뿐입니다. 실제 Module 장착과 상태 저장은 PM2, 직접 편집은 PM3에서 검증합니다.

### 12. Web Quality Profile 보완안

좋은 웹의 품질을 한 가지 점수로 자동 PASS하지 말고 다음 독립 Gate로 구성하세요.

```yaml
web_quality_profile:
  task_success:
    - 핵심 사용자 목표 완료
    - 초보자 막힘과 재작업 횟수
    - 완료 시간
  visual_quality:
    - 정보 우선순위
    - Reference 대비 품질
    - 디자인 시스템 일관성
  responsive:
    - 고객 제품 390px_and_430px
    - PC 회귀
    - overflow_and_touch_targets
  motion:
    - 목적 있는 Motion
    - reduced_motion
    - transform_and_opacity_preference
    - mobile_performance
  accessibility:
    - keyboard
    - focus
    - contrast
    - semantics
  performance:
    - Lighthouse
    - Core_Web_Vitals
    - bundle_and_runtime_profile
  reliability:
    - loading_empty_error_success_states
    - console_and_build
    - failure_isolation
  security:
    - dependency_and_secret_check
    - external_input_boundary
  recovery:
    - commit
    - rollback
    - restore
  user_verification:
    - requested_result_match
    - actual_use_feedback
```

적용 위치:

- PM1: `visual_quality`, 디자인 선택 편의성
- PM2: `reliability`, 조립 기능, 장애 격리
- PM3: 편집 정확성·Undo·Restore·반응형 회귀
- PM4: Source 품질과 조사 재현성
- PM5: 최초 의도·범위·결과 일치
- PM6: 전체 Web Quality Profile 통합 판정

Web Quality Profile 계약은 PM1을 다시 막지 않으며 PM6 이전 공식 문서에 반영해야 합니다.

### 13. 배포·운영 경계

현재 PM0~PM6은 안전한 로컬 제작과 검증까지를 우선합니다. 돈을 받고 실제 서비스를 운영하려면 후속 Production Readiness Gate가 필요합니다.

필수 항목:

- Staging·Production 분리
- 승인 기반 자동 배포
- Health Check
- 오류·성능 관찰
- 실제 장애 Rollback
- 외부 운영 Backup·Restore
- 배포 후 사용자 행동과 실패 분석

PM6 완료만으로 배포 운영 능력이나 10년차 전문가 대체를 자동 선언하지 마세요.

### 14. 전문가 수준 평가

`10년차 이상`은 기능 수나 화면 완성도로 주장하지 않습니다.

최소 다섯 개의 서로 다른 실제 프로젝트에서 다음을 반복 검증해야 합니다.

```text
조사
→ 기획
→ 디자인
→ 구현
→ 검증
→ 배포
→ 운영
→ 장애 복구
```

PM 완료마다 다음을 증거 기반으로 보고하세요.

- 대체 가능한 역할
- 대략적인 연차 범위
- 자동화된 반복 업무
- 계속 사람이 판단해야 하는 업무
- 실패 사례와 개선점
- 이전 PM보다 줄어든 시간·재작업·사용자 개입

증거가 없으면 `not_proven`으로 표시합니다.

### 15. 현재 수행할 작업 하나

PM1 Reference Board의 정보 구조를 먼저 설계하고 실제 Reference 조사에 착수하세요.

필수 구성:

1. 정적 Layout·Information Architecture Reference
2. Animated Component·Motion Demo Reference
3. 각 Reference의 URL·접근 시점·라이선스·사용할 부분·Section ID
4. `visual_reference`와 `reusable_code_block` 구분
5. 구조가 다른 전체 후보 10개 이상
6. 사용자에게 먼저 보여줄 추천 3개
7. Motion 강도 선택: `없음`, `절제`, `표현적`

아직 하지 말 것:

- 새 Animation Library 설치
- PM2 Module 구현
- PM3 Puck·Drag & Drop 구현
- Image-to-Code
- 제품 코드 변경
- Run·Commit·Push

보고 형식:

```yaml
repository_state:
  source_files: []
  head:
  dirty_preserved:

pm0:
  technical_status:
  deferred_operational_debt:
  pm1_allowed:

pm1_reference_board:
  static_candidates: []
  motion_candidates: []
  recommended_three: []
  license_risks: []
  missing_evidence: []

web_quality_profile:
  current_contract_status:
  pm6_document_fix_needed:

changes:
  files:
  install:
  run:
  commit:
  push:

verdict: PASS | PASS_WITH_FIX | BLOCKED
next_single_action:
```

---

## 작성자 종합 판정

GPT가 지적한 “실제 제작 능력 증거 부족”은 타당합니다. 특히 조립식 보드, 직접 편집, Web Quality, Production 운영, 전문가 수준 반복 증거는 아직 없습니다.

다만 PM0는 사용자의 명시적 유예 결정을 반영해야 합니다. 외부 Backup·Restore가 미완료라는 사실은 숨기지 않되 PM1 착수를 다시 금지하지 않습니다.

```yaml
gpt_gap_analysis: mostly_valid
pm0_incomplete_claim: corrected_to_pass_with_deferred_operational_debt
pm1_start: allowed
current_active_work: PM1_reference_board
design_method_finalized: false
animation_engine_adopted: false
web_quality_profile: required_document_enhancement
production_readiness: future_gate_required
senior_equivalent_capability: not_proven
```
