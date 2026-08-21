# Current State

새 Codex·Antigravity 세션은 반드시 [[SESSION_START_CONTRACT]]를 가장 먼저 읽고, 현재 Worktree·GitHub `origin/main`·Obsidian Vault의 SHA를 구분해 보고합니다. 직접 확인하지 않은 기능·상태·PASS·동기화·복구는 `확인 필요` 또는 `not_proven`으로 기록하며, 이 규칙이 환각을 0으로 보장한다고 표현하지 않습니다.

V2의 현재 엔지니어링 운영 방향은 [[V2_ENGINEERING_OPERATING_MODEL]]의 `Harness-first, Spec-guided, Eval-driven, Human-approved, Loop-assisted`입니다. 초기 방법 비교는 [[V2_ENGINEERING_METHOD_RESEARCH_2026-08-21]]에 기록했습니다. 첫 읽기 전용 PM 전환 증거 검사기는 정상·누락·충돌 Fixture와 기존 잠금·증거 Guard 회귀검사를 PASS했고, 같은 역할의 기존 기본 자동화가 없어 사용자가 `stable_default`로 채택했습니다. PM 자동 PASS·파일 자동 수정은 금지하며 다른 PM Manifest 일반화와 실제 프로젝트 반복 효과는 아직 `not_proven`입니다.

GitHub Spec Kit `v0.16.5`를 전역이 아닌 `/home/user/바탕화면/v2_spec_kit_pilot`에 격리 설치해 가짜 요구사항으로 시험했습니다. 사용자의 변경·유지·완료·회귀 의미가 Spec·Plan·20개 Task까지 보존돼 `PASS_WITH_FIX`이지만 작은 수정에 전체 흐름은 과합니다. 사용자는 작은 수정용 `Spec Lite`와 새 프로젝트·큰 기능용 `Spec Full` 분리를 승인했습니다. Repo-local `V2 Spec Adapter`를 만들고 `요구사항 창을 늘려줘` 요청의 원문·대상·보존 범위·완료 기준·회귀검사를 생성해 구조 검사와 읽기 전용 검증을 PASS했습니다. 이는 Core Runtime 자동 연결이나 실제 제품 구현 완료를 뜻하지 않습니다. 상세 증거는 [[SPEC_KIT_V2_ADAPTER_PILOT_2026-08-21]]을 사용합니다.

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

디자인 탐색·채택·구현·수정·검증의 단일 공식 원본은 [[DESIGN_SYSTEM]] · [GitHub 링크](DESIGN_SYSTEM.md)입니다. 흩어진 과거 디자인 문서는 증거로 보존하되 새 결정과 충돌하면 현재 Commit의 디자인 시스템을 우선합니다.

현재 `M7 — PDF 도면 스탬프 MVP E2E`까지 구현·독립 검증·사용자 승인·Result Commit·Rollback/Restore가 완료됐습니다. M7 공식 Run은 `run-c0a968f3`, 제품 Result Commit은 `3b592c8`입니다. 이로써 `AI OS V2 Core MVP M1~M7`은 검증 완료·동결 상태입니다. Post-MVP 설계는 [[POST_MVP_PM0_PM6_BASELINE]]의 `PM0~PM6`으로 완료됐으며 완료 범위와 미구현 항목은 [[POST_MVP_DESIGN_COMPLETION_REPORT]]에 기록합니다. `PM0 — 운영환경 준비`는 기술 Preflight와 격리 재현을 통과했고, 사용자가 외부 Backup·표본 Restore만 후속으로 유예한 조건으로 PASS했습니다. `PM1 — 디자인 전략·탐색·채택`은 `single_visual_target_with_ui_ux_pro_guard` 방식과 PC 운영 UI를 PASS했습니다. `PM2 — 조립식 제작 보드`는 두 프로젝트 결과 Module, 단일 선택 Preview, 프로젝트별 기능 목록, Core 상태·Action·격리·복원을 사용자·Codex가 PASS했습니다. PM3은 사용자 조건부 통과로 범위를 잠갔고 기술 완료는 `not_proven`이며 PM6 재검증이 필수입니다. 다음 진행 가능 단계는 `PM4 — 조사·Design Intelligence`입니다. `run-ef4986d7`의 기존 Preview v1과 PM1의 실패 Pilot은 당시 거절 판정 그대로 보존하며 구현 입력으로 사용하지 않습니다.

2026-08-21 PM4는 로컬 우선 Collector 최소 Pilot으로 시작했습니다. Interview → Collector(수집만) → Analyzer(사실·충분성 분석) 역할을 분리하고, 기존 성공 자산이 충분하면 외부 조사를 생략하며 부족하면 필요한 근거만 조사 요청으로 만드는 두 분기를 Network 없이 `9/9 PASS`했습니다. 이는 PM4 전체 PASS가 아닙니다. 실제 조사 요청, 출처 검증, 사용자 `채택·보류·폐기`, 채택 후 Capability Lab 연결은 아직 `not_yet_verified`입니다. GitHub 공개 Metadata 외 Reddit·YouTube·Threads·Instagram Adapter는 `planned_not_connected`입니다. 자세한 증거는 [[PM4_LOCAL_FIRST_COLLECTOR_PILOT_2026-08-21]]을 사용합니다.

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
