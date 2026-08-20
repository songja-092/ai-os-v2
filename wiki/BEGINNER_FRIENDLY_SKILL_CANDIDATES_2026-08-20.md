# 초보자 친화 Skill 후보 조사 — 2026-08-20

## 기준

초보자에게 전문용어를 더 보여주는 Skill이 아니라, 잘못 만들기·무작위 수정·근거 없는 구현·복구 불가를 줄이는 Skill만 후보로 남깁니다. 현재 V2 Skill·Core·PM과 중복되면 새로 설치하지 않습니다.

## 우선순위

### 1. Source-driven Development — 다음 격리 시험 추천

- 쉬운 역할: Library·Framework 사용법을 기억으로 추측하지 않고 공식 문서에서 확인합니다.
- 초보자 가치: “된다고 했는데 실제 버전에서는 안 됨”을 줄입니다.
- V2 위치: 조사 결과를 구현 Brief에 넣는 내부 검증 Skill.
- 중복: V2의 환각 방지 공통규칙과 일부 중복하지만, 공식 출처→구현 결정 연결 절차는 더 구체적입니다.
- 판정: `trial_recommended`.

### 2. Debugging and Error Recovery — 조건부 시험 추천

- 쉬운 역할: 오류가 날 때 아무 곳이나 고치지 않고 증거 보존→재현→원인 확인→최소 수정으로 진행합니다.
- 초보자 가치: 사용자가 같은 화면 수정을 반복 요청하는 일을 줄일 가능성이 있습니다.
- V2 위치: `문제 있어요` 행동과 PM6 회귀·복구 내부 Workflow.
- 중복: Browser 검증·Playwright·기존 회귀 규칙과 겹칩니다. UI보다 원인 진단 절차만 비교해야 합니다.
- 판정: `trial_after_source_driven`.

### 3. Idea Refine — 보류

- 쉬운 역할: 막연한 아이디어를 여러 방향으로 넓힌 뒤 하나로 좁힙니다.
- 장점: 사용자가 해결 방법을 아직 모를 때 유용합니다.
- 위험: Interview Me·디자인 총괄·방향 2~3개 비교와 겹치며 선택 피로를 다시 늘릴 수 있습니다.
- 판정: `hold_optional_user_request_only`.

## 새로 설치하지 않을 후보

- `Planning and Task Breakdown`: PM 계획·Gate·인수인계와 중복
- `Spec-driven Development`: 기존 Spec Kit·PM 문서와 중복
- `Context Engineering`: 세션 공통계약·CURRENT_STATE와 중복
- `Frontend UI Engineering`: V2 Design Finish·UI UX Pro·Frontend App Builder와 중복
- `Browser Testing with DevTools`: 현재 Browser·Playwright 검사와 중복
- `Code Review and Quality`: Codex 독립 검증·PM6 품질 Gate와 중복
- `Code Simplification`: Ponytail과 중복
- `Doubt-driven Development`: 모든 변경에 적용하면 비용·질문량이 커지며 현재 증거 감사와 중복

## 권장 도입 순서

```text
Interview Me 사용자 채택 여부 결정
→ Source-driven Development Skill 하나만 격리 시험
→ 실제 환각·구버전 구현 감소 효과 확인
→ 효과가 있으면 비활성 Adapter로 채택
→ Debugging Skill은 회귀 오류 사례 하나로만 비교
```

Skill 개수를 늘리는 것이 목표가 아닙니다. `요청 명확화`, `공식 출처 확인`, `체계적 오류 복구` 세 병목이 각각 실제로 줄어드는 경우에만 하나씩 채택합니다.
