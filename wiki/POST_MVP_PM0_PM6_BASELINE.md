# AI OS V2 Post-MVP PM0~PM6 공식 기준

작성일: 2026-08-17
상태: 사용자 승인 완료·설계 완료
적용 범위: Post-MVP 계획만
보존 범위: Core MVP M1~M7, 기존 Run·Artifact·Commit

## 1. 공식 순서

```text
PM0 운영환경 준비
→ PM1 디자인 탐색·채택
→ PM2 조립식 V2 보드
→ PM3 부분 수정
→ PM4 자료 조사
→ PM5 사용자 의도 정합성
→ PM6 전체 통합·최종 검증
```

이 문서는 과거 Post-MVP PM0~PM7 번호 체계를 대체합니다. 기능을 삭제한 것이 아니라 이동·통합해 중복을 제거했습니다. Core MVP M1~M7의 완료 판정과 증거에는 영향을 주지 않습니다.

## 2. PM별 책임과 PASS

### PM0 — 운영환경 준비

목적: 기존 프로젝트를 손상하지 않고 실제 구현을 반복 실행·복구할 수 있는 환경을 만듭니다.

구현 범위:

- 격리 Worktree와 고정 Runtime·실행 명령
- 고정 Port와 `strictPort` 충돌 차단
- Antigravity 안전 실행
- Preview 장애 격리
- 외부 Backup·Rollback·Restore
- 새 Codex 세션 재현

PASS:

- 새 세션에서 같은 환경을 재현합니다.
- 병원 웹과 PDF Preview를 독립 실행합니다.
- Preview 실패가 Core와 다른 프로젝트에 전파되지 않습니다.
- Backup 표본의 Restore를 확인합니다.

### PM1 — 디자인 탐색·채택

목적: AI 생성안만 반복하지 않고 사용자가 더 다양하고 좋은 디자인을 눈으로 선택하게 합니다.

후보 구성:

- 검증된 외부 Block 조합 A
- 구조가 다른 외부 Block 조합 B
- 현재 디자인 유지안
- 필요한 경우에만 AI 보완안

구현 범위:

- 공식 Registry, 라이선스가 확인된 OSS와 검증된 디자인 시스템 우선 조사
- 출처·라이선스·의존성·기술 호환성 확인
- 같은 실제 V2 데이터와 Viewport로 후보 3개와 현재안 비교
- 전체 구조·특정 Section·Design DNA의 자연어 선택
- V2 기본 Typography·Color·Button 규칙으로 시각 통일
- 선택 출처·Section ID·Design Recipe 기록
- 승인된 Visual Target 등록과 승인 전 구현 차단

PASS — 디자인 품질:

- 출처와 라이선스를 확인한 구조적으로 다른 후보가 존재합니다.
- 모든 후보를 같은 데이터와 Viewport로 비교합니다.
- 사용자가 현재안보다 나은 방향 또는 현재안 유지를 명시적으로 선택합니다.
- 선택 결과가 Visual Target·Section ID·Design Recipe에 연결됩니다.
- 사용자 승인 전 PM2 구현을 시작하지 않습니다.

제외: 대규모 자동 수집기, 새 DB, 자동 Template 혼합, 출처 없는 복제.

### PM2 — 조립식 V2 보드

목적: PM1에서 승인한 디자인을 실제로 조립·격리·복원 가능한 보드로 작동시킵니다.

구현 범위:

- PC 전용 V2 UI Shell과 Project Registry
- Slot Renderer
- 검증 가능한 Module Manifest와 정적 Module Registry
- `project_home`, `workspace_preview`, `workspace_tools`, `background_capability` Slot
- 기존 기능 Module 2개 장착
- Module 순서 이동과 활성화·비활성화
- Module 오류·Preview 장애 격리
- 순서·활성 상태 복원
- 실제 `V2 Core → ui-state → UI → ui-action → V2 Core`
- 로컬 프로젝트 등록·전환·이름 변경·보관·복원

PASS — 조립 기능:

- 유효한 Manifest의 Module만 장착됩니다.
- Module 2개를 이동하고 하나를 비활성화할 수 있습니다.
- 한 Module 실패가 Core·다른 Module·다른 프로젝트에 전파되지 않습니다.
- 이전 순서와 활성 상태를 복원합니다.
- Core가 허용하지 않은 Action은 표시하거나 실행하지 않습니다.
- 프로젝트별 Run·Preview·결과가 섞이지 않습니다.

예쁜 화면만으로 조립 기능을 PASS하지 않고, Module 동작만으로 PM1 디자인 품질을 PASS하지 않습니다.

### PM3 — 부분 수정

목적: 승인된 보드와 고객 결과물을 제한된 범위에서 안전하게 수정합니다.

구현 범위:

- Section 선택과 자연어 수정
- 여백·크기·순서·표현 변경
- 변경 전후 Preview
- 새 Design Version
- 적용·폐기·이전 Version 복구
- 고객 결과물 390px·430px 모바일 회귀검증

PASS:

- 선택한 Section 이외의 변경이 없습니다.
- 변경 전후를 확인하고 취소·적용할 수 있습니다.
- 새 Version과 Restore 지점이 존재합니다.
- 모바일 핵심 흐름이 깨지지 않습니다.

기존 M6 Quick Change 증거는 자연어 국소 수정의 선행 증거로 보존하지만 직접 보드 편집 완료 증거로 확대하지 않습니다.

### PM4 — 자료 조사

목적: 프로젝트 제작과 병목 해결에 필요한 출처가 확인된 자료를 확보합니다.

구현 범위:

- 공식 웹·문서와 GitHub 조사
- Reddit 조사
- 사용자가 제공한 Threads 자료
- PDF·Markdown·Text·Screenshot
- 프로젝트 병목 조사
- Source·수집 시점·공식 자료와 보조 의견 구분

PASS:

- 주장과 출처가 연결됩니다.
- 공식 자료와 보조 의견이 구분됩니다.
- 조사 실패가 Core와 기존 제작 기능을 막지 않습니다.
- 승인 전 제품을 변경하지 않습니다.

제외: 로그인·유료 제한 우회, 무단 대량 Scraping, 상시 수집 Agent, 별도 Queue·Worker·DB.

### PM5 — 사용자 의도 정합성

목적: AI가 요청을 잘못 이해한 상태로 구현을 시작하지 못하게 합니다.

구현 범위:

- 사용자 원문과 Intent Packet
- AI Intent Receipt
- 변경·비변경 범위
- Acceptance Checks
- 구현 전 불일치 차단과 구현 후 원문 비교

PASS:

- 구현 전 사용자 요청과 AI 이해가 일치합니다.
- 범위 충돌이나 누락이 있으면 구현을 차단합니다.
- 구현 결과를 최초 요청과 다시 비교합니다.

### PM6 — 전체 통합·최종 검증

목적: PM0~PM5가 하나의 안전하고 복구 가능한 제작 흐름으로 작동하는지 확인합니다.

통합 흐름:

```text
프로젝트 등록 → 자료 조사 → 의도 확인 → 디자인 탐색·선택
→ 보드 조립 → 부분 수정 → 최종 Preview → 승인
→ Commit·Rollback·Restore → 결과 전달
```

PASS:

- 초보자가 자연어와 Preview 중심으로 전체 과정을 완료합니다.
- 프로젝트와 Run이 섞이지 않습니다.
- 실패 단계에서 중단·재개할 수 있습니다.
- 승인 결과를 저장하고 이전 상태로 복구합니다.
- 최종 Preview·검증 보고서·실행 방법·제한사항을 함께 전달합니다.

## 3. 고정 Gate

```text
PM0 FAIL → 실제 Post-MVP 구현 금지
PM1 디자인 품질 FAIL → PM2 구현 금지
PM2 조립 기능 FAIL → PM3 및 영상·3D Adapter 추가 금지
PM3 FAIL → 부분 수정 완료 선언 금지
PM4·PM5 FAIL → 해당 프로젝트 구현 진행 금지
PM6 FAIL → Post-MVP 완료 선언 금지
```

영상·3D 같은 새 기능은 PM2 조립식 보드 PASS 이후 별도 Adapter·Preview Module 후보로 검토합니다.

## 4. 기존 PM 기능·증거 매핑

| 이전 Post-MVP 기능 | 새 위치 | 판정 | 기존 증거 |
|---|---|---|---|
| PM0 운영환경 | PM0 | 유지 | 원본 ID·경로로 보존 |
| PM1 대시보드·작업실 | PM2 | 조립식 보드로 이동 | Preview는 당시 판정 그대로 보존 |
| PM2 로컬 프로젝트 관리 | PM2 | Project Registry에 통합 | 보존 |
| PM3 디자인 Reference | PM1 | 디자인 탐색으로 이동 | Reference 출처·Artifact 보존 |
| PM3 일반 자료·병목 조사 | PM4 | 유지 | Run·분석 Artifact 보존 |
| PM4 사용자 의도 확인 | PM5 | 이동 | 계약·검증 증거 보존 |
| PM5 디자인 다양성 | PM1 | 디자인 탐색과 통합 | 후보·선택 증거 보존 |
| PM6 최신 디자인 조사 | PM1 | 후보 조사와 통합 | 출처 증거 보존 |
| PM6 부분 수정 | PM3 | 이동 | M6 Quick Change 증거 보존 |
| PM7 전체 통합 | PM6 | 번호 이동 | 원래 Run·Commit·Artifact 보존 |

증거 보존 원칙:

- 기존 `run_id`, Commit SHA, Artifact 경로와 SHA-256을 변경하지 않습니다.
- 당시 PASS·FAIL·rejected 판정을 그대로 유지합니다.
- 새 PM 번호는 별도 매핑으로만 연결합니다.
- 과거 증거가 검증하지 않은 새 기능까지 PASS한 것으로 확대하지 않습니다.
- Core MVP M1~M7 파일과 완료 기록을 수정하지 않습니다.

## 5. 현재 상태

```yaml
core_mvp_m1_m7: completed_and_frozen
post_mvp_design: completed
official_post_mvp_sequence: PM0_to_PM6
active_gate: PM0
pm1_design_exploration: not_started_under_new_baseline
pm2_modular_board: not_started
pm3_to_pm6: not_started
```

다음 구현 작업은 PM0 Gate를 완료하는 것입니다. PM0 PASS 후 PM1 디자인 탐색·채택을 시작합니다.
