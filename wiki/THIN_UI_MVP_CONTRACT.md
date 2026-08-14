# V2 Thin UI MVP Contract

이 문서는 `AI OS V2 Core MVP` 위에 제작할 Post-MVP `PM1 — 얇은 UI`의 승인된 설계 계약입니다. UI 코드, 클릭형 Preview 또는 새 상태 저장소를 구현했다는 의미가 아닙니다.

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

## 클릭형 Preview 디자인 기준

- 프로젝트 홈: `B — 프로젝트·다음 행동 중심`
- 프로젝트 작업실: `A — Preview 중심`
- 요청 영역: 필요할 때 펼치는 보조 영역
- 기본 비율: 요청 `25%` / Preview `75%`
- Preview 집중: 요청 `10%` / Preview `90%`
- 모바일 진입: 현재 행동에 따라 `프로젝트`, `미리보기`, `진행` 중 하나
- Reference Mix는 [[ui-reference-mix]] · [GitHub 링크](ui-reference-mix.md)를 따르며 특정 제품의 화면·브랜드·코드·아이콘을 복제하지 않습니다.
- 기존 이미지 시안 5장은 초기 참고자료이며 공식 UI 승인 결과가 아닙니다.

## 현재 상태와 다음 Gate

```yaml
thin_ui:
  contract_status: approved
  implementation_status: not_started
  image_mockup_status: reference_only
  reference_mix_status: researched
  clickable_preview_status: not_started
  next_action: create_mobile_first_clickable_previews_a_b
```

다음 작업은 같은 계약과 Reference Mix를 반영한 모바일 우선 클릭형 Preview A/B를 비교하는 것입니다. 사용자는 `A`, `B` 또는 `수정 요청`만 선택합니다. 사용자 선택 전에는 실제 PM1 UI, Registry 실행 연결, Preview 프로세스 제어, ADB 연결 또는 새 패키지를 구현하지 않습니다.
