# PM Codex 제작·검증 도구 도입 계약

## 사용자 결정

2026-08-24 사용자는 다음 Codex 도구를 해당 PM의 기본 작업 경로로 도입하기로 결정했습니다.

- PM1: `Product Design`
- PM2: `Build Web Apps`
- PM6: `Frontend Testing + Product Design Audit`

이 결정은 새 Package 설치나 V2 Core Runtime 연결을 뜻하지 않습니다. 현재 Codex 환경에서
호출 가능한 Skill을 PM 작업에 우선 사용하는 운영 계약입니다. 각 도구는 제거 가능한
작업 Adapter이며 V2 Core의 상태·승인·Version·복구 권한을 갖지 않습니다.

## PM1 — Product Design

### 역할

- 인터뷰와 제작 범위 확인서가 승인된 뒤 시각 방향을 탐색합니다.
- 기존 성공 Recipe로 해결되지 않을 때 서로 다른 시각 방향을 최대 3개 보여줍니다.
- 사용자가 선택한 방향만 Visual Target으로 승격합니다.
- 구현된 화면을 Screenshot 증거로 감사해 사용성·시각 품질·접근성 문제를 찾습니다.

### 경계

- ImageGen 3개 반복은 모든 요청의 기본값이 아닙니다.
- 이미 승인된 Recipe·Reference·Visual Target이 있으면 재사용을 먼저 검토합니다.
- 사용자 선택 전 PM2 구현을 시작하지 않습니다.
- Product Design이 최종 방향이나 PM PASS를 자동 결정하지 않습니다.

### 현재 증거 상태

- `Product Design Audit` 사용 기록이 존재합니다.
- PM1 전체 요청에서 이 경로가 반복 성공했다는 증거는 아직 없습니다.

## PM2 — Build Web Apps

### 역할

- 승인된 Visual Target·Design Recipe·실제 문구와 데이터를 구현합니다.
- 기존 Component와 shadcn Block을 우선 재사용합니다.
- React 화면은 성능·반응형·접근성 기본 규칙을 함께 적용합니다.
- 실행 가능한 Preview를 만든 뒤 PM6 검증 입력으로 넘깁니다.

### 경계

- PM2에서 디자인 방향을 다시 해석하거나 새 시안을 만들지 않습니다.
- Module Manifest·Registry·Slot·권한·오류 격리는 V2 Core 계약을 따릅니다.
- Build Web Apps가 Core 상태를 직접 변경하거나 사용자 승인 없이 배포하지 않습니다.

### 현재 증거 상태

- `frontend-app-builder` 직접 호출과 Browser 기술 검증 기록이 존재합니다.
- 모든 V2 Module 제작에 자동 연결된 Runtime은 아직 없습니다.

## PM6 — Frontend Testing + Product Design Audit

### 역할

- 실제 실행 화면의 Route·Console·상호작용·Desktop·390·430 Viewport를 검사합니다.
- 승인 Visual Target과 구현 Screenshot을 나란히 비교합니다.
- 기능 PASS와 디자인 마감 PASS를 별도로 판정합니다.
- 접근성·반응형·회귀·원본 보존·Undo·Version Restore 증거를 확인합니다.

### 필수 구분

- Build 성공은 기능 PASS가 아닙니다.
- 기능 PASS는 디자인 품질 PASS가 아닙니다.
- Product Design Audit 결과는 사용자 최종 승인을 대신하지 않습니다.
- Screenshot만 확인하고 실제 상호작용을 검증했다고 말하지 않습니다.

### 현재 증거 상태

- 개별 Browser·Viewport·상호작용 검증 기록은 존재합니다.
- 이 통합 PM6 경로의 실제 고객 결과물 E2E는 아직 `not_proven`입니다.

## 기본 실행 흐름

```text
PM5 인터뷰·제작 범위 확인
→ 기존 성공 Recipe 우선 확인
→ PM1 Product Design으로 필요한 방향만 탐색·선택
→ 사용자 Visual Target 승인
→ PM2 Build Web Apps로 승인안 구현
→ PM3에서 사용자 부분 수정
→ PM6 Frontend Testing으로 기능·회귀 검사
→ PM6 Product Design Audit으로 디자인 마감 검사
→ 사용자 최종 승인
→ Version 저장·복구 증거 고정
```

## 제거 계약

해당 도구가 시간·품질·재작업을 개선하지 못하면 PM 계약에서 호출만 제거합니다. 제거 후에도
Interview Receipt·Visual Target·Design Recipe·Module·Version·검증 증거·복구 Commit은
그대로 유지되어야 합니다.

## Codex Sites 후속 적용 경계

- 개인정보·결제·중요 데이터가 없는 고객 웹은 조건부 우선 후보로 사용합니다.
- 로그인·간단한 데이터가 포함되면 격리 Pilot을 먼저 수행합니다.
- 결제·민감정보·복잡한 권한·관리자 기능·Migration·다중 사용자·V2 Core 연동이 발견되면 작업을 확대하지 않고 사용자 회의를 요청합니다.
- 복잡한 프로젝트는 현재 검증된 `Antigravity 구현 + Codex 독립 검증` 경로와 Sites 범위 확장 Pilot을 비교한 뒤 사용자가 결정합니다.
- 반복 성공 증거가 쌓이면 허용 범위를 넓힐 수 있지만, 사용자 승인 없는 자동 배포는 금지합니다.

## 첫 통합검증 대상

2026-08-24 사용자 회의에서 기존 병원 웹을 첫 통합검증 대상으로 확정했습니다.

```yaml
pilot_project: existing_hospital_web
workspace: isolated_copy
preserve_original: true
deployment: excluded
target_flow:
  - PM1_Product_Design
  - PM2_Build_Web_Apps
  - PM3_partial_edit
  - PM6_Frontend_Testing
  - PM6_Product_Design_Audit
user_final_approval: required
version_restore_evidence: required
execution_status: not_started
```

- 기존 병원 웹과 기존 증거를 직접 수정하거나 통합검증 PASS 기준에 맞춰 갱신하지 않습니다.
- 시작 전 기존 Interview Receipt·Visual Target·Recipe·잠금 Commit을 확인하고, 이번 변경 범위만 짧은 인터뷰로 확정합니다.
- PM1에서는 필요한 디자인 개선 방향만 확인하고, PM2는 승인된 방향을 다시 해석하지 않습니다.
- PM3 수정은 새 Draft에만 기록하고, PM6에서 기능·모바일·접근성·회귀·디자인 마감을 각각 판정합니다.
- 실패하거나 사용자가 중단하면 격리 복사본만 폐기할 수 있어야 합니다.

## 판정

```yaml
adoption_decision: approved_by_user
installation_required: false
pm1_product_design: adopted_as_codex_work_adapter
pm2_build_web_apps: adopted_as_codex_work_adapter
pm6_frontend_testing: adopted_as_codex_verification_adapter
pm6_product_design_audit: adopted_as_codex_design_quality_adapter
v2_core_runtime_integration: not_implemented
integrated_e2e_evidence: not_proven
next_validation: isolated_existing_hospital_web_pm1_to_pm6
```

## oh-my-design 비교 순서 결정

2026-08-24 사용자는 현재 병원 웹 A/B 결과를 예비 증거로만 보존하고,
oh-my-design의 공식 채택 판정을 확정된 V2 디자인 탐색·채택 흐름 Runtime 연결 이후로
미루기로 결정했습니다.

- 현재 A/B는 Codex가 일부 단계를 수동 실행한 격리 Pilot입니다.
- 현재 결과를 V2 Core 생성·공식 Design Recipe·전체 E2E 증거로 사용하지 않습니다.
- 먼저 `인터뷰 → 기존 Recipe 확인 → 후보 탐색 → 서로 다른 3개 방향 → 사용자 선택 →
  선택 후보의 Design DNA → Visual Target → Design Recipe`를 V2 실행 흐름으로 연결합니다.
- 그 뒤 같은 Brief·문구·기능·이미지·Viewport를 고정해 V2 기본 흐름과
  oh-my-design을 다시 비교합니다.
- 최종 채택·보류·폐기는 두 번째 비교 결과를 본 사용자가 결정합니다.

```yaml
oh_my_design_current_status: preliminary_isolated_pilot
adoption_decision: deferred_until_v2_baseline_exists
comparison_fairness_contract: same_brief_content_function_assets_viewports
core_changed_by_trial: false
```
