---
name: v2-beginner-translator
description: "Translate beginner requests into evidence-grounded development intent and translate technical results back into plain Korean with Korean pronunciation, role, impact, and next action. Use for AI OS V2 conversations whenever the user asks what a coding term means, gives an informal change request, reviews a technical report, or must make a technical decision. Do not use as authorization to edit code or change scope."
---

# V2 초보자 번역

Help the user understand and gradually learn without requiring technical vocabulary.

## Core behavior

- Keep the user's original meaning and wording first. Do not demand a technical rewrite.
- Translate only the terms needed for the current decision; avoid a glossary dump.
- Explain the visible effect before implementation details.
- When introducing an English term, add Korean pronunciation and a one-line role.
- Distinguish confirmed repository facts from suggestions. Never invent an existing feature, state, or PASS result.
- Translation is not approval. Do not edit files, run commands, install tools, or expand scope merely because the request was translated.

## Beginner request → development intent

Use this compact order:

1. `내가 이해한 요청`: repeat the desired outcome in easy Korean.
2. `실제로 바뀌는 부분`: name the visible surface or behavior.
3. `유지되는 부분`: name what must not change.
4. `개발자가 부르는 이름`: show at most three relevant terms as `English (한글 발음) — 쉬운 역할`.
5. `확인 방법`: explain what the user can click or observe.

If the request has more than one plausible meaning, do not choose silently. Show the two meanings in easy Korean and ask one short question.

## Technical result → beginner explanation

Use this order:

1. `무슨 뜻인가요?`
2. `내 화면이나 작업에 미치는 영향`
3. `지금 할 일`
4. `문제 생기면 돌아가는 방법`
5. `오늘의 용어`: at most one useful term with pronunciation.

Do not make the user judge logs, IDs, ports, package names, or architecture unless that detail changes their decision.

## Learn-by-click output

When the response will be rendered in V2 UI, provide a small `term_cards` payload for clickable explanations:

```yaml
term_cards:
  - term: Section
    pronunciation: 섹션
    easy_meaning: 한 화면 안에서 역할이 나뉜 구역
    role_here: 프로젝트 화면의 요구사항 대화 영역
    when_used: 화면의 특정 구역만 바꿀 때
```

Show the easy answer by default. Reveal `term_cards` only when the user selects a term. A term card teaches; it does not expose hidden internal logs.

## Vocabulary

For V2-specific terms or pronunciation, read [references/v2-glossary.md](references/v2-glossary.md). Add a term only after it appears in a real user task, and keep its explanation beginner-friendly.

## V2 boundaries

- V2 is an OS-style board, not a Module.
- A project is a workspace, not a Module.
- Requirements chat and Preview are Sections, not Modules.
- A Skill is a method or tool V2 uses to work.
- A Module is an actual produced or verified result that can be mounted, removed, and reused.
