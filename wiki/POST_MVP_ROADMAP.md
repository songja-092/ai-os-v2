# Post-MVP Roadmap

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

`AI OS V2 Core MVP M1~M7`은 완료·동결합니다. Post-MVP는 사용자가 각 단계에서 새로 할 수 있는 기능을 기준으로 `PM1~PM4`를 순서대로 진행합니다. 이 문서는 구현 권한을 부여하지 않으며, 각 PM 구현 직전에 현재 설치 Skill, 기존 코드와 공식 기능, 공식 문서, 유지관리되는 GitHub OSS, 최소 직접 구현 순으로 환경을 다시 조사합니다.

```yaml
post_mvp:
  planning_status: approved
  active_milestone: PM1
  implementation_status: not_started
  auto_research_allowed: true
  auto_analysis_allowed: true
  auto_implementation_allowed: false
  user_approval_required_for_implementation: true
```

## 상태 언어

후보 판정과 구현 상태를 분리합니다.

```yaml
decision_status: adopted | conditional | deferred | rejected
lifecycle_status: proposed | researched | pilot_ready | implemented | verified
```

조사하거나 채택했다는 이유만으로 구현·검증 완료로 올리지 않습니다. 재사용 Recipe는 실제 프로젝트 실행, 실패 처리, 사용자 확인, Result Commit과 Rollback/Restore가 필요합니다.

## PM1 — 얇은 UI

### 이번 단계에서 생기는 기능

사용자는 프로젝트를 선택하고 현재 요청과 상태, 실제 Preview를 확인한 뒤 `통과`, `수정 요청`, `중단` 중 Core가 허용한 행동을 선택할 수 있습니다. 다른 프로젝트로 이동해도 각 Preview와 Run 상태는 독립적으로 유지됩니다.

### 화면에서 보이는 흐름

```text
프로젝트 홈
→ 현재 상태와 다음 행동 확인
→ 프로젝트 작업실
→ 실제 Preview 확인
→ 통과 / 수정 요청 / 중단
→ 다른 프로젝트로 전환
```

### 필수 범위

- 프로젝트 홈과 프로젝트 작업실
- `ui-state`, `ui-action`, `allowed_actions`, `state_version`, `action_id`
- Core가 소유하는 Project Registry와 허용된 고정 실행 명령
- 프로젝트별 고정 Port와 Preview Process 소유권
- stale·중복·다른 프로젝트 Action 차단
- 실제 Preview와 초기화 상태 신호
- Preview 장애 격리와 최소 오류 보고서
- 390px·430px·PC Preview
- 사용자 판정, Result Commit, Rollback/Restore
- 병원 웹과 PDF 제품의 독립 실행 경로

### 디자인 준비

프로젝트 홈은 `B — 프로젝트·다음 행동 중심`, 프로젝트 작업실은 `A — Preview 중심`을 기본 조합으로 사용합니다. 요청 영역은 필요할 때 펼치며 기본 비율은 `25:75`, Preview 집중 모드는 `10:90`입니다. 이는 클릭형 Preview 제작 기준이며 최종 구현 화면 승인이 아닙니다.

Reference Mix는 PM1 내부 절차이며 [[ui-reference-mix]] · [GitHub 링크](ui-reference-mix.md)의 여섯 제품에서 각각 1~2개 패턴만 사용합니다. 기존 이미지 시안 5장은 초기 참고자료로 보존하되 공식 UI 승인 결과로 사용하지 않습니다.

### 제외

- Galaxy 실제 연결
- Source Adapter UI와 직접 부분 수정
- Plugin 관리와 범용 설정
- 자유 Dashboard 편집과 기능 Marketplace

### 완료 기준

모바일 우선 클릭형 Preview A/B에서 프로젝트 선택, 실제 Preview, 정상·장애·프로젝트 전환, 사용자 Action을 확인하고 사용자가 `A`, `B` 또는 수정안을 명시적으로 선택합니다. 이후 실제 UI가 Core 계약을 지키고 Result Commit과 Rollback/Restore까지 통과해야 PM1을 완료합니다.

```yaml
id: thin_ui
decision_status: adopted
lifecycle_status: proposed
```

## PM2 — 직접 부분 수정

### 이번 단계에서 생기는 기능

```text
Preview에서 HERO-01 선택
→ 글자 크기·콘텐츠 폭·줄바꿈·배경색 조절
→ 미리보기
→ 원래대로 / 적용
```

### V2가 뒤에서 처리하는 것

- Draft Preview를 제품 원본과 분리
- 첫 구현은 기본 HTML Control과 CSS 변수 사용
- 적용 시 Quick Change Run 생성
- 390px·430px·1440px와 가로 넘침·Console 검증
- Result Commit과 Rollback/Restore

Tweakpane은 기본 입력 방식이 부족하다는 실제 증거가 생길 때만 조건부 검토합니다. 범용 페이지 편집기나 자유 CSS 입력은 사용하지 않습니다.

```yaml
id: direct_partial_edit
decision_status: adopted
lifecycle_status: proposed
```

## PM3 — 자료 가져오기

### 이번 단계에서 생기는 기능

```text
Threads·Reddit·GitHub·웹·문서 자료 제공
→ 핵심 내용 확인
→ 공식 자료 교차검증
→ V2 중복·적합성·라이선스 확인
→ 채택 / 후보 / 보류 / 폐기
```

### 필수 지원

- 직접 붙여넣은 본문과 Markdown·Text
- PDF와 일반 공개 웹페이지
- GitHub 저장소·README·Issue·Release
- Reddit 게시글·댓글
- 사용자가 제공한 Threads 링크·본문·Screenshot

YouTube 공개 자막, Threads 자동 수집과 동적 웹페이지 전용 수집기는 조건부입니다. 공식 문서는 사실확인, GitHub는 코드·Issue·Release·라이선스 검증, Reddit은 사용 경험·오류 사례, Threads는 아이디어 발견, YouTube는 공개 자막 확보 시 내용 분석에 사용합니다. Reddit과 Threads의 개인 의견은 검증된 사실로 취급하지 않습니다.

### V2가 뒤에서 처리하는 것

- 공통 Source Schema, 출처 URL, 수집 시각과 Checksum
- 실제 접근 범위와 사실·주장·추정·추천 분리
- 공식 자료 교차검증과 `needs_more_source`
- 수집 실패의 Core 격리
- 사용자 승인 전 후보 자동 등록 차단

기존 Browser·PDF·GitHub 도구를 먼저 사용합니다. Trafilatura는 정적 본문 추출 개선이 확인될 때만 조건부이며 Crawl4AI는 동적 페이지 문제가 실제로 확인될 때까지 보류합니다. 로그인 우회, 쿠키 사용과 Threads 무단 대량 Scraping은 금지합니다.

```yaml
id: source_adapters
decision_status: adopted
lifecycle_status: proposed
```

## PM4 — 제작 정확도와 AI 교체 기반

### 이번 단계에서 생기는 기능

```text
자연어 요청
→ V2와 구현 AI의 이해 비교
→ 일치하면 제작
→ 오해하면 구현 전에 차단
→ 정말 모호할 때 질문 하나
```

### V2가 뒤에서 처리하는 것

- `speckit-analyze`, Intent Packet과 Intent Receipt
- 핵심 용어, 올바른 예·잘못된 예와 시각 Reference
- 변경 허용·금지 범위와 Acceptance Checks
- 불일치 차단, 모호성 질문 하나와 오류 보고서
- AI 역할 Adapter 계약
- Provider별 품질·비용·권한·복구 기록

PM1부터 Antigravity 지시서에 간단한 수동 Intent Receipt를 사용하고 PM4에서 공식 Core 기능으로 일반화합니다.

```yaml
roles:
  planner:
    provider: codex
  implementer:
    provider: antigravity
  verifier:
    provider: codex
```

이 구조는 Provider 교체 구현 완료를 의미하지 않습니다.

```yaml
id: ai_role_adapter
decision_status: adopted_as_architecture_boundary
lifecycle_status: proposed
```

## 마일스톤별 도구 조사 원칙

각 PM 구현 직전에 다음 순서로 조사합니다.

```text
현재 설치 Skill
→ 기존 코드와 공식 기능
→ 검증된 GitHub 오픈소스
→ 공식 문서
→ 최소 직접 구현
```

각 단계에서 현재 도구, 비어 있는 역할, 추가 후보 최대 2개, 중복, 라이선스, 설치 필요성과 가장 작은 격리 실험을 보고합니다. 도구를 발견했다는 이유만으로 설치하지 않습니다. Antigravity 환경 감사 기준 현재 추가 Skill은 설치하지 않으며 `code-reviewer`는 필요 발생 시, `diagnosing-bugs`는 반복 디버깅 실패 시에만 재검토합니다.

## 후보 판정

### 채택

- PM1 얇은 UI와 Reference Mix
- PM2 직접 부분 수정
- PM3 Source Adapter 공통 구조
- PM4 Intent 정합성
- 최소 오류 보고서
- AI 역할 Adapter 경계

### 조건부

- shadcn/ui
- Tweakpane
- Trafilatura
- YouTube 공개 자막
- Threads 사용자 공유
- Reddit 공개 자료
- GitHub 전용 Adapter

### 보류

- Crawl4AI
- Paseo
- OpenClaw
- Galaxy 실제 연결
- Package Registry
- 고객 OS
- Runtime Plugin
- Promptfoo
- GitHub MCP 쓰기

### 폐기 기록

```yaml
- id: web_chatgpt_dom_automation
  reason: UI 변경과 로그인 상태에 취약하고 공식 연결이 아님
  reconsider_when: 공식 API 또는 승인된 Connector가 같은 목적을 제공할 때
- id: login_cookie_bypass
  reason: 개인정보·계정·서비스 정책 위험
  reconsider_when: 공식 인증 API와 사용자 승인 범위가 제공될 때
- id: threads_bulk_scraping
  reason: 무단 대량 수집과 서비스 정책 위험
  reconsider_when: 공식 API와 명확한 사용 권한이 제공될 때
- id: ui_direct_run_yaml_write
  reason: Core 상태 소유권과 충돌
  reconsider_when: 없음
- id: ui_arbitrary_shell
  reason: Project Registry와 실행 권한 경계를 우회
  reconsider_when: 없음
- id: generic_workflow_engine
  reason: 현재 V2 단일 Orchestrator와 중복되는 과설계
  reconsider_when: 검증된 Core로 표현할 수 없는 반복 흐름이 생길 때
- id: default_rag_vector_db
  reason: 현재 파일·Run·공식 자료 검색으로 충분
  reconsider_when: 자료 규모 때문에 검색 품질 저하가 반복 검증될 때
- id: runtime_plugin_marketplace
  reason: Package Registry 이전 단계에 불필요한 권한·유지보수 부담
  reconsider_when: 검증된 Module Registry가 안정화된 뒤
- id: puck_full_editor
  reason: PM2의 제한된 부분 수정 범위를 초과
  reconsider_when: 사용자 요구가 범용 페이지 편집으로 확정될 때
- id: free_drag_resize_dashboard
  reason: 얇은 UI의 안정된 Shell과 초보자 흐름을 해침
  reconsider_when: 고정 레이아웃으로 해결되지 않는 사용성 증거가 생길 때
```

## 현재 다음 작업

```text
Reference Mix를 반영한 모바일 우선 클릭형 Preview A/B 제작
→ 390px·430px·PC 및 정상·장애·프로젝트 전환 검증
→ 사용자 A / B / 수정 요청
```

클릭형 Preview에는 기존 Product Design Ideate, frontend-app-builder, Product Design Audit, frontend-testing-debugging과 Browser만 사용하며 새 UI 라이브러리를 설치하지 않습니다.
