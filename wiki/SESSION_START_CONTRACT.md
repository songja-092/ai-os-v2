# AI OS V2 새 세션 시작 계약

이 문서는 Codex·Antigravity·기타 AI가 새 세션에서 **가장 먼저 읽는 공식 진입점**입니다.

## 가장 중요한 규칙

> 직접 확인하지 않은 기능·상태·PASS·동기화·복구를 된다고 말하지 않습니다.

- 이 계약은 AI의 환각을 0으로 만들거나 완전히 차단한다고 보장하지 않습니다.
- 채팅 기억, 이전 세션 요약, 사용자의 과거 설명은 현재 상태의 증거가 아닙니다.
- 현재 Commit의 파일·코드·실행 결과·검증 증거만 공식 사실로 사용합니다.
- 증거가 없거나 접근할 수 없으면 `확인 필요` 또는 `not_proven`으로 기록합니다.
- 설계됨, 승인됨, 구현됨, 검증됨, 사용자 PASS를 서로 바꾸어 말하지 않습니다.

## 세 저장 위치를 구분합니다

새 세션은 다음을 하나로 간주하지 않고 각각 확인합니다.

1. 현재 작업 중인 로컬 Worktree와 Branch
2. GitHub `origin/main`
3. Obsidian에서 여는 저장소 또는 Vault

각 위치의 HEAD SHA가 같다는 증거가 있을 때만 `동기화됨`이라고 표현합니다. 다르면 어느 위치가 앞서거나 뒤처졌는지 보고하고, 자동 Merge·Reset·Restore·Stash를 하지 않습니다.

Obsidian은 문서를 보여주는 도구일 뿐 별도의 최신 상태 보증 장치가 아닙니다. Obsidian Vault의 Git HEAD와 현재 작업 Worktree의 HEAD가 다르면 두 문서 집합을 섞어 현재 사실을 만들지 않습니다.

## 새 세션 필수 순서

사용자의 첫 작업을 수행하기 전에 다음을 완료합니다.

1. 현재 저장소 경로, Branch, HEAD, Dirty 상태를 확인합니다.
2. 원격 조회가 허용되고 가능하면 `origin/main`을 갱신해 SHA를 확인합니다. 조회하지 못하면 `not_checked`로 표시합니다.
3. Obsidian Vault 경로와 그 저장소 HEAD를 확인합니다. 접근하지 못하면 `not_checked`로 표시합니다.
4. 이 문서를 읽은 다음 아래 문서를 실제 파일에서 읽습니다.
   - `AGENTS.md`
   - `wiki/GOAL.md`
   - `wiki/CURRENT_STATE.md`
   - `wiki/DECISIONS.md`
   - `wiki/ARCHITECTURE.md`
   - `wiki/VERIFICATION.md`
   - `wiki/DESIGN_SYSTEM.md`
   - `wiki/POST_MVP_PM0_PM6_BASELINE.md`
   - `wiki/PM1_PM4_DESIGN_MEETING_2026-08-19.md`
   - `wiki/AI_EVIDENCE_GUARD.md`
   - 현재 활성 PM의 최신 완료·진행 보고서
5. 완료된 PM의 잠금 Commit·Tag·Hash와 현재 활성 PM을 확인합니다.
6. 아래 형식의 시작 보고를 먼저 제공합니다.

```yaml
session_preflight:
  repo_path:
  branch:
  local_head:
  dirty_preserved:
  origin_main:
  github_alignment: same | different | not_checked
  obsidian_vault:
  obsidian_head:
  obsidian_alignment: same | different | not_checked
  current_pm:
  locked_pms: []
  implemented: []
  verified: []
  not_proven: []
  next_single_action:
```

문서를 일부만 읽었거나 경로에 접근할 수 없으면 `AI OS V2 Memory Loaded`라고 말하지 않습니다. 대신 무엇을 읽지 못했는지 보고합니다.

## 변하지 않는 사용자 계약

- 사용자는 초보자입니다. 먼저 쉬운 한국어로 설명합니다.
- 영어 기술 용어는 필요할 때 `English (한글 발음) — 쉬운 뜻`으로 설명합니다.
- 사용자의 결정이 필요한 경우 `회의할 항목이 있습니다`라고 알리고 한 번에 한 주제씩 다룹니다.
- 회의가 끝나면 `회의가 끝났습니다`라고 명확히 말하고 결과를 기록합니다.
- PM 범위를 벗어난 요청이면 현재 작업을 섞지 않고 어느 PM 범위인지 먼저 알립니다.
- 사용자가 PM을 PASS하면 해당 PM의 승인 화면·동작·유지 범위·복구 기준을 고정하고 잠근 뒤 다음 PM으로 이동합니다.
- PM이 완료되거나 Repo-local Skill을 새로 만들거나 변경하면 같은 작업에서 이 세션 공통계약의 `정확한 상태`와 Skill 목록을 갱신합니다. 공통계약 반영 전에는 PM 저장이 끝났다고 보고하지 않습니다.
- Dirty 변경은 사용자의 변경으로 보존하며 임의로 Reset·Restore·Stash·Commit하지 않습니다.
- 설치·외부 전송·제품 적용·Commit·Push는 승인 범위 안에서만 수행합니다.

## 변하지 않는 V2 용어 계약

- `V2`: Skill을 사용해 결과물을 만들고 Module을 장착·관리하는 OS형 제작 보드판입니다. V2 자체는 Module이 아닙니다.
- `프로젝트`: 제작 작업공간입니다. 프로젝트 자체는 Module이 아닙니다.
- `Section`: 요구사항 대화, 현재 단계, Preview처럼 화면을 구성하는 영역입니다.
- `Skill`: V2가 작업에 사용하는 방법이나 도구입니다. 사용자 화면에서는 `스킬`이라고 부릅니다.
- `Module`: V2가 제작했거나 가져와 검증했고 장착·제거·재사용할 수 있는 실제 결과물입니다.
- `디자인 시스템`: 디자인 탐색·채택·구현·수정·검증의 단일 공식 원본인 `wiki/DESIGN_SYSTEM.md`입니다.
- 카톡형 요구사항 대화창과 Preview는 Section이며 Module이 아닙니다.
- 외부 GitHub 프로젝트나 Skill은 가져왔다는 이유만으로 Module이 되지 않습니다. 계약 변환·격리·동작 검증을 통과해야 Module 후보 또는 Module이 됩니다.

## 모든 AI가 확인할 Repo-local Skill

- `V2 Beginner Technical Translator`: 초보자 표현과 개발 설명을 서로 번역하는 Codex 대화용 Skill
- `V2 Design Finish`: Visual Target 제작부터 디자인 마감 검사까지 지원하는 Skill
- `V2 Capability Lab`: 외부 Skill·Plugin·오픈소스를 비공개 프로젝트와 분리해 격리 시험하는 Skill
- `프로젝트 패키징` (`v2-project-packaging`): 이미 제작된 프로젝트 결과를 읽고 Module Manifest·기능 목록·격리 Preview 초안을 만드는 Skill. 자동 기능 완료 판정·자동 Core 등록·자동 채택은 하지 않습니다.
- `V2 Layout Editor Integration` (`v2-layout-editor-integration`): Puck·React Grid Layout을 제거 가능한 PM3 Adapter로 연결하고, PC·모바일 배치 분리, 이미지 Slot, 단색·투톤 Palette, 자동 정리, Undo·Restore와 Recipe 안전 검사를 수행하는 Codex Skill. 현재 격리 Pilot 검증 단계이며 Core Registry에는 승격되지 않았습니다.
- `V2 Design Director` (`v2-design-director`): 후보별 Reference 탐색·시각 결과·사용자 채택/보류/폐기를 기록하고, 채택 공급원을 역할별 Section에 연결한 Draft Design Recipe와 HTML 추적 상태를 자동 검사합니다. 사용자 결정을 대신하거나 Core·제품에 자동 적용하지 않습니다.

Skill의 최신 상세 기능과 상태는 `wiki/V2_SKILL_INVENTORY_AND_TRANSLATOR_RESEARCH_2026-08-19.md`에서 확인합니다. 문서에 이름만 있다고 Runtime에 자동 연결됐다고 판단하지 않습니다.

## 이 문서 작성 시점의 정확한 상태

- Core MVP M1~M7: 완료·동결로 기록되어 있으나 새 세션은 현재 Commit의 증거를 다시 연결해야 합니다.
- PM0: 사용자 유예 조건이 포함된 PASS로 기록되어 있습니다.
- PM1: 사용자 PASS 후 잠금 기준이 존재합니다.
- PM2: 사용자·기술 PASS 후 `pm2-complete-2026-08-19` Tag로 잠겼습니다.
- `pdf-result-preview`와 `hospital-web-result-preview`: 검증된 프로젝트 결과 Module입니다.
- 목록에서 선택한 Module 하나만 Preview하며 프로젝트별 기능 목록을 분리합니다.
- Core `ui-state → UI → ui-action → Core`, 선택 상태 저장, 비활성, 오류 격리, 복원과 금지 Action 차단을 검증했습니다.
- 현재 활성 단계: PM3 — 부분 수정·Motion Adapter
- 디자인 공급원 비교는 `pm3-artifacts/design-director-trials/trial-index.json`의 순서와 고정 Brief를 사용합니다. 최초 Figma 실행은 연결 예비 시험이며 본 비교 결과로 계산하지 않습니다.
- 디자인 공급원 10개 시각 시험은 종료됐습니다. 5번 Design MCP와 7번 UI UX Pro MCP가 명시적 선호 1·2위이며, 2·3·4·5·7·9·10번 방향을 채택하고 6·8번은 보류했습니다. 여러 채택 공급원을 역할별로 함께 사용할 수 있습니다.
- `reference-adoption-pilot-v1`에서 채택 공급원 5개가 Draft Recipe와 실제 HTML 5개 Section에 연결되는 것을 자동 검증했습니다. Core 자동 선택·제품 적용·PM3 수정 뒤 방향 보존·다른 프로젝트 재사용은 아직 `not_proven`입니다.
- 디자인 규칙과 역할의 공식 원본은 `wiki/DESIGN_SYSTEM.md`입니다. V2 운영 화면과 고객 결과물은 공통 품질 규칙만 공유하며, Codex는 디자인 총괄·지시·독립 검증, Antigravity는 승인된 실제 구현, 사용자는 최종 판정을 담당합니다.
- PM3 격리 Pilot에는 카드 3개의 Puck·React Grid Layout 편집, 글씨와 Grid 크기 독립성, 넘침 경고, 이미지 Slot, 구역별 색상, 대표색 자동 Palette와 자동 배치·줄바꿈 Draft가 구현됐습니다. Build와 핵심 상호작용은 검증했지만 실제 병원 웹 Section 적용, 접근성·Bundle 분리, 사용자 최종 PASS는 아직 `not_proven`입니다.
- 새 세션은 위 문장을 그대로 믿지 말고 `CURRENT_STATE.md`와 해당 증거 파일을 현재 SHA에서 다시 확인합니다.

## 공식 사실을 바꾸는 순서

`작업 → 실제 검증 → 사용자 승인 → Wiki·세션 공통계약 반영 → Commit → Push`

Push하지 않은 로컬 Commit은 GitHub `main`의 공식 상태가 아닙니다. Commit하지 않은 Obsidian 문서는 다른 세션의 공식 기억이 아닙니다.
