# Design artifact contract

Use one manifest per Visual Target or implemented revision.

## Required identity

- `artifact_version`: contract version, currently `1.0`.
- `project_id`: stable project identifier.
- `target_surface`: `v2_board` or `customer_product`.
- `status`: `draft`, `awaiting_user_review`, `approved`, `implemented`, `verified`, `rejected`, or `discarded`.
- `viewport`: width, height, theme, and motion state used for comparison.

## Evidence

- `brief`: purpose, primary task, required information, untouched areas, prohibited patterns.
- `references`: URL or local image, checked date, used part, license/access status, selected properties, excluded content and branding.
- `tools`: tool name, version or source identity, role, inputs, outputs, and whether it changed files.
- `implementation_candidates`: Block or component source, immutable hash, dependencies, target Sections, and modifications.
- `visual_target`: image path, SHA-256, prompt record, and approval state.
- `changes`: Section ID, property, before, after, source, and target viewport.
- `verification`: technical Gate and design-finish Gate recorded separately.

## Promotion rules

1. Keep extractor output untrusted and isolated.
2. Normalize selected values into the V2-owned Recipe or artifact.
3. Require user approval before `approved`.
4. Require rendered verification before `verified`.
5. Never overwrite a prior Version; Restore creates a new draft.
6. Removing a tool must not remove an approved Recipe, source record, Visual Target, or verification result.
