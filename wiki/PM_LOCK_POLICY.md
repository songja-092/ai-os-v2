# PM Lock Policy

완료·사용자 승인된 PM은 다음 PM에서 직접 수정하지 않는다. 새 PM은 잠긴 기준 위에 새 Module·Adapter·Artifact를 추가한다.

## PM1 잠금 기준

- 상태: `completed_and_user_approved`
- Commit: `75074311d2e5329d0b770765a95801c6a64f9ff0`
- Tag: `pm1-complete-2026-08-18`
- 승인 화면: `pm1-complete-review.html`

### 핵심 파일 SHA-256

| 파일 | SHA-256 |
|---|---|
| `pm1-complete-review.html` | `68788ad015b933c6c5ea6507f57219b2c59605bc2cc19c33c12e3e02187ef83a` |
| `wiki/PM1_COMPLETION_REPORT_2026-08-18.md` | `5d21ebdae9d81c0e951519db7488d4726c87afe3a9c83f53ac608f36919b8cd2` |
| `pm1-artifacts/visual-target-v1/section-contract.json` | `8107e07dcbf62fdf77d0581ac8159f5b8646c1d8ca1fa0ef8066e4518cdf2263` |

## 다음 PM 규칙

1. 작업 시작 전 `tools/verify-pm-locks`를 실행한다.
2. 잠긴 PM 파일은 수정하지 않는다.
3. 새 PM은 별도 Worktree와 Branch에서 시작한다.
4. 이전 PM의 화면·메뉴·주요 사용자 흐름을 회귀검사한다.
5. 사용자 통과 후 Commit을 만들고 해당 Commit에 `pmN-complete-YYYY-MM-DD` Tag를 붙인다.
6. 실패한 Pilot은 삭제하지 않고 별도 작업공간에 보존한다.

## PM2 작업 기준

- Worktree: `/home/user/바탕화면/ai_os_v2_pm2`
- Branch: `codex/pm2-from-pm1-lock`
- Base: `pm1-complete-2026-08-18`
- 금지: PM1 승인 화면·완료 보고서·Section 계약 직접 수정
- 필수: PM1 전체 화면을 유지한 상태에서 조립 기능만 추가

## PM2 잠금 기준

- 상태: `completed_and_user_approved`
- Tag: `pm2-complete-2026-08-19`
- 승인 화면: `pm2-module-test.html`
- 복원: 위 Tag 또는 PM2 완료 Commit으로 전체 상태 복원

### 핵심 파일 SHA-256

| 파일 | SHA-256 |
|---|---|
| `pm2-module-test.html` | `1d440bbbdf6c90fe5e24e6463060911801d62b5d96c33e34c1aa2bf634de1fb8` |
| `wiki/PM2_FIRST_MODULE_PILOT_REPORT_2026-08-19.md` | `768d7b13ec42c353f8757d6603f455203189ead69adae55838459da0b6fc0902` |
| `pm2-artifacts/module-registry-v1/core-verification.json` | `da8adcb9e34cee648e466509b63ae0396195697f58b883c7749ff8179a22ebb5` |

PM3부터 위 세 파일을 직접 수정하지 않습니다. PM2의 프로젝트 선택·단일 Preview·기능 목록을 변경해야 한다면 별도 Change Run과 사용자 승인을 사용합니다.

## PM4 잠금 기준

- 상태: `completed_and_user_approved`
- Result Commit: `4d5dd0a8cf2a2a9c88a6d8d14150c91dd9eb6305`
- Tag: `pm4-complete-2026-08-26`
- 승인 화면: `pm4-electronic-card-visual-target.html`
- 완료 경계: 전자명함 요청의 인터뷰·수집·시각 Reference·리필·사용자 선택·Design DNA·전체 흐름 Visual Target·PM5 인계

### 핵심 파일 SHA-256

| 파일 | SHA-256 |
|---|---|
| `wiki/PM4_COMPLETION_REPORT_2026-08-26.md` | `79b038c51c0c428b3961945c0bd8cbf58312f2c52b5b54708decdb7830fead53` |
| `pm4-artifacts/project-collector-mvp-v1/electronic-card-design-handoff.json` | `974d00ea3d7ec41d69430562514c1aee7942d8afe215340686f49d4fe9a00e2e` |
| `pm4-artifacts/project-collector-mvp-v1/design-candidates/direction-2-full-flow-visual-target.png` | `053735a40d6cf9c65396ba871885409e6c0a30cf963591512267524dbcd40748` |
| `state/pm4-design-ideation-state.json` | `f06e1c349f404c84571f5fda444b924ae748fe861dfb7bc36ccc091e919fe39a` |
| `pm4-artifacts/project-collector-mvp-v1/visual-reference-selection-handoff.json` | `aa47d48932896a118c48f98bbbdb64d9ae08774a35d7f5721525f81e0008efff` |

PM5부터 위 다섯 파일을 직접 수정하지 않습니다. PM4 범위를 확장하거나 승인 결과를 변경하려면 별도 Change Run과 사용자 승인을 사용합니다.
