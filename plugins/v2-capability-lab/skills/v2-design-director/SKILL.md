---
name: v2-design-director
description: "Run and record one-at-a-time visual supplier trials for AI OS V2, turning references into a coherent, implementable V2 UI direction without treating 'OS' as a visual style. Use for design exploration, reference adoption, candidate comparison, and user adopt/hold/discard meetings."
---

# V2 Design Director

Use one fixed V2 benchmark brief for every supplier trial. The purpose is to compare whether a
candidate improves the same V2 interface, not whether it can produce an unrelated attractive
screen.

## Invariants

- `V2 is an OS-type production platform` is an architecture statement, not a visual prompt.
- Describe the tested surface as a `modular production workspace` unless the user explicitly asks
  for an operating-system visual metaphor.
- Do not expose private projects, credentials, Git history, Cookies, or unpublished assets to a
  candidate. Use only the approved generated Fixture.
- Test one candidate at a time. Do not merge two unapproved candidates into one result.
- Preserve the same viewport, fixture data, required sections, and interaction state across trials.
- A supplier trial must end in a visible result or an honest `no_visual_output` finding.
- Only the user may decide `adopt`, `hold`, or `discard`.
- Adoption means a removable V2 Adapter or approved reference source; it does not grant Core write
  access and does not replace Design Recipe as the source of truth.

## Per-candidate flow

1. Read the fixed benchmark Brief and the candidate's Capability Lab record.
2. Search or generate only enough references to demonstrate the candidate's real value.
3. Record every source link, access condition, license, query, and selected part.
4. Produce one V2 UI Visual Target using the fixed Fixture.
5. Record what the candidate contributed and what the Design Director changed or rejected.
6. Check implementation feasibility, responsive rules, accessibility risks, and removable fallback.
7. Present the visible result and a short comparison with the current V2 UI.
8. Ask the user for exactly one decision: `채택`, `보류`, or `폐기`.
9. Save the decision without silently changing the next candidate or Core.

## Adopted-source automation

When the user wants to combine adopted sources, keep their roles separate instead of choosing one
winner. Create a small `selection.json` that maps each source to a role and stable Section IDs, then
run `scripts/reference_flow.py`. The script may compile a draft Design Recipe and verify that the
rendered HTML carries the same source-to-Section trace.

The automation must stop when a source is not user-adopted, a Section is missing, or the Preview
hash changes after compilation. It does not judge visual quality, choose sources for the user,
apply a draft to a product, or write to Core. Read [references/adoption-automation.md](references/adoption-automation.md)
before compiling or verifying a combined Recipe.

## End-to-end evidence audit

When the user asks whether the design workflow actually happened, do not infer completion from the
existence of documents or a visible mockup. Read
[references/workflow-evidence.md](references/workflow-evidence.md) and map every stage to its real
input, output, user decision, and hash or Version. Report the first missing handoff as the current
blocker. A Reference trace PASS is not an implementation, Fidelity, final approval, or Restore PASS.

`UI Remix` and `Misty` are research evidence for example search and whole/partial selection. They are
not installed V2 Runtime tools unless a separate audited Adapter and execution evidence exist. Do not
claim that V2 "uses UI Remix" merely because its interaction principle influenced the workflow.

## Required record

Read [references/trial-contract.md](references/trial-contract.md) before starting or closing a
candidate trial. Use the schema there for every trial so a new session can continue without chat
memory.
