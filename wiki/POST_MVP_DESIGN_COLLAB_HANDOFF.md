# Post-MVP GPT 공동 설계 전달서

작성일: 2026-08-15  
대상: 사용자와 함께 `AI OS V2`의 Post-MVP 마일스톤을 설계할 GPT  
목적: 기존 문서를 참고하되 `PM1~PM4`를 확정안으로 오해하지 않고, 사용자와 기능·순서·완료 기준을 다시 설계하기 위함

## 1. GPT에게 전달할 핵심 요청

```text
GitHub 저장소 songja-092/ai-os-v2의 main과 아래 공식 문서를 먼저 확인해줘.

- wiki/CURRENT_STATE.md
- wiki/POST_MVP_ROADMAP.md
- wiki/THIN_UI_MVP_CONTRACT.md
- wiki/ui-reference-mix.md
- wiki/ARCHITECTURE.md
- wiki/DECISIONS.md
- wiki/PM1_HANDOFF.md
- wiki/POST_MVP_DESIGN_COLLAB_HANDOFF.md

단, 현재 문서에 적힌 PM1~PM4의 `approved`, `확정`, `active_milestone: PM1` 표현은 최신 사용자 의도가 아니다.
정확한 현재 상태는 다음과 같다.

Core MVP M1~M7: 완료·검증·동결
Post-MVP PM 구성: 검토용 기본틀
PM 개수·순서·기능·PASS 조건: 사용자와 조정 중
구현 상태: 시작 전
현재 작업: PM 전체 구조 공동 설계

나와 함께 PM별 사용자 기능, 제외 범위, 선행조건과 완료 기준을 검토해줘.
한 번에 너무 많은 결정을 요구하지 말고, 영향이 큰 질문부터 하나씩 쉬운 말로 물어봐줘.
내 답을 반영해 수정된 전체 구조를 계속 보여주고, 내가 명시적으로 승인하기 전에는 설계 완료나 PM1 시작을 선언하지 마.
Skill 설치, 패키지 설치, 외부 서비스 연결, 코드 구현, Commit과 Push도 하지 마.
```

## 2. 현재 공식 Git 기준점

```yaml
repository: https://github.com/songja-092/ai-os-v2
official_branch: main
official_commit: da33544fac365e6915aad73ec533124d12309803

core_mvp:
  milestones: M1-M7
  status: completed_and_frozen

post_mvp:
  planning_status: draft_baseline
  scope_status: under_review
  sequence_status: under_review
  implementation_status: not_started

current_work: post_mvp_structure_review
pm1_clickable_preview: blocked_until_plan_approval
```

제품 저장소 `/home/user/바탕화면/test_project`에는 병원 웹, M6 부분 수정과 M7 PDF 제품의 완료 Commit이 존재합니다. V2 저장소와 제품 저장소의 Commit을 하나로 취급하지 않습니다.

## 3. 현재 PM 기본틀

아래 구조는 토론 시작점이며 확정안이 아닙니다. PM 추가·삭제·병합·분리와 순서 변경이 가능합니다.

### PM1 후보 — 얇은 UI

사용자가 프로젝트를 선택하고 현재 요청·상태·Preview를 확인하며 Core가 허용한 행동을 수행하는 최소 화면입니다.

현재 후보 기능:

- 프로젝트 홈과 프로젝트 작업실
- 병원 웹·PDF 도면 기호 등 프로젝트 선택과 전환
- 현재 요청, 진행 상태와 다음 행동
- 실제 Preview 실행·중단·전환
- `통과`, `수정 요청`, `중단`
- 모바일 390px·430px와 PC
- Preview 장애·Port 충돌·초기화 실패 표시 및 격리
- stale·중복·다른 프로젝트 Action 차단
- 최소 오류 보고서
- Result Commit과 Rollback/Restore

논의할 항목:

- 프로젝트 생성·가져오기·검색·보관이 PM1에 필요한가
- 최근 프로젝트, 즐겨찾기와 승인 대기 모음이 필요한가
- 과거 결과·Preview 버전 비교와 알림이 필요한가
- 초보 모드와 상세 모드를 분리할 것인가

### PM2 후보 — 직접 부분 수정

사용자가 Preview의 제한된 영역을 안전한 값으로 직접 조절하고 Quick Change Run으로 적용하는 기능입니다.

현재 후보 기능:

- `HERO-01` 영역 선택
- 글자 크기, 콘텐츠 폭, 줄바꿈과 배경색
- 원본과 분리된 Draft Preview
- `원래대로`, `미리보기`, `적용`
- 허용된 CSS 변수와 제한 값만 사용
- 모바일·PC 회귀검증
- Result Commit과 Rollback/Restore

논의할 항목:

- 글꼴·굵기·행간·여백·모서리·테두리·그림자 추가 여부
- 버튼과 이미지의 제한 편집 허용 여부
- 모바일과 PC 값을 따로 설정할지
- 변경 전후 비교와 버전 복원을 제공할지
- 직접 수정 가능 영역을 어떤 기준으로 확대할지
- AI 보조 수정과 직접 편집의 경계를 어디에 둘지

### PM3 후보 — 조사·자료 수집·병목 진단

새 프로젝트에 필요한 자료를 조사하거나 기존 프로젝트의 가장 큰 병목을 증거 기반으로 찾는 기능입니다.

현재 후보 기능:

- 본문·Markdown·Text·PDF·일반 공개 웹페이지
- GitHub 저장소·README·Issue·Release
- Reddit 게시글·댓글
- 사용자가 제공한 Threads 링크·본문·Screenshot
- 출처 URL·수집 시각·Checksum
- 사실·주장·추정·추천 분리
- 공식 자료 교차검증과 자료 부족 표시
- 새 프로젝트 조사 1건
- 기존 프로젝트 병목 진단 1건
- 가장 영향이 큰 병목 하나와 해결책 최대 2개
- 승인 전 제품 변경 차단

논의할 항목:

- 자료 수집과 병목 진단을 하나의 PM으로 둘지 분리할지
- 시장·경쟁 제품·사용자 리뷰 조사를 포함할지
- 보안·접근성·SEO·성능·의존성·테스트·비용 진단을 포함할지
- 여러 병목의 영향도·긴급도 순위를 제공할지
- 반복 진단과 개선 전후 비교를 지원할지
- 수집 자료의 보존·삭제·개인정보 정책을 어디까지 만들지

### PM4 후보 — AI 의도 정합성

구현 전에 사용자 요청과 구현 AI의 이해가 일치하는지 비교하고, 오해한 상태의 구현 시작을 차단하는 기능입니다.

현재 후보 기능:

- 자연어 요청을 Intent Packet으로 구조화
- 구현 AI의 Intent Receipt
- 핵심 용어와 허용·금지 범위 비교
- 올바른 예·잘못된 예와 시각 Reference
- Acceptance Checks
- 불일치 시 구현 차단
- 정말 모호할 때 질문 하나
- Planner·Implementer·Verifier 역할 계약 경계

현재 제외 후보:

- AI Provider 자동 교체
- AI Marketplace
- 비용 기반 자동 선택과 자동 Fallback
- 사용자의 AI 선택 화면
- Paseo·OpenClaw 연결

논의할 항목:

- 구현 전 사용자 확인을 필수로 할지
- 빠진 조건·과거 결정 충돌·Scope Creep을 차단할지
- 브랜드·보안·개인정보 요구도 비교할지
- 구현 후 결과와 최초 의도의 정합성까지 재검증할지
- 반복된 AI 오해 유형을 프로젝트 기억으로 남길지

## 4. 공동 설계 시 먼저 결정할 질문

GPT는 아래 질문을 한꺼번에 던지지 말고 영향이 큰 것부터 한 번에 하나씩 물어봅니다.

1. 사용자가 Post-MVP 마지막에 실제로 할 수 있어야 하는 핵심 행동은 무엇인가?
2. 현재 PM1~PM4 순서를 유지할 것인가?
3. PM을 추가·삭제·병합·분리해야 하는가?
4. PM1은 단순 조회·승인 UI인가, 프로젝트 생성·가져오기까지 포함하는가?
5. PM2의 직접 편집은 어느 속성과 영역까지 허용하는가?
6. PM3의 자료 수집과 병목 진단을 하나로 유지할 것인가?
7. PM4는 구현 전 차단만 담당하는가, 구현 후 결과 정합성도 검증하는가?
8. 각 PM 완료 시 사용자가 직접 확인할 대표 시나리오는 무엇인가?
9. 각 PM에서 의도적으로 만들지 않을 기능은 무엇인가?
10. 어떤 작업에 사용자 승인·외부 계정·비용·위험 권한이 필요한가?

## 5. 답변마다 유지할 설계표

GPT는 사용자 답변을 받을 때마다 아래 표를 갱신해 전체 구조를 보여줍니다.

| PM | 사용자가 새로 할 수 있는 일 | 필수 기능 | 제외 범위 | 선행조건 | 사용자 확인 시나리오 | PASS 기준 | 상태 |
|---|---|---|---|---|---|---|---|
| PM1 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | draft |
| PM2 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | draft |
| PM3 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | draft |
| PM4 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | 검토 중 | draft |

PM 수가 달라지면 행을 추가·삭제합니다. 기술 도구가 아니라 사용자가 새로 할 수 있는 일을 기준으로 PM을 구분합니다.

## 6. 설계 완료 Gate

다음 조건을 모두 만족하기 전에는 설계 완료로 판정하지 않습니다.

- 사용자가 PM 개수와 순서를 명시적으로 승인함
- 각 PM의 사용자 기능과 제외 범위가 확정됨
- 각 PM의 선행조건과 대표 사용자 시나리오가 확정됨
- 기술 검증과 사용자 확인을 포함한 PASS 조건이 확정됨
- 위험 권한·비용·외부 계정이 필요한 지점이 표시됨
- PM 사이 중복과 누락을 검토함
- 구현하지 않을 후보와 후속 후보가 분리됨
- 사용자가 전체 설계안을 최종 승인함

완료 시 GPT는 다음 문구를 명확히 사용합니다.

```text
Post-MVP 설계 완료
```

사용자 승인 전에는 `확정`, `설계 완료`, `PM1 시작 가능`이라고 표현하지 않습니다.

## 7. 설계 완료 후 환경 조사 단계

설계가 완료되면 바로 구현하지 않고 PM을 원활히 수행할 환경을 조사합니다.

```text
현재 설치 Skill
→ 기존 V2 Core와 제품 코드의 재사용 기능
→ 공식 제품 기능과 공식 문서
→ 유지관리되는 GitHub 오픈소스
→ 최소 직접 구현
```

각 후보에서 확인할 항목:

- 담당할 PM 기능과 실제 필요성
- 기존 기능과 중복 여부
- 최근 Commit·Release와 Issue 대응 상태
- 라이선스와 상업적 사용 조건
- 보안·개인정보·외부 전송 위험
- 설치·계정·API Key·기기·권한 필요 여부
- 기존 V2 단일 Orchestrator와 충돌 여부
- 제거와 Rollback 가능성
- 가장 작은 격리 실험 방법

추가 후보는 역할별 최대 2개로 제한하며, 발견만으로 설치·채택·검증 완료 처리하지 않습니다.

## 8. 사용자 준비사항 보고 형식

환경 조사 후 다음 형식으로 사용자가 준비할 것을 보고합니다.

```yaml
post_mvp_design: completed

environment_readiness:
  existing_tools: []
  reusable_skills: []
  missing_capabilities: []
  recommended_open_source: []
  installation_required: []
  user_preparation_required:
    required_now: []
    required_later_by_pm: []
    optional: []
    requires_security_or_cost_approval: []
    not_needed: []
  risks_and_licenses: []
  validation_plan: []
  ready_to_start: false
```

## 9. 안전 규칙

- 현재 V2 작업 폴더의 Dirty 변경은 사용자 소유이므로 수정·Stage·Commit·삭제하지 않습니다.
- 설계 중에는 Skill·패키지·Plugin을 설치하지 않습니다.
- 외부 계정 연결, API Key 사용, 유료 서비스, 배포와 데이터 전송을 자동 승인하지 않습니다.
- 로그인 우회, 쿠키 재사용과 무단 대량 Scraping을 제안하지 않습니다.
- 조사와 설계 결과를 구현 완료 또는 검증 완료로 기록하지 않습니다.
- 사용자가 최종 승인하기 전 PM1 클릭형 Preview와 실제 제품 구현을 시작하지 않습니다.

## 10. GPT가 시작할 첫 질문

문서와 저장소 상태를 확인한 뒤 현재 PM 기본틀을 짧게 요약하고 다음 질문 하나만 합니다.

```text
Post-MVP가 모두 끝났을 때, 가장 먼저 “반드시 혼자 할 수 있어야 한다”고 생각하는 사용자 행동은 무엇인가요?
```

## 11. 추가 사용자 방향 — 수집·디자인 Reference·UI UX Pro 시각화

아래 내용은 이후 GPT 공동 설계에서 반드시 반영할 최신 사용자 방향입니다. 아직 전체 PM 설계의 최종 승인을 의미하지 않습니다.

### 공통 수집 Source

새 웹·앱 요청을 받으면 현재 V2의 `수집 → 분석 → 추천 → 사용자 승인` 흐름을 확장해 다음 Source를 우선 사용합니다.

```yaml
source_adapters:
  web: required
  github: required
  reddit: required
  threads:
    user_provided_link_text_screenshot: required
    official_api_search: conditional_pilot
    unofficial_scraping: prohibited
```

Source별 역할은 분리합니다.

- Web: 공식 사실, 실제 운영 제품, 화면 구성요소와 사용자 흐름
- GitHub: 구현 가능성, 공식 Repository, Demo, Release, Issue와 License
- Reddit: 실제 사용자 경험, 반복 불만과 실패 사례
- Threads: 최신 아이디어·디자인 사례·개인 주장. 사용자 제공 자료를 기본으로 사용

수집기는 해당 웹에 필요한 업무, 화면 구성요소, 일반 사용자 흐름, 실제 Reference와 구현 후보를 수집합니다. 분석기는 수집 결과에서 필수·권장·선택·제외 기능, 위험, 최소 MVP와 디자인 방향을 판단합니다. 개인 의견은 공식 사실과 분리하고 교차검증합니다.

### 디자인 Reference 다양화

Reference 수만 늘리지 말고 다음 축이 서로 다른 방향을 의도적으로 조사합니다.

- 동일 업종·인접 업종·다른 업종의 유사 업무
- 빠른 완료·안심 확인·비교 선택·초보자 안내·전문 작업
- Preview 중심·대화 중심·Dashboard·Wizard·Canvas·Split View
- Minimal·Editorial·Industrial·Calm Professional·Bold Experimental
- Spacious·Balanced·Compact 밀도
- Minimal·Functional·Expressive Motion

한 조사 Run은 구조적으로 다른 방향을 최대 세 개로 제한하고, 각 방향의 실제 링크·이미지를 사용자가 직접 확인하도록 합니다. 색상만 다른 후보는 디자인 다양성으로 인정하지 않습니다.

### UI UX Pro 대표 Landing Page Sample

UI UX Pro Max는 디자인 지식·규칙 도구로 인정합니다. 다만 CSV 검색 결과나 텍스트 설명만으로 사용자가 디자인을 확인했다고 판정하지 않습니다.

빠르게 생성할 수 있다면 UI UX Pro의 추천 결과를 대표 Landing Page Sample로 시각화합니다. 이 Sample의 목적은 완성 제품이나 세부 UX 승인이 아니라 다음 톤앤매너를 눈으로 확인하는 것입니다.

```yaml
ui_ux_pro_visual_sample:
  purpose: tone_and_manner_review
  artifact_type: representative_landing_page
  fidelity: concept
  interaction_required: false
  implementation_claim: prohibited
  user_visual_confirmation: required
```

Sample에 최소한 다음을 표시합니다.

- 전체 Style과 분위기
- 대표 Color Palette
- 제목·본문 Typography
- 공간감과 Density
- Hero와 대표 Card·Button·Input
- 이미지 사용 방식
- Motion 강도를 설명하는 짧은 표기
- 해당 업종에서 피할 금지 Pattern

빠른 Tone Sample은 정적 이미지 또는 단순 HTML로 만들 수 있습니다. 기능·사용 흐름을 선택해야 하는 단계에서는 별도의 클릭형 A/B/C Preview가 필요하며 Tone Sample로 이를 대체하지 않습니다.

### 시각 확인과 구현 연결

디자인은 다음 증거 순서로 진행합니다.

```text
실제 Reference 링크·사용자 Screenshot
→ 사용자가 눈으로 확인
→ UI UX Pro 대표 Landing Page Sample로 톤앤매너 확인
→ Reference Mix와 Design Contract
→ 구조가 다른 클릭형 A/B/C
→ 사용자 선택
→ 실제 구현
→ Reference·Preview·구현 결과 비교
```

구현이 어렵거나 원본 화면을 직접 재현할 수 없다면 최소한 사용자가 열 수 있는 원본 페이지 링크, 이미지 링크 또는 출처가 기록된 Screenshot을 제공합니다. 출처 없는 이미지는 분위기 참고만 가능하며 검증된 Reference로 승격하지 않습니다.

### 인정 도구와 검증 상태

```yaml
design_toolchain:
  ui_ux_pro_max:
    role: design_knowledge_and_rules
    status: locally_installed_and_called
  frontend_app_builder:
    role: clickable_preview_generation
    status: verified_in_existing_v2_flow
  imagegen:
    role: visual_concept_exploration
    status: visual_artifact_verified
  browser_and_frontend_testing:
    role: rendered_result_verification
    status: verified_in_existing_v2_flow
  product_design_ideate_and_image_to_code:
    role: candidate_visual_exploration_and_implementation
    status: installed_candidate_requires_isolated_pilot
```

새 Skill·오픈소스는 `발견 → 공식 출처·License 확인 → 격리 Pilot → 실제 화면 생성 → 기존 방법과 비교 → 사용자 확인`을 통과한 경우에만 인정 도구로 승격합니다.

## 12. 얇은 UI 착수 Gate

얇은 UI는 Post-MVP 전체 설계가 확정된 뒤 본격적으로 작업합니다. 현재 `THIN_UI_MVP_CONTRACT.md`, `PM1_HANDOFF.md` 등에 있는 `approved`, `active_milestone: PM1`, `다음 작업은 클릭형 Preview` 표현은 최신 사용자 최종 승인으로 해석하지 않습니다.

```yaml
thin_ui:
  planning_reference: existing_contract_only
  clickable_preview: blocked
  implementation: blocked
  unblock_conditions:
    - final_pm_count_and_sequence_approved
    - each_pm_scope_and_exclusions_approved
    - each_pm_pass_criteria_approved
    - design_intelligence_flow_approved
    - source_adapter_scope_approved
    - user_explicitly_declares_post_mvp_design_approved
```

위 조건을 모두 만족하기 전에는 얇은 UI의 새 이미지 시안, 클릭형 Preview, Core API, Registry, Preview Process 제어, ADB 연결, 패키지 설치와 제품 구현을 시작하지 않습니다.

## 13. GPT에게 전달할 최신 의견 요청

아래 요청문을 GPT 공동 설계 대화에 그대로 전달할 수 있습니다.

```text
현재 PM 설계에 다음 사용자 방향을 반영해서 의견을 줘.

1. 새 웹·앱 요청의 수집기는 Web, GitHub, Reddit, Threads를 사용한다. Web은 공식 사실과 실제 운영 사례, GitHub는 구현 가능성·Demo·Release·Issue·License, Reddit은 실제 사용자 경험, Threads는 최신 아이디어와 디자인 사례를 담당한다. Threads는 사용자 제공 링크·본문·Screenshot을 기본으로 하고 공식 API 검색은 조건부 Pilot, 비공식 Scraping은 금지한다.

2. 수집기는 해당 웹에 필요한 구성요소, 업무 흐름, 실제 Reference와 구현 후보를 조사하고, 분석기는 필수·권장·선택·제외 기능, 위험, 최소 MVP와 디자인 방향을 판단한다. 이 흐름은 현재 V2의 수집→분석→추천→사용자 승인 흐름에 편승한다.

3. 디자인 Reference는 계속 추가할 수 있어야 하지만 자동 채택하지 않는다. 실제 링크·이미지를 사용자가 눈으로 보고 선택하고, 검증된 특징만 Design System으로 승격한다. 다양성은 업종, 사용자 목표, 정보 구조, 시각 스타일, 모바일 흐름, 밀도와 모션 축을 달리해 만든다. 색상만 다른 후보는 인정하지 않는다.

4. UI UX Pro Max는 인정된 디자인 지식·규칙 도구다. 빠르게 가능하다면 검색 결과를 대표 Landing Page Sample로 시각화해 사용자가 톤앤매너만 눈으로 확인할 수 있게 한다. 이 Sample은 완성 제품이나 클릭형 UX 승인이 아니다. 기능과 흐름은 이후 구조가 다른 클릭형 A/B/C에서 별도로 확인한다.

5. 기본 검증 Toolchain은 실제 Reference 링크·사용자 Screenshot + UI UX Pro Max + frontend-app-builder + Browser 검증 + 사용자 시각 승인이다. ImageGen은 새 Concept 탐색 보조이며 실제 운영 Reference를 대체하지 않는다. 새 Skill은 격리 Pilot과 실제 결과 비교 전에는 인정 도구로 승격하지 않는다.

6. 얇은 UI는 전체 Post-MVP 설계가 사용자의 명시적 승인으로 확정된 뒤 본격적으로 작업한다. 그전에는 기존 문서의 approved 표현과 관계없이 PM1 Preview·설치·구현을 시작하지 않는다.

이 방향에서 기능 중복, 빠진 계약, 구현 위험과 PM 구조에 반영할 수정안을 제시해줘. 아직 설계 완료를 선언하지 말고, 다음에 사용자가 결정해야 할 가장 중요한 질문 하나만 마지막에 물어봐줘.
```
