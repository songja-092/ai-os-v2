# Capability Lab policy

## Data classes

| Class | Examples | External use |
|---|---|---|
| public | Public URL, public GitHub repository | Allowed in a declared public-network trial |
| generated_fixture | Fake HTML, fake data, test image | Allowed |
| private_project | Local source, Git history, unpublished design | Never provided to candidates |
| secret | Token, Cookie, `.env`, SSH key, password | Never provided or logged |

## Lifecycle

`discovered → prepared → static_reviewed → isolated_tested → user_selected → adopted`

Rejected candidates become `discarded`, not silently deleted. An adopted capability must retain
source URL, Commit, license, test command, evidence, permissions, network mode, removal steps, and
fallback. Removing it must not remove V2 Recipes or prior evidence.

## Automatic actions

Allowed without a second approval:

- clone a public GitHub repository into the Lab
- calculate hashes and inspect files
- generate a fake Fixture
- execute an already reviewed command with no network in Bubblewrap

Require explicit user approval:

- public-network execution
- package installation or install scripts
- adoption into the active V2 Registry
- discard or removal

Always prohibited:

- global package or Skill installation
- candidate access to private project folders or secrets
- login, Cookie reuse, paywall bypass, localhost forwarding, or automatic Core writes
