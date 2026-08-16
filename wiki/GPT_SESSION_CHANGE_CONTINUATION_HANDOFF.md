# AI OS V2 — GPT 세션 변경 후 작업 지시서

아래 내용을 새 GPT 세션에 그대로 전달한다.

---

AI OS V2의 Post-MVP 작업을 이어서 진행해줘.

과거 대화나 GitHub main만으로 현재 상태를 추정하지 말고, 아래 로컬 저장소·최종 설계 보고서·Run Artifact를 직접 읽은 뒤 판정해.

## 1. 확인 경로

### 최종 설계 원본

- `/home/user/문서/ai스튜디오/AI_OS_V2_POST_MVP_FINAL_DESIGN_REPORT.md`
- `/home/user/문서/ai스튜디오/GPT_POST_MVP_DESIGN_COMPLETION_HANDOFF.md`

### Core와 Obsidian Wiki

- `/home/user/바탕화면/ai_os_v2`
- `/home/user/바탕화면/ai_os_v2/wiki`

### PM1 디자인 Preview

- `/home/user/바탕화면/V2_UI/pm1-clickable-preview`
- `/home/user/바탕화면/V2_UI/PM1_visual_targets_v2`
- `/home/user/바탕화면/V2_UI/PM1_visual_targets_v2_evidence`
- `/home/user/바탕화면/V2_UI/PM1_mobile_first_v3_options`
- `/home/user/바탕화면/V2_UI/PM1_mobile_first_v3_evidence`

### 제품 저장소

- `/home/user/바탕화면/test_project`

## 2. 현재 확정 상태

```yaml
core_mvp: M1_to_M7_completed_and_frozen
post_mvp_plan: PM0_to_PM7
post_mvp_design: completed
current_stage: PM1_design_preview
pm1_visual_ui: preview_only
pm1_product_ui: not_started
pm1_core_integration: not_started
image_to_code_for_product: not_started
```

최종 설계 보고서에는 정확히 `Post-MVP 설계 완료`가 선언돼 있다. PM0~PM7의 목적·기능·제외 범위·PASS·의존성과 실행 안전 계약은 이 보고서를 기준으로 사용한다.

다만 설계 완료와 Git 공식 저장은 분리해서 판정해야 한다.

```yaml
final_design_documents_exist: true
final_design_documents_git_commit: not_verified
core_wiki_pm0_to_pm7_sync: not_verified
github_main_sync: not_verified
```

`/home/user/문서/ai스튜디오`는 마지막 확인 당시 `No commits yet`이었고 최종 설계 문서 두 개는 미추적 상태였다. Core Wiki에는 과거 PM1~PM4 계획이 남아 있을 가능성이 있다. 따라서 PM0~PM7 설계를 다시 논의하지 말고, 먼저 실제 Git 상태와 공식 문서 동기화 여부를 확인해야 한다.

## 3. 공식 PM 구조

1. `PM0 — 운영환경 준비`
2. `PM1 — 대시보드·프로젝트 작업실`
3. `PM2 — 로컬 프로젝트 관리`
4. `PM3 — 자료·디자인 Reference 수집`
5. `PM4 — 사용자 의도 확인`
6. `PM5 — 디자인 다양성 생성·비교`
7. `PM6 — 최신 디자인·모션·부분 수정`
8. `PM7 — 전체 통합·최종 검증·결과 전달`

이 구조를 과거 Core Wiki의 PM1~PM4로 되돌리지 않는다. PM0~PM7을 새로 설계하지도 않는다. 최종 설계 보고서의 내용을 공식 저장 위치에 안전하게 동기화하는 것이 우선이다.

## 4. 현재 PM1 작업의 정확한 성격

지금까지 만든 UI는 PM1 제품 구현이 아니라 설계 Preview와 Visual Target 후보이다.

다음과 혼동하지 않는다.

```yaml
pm1_design_preview: in_progress
pm1_product_implementation: false
v2_core_modification_for_pm1: false
official_visual_target_approved: false
```

최근 방향:

- 전역 대시보드와 프로젝트 작업실 분리
- 전역 `디자인` 메뉴 제거
- 기능 없는 `HJ` 사용자 Avatar 제거
- 프로젝트가 10~50개일 때 검색·유형 필터·목록으로 관리
- 디자인은 프로젝트 제작 단계 안에서 처리
- 모바일 390px 우선, 이후 430px, 마지막 PC
- 모바일 작업실은 작은 휴대폰 Mockup이 아니라 Preview가 주 작업 영역
- Docker는 운영환경 상태 진입점 후보이며 무제한 관리 Console이 아님

사용자는 방금 제시된 모바일 시안 세 개를 모두 거절했다. 따라서 시안 1·2·3 중 하나가 선택됐다고 기록하면 안 된다.

## 5. 디자인 기록 의무

앞으로 모든 UI 작업은 다음 Provenance를 남긴다.

```yaml
design_provenance:
  references_used: []
  tools_used: []
  skills_used: []
  generated_with:
  implemented_with:
  verified_with:
  input_images: []
  prompts: []
  source_viewport: 390x844
  derived_viewports: [430x932, 1440x950]
  section_ids: []
  section_order: []
  user_decision: pending
  rejection_reason:
```

예:

- UI UX Pro Max를 실제 사용했으면 `UI UX Pro Max`라고 기록
- Figma를 실제 사용했으면 Figma File·Node URL과 역할 기록
- built-in ImageGen이면 `OpenAI built-in ImageGen`이라고 기록
- 사용하지 않은 도구는 `not_used`로 구분하고 사용했다고 표현하지 않음
- Reference는 URL·조회일·적용 영역·License 또는 이용 조건 기록

색상만 다른 후보는 디자인 다양성으로 인정하지 않는다. 정보 우선순위·Navigation·Section 순서·밀도·CTA 위치·모바일 흐름이 구조적으로 달라야 한다.

디자인 Reference 수집은 새 PM이 아니라 PM3의 제한형 Workflow다. 프로젝트 요청 또는 사용자의 `Reference 다시 찾기`로 시작하며 Collector → Analyzer → 사용자 Curator 흐름을 사용한다. 항상 실행되는 감시 Agent, 대량 Scraping, Queue·Worker·별도 DB는 현재 범위에 포함하지 않는다.

## 5-1. PM 완료 Commit 규칙

- PM 하나를 완료할 때마다 별도 Result Commit 하나를 만든다.
- PM PASS, Codex 검증 PASS, 사용자 PASS와 Rollback·Restore 증거 전에는 완료 Commit을 만들지 않는다.
- 다른 PM 작업, 실패 Run, 사용자 Dirty 변경과 캐시를 포함하지 않는다.
- 완료 Commit 뒤에만 Wiki·CURRENT_STATE·다음 활성 PM을 갱신한다.
- 권장 제목은 `feat(pmN): complete <milestone-name>`이다.

## 6. 디자인이 마음에 들지 않을 때

```text
현재안 보존
→ 사용자가 싫다고 한 화면·Section 확인
→ rejection_reason 기록
→ 유지할 부분과 버릴 부분 분리
→ Reference 재수집
→ 구조가 다른 후보 생성
→ 390px에서 먼저 확인
→ 선택 또는 혼합
→ 단일 Visual Target
→ 430px·PC 파생
→ 사용자 승인
→ 승인 후에만 Image-to-Code
```

사용자가 거절한 시안을 삭제하거나 덮어쓰지 말고 Versioned Evidence로 보존한다.

## 7. 새 GPT가 가장 먼저 할 작업 하나

### 작업명

`PM0~PM7 최종 설계·Core Wiki·PM1 Preview의 로컬 공식 상태 동기화 감사`

### 읽기 전용 확인

1. 세 저장소의 HEAD·Branch·Remote·Dirty 상태
2. `/home/user/문서/ai스튜디오`의 Git 상태와 최종 설계 문서 존재 여부
3. Core Wiki가 PM0~PM7인지 과거 PM1~PM4인지
4. `run-ef4986d7`의 실제 상태와 Commit된 상태 차이
5. PM1 Preview 저장소에서 Commit된 파일과 미추적 디자인·코드 분리
6. 최근 Visual Target·모바일 시안이 공식 Run에 등록됐는지
7. Obsidian Wiki와 Git 문서가 같은 내용을 가리키는지
8. 사용자 Dirty Run·`v2`·IDEA_ARCHIVE·캐시를 제외하고 안전하게 Commit할 수 있는 파일 목록

### 첫 작업에서 금지

- PM0~PM7 재설계
- 새 Visual Target 생성
- PM1 제품 구현
- V2 Core 코드 수정
- Run 생성·상태 변경
- 패키지·Skill 설치
- Dirty 파일 Reset·Restore·Stash
- 기존 Run 자동 Commit
- Commit·Push

첫 감사에서는 Commit하지 말고 정확한 동기화 대상 목록과 Commit 계획만 보고한다. 사용자 승인을 받은 뒤 설계 문서·Obsidian Wiki·PM1 Preview를 저장소별로 분리 Commit한다.

## 8. 기존 Dirty 변경 보호

Core 저장소에는 사용자 소유의 Dirty 변경이 남아 있을 수 있다.

보존 대상:

- 기존 실패·진단 Run
- `run-ef4986d7`의 미커밋 상태
- `v2` 코드 변경
- `wiki/GOAL.md`
- IDEA_ARCHIVE
- `__pycache__`, `tmp`, 기타 캐시
- 사용자 생성 이미지와 별도 Evidence

정확한 소유권을 확인하기 전에는 Stage하지 않는다.

## 9. 첫 보고 형식

```yaml
authoritative_design:
  source_files: []
  pm_structure:
  design_completed:
  contradictions: []

repositories:
  core:
    head:
    branch:
    origin_main:
    dirty_files: []
  preview:
    head:
    branch:
    dirty_files: []
  product:
    head:
    branch:
    dirty_files: []

current_work:
  exact_classification:
  official_run:
  visual_target_approved:
  product_implementation_started:

sync_plan:
  core_wiki_files: []
  preview_files: []
  excluded_user_dirty_files: []
  proposed_commits: []
  push_required:

verdict: PASS | PASS_WITH_FIX | BLOCKED
next_single_action:
```

## 10. 판정 원칙

- 최종 설계 원본은 PM0~PM7이다.
- `Post-MVP 설계 완료` 상태를 다시 미완료로 되돌리지 않는다.
- 설계 완료를 PM1 제품 구현 완료로 해석하지 않는다.
- PM1 Preview가 존재해도 사용자 승인 Visual Target과 Fidelity PASS 전에는 제품 UI 구현 완료가 아니다.
- 파일 존재, Git Commit, Push, Run 등록과 사용자 승인을 서로 다른 상태로 기록한다.
- 문서 충돌을 발견하면 기억으로 고치지 말고 정확한 파일·Commit·Diff를 보고한다.

---

이 지시서를 읽은 새 GPT의 첫 행동은 추가 디자인이나 구현이 아니라 읽기 전용 동기화 감사이다.
