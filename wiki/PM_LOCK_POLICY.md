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
