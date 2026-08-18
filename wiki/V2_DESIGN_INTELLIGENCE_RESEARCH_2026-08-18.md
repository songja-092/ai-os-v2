# V2 Design Intelligence 조사·환경 구성 보고서

작성일: 2026-08-18
상태: Repo-local 자동 수집 Pilot 구현, 후보 사용자 판정 대기

## 이름 정리

- `v2-design-finish`: 하나의 Visual Target을 전문적으로 마감하는 Skill
- `디자인 시스템`: 채택된 Typography·Color·Spacing·Component·Motion 규칙
- `디자인 자료실`: 사용자가 보는 Reference·Block·성공/실패 사례
- `Design Intelligence`: 자료 수집·분석·최신성 확인·추천·채택/보류/폐기·재사용 전체
- `Design Freshness`: Design Intelligence 안의 최신성 검사

따라서 현재 업그레이드한 기능의 공식 내부 이름은 `Design Intelligence`가 적절합니다.

## 조사 결론

### 바로 사용하는 기반

1. shadcn Registry
   - 공식 Registry API와 Schema 제공
   - `view`, `dry-run`, `diff`, Registry 검증과 Git Commit 고정 가능
   - Design Intelligence의 실제 구현 Block Source로 사용
2. GitHub 공개 Metadata
   - Star는 보조 정보로만 사용
   - License, Archive 상태, 마지막 Push, 기본 Branch와 URL 기록
3. V2 Capability Lab
   - 공개 후보의 Source를 고정하고 가짜 Fixture로 격리 시험
   - 비공개 프로젝트와 Secret을 후보에 제공하지 않음

### 현재 도입하지 않는 대형 Crawler

- Firecrawl: Search·Scrape에는 강하지만 AGPL 서버 또는 외부 Cloud 운영이 필요해 현재
  후보 3~8개 수집 목적에는 과합니다.
- Crawl4AI: 동적 Web 수집에 유용하지만 Browser·Python 환경과 유지비가 추가됩니다.

Design Intelligence가 실제 페이지 내용 추출에서 반복 실패할 때만 Capability Lab에서
하나를 시험합니다.

## 자동 수집 결과

2026-08-18 공개 GitHub Metadata 기준으로 다음 8개가 Review Queue에 들어갔습니다.

| 후보 | 역할 | 1차 판정 |
|---|---|---|
| shadcn/ui | 검증된 Component·Block Registry | 채택 추천 |
| Kokonut UI | Motion 기반 shadcn 시각 Block | 보류 추천 — PM2 Stack 뒤 시험 |
| Impeccable | 마감·안티패턴 2차 검사 | 격리 시험 PASS, 채택 추천 |
| Taste Skill v1 | 디자인 다양성 Dial·안티슬롭 | 보류 추천 |
| Stitch Skills | 외부 Stitch Workflow | 보류 추천 |
| Motion | React Motion 엔진 | 보류 추천 — PM2 뒤 |
| AutoAnimate | Card 추가·삭제·이동 Animation | 보류 추천 — PM3 뒤 |
| Storybook | Component 상태 전시장·검증 | 보류 추천 — Module 생성 뒤 |

Taste Skill v1은 `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY` 세 축이 있지만
기본값이 강하고 무한 Animation·Bento Pattern을 과도하게 권장하는 부분이 V2 운영 UI와
충돌합니다. 현재 `v2-design-finish`의 7개 Design DNA 축이 더 세밀하므로 전체 Skill
채택보다 필요한 Dial 개념만 참고하는 것이 안전합니다.

## 사용자 흐름

```text
Design Intelligence가 공개 후보 수집
→ V2가 License·최신성·역할 확인
→ 사용자에게 링크와 쉬운 설명 표시
→ [채택] [보류] [폐기]

[채택]
→ Capability Lab 가짜 Fixture 시험
→ 실제 결과 표시
→ 다시 [채택]하면 비활성 Adapter 등록

[보류]
→ 다음 PM 또는 조건이 맞을 때 다시 표시

[폐기]
→ 활성 후보에서 제외하고 이유 보존
```

사용자는 폴더, Clone, SHA, Sandbox 명령과 Registry 위치를 관리하지 않습니다.

## 검증 상태

```yaml
design_intelligence_collector: implemented_repo_local_pilot
candidate_metadata_count: 8
private_project_input: prohibited
public_network: allowed_when_declared
automatic_global_install: false
automatic_core_adoption: false
impeccable: isolated_trial_pass
taste_skill_v1: isolated_structure_trial_pass_with_fit_concerns
pm4_complete: false
core_or_product_change: false
```
