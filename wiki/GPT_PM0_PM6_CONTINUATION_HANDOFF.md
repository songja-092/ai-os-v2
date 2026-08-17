# AI OS V2 PM0~PM6 다음 세션 인수인계

먼저 [[POST_MVP_PM0_PM6_BASELINE]]과 실제 저장소 상태를 읽습니다. 과거 대화나 이전 PM 번호보다 현재 파일과 Git 상태를 우선합니다.

## 고정 상태

```yaml
core_mvp_m1_m7: completed_and_frozen
post_mvp_design: completed
official_sequence: PM0_to_PM6
active_gate: PM0
actual_post_mvp_implementation: not_started_under_new_baseline
```

공식 순서:

```text
PM0 운영환경 준비
→ PM1 디자인 탐색·채택
→ PM2 조립식 V2 보드
→ PM3 부분 수정
→ PM4 자료 조사
→ PM5 사용자 의도 정합성
→ PM6 전체 통합·최종 검증
```

## 절대 보존

- 완료된 Core MVP M1~M7 코드·Run·검증·Commit을 변경하지 않습니다.
- 기존 Dirty 변경을 Reset·Restore·Stash·자동 Commit하지 않습니다.
- 기존 `run_id`, Artifact 경로·SHA-256과 당시 PASS·FAIL·rejected 판정을 유지합니다.
- 과거 증거를 새 PM 기능의 완료 증거로 확대 해석하지 않습니다.
- PM 하나가 실제 PASS할 때마다 해당 범위만 별도 Commit합니다.

## Gate

- PM0 PASS 전 실제 Post-MVP 구현 금지
- PM1 디자인 품질 PASS 전 PM2 구현 금지
- PM2 조립 기능 PASS 전 PM3와 영상·3D Adapter 추가 금지
- 사용자 승인 전 Visual Target 구현 금지
- PM6 PASS 전 Post-MVP 구현 완료 선언 금지

## 다음 작업 하나

PM0 전용 Worktree와 Preflight의 현재 상태를 실제 파일 기준으로 재조회하고, 남은 Blocker만 보고합니다. 설치·제품 수정·Run 생성·Commit·Push는 사용자 승인 없이 수행하지 않습니다.

PM0 PASS 이후 PM1에서는 공식 Registry, 라이선스가 확인된 OSS와 검증된 디자인 시스템을 우선 조사합니다. 자동 수집 시스템을 먼저 만들지 않고 외부 Block 조합 A·B·현재안·필요 시 AI 보완안을 동일 V2 데이터와 Viewport로 비교합니다.

PM2에서는 승인된 Visual Target 하나로 Slot Renderer, Module Manifest, Module 2개, 이동·비활성화·복원·장애 격리와 실제 `ui-state → ui-action`을 검증합니다. 현재 저장소에는 이 조립 기능이 구현·검증됐다고 가정하지 않습니다.
