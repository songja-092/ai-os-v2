# Post-MVP Roadmap

표준 사용자 제작 흐름은 [[V2_STANDARD_USER_FLOW]] · [GitHub 링크](V2_STANDARD_USER_FLOW.md)를 따릅니다.

M7 PASS 이후 V2가 사용자의 반복 설명 없이 다음 조사·분석 후보를 불러오기 위한 공식 로드맵입니다. 이 문서는 자동 구현 권한을 부여하지 않습니다.

## 연속 실행 상태

```yaml
post_mvp:
  status: ready_after_m7_pass
  roadmap_path: wiki/POST_MVP_ROADMAP.md
  next_candidate: direct_partial_edit_panel
  auto_research_allowed: true
  auto_analysis_allowed: true
  auto_implementation_allowed: false
  user_approval_required_for_implementation: true
```

## 후보 상태 언어

- 💡 `proposed`
- 🔎 `researched`
- 🧪 `pilot_ready`
- 🔨 `implemented`
- ✅ `verified`
- 📦 `reusable_recipe`
- ⏸ `deferred`
- ❌ `rejected`

GitHub에서 발견하거나 문서로 조사했다는 이유만으로 `verified`로 올리지 않습니다. `reusable_recipe`는 실제 프로젝트·환경 실행, 실패 처리, 사용자 확인, Commit과 Rollback/Restore가 필요합니다.

## 2순위 UI 후보 — Direct Partial Edit Panel

```yaml
id: direct_partial_edit_panel
status: proposed
scope: HERO-01 only
goal: 초보 사용자가 Preview에서 HERO-01을 선택하고 글자 크기·콘텐츠 폭·줄바꿈·배경색을 제한된 값으로 조절한다.
controls:
  - 원래대로
  - 미리보기
  - 적용
required_verification:
  - 390px
  - 430px
  - 1440px
  - horizontal overflow
  - console errors
  - new artifact version
  - rollback
tool_candidate: Tweakpane
implementation_approved: false
```

M6에서 `HERO-01` AI 부분 수정과 복구 기반은 검증했지만 Preview 요소 선택, 슬라이더·색상 선택, 실시간 적용, 설정 저장과 새 Artifact Version은 아직 미검증입니다. Dashboard 전체나 범용 페이지 편집기보다 이 한 영역 파일럿을 먼저 검토합니다.

## 1순위 UI 후보 — 실제 Run 상태를 읽는 얇은 UI

Core의 실제 Run·Gate·검증 결과만 읽어 사용자에게 요청, 현재 단계, Preview와 다음 행동을 보여줍니다. 가짜 진행률이나 별도 상태 저장소를 만들지 않습니다. 다섯 가지 승인 계약은 [[THIN_UI_MVP_CONTRACT]] · [GitHub 링크](THIN_UI_MVP_CONTRACT.md)를 따르며 현재 다음 작업은 정적 이미지 시안 2개 비교입니다.

## 기능 후보 — Web Camera Capture

```yaml
id: web_camera_capture
status: researched
goal: Galaxy에서 후면 카메라로 촬영하고 Preview에서 확인·재촬영·압축하며 휴대폰 앨범에는 자동 저장하지 않는다.
base_technology:
  - getUserMedia
  - Canvas 또는 ImageCapture
required_verification:
  - Galaxy 실제 기기
  - 권한 거절
  - 전면·후면 전환
  - 화면 회전
  - 연속 촬영
  - 사진 압축
  - 카메라 실패 대체 경로
implementation_approved: false
```

현재 상태는 공식 자료 기반 조사 완료이며 V2 실제 파일럿과 검증 전입니다.

## 편의·품질·운영 후보 — 2026-08-14 조사

아래 항목은 공식 문서·공식 GitHub와 공개 사용 사례를 확인한 `researched` 후보입니다. 등록은 설치·채택·호출·검증 완료를 의미하지 않으며, 현재 1순위 얇은 UI와 2순위 `Direct Partial Edit Panel`의 순서를 바꾸지 않습니다.

### 우선 파일럿 후보

| 후보 | 역할 | 적용 조건 | 상태 |
| --- | --- | --- | --- |
| GitHub MCP Server | 저장소·Issue·PR·Actions 읽기/쓰기 | 프로젝트 한정 권한, 쓰기 전 Core 승인 Gate | 🔎 researched |
| Dependabot | 취약 의존성 경고와 보안 업데이트 PR | GitHub 저장소별 활성화 | 🔎 researched |
| Gitleaks | Commit 전 Token·비밀번호 등 비밀값 탐지 | 읽기 전용 검사 파일럿 후 차단 여부 결정 | 🔎 researched |
| Lighthouse | 성능·접근성·SEO·기본 품질 검사 | 기존 Chrome으로 최종 검증·배포 준비 시 실행 | 🔎 researched |
| ADB reverse + scrcpy | 실제 Galaxy Preview와 PC 제어 | 별도 창 방식의 실기기 파일럿 승인 시 | 🔎 researched |

GitHub 쓰기는 V2가 임의 실행하지 않고 `변경 준비 → 사용자 확인 → 승인된 쓰기` 순서를 따른다. 후보가 실제 도입되기 전에는 현재 `gh` 설치 여부나 GitHub 연결을 V2 기능 검증으로 간주하지 않는다.

### 프로젝트 요구가 생길 때만 검토

| 후보 | 역할 | 적용 조건 | 상태 |
| --- | --- | --- | --- |
| axe-core | 자동 접근성 검사 | 공공·상업 웹 또는 접근성 요구가 명확한 프로젝트 | 🔎 researched |
| MSW | Backend 없이 성공·오류·지연 응답 검증 | 데이터 연동 UI를 Backend보다 먼저 검증할 때 | 🔎 researched |
| Mockoon | GUI 기반 로컬 Mock API | 비개발자가 가짜 API 상태를 직접 조절해야 할 때만 MSW 대안 | 🔎 researched |
| Bruno | 로컬·Git 기반 API 요청 검증 | API·인증·Full-stack 프로젝트 | 🔎 researched |
| mkcert | 로컬 HTTPS | LAN·카메라·PWA에서 HTTPS가 실제로 필요하고 localhost로 해결되지 않을 때 | 🔎 researched |
| Trivy | Container·의존성·설정·SBOM 검사 | Docker·배포 가능한 프로젝트 | 🔎 researched |
| Sentry | 배포 후 Runtime 오류 수집 | 외부 전송·개인정보 정책을 승인한 운영 프로젝트 | 🔎 researched |

MSW와 Mockoon은 중복 기본 도구로 함께 설치하지 않는다. 코드·자동검증 연결이 중요하면 MSW, GUI 조작이 중요하면 Mockoon 하나만 작은 프로젝트에서 시험한다.

### V2 Core에 결합하지 않는 개인 편의 후보

- `LocalSend`: PC와 Galaxy 사이의 로컬 파일 전송 후보입니다. V2 Core 기능이 아니라 선택형 개인 도구로만 둡니다.
- `GitButler`: 시각적 Git 작업 관리 후보지만 V2 Core의 Run·Commit·Rollback 책임과 중복되고 라이선스 검토도 필요하므로 제품 통합 대상에서 제외합니다.

### 현재 보류 또는 과설계 방지

- `Renovate`: Dependabot으로 부족함이 증명되는 다중 저장소·복잡한 업데이트 단계까지 보류합니다.
- `Uptime Kuma`: 배포된 서비스가 여러 개 생기기 전에는 로컬 Health 표시보다 무겁습니다.
- 외부 Web Testing·Security Skill 대량 설치: 현재 Codex·Browser·`frontend-testing-debugging`과 중복 여부를 먼저 검증합니다.
- 모든 프로젝트의 Docker·Dev Container 강제: 프로젝트별 재현성 이득이 설정·자원 부담보다 클 때만 사용합니다.

권장 검증 순서는 `얇은 V2 UI → GitHub MCP 최소 권한 → Gitleaks 읽기 전용 검사 → Lighthouse → Galaxy ADB/scrcpy`입니다. 이후 도구는 실제 프로젝트 요구가 생길 때 하나씩 검증합니다.

## M7 이후 자동 허용 범위

`상태 조회 → 후보 로드 → 기존 레시피·설치 도구 확인 → 공식 문서·GitHub 조사 → 구현 가능성 분석 → 추천 보고서와 Preview 준비안 생성`

사용자에게는 다음만 제시합니다.

```text
다음 추천: 직접 부분 수정 패널
현재 상태: 제안
추천 목표: HERO-01 하나에서 제한된 값을 직접 조절하고 안전하게 복구하는 Preview

[진행] [나중에] [다른 후보 보기]
```

## 사용자 승인 Gate

외부 패키지 설치, 기존 제품 변경, 실제 데이터, 로그인·권한, DB, 개인정보, 결제, 배포, 비밀키, 삭제·마이그레이션과 고객 계정 접근은 사용자 승인 전 실행하지 않습니다.

별도 임시 디렉터리, 새 Preview Version, 가짜 데이터와 원본 불변 조건을 만족하는 가역적 파일럿만 자동 후보가 될 수 있습니다. 자동 재시도는 하지 않으며 실패하면 즉시 중단하고 증거를 보존합니다.

## 후속 후보 원칙

추가 후보는 한 번에 하나씩 `proposed`로 등록합니다. 별도 학습 모델·Vector DB·Fine-tuning은 만들지 않고, 검증 Run의 성공·실패 이유와 Recipe 상태를 다음 Run의 검색 우선순위로 재사용합니다.
