# AI OS V2 — 디자인 공급원 시험·자동화 동기화 보고

- 날짜: 2026-08-20
- 작업공간: `/home/user/바탕화면/ai_os_v2_pm3`
- 범위: 회의 결정 동기화, Reference 추적 자동화, 최소 통합검증

## 1. 사용자 판정

| 번호 | 후보 | 판정 | 기록된 사용자 의견 |
|---|---|---|---|
| 1 | Design Director Control | 비교 제외 | 고객 웹 시험 Surface와 달라 선호 비교에서 제외 |
| 2 | 한국 공개 웹 Reference | 채택 | 국내 감각 공급원으로 보존 |
| 3 | Figma Official | 채택 | 1~3번 중 가장 깔끔함 |
| 4 | 21st.dev | 채택 | 3번과 다른 느낌이어서 비교가 쉬움 |
| 5 | Design MCP | 채택 | 시험 중 가장 선호함 |
| 6 | Framesmith | 보류 | 나쁘지 않지만 확정하지 않음 |
| 7 | UI UX Pro MCP | 조건부 채택 | 두 번째로 선호, 이미지 비중 조정 필요 |
| 8 | awesome-design-md + Framesmith | 보류 | 낫배드 수준 |
| 9 | Creative Tim UI | 채택 | 편집형 정보 구조 공급원으로 보존 |
| 10 | Aceternity UI + React Bits | 채택 | Motion·표현 공급원으로 보존 |

Mobbin은 실제 연결·시험 증거가 없고 유료 접근 가능성이 있어 `optional_paid_hold`입니다. Figma 최초 연결 시험은 계정·Library 검색 확인일 뿐 위 3번 Visual 시험과 구분합니다.

## 2. 확정된 운영 방식

- 공급원 하나만 우승자로 정하지 않습니다.
- 프로젝트마다 역할이 다른 공급원을 2~4개 추천할 수 있습니다.
- 방향 3개는 완성 코드 3개가 아니라 빠른 비교용 시안입니다.
- 실제 Code Preview는 선택된 조합 하나만 만듭니다.
- 사용자는 전체 방향 또는 일부 Section을 선택할 수 있습니다.
- 디자인 총괄이 색상·글꼴·간격·Component·Motion을 하나의 시스템으로 통일합니다.
- 링크·Screenshot이 추가되면 수집→분석→시각 확인→채택·보류·폐기 순서로 처리하고 채택 자료만 공급원에 남깁니다.
- 기존 성공 Recipe·Block으로 충분하면 수집기를 실행하지 않습니다.

권장 역할 조합:

- `Design MCP`: 방향 탐색
- `21st.dev`: 구현 가능한 Component·Block 후보
- `UI UX Pro MCP`: 규칙·품질 검사
- `Creative Tim UI`: 편집형 정보 구조
- `Aceternity UI + React Bits`: Motion·표현

## 3. 자동화한 부분

`V2 Design Director`에 `reference_flow.py`를 추가했습니다.

자동 처리:

1. 선택된 후보의 실제 Trial 기록을 읽습니다.
2. 사용자 채택 상태가 아니면 중단합니다.
3. 공급원 역할과 적용 Section을 Draft Design Recipe로 만듭니다.
4. Trial과 Preview의 SHA-256을 고정합니다.
5. 실제 HTML의 `data-v2-section`과 `data-v2-sources`를 대조합니다.
6. Preview가 변경되면 이전 검증 결과를 재사용하지 못하게 합니다.

자동화하지 않는 것:

- 사용자 대신 채택·보류·폐기 결정
- 디자인 품질 PASS
- Core 자동 적용
- 제품 코드 변경
- Commit·Push

## 4. 통합검증 결과

Pilot: `pm3-artifacts/reference-adoption-pilot-v1/`

```yaml
reference_to_recipe: PASS
recipe_to_visible_sections: PASS
verified_sources: 5
verified_sections: 5
preview_hash_locked: PASS
skill_structure_validation: PASS
visual_diversity: user_confirmed_improved
```

실제 연결:

- Hero: Design MCP + Creative Tim + Aceternity/React Bits
- Navigation: Creative Tim + UI UX Pro
- Community Feed: 21st.dev + Creative Tim + UI UX Pro
- Live Topics: Aceternity/React Bits
- Questions: Creative Tim + Aceternity/React Bits

## 5. 아직 미검증

```yaml
core_automatic_source_selection: not_implemented_by_design
core_product_application: not_proven
pm2_locked_product_direction_preservation: not_retested
pm3_editor_direction_preservation: not_proven
cross_project_recipe_reuse: not_proven
visual_quality_of_combined_recipe: requires_user_review
```

이번 PASS는 **채택 Reference가 Recipe와 실제 화면 Section까지 추적되는 것**을 증명합니다. V2 Core가 자동으로 최고의 디자인을 선택하거나 제품에 적용했다는 뜻이 아닙니다.

## 6. 다음 Gate

현재 PM3의 다음 최소 검증은 이 Draft Recipe를 Puck·React Grid Layout 편집기에 읽기 전용으로 불러와, 카드 순서·크기·색상 변경 후에도 다섯 공급원의 Section 연결이 보존되는지 확인하는 것입니다. 실제 제품 적용과 PM2 잠금 변경은 하지 않습니다.
