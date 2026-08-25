# Design Intelligence 실제 구현 상태 감사

작성일: 2026-08-18

## Git 기준

```yaml
pm1_branch: codex/pm1-design-adoption
pm1_head: 2c7863e7c093edc063c1b2d579f8469669e53500
origin_branch_head: 2c7863e7c093edc063c1b2d579f8469669e53500
origin_main: 75f2f4d97ff21ab68cf698dafc8f5190fd1b1d9b
expected_commit_match: true
pm1_worktree_dirty_before_audit: false
core_dirty_preserved: true
preview_dirty_preserved: true
```

## 사용자 PM 수정 승인

2026-08-18 사용자는 Design Intelligence, 디자인 다양성, 가격별 맞춤
제작과 구현 도구 확장을 반영하기 위해 Post-MVP PM을 수정해도 된다고
명시적으로 지시했습니다. Core MVP M1~M7과 과거 Run·Artifact·Commit은 이 승인의
변경 대상이 아닙니다.

## Design Intelligence

```yaml
route: /design-intelligence
status: fixture_ui
candidate_source: hardcoded_catalog_plus_live_public_github_metadata
candidate_count: 8
selection_persistence: json_artifact
collector_connection: not_implemented
recipe_reuse_first: not_implemented
collection_request_schema_connection: not_implemented
lab_queue_connection: not_implemented
trial_result_return_path: not_implemented
inactive_adapter_registration: not_implemented
```

`GET /api/design-intelligence`는 고정된 Collection JSON을 읽고, `POST
/api/design-intelligence/decision`은 `design_intelligence.py decide`를 호출해 사용자의
`채택·보류·폐기`를 같은 JSON에 저장합니다. `채택`은 격리 시험 명령을
`next_action`으로 기록할 뿐 실제 Queue나 Runner를 시작하지 않습니다.

## V2 Capability Lab

```yaml
status: isolated_execution
plugin_manifest: present_and_validated
source_commit_pinning: implemented
static_risk_scan: implemented_pattern_scan_not_security_proof
isolated_home: implemented
bubblewrap_execution: evidenced
network_default: blocked
private_project_mount: prohibited_and_tested_absent
secret_forwarding: false_in_recorded_trials
fixture_only_execution: evidenced_for_two_candidates
timeout: implemented
process_cleanup: bubblewrap_die_with_parent_present_but_post_timeout_residue_not_separately_evidenced
artifact_output: implemented
adopted_registry_count: 0
disable_and_removal: code_path_present_not_end_to_end_verified
```

`impeccable` 시험 3개와 `taste-skill-v1` 구조 시험 1개가 Artifact로
남아 있습니다. 이 증거는 격리 실행을 증명하지만 Core 연결·채택·제거의
종단간 재현을 증명하지는 않습니다.

## v2-design-finish

```yaml
status: executed_with_evidence
skill_file: present_and_validated
entrypoint: scripts/design_run.py
input_output_contract: present
design_dna_seven_axes: present
ui_ux_pro_boundary: recommendation_and_guard_only
core_boundary: documented_not_connected
recipe_ownership: does_not_own_core_recipe
before_after_evidence: present
accessibility_responsive_motion_gates: present
user_approval_gate: present
failure_preservation: documented_and_artifact_present
```

Skill은 Manifest 초기화·환경 점검·Gate 검증을 수행합니다. V2 Core 상태나
Design Recipe를 자동으로 읽고 쓰는 Adapter는 아직 없습니다.

## 판정

```yaml
verdict: PASS_WITH_FIX
documentation_claims_corrected: true
core_or_product_changed: false
new_tool_installed: false
next_single_action: >
  기존 V2 Collection Request·Collector·Analyzer와 Design Intelligence 사이의
  최소 Adapter 계약을 확정하고, 후보 1개에 대해 선택→격리시험→
  결과표시→비활성 Registry 등록→제거를 종단간으로 검증하는 것.
```
