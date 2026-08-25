# AI OS V2 — Design Intelligence 다음 GPT 인수인계

작성일: 2026-08-18

## 사용자의 명시적 승인

> 2026-08-18 사용자가 Design Intelligence, 디자인 다양성, 가격별
> 맞춤 제작, Animation·3D·구현 도구 확장을 반영하기 위해
> Post-MVP PM의 이름·순서·범위·PASS 조건을 수정해도 된다고
> 명시적으로 지시했다.

이 승인은 Core MVP M1~M7, 과거 Run·Artifact·Commit과 당시 판정을
수정하라는 승인이 아닙니다. 기능을 새 PM으로 이동할 때도 기존 증거를
새 번호로 소급해 무효화하지 마세요.

## 먼저 읽을 파일

1. `wiki/CURRENT_STATE.md`
2. `wiki/POST_MVP_PM0_PM6_BASELINE.md`
3. `wiki/DECISIONS.md`
4. `wiki/DESIGN_INTELLIGENCE_IMPLEMENTATION_AUDIT_2026-08-18.md`
5. `wiki/V2_DESIGN_INTELLIGENCE_RESEARCH_2026-08-18.md`

## 현재 사실

```yaml
branch: codex/pm1-design-adoption
audited_base_head: 2c7863e7c093edc063c1b2d579f8469669e53500
design_intelligence: fixture_ui
v2_collector_connection: not_implemented
capability_lab: isolated_execution
v2_design_finish: executed_with_evidence
adopted_capability_count: 1
adopted_capabilities: [impeccable_inactive_adapter]
core_mvp: completed_and_frozen
pm_final_flow_approved_by_user: true
```

> [!IMPORTANT]
> 2026-08-18 후속 환경 구성에서 `impeccable` 1개가 비활성 Adapter로 채택됐습니다.
> 최신 상태는 [[PM1_CAPABILITY_ENVIRONMENT_REPORT_2026-08-18]]을 우선하며,
> 나머지 후보는 각 PM Gate 전 설치하지 않습니다.

## 2026-08-18 최종 PM 흐름

```text
PM0 운영환경·Capability Lab 준비
→ PM1 디자인 전략·탐색·채택
→ PM2 조립식 제작 보드
→ PM3 부분 수정·Motion Adapter
→ PM4 조사·Design Intelligence
→ PM5 사용자 의도·범위·자산 정합성
→ PM6 전체 통합·품질·복구 검증
```

사용자가 위 흐름으로 최종 동기화하라고 지시했습니다. 다음 GPT는
과거 PM 순서를 복원하거나 PM4·PM5를 생략하지 마세요.

## 현재 결론

- 기존 A/B/C ImageGen은 기본이 아닌 Fallback입니다.
- 기본 방식은 `성공 Recipe 재사용 → 부족할 때만 제한 조사 →
  구현 가능한 Block → Visual Target 1개 → 마감 → Code Preview 1개`입니다.
- 디자인 다양성은 더 많은 검사 Skill보다 Verified Code Block, Layout Recipe,
  Style Pack, Industry Pattern, Motion·3D Module을 축적해 늘립니다.
- 같은 이비인후과 100개도 환자·진료·사업 전략과 계약 등급에 따라
  재사용·맞춤·고객 전용 자산의 비율을 다르게 합니다.
- 기본형·성장형·프리미엄형 가격 정책은 사업 운영 계약으로 분리하고
  PM1 기능 계약에 직접 넣지 않습니다.

## 도구 후보 기본 판정

```yaml
primary_block_source: shadcn_ui
conditional_visual_block: magic_ui
deferred_until_real_3d_project: react_three_fiber
deferred_until_interactive_2d_need: rive
deferred_until_loading_or_illustration_need: dotlottie
hold:
  - base_ui
  - ark_ui
  - react_bits
  - spline
  - theatre_js
```

후보를 모두 설치하지 마세요. 현재 V2 운영 Dashboard에는 3D 요구가
없으므로 React Three Fiber·Rive·dotLottie 시험을 자동 시작하지 마세요.

## 다음 한 작업

Design Intelligence를 별도 Collector로 만들지 말고 기존 V2
`Collection Request → Collector → Analyzer`의 제거 가능한 Workflow로 연결할
최소 Adapter 계약을 설계하세요. 계약은 다음을 포함해야 합니다.

```text
성공 Recipe 우선 검색
→ 부족할 때만 제한 수집
→ 사용자 채택·보류·폐기
→ 채택 후보 1개만 격리 시험
→ 결과를 같은 화면에 표시
→ 사용자 최종 채택
→ 비활성 Adapter 등록
→ Feature Flag OFF·제거·복구
```

구현 전 수정된 PM 전체를 표로 보여주고 기능 중복·누락·선행 Gate를
검토하세요. 사용자가 PM 수정을 승인했으므로 필요한 PM 재배치를 제안할
수 있지만, 사용자의 기능 선택과 구현 승인을 자동으로 간주하지 마세요.
