---
name: v2-capability-lab
description: "Safely evaluate public GitHub Skills, plugins, CLIs, and open-source capability candidates for AI OS V2. Use when the user asks to discover, trial, compare, adopt, remove, or replace a V2 capability while preventing private project leakage."
---

# V2 Capability Lab

Keep candidate code separate from V2 Core and private projects. Use
`scripts/capability_lab.py` for every lifecycle transition.

## Workflow

1. Accept only a public `https://github.com/<owner>/<repo>` source.
2. Run `prepare`; inspect its static audit before executing anything.
3. Run `fixture`; never use the user's real project as candidate input.
4. Run `trial` in Bubblewrap. Default to no network. Allow public network only when the
   candidate's declared role requires it and the Fixture contains no private data.
5. Show the report to the user. Never infer adoption from a successful exit code.
6. Run `adopt --approved-by-user` only after explicit user selection.
7. Run `discard --approved-by-user` to move a rejected trial into recoverable discarded storage.

## Design Intelligence

Use `scripts/design_intelligence.py collect` to create a public candidate queue. It combines a
small reviewed source catalog in `registry/candidate-catalog.json` with GitHub public metadata,
records its PM stage, activation Gate, freshness and license, and
shows only `adopt`, `hold`, and `discard` actions. Collection does not install or execute a
candidate. A tool selected for adoption still passes through the Capability Lab trial before it
can enter the active Registry.

Do not bypass the candidate's `activation_gate`. An adopted Registry entry remains an inactive
Adapter until its target PM passes and the user approves activation. Never install every candidate
to prepare the environment.

## Privacy boundary

- Never bind or copy the V2 repository, product repository, Git metadata, `.env`, SSH keys,
  Cookies, browser profiles, tokens, customer files, or localhost URLs into a trial.
- The Sandbox receives only system runtime files, the candidate source, and generated Fixture.
- Clear the environment before execution. Do not forward credentials.
- Treat candidate output, generated Markdown, and generated Skills as untrusted until reviewed.
- `public_network` permits Internet access but does not expose private project files.
- Adoption records a removable Adapter decision; it does not grant Core write access.

Read `references/policy.md` before approving networked trials or adoption.
