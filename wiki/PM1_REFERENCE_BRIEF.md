# PM1 Reference Brief — V2 디자인 채택 방식 시험

작성일: 2026-08-17  
상태: PM1 조사 입력 승인  
대상: `v2_board`  
구현 상태: 시작 전

## 1. 시험 목적

AI OS V2 운영 UI의 디자인 하나를 바로 확정하는 것이 아니라, 초보자가 전문용어와 반복 이미지 생성 없이 좋은 방향을 빠르게 고를 수 있는 채택 방식을 비교합니다.

비교할 방식은 다음 세 가지입니다.

1. `추천형`: V2가 실제 Reference 10개 이상을 조사하고 구조가 다른 추천 3개를 먼저 보여줍니다.
2. `Reference 가져오기`: 사용자가 URL 또는 Screenshot을 제공하고 화면 전체나 사용할 Section을 마우스로 선택합니다.
3. `직접 조립형`: 검증된 Block·Section 후보를 골라 순서를 조합한 저비용 구조 Draft를 확인합니다.

모든 방식에서 `현재안 유지`, `다른 방식`, `중단`을 선택할 수 있습니다. 사용자가 편하다고 판정한 방식만 이후 V2 기본 Workflow 후보가 됩니다.

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

최소 10개를 조사하되 숫자를 채우기 위해 비슷한 구조를 반복하지 않습니다.

각 후보 기록:

- URL과 접근 확인 시점
- `visual_reference` 또는 `reusable_code_block`
- 사용할 화면·Section
- V2에 적용할 구체적인 부분
- 라이선스와 코드 재사용 가능 여부
- 의존성과 React 19·Vite 호환 가능성
- 접근성·반응형·구현 난이도
- Section ID 후보

같은 기준으로 0~5점을 기록하지만 총점으로 자동 선택하지 않습니다. 추천 3개와 전체 목록을 모두 사용자가 열람할 수 있어야 합니다.

## 6. 저비용 Preview 원칙

```text
Reference 10개 이상
→ 구조가 다른 추천 3개
→ Section 선택·조합
→ 구조 Draft 1~2개
→ 방향 확인
→ 실제 V2 데이터 Code Preview 1개
→ 사용자 채택 방식·디자인 판정
```

- 여러 Reference 조합을 이해하기 어려울 때만 조합 이미지 한 장을 만듭니다.
- 반복 ImageGen A/B/C는 기본 흐름으로 사용하지 않습니다.
- 사용자 방향 승인 전 Image-to-Code를 시작하지 않습니다.
- 중단하면 제품·Recipe·Registry를 변경하지 않습니다.
- 검증된 Browser 기본 기능과 현재 Stack을 우선하며, 여러 UI·Animation Library를 동시에 설치해 비교하지 않습니다.
- 새로운 도구는 현재 기본 방식의 부족함이 실제 증거로 확인된 뒤 제거 가능한 격리 Pilot 하나로만 검증합니다.

## 7. 도구 역할과 적용 가치

| 도구 | PM1 역할 | 현재 판정 |
|---|---|---|
| Product Design | Reference 근거·화면 비교·시각 검증 절차 | 사용 |
| UI UX Pro | 사용성·구조 분석 보조 | 사용 가능 |
| shadcn·라이선스 확인 OSS | 실제 재사용 가능한 Block 후보 | 우선 조사 |
| NotebookLM | 공식 문서·웹·YouTube 자막의 수동 출처 비교 | 선택 보조, Core 연결 없음 |
| Google Stitch | 자연어·이미지 기반 생성 방향을 Reference-first 결과와 비교 | 선택 후보, 기본 방식 아님 |
| Taste Skill | 시각 평가 보조 | 미검증 후보 |
| Puck | 승인된 Recipe의 부분 편집 Adapter | PM3 조건부 후보, PM1 설치 금지 |
| Lighthouse·PageSpeed Insights | 고객 결과물 성능·접근성 검증 | PM2 이후 |
| Google Drive | 외부 Backup 후보 | 사용자 요청으로 PM1 동안 유예 |

NotebookLM의 요약과 Stitch의 생성 결과는 검증 증거를 대신하지 않습니다. Google 도구는 제거 가능한 보조 수단이며 계정·API·유료 연결을 PM1 필수 조건으로 만들지 않습니다.

## 8. PM1 PASS 조건

- 실제 Reference 10개 이상과 구조가 다른 추천 3개를 보여줍니다.
- 출처·접근·라이선스·사용 부분·구현 가능성을 기록합니다.
- 현재안·추천형·가져오기·직접 조립형을 마우스로 전환합니다.
- 전체 화면 또는 특정 Section을 선택할 수 있습니다.
- 실제 V2 데이터 Code Preview는 최종 후보 하나만 만듭니다.
- 사용자가 디자인 품질과 채택 방식 편의성을 각각 판정합니다.
- 선택 결과를 Visual Target·Section ID·Design Recipe에 연결합니다.
- 사용자 승인 전 PM2 구현을 시작하지 않습니다.

## 9. 현재 Gate

```yaml
pm0: pass_with_user_deferred_backup
pm1: active
pm1_method_selected: false
pm1_visual_target_approved: false
pm2_allowed: false
product_code_changed: false
core_code_changed: false
```

다음 한 작업은 이 Brief를 바탕으로 실제 Reference 10개 이상을 조사하고, Reference Board 초안을 만드는 것입니다.
