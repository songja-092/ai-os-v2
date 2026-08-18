# AI OS V2 — PM1 Visual Target 제작부터 마감까지 결과 보고서

작성일: 2026-08-18
대상: V2 운영 UI PC 대시보드 1개 화면
구현 형태: PM1 격리 Fixture 기반 Interactive Prototype
최종 판정: `PROTOTYPE_PASS / PRODUCTION_NOT_READY`

## 1. 요약

승인된 Visual Target을 실제 브라우저에서 작동하는 PC 대시보드로 구현하고, 원본과 동일 Viewport에서 비교·수정·상호작용 검증까지 마쳤습니다.

현재 결과는 **디자인 회사가 고객에게 방향 확인용으로 보여줄 수 있는 완성도 높은 Prototype**으로는 볼 수 있습니다. 그러나 **실제 납품·운영까지 끝낸 디자인 회사의 최종 결과물**로 보기는 어렵습니다. 가장 큰 이유는 화면의 미관이 아니라 Core 실제 데이터 연결, 전체 상태 설계, 접근성 자동·수동 검사, 여러 화면의 일관성, 실제 사용자 검증이 아직 없기 때문입니다.

```yaml
visual_direction: approved
interactive_prototype: pass
visual_fidelity: pass
core_data_connection: not_implemented
full_state_design: incomplete
accessibility_verification: incomplete
real_user_validation: not_performed
production_readiness: not_ready
```

## 2. 증거

### 승인 Visual Target

![승인 Visual Target](/home/user/바탕화면/v2_ui_images/AI%20OS%20V2%20PM1%20Visual%20Target%20v1.png)

- 원본: `/home/user/바탕화면/v2_ui_images/AI OS V2 PM1 Visual Target v1.png`
- 크기: `1586 × 992`
- SHA-256: `d2738069ee6a404c8c25da2e0eecf8a7c5e4801fee1a5e59d0b5532fc0c66a2a`

### 브라우저 구현 결과

![브라우저 구현 결과](/home/user/바탕화면/ai_os_v2_pm1/pm1-artifacts/visual-target-v1/audit-evidence/01-dashboard-default.jpg)

- Route: `http://127.0.0.1:8200/pm1-finish-test`
- 감사 캡처: `1600 × 1000`
- 기본 상태 증거: `pm1-artifacts/visual-target-v1/audit-evidence/01-dashboard-default.jpg`

### 제작 흐름 펼친 상태

![제작 흐름 펼친 상태](/home/user/바탕화면/ai_os_v2_pm1/pm1-artifacts/visual-target-v1/audit-evidence/02-flow-expanded.jpg)

- 펼치기 상태: `aria-expanded=true`
- 증거: `pm1-artifacts/visual-target-v1/audit-evidence/02-flow-expanded.jpg`

## 3. 제작 과정

| 단계 | 수행 내용 | 도구·근거 | 결과 |
|---|---|---|---|
| 1. 방향 정리 | 기존 V2 대시보드의 정보 과다, 어두운 Sidebar, 작업실 혼합 문제를 제거 | 사용자 피드백, 기존 Version 보존 | PASS |
| 2. 디자인 규칙 | 밝은 청회색 Shell, 흰 Surface, Navy Text, Blue Action, Teal Sync, 중간 정보 밀도 설정 | UI UX Pro Max | PASS |
| 3. 구현 후보 확인 | Sidebar와 Dashboard Block의 구조·의존성·License를 읽기 전용 확인 | shadcn `sidebar-07`, `dashboard-01` | PASS, 설치 안 함 |
| 4. Visual Target 제작 | PC 전용 대시보드 한 장 생성 | OpenAI built-in ImageGen | PASS |
| 5. 사용자 방향 승인 | 사용자가 “오케이 이걸로하고”로 시각 방향 승인 | `manifest.json` | PASS, PM1 전체 승인 아님 |
| 6. 정적 마감 Audit | 상태색, 중복 문구, 흐린 Border, Core 상태 추정 문제 확인 | Product Design Audit | PASS_WITH_FIX |
| 7. 실제 구현 | 승인 이미지의 구조를 HTML·CSS·JavaScript로 재현 | Codex image-to-code, Material Symbols | PASS |
| 8. 기능 연결 | 검색, Filter, 제작 흐름, 동기화 Feedback 구현 | Fixture 기반 Browser Prototype | PASS |
| 9. 시각 비교 | 원본과 구현을 동일 보드에서 비교 | `PM1 Finish Comparison.jpg` | PASS |
| 10. 디자인 QA | Typography, Spacing, Color, Asset, Copy 검사 | `design-qa.md` | PASS |

## 4. 실제로 작동하는 기능

1. 프로젝트 이름 검색
2. 프로젝트 유형별 Filter
3. 제작 흐름 펼치기·접기
4. 동기화 확인 Feedback
5. 빠른 실행과 프로젝트 열기 Feedback
6. PC 대시보드 기본 Navigation 표현

단, 현재 동작은 실제 V2 Core가 아닌 Fixture입니다. `새 프로젝트`, `프로젝트 열기`, 각 전역 메뉴는 완전한 다음 화면으로 이어지지 않습니다.

## 5. 잘된 부분

### 정보 구조

- 사용자가 가장 먼저 보는 항목이 `빠른 실행`과 `프로젝트`로 정리됐습니다.
- 전역 Navigation과 프로젝트 작업 영역의 역할이 분리됐습니다.
- Core 제작 흐름은 기본적으로 숨겨져 초보자에게 불필요한 복잡성을 주지 않습니다.
- 프로젝트가 많아질 때 검색과 유형 Filter로 확장할 기본 구조가 있습니다.

### 시각 마감

- 밝은 청회색 Navigation과 흰 Panel의 구분이 안정적입니다.
- Border, 글자 Contrast, 간격이 ImageGen 원본보다 실제 구현에서 선명해졌습니다.
- Blue·Teal·Amber·Purple을 Action·정상·대기·검증 상태에 나눠 사용했습니다.
- Radius와 Shadow가 절제돼 업무용 도구의 신뢰감을 유지합니다.

### 초보자 친화성

- Run ID, Commit, Port, 내부 Gate, Agent Log를 기본 화면에서 숨겼습니다.
- `새 프로젝트`, `기존 프로젝트 등록`, `최근 작업 계속`처럼 행동 중심 문구를 사용했습니다.
- 완료가 아닌 디자인 확인 상태를 초록 Check가 아닌 Amber 대기로 표현했습니다.

## 6. 부족한 부분과 우선순위

### P0 — PM2 구현 전 반드시 해결

#### 1. Core 상태와 연결되지 않음

현재 프로젝트 상태, 다음 행동, 시간, 동기화 상태는 Fixture입니다. 실제 제품에서는 Core `ui-state`와 `allowed_actions`만 표시해야 합니다.

필요 작업:

- Fixture 제거
- Core 상태 → UI View Model Adapter 구현
- 허용되지 않은 Button 자동 숨김
- Project 간 상태 혼합 차단

#### 2. 핵심 사용 흐름이 끝까지 이어지지 않음

현재 Button은 Feedback만 제공하며 새 프로젝트 생성, 기존 프로젝트 등록, 작업실 진입을 완료하지 못합니다.

필요 작업:

- `새 프로젝트` 최소 Flow
- `기존 프로젝트 등록` 최소 Flow
- 프로젝트 작업실 Route
- 중단·재개·복구 Flow

### P1 — 디자인 회사 최종 납품 전 필요

#### 3. 상태 설계가 부족함

현재 정상 Fixture만 있습니다.

빠진 상태:

- 빈 프로젝트
- 검색 결과 없음
- Loading
- 동기화 실패
- Background 작업 실패
- 권한 또는 Action 불가
- Offline·재연결
- 긴 프로젝트명과 50개 이상 프로젝트

#### 4. 접근성 검증이 부족함

Semantic Label 일부와 `aria-expanded`는 적용됐지만 다음은 검증하지 않았습니다.

- 전체 Keyboard 이동 순서
- 명확한 `:focus-visible`
- Screen Reader 상태 알림
- 실제 색 Contrast 측정
- 200% Zoom과 Text 확대
- Motion 감소 설정

따라서 WCAG 준수라고 주장할 수 없습니다.

#### 5. 시각적 개성이 약함

현재는 안정적인 B2B Dashboard 문법을 잘 따르지만, AI OS V2만의 강한 시각 Signature는 부족합니다. 경쟁 Dashboard와 구분되는 고유한 Project State 표현, Preview 방식, Module 조립 표현이 아직 없습니다.

#### 6. 상태와 다음 행동이 일부 반복됨

`디자인 확인`과 `디자인 확인하기`, `구현 계속`과 `구현 계속하기`가 가까이 배치돼 정보가 약간 중복됩니다. Core 상태 연결 시 상태는 짧게, 다음 행동은 Button 하나로 더 분리해야 합니다.

### P2 — PM2·PM3에서 개선

#### 7. Component화되지 않은 단일 HTML

현재는 검증용 한 파일입니다. Module Manifest, Registry, Slot Renderer, Design Recipe가 실제 React Component를 소유하지 않습니다.

#### 8. 실제 Thumbnail 품질이 일정하지 않음

기존 증거 이미지를 Fixture Thumbnail로 사용해 Crop과 선명도가 제각각입니다. 실제 Project Preview Capture 계약이 필요합니다.

#### 9. 펼친 제작 흐름에서 세로 공간이 증가함

1600×1000에서 펼친 흐름은 프로젝트와 오른쪽 동기화 Panel 일부를 아래로 밀어냅니다. 사용자에게 중요한 작업이 가려지지 않도록 Overlay, Drawer 또는 더 조밀한 Step Bar를 비교할 필요가 있습니다.

#### 10. 자동화된 품질 환경이 아직 없음

현재 Browser 수동 검증은 했지만 다음은 아직 연결되지 않았습니다.

- Playwright 기준 Screenshot 회귀
- axe 자동 접근성 1차 검사
- Storybook Component 상태 전시장
- 실제 Performance Budget
- 여러 OS·Font 환경 검사

## 7. 품질 평가

### Prototype 기준

| 평가 항목 | 점수 | 판단 |
|---|---:|---|
| 정보 우선순위 | 86/100 | 중요한 행동과 프로젝트가 잘 보임 |
| Layout·Spacing | 83/100 | 안정적이나 펼친 Flow의 세로 점유 개선 필요 |
| Typography | 79/100 | 읽기 쉽지만 브랜드 고유성이 약함 |
| Color·상태 표현 | 82/100 | 상태색 분리 양호, 실제 상태 계약은 미연결 |
| Component 마감 | 78/100 | Border·Radius·Icon 일관성 양호 |
| 초보자 사용성 | 76/100 | 용어는 쉽지만 전체 Task가 아직 끝까지 연결되지 않음 |
| 접근성 증거 | 48/100 | 일부 기반만 있고 검증 부족 |
| 브랜드 차별성 | 58/100 | 안정적이나 범용 B2B Dashboard와 유사 |
| 실제 운영 준비 | 32/100 | Fixture·단일 화면·회귀 자동화 미완료 |

- 시각 Prototype 완성도: **약 80/100**
- 실제 제품 완성도: **약 45/100**

점수는 절대적인 업계 인증이 아니라, 현재 증거 범위에서 다음 작업의 우선순위를 정하기 위한 내부 평가입니다.

## 8. 디자인 회사가 만든 것으로 볼 수 있는가

### 결론

**방향 제안·Interactive Prototype 단계라면 “디자인 회사가 만든 것처럼 보일 수 있다”가 맞습니다.**
**고객에게 최종 납품된 운영 제품이라면 아직 아니다가 맞습니다.**

디자인 회사의 최종 결과물에는 보통 다음이 함께 있어야 합니다.

- 전체 핵심 Flow
- 정상·빈 상태·오류·Loading 상태
- Component와 Token 문서
- 접근성 검증
- 실제 데이터 기반 검증
- 개발 결과와 디자인의 회귀 비교
- 실제 사용자 Task Test
- 수정·승인 기록

현재는 첫 화면의 방향과 마감은 갖췄지만 이 묶음 전체가 없습니다.

```yaml
agency_concept_quality: pass
agency_interactive_prototype_quality: pass_with_limits
agency_final_delivery_quality: not_proven
production_design_system: not_implemented
```

## 9. 디자이너 연차·인원 환산 판단

정확한 연차나 인원은 화면만으로 증명할 수 없으므로 **결과물 범위의 등가 추정치**로만 판단합니다.

### 디자인만 평가

- 등가 수준: **제품 UI 디자이너 3~5년차 1명**이 만든 1차 Interactive Prototype
- Senior Review 환산: **7년차 이상 디자이너의 짧은 Review 0.1~0.2명분**이 더해진 형태와 유사
- 10년차 Lead Designer 수준: **아직 아님**

근거:

- 3~5년차 수준으로 보는 이유: 정보 구조, 간격, 상태색, 초보자 문구, 구현 가능한 Layout이 안정적입니다.
- Senior 단독 결과로 보지 않는 이유: 고유한 Design Language, 복잡한 상태 체계, 실제 사용자 검증, Component System 전체가 없습니다.

### 구현까지 포함

- **제품 UI 디자이너 3~5년차 1명 + Frontend Prototype 개발자 2~4년차 1명**의 짧은 협업 결과와 비슷합니다.
- 또는 **Design Engineer 4~6년차 1명**이 제한된 한 화면을 만든 결과로 볼 수 있습니다.

이는 실제로 여러 사람이 작업했다는 뜻이 아닙니다. ImageGen, UI UX Pro, Codex, Browser QA가 각 역할을 보조한 결과를 사람 팀의 작업 범위로 환산한 것입니다.

## 10. 10년차 이상 수준으로 가기 위한 증거

다음이 완료돼야 10년차 이상 전문가 대체 가능성을 평가할 수 있습니다.

1. 서로 다른 실제 Project 3~5개에서 반복 성공
2. PM2 Module 조립·장애 격리·Restore 통과
3. PM3 마우스 편집·Version·Undo·Restore 통과
4. PM4 자동화 Capability의 채택·폐기 검증
5. PM5 의도 정합성 및 범위 잠금 통과
6. PM6 전체 사용자 Flow·접근성·성능·배포·복구 통과
7. 실제 초보자 사용자가 전문가 도움 없이 Task 완료
8. 외부 전문가 또는 인정된 품질 기준과 Blind 비교

현재 한 화면만으로 “10년차 디자이너를 대체한다”고 주장하면 과장입니다.

## 11. 다음 권장 작업

가장 작은 다음 작업은 **현재 Prototype을 더 예쁘게 다듬는 것이 아니라, PDF 도면 기호 한 프로젝트의 실제 Core `ui-state`와 `allowed_actions`를 이 화면에 연결하는 것**입니다.

그다음 순서:

```text
Core 실제 상태 연결
→ 프로젝트 작업실 한 화면 연결
→ 빈 상태·오류·Loading 추가
→ Keyboard·axe 검사
→ Playwright 기준 Screenshot 저장
→ 사용자 실제 Task 확인
→ PM1 최종 승인 여부 결정
```

## 12. 변경·보존 상태

- Core M1~M7: 변경 없음
- 제품 저장소: 변경 없음
- Run: 생성·수정 없음
- PM2: 시작하지 않음
- Commit·Push: 수행하지 않음
- 기존 rejected Pilot: 보존
- 기존 Dirty 변경: 보존

최종 판정:

```yaml
report_verdict: PASS_WITH_LIMITS
visual_target_to_prototype: completed
design_finish: prototype_pass
design_company_level: concept_and_prototype_only
designer_equivalent: one_mid_level_product_designer_with_light_senior_review
production_ready: false
pm1_final_user_approval: pending
```
