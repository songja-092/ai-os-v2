# Adopted reference automation

Use this only after the user has decided `adopt`, `hold`, or `discard` for the relevant trials.

## Input

`selection.json` records the project, target surface, Preview path, and adopted sources. Each source
must include a stable `source_id`, a `trial_path`, one role, the Section IDs it affects, and a short
description of what is used.

## Command

```bash
python3 scripts/reference_flow.py \
  /absolute/path/to/selection.json \
  --recipe /absolute/path/to/design-recipe.json \
  --report /absolute/path/to/verification.json
```

To recheck an existing Recipe without recompiling it, add `--verify-only` and omit the selection path.

## Proven by PASS

- every selected source has a preserved user-adopted trial record;
- the draft Recipe stores the exact trial and Preview hashes;
- every selected source is attached to the intended `data-v2-section` in the visible HTML;
- a changed Preview cannot silently reuse the old verification result.

## Not proven by PASS

- visual quality or user preference;
- Core automatically selecting the best source;
- Core or Antigravity applying the Recipe to a product;
- PM2 or PM3 regression safety after product implementation;
- successful reuse in another project.

Those require separate implementation, visual review, and user approval.
