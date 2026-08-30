# omd-hospital-ab-v1 비교 시험 보고서

## 목적

같은 병원 웹 요구사항, 같은 문구, 같은 의료진 이미지, 같은 예약 동작을 고정하고
디자인 적용 방법만 바꿔 실제 결과를 비교한다.

- A: 현재 V2 계약을 Codex가 수동 실행한 구현
- B: 격리 설치된 `oh-my-design-cli 2.0.0`의 추천·규칙을 보조로 사용한 구현

이 시험은 V2 Core Runtime의 자동 생성 증거가 아니다. 두 결과 모두 격리된 정적 Pilot이며
사용자의 채택 전에는 기본 Skill·Recipe·제품으로 승격하지 않는다.

## 고정 조건

| 항목 | 고정값 |
|---|---|
| Visual Target SHA-256 | `6f3600f7a256280c558b97c10b6e55eed94090b408fddaef3732709fdb3f202a` |
| 의료진 이미지 SHA-256 | `e669d1a55228293721f3130a18dd4ba7c4a303b19d9b3ca3e7909ad5f7731d65` |
| 핵심 콘텐츠 | 진료, 의료진, 위치, 진료시간, 예약 요청 |
| 핵심 동작 | 예약창 열기 → 필수값 입력 → 접수 결과 표시 |
| 검증 Viewport | Desktop 1440×900, Mobile 390×844 |
| 배포 | 제외 |

## B안의 oh-my-design 적용 범위

- 설치 위치: 이 Trial의 `oh-my-design/.agents`, `oh-my-design/.codex` 내부
- 전역 설치: 없음
- 고정 Package: `oh-my-design-cli@2.0.0`
- 고정 원본 Commit: `9c181086dae537395f5a34a768c03a49d875acce`
- Reference Query 결과 1순위: `lovable`
- Reference 품질: `verified_v2`
- 적용 요소: 밝은 canvas, 검은 ink, 얇은 hairline, 강한 Typography 위계,
  8px compact action, 절제된 surface와 카드 수

`lovable`은 이번 격리 시험에서만 자동 1순위로 고정했다. 사용자가 직접 채택한 Reference가
아니며 V2 기본 디자인으로 승격하지 않는다.

## 실제 검증 결과

| 검사 | A | B |
|---|---|---|
| HTTP 응답 | PASS · 200 | PASS · 200 |
| 의미 있는 첫 화면 | PASS | PASS |
| 예약 Dialog 열림 | PASS | PASS |
| 이름·연락처·진료 선택 | PASS | PASS |
| 접수 상태 표시 | PASS | PASS |
| 390px 가로 넘침 | PASS · `scrollWidth=clientWidth=375` | PASS · `scrollWidth=clientWidth=375` |
| 동일 Visual Target | PASS · 동일 Hash | PASS · 동일 Hash |
| 동일 의료진 이미지 | PASS · 동일 Hash | PASS · 동일 Hash |

In-app Browser에서 Electron 공통 CSP 경고와 Browser Client의 `MutationObserver` 오류가
관찰됐다. 두 페이지 자체의 예약·반응형 동작에는 재현되지 않았지만, 앱 코드 오류와
분리된 독립 Browser Session 증거가 없으므로 Console 전체 PASS는 보류한다.

## 시각 비교

### A — 현재 V2 방식

- 선택된 네이비·골드 Visual Target의 분위기와 구성에 더 가깝다.
- 인물 사진 위에 Copy를 겹치고 상태 Card를 두어 병원 웹의 익숙한 신뢰감을 준다.
- 약점: 기존 프리미엄 병원 Template과 비슷해질 가능성이 높고, 카드와 Section 문법이
  비교적 전통적이다.

### B — oh-my-design 보조 방식

- 인물 사진과 큰 문장 위계가 분리돼 첫 화면의 메시지가 더 빠르게 읽힌다.
- Card를 줄이고 행과 hairline을 사용해 A와 명확히 다른 편집 디자인을 만든다.
- 약점: `lovable`은 Healthcare 전용 Reference가 아니라서 의료 신뢰 장치와 한국 병원
  관습은 별도 보완이 필요하다.
- 엄격한 `omd:final-qa`의 Brand Token 단일성·외부 Link 200 검사를 모두 닫은 공식
  OMD Project Package는 아니다. 현재 상태는 `OMD-assisted isolated pilot`이다.

## 판정

```yaml
trial_execution: completed
same_input_contract: verified
same_asset_hash: verified
current_core_variant: implemented_and_browser_verified
oh_my_design_variant: implemented_and_browser_verified
oh_my_design_full_canonical_flow: not_proven
console_gate: blocked_by_shared_browser_runtime_noise
user_visual_preference: pending
default_adoption: prohibited_until_user_decision
```

## 2026-08-24 사용자 후속 결정

이번 A/B는 `예비 비교 시험`으로만 보존한다. 이 결과만으로 oh-my-design을 채택하거나
V2 기본 디자인 흐름을 변경하지 않는다.

다음 비교 순서는 아래와 같이 고정한다.

```text
확정된 V2 디자인 탐색·채택 흐름 Runtime 연결
→ 같은 병원 Brief로 V2 공식 결과 제작
→ 동일 Brief·콘텐츠·기능·Viewport를 고정
→ oh-my-design 결과 제작
→ 디자인·기능·재작업·시간·사용자 선호 비교
→ 사용자 채택·보류·폐기
```

```yaml
trial_role: preliminary_evidence_only
oh_my_design_adoption: deferred
required_baseline: completed_v2_design_adoption_runtime
next_ab_test: after_confirmed_flow_implementation
user_decision_recorded: true
```

현재 채택 판정은 하지 않는다. 확정된 V2 흐름으로 만든 Baseline이 생긴 뒤
`V2 기본안 / oh-my-design안 / 혼합 / 폐기`를 다시 판정한다.
