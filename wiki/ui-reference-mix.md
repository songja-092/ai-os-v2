# PM1 UI Reference Mix

확인일: 2026-08-14

이 문서는 Post-MVP `PM1 — 얇은 UI`의 클릭형 Preview A/B를 만들기 위한 구조 Reference입니다. 특정 제품을 복제하지 않고 제품마다 1~2개 패턴만 사용합니다. Screenshot, 브랜드, 색상, 아이콘, 이미지와 소스 코드는 복사하지 않습니다.

## Linear

```yaml
name: Linear
official_url: https://linear.app/docs/projects
verified_at: 2026-08-14
useful_pattern:
  - 여러 프로젝트에서 진행 중·최근 항목을 먼저 찾는 구조
  - 프로젝트명 옆의 짧은 상태와 다음 행동
why_it_fits_v2: 프로젝트가 늘어도 현재 작업과 정상·진행 상태를 빠르게 구분할 수 있다.
do_not_copy: Issue·Cycle·팀 협업·Timeline·복잡한 필터
applied_area: PM1 프로젝트 홈
```

## Figma Prototype

```yaml
name: Figma Prototype
official_url: https://help.figma.com/hc/en-us/articles/360040318013-Play-your-prototypes
verified_at: 2026-08-14
useful_pattern:
  - 편집 화면 안의 Inline Preview와 별도 집중 보기
  - 보조 UI 숨김과 기기·크기 전환
why_it_fits_v2: Preview를 작업실의 주인공으로 두고 요청 영역을 접어도 결과 확인을 지속할 수 있다.
do_not_copy: 무한 Canvas·레이어·벡터·디자인 속성 편집기
applied_area: PM1 프로젝트 작업실
```

## ChatGPT Canvas

```yaml
name: ChatGPT Canvas
official_url: https://help.openai.com/en/articles/9930697-deep-research
verified_at: 2026-08-14
useful_pattern:
  - 요청과 결과물을 좌우로 분리
  - 특정 부분을 지정한 수정과 이전 Version 복원
why_it_fits_v2: AI 설명이 Preview를 덮지 않고 요청과 실제 결과의 관계가 명확해진다.
do_not_copy: 범용 ChatGPT 대화·자유 코드 편집·자동 Canvas 전환
applied_area: PM1 요청 패널과 Preview 작업실
```

공식 Help Center의 현재 URL slug는 `deep-research`이지만 실제 문서 제목과 본문은 `What is the canvas feature in ChatGPT and how do I use it?`이며 Canvas 기능을 설명하는 것을 확인했습니다. 존재하지 않는 추정 URL을 만들지 않고 현재 접근 가능한 공식 URL을 기록합니다.

## Home Assistant

```yaml
name: Home Assistant Dashboards
official_url: https://www.home-assistant.io/dashboards/
verified_at: 2026-08-14
useful_pattern:
  - 한눈에 보는 작은 상태 Badge
  - 기능과 영역별 독립 Card·View
why_it_fits_v2: 한 Preview의 장애가 다른 프로젝트 상태를 덮지 않는 구조를 표현하기 쉽다.
do_not_copy: 자유 Dashboard 편집·사용자 정의 Card 생태계
applied_area: PM1 프로젝트 상태와 장애 안내
```

## SafetyCulture

```yaml
name: SafetyCulture
official_url: https://safetyculture.com/iauditor
verified_at: 2026-08-14
useful_pattern:
  - 모바일 현장에서 한 단계씩 확인
  - 문제 항목을 바로 후속 Action으로 연결
why_it_fits_v2: 긴 기술정보 없이 현재 확인할 행동에 집중하고 문제 판정을 수정 요청으로 연결할 수 있다.
do_not_copy: 검사표 제작·조직·담당자·보고서 관리 시스템
applied_area: PM1 모바일 진행 화면
```

## Shopify POS Smart Grid

```yaml
name: Shopify POS Smart Grid
official_url: https://help.shopify.com/en/manual/sell-in-person/getting-started/smart-grid
verified_at: 2026-08-14
useful_pattern:
  - 현재 필요한 행동을 큰 Tile로 표시
  - 위치·상황별로 필요한 Tile만 구성
why_it_fits_v2: 기능이 늘어나도 Core Shell을 바꾸지 않고 Core가 허용한 Action만 표시할 수 있다.
do_not_copy: 자유 Tile 재배치·POS 상품·결제 구조
applied_area: PM1 프로젝트별 allowed_actions
```

## 클릭형 Preview 적용 방향

### A — Preview 중심 작업실

Figma의 집중 Preview, ChatGPT Canvas의 요청·결과 분리, SafetyCulture의 단순 판정 흐름을 조합합니다.

```text
프로젝트 선택
→ Preview 크게 표시
→ 요청 영역 필요할 때 펼침
→ Preview 근처에서 통과 / 수정 요청 / 중단
```

### B — 프로젝트·다음 행동 중심

Linear의 프로젝트 상태, Home Assistant의 독립 상태 Card, Shopify POS의 허용 Action Tile을 조합합니다.

```text
프로젝트 홈
→ 현재 상태와 다음 행동 확인
→ 작업실 진입
→ Preview 확인
→ 통과 / 수정 요청 / 중단
```

공식 기본 조합은 `B의 프로젝트 홈 + A의 Preview 작업실`이며, 실제 화면 형태는 클릭형 Preview A/B를 확인한 사용자의 선택으로 확정합니다.
