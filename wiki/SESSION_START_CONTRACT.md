# AI OS V2 새 세션 시작 계약

## 2026-08-26 콘텐츠 Reference 레이더

- 사용자 결정: 기본 Reference 탐색은 Instagram 카드뉴스·슬라이드와 Threads 글을 우선합니다.
  Shorts·Reels는 마케터 역할 또는 영상 마케팅 요청에서만 사용하며 기본 후보에 섞지 않습니다.
- `v2-content-reference-radar` 저장소 Skill은 사용자의 쉬운 주제와 Interview/Spec 입력을
  YouTube·Instagram·Threads 공개 Reference 후보로 바꾸고, 플랫폼 내부에서만 순위화한 뒤 최대
  10개를 `채택·보류·폐기`로 넘깁니다.
- `haeun2525/trend-radar` Commit `835558a3439b1e445b1bbbedb341f7e50ae7ec33`은 License 파일이
  없어 코드 복사 없이 구조만 참고했습니다.
- 로그인된 Aside Browser에서 `#바이브코딩` 공개 게시물 10건·영상 5건을 확인했고, 영상 3건의 공개
  반응 지표로 Instagram 내부 순위화까지 Runtime PASS했습니다. Threads는 공개 후보 5건·본문 3건을
  읽었지만 검색 숫자의 지표 이름이 노출되지 않아 실제 순위화는 `not_proven`입니다.
  Cookie·Token·Browser Profile과 비공개 자료는 저장하지 않습니다.
- 새 세션은 `pm4-artifacts/content-reference-radar-v1/runtime-evidence.json`을 읽고 이 결과를 PM4
  완료나 범용 Runtime으로 확대 해석하지 않습니다.
- PM4 Evidence Router는 현재 **단일 주제 제한 Runtime**입니다. `AI 바이브코딩 웹 디자인
  Reference` 요청에서 Instagram·Threads·YouTube·GitHub·공식 웹의 기존 Artifact를 네 가지
  증거 역할(시각 Reference·실사용 반응·구현 재료·공식 사실)로 나눠 10개를 수집했고,
  `tools/verify-v2-content-reference-radar`와 실제 Browser 검토 화면을 PASS했습니다.
- 10개 중 한국어로 내용과 참고 이유를 설명할 수 있는 4개만 사용자 Gallery에 표시합니다.
  설명이 빈약한 제목뿐인 Threads·YouTube 항목과 번역되지 않은 GitHub 설명 등 6개는 수집
  증거로만 보존하고 선택 후보에서는 제외합니다. 사용자 행동은 `원문 보기·채택`만 제공합니다.
- 검토 화면의 채택은 이제 `state/pm4-evidence-reference-state.json`에 Core 상태로 저장됩니다.
  시험 채택 1건을 저장하고 Dashboard 서버 재시작 뒤 복원한 다음 시험값을 비우는 Runtime을
  PASS했습니다. 이는 Core 승인이나 제품 적용이 아닙니다. 임의 주제 범용 수집, 자동 채택,
  자동 제품 적용, 사용자 최종 PM4 PASS는 `not_proven`입니다.

이 문서는 Codex·Antigravity·기타 AI가 새 세션에서 **가장 먼저 읽는 공식 진입점**입니다.

새 세션은 이 문서를 읽은 직후 `wiki/CODEX_COMMON_EXECUTION_CONTRACT.md`를 읽습니다. 이 공통 실행계약은 Codex만의 설정이 아니라 웹 GPT·Antigravity를 포함해 저장소를 작업하는 모든 AI가 사용하는 작업·검증·복구 기준입니다.

## 가장 중요한 규칙

> 직접 확인하지 않은 기능·상태·PASS·동기화·복구를 된다고 말하지 않습니다.

- 이 계약은 AI의 환각을 0으로 만들거나 완전히 차단한다고 보장하지 않습니다.
- 채팅 기억, 이전 세션 요약, 사용자의 과거 설명은 현재 상태의 증거가 아닙니다.
- 현재 Commit의 파일·코드·실행 결과·검증 증거만 공식 사실로 사용합니다.
- 증거가 없거나 접근할 수 없으면 `확인 필요` 또는 `not_proven`으로 기록합니다.
- 설계됨, 승인됨, 구현됨, 검증됨, 사용자 PASS를 서로 바꾸어 말하지 않습니다.

## 세 저장 위치를 구분합니다

새 세션은 다음을 하나로 간주하지 않고 각각 확인합니다.

1. 현재 작업 중인 로컬 Worktree와 Branch
2. GitHub `origin/main`
3. Obsidian에서 여는 저장소 또는 Vault

각 위치의 HEAD SHA가 같다는 증거가 있을 때만 `동기화됨`이라고 표현합니다. 다르면 어느 위치가 앞서거나 뒤처졌는지 보고하고, 자동 Merge·Reset·Restore·Stash를 하지 않습니다.

Obsidian은 문서를 보여주는 도구일 뿐 별도의 최신 상태 보증 장치가 아닙니다. Obsidian Vault의 Git HEAD와 현재 작업 Worktree의 HEAD가 다르면 두 문서 집합을 섞어 현재 사실을 만들지 않습니다.

## 새 세션 필수 순서

사용자의 첫 작업을 수행하기 전에 다음을 완료합니다.

1. 현재 저장소 경로, Branch, HEAD, Dirty 상태를 확인합니다.
2. 원격 조회가 허용되고 가능하면 `origin/main`을 갱신해 SHA를 확인합니다. 조회하지 못하면 `not_checked`로 표시합니다.
3. Obsidian Vault 경로와 그 저장소 HEAD를 확인합니다. 접근하지 못하면 `not_checked`로 표시합니다.
4. 이 문서를 읽은 다음 아래 문서를 실제 파일에서 읽습니다.
   - `AGENTS.md`
   - `wiki/CODEX_COMMON_EXECUTION_CONTRACT.md`
   - `wiki/GOAL.md`
   - `wiki/CURRENT_STATE.md`
   - `wiki/DECISIONS.md`
   - `wiki/ARCHITECTURE.md`
   - `wiki/VERIFICATION.md`
   - `wiki/DESIGN_SYSTEM.md`
   - `wiki/V2_ENGINEERING_OPERATING_MODEL.md`
   - `wiki/V2_ENGINEERING_METHOD_RESEARCH_2026-08-21.md`
   - `wiki/SPEC_KIT_V2_ADAPTER_PILOT_2026-08-21.md`
   - `wiki/POST_MVP_PM0_PM6_BASELINE.md`
   - `wiki/PM1_PM4_DESIGN_MEETING_2026-08-19.md`
   - `wiki/AI_EVIDENCE_GUARD.md`
   - 현재 활성 PM의 최신 완료·진행 보고서
5. 완료된 PM의 잠금 Commit·Tag·Hash와 현재 활성 PM을 확인합니다.
6. 아래 형식의 시작 보고를 먼저 제공합니다.

```yaml
session_preflight:
  repo_path:
  branch:
  local_head:
  dirty_preserved:
  origin_main:
  github_alignment: same | different | not_checked
  obsidian_vault:
  obsidian_head:
  obsidian_alignment: same | different | not_checked
  current_pm:
  locked_pms: []
  implemented: []
  verified: []
  not_proven: []
  next_single_action:
```

문서를 일부만 읽었거나 경로에 접근할 수 없으면 `AI OS V2 Memory Loaded`라고 말하지 않습니다. 대신 무엇을 읽지 못했는지 보고합니다.

## 변하지 않는 사용자 계약

- 사용자는 초보자입니다. 먼저 쉬운 한국어로 설명합니다.
- 영어 기술 용어는 필요할 때 `English (한글 발음) — 쉬운 뜻`으로 설명합니다.
- 사용자의 결정이 필요한 경우 `회의할 항목이 있습니다`라고 알리고 한 번에 한 주제씩 다룹니다.
- 회의가 끝나면 `회의가 끝났습니다`라고 명확히 말하고 결과를 기록합니다.
- PM 범위를 벗어난 요청이면 현재 작업을 섞지 않고 어느 PM 범위인지 먼저 알립니다.
- 사용자가 PM 진행을 승인한 뒤에는 매 단계마다 `다음` 입력을 요구하지 않고 승인 범위 안의 작업을 연속 수행합니다. 사람의 디자인·사업 판정, 로그인·권한·비용, 범위 확대, Dirty·잠금 충돌에서만 멈추며 PM 잠금 전 자동화 후보 감사와 최종 PASS는 생략하지 않습니다.
- 사용자가 PM을 PASS하면 해당 PM의 승인 화면·동작·유지 범위·복구 기준을 고정하고 잠근 뒤 다음 PM으로 이동합니다.
- PM이 완료되거나 Repo-local Skill을 새로 만들거나 변경하면 같은 작업에서 이 세션 공통계약의 `정확한 상태`와 Skill 목록을 갱신합니다. 공통계약 반영 전에는 PM 저장이 끝났다고 보고하지 않습니다.
- Dirty 변경은 사용자의 변경으로 보존하며 임의로 Reset·Restore·Stash·Commit하지 않습니다.
- 설치·외부 전송·제품 적용·Commit·Push는 승인 범위 안에서만 수행합니다.
- V2가 만드는 모든 **새 제작**은 인터뷰로 시작합니다. 새 프로젝트는 전체 인터뷰,
  큰 기능 변경은 기존 답을 재사용한 짧은 인터뷰, 승인 범위 안의 명확한 작은 수정은
  인터뷰를 생략합니다. 모호하거나 충돌하면 한 번에 질문 하나만 합니다.
- 인터뷰 결과는 대화로만 소비하지 않고 `제작 범위 확인서`로 정리해 사용자가
  `이대로 시작 | 수정 | 추천 | 중단` 중 하나를 고른 뒤에만 제작 입력으로 사용합니다.
- 작은 수정이 새 Section·새 편집 기능·외부 도구·여러 화면으로 커지면 즉시 멈추고
  짧은 인터뷰를 다시 수행합니다. 확인된 Interview Receipt가 없으면 확장 구현을
  시작하지 않습니다.
- V2의 현재 엔지니어링 기본 방향은 `Harness-first, Spec-guided, Eval-driven, Human-approved, Loop-assisted`입니다. 짧게 `Harness-first, Loop-ready`라고 부릅니다. 사람의 목표·범위·승인·복구 계약 안에서 AI가 작업하고, 반복 가능하며 기계적으로 검증·복구 가능한 병목만 제한된 Loop로 자동화합니다.
- 새로운 방법은 `조사 → 격리 시험 → 기존 방식 비교 → 사용자 채택 → 실제 프로젝트 → 반복 성공` 순서를 거쳐야 기본값이 됩니다. 유행, GitHub Star, 홍보 문구만으로 기본 Skill이나 Core 기능으로 승격하지 않습니다.
- 자동화에는 시도·시간·비용 제한, PASS·중단 조건, Rollback, 사용자 호출 조건이 있어야 하며 효과가 없으면 수동 흐름과 기존 Artifact를 보존한 채 제거할 수 있어야 합니다.
- 모든 PM은 마지막 잠금 전에 읽기 전용 `자동화 후보 감사`를 수행합니다. 후보가 없으면 근거를 기록하고 잠금으로 진행합니다. 후보가 있으면 자동화 대상·증거·최소 범위·위험·복구 방법을 먼저 보여주고 사용자의 `채택 | 보류 | 폐기` 판정을 받은 뒤, 공통계약·PM 잠금·승인 범위와 충돌이 없을 때만 자동화하고 재검증합니다. PM PASS를 자동화 승인으로 간주하지 않습니다.
- PM을 넘기기 전 `tools/verify-pm-transition-evidence`를 실행해 잠금·Tag·사용자 PASS·기술 증거·현재 상태의 누락과 충돌을 읽기 전용으로 확인합니다. 이 검사는 기본 자동화이지만 PM을 자동 PASS하거나 파일을 자동 수정하지 않습니다.
- 상세 운영 원본은 `wiki/V2_ENGINEERING_OPERATING_MODEL.md`입니다. 이 문서와 충돌하는 임시 대화·보고서는 공식 기본 규칙으로 사용하지 않습니다.

## 변하지 않는 V2 용어 계약

- `V2`: Skill을 사용해 결과물을 만들고 Module을 장착·관리하는 OS형 제작 보드판입니다. V2 자체는 Module이 아닙니다.
- `프로젝트`: 제작 작업공간입니다. 프로젝트 자체는 Module이 아닙니다.
- `Section`: 요구사항 대화, 현재 단계, Preview처럼 화면을 구성하는 영역입니다.
- `Skill`: V2가 작업에 사용하는 방법이나 도구입니다. 사용자 화면에서는 `스킬`이라고 부릅니다.
- `Module`: V2가 제작했거나 가져와 검증했고 장착·제거·재사용할 수 있는 실제 결과물입니다.
- `디자인 시스템`: 디자인 탐색·채택·구현·수정·검증의 단일 공식 원본인 `wiki/DESIGN_SYSTEM.md`입니다.
- 카톡형 요구사항 대화창과 Preview는 Section이며 Module이 아닙니다.
- 외부 GitHub 프로젝트나 Skill은 가져왔다는 이유만으로 Module이 되지 않습니다. 계약 변환·격리·동작 검증을 통과해야 Module 후보 또는 Module이 됩니다.

## 모든 AI가 확인할 Repo-local Skill

- `V2 Beginner Technical Translator`: 초보자 표현과 개발 설명을 서로 번역하는 Codex 대화용 Skill
- `V2 Design Finish`: Visual Target 제작부터 디자인 마감 검사까지 지원하는 Skill
- `V2 Capability Lab`: 외부 Skill·Plugin·오픈소스를 비공개 프로젝트와 분리해 격리 시험하는 Skill
- `프로젝트 패키징` (`v2-project-packaging`): 이미 제작된 프로젝트 결과를 읽고 Module Manifest·기능 목록·격리 Preview 초안을 만드는 Skill. 자동 기능 완료 판정·자동 Core 등록·자동 채택은 하지 않습니다.
- `V2 Layout Editor Integration` (`v2-layout-editor-integration`): Puck·React Grid Layout을 제거 가능한 PM3 Adapter로 연결하고, PC·모바일 배치 분리, 이미지 Slot, 단색·투톤 Palette, 자동 정리, Undo·Restore와 Recipe 안전 검사를 수행하는 Codex Skill. 현재 격리 Pilot 검증 단계이며 Core Registry에는 승격되지 않았습니다.
- `V2 Spec Adapter` (`v2-spec-adapter`): 사용자의 짧은 자연어를 원문 그대로 보존하고 현재 화면·Section·잠금 계약을 읽어 작은 수정용 `Spec Lite` 또는 새 프로젝트·큰 기능용 `Spec Full`로 변환하는 Repo-local Skill입니다. `요구사항 창을 늘려줘` 수준의 요청도 변경 범위·보존 범위·완료 기준·회귀검사로 정리하며, 사용자는 쉬운 확인만 봅니다. Skill 구조와 가짜 요청 Pilot은 PASS했지만 V2 Core Runtime 자동 연결은 아직 구현되지 않았습니다.
- `V2 Design Director` (`v2-design-director`): 후보별 Reference 탐색·시각 결과·사용자 채택/보류/폐기를 기록하고, 채택 공급원을 역할별 Section에 연결한 Draft Design Recipe와 HTML 추적 상태를 자동 검사합니다. 사용자 결정을 대신하거나 Core·제품에 자동 적용하지 않습니다.

## PM별 Codex 기본 도구 계약

- PM1은 현재 Codex 환경의 `Product Design`을 디자인 탐색·Visual Target·Screenshot 기반 디자인 감사의 기본 작업 Adapter로 사용합니다.
- PM2는 `Build Web Apps`를 승인된 Visual Target·Design Recipe의 실제 화면 구현 Adapter로 사용합니다.
- PM6은 `Frontend Testing`으로 실행 화면·상호작용·Console·반응형·회귀를 검사하고, `Product Design Audit`으로 디자인 마감 품질을 별도로 검사합니다.
- 위 도구는 Codex 작업 환경에 이미 존재하므로 새 Package 설치가 필요하지 않습니다. V2 Core Runtime에 자동 연결됐다는 의미는 아닙니다.
- 도구는 Core 상태·승인·Version·복구를 소유하지 않으며, 사용자 승인과 PM PASS를 대신하지 않습니다.
- 기능 PASS와 디자인 PASS를 분리하고 실제 고객 결과물의 PM1→PM2→PM3→PM6 E2E가 재현되기 전에는 통합 완료로 표현하지 않습니다.
- 상세 계약과 현재 증거 상태는 `wiki/PM_CODEX_TOOLCHAIN_ADOPTION_2026-08-24.md`를 사용합니다.

## Codex Sites 고객 웹 적용 계약

- `Codex Sites`는 고객용 랜딩페이지·병원·인테리어·포트폴리오·소개 웹처럼 개인정보·결제·중요 데이터가 없는 낮은 위험 프로젝트의 조건부 제작·배포 Adapter로 우선 사용합니다.
- 로그인이나 간단한 데이터 저장이 포함되면 격리 Pilot에서 권한·데이터 보존·배포·복구를 먼저 확인한 뒤 적용 여부를 결정합니다.
- 결제·민감정보·복잡한 사용자 권한·관리자 기능·Migration·여러 사용자 동시 작업·V2 Core 상태 연결이 포함되면 `회의할 항목이 있습니다`라고 사용자에게 먼저 알립니다.
- 위 복잡한 요구가 발견되면 Codex Sites로 바로 구현하거나 자동 배포하지 않고, `Sites 범위 확장 시험`과 `기존 Antigravity 구현 + Codex 검증` 중 안전한 경로를 사용자에게 쉬운 말로 비교합니다.
- 단순 웹 우선은 영구 제한이 아닙니다. 실제 프로젝트에서 구현·기능·보안·복구·사용자 승인까지 반복 검증된 범위만 단계적으로 확대합니다.
- Codex Sites는 V2 Core, Design Recipe, Module Registry, 승인, Version 또는 Restore의 원본이 될 수 없습니다.

## PM Codex 도구 첫 통합검증 결정

- 첫 통합검증 대상은 사용자가 승인한 `기존 병원 웹`입니다.
- 기존 원본과 증거를 보존한 격리 복사본에서 `PM1 Product Design → PM2 Build Web Apps → PM3 부분 수정 → PM6 Frontend Testing + Product Design Audit` 흐름을 검증합니다.
- 이번 Pilot에는 실제 배포를 포함하지 않습니다.
- 실행 전 기존 잠금·Recipe·Visual Target을 확인하고 변경 범위만 짧은 인터뷰로 확정합니다.
- 기능·디자인·모바일·접근성·회귀·Version Restore와 사용자 최종 승인이 모두 확인되기 전에는 통합검증 완료 또는 PASS라고 표현하지 않습니다.
- 상세 범위와 상태는 `wiki/PM_CODEX_TOOLCHAIN_ADOPTION_2026-08-24.md`를 사용합니다.

Skill의 최신 상세 기능과 상태는 `wiki/V2_SKILL_INVENTORY_AND_TRANSLATOR_RESEARCH_2026-08-19.md`에서 확인합니다. 문서에 이름만 있다고 Runtime에 자동 연결됐다고 판단하지 않습니다.

## 이 문서 작성 시점의 정확한 상태

- Core MVP M1~M7: 완료·동결로 기록되어 있으나 새 세션은 현재 Commit의 증거를 다시 연결해야 합니다.
- PM0: 사용자 유예 조건이 포함된 PASS로 기록되어 있습니다.
- PM1: 사용자 PASS 후 잠금 기준이 존재합니다.
- PM2: 사용자·기술 PASS 후 `pm2-complete-2026-08-19` Tag로 잠겼습니다.
- `pdf-result-preview`와 `hospital-web-result-preview`: 검증된 프로젝트 결과 Module입니다.
- 목록에서 선택한 Module 하나만 Preview하며 프로젝트별 기능 목록을 분리합니다.
- Core `ui-state → UI → ui-action → Core`, 선택 상태 저장, 비활성, 오류 격리, 복원과 금지 Action 차단을 검증했습니다.
- PM3은 2026-08-21 사용자가 `일단 통과`로 판정해 범위를 잠갔습니다. 기술 완료는
  `not_proven`이며 다음 진행 가능 단계는 PM4입니다.
- 2026-08-21 PM3 편집기 확장 인터뷰를 완료했습니다. 기능 동작은 PM3에서 판정하되
  실제 고객 결과물·390/430·Undo·원본 보존·격리·접근성·회귀는 PM6에서 다시 검증합니다.
  병원 웹 편집 Draft는 PM6 재검증 전 동결 상태입니다. 상세 원본은
  `wiki/PM3_EDITOR_INTERVIEW_AND_RESEARCH_2026-08-21.md`입니다.
- PM3 사용자 판정과 잠금 경계는
  `wiki/PM3_USER_PASS_WITH_PM6_REVALIDATION_2026-08-21.md`를 사용합니다.
- PM4는 2026-08-21 Interview → Collector(수집만) → Analyzer(사실·Link·짧은 요약) →
  사용자 확인을 분리한 로컬 우선 최소 Pilot을 `9/9 PASS`했고 현재 `started`입니다.
  V2는 자료가 충분하다고 단정하지 않으며 사용자가 `자료 더 찾기·이 정도면 충분·조사 방향 수정`을 선택합니다.
  실제 조사 요청·출처 검증·사용자 판정·Capability Lab 연결 전에는
  단일 Pilot만으로 PM4 전체 PASS라고 말하지 않습니다. 새 세션은
  `wiki/PM4_LOCAL_FIRST_COLLECTOR_PILOT_2026-08-21.md`를 먼저 읽습니다.
- 2026-08-24 사용자는 PM4 MVP를 `인터뷰 → Spec Lite 제작 범위 확인서 → 명세 기반
  프로젝트 자료 수집 → 제작 가능한 서로 다른 후보 3개 → 사용자 선택`으로 확정했습니다.
  현재 뉴스·도구 브리핑은 제거하지 않고 선택형 Module로 분리하며, 새 프로젝트 제작의
  기본 수집기로 간주하지 않습니다. PM4 MVP에서는 Preview 제작·외부 도구 설치·제품 적용·
  배포를 하지 않습니다. Workflow는 새 엔진을 만들지 않고 기존 V2 Spec Adapter와 격리
  Spec Kit 방식으로 위 단계만 연결하며 사용자 선택에서 반드시 멈춥니다.
- PM4 MVP의 첫 실제 검증 대상은 `전자명함`입니다. PASS 조건은 확인된 인터뷰 결과가
  검색 조건에 보존되고, 전자명함과 직접 관련된 출처·원문 Link·선정 이유를 가진 서로 다른
  후보가 표시되며, 중복 제거·출처 실패 격리·사용자 선택 저장/복원·중단 시 제품 무변경이
  실제로 확인되는 것입니다. 이 E2E 증거와 사용자 PASS 전에는 `spec_based_project_collector`,
  `pm4_workflow_connection`, `PM4 완료`를 모두 `not_proven`으로 기록합니다.
- 기본 후보 수는 3개이지만 작은 결과물은 인터뷰에서 사용자가 늘릴 수 있습니다. 첫 전자명함
  시험은 사용자의 2026-08-24 결정에 따라 같은 필수 기능을 유지한 서로 다른 시각 방향 5개로
  검증합니다.
- PM4 프로젝트 수집은 `인터뷰에서 기능 확정 → Reddit·YouTube·Instagram·Threads에서 실제 사용·불편·표현 방식 탐색
  → 디자인·사용 방향 정리 → 그 방향을 구현할 GitHub 코드·기능·라이선스 확인 → 출처별 조사 상태 공개
  → 참고 후보 선택`으로 분리합니다. GitHub가 먼저 후보 방향을 결정하거나 GitHub 저장소 5개를
  곧바로 시안 5개로 취급하지 않습니다. 기능을 후보 카드마다
  다시 고르게 하거나 디자인 선택과 기술 선택을 한 버튼으로 합치지 않습니다.
- GitHub는 국가별 디자인 공급원이 아니라 구현 코드·기능·라이선스 증거 공급원입니다. 한국
  시각·문구·시장 적합성은 한국 실제 웹·Figma·Instagram·Threads 등에서 보완하고, 구현 후보에는
  국가 혼합 조건을 강제하지 않습니다.
- Core는 확정된 인터뷰·수집 근거·구현 가능성을 기준으로 후보 하나를 `추천`할 수 있지만 자동
  선택·채택·설치하지 않습니다. 사용자가 선택하지 않은 후보도 즉시 폐기하지 않고 비교·거절
  기록으로 보존하며, 사용자가 폐기하거나 새 후보가 대체할 때만 상태를 변경합니다.
- 첫 전자명함 시험의 과거 대화 기록과 Handoff Artifact가 충돌했으나, 2026-08-25 사용자가
  1번 `QR·NFC로 바로 연결하는 명함`을 최종 재확인했습니다. Core 추천 3번은 비교 근거로만
  보존하며 자동 선택이 아닙니다. 나머지 후보는 `candidate_preserved`로 보존하고 실제 설치·
  구현·제품 적용·배포는 다음 승인 전까지 금지합니다.
- 출처 Adapter가 존재한다는 사실과 해당 요청에서 실제 실행됐다는 사실을 분리해 표시합니다.
  첫 전자명함 시험은 Reddit 3건·YouTube 2건·Threads 3건과 GitHub 구현 재료 5건을 실제 Link로
  연결했습니다. Instagram은 수집 브라우저의 로그인 세션 미연결로 0건이며 PM4 마지막 검증으로
  미뤘습니다. 이 상태에서 Instagram 수집 완료 또는 5개 출처 전체 PASS라고 표현하지 않습니다.
- `다음 → 선택 기록 → 제작 가능 확인서` 자동 생성과 Handoff 복원 경로는 검증됐고 최종 선택은
  1번으로 확정됐습니다. 로그인 세션 관리·Instagram 수집과 PM4 최종 PASS는 PM4 마지막 검증
  항목으로 잠급니다.
- 2026-08-26 후속 시각 시안 3번의 중립 색상 수정본은 사용자 `보류`입니다. 이는 PM4 기능 방향
  1번을 취소한 것이 아닙니다. Visual Target 승인·구현은 시작하지 않으며, 전자명함 Reference
  품질 개선과 새 Visual Target 제작은 PM1 디자인 작업으로 넘깁니다.
- 2026-08-26 기존 PM4에 검색 기반 시각 Reference Adapter를 추가했습니다. 고정 Seed 없이 확정된
  전자명함 명세에서 공개 Gallery 검색어를 만들고 화면 8개를 수집했으며, 인테리어 커뮤니티 Fixture에서도
  별도 8개를 수집해 동일 Core 상태 경로로 연결했습니다. 이미지 Hash·출처·한글 요약을 보존하고,
  HTML·Script 실행·Cookie 저장·제품 자동 적용은 금지합니다. 출처 실패 격리·판정 저장·복원은 PASS지만
  두 입력과 Behance 공개 검색 Adapter의 제한 증거이므로 임의의 모든 주제나 Reference 품질 승인,
  PM1 Visual Target PASS로 확대하지 않습니다. 검토 화면은 `/pm4-visual-reference-review.html`,
  검증기는 `tools/verify-pm4-visual-reference`입니다.
- 2026-08-26 PM4 시각 Reference 화면에 `추가 탐색` Refill Loop를 연결했습니다. 기존 후보와
  채택·보류·폐기 판정을 유지하고, 인접 표현으로 검색 범위를 넓혀 URL·SHA-256·이미지 dHash
  유사도 중복을 제거한 새 후보 3~5개만 추가합니다. 첫 전자명함 실제 실행은 기존 12개에 새
  5개를 추가했습니다. 디자인 참고와 GitHub·YouTube 기반 기능 참고는 한 목록으로 섞지 않습니다.
  사용자 URL·이미지는 등록 시 최고 우선순위지만 입력 UI는 아직 없으며, Instagram·Threads 로그인
  수집도 PM4 마지막 검증 전까지 `deferred_login_adapter`입니다. Refill PASS를 범용 주제 탐색이나
  Reference 품질·Visual Target·제품 적용 PASS로 확대하지 않습니다.
- 2026-08-26 사용자는 Refill 결과를 포함한 17개 중 6개 시각 Reference를 채택했습니다.
  `pm4-artifacts/project-collector-mvp-v1/visual-reference-selection-handoff.json`이 다음 세션의
  공식 선택 전달서입니다. 다음 단계는 선택한 Reference를 서로 다른 디자인 방향으로 정리하는
  작업입니다. 이후 사용자는 외부 시안 2번과 이를 확장한 8개 화면 Visual Target을 승인했고,
  Design DNA·사진 유형별 비파괴 보정 계약을 PM4 인계 자료로 고정했습니다. 실제 제품 구현은
  시작하지 않았습니다.
- 2026-08-26 사용자 최종 PASS로 PM4의 제한된 완료 범위를 고정했습니다. 완료 범위는 실제
  전자명함 요청의 인터뷰·수집·Reference 보충·사용자 선택·Design DNA·Visual Target 인계입니다.
  현재 Instagram 로그인 세션은 확인했지만 장기 유지, 임의 주제 범용 수집, 자동 DNA·자동 승인,
  실제 제품 구현은 완료 범위가 아니며 `not_proven`입니다. 다음 활성 단계는 PM5입니다.
- 2026-08-26 `V2 콘텐츠 Reference 레이더`에 국내 3개·해외 4개, 총 7개 AI 코딩·개발
  YouTube 공식 Feed를 연결했습니다. 실제 Runtime에서 7개 Feed 모두 연결되고 최근 30일 후보
  10개가 수집됐으며, 기본 Reference 모드에서는 Shorts를 제외하고 채널별 관련 후보 한 건을
  먼저 보여줍니다. 이는 아이디어·기능 공급원 연결 증거이며 채널 콘텐츠의 자동 채택·제품 적용,
  Instagram·Threads 채널 수집 완료 또는 범용 주제 적합성 PASS가 아닙니다. 증거는
  `pm4-artifacts/content-reference-radar-v1/coding-channel-runtime.json`입니다.
- PM4의 장기 발전안은 **조건부 승격 후보**로 보존합니다. 현재 즉시 허용되는 범위는
  `게시물·이미지·영상 수집 → AI 한글 내용 분석 → URL·이미지 Hash·의미 유사 후보 묶기
  → 사용자 판정`까지입니다. `사용자 취향 학습 → 명세 적합성 자동 점수 → 성공 가능성 추천`은
  지금 구현·활성화하지 않습니다. 서로 다른 실제 프로젝트에서 채택 이유·폐기 이유·구현 결과·
  사용자 최종 판정이 반복 기록되고, 자동 추천의 PASS·FAIL을 검증할 수 있을 때만 사용자가
  승격 여부를 다시 결정합니다. 조건 충족은 자동 도입이 아니라 `승격 검토 요청`을 발생시키는
  시점이며 자동 채택·자동 제품 적용은 계속 금지합니다.
- PM4 일일 탐색 브리핑은 Codex App Automation `v2`로 매일 오전 7시에 실행됩니다.
  Reddit·GitHub·YouTube·Threads·Instagram의 Link와 짧은 요약만 수집하며 충분성·채택을
  자동 판정하지 않습니다. Automation 존재를 각 공급원 Adapter 접근 PASS로 표현하지 않습니다.
- Codex App Automation `v2`는 사용자의 개인용 오전 7시 브리핑으로 별도 유지합니다.
  `pm4-modules/daily-discovery-briefing`은 사용자가 조사 주제·시간·플랫폼을 정하는 제거 가능한
  공용 Candidate Module Draft입니다. `briefing.config.update` Action만 생성하며 Core→Automation
  Adapter·실제 수집·사용성은 PM 마지막 검증 전까지 `not_yet_verified`입니다.
- 작은 수정은 `V2 Spec Adapter`의 `Spec Lite`를 먼저 사용합니다. 사용자가 개발 용어로 다시 설명하게 하지 않고 선택된 화면에서 대상을 찾은 뒤 `바꿀 것·유지할 것·확인 방법`만 보여줍니다. 새 프로젝트·새 Module·여러 화면·데이터·권한·배포가 포함되면 `Spec Full`로 승격해 저장소의 공식 Spec Kit Skill을 사용합니다. 명세 생성은 구현·PASS·Commit 승인이 아닙니다.
- 디자인 공급원 비교는 `pm3-artifacts/design-director-trials/trial-index.json`의 순서와 고정 Brief를 사용합니다. 최초 Figma 실행은 연결 예비 시험이며 본 비교 결과로 계산하지 않습니다.
- 디자인 공급원 10개 시각 시험은 종료됐습니다. 5번 Design MCP와 7번 UI UX Pro MCP가 명시적 선호 1·2위이며, 2·3·4·5·7·9·10번 방향을 채택하고 6·8번은 보류했습니다. 여러 채택 공급원을 역할별로 함께 사용할 수 있습니다.
- `reference-adoption-pilot-v1`에서 채택 공급원 5개가 Draft Recipe와 실제 HTML 5개 Section에 연결되는 것을 자동 검증했습니다. Core 자동 선택·제품 적용·PM3 수정 뒤 방향 보존·다른 프로젝트 재사용은 아직 `not_proven`입니다.
- 디자인 규칙과 역할의 공식 원본은 `wiki/DESIGN_SYSTEM.md`입니다. V2 운영 화면과 고객 결과물은 공통 품질 규칙만 공유하며, Codex는 디자인 총괄·지시·독립 검증, Antigravity는 승인된 실제 구현, 사용자는 최종 판정을 담당합니다.
- PM별 최신 사용자 결정 배치와 미구현 항목은
  `wiki/PM_FLOW_DECISION_ALIGNMENT_2026-08-21.md`를 사용합니다. 실행 순서는
  `PM5 인터뷰·명세 → PM4 기존 자산 우선·필요 시 조사 → PM1 방향 3개·선택 후 DNA·
  Visual Target → PM2 구현 조립 → PM3 부분 수정 → PM6 전체 재검증`이며, PM 번호는
  기능 구현·검증 단계이므로 실행 호출 순서와 다를 수 있습니다.
- PM3 격리 Pilot에는 카드 3개의 Puck·React Grid Layout 편집, 글씨와 Grid 크기 독립성, 넘침 경고, 이미지 Slot, 구역별 색상, 대표색 자동 Palette와 자동 배치·줄바꿈 Draft가 구현됐습니다. Build와 핵심 상호작용은 검증했지만 실제 병원 웹 Section 적용, 접근성·Bundle 분리, 사용자 최종 PASS는 아직 `not_proven`입니다.
- PM3 부분수정의 고정 흐름은 `승인 Recipe → 새 Draft → Viewport·Section 선택 → 마우스 수정 → Recipe Diff → Preview·경고 → 권한·반응형·Motion·Reference Trace 검사 → 사용자 적용 → 새 Version·Restore Draft`입니다. Auto 정리는 Draft 제안일 뿐이며 실제 제품에 자동 적용하지 않습니다. 상세 원본은 `wiki/PM3_PARTIAL_EDIT_FINAL_FLOW_2026-08-20.md`입니다.
- 디자인 탐색·채택은 업계의 `탐색 → 정의 → 방향 개발 → Prototype 확인 → 선택·전달` 흐름과 정합하지만 V2 자동 성공 증거는 아닙니다. Design Recipe는 Visual Target 승인 후 처음 쓰지 않고 Reference 선택 시 Draft로 시작해 승인 때 승격합니다.
- `UI Remix`·`Misty`는 설치된 V2 Skill·Runtime이 아니라 디자인 탐색·부분 선택의 외부 연구 근거입니다. 현재 전체 디자인 흐름은 Draft Recipe와 Section Trace까지 증명됐고, 승인 Recipe 기반 실제 제품 구현→독립 Fidelity 검증→사용자 최종 승인→Version Restore는 아직 `not_proven`입니다. 새 세션은 `wiki/DESIGN_WORKFLOW_EVIDENCE_AUDIT_2026-08-20.md`의 첫 누락 Handoff부터 이어가며, 추가 조사는 `wiki/DESIGN_WORKFLOW_RESEARCH_HANDOFF_2026-08-20.md`를 그대로 사용합니다.
- 디자인 E2E 구현 Handoff는 2026-08-20 고정 Hash와 격리 Base Commit으로 생성됐습니다. 현재 첫 Blocker는 Handoff가 아니라 `antigravity_execution`이며 CLI Chat 명령 호환 오류 때문에 제품 파일은 0개입니다. Codex 대체 구현으로 이 단계를 PASS 처리하지 말고 `pm3-artifacts/design-flow-e2e-v1/execution-attempt.json`에서 이어갑니다.
- 디자인 E2E를 나중에 재개할 때는 `wiki/DESIGN_FLOW_E2E_CONTINUATION_2026-08-21.md`를 읽고, 격리 저장소·고정 Hash·첫 Blocker를 재확인한 뒤 그 문서의 다음 작업 하나부터 이어갑니다.
- `Interview Me(인터뷰 미)` 원본 Skill Trial은 2026-08-20 사용자의 당시 결정으로
  `discarded_by_user`였고 전역 Skill·Core Registry에는 연결되지 않았습니다. 이 과거
  판정은 유지합니다. 2026-08-21 사용자는 **V2가 만드는 모든 새 제작을 인터뷰로
  시작**하도록 새 결정을 내렸습니다. 이는 원본 Skill의 무조건 자동 실행이 아니라
  PM5가 소유할 V2 전용 `인터뷰 우선 제작 시작 계약`입니다. 새 프로젝트는 전체,
  큰 변경은 짧게, 작은 수정은 명확하면 생략하며, 출력은 Versioned Intent Packet과
  `제작 범위 확인서`입니다. Runtime 구현·Core 연결은 아직 `not_implemented`입니다.
  과거 Trial 근거는 `wiki/INTERVIEW_ME_CAPABILITY_LAB_REPORT_2026-08-20.md`, 새 회의
  결정은 `wiki/DESIGN_AND_EDITOR_MEETING_2026-08-21.md`를 사용합니다.
- 새 세션은 위 문장을 그대로 믿지 말고 `CURRENT_STATE.md`와 해당 증거 파일을 현재 SHA에서 다시 확인합니다.
- V2 엔지니어링 운영 모델의 초기 비교 조사는 완료됐으며 `Harness-first, Spec-guided, Eval-driven, Human-approved, Loop-assisted`를 현재 기본 구조로 사용합니다. 업계 절대 최선이라는 주장, 자동화 Runtime, 실제 프로젝트 반복 효과는 `not_proven`입니다. 상세 기준은 `wiki/V2_ENGINEERING_OPERATING_MODEL.md`, 조사 근거는 `wiki/V2_ENGINEERING_METHOD_RESEARCH_2026-08-21.md`를 사용합니다.

## 공식 사실을 바꾸는 순서

`작업 → 실제 검증 → 사용자 승인 → Wiki·세션 공통계약 반영 → Commit → Push`

Push하지 않은 로컬 Commit은 GitHub `main`의 공식 상태가 아닙니다. Commit하지 않은 Obsidian 문서는 다른 세션의 공식 기억이 아닙니다.
