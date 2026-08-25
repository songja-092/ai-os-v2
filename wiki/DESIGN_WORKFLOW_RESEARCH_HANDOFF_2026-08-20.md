# AI OS V2 — 디자인 탐색·채택 고도화 조사 지시서

아래 내용을 새 GPT 조사 세션에 그대로 전달합니다.

## 목적

AI OS V2의 디자인 탐색·채택 방식이 단순히 업계 표준을 흉내 내는 수준인지, 초보자가 더 적은 비용과 수정 횟수로 전문 디자인 결과를 얻도록 업계 표준보다 개선할 여지가 있는지 검증해 주세요.

기억이나 이전 대화가 아니라 다음 최신 문서를 우선합니다.

- `wiki/SESSION_START_CONTRACT.md`
- `wiki/CURRENT_STATE.md`
- `wiki/DESIGN_SYSTEM.md`
- `wiki/DESIGN_ADOPTION_METHOD_REVIEW_2026-08-20.md`
- `wiki/PM3_PARTIAL_EDIT_FINAL_FLOW_2026-08-20.md`
- `wiki/DESIGN_SUPPLIER_TRIAL_SYNC_2026-08-20.md`
- `plugins/v2-capability-lab/skills/v2-design-director/SKILL.md`
- `plugins/v2-capability-lab/skills/v2-design-director/references/workflow-evidence.md`

## 사실 경계

- V2는 `UI Remix`를 설치하거나 Runtime에서 사용하지 않습니다.
- UI Remix는 실제 UI 사례 검색과 전체·Component 선택 방식의 연구 근거입니다.
- Misty도 설치된 도구가 아니라 Screenshot 구역·속성 선택과 Semantic Diff의 연구 근거입니다.
- 디자인 공급원 10개 시각 시험과 사용자 채택·보류 기록은 존재합니다.
- 채택 공급원 5개를 Draft Design Recipe와 HTML 5개 Section에 연결한 추적 검증은 PASS했습니다.
- 이는 실제 제품 구현·Fidelity·사용자 최종 승인·Version Restore PASS가 아닙니다.
- PM1·PM2는 잠겼고 현재 활성 단계는 PM3입니다.
- Core MVP M1~M7과 기존 Run 증거를 수정하거나 새 PM 번호로 무효화하지 않습니다.

## 현재 권장 흐름

```text
사용자 요청
→ 디자인 총괄이 목적·정보 우선순위·금지 요소 정리
→ 기존 성공 Recipe 우선 확인, 부족할 때만 Reference·공급원 조사
→ 구조적으로 다른 방향 2~3개와 전체·부분 선택
→ 선택·제외·출처를 Draft Design Recipe로 기록
→ 실제 데이터 Visual Target 하나 제작
→ 사용자 방향 승인과 Recipe 승격
→ 승인 Recipe·Component·Asset 구현 지시
→ 실제 구현
→ 독립 Fidelity·기능·회귀 검증
→ 사용자 최종 승인
→ 새 Version 저장·Restore 검증
```

중요: 기존 문장의 `사용자 승인 → Design Recipe 작성`은 부정확합니다. Recipe는 Reference 선택 때 Draft로 시작하고 Visual Target 승인 때 승격해야 합니다.

## 조사 질문

1. Double Diamond, IBM Enterprise Design Thinking, IDEO, Design Sprint, Shape Up, Lean UX, Dual Track, Continuous Discovery 중 V2에 실제로 필요한 부분은 무엇입니까?
2. 초보자 한 명이 디자인 총괄·Reference 선택·실제 Preview 판정을 수행할 때 수정 횟수와 선택 피로를 줄인 검증 사례가 있습니까?
3. `방향 2~3개 → 실제 Code Preview 하나`가 비용과 품질 측면에서 타당합니까? 더 검증된 대안이 있습니까?
4. Reference 검색·부분 선택·Recipe 보존·실제 구현·Fidelity 검사를 한 흐름으로 연결한 제품·오픈소스·연구 사례가 있습니까?
5. 디자인 총괄의 결정 품질을 높이는 검증된 Critique·Playback·Design Review 구조는 무엇입니까?
6. 디자인 다양성, 고유성, 사용성, 구현 가능성을 동시에 평가하는 최소 Scorecard는 무엇입니까?
7. AI 생성 디자인의 `평균적·AI 같은 느낌`, Reference 고착, 브랜드 복제, 과도한 Motion을 막는 검증 방법은 무엇입니까?
8. V2가 업계 표준보다 잘하려면 어떤 단계가 자동화되어야 하고, 어떤 결정은 반드시 사용자에게 남겨야 합니까?
9. PM3 부분수정에서 Puck·React Grid Layout보다 더 검증된 조합이 있는지, 현재 조합을 유지한다면 어떤 Adapter 경계가 필요합니까?
10. 실제 흐름 검증을 위해 다음 프로젝트 하나에서 어떤 Artifact와 지표를 수집해야 합니까?

## 조사 원칙

- 공식 문서, 원 논문, 유지관리 중인 공식 GitHub 저장소, 공개된 실제 산업 사례를 우선합니다.
- 인기·Star·마케팅 문구를 성공 증거로 취급하지 않습니다.
- Reddit은 반복되는 실무 문제와 실패 사례를 찾는 보조 근거로만 사용합니다.
- 유료 API나 복잡한 외부 연결을 기본 해법으로 제안하지 않습니다.
- 도구를 더 추가하기 전에 현재 `V2 Design Director`, UI UX Pro, Puck·React Grid Layout과 중복을 확인합니다.
- 설치·코드·문서·Run·Commit·Push는 하지 않습니다.
- “가능하다”와 “현재 구현됐다”를 구분합니다.

## 반드시 비교할 방법

| 방식 | 기능 | 검증 근거 | 장점 | 단점 | V2 적용 위치 | 자동화 가능 | 사용자 결정 필요 | 제거 가능성 |
|---|---|---|---|---|---|---|---|---|

최소 비교 대상:

- 현재 V2 Design Director 흐름
- Double Diamond 기반 흐름
- Design Sprint 기반 흐름
- Continuous Discovery·Playback 기반 흐름
- UI Remix 원칙의 선택형 흐름
- Misty 원칙의 부분 적용 흐름
- 검증된 Component·Design System 중심 흐름

## 최종 보고 형식

```yaml
current_flow:
  industry_alignment:
  proven_stages: []
  missing_evidence: []

ui_remix:
  installed_or_used: false
  principle_reused:
  appropriate_optional_role:

better_than_standard:
  feasible: true | false | conditional
  required_changes: []
  avoid: []

workflow_evidence_audit:
  first_missing_stage:
  verdict: PASS | PASS_WITH_FIX | BLOCKED | FAIL

skill_review:
  keep: []
  sharpen: []
  remove_or_merge: []
  new_skill_required: true | false

recommended_flow: []
measurement_plan: []
verdict: PASS | PASS_WITH_FIX | BLOCKED
next_single_action:
```

## 원하는 결론 수준

도구 목록을 늘리는 답이 아니라, 다음 실제 프로젝트에서 `요청 → 방향 → Reference → Recipe → Visual Target → 구현 → 검증 → 승인 → 복구`가 끊김 없이 이어졌는지 증명할 수 있는 최소 실행안을 제시해 주세요.
