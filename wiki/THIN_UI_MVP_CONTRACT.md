# V2 Thin UI MVP Contract

> 현재 PM0~PM6 구조에서 이 계약은 `PM2 — 조립식 V2 보드`의 Thin UI 기술 경계로 계속 유효합니다. 전체 순서와 PASS 기준의 최신 원본은 [[POST_MVP_PM0_PM6_BASELINE]]입니다.

이 문서는 `AI OS V2 Core MVP` 위에 제작할 Post-MVP `PM2 — 조립식 V2 보드`의 승인된 기술 계약입니다. UI·Registry 코드 또는 새 상태 저장소를 구현했다는 의미가 아닙니다.

## 1. Core 경계와 데이터 흐름

```text
V2 Core → ui-state(JSON) → UI
UI → ui-action → V2 Core
```

- UI는 `run.yml`, Wiki 또는 프로젝트 파일을 직접 읽거나 수정하지 않습니다.
- UI는 표시와 사용자 입력 전달만 담당합니다.
- 상태 판정, 파일 변경, 프로세스 실행과 검증은 V2 Core가 담당합니다.
- UI가 별도 상태 저장소를 만들거나 Core 상태를 추측하는 것을 금지합니다.

## 2. 프로젝트별 Run 선택

표시 우선순위는 프로젝트마다 `active_run → result_run → 표시할 Run 없음`으로 고정합니다.

- 실패 Run은 `diagnostic_runs`에만 표시합니다.
- `latest_run`은 기록 조회용이며 표시할 정상 결과를 선택하는 근거가 아닙니다.
- 실패 Run이 정상 결과 Run을 덮어쓰지 않습니다.
- 프로젝트마다 Run을 독립적으로 선택합니다.

## 3. Project Registry와 Preview 실행 권한

UI는 V2 Core가 관리하고 검증한 허용 목록만 사용합니다.

```yaml
project_id: pdf-stamp
display_name: PDF 도면 기호
path: 허용된 고정 경로
port: 5174
start_command: 허용된 고정 명령
health_url: /
strict_port: true
```

- UI에서 경로, 명령 또는 Port를 자유 입력하거나 임의 실행할 수 없습니다.
- 프로젝트 추가와 변경은 Registry 검증을 통과해야 합니다.
- 프로젝트별 고정 Port와 `strict_port: true`를 사용하며 충돌 시 다른 Port로 자동 변경하지 않습니다.
- 프로젝트마다 Preview 프로세스 하나만 허용하고 프로젝트 전환 시 이전 iframe을 제거합니다.

## 3-1. 최소 조립식 기반

PM2는 고정 V2 Core 위에 `UI Shell`, `Project Registry`, 정적 `Capability/Module Registry`, 고정 UI Slot, Design Recipe와 Project·Feature Adapter 경계를 둡니다.

- Module Registry는 검증된 Manifest만 읽는 정적 허용 목록이며 Marketplace나 외부 코드 Runtime이 아닙니다.
- 최소 Slot은 `project_home`, `workspace_preview`, `workspace_tools`, `background_capability`입니다.
- Module은 Run·Gate·Artifact·권한·Action을 직접 수정할 수 없습니다.
- Module의 `health`, `enabled`, `fallback` 상태는 해당 Module에만 영향을 주며 Core와 다른 프로젝트로 실패를 전파하지 않습니다.
- Design Recipe는 Design Token, 화면·Section ID, 순서, 컴포넌트, Reference, 모바일 동작과 Version을 Core 상태에서 분리합니다.

## 4. Core가 허용한 Action만 표시

```json
{
  "status": "preview_ready",
  "next_action": "결과를 확인해주세요",
  "allowed_actions": [
    "approve",
    "request_change",
    "open_on_phone",
    "stop_preview"
  ]
}
```

- UI는 `allowed_actions`에 포함된 버튼만 표시합니다.
- UI가 상태 문자열을 보고 가능한 Action을 자체 추론하지 않습니다.
- 클릭 후 V2 Core가 성공을 반환한 뒤에만 화면 상태를 갱신합니다.
- YAML 직접 수정, 임의 Shell 실행과 낙관적 상태 변경을 금지합니다.

## 5. 장애 격리와 준비 상태 검증

첫 UI 검증은 정상 화면보다 장애 격리를 우선합니다.

필수 시나리오:

1. PDF Preview 서버 종료 후에도 V2 UI가 유지됩니다.
2. 다른 프로젝트로 이동하면 해당 프로젝트 Preview가 정상 표시됩니다.
3. Port 충돌을 안내하고 임의 Port 변경을 하지 않습니다.
4. Galaxy 연결이 끊겨도 PC Preview가 유지됩니다.
5. HTTP `200`이어도 제품 초기화 신호가 없으면 미리보기 문제로 표시합니다.
6. Preview 장애가 Core, 다른 프로젝트와 과거 결과에 영향을 주지 않습니다.

Preview 준비 완료는 `health_url` 응답과 제품 초기화 상태 신호를 모두 확인한 경우에만 인정합니다.

## 승인된 표시·연결 기준

- 기본 레이아웃: 요청 `25%` / Preview `75%`
- 대화 보기: `40%` / `60%`
- Preview 크게: `10%` / `90%`
- V2 UI Port: `8200`
- 휴대폰 기본 연결: USB + `adb reverse`
- `scrcpy`: 선택 기능
- 기본 화면에서는 Run ID, Commit SHA, 내부 Gate와 기술 로그를 숨깁니다.

## 공식 디자인 방식 — Hybrid H

```text
Reference Mix → Design DNA 이미지 탐색 → A/B/C 비교 → 선택·혼합
→ 화면·핵심 상태별 visual_target → 사용자 시각 승인 → Image-to-Code
→ 동일 Viewport Fidelity 비교·수정 → Fidelity PASS → 코드가 디자인 원본
```

- `design-draft.json`은 구조 계약이며 시각 원본을 대신하지 않습니다.
- 승인된 `visual_target`을 Image-to-Code에 직접 입력합니다.
- 화면 전체를 한 이미지에 강제하지 않고 화면·핵심 상태별 `visual_target`을 허용합니다.
- 기준 Viewport는 `1440×950`, `430px`, `390px`입니다.
- Fidelity는 레이아웃, 정보 우선순위, 타이포그래피, 색상·배경, 표면·테두리, 간격·밀도, 모바일 흐름과 Preview 비중을 확인합니다.
- Fidelity PASS 이후에만 코드가 공식 `design_source_of_truth`가 됩니다.
- 이후 변경은 Section ID·Design Token·컴포넌트 단위로 수행하며 큰 방향 변경만 이미지 탐색부터 다시 시작합니다.

## 현재 상태와 다음 Gate

```yaml
thin_ui:
  contract_status: approved
  implementation_status: not_started
  selected_direction: MIX-1
  reference_mix_status: researched
  clickable_preview_status: rejected_visual_fidelity
  current_preview_usage: rejected_design_evidence
  implementation_input: prohibited
  next_action: create_and_review_visual_targets
```

기존 클릭형 Preview는 상호작용·반응형 구조 증거로 보존하지만 시각 충실도 실패로 구현 입력에 사용할 수 없습니다. 다음 작업은 MIX-1의 화면·핵심 상태별 `visual_target`을 만들고 사용자 시각 승인을 받는 것입니다.
