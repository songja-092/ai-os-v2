# AI OS V2 Codex 공통 실행계약

상태: `candidate_implementation`

적용 범위: 모든 PM, 유지보수, 버그 수정, Capability Pilot

## 1. 우선순위

1. 플랫폼 안전·권한 규칙과 사용자의 현재 명시적 요청
2. 잠긴 Core MVP M1~M7, 완료 PM, 사용자 기존 변경
3. 이 Codex 공통 실행계약
4. 개별 PM 작업 지시
5. 임시 Prompt

현재 요청이 보호 대상을 정확히 지정해 변경을 승인하지 않는 한 잠긴 결과를 수정하지 않습니다.

## 2. 기본 실행 흐름

사용자 원문과 완료 조건 보존
→ 저장소·Dirty·PM 잠금 확인
→ 변경 파일에 맞는 기존 검사 선택
→ 승인 범위 안에서 최소 구현
→ Build·Test·Browser·Console·회귀검사
→ 실패와 원인 기록
→ 일반 코드 오류 최소 수정
→ 실패했던 동일 검사 재실행
→ 임시 상태 원상복구 확인
→ 기술 결과와 사용자 판단 항목을 분리해 보고

작고 명확한 수정은 바로 구현·검증합니다. 현상 유지·사용자안·최소 대안·반례 비교는 구조·도구·Workflow·범위가 달라지는 결정에서만 수행합니다.

## 3. 자율 완료 경계

Codex는 승인 범위 안에서 해결 가능한 일반 코드 오류를 최대 3회 수정합니다. 검사 재실행은 수정 횟수에 포함하지 않습니다. 다음 조건은 첫 발견부터 중단합니다.

- 데이터 손실 또는 파괴적 변경 위험
- 로그인·권한·결제·비용 필요
- 사용자 Dirty와 작업 대상 충돌
- PM 잠금 또는 Core 보호 범위 충돌
- 승인 범위 확대 필요
- Harness 자체 오류로 제품 정상 여부를 판단할 수 없음

완료는 자동 검사 가능한 조건이 모두 PASS이고 사용자 변경·잠금·복구 상태가 보존됐을 때만 기술 PASS입니다. 디자인·사업 방향·최종 적용 같은 사람의 판단은 `pending`으로 남깁니다.

## 4. Harness 경계

`tools/verify-work-item`은 새 Workflow 엔진이 아니라 기존 검증기를 호출하는 얇은 Dispatcher입니다. Route는 `verification-routing.json`, 증거 형식은 `schemas/work-evidence.schema.json`을 사용합니다.

- Route 없는 작업은 검증 방법이 없으므로 BLOCKED입니다.
- 잠긴 파일 Route를 다른 Route보다 먼저 검사합니다.
- `contract_only` PASS는 계약만, `fixture_specific` PASS는 해당 Fixture만, `runtime` PASS는 실행한 Runtime 경로만 증명합니다.
- 단일 Fixture PASS를 범용 기능 PASS로 승격하지 않습니다.
- 임시 상태 변경 검증기는 선언된 파일의 실행 전후 Hash가 같아야 합니다.
- Harness는 PM 변경·Restore·Commit·Push를 자동 실행하지 않습니다.

## 5. 반복 자동화 승격

결정형 검사는 수동 성공 1회와 정상·실패 Fixture가 있으면 자동화할 수 있습니다. 판단형 Workflow는 서로 다른 실제 프로젝트에서 반복되고 자동 판정·승인·제거 경계가 확인된 뒤 제한 Pilot로 만듭니다.

제한 자동화 PASS에는 서로 다른 실제 입력 2건 이상, 의도된 실패 1건, Restore 1건, 시간 또는 사용자 개입 감소, 승인 지점과 제거 방법이 필요합니다. 같은 Fixture를 세 번 실행한 것은 범용화 증거가 아닙니다.

## 6. 증거 언어

- `PASS`: 해당 검사와 해당 범위의 증거가 있음
- `BLOCKED`: 완료 조건 또는 안전 조건을 충족하지 못함
- `NOT_PROVEN`: 검사하지 않았거나 Runtime 증거가 없음
- `NOT_APPLICABLE`: 해당 없음과 이유가 기록됨

실패 기록은 최종 PASS로 덮어쓰지 않습니다. Commit되지 않은 작업은 복구 가능한 Version이라고 표현하지 않습니다.
