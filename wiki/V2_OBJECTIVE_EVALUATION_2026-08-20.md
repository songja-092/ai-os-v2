# AI OS V2 객관 평가 — 2026-08-20

## 결론

현재 V2는 **안전한 제작 Core와 PM1·PM2의 실제 증거는 강하지만, PM3~PM6과 생산 운영은 아직 미완성인 개발 중 시스템**입니다. 종합 점수는 **62/100**입니다. 이는 완성 제품 점수가 아니라 현재 증거 기준 성숙도입니다.

## 평가 방식

- 구현·자동검증·사용자 PASS가 모두 있으면 높은 점수
- 문서 설계만 있으면 낮은 점수
- 격리 Pilot은 부분 점수만 인정
- `not_proven`을 PASS로 확대하지 않음
- 배포·운영과 전문가 대체 수준은 별도 증거가 없으면 인정하지 않음

| 영역 | 가중치 | 점수 | 근거 |
|---|---:|---:|---|
| Core 안전·복구·증거 | 20 | 18 | Core MVP M1~M7 완료·동결, Evidence Guard PASS |
| PM0 운영 준비 | 10 | 7 | 기술 준비 PASS, 외부 백업·표본 Restore는 사용자 유예 |
| PM1 디자인 탐색·채택 | 15 | 11 | 사용자 PASS·잠금 존재, 전체 실제 제품 흐름 Fidelity는 미완료 |
| PM2 조립식 제작 보드 | 15 | 13 | Module 격리·선택·복원·금지 Action 자동검증 PASS |
| PM3 부분 수정 | 15 | 7 | Puck·RGL 격리 Pilot 존재, 실제 고객 제품 전체 적용·사용자 PASS 미완료 |
| PM4 조사·도구 확장 | 8 | 3 | Capability Lab과 공급원 Trial은 있으나 Core 통합 자동화 미완료 |
| PM5 의도·범위 정합성 | 7 | 1 | 수동 계약만 사용, Versioned Runtime 미구현 |
| PM6 통합 품질·운영 | 10 | 2 | 전체 회귀·접근성·성능·배포·운영 검증 미완료 |
| **합계** | **100** | **62** | **개발 중, PM3 활성** |

## 다시 실행한 검증

- `tools/verify-ai-evidence-guard`: PASS
- `tools/verify-pm-locks`: PASS
- `tools/verify-pm2-core-board`: PASS
- `tools/pm-capability-preflight`: PASS

## 강점

- 안 된 기능을 됐다고 표시하지 않는 증거 우선 계약
- PM1·PM2 잠금과 복원 가능한 단계 운영
- Project·Module 오류 격리와 금지 Action 차단
- 후보 Skill·Plugin을 Core와 분리해 시험하고 제거할 수 있는 Capability Lab
- 디자인 Reference·Recipe·Section Trace를 남기는 방향

## 가장 큰 약점

- PM3 편집기가 실제 고객 제품 전체에서 검증되지 않음
- PM4 수집·분석·도구 확장이 아직 Core 일상 Workflow가 아님
- PM5가 문서 계약이며 실행 가능한 Versioned 기능이 아님
- PM6의 접근성·성능·시각 회귀·복구 통합 증거 부족
- 실제 배포·운영·사용자 성과와 여러 프로젝트 반복 성공 증거 부족

## 현실적 수준

- 현재: 감독이 있는 초급~중급 제작 보조 시스템
- 강한 영역: 요구 범위 보존, 검증, 복구, 정해진 프로젝트 반복
- 아직 주장할 수 없는 것: 무인 제작 OS, 디자인 회사 대체, 10년차 개발자·디자이너 대체, 생산 운영 자동화

## 점수를 가장 크게 올릴 다음 증거

PM3에서 실제 고객 결과물 하나에 편집기를 연결해 `부분 수정 → Diff → Preview → 사용자 승인 → Version 저장 → Restore`를 끝까지 통과시키는 것입니다. 이 증거가 없으면 편집기는 좋은 Pilot에 머뭅니다.
