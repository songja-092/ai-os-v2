# Spec Kit V2 Adapter 격리 Pilot — 2026-08-21

## 목적

사용자의 쉬운 자연어가 구현 과정에서 다르게 해석되는 병목을 줄이기 위해 GitHub Spec Kit을 V2의 명세·작업 분리 보조 도구로 사용할 가치가 있는지 확인했습니다.

## 격리 조건

- 공식 Source: `github/spec-kit`
- 고정 Tag: `v0.16.5`
- 설치 시 해석된 Source Commit: `87a0e9715d59079e46b44208ba009bf1a6976643`
- CLI: `specify 0.16.5`
- 격리 경로: `/home/user/바탕화면/v2_spec_kit_pilot`
- 전체 격리 크기: 약 `23M`
- V2 Core·제품·PM 잠금 파일 접근: 없음
- 비공개 고객 자료 입력: 없음
- 전역 PATH·전역 Codex Skill 변경: 없음
- 제품 구현·Run·배포: 없음

## 가짜 사용자 요청

> 프로젝트 작업실에서 요구사항 전달 영역을 카톡처럼 길게 만들어줘. 왼쪽에 두고 Preview와 메뉴는 그대로 유지해줘. 메시지와 파일을 보낼 수 있게 해줘.

과거 화면 수정 중 메뉴·Preview가 사라진 회귀와 같은 종류의 문제를 일부러 선택했습니다.

## 생성 결과

Spec Kit의 Codex Skill·Template 흐름을 사용해 다음을 만들었습니다.

- `spec.md`: 사용자 시나리오, 변경 범위, 유지 범위, 오류 상황, 성공 기준
- `checklists/requirements.md`: 명세 완전성 검사
- `plan.md`: 구현 경계와 수정 금지 영역
- `research.md`: 선택 이유와 제외한 대안
- `contracts/ui-contract.md`: 입력·출력·유지·금지 계약
- `quickstart.md`: 실제 확인 순서
- `tasks.md`: 구현·검사 작업 목록

측정값:

```yaml
artifact_count: 7
functional_requirements: 11
success_criteria: 4
implementation_and_test_tasks: 20
spec_sha256: 468eb4870eba2cc460f139a6dfaafaf6ddb4203a4852661da9a1aaa9e17180e5
plan_sha256: 1c269f5b7914bb9a3be0b7d6d2dd361e1b0f76ddd5c5f0151c3f5a5926d2517b
tasks_sha256: d6272f0c113d3a1215b3f8e3f4892627f04ced300e3e768a4dcd6b23dc3a3472
```

## 자연어 보존 결과

| 사용자 의미 | Spec·Task 보존 |
|---|---|
| 카톡처럼 긴 요구사항 대화 | PASS |
| 왼쪽 Section | PASS |
| 메시지 전송 | PASS |
| 파일 선택·확인·제거·전송 | PASS |
| 기존 메뉴 유지 | PASS — 메뉴 7개를 회귀검사 대상으로 고정 |
| Preview 유지 | PASS — 선택 프로젝트·동기화 상태까지 보존 |
| 다른 부분을 건드리지 않음 | PASS — `requirements-chat` Section으로 범위 제한 |
| 적용 전 사용자 확인 | PASS — 적용·수정·중단 Gate 포함 |

사용자 문장에 없지만 과거 오류 증거와 V2 계약에서 필요한 긴 Text Overflow, 전송 실패 Draft 보존, Section 오류 격리, PM 잠금 Hash 검사도 작업으로 추가됐습니다.

## 확인된 장점

- 사용자의 짧은 문장을 구현 가능한 요구사항과 검사 기준으로 바꿉니다.
- `바꿀 것`뿐 아니라 `유지할 것`을 Task와 회귀검사까지 전달합니다.
- 기능 요구사항과 기술 계획을 분리해 사용자가 쉬운 문서를 볼 수 있습니다.
- Requirement→Plan→Task Artifact가 남아 세션이 바뀌어도 의미 손실을 줄일 수 있습니다.
- `analyze` 단계로 명세·계획·작업의 누락과 충돌을 읽기 전용 검사할 수 있습니다.

## 확인된 한계

- 작은 UI 수정에도 Artifact 7개와 Task 20개가 생겨 매번 Full Flow를 실행하면 과합니다.
- Spec Kit은 사용자의 진짜 의도를 스스로 확정하지 못하므로 V2 Interview와 사용자 확인을 대체하지 못합니다.
- 디자인 후보 탐색·Visual Target·사용자 취향 판정 기능은 없습니다.
- PM 승인·Core 상태·Module Registry·Version Restore를 대체하지 못합니다.
- Agent가 명세를 작성하므로 잘못된 가정은 여전히 생길 수 있으며 사용자 확인과 독립 검증이 필요합니다.

## V2 권장 Adapter

```text
사용자 자연어
→ V2 Interview
→ 쉬운 제작 범위 확인서
→ 사용자 확인
→ 요청 규모 판정
   ├─ 작은 수정: Spec Lite
   └─ 새 프로젝트·큰 기능: Spec Full
→ Antigravity 구현용 명세·작업
→ Codex 최초 요청·명세·결과 검증
→ 사용자 승인
→ V2 Version·Restore
```

### Spec Lite

작은 수정은 다음 네 항목만 생성합니다.

- 바꿀 것
- 유지할 것
- 완료 기준
- 회귀검사

Full Plan·Research·Data Model·20개 수준의 Task 분해는 생략합니다.

### Spec Full

다음 경우에만 Spec Kit 전체 흐름을 사용합니다.

- 새 프로젝트
- 큰 기능
- 여러 Section·Module 변경
- 보안·결제·데이터·배포 영향
- 작업이 여러 Agent나 세션으로 나뉨
- 같은 요구가 반복해서 잘못 전달됨

## 제거 방법

격리 Pilot을 폐기할 때 `/home/user/바탕화면/v2_spec_kit_pilot`만 제거하면 됩니다. 전역 PATH와 V2 Core에 연결하지 않았으므로 기존 V2 Workflow는 그대로 유지됩니다.

## 판정

```yaml
spec_kit_source: verified_official_tag
isolated_install: PASS
natural_language_to_spec: PASS
preserve_scope_and_regression_requirements: PASS
small_change_full_flow: TOO_HEAVY
v2_interview_replacement: false
v2_pm_replacement: false
recommended_role: removable_spec_adapter
recommended_modes:
  spec_lite: small_changes
  spec_full: new_projects_and_large_features
core_adoption: pending_user_review
verdict: PASS_WITH_FIX
```
