# PM1 Capability 환경 구성 보고서

작성일: 2026-08-18
기준: [[POST_MVP_PM0_PM6_BASELINE]]
상태: `PASS`

## 결과

새 최종 PM 흐름에 맞춰 후보 도구를 한꺼번에 설치하지 않고, PM·선행 Gate·현재 판정과
제거 경로를 Catalog로 관리하도록 환경을 구성했습니다.

```text
후보 발견 또는 기존 성공 자산 재사용
→ 정적 감사
→ 가짜 Fixture 격리 시험
→ 사용자 채택·보류·폐기
→ 비활성 Adapter 등록
→ 대상 PM 실제 검증
→ 사용자 활성 승인
```

## PM1에서 사용할 구성

| 구성 | 현재 역할 | 상태 |
|---|---|---|
| `v2-design-finish` | Visual Target 제작부터 마감 Gate까지 | 사용 가능 |
| UI UX Pro Max | 디자인 규칙·접근성·금지 Pattern 검사 | 사용 가능 |
| shadcn/ui | 실제 구현 가능한 Block을 설치 없이 검토 | PM1 읽기 전용 |
| Impeccable | 마감 결과의 선택형 2차 의견 | 채택·비활성 Adapter |

Impeccable은 격리 시험과 PM1 마감 테스트에서 유효한 지적을 제공한 증거가 있어
Registry에 등록했습니다. 자동 활성화·전역 설치·Core 쓰기·비공개 프로젝트 접근은
허용하지 않았습니다.

## 보류한 후보

| 후보 | 예정 단계 | 활성 조건 |
|---|---|---|
| Taste Skill v1 | PM1 선택 | 같은 결과물 비교 후 사용자 선택 |
| Kokonut UI | PM1 Reference·PM3 적용 | PM2 PASS와 실제 Motion 필요 |
| Motion | PM3 | PM2 PASS와 승인된 Visual Target의 Motion 요구 |
| AutoAnimate | PM3 | Motion 미설치 상태의 순서 변경 전용 요구 |
| Storybook | PM2 후반·PM6 | 재사용 Module이 실제로 생성됨 |
| Stitch Skills | PM1 Fallback | 사용자 재요청과 새 품질 증거 |

영상·Illustration·3D 후보는 PM2 조립식 보드 PASS와 실제 고객 요구 전에는 설치하지
않습니다.

## 구현된 환경 변경

- 후보 Catalog를 Python 하드코딩에서 JSON Registry로 분리
- 후보마다 `pm_stage`, `current_decision`, `activation_gate`,
  `install_allowed_now` 기록
- Design Intelligence 출력에 PM과 Gate 표시
- `tools/pm-capability-preflight` 읽기 전용 검사 추가
- Capability Lab Plugin `0.2.0` 검증
- Skill·Plugin·JSON·YAML·Python 구문과 공개 Metadata 수집 Smoke Test PASS

## Preflight 결과

```yaml
candidate_catalog: PASS_8
candidate_install_preapproved: 0
adopted_registry: PASS_1_inactive
core_write_allowed: false
private_project_access: false
skill_validation: PASS
plugin_validation: PASS
design_intelligence_smoke: PASS
```

## 현재 판정

```yaml
pm0_capability_environment: PASS
pm1_environment: READY
pm1_active_method: single_visual_target_with_ui_ux_pro_guard
pm1_finish_second_opinion: impeccable_inactive_adapter
pm2_to_pm6_installations: DEFERRED_BY_GATE
product_code_changed: false
core_m1_m7_changed: false
```

## 다음 한 작업

PM1에서 기존 승인 Visual Target을 기준으로 `v2-design-finish` 기본 결과와 선택형
Impeccable 2차 의견을 같은 화면에서 비교하고, 사용자가 PM1 기본 마감 흐름을
`채택`, `수정`, `다른 방법` 중 하나로 판정합니다.
