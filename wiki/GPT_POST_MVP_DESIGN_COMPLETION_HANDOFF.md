# AI OS V2 Post-MVP 설계 완료 협업 전달서

작성일: 2026-08-16
대상 저장소: `songja-092/ai-os-v2`
목적: GPT와 대화로 Post-MVP 설계를 끝내기 위한 사실 기준·충돌 목록·결정 질문을 제공한다.

---

## 1. GPT에게 요청할 작업

아래 내용을 저장소의 실제 커밋 상태와 구분해 검토해 주세요.

1. 구현하거나 파일을 수정하지 말고 설계만 검토합니다.
2. 현재 GitHub `main`, 로컬 커밋 설계, 사용자가 새로 합의한 PM0~PM7을 구분합니다.
3. 새 PM을 불필요하게 추가하지 말고 기존 PM0~PM7 안에서 중복·누락을 정리합니다.
4. SaaS 인증·앱 내부 결제·테넌트 격리·팀 협업·자동 배포는 범위에서 제외합니다.
5. 한 명의 운영자가 로컬에서 고객 프로젝트를 제작하고 결과를 전달해 돈을 받는 사용 모델을 전제로 합니다.
6. PM1 시각 방향, 상태·데이터 모델, 실행 안전 계약, 측정 가능한 PASS 조건을 완성합니다.
7. 설계가 충분하면 사용자에게 전체안을 한 번에 제시하고 최종 승인을 요청합니다.
8. 사용자 최종 승인 전에는 `Post-MVP 설계 완료`라고 선언하지 않습니다.
9. 최종 승인 후에는 반드시 정확히 `Post-MVP 설계 완료`라고 선언합니다.

---

## 2. 실제 저장소 감사 결과

### GitHub 공식 상태

```yaml
repository: https://github.com/songja-092/ai-os-v2
github_main_sha: da33544fac365e6915aad73ec533124d12309803
github_main_latest_subject: docs_prepare_PM1_continuation_handoff
```

### 현재 로컬 작업 브랜치

```yaml
branch: antigravity/v2-m1-run-core
head: 27237609e53aaf6872e30c195b263c4e085c78f8
commits_after_github_main:
  - sha: 7055705e85d0dee6c5b2ea01afc3cf76fd9cb1a3
    subject: docs_define_PM1_modular_foundation_and_hybrid_design_standard
  - sha: 27237609e53aaf6872e30c195b263c4e085c78f8
    subject: feat_add_design_artifact_and_fidelity_foundation
github_main_contains_these_commits: false
```

현재 로컬 작업 폴더에는 사용자 소유 Dirty 변경이 있으므로 수정·정리·Stage·Commit하면 안 됩니다.

### 로컬 최신 커밋 문서가 말하는 상태

```yaml
core_mvp_m1_m7: completed_and_frozen
post_mvp_documented_structure: PM1_to_PM4
post_mvp_planning_status_in_docs: approved
active_milestone: PM1
pm1_design_method: Hybrid_H
pm1_selected_direction: MIX-1
pm1_clickable_preview_v1: rejected_visual_fidelity
pm1_visual_target: required
pm1_design_source_of_truth: not_established
pm1_implementation: not_started
```

근거 문서:

- `wiki/CURRENT_STATE.md`
- `wiki/DECISIONS.md`
- `wiki/POST_MVP_ROADMAP.md`
- `wiki/PM1_HANDOFF.md`
- `wiki/THIN_UI_MVP_CONTRACT.md`
- `wiki/VERIFICATION.md`
- `runs/run-ef4986d7/run.yml`

### 중요한 불일치

1. GitHub `main`은 `da33544`지만 로컬 설계 HEAD는 `2723760`입니다.
2. 로컬 최신 공식 문서는 Post-MVP를 PM1~PM4로 기록합니다.
3. 사용자와 최근 대화에서 정리한 목표 구조는 PM0~PM7입니다.
4. 기존 PM2는 `직접 부분 수정`이지만 새 구조의 PM2는 `로컬 프로젝트 관리`입니다.
5. 기존 PM3는 조사·수집·병목 진단이지만 새 구조에서는 디자인 Reference 역할이 확대됩니다.
6. 기존 PM4 이후 PM5~PM7은 커밋 문서에 존재하지 않습니다.
7. 따라서 현재 저장소만으로는 PM0~PM7 설계 완료를 증명할 수 없습니다.

---

## 3. 사용자가 원하는 최신 PM 기본틀

### PM0 — 운영환경 준비

목적: 실제 구현을 안전하게 시작할 수 있는 상태를 만든다.

포함:

- 작업공간 격리
- Runtime·Port 확인
- Antigravity 안전 실행
- Preview 실행 환경 확인
- 백업·복원
- 새 세션 재현
- 작업 실패 후 환경 복구와 안전 종료

제외:

- 제품 기능 구현
- 디자인 제작
- 불필요한 도구·패키지 설치

PM0는 설계 논의를 막지 않고 실제 구현만 차단하는 Gate입니다.

### PM1 — 대시보드·프로젝트 작업실

목적: 사용자가 여러 프로젝트를 선택하고 현재 상태와 실제 결과를 확인한다.

포함:

- 프로젝트 홈과 부모 보드
- 프로젝트별 자식 작업 보드
- 현재 요청·단계·막힌 이유·다음 행동
- 실제 Preview 중심 작업실
- 390px·430px·PC 전환
- 통과·수정 요청·중단
- 프로젝트 전환
- 오류 요약
- 결과물·전달 준비 상태
- 저장되지 않은 변경과 마지막 검증 시점

PM1은 Commit·Rollback을 직접 수행하는 엔진이 아니라 Core가 허용한 행동과 상태를 표시하는 얇은 UI입니다.

남은 필수 결정:

- 대표 Landing Page Sample A/B 또는 A/B/C
- 톤앤매너
- 정보 구조
- 모바일 우선 흐름
- 화면·핵심 상태별 `visual_target`
- `1440x950`, `430px`, `390px` Fidelity PASS

### PM2 — 로컬 프로젝트 관리

포함:

- 새 프로젝트 시작
- 기존 로컬 프로젝트 등록
- 선택·전환
- 표시 이름 변경
- 보관·복원
- 고유 Project ID와 실제 경로 분리
- 중복 경로·허용 Root 이탈·Symlink 탈출 차단

실제 폴더 자동 이름 변경·이동·삭제는 하지 않습니다.

### PM3 — 자료·디자인 Reference 수집

포함:

- 공개 Web·공식 문서·GitHub·Reddit 조사
- 사용자 제공 Threads 본문·링크·Screenshot
- PDF·Markdown·Text·Screenshot
- 디자인 Reference 수집·비교·선택
- 출처·수집 시점·확인 범위 기록
- 사실·주장·추정·추천 분리
- 새 프로젝트 조사와 기존 프로젝트 병목 진단
- 선택·제외·실제 적용 Reference 구분

초기 보관은 V2 로컬 폴더를 사용합니다. Mobbin은 수동 검색처, Figma는 필요할 때 비교 보드로만 사용하며 유료 API 연결은 기본 범위가 아닙니다.

### PM4 — 사용자 의도 확인

포함:

- 이해한 목표
- 만들 화면과 기능
- 변경할 영역과 금지 영역
- 완료 확인 방법
- 빠진 조건과 기존 결정 충돌
- 모호한 부분 질문 하나
- 범위 불일치 시 구현 차단
- 구현 후 최초 요청과 결과 비교
- 요청 변경과 승인 이력

### PM5 — 디자인 다양성 생성·비교

포함:

- PM3 Reference Mix
- UI UX Pro 디자인 규칙
- 구조적으로 다른 Design DNA 2~3개
- 클릭 가능한 A/B 또는 A/B/C
- 모바일·PC 비교
- 사용자 선택 또는 혼합
- 선택 이유와 적용 규칙 보존

시안은 색상뿐 아니라 정보 우선순위, 이동 방식, Section 순서, Typography, Card 구조, Image 사용, CTA 위치와 모바일 흐름이 달라야 합니다.

### PM6 — 최신 디자인·모션·부분 수정

포함:

- 필요할 때 최신 경향 조사
- 적절한 Motion 후보
- Typography·폭·줄바꿈·색상·여백·모서리 수정
- Section·Layout 순서 변경
- 표시·숨김
- 변경 전후 Preview
- 원래대로·적용
- Draft → 검증 → 적용
- 부분 Undo와 수정 이력
- `prefers-reduced-motion`
- 모바일·PC 회귀검증

Figma 수준 자유 Canvas와 무제한 Drag & Drop은 제외합니다.

### PM7 — 전체 통합 흐름·최종 검증

통합 흐름:

```text
프로젝트 시작·등록
→ 자료와 Reference 조사
→ AI 의도 확인
→ 구조가 다른 디자인 Preview 비교
→ 사용자 선택
→ 구현
→ 부분 수정
→ 최종 Preview
→ 통과
→ Commit·Rollback·Restore
→ 결과 전달
```

포함:

- PM 간 상태 전달
- 프로젝트 교차 작업 차단
- 실패 지점부터 재개
- 결과 Commit
- Rollback·Restore
- 최종 결과물 목록
- 실행 방법과 알려진 제한
- 고객용 완료 보고서와 전달 패키지
- 모바일·PC 최종 검증

---

## 4. 설계 완료 전에 반드시 결정할 항목

### A. 핵심 데이터 모델

최소 Entity와 관계를 확정해야 합니다.

```text
Project
├─ Request Specification
├─ Reference
├─ Design Candidate
├─ Run
│  ├─ Artifact
│  ├─ Verification Result
│  └─ Error Report
├─ Revision Request
├─ Approval
└─ Delivery Package
```

`Project`, `Run`, `Preview`, `Artifact`, `Revision`, `Approval`의 ID·소유 관계·저장 위치를 정의해 주세요.

### B. 상태 전환 모델

다음 상태를 채택·수정하고 각 전환 조건을 정의해 주세요.

```text
draft
→ researching
→ intent_review
→ design_selection
→ ready_to_build
→ implementing
→ verifying
→ revision_requested
→ approved
→ completed
→ archived
```

각 상태마다 다음을 결정합니다.

- 누가 전환하는가
- 필수 Artifact는 무엇인가
- 사용자 승인이 필요한가
- 실패하면 어디로 가는가
- 중단 후 어디서 재개하는가
- 허용 Action은 무엇인가

### C. AI 실행 안전 계약

- 읽기 허용 경로
- 수정 허용 파일
- 수정 금지 파일
- 허용 명령
- 외부 통신
- 승인 필요 행동
- 작업 단위
- 재시도 한도
- 한 시점의 단독 Writer

기존 계약 `V2 Core → ui-state → UI → ui-action → V2 Core`와 `allowed_actions`, `state_version`, `action_id`를 유지할지 확정해 주세요.

### D. Sample·Preview·Implementation 구분

```yaml
concept_sample:
  purpose: tone_and_manner
  product_code: false
clickable_preview:
  purpose: structure_and_navigation
  product_code: false
implementation:
  purpose: real_project_change
  product_code: true
```

시각 Sample 선택이 자동 제품 변경으로 이어지지 않도록 Gate를 정의해 주세요.

### E. Commit·Undo·Rollback·Restore

- `Undo`: 적용 전 Draft 취소
- `Rollback`: Git Commit 기준 이전 상태 확인
- `Restore`: 백업으로 파일·환경 복구
- 기존 Dirty 변경 자동 포함 금지
- AI 변경 파일만 분리
- Commit 전 변경 목록 표시
- Git이 없는 프로젝트의 Snapshot 방식

### F. 측정 가능한 PASS

최소 공통 기준을 확정해 주세요.

```yaml
responsive:
  widths: [390, 430, 1440]
  horizontal_overflow: false
accessibility:
  keyboard_core_flow: pass
  visible_focus: pass
  text_contrast: wcag_aa
  reduced_motion: supported
project_isolation:
  cross_project_artifact_mix: 0
  cross_project_preview_mix: 0
recovery:
  resume_from_last_successful_step: true
  user_dirty_changes_lost: 0
delivery:
  final_preview: required
  verification_report: required
  result_commit_or_snapshot: required
  run_instructions: required
  known_limitations: required
  restore_point: required
```

### G. 오류·재개 모델

오류 종류:

- 환경
- 프로젝트 코드
- 자료 수집
- AI 의도 불일치
- Preview
- 검증
- Commit
- 복구

사용자에게는 다음만 기본 표시합니다.

- 무엇이 실패했는가
- 기존 결과가 안전한가
- 재시도 가능한가
- 사용자가 해야 할 일
- 재개 지점

### H. Reference → Design System 승격 규칙

```text
수집 Reference
→ Pattern 분석
→ 사용자 선택
→ Project Design DNA
→ Token·Component 규칙
→ 실제 구현
→ 반복 검증된 규칙만 공통 Design System 후보
```

Reference 수집만으로 자동 채택하지 않고 프로젝트별 Design DNA를 분리합니다.

---

## 5. GPT가 사용자에게 물어볼 최종 결정

질문을 한꺼번에 늘어놓지 말고 가장 큰 결정부터 한 번에 하나씩 묻습니다.

1. PM1 Sample에서 먼저 비교할 정보 구조 2~3개
2. 선택할 톤앤매너 또는 혼합 방향
3. PM0~PM7 최신 구조를 기존 PM1~PM4 공식 문서 대신 새 기준으로 채택할지
4. 위 데이터·상태·안전·PASS 모델의 최종 승인
5. 전체 Post-MVP 설계 최종 승인

---

## 6. 설계 완료 Gate

아래가 모두 `true`일 때만 완료입니다.

```yaml
post_mvp_design_completion_gate:
  pm0_to_pm7_scope_approved: false
  entity_and_state_model_approved: false
  execution_safety_contract_approved: false
  measurable_pass_criteria_approved: false
  error_resume_model_approved: false
  reference_design_system_rule_approved: false
  pm1_visual_target_approved: false
  cross_pm_duplicate_and_gap_review_passed: false
  user_final_approval: false
```

완료 전:

```yaml
post_mvp_design: in_progress
pm_design_allowed: true
pm0_implementation_gate: blocked
pm_implementation_allowed: false
```

완료 후 사용자에게 반드시 표시할 문구:

> **Post-MVP 설계 완료**

그 뒤에도 PM0 운영 Gate를 통과하기 전에는 PM1 실제 구현을 시작하지 않습니다.

---

## 7. GPT가 최종 답변에서 제공할 형식

```yaml
design_review:
  verdict: PASS | PASS_WITH_FIX | BLOCKED
  missing_decisions: []
  contradictions_resolved: []
  pm0_to_pm7_final_scope: approved | pending
  pm1_visual_direction: approved | pending
  implementation_allowed: false
```

설계가 아직 부족하면 다음 결정 하나만 제시합니다. 설계가 모두 승인되면 `Post-MVP 설계 완료`를 선언하고, 공식 문서에 반영해야 할 변경 목록을 별도로 제시합니다.
