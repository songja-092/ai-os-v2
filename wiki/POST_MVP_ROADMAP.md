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

## 1순위 UI 후보 — Direct Partial Edit Panel

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

## 2순위 UI 후보 — 실제 Run 상태를 읽는 얇은 UI

Core의 실제 Run·Gate·검증 결과만 읽어 사용자에게 요청, 현재 단계, Preview와 다음 행동을 보여줍니다. 가짜 진행률이나 별도 상태 저장소를 만들지 않습니다.

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
