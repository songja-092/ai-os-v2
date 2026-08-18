# PM1 Reference Brief — V2 디자인 채택 방식 시험

작성일: 2026-08-17  
상태: 실패 Pilot 반영 후 우선 Workflow 검증 입력
대상: `v2_board`  
구현 상태: 시작 전

## 1. 시험 목적

초보자가 Reference 목록과 디자인 전문용어를 직접 다루지 않고, 실제 V2 데이터가 들어간 완성도 높은 화면 하나를 빠르게 확인하는 방식을 검증합니다. 우선 후보는 `single_visual_target_with_ui_ux_pro_guard`이며 아직 최종 확정이 아닙니다.

기본 흐름은 `쉬운 요청 → 필요한 Reference만 내부 조사 → UI UX Pro 규칙·품질 검사 → Visual Target 하나 → 부분 수정 → 승인·거절·중단`입니다. 거절된 경우에만 이유를 반영한 구조적으로 다른 대안 하나를 만듭니다.

## 2. 사용자와 사용 환경

- 주 사용자: 개발·디자인 전문용어를 모르는 1인 사용자
- 운영 UI: PC 전용
- 고객 결과물: 모바일 우선이며 390px·430px은 하나의 모바일 규칙을 검증하는 Viewport
- 입력 우선순위: 마우스 선택 → 간단한 선택 버튼 → 자연어 보조
- 기본 화면에서 숨길 것: Run ID, Commit SHA, Port, PID, 내부 Gate와 Agent 로그

## 3. 필요한 화면과 정보

### 대시보드

- 프로젝트 검색·분류·열기
- 빠른 실행
- 백그라운드 작업과 문제 상태
- 최근 완료
- 접을 수 있는 Core 제작 흐름
- 동기화 상태 Panel
- 자료 조사, 스킬·기능, Docker, 작업 기록, 설정 진입점

### 프로젝트 작업실

- 하나의 큰 작업·Preview Panel
- 프로젝트명·유형과 현재 상태
- 선택한 Reference와 사용 Section
- 실제 V2 데이터 Preview
- 채택·다른 방식·중단
- 기술 상세 접기

PM1은 구조와 채택 편의성을 시험합니다. 실제 Module 장착·상태 저장·장애 격리는 PM2, Card 이동·Resize·부분 수정은 PM3 범위입니다.

## 4. 시각 기준

유지할 것:

- 명확한 Panel 경계와 정보 우선순위
- 높은 신뢰감을 주는 절제된 색상
- 읽기 쉬운 글자와 충분한 Contrast
- 큰 Preview와 하나의 주 행동
- 프로젝트가 10개·50개로 늘어나도 검색·필터·목록으로 관리 가능한 구조

피할 것:

- 지나치게 흰 화면과 약한 테두리
- 작은 Preview와 과도한 설명
- 색상만 다른 후보 반복
- 현재 구현되지 않은 기능을 완료된 것처럼 표시
- V2 전체 대시보드와 한 프로젝트 작업실의 역할 혼합
- Figma 수준 자유 Canvas를 PM1에서 구현

## 5. Reference 조사 계약

Reference는 필요할 때 내부적으로 제한 조사하며 개수 채우기를 목표로 하지 않습니다. 같은 화면 종류의 실제 사례, 공식 자료, 라이선스가 확인된 OSS와 검증된 디자인 시스템을 우선합니다. 실제 Screenshot을 Wireframe으로 변환하지 않고 디자인 사례와 UI Library·Editor·Animation 도구를 디자인 후보처럼 섞지 않습니다. 전체 목록과 구역·속성 선택은 사용자가 명시적으로 요청할 때만 제공합니다.

각 후보 기록:

- URL과 접근 확인 시점
- `visual_reference` 또는 `reusable_code_block`
- 사용할 화면·Section
- V2에 적용할 구체적인 부분
- 라이선스와 코드 재사용 가능 여부
- 의존성과 React 19·Vite 호환 가능성
- 접근성·반응형·구현 난이도
- Section ID 후보
- 의미 있는 구역 이름과 Screenshot의 정규화 좌표
- 가져올 속성과 가져오지 않을 속성

필요하면 같은 기준으로 0~5점을 기록하지만 총점으로 자동 선택하지 않습니다. 기본 사용자 화면에는 Visual Target, 쉬운 추천 이유, 선택형 `근거 보기`만 제공합니다.

구역 선택 계약:

```yaml
selection:
  reference_id: string
  region_label: string
  normalized_bounds: {x, y, width, height}
  target_section_id: string
  selected_properties: [layout, spacing]
apply:
  layout: true
  spacing: true
  color: false
  typography: false
  content: false
  branding: false
  motion: false
```

좌표와 의미 있는 구역 이름을 함께 기록합니다. 선택하지 않은 속성은 잠그며 원본 문구·Logo·브랜드 자산은 기본적으로 가져오지 않습니다.

## 6. 저비용 Preview 원칙

```text
쉬운 사용자 요청
→ 필요한 Reference만 내부 조사
→ UI UX Pro 규칙·품질 검사
→ 실제 V2 데이터 Visual Target 1개
→ 사용자 진행·부분 수정·다른 방향·현재안 유지·중단
→ 거절된 경우에만 구조적으로 다른 대안 1개
→ 최종 승인 후 PM2 허용
```

- 여러 Reference 조합을 이해하기 어려울 때만 조합 이미지 한 장을 만듭니다.
- 반복 ImageGen A/B/C는 기본 흐름으로 사용하지 않습니다.
- 사용자 방향 승인 전 Image-to-Code를 시작하지 않습니다.
- Reference와 Preview는 동일 Viewport·실제 V2 데이터·화면 상태·Light/Dark Mode·확대 비율·Motion 시점에서 비교합니다.
- 중단하면 제품·Recipe·Registry를 변경하지 않습니다.
- 검증된 Browser 기본 기능과 현재 Stack을 우선하며, 여러 UI·Animation Library를 동시에 설치해 비교하지 않습니다.
- 새로운 도구는 현재 기본 방식의 부족함이 실제 증거로 확인된 뒤 제거 가능한 격리 Pilot 하나로만 검증합니다.

## 7. 도구 역할과 적용 가치

| 도구 | PM1 역할 | 현재 판정 |
|---|---|---|
| Product Design | Visual Target 제작·시각 검증 절차 | 사용 |
| UI UX Pro | 디자인 규칙 제안·사용성·접근성·최종 품질 검사 | 우선 검증 후보의 Guard |
| shadcn·라이선스 확인 OSS | 실제 재사용 가능한 Block 후보 | 우선 조사 |
| NotebookLM | 공식 문서·웹·YouTube 자막의 수동 출처 비교 | 선택 보조, Core 연결 없음 |
| Google Stitch | 이번 생성 결과 비교 | 사용자 비교에서 기본 방식 거절, 재도입 보류 |
| Taste Skill | 시각 평가 보조 | 미검증 후보 |
| Puck | 승인된 Recipe의 부분 편집 Adapter | PM3 조건부 후보, PM1 설치 금지 |
| Lighthouse·PageSpeed Insights | 고객 결과물 성능·접근성 검증 | PM2 이후 |
| Google Drive | 외부 Backup 후보 | 사용자 요청으로 PM1 동안 유예 |

NotebookLM의 요약과 Stitch의 생성 결과는 검증 증거를 대신하지 않습니다. Google 도구는 제거 가능한 보조 수단이며 계정·API·유료 연결을 PM1 필수 조건으로 만들지 않습니다.

## 8. PM1 PASS 조건

- 실제 V2 데이터로 Visual Target 하나를 만들고 사용한 UI UX Pro 규칙과 Reference가 있다면 출처를 기록합니다.
- 사용자가 실제 화면을 눈으로 확인하고 필요한 Section만 수정할 수 있습니다.
- 부분 수정에서 지정하지 않은 영역을 보존하고 변경 전후를 확인합니다.
- 사용자가 이 방식이 거절된 Pilot보다 빠르고 편하다고 판정합니다.
- 사용자가 디자인 품질을 승인합니다.
- 실패·중단 시 제품·Recipe·Registry와 이전 상태를 보존합니다.
- 사용자 승인 전 PM2 구현을 시작하지 않습니다.

## 9. 현재 Gate

```yaml
pm0: pass_with_user_deferred_backup
pm1: active
pm1_original_pilot: rejected_and_preserved
pm1_reference_board: rejected_and_preserved
pm1_visual_companion: rejected_and_preserved
google_stitch: rejected_by_user_comparison
pm1_selected_workflow: single_visual_target_with_ui_ux_pro_guard
selection_status: preferred_candidate_for_validation
pm1_visual_target_v1: approved_visual_direction_with_implementation_fixes
pm1_visual_target_approved: visual_direction_only
pm1_usability_pass: awaiting_explicit_user_confirmation
pm2_allowed: false
product_code_changed: false
core_code_changed: false
```

다음 한 작업은 사용자 요청·기존 V2 결정·실제 V2 데이터와 기록 가능한 UI UX Pro 규칙을 입력으로 삼아 제품과 분리된 Visual Target 하나의 최소 제작 범위를 확정하는 것입니다.
