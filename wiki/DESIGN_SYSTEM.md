# AI OS V2 디자인 시스템

최종 갱신: 2026-08-20
상태: 사용자 회의 결정 반영·구현 전 계약 포함
공식 이름: `V2 디자인 시스템(Design System, 디자인 시스템)`

이 문서는 AI OS V2의 디자인 탐색·채택·구현·수정·검증 규칙을 한곳에 모은 **공식 원본**입니다. 다른 Wiki, 과거 Run, Pilot 보고서와 디자인 규칙이 충돌하면 현재 Commit의 이 문서를 우선하고 충돌을 보고합니다. 과거 문서는 당시 판단과 실패·검증 증거로 보존하며 삭제하지 않습니다.

## 1. 범위와 용어

- `V2 운영 화면`: V2를 조작하는 PC 전용 보드 화면입니다.
- `고객 결과물`: V2가 제작하는 웹사이트·앱·기능 도구·전자명함·업무용 자식 OS 등입니다. 자식 OS는 고객 결과물의 한 종류이지 고객 결과물 전체를 뜻하지 않습니다.
- `Reference(레퍼런스, 참고 디자인)`: 사용자가 눈으로 확인하고 전체 또는 일부를 선택할 실제 디자인 사례입니다.
- `디자인 총괄(Design Director, 디자인 디렉터)`: 사용자가 선택한 Reference를 프로젝트 목적에 맞는 하나의 구현 가능한 방향으로 정리하는 역할입니다.
- `Design Recipe(디자인 레시피)`: V2가 소유하는 Versioned 디자인 상태 원본입니다.
- `DESIGN.md(디자인 엠디)`: 필요할 때 Design Recipe에서 생성하는 AI용 읽기 형식입니다. 별도 원본이 아니며 독립적으로 수정하지 않습니다.
- `Visual Target(비주얼 타깃)`: 사용자가 구현 전 방향을 눈으로 확인하는 이미지입니다.

`V2가 OS형 제작 플랫폼이라는 정의`는 상태·승인·Skill·Module·복구를 소유하는 구조 설명입니다. 디자인 검색어·Layout·색상·Typography를 운영체제 Dashboard처럼 제한하는 시각 스타일 지시가 아닙니다. Reference 조사와 후보 시험에서는 기본적으로 `조립형 제작 작업공간`이라고 표현하며, 사용자가 요청하지 않은 OS형 외관을 자동 적용하지 않습니다.

에반의 skills.ag `DESIGN.md` Skill은 실제 파일을 확보·감사하지 않았으므로 Runtime Skill로 채택하지 않습니다. 다만 색상·글꼴·간격·Component 규칙을 YAML+Markdown 한 장으로 고정해 다음 AI가 같은 방향을 유지하게 하는 공개 개념은 디자인 시스템 설계 참고로 채택합니다. V2의 원본은 Design Recipe이며, 에반 Skill을 디자인 총괄이나 Reference 공급처로 간주하지 않습니다.

## 2. 디자인 규칙의 분리

V2 운영 화면과 고객 결과물은 기본 품질 규칙만 공유합니다. 색상·글꼴·배치·이미지·Motion·브랜드 개성은 서로 분리합니다.

### 공통 품질 규칙

1. 정보 우선순위가 분명해야 합니다.
2. 여백이 일관되고 의도적으로 사용돼야 합니다.
3. 제목·본문·보조 정보의 글자 위계가 분명해야 합니다.
4. 기본·Hover·Focus·Disabled·Loading·Empty·Error·Success 상태가 필요한 범위에서 완성돼야 합니다.
5. Border와 Surface가 식별 가능하고 Contrast가 접근성 기준을 해치지 않아야 합니다.
6. 대상 Viewport에서 Layout과 줄바꿈이 무너지지 않아야 합니다.
7. Motion은 상태와 행동을 설명할 때만 사용하고 동작 줄이기를 지원해야 합니다.
8. 선택한 Reference 또는 승인된 Visual Target과 실제 결과의 방향이 일치해야 합니다.
9. 사용자가 핵심 작업을 완료할 수 있어야 합니다.
10. 기술 검사 PASS와 사용자 시각 승인 PASS를 분리합니다.

### 현재 V2 운영 화면 규칙

- 밝은 PC 전용 작업 보드
- 밝은 중성 배경과 구분되는 Surface
- 짙은 본문 Text
- 선명한 Primary Action
- 정상·동기화 상태의 별도 의미색
- 중간 정보 밀도와 초보자용 쉬운 문구
- 내부 Run ID·Commit·Port·PID·Agent Log는 기본 화면에서 숨김

현재 색상값은 영구 브랜드 규칙이 아니라 PM1에서 승인된 방향입니다. 변경할 때는 새 Design Recipe Version과 사용자 승인이 필요합니다.

### 고객 결과물 규칙

- 프로젝트마다 별도 Design Recipe를 사용합니다.
- 모바일 결과가 필요한 고객 제품은 하나의 모바일 규칙을 사용하고 `390px`, `430px`에서 회귀검증합니다.
- PC 변경이 모바일 Override를 자동 변경하지 않습니다.
- 같은 업종이라도 정보 우선순위·Navigation·Media·기능·시각 방향을 프로젝트 목적에 맞게 정합니다.
- 고유한 시각 요소의 최소 개수를 강제하지 않습니다. 필요한 차별점만 디자인 총괄이 제안하고 사용자가 선택합니다.

## 3. 공식 역할 분담

### 사용자

- Reference의 전체·부분 선택
- 디자인 방향 승인
- 최종 결과의 채택·수정·폐기 판정

### Codex(코덱스)

- 저장소 사실 확인과 디자인 요청서 정리
- 디자인 총괄 절차 실행과 방향 제안
- Reference 출처·접근·라이선스·구현 가능성 확인
- Antigravity용 작업 지시서 작성
- V2 Core·Run·Gate·Skill 연결과 독립 기술 검증
- 사용자 승인 후 Commit·복구점 관리

Codex는 공식 제품 구현자가 아니며 사용자 대신 디자인을 확정하거나 PASS하지 않습니다.

### Antigravity(안티그래비티)

- 승인된 Visual Target·Design Recipe·작업 지시서를 기준으로 실제 웹·앱·화면·기능 구현
- 승인된 Component·Skill·Motion 적용
- 변경 파일·실행 결과·남은 문제 보고

Antigravity는 디자인 방향·범위를 임의로 확대하거나 자신의 구현을 최종 PASS하지 않습니다.

### V2 Core

- 현재 단계·허용 Action·승인 상태·Version·Evidence·Rollback·Restore 소유
- 디자인을 생성하거나 사용자를 대신해 판단하지 않음

동일 Run에는 한 시점에 쓰기 담당자 한 명만 허용합니다. 공식 기본은 `Antigravity 구현 → Codex 독립 검증 → 사용자 판정`입니다.

## 4. 디자인 탐색·채택·구현 흐름

```text
쉬운 사용자 요청
→ Codex가 짧은 디자인 요청서로 정리
→ 기존 성공 Recipe·Block으로 해결 가능한지 확인
→ 부족할 때만 V2 수집기가 한국 중심 실제 Reference 조사
→ 비교 이미지 한 장과 원본 링크 제공
→ 사용자가 전체·부분 선택
→ 출처·라이선스·반응형·기술·자산의 제작 가능성 확인
→ Codex가 디자인 총괄 절차로 하나의 구현 가능한 방향 제안
→ 방향 Visual Target 한 장을 사용자가 승인
→ Design Recipe와 구현 Component 목록 확정
→ UI UX Pro가 사용성·접근성·기본 규칙 검사
→ Codex가 Antigravity 작업 지시서 작성
→ Antigravity가 실제 구현
→ 동일 조건에서 Reference·Visual Target·실제 결과 비교
→ V2 Design Finish가 마감 검사
→ Codex 독립 기술 검증
→ 사용자 채택·수정·폐기
→ 채택 결과만 성공 Recipe·Block으로 승격
```

사용자가 직접 결정하는 기본 지점은 `요청 확인`, `Reference 선택`, `방향 이미지 승인`, `최종 판정`입니다. 나머지는 내부 절차로 처리하고 전문용어를 기본 화면에 노출하지 않습니다.

## 5. Reference 제공 계약

- 한국의 품질 좋은 실제 웹·서비스·브랜드·디자인 회사 사례를 우선합니다.
- 부족한 구조·표현만 해외 Reference로 보완하고 한국·해외를 구분합니다.
- 기본 산출물은 후보를 비교하는 **이미지 한 장**과 클릭 가능한 원본 링크입니다.
- 후보마다 `추천 이유`, `가져올 부분`, `가져오지 않을 부분`, `접근 확인일`을 표시합니다.
- 사용자가 요청할 때만 상세 PDF를 만듭니다. PDF는 이미지·구성요소·구현 조건을 함께 볼 가치가 있을 때만 사용합니다.
- 로그인·접근 제한·저장 금지 화면을 우회하거나 무단 복제하지 않습니다.
- 문구·Logo·브랜드 자산은 기본적으로 가져오지 않습니다.
- 수집기를 항상 실행하지 않습니다. 기존 성공 Recipe·Block으로 충분하면 재사용합니다.

## 6. 디자인 총괄 계약

디자인 총괄은 다음을 한 방향으로 정리합니다.

- 프로젝트가 줄 인상
- 사용자와 핵심 행동
- 정보 우선순위와 화면 구조
- 채택한 Reference의 전체·부분
- 가져오지 않을 요소
- 색상·글꼴·간격·정보 밀도
- Component·이미지·Motion 방향
- PC·모바일 기준
- 실제 구현 가능한 Component·Block 후보

`UI Craft(유아이 크래프트)`를 우선 후보로 사용합니다. 회의 종료 후 실제 파일·License·Script·외부 전송·V2 충돌을 감사하고 안전하면 원형을 유지한 채 격리 적용합니다. 부족한 연결만 V2 Adapter로 보완하고 효과가 없으면 제거할 수 있어야 합니다. 아직 설치·채택·검증 완료로 기록하지 않습니다.

후보 비교는 Repo-local Skill `V2 Design Director`와 고정 Brief `v2-ui-project-workspace-v1`을 사용합니다. 모든 후보는 같은 V2 Fixture와 `1440x950` 조건에서 하나씩 시험하고, 탐색 Source·선택 부분·총괄의 유지·수정·거절·시각 결과·구현 가능성·사용자 판정을 기록합니다. 단순 연결 확인이나 Markdown 보고서만으로 디자인 후보 시험을 PASS하지 않습니다.

Victor Design과 Design Skill은 조사 참고 후보일 뿐 현재 기본 Skill로 채택하지 않습니다. UI UX Pro는 디자인 총괄이 아니라 사용성·접근성·규칙 검사 역할입니다.

## 7. Design Recipe와 DESIGN.md

Design Recipe는 최소한 다음을 Version별로 보존합니다.

- 프로젝트와 대상 Surface
- Section ID·Module ID·Slot·순서·표시 상태
- Layout·크기 제한·Spacing·Typography·Color Token
- Reference URL·사용 부분·License·선택 상태
- Desktop·Mobile Override
- 직접 편집·자연어 편집·Restore Diff
- Draft·Approved·Applied·Discarded·Restored 상태

기존 Version을 덮어쓰지 않습니다. 직접 편집과 자연어 편집은 같은 Recipe Diff를 만들고 사용자 승인 전 실제 제품에 적용하지 않습니다.

`DESIGN.md`가 필요하면 승인된 Design Recipe에서 생성합니다. Recipe 변경 시 다시 생성하며 DESIGN.md를 따로 편집해 두 원본을 만들지 않습니다.

## 8. 마감과 검증

Reference·Visual Target·구현 결과 비교 시 다음 조건을 고정합니다.

- Viewport
- 실제 또는 승인된 Fixture 데이터
- 화면 상태
- Light·Dark Mode
- 확대 비율
- Motion 재생 시점

마감 검사는 공통 품질 규칙 10개를 사용합니다. Build·Type·Console·접근성·회귀검사를 통과해도 디자인 품질이 자동 PASS되는 것은 아닙니다. 사용자 시각 승인과 실제 작업 완료를 별도로 확인합니다.

## 9. PM 연결과 현재 사실

- PM1: 디자인 요청·Reference·디자인 총괄·Visual Target 채택
- PM2: 승인된 Recipe·Component를 실제 Module로 조립
- PM3: 마우스 중심 부분 수정·Motion·Version·Restore
- PM4: 디자인 외 일반 자료·병목의 제한 조사
- PM5: 최초 의도·변경 범위·자산 경계 재확인
- PM6: 디자인·기능·접근성·성능·회귀·복구 통합 검증

PM1과 PM2는 잠금 기준이 존재하며 현재 활성 단계는 PM3입니다. 최근 Puck·React Grid Layout Pilot은 PM3 격리 시험이며 Core Registry 승격·실제 고객 제품 적용·사용자 최종 PASS는 아직 증명되지 않았습니다.

현재 PM1의 기존 기본 방식은 사용자 PASS 증거로 보존합니다. 이번 디자인 총괄·한국 중심 Reference 비교 이미지 흐름은 사용자 회의에서 승인된 **다음 개선 계약**이며 아직 V2 Core 자동 기능으로 구현·검증된 것은 아닙니다.

## 10. 과거 문서 보존과 충돌 처리

다음 문서는 삭제하지 않고 역사·조사·실패·검증 증거로만 사용합니다.

- `PM1_REFERENCE_BRIEF.md`
- `PM1_REFERENCE_BOARD.md`
- `PM1_VISUAL_TARGET_FINISH_REPORT.md`
- `V2_DESIGN_INTELLIGENCE_RESEARCH_2026-08-18.md`
- `V2_DESIGN_SKILL_DIVERSITY_RESEARCH_2026-08-18.md`
- `DESIGN_INTELLIGENCE_IMPLEMENTATION_AUDIT_2026-08-18.md`
- `POST_MVP_FINAL_DESIGN.md`의 과거 PM 번호 체계

새 디자인 결정은 이 문서에 먼저 반영하고 다른 문서에는 상태와 링크만 기록합니다. 별도의 디자인 원본 문서를 늘리지 않습니다.

## 11. 이번 회의 결과

- V2 운영 화면과 고객 결과물 디자인 규칙 분리: 확정
- 디자인 총괄 단계 추가: 확정
- Codex·Antigravity·사용자·Core 역할 분리: 확정
- 한국 Reference 우선, 해외 보완: 확정
- Reference 비교 이미지 한 장과 원본 링크: 확정
- PDF 기본 제공: 제외, 요청 시 선택
- 고유 시각 요소 최소 개수: 강제하지 않음
- 에반 DESIGN.md Skill: Runtime 채택 제외, 한 장의 AI용 디자인 시스템 개념은 설계 참고
- UI Craft: 원형 우선 격리 감사 후보
- DESIGN.md: Design Recipe의 선택형 파생 형식
- 문서·코드 변경은 회의 종료 후 수행: 준수

**회의가 끝났습니다.**

## 12. 디자인 공급원 다중 채택과 추적 자동화

2026-08-20 사용자 비교 시험 결과, 한 공급원만 선택하지 않고 역할이 다른 채택 공급원을 조합하는 방식을 확정했습니다. 기본 역할은 `방향 탐색`, `구현 Block`, `정보 구조`, `품질 검사`, `Motion·표현`으로 분리합니다. 사용자에게 보여주는 방향 3개는 빠른 비교 시안이며, 실제 Code Preview는 선택된 조합 하나만 제작합니다.

링크·Screenshot을 새로 받으면 수집기와 분석기가 접근·출처·License·사용 부분을 확인하고 사용자는 시각 결과를 본 뒤 `채택·보류·폐기`합니다. 기존 성공 Recipe·Block으로 충분하면 수집기를 실행하지 않습니다. 채택 전 자료는 후보이며 기본 공급원으로 자동 승격하지 않습니다.

Repo-local `V2 Design Director`는 채택 Trial→역할별 Section→Draft Design Recipe→실제 HTML 출처 표시를 자동 검사합니다. 자동화는 사용자 결정을 대신하지 않고 Core·제품에 적용하지 않습니다. 검증 결과와 한계는 [[DESIGN_SUPPLIER_TRIAL_SYNC_2026-08-20]]을 사용합니다.
