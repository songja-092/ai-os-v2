# AI OS V2 엔지니어링 방법 비교 조사 — 2026-08-21

## 조사 목적

현재 V2 구조를 정당화하는 것이 아니라, 초보자가 AI로 상업적 결과물을 반복 제작할 때 품질·속도·안전·복구를 함께 높이는 지속 가능한 방법을 찾습니다.

## 비교한 방법

| 방법 | 쉬운 뜻 | 강점 | 단독 사용의 약점 | V2 판정 |
|---|---|---|---|---|
| Harness Engineering | AI가 일할 환경·규칙·도구·검사를 설계 | 긴 작업, 여러 AI, 증거·복구 관리에 강함 | 너무 크게 만들면 느리고 비쌈 | 상위 기본 구조 |
| Spec-driven Development | 만들 것을 먼저 합의하고 단계별 문서로 전달 | 요구 누락·세션 간 Drift 감소 | 문서가 과하면 사용자가 지치고 기존 Wiki와 중복 | 인터뷰·제작 범위 확인서로 필요한 부분만 사용 |
| Eval-driven Development | 결과를 점수·테스트·기준 화면으로 비교 | 좋아졌는지 객관적으로 판단 | 평가 기준이 나쁘면 잘못된 방향을 자동 강화 | 모든 자동화의 승격 조건 |
| Human-in-the-loop | 중요한 결정을 사람이 승인 | 취향·비용·보안·공개 결정에 안전 | 모든 단계에 승인을 넣으면 병목 | 채택·적용·배포·최종 승인에만 유지 |
| Agent-first | AI가 대부분 실행하고 사람은 방향을 관리 | 높은 처리량 | 환경·테스트·문서가 약하면 빠르게 혼란이 커짐 | 하네스 안의 실행 방식 |
| Loop Engineering | 실행→관찰→수정→재검사를 자동 반복 | 반복 수정 비용 감소 | 중단 조건이 없으면 Token·시간 낭비와 오류 반복 | 판정·복구 가능한 작업만 제한 적용 |

## 조사 근거 요약

### 공식·산업 근거

- OpenAI의 Harness Engineering 사례는 Repo-local 문서, 짧은 진입점, 구조 검사, 테스트, 반복 정리 작업을 결합했고 실제 내부 사용 제품을 소수 인원이 빠르게 제작했다고 보고합니다. 동시에 이 결과가 같은 투자 없이 일반화된다고 가정하면 안 된다고 명시합니다.
- Anthropic은 Planner·Generator·Evaluator와 구조화 Artifact가 긴 작업과 Frontend 품질을 높였다고 보고하지만, Harness가 크고 느리며 비싸질 수 있고 모델이 발전하면 불필요한 요소를 제거해야 한다고 설명합니다.
- GitHub Spec Kit는 `Spec → Plan → Tasks → Implement`를 제공하고 Codex를 포함한 여러 Agent와 Offline 환경을 지원합니다. 그러나 V2에는 인터뷰, 제작 범위 확인서, PM 문서, 계약, Artifact가 이미 있어 전체 설치는 중복 여부를 먼저 검사해야 합니다.
- OpenAI와 Anthropic의 공통점은 처음부터 복잡한 다중 Agent를 쓰는 것이 아니라 가장 단순한 구조에서 시작하고, 실제 실패가 반복될 때 도구·검사·자동화를 추가하는 것입니다.

### GitHub 후보에서 확인한 공통 패턴

- 명세와 완료 기준을 구현 전에 고정합니다.
- Agent 행동과 최종 결과를 함께 추적합니다.
- Golden Case·Baseline·회귀 차이로 개선을 판정합니다.
- Tool Call과 Output을 Schema로 제한합니다.
- 자동화 실패 시 사람이 확인할 수 있는 Trace를 남깁니다.

GitHub Star, 자체 Benchmark, README의 성능 주장은 참고 자료이며 V2 채택 증거가 아닙니다.

### Reddit·YouTube에서 확인한 실패·성공 패턴

- 명확한 범위, 작은 작업, 구현 전 계획, 다른 검사 주체가 있을 때 결과가 안정적이라는 경험이 반복됩니다.
- 테스트·E2E·사람 검토 없이 완전 자동화하면 빠르게 많은 코드를 만들지만 충돌·회귀·디버깅 비용이 커진다는 사례가 있습니다.
- Spec 도구는 계획을 돕지만 문서 작성 자체가 작업이 될 수 있으며, 리뷰·배포·운영 검증을 자동으로 해결하지는 않습니다.
- Community 사례는 통제 실험이 아니므로 방향을 찾는 보조 증거로만 사용합니다.

## V2에 맞는 결론

새로운 단일 방법론을 도입하지 않습니다. 다음 조합을 공식 운영 구조로 사용합니다.

```text
Harness
├─ Interview·제작 범위 확인서: 필요한 만큼의 Spec
├─ PM·Design Recipe·Module Manifest: 실행 계약
├─ Codex·Antigravity·Skill·MCP: 교체 가능한 실행 수단
├─ Build·Browser·Fidelity·접근성·Restore: Eval
├─ 채택·적용·배포·최종 승인: Human-in-the-loop
└─ 반복·판정·복구 가능한 병목: Bounded Loop
```

즉, `Harness-first, Spec-guided, Eval-driven, Human-approved, Loop-assisted`가 V2의 자세한 운영 표현입니다.

## 설치 판정

### 지금 설치하지 않음

- GitHub Spec Kit: 기능과 유지관리 근거는 충분하지만 V2의 인터뷰·PM·계약 문서와 중복 가능성이 큽니다.
- 별도 Agent Harness 제품: Codex·Antigravity·V2 Core 위에 또 다른 제어 계층을 얹으면 상태 원본이 나뉠 수 있습니다.
- 자동 Harness 개선 도구: Baseline과 Golden Case가 없는 상태에서 Prompt·규칙을 자동 수정하면 개선 여부를 판정할 수 없습니다.

### 필요한 부분만 흡수

- Spec Kit의 단계별 Artifact 연결
- Harness 사례의 짧은 진입점과 Progressive Disclosure
- Eval Harness의 Golden Case·Baseline Diff·Trace
- Anthropic 사례의 독립 Evaluator와 불필요한 Harness 제거 원칙

## 첫 자동화 Loop 후보

첫 Loop는 디자인 생성이나 코드 자동 수정이 아니라 **PM 전환 증거 검사기**로 제한하는 것이 안전합니다.

입력:

- 현재 PM
- 잠금 Commit·Tag
- 사용자 PASS 기록
- 필수 Artifact·검사 결과
- Session Contract·Current State 링크
- Git 상태

출력:

- 완료됨
- 누락됨
- 서로 충돌함
- 사용자 확인 필요

이 Loop는 파일을 자동 수정하거나 PM을 자동 PASS하지 않습니다. 보고서만 만들고 사용자가 승인하면 문서·Commit·Push 단계로 이동합니다.

```yaml
pm_transition_evidence_loop:
  state: stable_default
  mode: read_only
  max_attempts: 1
  pass_condition: required_evidence_present_and_consistent
  stop_condition: missing_or_conflicting_evidence
  rollback_method: not_required_no_mutation
  human_escalation: always_before_pm_pass_or_lock
```

## 다음 검증 순서

1. PM1·PM2의 완료 증거를 Fixture로 사용해 검사 항목을 정의합니다.
2. 정상 Fixture 1개와 누락·충돌 Fixture 2개를 만듭니다.
3. 읽기 전용 검사기가 정상·누락·충돌을 정확히 구분하는지 확인합니다.
4. 현재 PM3에는 판정만 실행하고 자동 수정하지 않습니다.
5. 사용자 판정 후 채택·보류·폐기합니다.

2026-08-21 격리 검증에서 정상 Fixture는 `PASS`, 필수 파일 누락 Fixture와 Hash 충돌 Fixture는 각각 `BLOCKED`로 구분했습니다. 기존 `verify-pm-locks`와 `verify-ai-evidence-guard`도 함께 PASS했습니다. 같은 날 사용자가 기존 기본 자동화가 없음을 조건으로 채택했으며, 확인 결과 같은 역할의 기존 자동화가 없어 `stable_default`로 승격했습니다. PM 자동 PASS·파일 자동 수정은 계속 금지하며 다른 PM Manifest는 해당 PM 완료 때 별도 검증합니다.

## 현재 판정

```yaml
initial_comparative_research: completed
recommended_operating_model: harness_first_spec_guided_eval_driven_human_approved_loop_assisted
new_framework_installation: not_required_now
spec_kit: watchlist_due_to_contract_overlap
first_bounded_loop: pm_transition_evidence_checker
first_loop_implementation: isolated_fixture_verified
first_loop_user_adoption: adopted
first_loop_status: stable_default
industry_best_absolute_claim: not_proven
```
