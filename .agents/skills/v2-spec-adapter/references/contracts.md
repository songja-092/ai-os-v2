# V2 Spec Adapter Contracts

## Spec Lite

```yaml
spec_lite:
  schema_version: "1.0"
  request_id: string
  project_id: string
  original_request: string
  target:
    surface_id: string
    section_id: string
    selected_by_user: boolean
    resolution_evidence: string
  change:
    command: string
    property: string
    requested_direction: string
    exact_value: string | null
  preserve: []
  done_when: []
  regression_checks: []
  assumptions: []
  unresolved_questions: []
  approval:
    required: true
    status: pending | approved | revision_requested | cancelled
```

`exact_value` may remain null when the user asks for a relative change such as `늘려줘`. The
implementation must first create a Draft that fits the surrounding layout; it may not silently turn
the relative request into an unrestricted resize.

## User-facing confirmation

```text
이렇게 이해했습니다: 요구사항 창을 더 길게 만듭니다.
그대로 유지합니다: 메뉴, Preview, 현재 프로젝트와 동기화 상태
확인 방법: 변경 전후 화면과 기존 메뉴 동작을 함께 확인합니다.

[이대로 진행] [다르게 수정] [중단]
```

Do not show Section IDs, task IDs, Git, Port, Run, Hash, or internal gate names unless the user opens
technical details.

## Promote Lite to Full when

- more than one independently owned Section must change;
- a new Module, persistent data, permission, external service, payment, deployment, or migration is
  required;
- more than one project is affected;
- preserving existing behavior cannot be proven with bounded checks;
- the implementation requires several agents or sessions;
- the same intent has already been implemented incorrectly more than once.

## Required Full artifacts

- confirmed V2 production-scope receipt;
- Spec Kit `spec.md` with user stories and measurable success criteria;
- `plan.md` with technical boundaries and locked dependencies;
- `tasks.md` that maps work and tests to user stories;
- read-only Analyze result with requirement coverage;
- V2 handoff that separates implementation permission from specification approval.
