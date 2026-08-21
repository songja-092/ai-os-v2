# PM3 사용자 통과·PM6 재검증 이관 — 2026-08-21

## 사용자 판정

사용자는 2026-08-21 현재 PM3 편집 Pilot을 `일단 통과`로 판정하고, 남은 실제 검증은
PM6 최종 단계에서 수행하기로 결정했습니다.

- PM3 사용자 흐름·방향: 통과
- PM3 인터뷰 계약: 검증됨
- 현재 확인된 편집 기능: 격리 Pilot 수준
- 확정 인터뷰 기능 전체 구현·자동검증: 미완료
- 실제 고객 결과물 전체 적용: 미완료
- PM6 최종 재검증: 필수

## PM6에서 반드시 다시 확인할 항목

1. 실제 고객 결과물에서 편집 기능이 작동하는지
2. PC와 모바일 배치가 독립적으로 유지되는지
3. 모바일 390px·430px에서 깨지지 않는지
4. `이전으로`와 `수정 전체 버리기`가 정확히 작동하는지
5. 원본 제품과 승인 Version이 보존되는지
6. 다른 프로젝트와 상태가 섞이지 않는지
7. 접근성·기능·화면 회귀가 없는지

## 잠금 경계

- PM1·PM2 잠금은 변경하지 않습니다.
- 현재 병원 웹 PM3 Draft는 검증 전 제품 기준으로 승격하거나 원본에 합치지 않습니다.
- 검증되지 않은 기능을 `✅ 검증됨` 또는 기술 PASS로 표시하지 않습니다.
- PM3의 새 범위 변경은 잠금을 다시 여는 사용자 결정 없이는 수행하지 않습니다.
- PM4·PM5 진행은 가능하지만 PM6 완료 선언은 위 항목을 모두 확인한 뒤에만 가능합니다.

```yaml
pm3_user_decision: pass
pm3_close_mode: user_pass_with_deferred_pm6_revalidation
pm3_technical_completion: not_proven
pm3_scope_locked: true
pm4_start_allowed: true
pm6_revalidation_required: true
product_commit: not_performed
product_merge: not_performed
```
