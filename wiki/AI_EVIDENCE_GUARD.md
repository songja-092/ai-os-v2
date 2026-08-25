# AI Evidence Guard

AI OS V2를 제작하는 Codex·Antigravity·기타 AI가 기억과 추측을 공식 사실로 표현하는 문제를 줄이기 위한 공통 정책입니다.

## 한계

이 규칙은 AI의 환각을 0으로 보장하지 않습니다. 대신 다음 조합으로 잘못된 주장이 공식 기록에 들어가는 것을 막습니다.

- Commit으로 저장된 문서 우선
- 상태와 증거 분리
- 실제 파일·실행·검증 확인
- 사용자 PASS와 AI 기술 PASS 분리
- 증거가 없으면 `확인 필요` 또는 `not_proven`

## 작업 전 필수 확인

1. `git status`, 현재 HEAD, 현재 Branch를 읽습니다.
2. `AGENTS.md`, `CURRENT_STATE.md`, `DECISIONS.md`, `ARCHITECTURE.md`, `VERIFICATION.md`를 실제 파일에서 읽습니다.
3. 현재 PM과 잠금된 이전 PM을 확인합니다.
4. 기능 존재는 코드·Manifest·Registry에서, 상태는 Core 상태에서, PASS는 검증 증거에서 확인합니다.
5. 직접 읽지 못한 파일·웹·실행 결과를 요약했다고 표현하지 않습니다.

## 주장별 필요 증거

| 주장 | 최소 증거 |
|---|---|
| 기능이 존재함 | 실제 코드·Manifest·Registry 경로 |
| 기능이 작동함 | 실행 명령, 종료 코드, 렌더링·상호작용 증거 |
| PASS함 | PASS 기준, 대상 Commit, 검증 결과 |
| 사용자가 승인함 | 사용자 판정 문구와 범위 |
| 원격과 동기화됨 | `git fetch` 후 확인한 원격·로컬 SHA |
| 복구 가능함 | 별도 위치의 Rollback·Restore 실행 증거 |

## 금지된 확대 해석

- 문서에 설계된 기능을 실제 구현된 기능으로 표현하지 않습니다.
- Fixture·Pilot·정적 Preview를 Core 연결 완료로 표현하지 않습니다.
- 과거 Run의 PASS를 현재 Commit에 자동 적용하지 않습니다.
- 하나의 Module 시험을 PM2 전체 PASS로 표현하지 않습니다.
- AI가 사용자 대신 시각 승인·사용성 PASS를 내리지 않습니다.

## 보고 형식

확정 주장은 가능하면 다음을 함께 제시합니다.

```yaml
claim:
status: proposed | approved | implemented | verified | not_proven
source_files: []
target_commit:
verification:
user_approval:
limitations: []
```
