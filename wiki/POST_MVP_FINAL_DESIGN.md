# AI OS V2 Post-MVP 최종 설계 보고서

작성일: 2026-08-16
문서 상태: Final Design Baseline
대상: 단일 운영자가 로컬 환경에서 고객 프로젝트를 조사·설계·제작·검증·전달하는 AI OS V2
구현 상태: 시작 전

---

## 1. 최종 결론

AI OS V2 Post-MVP는 `PM0~PM7`의 8개 단계로 확정합니다.

```text
PM0 운영환경 준비
→ PM1 대시보드·프로젝트 작업실
→ PM2 로컬 프로젝트 관리
→ PM3 자료·디자인 Reference 수집
→ PM4 사용자 의도 확인
→ PM5 디자인 다양성 생성·비교
→ PM6 최신 디자인·모션·부분 수정
→ PM7 전체 통합·최종 검증·결과 전달
```

본 설계는 다음 운영 모델을 전제로 합니다.

- 한 명의 운영자가 로컬 컴퓨터에서 사용합니다.
- 고객은 완성된 웹·앱·결과물을 제공받습니다.
- SaaS 사용자 인증, 앱 내부 결제, Tenant 격리와 팀 협업은 제외합니다.
- 자동 배포와 무인 자동 승인도 제외합니다.
- 기술정보를 모르는 사용자는 자연어·선택지·Preview 중심으로 사용합니다.
- 실제 파일 변경·Commit·Rollback은 V2 Core가 통제합니다.

---

## 2. 기준 상태

```yaml
repository: https://github.com/songja-092/ai-os-v2
core_mvp_m1_m7: completed_and_frozen
pm_design_foundation_commit: 27237609e53aaf6872e30c195b263c4e085c78f8
current_core_head_at_review: bf8dda49e4d16529d9c43e4ed4afdc2d563f5750
pm_design_environment_smoke: pass
pm1_real_implementation: not_started
pm0_operational_gate: blocked
push_of_design_foundation: not_performed
```

디자인 환경 Fixture에서는 Visual Target 등록·승인 Gate, Image-to-Code, Browser, Fidelity Ledger, Product Design Audit, Rollback·Restore와 Core Fixture 29개 검사를 통과했습니다. 이는 설계·도구 경로의 실행 가능성을 증명하지만 실제 PM1 디자인 승인이나 제품 구현 완료를 의미하지 않습니다.

---

## 3. 설계 원칙

### 3.1 사용자 경험

```text
원하는 것을 말한다
→ AI가 이해한 내용을 확인한다
→ 조사·디자인 후보를 눈으로 고른다
→ 실제 결과를 확인한다
→ 완료 또는 수정 요청을 말한다
```

- 한 화면에서 가장 중요한 질문과 다음 행동 하나를 우선합니다.
- 기본 선택지는 가능한 경우 `추천대로 진행`과 `직접 선택`으로 단순화합니다.
- Run ID, Port, Commit SHA, 내부 Gate, Stack과 상세 Log는 기본 화면에서 숨깁니다.
- 문제 발생 시 기술 원문보다 `무엇이 실패했는지`, `결과가 안전한지`, `다음 행동`을 먼저 보여줍니다.

### 3.2 단일 상태 소유자

```text
V2 Core → ui-state(JSON) → Thin UI
Thin UI → ui-action → V2 Core
```

- V2 Core만 Project, Run, Gate, Artifact, Action과 Git 상태를 판정합니다.
- UI는 Core가 제공한 상태를 표시하고 입력을 전달합니다.
- UI는 Run YAML, Wiki, 프로젝트 파일을 직접 수정하지 않습니다.
- UI는 임의 Shell 명령이나 Port를 만들지 않습니다.
- 동일 Run에는 한 시점에 Writer 한 명만 허용합니다.

### 3.3 조립 우선

```text
현재 설치 Skill
→ 기존 V2 Core와 제품 기능
→ 공식 도구와 문서
→ 유지관리되는 GitHub OSS
→ 최소 연결 코드
→ 필요한 경우에만 신규 구현
```

도구를 발견했다는 이유만으로 설치·채택·검증 완료 처리하지 않습니다.

### 3.4 검증 후 엔터프라이즈 확장

V2는 현재 필요한 로컬 단일 운영자 흐름을 우선 구현하되, 반복 사용으로 가치가 증명된 기능은 Core를 다시 작성하지 않고 엔터프라이즈급 모듈로 승격할 수 있어야 합니다. 이를 위해 초기 구현부터 다음 경계를 지킵니다.

- UI, Application Service, Domain, 외부 도구 Adapter와 저장소 Adapter를 분리합니다.
- Project·Run·Artifact·Action·Approval 계약은 Versioned Schema로 관리합니다.
- 파일시스템, Git, Browser, AI Provider, Reference Source는 교체 가능한 Port·Adapter로 연결합니다.
- 모든 상태 변경은 `project_id`, `run_id`, Actor, 시각, 입력 Version과 결과를 Audit Event로 남길 수 있게 합니다.
- Project 데이터와 Artifact는 명시적 소유 경계를 가지며 Export·Import·Backup이 가능해야 합니다.
- 동시 실행은 Idempotency, Writer Lock, Retry·Timeout과 Failure Isolation 계약을 따릅니다.
- 비밀정보는 코드·Artifact·Log와 분리하고 최소 권한 정책을 적용할 수 있게 합니다.
- 관측성은 구조화 Log, 오류 분류, 처리시간과 실패 단계부터 시작하고 중앙 수집은 필요할 때 Adapter로 추가합니다.
- 공개 API, Queue, 원격 Storage, 조직·권한, Tenant 격리는 현재 구현하지 않지만 Domain 계약을 깨지 않고 추가할 수 있어야 합니다.

엔터프라이즈 승격은 기능이 존재한다는 이유로 진행하지 않습니다. 다음 조건을 충족한 모듈만 후보가 됩니다.

```yaml
enterprise_promotion_gate:
  repeated_real_use: true
  measurable_user_value: true
  stable_versioned_contract: true
  automated_regression_and_recovery: true
  audit_and_security_boundary_defined: true
  operational_cost_understood: true
  migration_and_rollback_path_defined: true
```

초기 PM에 Kubernetes, Microservice, 분산 Queue나 복잡한 권한 체계를 미리 도입하지 않습니다. 먼저 Modular Monolith와 명확한 계약으로 구현하고, 실제 병목이 증명된 경계만 독립 서비스로 분리합니다.

---

## 4. 핵심 데이터 모델

### 4.1 Entity

```yaml
Project:
  owns:
    - RequestSpecification
    - ReferenceCollection
    - DesignCandidate
    - Run
    - RevisionRequest
    - Approval
    - DeliveryPackage

Run:
  owns:
    - Artifact
    - PreviewSession
    - VerificationResult
    - ErrorReport
    - RecoveryPoint
```

### 4.2 필수 식별자

| Entity | 필수 ID | 역할 |
|---|---|---|
| Project | `project_id` | 실제 경로와 분리된 불변 ID |
| Request | `request_id`, `version` | 요청 변경과 승인 추적 |
| Run | `run_id` | 작업·증거·결과 연결 |
| Reference | `reference_id` | 출처·선택·적용 추적 |
| Design Candidate | `candidate_id`, `design_dna_id` | 구조적으로 다른 시안 구분 |
| Visual Target | `visual_target_id`, `sha256` | 승인된 이미지 원본 식별 |
| Revision | `revision_id` | 수정 요청과 전후 결과 연결 |
| Artifact | `artifact_id`, `sha256` | 결과 원본성과 변경 감지 |
| Action | `action_id`, `state_version` | 중복·Stale Action 차단 |
| Approval | `approval_id`, `target_version` | 승인 대상 Version 고정 |

### 4.3 저장 경계

- Project Registry에는 표시명, 실제 경로, 유형, 허용 명령, Port와 상태만 저장합니다.
- 고객 프로젝트 파일은 원래 프로젝트 경로에 유지합니다.
- Run과 검증 증거는 V2가 소유합니다.
- 디자인 Reference와 Visual Target은 Versioned Artifact로 보존합니다.
- Draft Preview는 제품 원본과 분리합니다.
- UI 전용 별도 진실 저장소를 만들지 않습니다.

---

## 5. 프로젝트 상태 모델

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

### 상태 전환 계약

| 현재 상태 | 다음 상태 | 필수 조건 | 실패·취소 |
|---|---|---|---|
| draft | researching | Project와 요청 원문 존재 | draft 유지 |
| researching | intent_review | 출처·확인 범위가 기록된 조사 결과 | `needs_more_source` |
| intent_review | design_selection | 사용자 목표·허용·금지·완료 기준 승인 | 불일치 시 차단 |
| design_selection | ready_to_build | Visual Target 또는 비시각 Plan 승인 | 선택 단계 유지 |
| ready_to_build | implementing | PM0 PASS, 승인된 Task, 안전 범위 | 구현 금지 유지 |
| implementing | verifying | 구현 Agent 완료 보고와 변경 범위 회수 | 실패 지점 보존 |
| verifying | approved | 기술 검증과 사용자 확인 PASS | revision_requested |
| revision_requested | implementing | 승인된 수정 범위와 새 Version | 기존 결과 보존 |
| approved | completed | Commit/Snapshot·전달 패키지·복구점 | approved 유지 |
| completed | archived | 사용자 보관 요청 | completed 복원 가능 |

Core가 성공을 반환한 후에만 UI 상태를 변경합니다. 실패한 Run은 정상 결과 Run을 덮어쓰지 않습니다.

---

## 6. 실행 안전 계약

### 허용 범위

- Project Registry에 등록된 고정 Root
- 검증된 고정 실행 명령
- 프로젝트별 고정 Port와 `strictPort`
- 승인된 Task와 파일 범위
- 읽기 전용 상태·Git·Build·Browser 검사

### 금지 범위

- UI에서 임의 Path·Shell·Port 입력
- 사용자 Dirty 변경 자동 Stage·Commit
- 허용 Root 밖 파일 접근
- Symbolic Link를 통한 Root 탈출
- 승인 없는 설치·삭제·외부 전송·권한 변경
- 실패를 숨기기 위한 `--no-sandbox` 등 안전 우회
- 다른 프로젝트 Preview·Artifact·Run 재사용

### Action 검증

모든 Action은 다음을 확인합니다.

```yaml
action_validation:
  project_id_matches: true
  run_id_matches: true
  state_version_current: true
  action_id_not_reused: true
  action_is_allowed: true
  writer_lock_acquired: true
```

---

## 7. 디자인 시스템과 Reference 흐름

```text
Reference 수집
→ Pattern 분석
→ 사용자 비교·선택
→ Project Design DNA
→ Design Token·Component·Section 규칙
→ Visual Target
→ Image-to-Code
→ Fidelity 검증
→ 코드가 프로젝트 디자인 Source of Truth
→ 반복 검증된 규칙만 공통 Design System 후보
```

### 공식 디자인 방식

```text
Reference Mix
→ 서로 다른 Design DNA A/B/C
→ 사용자 선택·혼합(MIX-1 포함)
→ 화면·핵심 상태별 단일 Visual Target
→ 사용자 시각 승인
→ Image-to-Code
→ 1440×950·430px·390px Fidelity 비교
→ Fidelity PASS
→ 코드 Source of Truth
→ Section ID 기반 부분 수정
```

Reference는 자동으로 Design System에 채택하지 않습니다. 프로젝트별 채택 결과를 분리하고, 기존 프로젝트 디자인을 새 Reference 때문에 자동 변경하지 않습니다.

### Sample 단계 구분

```yaml
concept_sample:
  purpose: tone_and_manner
  modifies_product: false
clickable_preview:
  purpose: structure_navigation_and_states
  modifies_product: false
implementation:
  purpose: real_project_feature
  modifies_product: true
```

---

## 8. PM0 — 운영환경 준비

### 목적

실제 PM 구현을 기존 프로젝트 손상 없이 시작·중단·복구·재현할 수 있는 상태를 만듭니다.

### 기능

- 공식 Commit 기반 격리 Worktree
- Core·Preview·제품 저장소 HEAD와 Dirty 상태 확인
- Runtime·Skill 경로·Version 확인
- 병원 웹·PDF 제품 독립 Worktree
- 고정 Port `5173`, `5174`, V2 UI `8200`
- `strictPort`와 충돌 차단
- Preview Process·PID·Log 소유권
- Antigravity의 Sandbox 적용 안전 실행
- Preview DOM·Console·장애 격리
- 외부 백업과 Restore 표본 시험
- 새 Codex 세션 Preflight 재현
- Commit·Rollback·Restore 경로 확인

### 제외

- 제품 기능 구현
- PM1 Visual Target과 실제 UI 제작
- 불필요한 Package·Skill 설치
- 기존 Dirty 파일 정리
- 승인 없는 권한 변경

### PASS

```yaml
pm0_pass:
  isolated_workspace: true
  dirty_changes_preserved: true
  runtimes_match_baseline: true
  ports_and_process_ownership_verified: true
  hospital_preview_verified: true
  pdf_preview_verified: true
  preview_failure_isolated: true
  antigravity_secure_launch_verified: true
  external_backup_verified: true
  restore_sample_passed: true
  new_session_reproduction_passed: true
```

PM0가 PASS하기 전에도 PM 설계와 Concept Sample은 가능하지만 실제 제품 구현은 금지합니다.

---

## 9. PM1 — 대시보드·프로젝트 작업실

### 목적

초보 사용자가 여러 프로젝트 중 하나를 선택하고 현재 요청·상태·실제 결과·다음 행동을 한 화면에서 이해합니다.

### 기능

- 프로젝트 홈과 부모 보드
- 프로젝트별 자식 작업 보드
- 최근 프로젝트와 현재 단계
- 현재 요청·막힌 이유·다음 행동
- 실제 Preview 중심 작업실
- 요청 25% / Preview 75% 기본 비율
- Preview 크게·대화 보기 전환
- 390px·430px·1440px
- 통과·수정 요청·중단
- 프로젝트 전환
- 저장되지 않은 변경 표시
- 마지막 검증 시점
- 최소 오류 보고서
- 결과물과 전달 준비 상태
- 기술 상세 보기

### 제외

- Run YAML과 프로젝트 파일 직접 수정
- 임의 Shell·Path·Port
- 복잡한 Dashboard Builder
- 자유형 Canvas 편집
- 팀 협업·사용자 권한
- PM2 이후 기능의 실제 구현

### 대표 시나리오

```text
프로젝트 홈
→ 병원 웹 선택
→ 현재 요청과 다음 행동 확인
→ 실제 Preview 확인
→ 수정 요청
→ PDF 프로젝트로 이동
→ 서로 다른 Preview와 상태 확인
```

### PASS

- 초보자가 기술정보 없이 프로젝트와 다음 행동을 찾습니다.
- 프로젝트 간 Run·Artifact·Preview 혼합이 0건입니다.
- Preview 실패가 Shell과 다른 프로젝트에 전파되지 않습니다.
- 390px·430px·1440px 핵심 흐름이 동작합니다.
- Keyboard 핵심 흐름, Focus, WCAG AA Contrast와 Reflow를 통과합니다.
- 승인된 Visual Target과 동일 Viewport Fidelity를 통과합니다.

---

## 10. PM2 — 로컬 프로젝트 관리

### 목적

컴퓨터에 존재하는 여러 프로젝트를 실제 파일 손상 없이 등록·선택·보관합니다.

### 기능

- 새 프로젝트 시작
- 기존 로컬 프로젝트 등록
- 프로젝트 선택·전환
- 표시 이름 변경
- 보관·복원
- Project ID와 실제 Path 분리
- 중복 Path 차단
- 허용 Root와 Symlink 탈출 검사
- Git 저장소·일반 Folder 구분
- 프로젝트 생명주기 상태 표시

### 제외

- GitHub 직접 가져오기
- Cloud Sync
- 실제 Project Folder 자동 이름 변경·이동·삭제
- 팀 협업
- 자동 배포

### PASS

- 여러 로컬 프로젝트를 독립적으로 등록·전환합니다.
- 동일 Path 중복과 허용 Root 밖 접근을 차단합니다.
- 표시 이름 변경이 실제 Folder 이름을 바꾸지 않습니다.
- 보관이 실제 파일을 삭제하지 않습니다.
- 기존 Git와 Dirty 상태 손실이 0건입니다.

---

## 11. PM3 — 자료·디자인 Reference 수집

### 목적

새 프로젝트에 필요한 정보·사례·디자인 Pattern과 기존 프로젝트의 가장 큰 병목 근거를 확보합니다.

### Source

```yaml
web: public_and_official
github: repository_readme_issue_release_license
reddit: public_experience_and_failure_cases
threads: user_provided_link_text_screenshot
documents: pdf_markdown_text_screenshot
```

### 기능

- 공개 Web·공식 문서 조사
- GitHub·Reddit 선택 조사
- 사용자 제공 Threads 활용
- PDF·Markdown·Text·Screenshot
- 디자인 Reference 수집·비교·선택
- Source URL·확인 시각·Checksum
- 사실·주장·추정·추천 분리
- 접근 실패와 확인 범위 기록
- 새 프로젝트 최소 MVP 조사 1건
- 기존 프로젝트 최대 병목 1건과 해결책 최대 2개
- 선택·제외·적용 Reference 구분
- Project별 Reference Collection

### 보관·도구

- 초기에는 V2 로컬 Versioned Artifact를 사용합니다.
- Mobbin은 수동 검색처로 선택 사용합니다.
- Figma는 필요할 때 비교 보드로 선택 사용합니다.
- 유료 API와 자동 대규모 수집 Agent는 사용하지 않습니다.

### 디자인 Reference 수집 Workflow

별도 PM을 추가하지 않고 PM3의 `Design Reference Collector` Workflow로 운영합니다. 항상 실행되는 감시 Agent가 아니라 프로젝트 요청 또는 사용자의 `Reference 다시 찾기` 행동으로 시작하는 제한형 작업입니다.

```text
프로젝트·화면 유형 확인
→ Web·GitHub·Reddit·사용자 제공 Threads·Screenshot에서 후보 수집
→ 출처·조회일·License·접근 범위 기록
→ 업종·정보 구조·시각 스타일·밀도·모바일 흐름으로 분류
→ 구조가 다른 후보 최대 6개 제시
→ 사용자 선택·제외
→ 선택 Reference를 Versioned Collection으로 보존
→ PM5 Reference Mix 입력으로 전달
```

```yaml
design_reference_workflow:
  collector: source_and_visual_candidate_collection
  analyzer: pattern_difference_and_risk_analysis
  curator: user_selection_and_versioned_collection
  writer_owner: v2_core
  max_parallel_jobs: 1
  max_presented_candidates: 6
  automatic_adoption: false
  continuous_monitoring: false
  bulk_scraping: false
```

- `collector`는 Reference를 찾지만 디자인을 생성하지 않습니다.
- `analyzer`는 구조·패턴·모바일 흐름과 적용 위험을 비교하지만 최종 선택하지 않습니다.
- `curator`는 사용자 선택 결과만 보존하며 제품 코드나 Design System을 직접 변경하지 않습니다.
- 실제 디자인 후보 생성은 PM5가 담당합니다.
- 사용자가 결과를 모두 거절하면 기존 Collection을 보존하고 거절 사유를 기록한 뒤 Source 축을 바꿔 한 번 다시 조사합니다.
- 로그인·유료 제한·Robots 정책·License로 접근할 수 없는 Source는 우회하지 않고 링크 또는 사용자가 제공한 Screenshot을 요청합니다.

### 제외

- 로그인·Paywall 우회
- Cookie 재사용
- 무단 대량 Scraping
- 출처 없는 자료
- 수집 실패로 Core 전체 차단
- Reference 원본 복제

### PASS

- 출처와 확인 범위를 가진 자료를 프로젝트에 연결합니다.
- 공식 사실과 사용자 의견을 구분합니다.
- 구조가 다른 디자인 Pattern을 비교합니다.
- 수집 실패가 기존 제작·Preview를 막지 않습니다.
- 채택 Reference와 실제 적용 Pattern을 추적합니다.

---

## 12. PM4 — 사용자 의도 확인

### 목적

AI가 요청을 잘못 이해한 상태에서 구현을 시작하지 못하게 합니다.

### Intent Packet

```text
이해한 목표:
대상 사용자:
만들 화면과 기능:
변경할 부분:
건드리지 않을 부분:
완료 확인 방법:
Reference와 올바른 예:
잘못된 예:
모호한 부분:
```

### 기능

- 요청 원문과 구조화된 Request Specification
- 구현 AI의 Intent Receipt
- 핵심 용어·허용·금지 범위 비교
- 빠진 조건·과거 결정 충돌·Scope Creep 확인
- 불일치 시 구현 차단
- 정말 모호할 때 질문 하나
- 요청 변경 시 Version 증가와 재승인
- 승인자·시점·대상 Version 기록
- 구현 후 최초 요청과 결과 재비교

### 제외

- AI Provider Marketplace
- 비용 기반 자동 Provider 교체
- 모든 요청의 긴 승인 문서
- 여러 질문 동시 제시

### PASS

- 구현 전 사용자 요청·Intent Packet·Receipt가 일치합니다.
- 승인된 Version과 구현 Task가 연결됩니다.
- 범위가 달라지면 구현이 시작되지 않습니다.
- 구현 후 결과가 최초 요청과 다시 비교됩니다.

---

## 13. PM5 — 디자인 다양성 생성·비교

### 목적

색상만 다른 시안이 아니라 구조와 사용 흐름이 다른 결과를 눈으로 비교합니다.

### 기능

- PM3 Reference Mix
- UI UX Pro 규칙 보조
- Design DNA 2~3개
- 클릭 가능한 A/B 또는 A/B/C
- 모바일·PC 비교
- 시안별 장점·주의점·구현 난이도
- 사용자 선택·혼합
- 선택 이유와 적용 규칙 보존
- Visual Target 생성과 승인

### 시안 최소 차이

- 정보 우선순위
- Menu·Navigation
- Section 순서
- Typography와 줄바꿈
- Card 구조
- Image 사용 방식
- CTA 위치
- 모바일 완료 흐름

### 제외

- 색상만 다른 A/B
- UI UX Pro 추천 자동 채택
- Reference 그대로 복제
- 매번 많은 시안 생성
- 승인 전 제품 코드 변경

### PASS

- 동일 요구사항을 충족하는 구조적 대안 2개 이상이 존재합니다.
- 390px·430px·1440px에서 비교 가능합니다.
- Empty·Loading·Error·Success 핵심 상태가 포함됩니다.
- 사용자 선택과 혼합 규칙이 Versioned Artifact로 남습니다.
- 승인된 Visual Target SHA가 존재합니다.

---

## 14. PM6 — 최신 디자인·모션·부분 수정

### 목적

선택된 디자인을 제한된 범위에서 안전하게 수정하고 기존 기능을 유지합니다.

### 기능

- 필요할 때 최신 디자인 경향 조사
- 적절한 Animation·Transition 후보
- Font Size·Weight·Line Height·Width·줄바꿈·색상
- 여백·모서리·Border·Shadow·Card 표현
- Section과 자식 Board 순서
- 영역 표시·숨김
- 변경 전후 Preview
- 원래대로·미리보기·적용
- Draft → 검증 → 적용
- Revision 단위 이력
- 부분 Undo
- `prefers-reduced-motion`
- 모바일·PC 회귀검증

### 제외

- Figma 수준 자유 Canvas
- 모든 요소 자유 Drag & Drop
- 자유 CSS 입력
- 항상 실행되는 Trend 감시 Agent
- 과도한 Motion
- 검증 없는 제품 덮어쓰기

### PASS

- 허용 Section·Token·Component만 수정합니다.
- 변경 전후를 비교하고 취소할 수 있습니다.
- 적용마다 Quick Change Run과 Revision ID가 생성됩니다.
- 모바일·PC 핵심 기능과 접근성이 유지됩니다.
- 사용자 Dirty 변경을 포함하지 않고 Commit/Snapshot 후보를 만듭니다.

---

## 15. PM7 — 전체 통합·최종 검증·결과 전달

### 목적

PM1~PM6이 하나의 자연스럽고 복구 가능한 제작 흐름으로 작동하며, 완성 결과를 고객에게 전달할 수 있게 합니다.

### 전체 흐름

```text
프로젝트 시작·등록
→ 자료와 Reference 조사
→ AI 의도 확인
→ 디자인 Preview 비교
→ 사용자 선택
→ 구현
→ 부분 수정
→ 최종 Preview
→ 사용자 통과
→ Commit 또는 Snapshot
→ Rollback·Restore
→ 전달 패키지
```

### 기능

- PM 간 상태와 Artifact 전달
- 프로젝트 교차 작업 차단
- 마지막 성공 단계부터 재개
- 실패 단계·원인·안전 여부 표시
- AI 변경 파일만 Commit 후보로 분리
- Commit 전 변경 목록
- Result Commit 또는 비Git Snapshot
- Rollback·Restore 검증
- 최종 Preview
- 구현·제외 기능 목록
- 실행 방법
- 알려진 제한사항
- 검증 보고서
- 복구 지점
- 고객용 완료 보고서
- 최종 전달 패키지

### 제외

- 자동 배포
- 팀 협업
- AI Provider Marketplace
- 무인 제작·승인
- 외부 계정 자동 연결

### PASS

- 초보 사용자가 자연어와 Preview로 전체 과정을 완료합니다.
- 프로젝트·Run·Artifact 혼합이 0건입니다.
- 실패 지점에서 안전하게 중단·재개합니다.
- 기존 Dirty 변경 손실이 0건입니다.
- 승인 결과를 Commit/Snapshot으로 저장합니다.
- 별도 Worktree에서 Rollback·Restore를 재현합니다.
- 전달 패키지로 다른 세션에서 실행·검증 방법을 확인할 수 있습니다.

---

## 16. 오류와 재개 모델

| 오류 종류 | 기본 영향 범위 | 기본 처리 |
|---|---|---|
| 환경 오류 | 해당 Runtime/Preview | PM0 또는 환경 점검으로 이동 |
| 프로젝트 코드 오류 | 해당 Project Run | 기존 Result 보존, 구현 단계 재개 |
| 자료 수집 실패 | 해당 Source | 다른 Source 유지, `needs_more_source` |
| Intent 불일치 | 구현 Gate | 구현 차단, 질문 하나 |
| Preview 실패 | 해당 Preview Session | Shell·다른 Project 유지 |
| 검증 실패 | 대상 Result | 승인 금지, Revision 생성 |
| Commit 실패 | 저장 단계 | 파일 유지, 자동 재시도 금지 |
| Restore 실패 | 복구 단계 | 원본 보존, 수동 확인 요청 |

사용자 기본 오류 보고:

```yaml
error_report:
  what_failed: required
  existing_result_safe: required
  retry_possible: required
  user_action: required
  resume_from: required
  technical_details: optional
```

---

## 17. Undo·Commit·Rollback·Restore

```text
Undo: 제품 적용 전 Draft 변경 취소
Commit: 승인된 AI 변경만 Git에 저장
Rollback: 이전 Git Commit의 정상 동작 확인
Restore: 결과 Commit 또는 Backup으로 다시 복구
Snapshot: Git이 없는 프로젝트의 승인 상태 보존
```

### 공통 안전 조건

- 기존 Dirty 변경 자동 포함 금지
- AI 변경 파일과 기존 변경 분리
- Commit 전 대상 파일 표시
- 사용자 승인 전 Commit 금지
- 별도 Worktree에서 Rollback·Restore
- 실패 시 현재 작업 폴더를 강제 Reset하지 않음

### PM별 완료 Commit 정책

각 PM은 사용자 기능·기술 검증·복구 증거가 모두 PASS한 뒤 하나의 독립 Result Commit으로 완료합니다. 진행 중 Draft, 실패 Run, 사용자 Dirty 변경과 다음 PM 작업을 섞지 않습니다.

```yaml
pm_completion_commit:
  one_result_commit_per_pm: true
  requires:
    - pm_pass_criteria_complete
    - codex_verification_pass
    - user_result_pass
    - allowed_path_diff_only
    - rollback_restore_evidence
    - wiki_and_current_state_update
  excludes:
    - unrelated_user_dirty_changes
    - diagnostic_and_failed_runs
    - cache_and_temp_files
    - next_pm_work
  naming: "feat(pmN): complete <milestone-name>"
```

PM 완료 Commit 이후에만 `CURRENT_STATE`, Roadmap, Handoff와 다음 활성 PM을 갱신합니다. 한 PM을 여러 기술 Commit으로 나눌 필요가 있으면 작업 Branch 내부 Commit은 허용하지만 공식 완료점은 마지막 Result Commit 하나로 식별합니다.

---

## 18. 공통 검증 기준

```yaml
responsive:
  viewports: [390, 430, 1440]
  horizontal_overflow: false

accessibility:
  keyboard_core_flow: pass
  visible_focus: pass
  text_contrast: wcag_aa
  reflow: pass
  reduced_motion: supported

project_isolation:
  cross_project_run_mix: 0
  cross_project_artifact_mix: 0
  cross_project_preview_mix: 0

git_safety:
  user_dirty_changes_lost: 0
  unrelated_files_in_result_commit: 0

recovery:
  resume_from_last_successful_step: true
  rollback_passed: true
  restore_passed: true

delivery:
  final_preview: required
  verification_report: required
  result_commit_or_snapshot: required
  run_instructions: required
  known_limitations: required
  restore_point: required
```

---

## 19. PM 의존성과 착수 Gate

```yaml
PM0:
  depends_on: []
  blocks_actual_implementation: true

PM1:
  design_sample_allowed_before_pm0: true
  actual_implementation_requires: [PM0_PASS]

PM2:
  requires: [PM0_PASS, PM1_CORE_UI_CONTRACT_PASS]

PM3:
  requires: [PM1_PROJECT_CONTEXT, PM2_PROJECT_REGISTRY]

PM4:
  requires: [PM2_PROJECT_IDENTITY, PM3_SOURCE_SCHEMA]

PM5:
  requires: [PM3_REFERENCE_COLLECTION, PM4_APPROVED_INTENT]

PM6:
  requires: [PM5_APPROVED_DESIGN_SOURCE]

PM7:
  requires: [PM1_TO_PM6_VERIFIED]
```

PM 번호는 구현 순서를 나타내지만 PM4의 간단한 Intent Receipt는 PM1부터 수동 계약으로 사용합니다. PM4에서 이를 Core 일반 기능으로 완성합니다.

---

## 20. 중복·누락 검토

```yaml
responsibility_map:
  PM0: environment_and_recovery_gate
  PM1: user_visible_thin_shell
  PM2: local_project_registry
  PM3: evidence_and_reference_collection
  PM4: intent_alignment_and_scope_gate
  PM5: structural_design_alternatives
  PM6: controlled_revision
  PM7: end_to_end_delivery_and_recovery
```

- PM3는 자료를 확보하며 디자인을 생성하지 않습니다.
- PM5는 자료를 이용해 디자인 후보를 생성합니다.
- PM6은 선택된 디자인만 수정합니다.
- PM4는 구현 전후 의도 일치를 담당합니다.
- PM7은 각 PM 기능을 다시 만들지 않고 통합 흐름을 검증합니다.
- PM1은 모든 기능을 노출하는 얇은 화면이며 상태 소유자가 아닙니다.
- PM2는 프로젝트 Registry이며 실제 파일 관리자가 아닙니다.
- PM0은 사용자 기능이 아니라 실제 구현 착수 Gate입니다.

새 PM을 추가해야 할 기능적 누락은 없습니다.

---

## 21. 의도적으로 제외한 기능

```yaml
excluded_from_post_mvp:
  - saas_user_authentication
  - in_app_payment
  - tenant_isolation
  - team_collaboration
  - automatic_deployment
  - ai_provider_marketplace
  - unattended_automatic_approval
  - freeform_figma_level_canvas
  - unrestricted_drag_and_drop
  - runtime_plugin_marketplace
  - default_vector_database
  - login_or_paywall_bypass
  - threads_bulk_scraping
```

---

## 22. 구현 전 사용자 준비사항

### 지금 필요한 것

- PM0 외부 Backup 위치 선택
- Antigravity 격리 Sandbox 권한 설정 시 sudo 입력
- PM1 실제 Visual Target 후보 확인과 선택

### PM별 나중에 필요한 것

- PM3: 사용자가 가진 Threads·Screenshot·Reference
- PM5: 디자인 후보 선택 또는 혼합 의견
- PM6: 수정할 영역과 원하는 변화
- PM7: 최종 결과 통과 판정

### 현재 불필요

- Figma 유료 연결
- Mobbin API
- 신규 Vector DB
- 신규 수집 Server
- SaaS Auth·결제
- 자동 배포 환경

---

## 23. 현재 구현 판정

```yaml
post_mvp_design:
  pm0_to_pm7_scope: approved
  entity_model: approved
  state_model: approved
  execution_safety_contract: approved
  design_reference_contract: approved
  error_resume_model: approved
  measurable_pass_criteria: approved
  duplicate_and_gap_review: pass
  status: completed

implementation:
  pm0: blocked_until_operational_checks_pass
  pm1_visual_sample: allowed
  pm1_product_implementation: prohibited_until_pm0_pass
  pm2_to_pm7: not_started
```

---

## 24. 다음 작업 하나

```text
PM0 전용 Worktree에서 남은 운영 Blocker를 해소하고 Preflight를 재실행한다.
```

남은 핵심 Blocker:

1. Antigravity의 `--no-sandbox` 없는 격리 실행
2. 병원·PDF 독립 Worktree와 `5173`·`5174 --strictPort` Preview
3. Preview 장애 격리
4. 외부 Backup과 Restore 표본
5. 새 세션 재현

PM0 진행 중에도 PM1 Concept Sample과 Visual Target 후보 설계는 가능하지만 실제 제품 코드는 수정하지 않습니다.

---

# Post-MVP 설계 완료

PM0~PM7의 목적, 사용자 기능, 제외 범위, 데이터·상태 모델, 실행 안전 계약, 디자인 흐름, 오류·재개, Commit·복구, 정량 PASS와 통합 전달 기준을 확정했습니다.

다음 단계는 설계 추가가 아니라 PM0 운영 Gate 완료입니다. PM0 PASS 전에는 실제 PM1 제품 구현을 시작하지 않습니다.
