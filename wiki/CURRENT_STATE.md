# Current State

2026-08-30 수익화·범용성 회의는 `Memory Story`와 `Knowledge Story`의 좁은 비교 Pilot로 종료했습니다.
독립 도메인을 제품·자료·결제의 본체로 두고 네이버 카페는 사례·지식, 카카오톡은 공지·재방문,
나머지 채널은 홍보로 사용합니다. `V2 Story Core`는 새 Orchestrator가 아니라 기존 Core 아래의 공통
제품 계층이며, 전자명함에서 발생한 반복 수정은 Product Contract·제품별 Adapter·Recipe·Verifier·
State Matrix·전체 회귀검사로 흡수합니다. 공식 계약은
`wiki/V2_STORY_PILOT_AND_CORE_COMPLETION_CONTRACT_2026-08-30.md`입니다. 현재 상태는
`approved_plan / implementation_not_started / revenue_not_proven`이며 Story 제품·결제·수익 PASS가
아닙니다.

2026-08-30 회의에서 V2 MVP의 남은 핵심을 `초기 모델 → 제품 계약 → 제품 조립 → Product Harness
→ PM6 → 배포·운영 확인·복구` 연결로 확정했습니다. 새 PM·Workflow 엔진·외부 패키지는 추가하지
않고, 기존 Product Contract·Registry·검증기를 사용하는 제한형 제품 조립기를 구현했습니다.
전자명함 Profile 하나에서 등록된 Core Content·Portrait Composer·Theme·QR Adapter와 기존
Product Contract·Portrait·PM6 Verifier의 기능·Gate Coverage를 결정적으로 연결합니다. Profile
중복, 미등록 제품, Adapter 증거 누락 Fixture는 `BLOCKED`를 확인했습니다. 이는 전자명함 단일 제품의
조립 계약 증거이며 다른 제품 범용 Runtime이나 배포 완료 증거가 아닙니다. PM5 시험 범위와 Visual
Target은 기존 사용자 승인 증거를 Product Contract에 동기화했습니다. 2026-08-30 사용자가 로컬 전자명함 1차 결과를 최종 승인해 PM5·PM6는 `completed_locked`이며, 실제 정보·공개 주소·QR·NFC 배포는 별도 범위로 유예했습니다.

2026-08-29 PM5 전자명함 시험 제작 범위를 사용자 승인 후 실제 제품 Runtime까지 연결했습니다. 테마 6종, 사용자 지정 색상, 이전 테마 복원은 `state/electronic-card-product-state.json`과 Core Action으로 저장·복구됩니다. 인물 합성은 일반 테마에서 부드러운 배경 면과 가장자리 그림자를 사용하고, 강한 대각선은 라임 편집형에만 제한합니다. PM5 의도·범위와 제품별 Core 연결의 기술 검사는 PASS이며, 이는 전자명함 제한 증거로 임의 프로젝트 범용 제작 Runtime을 뜻하지 않습니다. 실제 정보·공개 주소·문자 미리보기·QR·NFC·배포 전환 기준은 [[ELECTRONIC_BUSINESS_CARD_OPERATION_AND_DEPLOYMENT]]를 사용합니다.

2026-08-26 사용자 결정에 따라 `v2-content-reference-radar`의 기본 탐색 형식은 Instagram 카드뉴스·슬라이드와 Threads 공개 글입니다. Shorts·Reels는 `marketer_video` 모드에서만 사용합니다. 기존 Instagram 영상 3건 순위화 증거는 삭제하지 않고 마케터용으로 분류했으며, 현재 `#바이브코딩` 카드뉴스·정적 게시물 후보 5건을 기본 Reference 후보로 등록했습니다. 후보 등록은 사용자 채택이나 제품 적용이 아닙니다.

2026-08-26 `v2-content-reference-radar` Skill을 추가해 YouTube·Instagram·Threads의 공개 콘텐츠 후보를 V2 형식으로 중복 제거·플랫폼 내부 순위화·한글 요약하고 사용자의 `채택·보류·폐기`로 넘기는 최소 계약과 결정형 Fixture를 PASS했습니다. 로그인된 Aside Browser에서 `#바이브코딩` Instagram 공개 게시물 10건과 영상 5건을 확인했고, 영상 3건은 공개 좋아요·댓글·리포스트를 읽어 Instagram 내부 순위화까지 Runtime PASS했습니다. Threads는 로그인 없이 공개 검색 후보 5건과 본문 3건을 읽어 수집 PASS했지만 검색 화면 숫자의 지표 이름이 노출되지 않아 실제 순위화는 `not_proven`입니다. 참고한 `haeun2525/trend-radar`에는 License 파일이 없어 소스는 재사용하지 않았고 구조만 참고했습니다. Cookie·Token·비공개 콘텐츠는 저장하지 않았습니다.

2026-08-26 PM4 Evidence Router의 단일 주제 제한 Runtime을 추가했습니다. `AI 바이브코딩 웹 디자인 Reference` 한 건에서 기존 Artifact를 시각 Reference·실사용 반응·구현 재료·공식 사실의 네 역할로 분배하고 Instagram·Threads·YouTube·GitHub·공식 웹 5개 플랫폼에서 자료 10개를 수집했습니다. 최초 화면은 설명이 빈약하거나 영어뿐인 자료도 노출해 사용자에게 거절됐습니다. 이후 전자명함 Reference와 같은 Gallery 구조로 바꾸고, 한국어로 내용과 참고 이유를 설명할 수 있는 4개만 표시하며 사용자 행동을 `원문 보기·채택`으로 줄였습니다. 나머지 6개는 수집 증거로 보존하되 선택 후보에서는 제외합니다. 실제 Browser에서 모바일 단일 열, 채택 토글과 Console 오류 0건을 확인했습니다. 채택 상태는 Browser Local Storage에서 Core 상태 파일로 옮겼고, 시험 채택 저장 → Dashboard 서버 재시작 → 복원 → 시험값 제거까지 PASS했습니다. 이 결과는 한 주제의 연결 증거이며 임의 주제 범용 수집, Core 자동 승인, 제품 자동 적용, 사용자 PM4 최종 PASS를 뜻하지 않습니다.

새 Codex·Antigravity 세션은 반드시 [[SESSION_START_CONTRACT]]를 가장 먼저 읽고, 현재 Worktree·GitHub `origin/main`·Obsidian Vault의 SHA를 구분해 보고합니다. 직접 확인하지 않은 기능·상태·PASS·동기화·복구는 `확인 필요` 또는 `not_proven`으로 기록하며, 이 규칙이 환각을 0으로 보장한다고 표현하지 않습니다.

V2의 현재 엔지니어링 운영 방향은 [[V2_ENGINEERING_OPERATING_MODEL]]의 `Harness-first, Spec-guided, Eval-driven, Human-approved, Loop-assisted`입니다. 초기 방법 비교는 [[V2_ENGINEERING_METHOD_RESEARCH_2026-08-21]]에 기록했습니다. 첫 읽기 전용 PM 전환 증거 검사기는 정상·누락·충돌 Fixture와 기존 잠금·증거 Guard 회귀검사를 PASS했고, 같은 역할의 기존 기본 자동화가 없어 사용자가 `stable_default`로 채택했습니다. PM 자동 PASS·파일 자동 수정은 금지하며 다른 PM Manifest 일반화와 실제 프로젝트 반복 효과는 아직 `not_proven`입니다.

GitHub Spec Kit `v0.16.5`를 전역이 아닌 `/home/user/바탕화면/v2_spec_kit_pilot`에 격리 설치해 가짜 요구사항으로 시험했습니다. 사용자의 변경·유지·완료·회귀 의미가 Spec·Plan·20개 Task까지 보존돼 `PASS_WITH_FIX`이지만 작은 수정에 전체 흐름은 과합니다. 사용자는 작은 수정용 `Spec Lite`와 새 프로젝트·큰 기능용 `Spec Full` 분리를 승인했습니다. Repo-local `V2 Spec Adapter`를 만들고 `요구사항 창을 늘려줘` 요청의 원문·대상·보존 범위·완료 기준·회귀검사를 생성해 구조 검사와 읽기 전용 검증을 PASS했습니다. 이는 Core Runtime 자동 연결이나 실제 제품 구현 완료를 뜻하지 않습니다. 상세 증거는 [[SPEC_KIT_V2_ADAPTER_PILOT_2026-08-21]]을 사용합니다.

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

디자인 탐색·채택·구현·수정·검증의 단일 공식 원본은 [[DESIGN_SYSTEM]] · [GitHub 링크](DESIGN_SYSTEM.md)입니다. 흩어진 과거 디자인 문서는 증거로 보존하되 새 결정과 충돌하면 현재 Commit의 디자인 시스템을 우선합니다.

현재 `M7 — PDF 도면 스탬프 MVP E2E`까지 구현·독립 검증·사용자 승인·Result Commit·Rollback/Restore가 완료됐습니다. M7 공식 Run은 `run-c0a968f3`, 제품 Result Commit은 `3b592c8`입니다. 이로써 `AI OS V2 Core MVP M1~M7`은 검증 완료·동결 상태입니다. Post-MVP 설계는 [[POST_MVP_PM0_PM6_BASELINE]]의 `PM0~PM6`으로 완료됐으며 완료 범위와 미구현 항목은 [[POST_MVP_DESIGN_COMPLETION_REPORT]]에 기록합니다. PM0·PM1·PM2는 기존 판정대로 PASS, PM3은 사용자 조건부 통과와 PM6 재검증 조건으로 기존 증거를 유지합니다. PM4는 전자명함 실제 요청의 제한 범위에서 인터뷰·수집·Reference 보충·사용자 선택·Design DNA·전체 화면 Visual Target 인계까지 사용자·Runtime 검증으로 통과했습니다. 전자명함 PM5·PM6는 최신 전체 회귀검사와 사용자 최종 승인을 거쳐 2026-08-30 `completed_locked`로 전환했습니다. 실제 배포·다른 제품 범용 Runtime은 아직 `not_proven`입니다. Codex·외부 Skill 단독 결과는 정식 V2 결과가 아니며, Core가 입력·Artifact·검증·Version·Restore를 재현해야 한다는 공통 제작 계약을 유지합니다. `run-ef4986d7`의 기존 Preview v1과 PM1의 실패 Pilot은 당시 거절 판정 그대로 보존하며 구현 입력으로 사용하지 않습니다.

2026-08-29에는 전자명함 전용 `core-design-harness`를 공식 입력에서 제외하고, 기존 PM4 승인
Handoff·Design DNA·Visual Target과 PM5 Intent를 `run-electronic-card-official-v1`로 연결했습니다.
Core가 생성한 `draft-design-recipe.json`은 방향·화면·행동·사진 처리·반응형·금지 재해석과 입력
Hash를 잠급니다. 당시 PM5 Fixture 범위는 `pending`이었으나 이후 사용자가 시험 범위와 최종 결과를
승인했고, 최신 회귀검사를 거쳐 PM5·PM6는 `completed_locked`입니다. 실제 정보·공개 주소·QR·NFC
배포와 다른 제품 범용 Runtime은 여전히 별도 범위이며 `not_proven`입니다.

2026-08-24 PM4 프로젝트 수집 MVP는 전자명함 시험에서 `인터뷰 → 소셜 사용 근거 → 방향 5개 → GitHub 구현 재료 → Core 추천 → 사용자 시험 선택 → 제작 가능 확인서`까지 연결했습니다. Reddit 3건·YouTube 2건·Threads 3건과 GitHub 구현 재료 5건은 실제 Link로 보존했고, Instagram은 로그인 세션 미연결로 0건입니다. 후보 보존, `다음` 클릭 후 확인서 자동 생성, 서버 재시작 복원, 자동 설치·구현 차단은 PASS했습니다. 2026-08-25 사용자가 1번 `QR·NFC로 바로 연결하는 명함`을 최종 재확인해 대화 기록과 Handoff Artifact의 충돌을 해소했습니다. Core의 3번 추천은 비교 근거로만 보존하며 자동 선택으로 해석하지 않습니다. 2026-08-26 사용자는 후속 3번 시각 시안 수정본을 `보류`했습니다. 이후 기존 PM4에 검색 기반 시각 Reference Adapter를 추가해 고정 Seed 없이 전자명함 명세에서 공개 Gallery 검색어 3개를 생성하고 화면 8개를 출처·이미지 Hash·한글 요약·복제 금지 항목과 함께 수집했습니다. 같은 경로는 인테리어 커뮤니티 Fixture에서도 별도 화면 8개를 수집해 Core 연결됐고, 출처 하나의 의도된 실패가 다른 자료를 막지 않는 것도 PASS했습니다. Core 조회·판정 저장·서버 재시작 조회·제품 자동 적용 차단 역시 Runtime PASS입니다. 2026-08-26 `추가 탐색` Refill Loop를 Core Action으로 연결해 기존 12개를 보존하고 인접 검색어 5개로 새 후보 5개만 추가했습니다. URL·SHA-256·이미지 dHash 유사도 중복 제거, 채택 특징 우선·폐기 특징/유사 화면 제외, 판정 보존, 3개 미만 확보 시 원본 유지, 디자인/기능 자료 분리 표시를 검사했습니다. 기능 자료는 기존 GitHub·YouTube 근거를 별도 화면으로 재사용합니다. 사용자는 총 17개 중 6개 시각 Reference를 채택했고, 선택 결과는 `visual-reference-selection-handoff.json`으로 고정했습니다. 이 전달서는 PM1 디자인 방향 정리의 입력이며 DNA·Visual Target·구현 승인은 아닙니다. 사용자 URL·이미지는 등록되면 최고 우선순위지만 입력 UI는 아직 없고, Instagram·Threads 로그인 수집도 PM4 최종 보류 상태입니다. 이는 두 입력과 현재 공개 Gallery·등록 서비스 Adapter의 제한 증거이며 임의의 모든 주제, Reference 품질 승인, Visual Target 승인, 구현을 증명하지 않습니다. 로그인 세션 관리·Instagram 수집과 사용자 PM4 최종 PASS는 PM4 마지막 검증 항목으로 잠급니다. 과거 로컬 우선 Pilot 증거는 [[PM4_LOCAL_FIRST_COLLECTOR_PILOT_2026-08-21]]을 사용합니다.

사용자 개인용 Codex App Automation `v2` (`V2 일일 탐색 브리핑`)는 매일 오전 7시 로컬 실행으로 별도 유지합니다. 공용 `daily-discovery-briefing` Candidate Module은 고정 주제가 아니라 사용자가 `조사 주제·시간·GitHub/Reddit/YouTube/Threads/Instagram 플랫폼`을 정하는 범용 예약 조사 Module Draft로 수정했습니다. `briefing.config.update`는 Core 승인 요청만 생성합니다. 수정된 Module의 Core→Automation 연결·실제 수집·사용성은 사용자 요청에 따라 PM 마지막에 검증하며 현재 `not_yet_verified`입니다.

M2 공식 검증 Run은 `run-05dbfc27`입니다. `execution_mode: skills`, `workflow_run_id: null`인 동일 Run에서 Specify, 승인 전 Plan 차단, Spec 본문 수정과 Version 증가, 승인, Plan Artifact 생성과 새 프로세스 재조회를 확인했습니다.

M3에서도 같은 `run-05dbfc27`을 유지했습니다. UI UX Pro Max와 frontend-app-builder로 모바일 우선 Option C v2를 생성하고 Browser 기술 검증을 통과했습니다. 사용자는 디자인 마감에 `needs_improvement`를 남겼지만 M4 파이프라인 시험 입력으로 승인했습니다. 상업 디자인과 Reference 승인은 아닙니다.

공식 `speckit-tasks` Skill로 T001~T047의 `tasks.md`를 한 번 생성했고 Spec·Plan·Option C 정합성을 확인했습니다. Antigravity용 M4 Handoff는 실제 실행 범위를 5개 최소 묶음으로 정리했습니다. 제작 프로젝트 M3 기준점은 Commit `2554340`입니다.

M4에서는 Antigravity가 Vite·TypeScript 병원 웹을 구현하고 Codex가 390px·430px·1440px Browser 흐름, Typecheck, Build, Console, 비저장 동작을 독립 검증했습니다. 사용자가 파이프라인 테스트를 승인한 뒤 Result Commit `c970352`를 생성했고 별도 임시 worktree에서 기준 Commit `2554340`과 Result Commit의 Rollback·Restore를 재현했습니다. 당시 비차단 후속 개선으로 남긴 390px 제목 줄바꿈은 M6에서 해결했으며 상업 디자인과 Reference 승인은 계속 `false`입니다.

M6에서는 Quick Change Run `run-fa8b4386`으로 `HERO-01`만 수정했습니다. 제품 소스 변경은 `src/styles.css`의 국소 규칙 2개뿐이며 390px·430px 줄바꿈, 1440px 회귀, 메뉴·의료진·예약 오류·완료·복귀 흐름을 확인했습니다. 사용자 판정과 Codex 검증은 모두 `pass`이며 Result Commit은 `e2625bb`입니다. 기준 Commit `c970352`와 Result Commit을 별도 worktree에서 각각 Build하여 Rollback·Restore를 재현했습니다. 이는 자연어를 통한 AI 부분 수정의 검증이며 사용자가 Preview에서 직접 값을 조절하는 편집 패널이 구현됐다는 의미는 아닙니다.

`run-3b0ffae8`은 다른 Agent의 변경이 섞인 `diagnostic_failed` 기록이며 M2 PASS 증거로 사용하지 않습니다. 기존 실패 Run도 M2 PASS 증거가 아닙니다.

## Spec Kit 및 Core 상태

- ✅ 검증됨: V2 Core가 Run, Gate와 상태를 소유하는 단일 Orchestrator로 동작합니다. 사용자 표시명은 `Zeus`이며 별도 AI 모델이 아닙니다.
- ✅ 검증됨: Spec Kit은 `speckit-specify`, `speckit-plan`, `speckit-tasks` Skill과 Markdown Artifact 생성을 담당합니다.
- ✅ 검증됨: `specify integration upgrade codex`로 누락된 공식 관리 Skill 7개를 복구했고 integration status의 Missing/Modified managed files가 모두 0입니다.
- ✅ 검증됨: Spec Kit Workflow Run, Gate Resume와 상태 동기화는 M2 기본 실행 경로에서 제외됐습니다.
- ✅ 검증됨: Artifact가 없으면 Agent 종료코드가 `0`이어도 실패로 판정합니다.
- `workflow_run_id`는 과거 Workflow 증거를 보존하기 위한 nullable 선택 필드입니다.

## 역할과 단독 쓰기 규칙

- Codex는 M2부터 내부 설정, Core, Run, Gate, Git, Skill 연결과 기술 검증을 담당합니다.
- Antigravity는 실제 웹·앱·화면·기능 구현을 담당하며 M4 병원 웹 구현을 완료했습니다.
- 동일 Run은 한 시점에 쓰기 담당자 한 명만 허용합니다.
- 구현 Agent의 완료 보고는 공식 사실이 아니며, Codex 검증과 사용자 승인을 거친 변경만 Git에 저장합니다.
- 디자인 작업에서 Codex는 디자인 총괄 절차·작업 지시·독립 검증을 담당하고, Antigravity는 승인된 Visual Target·Design Recipe를 실제 제품으로 구현하며, 사용자가 최종 채택·수정·폐기를 판정합니다.

## 공식 기억 상태

- PM0~PM6 기준을 GitHub에 게시한 Commit은 `f1d6aa9498ab119d8752bca9565aa15cc59370a4`이며, 2026-08-17 정합성 확인 당시 원격 `origin/main` HEAD와 작업 브랜치 HEAD가 이 Commit으로 일치했습니다.
- 과거 Run의 `memory.official_commit`과 `v2_workspace.head`는 해당 Run이 생성·검증된 시점의 Base Memory와 작업 기준점입니다. 예를 들어 `72db6dc2fa5cde72c78cfd66184d13cc57ffc5aa`는 일부 M6·M7 Run의 역사적 기준이며 현재 원격 HEAD를 뜻하지 않습니다.
- 제작 프로젝트의 M3 기준점 `2554340`, M4 Result Commit `c970352`, M6 Result Commit `e2625bb`, M7 Result Commit `3b592c8`은 각 제품 저장소의 검증 증거입니다. AI OS V2 Core 저장소의 `origin/main`과는 별도 Commit 계보입니다.
- 원격 최신 HEAD는 세션 시작 시 `git fetch origin` 후 재확인하며, 과거 Run의 기억 값을 현재 HEAD로 덮어쓰지 않습니다.

## PM4 AI 코딩 채널 Feed 연결 (2026-08-26)

- 국내: 조코딩, 노마드 코더, 코딩애플
- 해외: Fireship, AI Jason, Cole Medin, IndyDevDan
- 공식 YouTube Atom Feed 7개가 실제 Runtime에서 모두 연결됐고, 기본 Reference 모드로
  최근 30일 후보 10개를 수집했습니다.
- 화면 편중을 줄이기 위해 관련 후보가 있는 채널마다 한 건을 먼저 배치한 뒤 최신순으로
  채우며, 기본 Reference 모드에서는 Shorts를 제외합니다.
- Feed 연결은 PASS지만 채널별 품질 채택·자동 제품 적용·Instagram/Threads 채널 연결·
  모든 주제에서의 범용 적합성은 아직 `not_proven`입니다.

## 다음 단계

- 2026-08-18 최종 Post-MVP 순서는 `PM0 운영환경·Capability Lab 준비 → PM1 디자인 전략·탐색·채택 → PM2 조립식 제작 보드 → PM3 부분 수정·Motion Adapter → PM4 조사·Design Intelligence → PM5 사용자 의도·범위·자산 정합성 → PM6 전체 통합·품질·복구 검증`입니다.
- 설계 상태는 `completed`, PM0 상태는 `pass_with_user_deferred_backup`, PM1·PM2 상태는 `pass`, PM3은 `user_pass_with_deferred_pm6_revalidation`, 다음 진행 가능 단계는 PM4입니다. 정적 Reference Board, 이를 이용한 `큰 미리보기 작업실` Pilot, 실제 화면 5개의 구역·속성을 선택하는 Visual Companion, Google Stitch 생성 결과는 사용자가 기존 UI UX Pro 중심 방식보다 느리거나 결과가 낮다고 판정했습니다. 이 결과들은 `rejected_and_preserved` 증거이며 제품·Registry·PM2에 적용되지 않았습니다. Visual Companion용 Route·API는 격리 Pilot 증거로만 보존하며 Core 공식 기능으로 간주하지 않습니다.
- PM1 기본 방식은 `쉬운 요청 → 기존 성공 Recipe·Block 우선 확인 → 필요할 때만 제한 조사 → UI UX Pro 규칙·품질 검사 → 실제 V2 데이터 Visual Target 하나 → 부분 수정 → 승인 또는 거절 → 거절 시 대안 하나`로 PASS했습니다. 완료 증거는 [[PM1_COMPLETION_REPORT_2026-08-18]]을 사용합니다.
- Reference는 출처·라이선스·사용 Section을 남기는 내부 보조 근거로 유지하고, 전체 목록·구역 선택·속성 선택은 사용자가 요청할 때만 제공하는 선택 기능으로 내립니다. `UI Remix` 연구 근거는 보존하지만 V2 기본 Workflow로 강제하지 않습니다.
- 반복 ImageGen A/B/C와 후보별 Code Preview는 기본 흐름에서 제외합니다. Visual Target과 수정 전후는 동일 Viewport·V2 데이터·화면 상태·Theme·확대 비율·Motion 시점에서 확인합니다.
- PM2는 `V2 Core → ui-state(JSON) → UI → ui-action → V2 Core` 경계와 Slot·Module을 실제 구현하는 조립 기능 Gate입니다.
- 2026-08-19 PM2에서 PDF 결과와 동네 병원 웹을 검증된 프로젝트 Module로 등록했습니다. 목록에서 선택한 결과 하나만 Preview하고 해당 프로젝트 기능만 표시합니다. Core `ui-state → UI → ui-action → Core`, 선택 상태 유지, 비활성, 오류 격리, 복원, 금지 Action·다른 Project 차단을 검증했으며 사용자가 PASS했습니다. PM2는 `completed_and_locked`, 다음 단계는 PM3입니다. 증거는 [[PM2_FIRST_MODULE_PILOT_REPORT_2026-08-19]]과 `pm2-artifacts/module-registry-v1/core-verification.json`을 사용합니다.
- 디자인 Reference 수집은 PM1, 일반 자료·병목 조사는 PM4에서 요청 시 제한형 Workflow로 수행합니다.
- 2026-08-20 디자인 공급원 비교에서 사용자 선호와 채택·보류 판정을 기록했습니다. 단일 우승자를 고르지 않고 Design MCP·21st.dev·UI UX Pro MCP·Creative Tim UI·Aceternity/React Bits처럼 역할이 다른 공급원을 조합합니다. 방향 3개는 빠른 비교 시안이고 실제 Code Preview는 선택 조합 하나만 제작합니다.
- `V2 Design Director`의 Reference Flow 자동화가 사용자 채택 Trial 5개를 Draft Design Recipe로 컴파일하고 실제 Preview의 5개 Section 출처와 SHA-256을 대조해 PASS했습니다. 이는 Reference 추적 자동화 증거이며 Core 자동 선택·제품 적용·PM3 편집 뒤 보존·교차 프로젝트 재사용 증거는 아닙니다. 상세 내용은 [[DESIGN_SUPPLIER_TRIAL_SYNC_2026-08-20]]을 사용합니다.
- PM3 부분수정의 최종 흐름을 [[PM3_PARTIAL_EDIT_FINAL_FLOW_2026-08-20]]에 고정했습니다. 승인 Recipe를 덮어쓰지 않고 새 Draft에서 Viewport·Section을 선택해 마우스로 수정하며, 모든 변경은 Recipe Diff·Preview·경고·권한·반응형·Motion·Reference Trace 검사를 거쳐 새 Version으로 적용됩니다. 실제 고객 결과물 전체 적용과 사용자 PM3 PASS는 아직 남아 있습니다.
- 디자인 탐색·채택 방식은 Double Diamond·Enterprise Design Thinking 및 UI Remix·Misty의 사례 선택·부분 적용 연구와 비교했습니다. 큰 흐름은 정합하지만 V2 고유 명칭과 자동화가 업계 표준이거나 성공이 증명됐다는 뜻은 아닙니다. Design Recipe는 Reference 선택 때 Draft로 시작하고 Visual Target 승인 때 승격합니다. 상세 검토는 [[DESIGN_ADOPTION_METHOD_REVIEW_2026-08-20]]을 사용합니다.
- `V2 Design Director`에 전체 흐름 Evidence Audit 계약을 추가했습니다. 현재는 요청·총괄·공급원 비교·Visual Target·사용자 방향 선택·Draft Recipe·Section Trace까지 근거가 있고, 같은 승인 Recipe를 사용한 실제 제품 구현·독립 Fidelity 검증·사용자 최종 승인·Version Restore는 아직 `not_proven`이므로 전체 흐름 완료 판정은 `BLOCKED`입니다. 상세 판정은 [[DESIGN_WORKFLOW_EVIDENCE_AUDIT_2026-08-20]], 추가 조사 지시서는 [[DESIGN_WORKFLOW_RESEARCH_HANDOFF_2026-08-20]]을 사용합니다.
- 2026-08-20 디자인 흐름 E2E 재검증에서 Recipe·Selection·Visual Target Hash와 격리 Base Commit을 포함한 Antigravity Handoff까지는 `proven`으로 승격했습니다. 그러나 현재 설치본의 CLI `chat` 실행이 `workbench.action.chat.newChat not found`로 실패해 제품 파일이 생성되지 않았습니다. 따라서 첫 Blocker는 `antigravity_execution`, 이후 실제 구현·Codex Fidelity·사용자 최종 승인·Version Restore는 계속 `not_proven`입니다.
- 이 작업의 중단 시점과 정확한 재개 절차는 [[DESIGN_FLOW_E2E_CONTINUATION_2026-08-21]]에 고정했습니다. 새 세션은 제품 구현을 추정하지 말고 격리 저장소의 `product/` 파일 수와 Git 상태부터 다시 확인합니다.
- Addy Osmani의 `Interview Me` 격리 Trial 자체는 PASS했지만 2026-08-20 당시 사용자가
  V2 제품 기능에는 불필요하다고 판정해 원본 Skill은 `discarded_by_user`로 보존합니다.
  2026-08-21 사용자는 이와 별개로 V2의 모든 새 제작을 인터뷰로 시작하는
  `인터뷰 우선 제작 시작 계약`을 승인했습니다. 새 프로젝트는 전체 인터뷰, 큰 변경은
  짧은 인터뷰, 명확한 작은 수정은 생략하며 결과를 `제작 범위 확인서`와 Intent Packet으로
  고정합니다. 이는 회의·설계 결정이며 PM5 Runtime·Core 자동 연결은 아직
  `not_implemented`입니다. [[DESIGN_AND_EDITOR_MEETING_2026-08-21]]을 사용합니다.
- 2026-08-20 실제 검증 증거에 가중치를 둔 V2 현재 성숙도 평가는 `62/100`입니다. Core·PM1·PM2는 강하지만 PM3은 Pilot, PM4~PM6은 미구현 비중이 높고 생산 배포·운영·다중 프로젝트 반복 성공은 `not_proven`입니다. 평가표는 [[V2_OBJECTIVE_EVALUATION_2026-08-20]]을 사용합니다.
- PM1~PM3의 Reference Brief·Reference-first 채택, Versioned Design Recipe·반응형 Override, Module Manifest·Slot Renderer와 제거 가능한 Puck Adapter 경계 설계는 완료됐습니다. PM3에서는 Puck 0.22.4와 React Grid Layout 2.2.4를 격리 Pilot에만 설치해 카드 3개의 구조·배치·속성 편집, 이미지 Slot, 단색·투톤 Palette, 자동 배치·줄바꿈·색상 Draft와 Undo를 검증했습니다. 이는 Core Registry 승격이나 실제 제품 적용 완료를 뜻하지 않으며, 실제 병원 웹 Section 적용·Bundle 지연 로딩·사용자 최종 PASS는 남아 있습니다.
- 2026-08-21 PM3 편집기 확장 인터뷰 11개 항목을 사용자 확인으로 완료했고, 사용자는
  현재 PM3을 `일단 통과`로 판정했습니다. 이는 사용자 흐름 판정이며 기술 완료는
  `not_proven`입니다. 실제 고객 결과물·모바일 390/430·Undo·원본 보존·프로젝트 격리·
  접근성·회귀는 PM6에서 의무적으로 다시 검증합니다. 병원 웹 Draft는 제품 Commit·원본
  Merge 없이 보존합니다. [[PM3_USER_PASS_WITH_PM6_REVALIDATION_2026-08-21]]을 사용합니다.
- 2026-08-21 사용자가 결정한 인터뷰·기존 자산 우선·필요 시 수집·서로 다른 방향 3개·
  선택 후 Design DNA·Visual Target 하나·Recipe·구현·부분 수정·PM6 재검증 흐름을
  PM0~PM6 공식 기준에 재배치했습니다. 문서 정합성은 완료됐지만 Collector·DNA 추출·
  Spec Runtime·편집기 Recipe 연결·전체 E2E는 아직 구현 또는 검증되지 않았습니다.
  [[PM_FLOW_DECISION_ALIGNMENT_2026-08-21]]을 사용합니다.
- 기존 PM1 Preview는 실제 제품 Stack이 아니라 `static_design_evidence_only`로 보존합니다. PM2 실제 보드는 React 19 + Vite를 권장 기반으로 기록하되 PM0 PASS와 구현 승인 전에는 채택·설치로 간주하지 않습니다.
- V2 운영 UI는 PC 전용이며, 390px·430px은 고객 결과물 하나의 모바일 규칙을 회귀검증하는 Viewport입니다.
- 각 PM은 PM PASS·Codex 검증·사용자 PASS·Rollback/Restore 이후 별도 Result Commit 하나로 완료합니다.
- M5의 수집·분석·레시피 선택 Core와 M6의 Quick Change Run·AI 부분 수정·회귀·복구 흐름, 그리고 M7 모바일 PDF 도면 스탬프 `local_product` E2E 구현 및 사용자 검증을 완료했습니다.
- 사용자에게는 `원하는 화면 요청 → 실제 결과 확인 → 진행·부분 수정·다른 방향·현재안 유지·중단·복구`만 기본으로 보입니다. 요청은 쉬운 말로 받고 결과 확인과 행동은 실제 Preview·마우스·간단한 버튼을 우선합니다.
- PM1은 `single_visual_target_with_ui_ux_pro_guard`를 기본 Workflow로 채택했습니다. 이는 PM1 디자인 채택 방식의 PASS이며 PM2 조립 기능이나 PM3 직접 편집 기능의 구현 완료를 뜻하지 않습니다.
- PM1 단일 Visual Target v1 `pm1-v2-dashboard-v1`을 실제 V2 데이터와 기존 선호 화면을 바탕으로 생성했습니다. UI UX Pro의 Grid·Typography·밀도·접근성 규칙만 채택하고 맞지 않는 Landing Pattern·보라/분홍 Palette·GSAP 제안은 거절 이유와 함께 기록했습니다. shadcn `sidebar-07`과 `dashboard-01`은 설치 없이 Registry 원본 Hash·파일·의존성을 확인했으며, `sidebar-07`만 PM2 구현 후보입니다. 사용자는 `오케이 이걸로하고`라고 Visual 방향을 승인했고 Design Finish Audit은 상태 표시·중복 문구·대비·Core 데이터 연결을 구현 시 수정하는 조건으로 `PASS_WITH_FIX`입니다. 이는 PM1 전체 편의성 PASS나 PM2 구현 승인을 대신하지 않습니다.
- Repo-local `V2 Capability Lab` Pilot은 공개 GitHub 후보 Clone·정적 감사·가짜 Fixture·
  Bubblewrap 격리 실행·사용자 승인 기반 채택/폐기와 Registry 기록을 구현했습니다. 실제
  시험에서 V2 저장소 비노출, Credential 0개, 별도 HOME, 기본 Network 차단과 승인 없는
  채택·폐기 거부를 확인했습니다. `Design Intelligence` Collection은 공개 후보 8개의
  GitHub 최신성·License·역할과 `채택·보류·폐기` Action을 생성했습니다. 이는 PM4 전체
  구현 PASS가 아니라 PM1 Worktree의 선행 Pilot이며 Core·제품에는 연결되지 않았습니다.
- 2026-08-18 최초 구현 감사에서 Design Intelligence는 `fixture_ui`였고 후보 8개가 Python 코드에 정의돼 있었습니다. 기존 V2 Collector Adapter, 성공 Recipe 우선 검색, 자동 격리 시험 Queue와 결과 회수는 아직 구현되지 않았습니다. Capability Lab은 `impeccable`과 `taste-skill-v1`을 실제 Bubblewrap으로 시험한 `isolated_execution` 수준이며 감사 당시 Registry 채택 수는 0개였습니다. `v2-design-finish`는 호출 가능한 Repo-local Skill과 실행 증거가 있지만 V2 Core·Design Recipe와 자동 연결된 기능은 아닙니다.
- 2026-08-18 환경 갱신으로 8개 후보 Catalog를 `plugins/v2-capability-lab/registry/candidate-catalog.json`으로 분리하고 PM·선행 Gate·설치 허용 상태를 기록합니다. `impeccable`은 기존 격리 시험과 사용자 만족 증거를 근거로 비활성 Adapter로 채택했으며 Core 쓰기·비공개 프로젝트 접근·자동 활성화는 금지됩니다. `tools/pm-capability-preflight`는 PASS했고 PM1 환경은 `READY`입니다. 상세 증거는 [[PM1_CAPABILITY_ENVIRONMENT_REPORT_2026-08-18]]을 사용합니다.
- PM1의 직접 조립은 구조 Draft·격리 Preview이며 실제 Module 장착과 상태 저장은 PM2 범위입니다. PM5가 구현되기 전 PM1~PM4에서는 수동 Intent Receipt·Scope Lock을 선행 Gate로 사용합니다.
- PM3은 Card Drag & Drop, 위·아래 이동, 허용 Slot 이동, 제한된 크기·여백·글자 조절, Manifest 경계 안의 복제와 Draft 제거, Undo·Redo와 Core Version Restore를 포함합니다.
- 실제 휴대폰 연결은 고객 결과물 검증을 위한 선택형 Adapter입니다. USB + `adb reverse`를 기본 후보로 하고 실패 시 390·430 Browser Preview로 전환하며 Cloud Sync·개인 파일 동기화·무선 외부 공개는 포함하지 않습니다.
- 자동 인터넷 크롤러, 별도 수집 서버·DB, 학습기, Dashboard UI와 Multi-Agent는 M5 범위에 포함하지 않습니다.
- 디자인 레시피는 현재 설치된 Product Design·frontend-app-builder·UI UX Pro Max를 우선 재사용합니다. UI UX Pro Max는 규칙 제안·품질 검사만 담당하며 최종 디자인을 결정하지 않습니다. Taste는 미검증 후보이고 Google Stitch는 이번 사용자 비교에서 기본 방식으로 거절됐으므로 새 증거와 별도 승인 전 재도입하지 않습니다.
- Google Drive는 외부 Backup 후보이지만 사용자가 이번 PM1 시험에서는 Backup·Restore 검증을 유예했습니다. NotebookLM은 PM1·PM4의 수동 출처 비교 보조, Google Stitch는 PM1의 선택형 생성 후보, Lighthouse·PageSpeed Insights는 PM2 이후 고객 결과물 검증 도구로만 평가하며 Core 필수 의존성으로 연결하지 않습니다.
- Supabase의 Auth·Postgres·RLS·Migration·검증·배포 흐름은 병원 파일럿에 추가하지 않고, 데이터 저장이 승인된 후속 프로젝트의 조건부 Full-stack 레시피 후보로 둡니다.
- M5의 공식 분석 요청은 `PDF 도면 위에 스탬프를 배치·이동·크기 조절하고 원본을 보존한 채 새 PDF로 저장`이며, 구현이나 패키지 설치 없이 최대 두 개의 현실적인 레시피와 다음 작업 하나만 제시합니다.
- M7은 M5에서 선택한 레시피로 모바일 PDF 도면 스탬프 `local_product`를 E2E 검증 및 승인 받았습니다.
- 다른 세션은 [[POST_MVP_PM0_PM6_BASELINE]]에서 시작합니다. [[POST_MVP_FINAL_DESIGN]], [[GPT_SESSION_CHANGE_CONTINUATION_HANDOFF]], [[PM1_HANDOFF]]의 이전 번호 체계는 역사적 기준으로만 사용합니다.
# PM4 전자명함 외부 시안 Core 연결 — 2026-08-26

채택 Reference 6개에서 전자명함 Design DNA를 작성하고, Codex Product Design `ideate`와 OpenAI ImageGen으로 만든 외부 시안 5개를 전자명함 Artifact에 저장했습니다. 이 이미지는 Core가 생성한 결과가 아니며 `core_generated: false`로 고정합니다. Core는 이미지 Hash·생성 출처·DNA·교체 가능 데이터 계약·사용자 선택만 관리합니다. 실제 Runtime에서 후보 5개 표시, 선택·취소, Dashboard 재시작 후 선택 복원, 시험 상태 원상복구, 제품 자동 적용 차단을 PASS했습니다. 사용자는 2번 `editorial_professional` 방향과 이를 확장한 8개 화면 Visual Target을 승인했습니다. 방문자 화면 외에 소유자용 이름·사진·연락처·테마·행동 순서 편집을 포함하며, 사진은 반명함·상반신·전신·가로 인물사진을 판정해 유형별 구도를 추천하되 원본 보존·모바일/PC Crop 분리·수동 위치 조정·얼굴 변형 금지를 계약으로 고정했습니다. 이 결과는 디자인 승인과 PM4 인계 증거이며 실제 사진 보정 Runtime·제품 구현·배포·PM4 최종 PASS는 아직 `not_proven`입니다.
