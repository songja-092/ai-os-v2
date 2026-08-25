# V2 디자인 Skill 다양성 조사·격리 시험 보고서

작성일: 2026-08-18

## 결론

현재 `v2-design-finish`는 한 화면을 끝까지 마감하는 흐름에는 유효하지만, 서로 다른
디자인 세계를 의도적으로 만드는 계약이 부족했다. Design DNA 7축과 다양성 Gate를
추가해 색상만 다른 시안을 새로운 방향으로 인정하지 않도록 보완했다.

Skill만으로 디자인회사의 모든 역할을 대신할 수는 없다. Skill은 작업 순서와 검사
기준을 반복 가능하게 만들지만, 좋은 Reference, 실제 제품 데이터, 사용성 검증,
라이선스, 브라우저 동작, 최종 사용자 만족을 스스로 보증하지 못한다.

## 현재 Skill에서 부족했던 부분

- 구성·밀도·Typography·표면·색·이미지·Motion을 분리한 다양성 축
- 대안이 실제로 구조적으로 다른지 확인하는 Gate
- 구조·시각·상호작용 Reference의 역할 분리
- 이미지 생성을 반복하지 않는 저비용 비교 절차
- 두 번째 독립 마감 검사기

## 격리 시험

### Impeccable 4.1.1

- 공식 저장소: https://github.com/pbakaus/impeccable
- License: Apache-2.0
- 전역 설치 없이 `/tmp`에 격리 설치
- 기존 `pm1-finish-test.html` 정적 검사
- 발견: `flat-type-hierarchy`, `dark-glow`
- 판정: 선택 실행하는 두 번째 마감 검토기로 채택

선택 이유는 디자인 다양성을 자동 생성해서가 아니다. 기존 마감 결과에서 실제로
추가 결함을 찾았고, `critique`, `polish`, `typeset`, `layout`, `animate`처럼 역할이
분리돼 있기 때문이다. Parser Dependency를 설치하지 않은 축소 검사였으므로 누락이
있을 수 있으며, PASS 증거로 단독 사용하지 않는다.

### SkillUI 1.3.4

- 공식 저장소: https://github.com/amaancoderx/npxskillui
- License: MIT
- 소스 정적 감사만 수행, 설치·실행하지 않음
- URL Mode가 Screenshot을 위해 대상 URL을 `api.microlink.io`로 전달
- 생성 Skill을 `~/.claude/skills`에 자동 복사
- 판정: V2 기본 도구로는 폐기, 공개 URL 전용 격리 시험 후보로 보존

좋아하는 사이트의 규칙 추출이라는 역할은 유용하다. 이후 정책을 “완전 로컬”에서
“비공개 프로젝트·Secret 유출 방지”로 구체화했다. 공개 URL은 Capability Lab의 격리
환경에서 조건부 시험할 수 있지만, 원본 프로젝트를 입력하거나 생성 Skill을 전역으로
자동 승격하는 사용은 계속 금지한다.

### Anthropic frontend-design

명확한 미적 방향과 비정형 결과를 유도하는 공개 Skill이다. 그러나 Impeccable이 이
접근을 기반으로 더 세분화된 검사와 명령을 제공하므로 별도 설치하지 않았다.

## 역할별 최종 구조

- `v2-design-finish`: 전체 흐름, 승인, 증거, Design DNA
- `UI UX Pro`: 사용성·접근성·기본 디자인 규칙
- `Impeccable`: 필요할 때만 두 번째 마감·안티패턴 검사
- `Product Design`: Visual Target과 시각 감사
- `shadcn/OSS`: 검증된 구현 부품
- Browser·Playwright: 실제 렌더링과 상호작용 증거
- 사용자: 최종 시각 선택과 채택·폐기 결정

## Skill로 불가능한 한계

- 취향과 품질을 객관적으로 100% 보증
- Reference의 저작권·상표 사용 권리 자동 확정
- 실제 사용자가 업무를 더 잘 완료하는지 증명
- 동적 사이트·Canvas·영상·3D의 완전한 구조 추출
- 하나의 규칙으로 모든 업종에서 독창성 보장
- 실제 Component·상태·데이터가 없는 디자인의 구현 가능성 보증

따라서 V2는 Skill을 교체 가능한 Reviewer·Extractor·Builder로 사용하고, Core는 승인된
Recipe와 증거만 소유해야 한다.

## 판정

```yaml
current_skill: PASS_WITH_FIX
design_diversity_contract: added
impeccable: adopted_optional_not_global
skillui: conditional_public_only_trial_candidate
global_installation: false
core_or_product_change: false
commit_or_push: false
next_gate: user_approves_one_live_trial_with_impeccable_findings_applied
```
