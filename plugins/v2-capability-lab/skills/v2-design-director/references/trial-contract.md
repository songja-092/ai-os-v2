# V2 Design Director trial contract

Each candidate gets one folder under `pm3-artifacts/design-director-trials/<candidate_id>/`.

Required `trial.json` fields:

```json
{
  "schema_version": "1.0",
  "trial_id": "string",
  "candidate_id": "string",
  "candidate_role": "reference_source | implementation_source | visual_workbench | quality_guard",
  "benchmark_brief_id": "v2-ui-project-workspace-v1",
  "status": "prepared | running | ready_for_user | adopted | held | discarded | blocked",
  "source_commit_or_version": "string",
  "queries": [],
  "references": [
    {
      "url": "string",
      "access_checked_at": "ISO-8601",
      "license_status": "verified | unclear | do_not_reuse",
      "selected_part": "string",
      "do_not_copy": []
    }
  ],
  "director_decision": {
    "kept": [],
    "changed": [],
    "rejected": [],
    "reason": "string"
  },
  "visual_output": {
    "url_or_path": "string",
    "viewport": "1440x950",
    "same_fixture": true
  },
  "implementation": {
    "possible": true,
    "dependencies": [],
    "estimated_lock_in": "none | low | medium | high",
    "removal_steps": []
  },
  "comparison": {
    "current_v2_strengths_preserved": [],
    "improvements": [],
    "regressions": [],
    "design_diversity_gain": "none | low | medium | high"
  },
  "user_decision": "pending | adopt | hold | discard",
  "user_reason": ""
}
```

The visible review must show the source links, the parts actually used, the V2 result, and the
current user decision. A Markdown-only result cannot close a visual supplier trial.
