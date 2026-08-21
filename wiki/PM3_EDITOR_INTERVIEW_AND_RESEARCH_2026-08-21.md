# PM3 편집기 인터뷰·후보 조사 — 2026-08-21

## 확정된 사용자 계약

PM3은 고객 결과물의 부분 수정 기능이 실제로 작동하는지 확인합니다. PM3에서 작동한
기능은 PM6에서 실제 고객 결과물·모바일 390/430·되돌리기·원본 보존·프로젝트 격리·
접근성·회귀를 다시 검증합니다. PM3 PASS가 PM6 PASS를 대신하지 않습니다.

- 글자: 화면에서 바로 수정과 오른쪽 설정창 수정 모두 제공
- 순서: 기본 화면에서는 마우스로 직접 끌어서 변경
- 크기: 테두리·모서리를 직접 끌며, 사용 불가능한 극단값만 차단하고 나머지는 경고
- 이미지: 교체와 크기만 제공
- 스타일: 선택한 Section 전체에 공통 적용
- 자동 정리: 선택한 Section의 Draft만 제안하며 적용 전 비교·취소
- 반응형: 문구·색상·이미지는 공통, 배치·순서·크기·여백·줄바꿈은 PC·모바일 분리
- 되돌리기: 한 단계씩 `이전으로`, 전체 Draft는 `수정 전체 버리기`
- 대상: 고객 결과물만 편집하며 V2 운영 UI는 제외
- 도구 선택: 안정성과 자유도의 균형을 우선

원본 계약은 `pm3-artifacts/editor-interview-v1/interview-receipt.json`이며,
`tools/verify-pm3-editor-interview`는 인터뷰 완결성만 검사합니다. 이 검사는 구현이나
PM3 PASS를 승인하지 않습니다.

## 1차 공식 자료 조사

| 후보 | 쉬운 역할 | 강점 | V2 주의점 | 현재 판정 |
| --- | --- | --- | --- | --- |
| Puck | React 결과물을 조립·편집 | MIT, React Component, Drag & Drop, 자체 데이터 소유, 최근 Inline Rich Text 지원 | 정밀 자유 Resize와 Viewport Recipe Adapter는 V2가 연결해야 함 | 우선 후보 |
| GrapesJS | 웹페이지를 자유롭게 편집 | BSD-3-Clause, Rich Text·Style·Device·Undo·Asset·Layer가 오래 검증됨 | HTML/CSS 모델이 V2 React Module·Design Recipe와 달라 변환·격리가 큼 | 자유도 비교 후보 |
| Craft.js | 원하는 편집기를 직접 조립 | MIT, React, Drag & Drop, Resize·Inline Text를 직접 구성 가능 | 완제품이 아니어서 자체 편집기 제작 병목을 반복할 수 있음 | 보류 |
| Penpot MCP | 전문 디자인 파일을 정밀 편집 | 오픈소스·Self-host, Token·Component·Grid/Flex, 공식 MCP | V2 안의 간단 편집기가 아니라 별도 전문 디자인 작업실에 가까움 | PM3 기본 편집기와 분리 검토 |

Star는 인기도 참고일 뿐 V2 적합성 증거로 단독 사용하지 않습니다.

공식 확인 자료:

- Puck: https://github.com/puckeditor/puck
- Puck Release·Inline Rich Text: https://github.com/puckeditor/puck/releases
- GrapesJS Core: https://github.com/GrapesJS/grapesjs
- GrapesJS API: https://grapesjs.com/docs/api/
- Craft.js: https://github.com/prevwong/craft.js
- Penpot: https://github.com/penpot/penpot
- Penpot MCP: https://github.com/penpot/penpot/blob/develop/mcp/README.md

## 다음 Gate

현재 병원 웹 편집 Draft는 `frozen_pending_editor_selection`입니다. 다음 두 방향을 실제
격리 비교로 보여주기 전 새로운 편집기 구현·설치·제품 Commit을 하지 않습니다.

1. Puck 중심: 현재 React·Recipe 구조를 유지하며 자유 Resize·Inline Text를 보완
2. GrapesJS 중심: 더 자유로운 편집을 확인하되 Recipe 변환과 React 격리 비용도 측정

Penpot은 위 두 방식과 같은 Runtime 편집기 후보로 섞지 않습니다.
