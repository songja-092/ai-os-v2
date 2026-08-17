# Post-MVP Roadmap

현재 공식 Post-MVP 설계 원본은 [[POST_MVP_FINAL_DESIGN]] · [GitHub 링크](POST_MVP_FINAL_DESIGN.md)입니다.

`AI OS V2 Core MVP M1~M7`은 완료·동결하며 Post-MVP 설계는 완료됐습니다.

```yaml
post_mvp:
  planning_status: completed
  official_structure: PM0_to_PM6
  implementation_gate: PM0
  pm1_design_preview_allowed_before_pm0: true
  pm1_product_implementation_allowed: false
  user_approval_required_for_implementation: true
```

## 공식 순서

> 최신 공식 순서와 PASS 기준은 [[POST_MVP_PM0_PM6_BASELINE]]을 사용합니다. 아래의 이전 PM0~PM7 상세는 역사적 기능 기록으로 보존합니다.

1. `PM0 — 운영환경 준비`
2. `PM1 — 디자인 탐색·채택`
3. `PM2 — 조립식 V2 보드`
4. `PM3 — 부분 수정`
5. `PM4 — 자료 조사`
6. `PM5 — 사용자 의도 정합성`
7. `PM6 — 전체 통합·최종 검증`

## 이전 PM0~PM7 순서

1. `PM0 — 운영환경 준비`
2. `PM1 — 대시보드·프로젝트 작업실`
3. `PM2 — 로컬 프로젝트 관리`
4. `PM3 — 자료·디자인 Reference 수집`
5. `PM4 — 사용자 의도 확인`
6. `PM5 — 디자인 다양성 생성·비교`
7. `PM6 — 최신 디자인·모션·부분 수정`
8. `PM7 — 전체 통합·최종 검증·결과 전달`

목적·기능·제외 범위·PASS·의존성·오류·복구 계약은 이 문서에 중복 기록하지 않고 [[POST_MVP_FINAL_DESIGN]]을 따릅니다.

## 현재 다음 작업

```text
PM0 전용 Worktree
→ 남은 운영 Blocker 확인
→ Preflight 재실행
→ 사용자 확인
→ PM0 PASS와 독립 Result Commit
→ PM1 제품 구현 Gate 개방
```

PM0 PASS 전에도 PM1 Concept Sample과 Visual Target 후보 설계는 가능하지만 실제 제품 UI·Core 연결 구현은 금지합니다.

## PM 완료 저장 규칙

각 PM은 다음 조건 이후 별도 Result Commit 하나로 완료합니다.

- PM PASS 기준 완료
- Codex 검증 PASS
- 사용자 결과 PASS
- 허용 경로만 포함
- Rollback·Restore 증거
- Wiki·CURRENT_STATE 갱신

사용자 Dirty 변경, 실패·진단 Run, Cache·Temp와 다음 PM 작업은 완료 Commit에서 제외합니다.

## PM3 디자인 Reference Workflow

새 PM이나 항상 실행되는 Agent를 만들지 않습니다. PM3 안에서 요청 시 다음 제한형 Workflow를 실행합니다.

```text
Collector
→ Analyzer
→ 사용자 Curator
→ Versioned Reference Collection
→ PM5 Reference Mix
```

자동 채택, 무단 대량 Scraping, Queue·Worker·별도 DB는 현재 범위에서 제외합니다.
