---
name: v2-spec-adapter
description: Convert a beginner's short natural-language request into a scope-safe V2 Spec Lite or Spec Full without making the user write technical requirements. Use before implementing new V2 projects, large features, or UI changes where target, preservation rules, acceptance criteria, task splitting, or regression checks must be made explicit.
---

# V2 Spec Adapter

The user may say only what they can naturally express, such as `요구사항 창을 늘려줘`.
Do not ask them to rewrite it in developer language. Preserve the original sentence and derive the
technical contract from the currently selected project, Section, approved Recipe, locked PMs, and
repository evidence.

## Invariants

- The user's original sentence is immutable evidence. Do not replace it with an inferred summary.
- Resolve an obvious target from the selected screen and V2 Section IDs before asking a question.
- Ask one easy question only when multiple interpretations materially change the result and no safe
  default or selected target exists.
- A short request does not authorize changing adjacent Sections, menus, Preview state, Core state,
  locked PM files, or customer data.
- Always define `change`, `preserve`, `done_when`, and `regression_checks` before implementation.
- Show the user a short confirmation, never the internal YAML or developer task list by default.
- Spec Kit artifacts are derived implementation inputs. V2 Intent Packet, user approval, Core state,
  Design Recipe, Module Manifest, Version, and Restore remain the source of truth.
- Do not implement, install, apply, commit, push, or mark PASS merely because a spec was generated.

## Choose the smallest mode

Use **Spec Lite** for one clear Section, property, copy, spacing, size, visibility, order, or small
behavior change that can be verified with a bounded regression check.

Use **Spec Full** for a new project, a new Module, several Sections, data or permission changes,
security, payment, deployment, multiple sessions or agents, or a request that repeatedly failed due
to lost intent.

If the mode is uncertain, start with Lite and promote to Full only when the discovered scope proves
that Lite cannot safely describe the work.

## Spec Lite flow

1. Read the active project, selected screen or Section, current PM, locked PM contract, and allowed
   actions.
2. Preserve the exact user sentence.
3. Resolve the target and convert the request to one bounded change command.
4. Derive adjacent state that must not change.
5. Define visible completion criteria and the smallest regression checks.
6. Show only:
   - `이렇게 이해했습니다`
   - `그대로 유지합니다`
   - `확인 방법`
   - `이대로 진행 | 다르게 수정 | 중단`
7. After user confirmation, pass the internal Lite contract to the implementation agent.

Read [references/contracts.md](references/contracts.md) for the exact Lite contract and promotion
rules.

## Spec Full flow

1. Start from the confirmed V2 Interview and production-scope receipt.
2. Use the existing repo-local Spec Kit skills in order:
   `speckit-specify → speckit-clarify when needed → speckit-plan → speckit-tasks → speckit-analyze`.
3. Keep the user-facing receipt short while storing technical artifacts for agents.
4. Stop before implementation when Analyze finds a critical conflict or an uncovered requirement.
5. Require user confirmation again if clarification changes cost, scope, privacy, design direction,
   delivery, or preserved behavior.

Do not run `speckit-implement` automatically. Implementation remains a separately authorized V2
handoff.

## Completion report

Report the original request, chosen mode, resolved target, protected scope, confirmation status,
artifact paths, unresolved risks, and next single action. Clearly distinguish `specified`,
`approved`, `implemented`, and `verified`.
