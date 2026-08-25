# AI OS V2 Design System 운영 계약

## 목적

AI OS V2에서 생성·선택·구현·부분 수정되는 모든 UI의 근거와 계보를 남깁니다. 도구 이름이나 디자인 출처를 추정하지 않으며 실제 실행 증거가 있는 항목만 기록합니다.

## 필수 Provenance

모든 Visual Target과 구현 결과는 다음을 기록합니다.

```yaml
design_provenance:
  artifact_id:
  version:
  created_at:
  target_screen:
  source_viewport: 390x844
  derived_viewports: [430x932, 1440x950]
  used_tools: []
  used_skills: []
  references: []
  input_images: []
  prompt_file:
  design_tokens:
  section_order: []
  component_families: []
  implementation_tool: null
  verification_tool: null
  user_decision: pending
  rejection_reason: null
```

### 기록 예

- UI UX Pro Max를 실제 호출했다면 `used_tools`에 `UI UX Pro Max`와 역할을 기록합니다.
- Figma에서 실제 Frame·Component를 만들었다면 Figma File·Node URL과 작업 방식을 기록합니다.
- built-in ImageGen으로 Visual Target을 만들었다면 `OpenAI built-in ImageGen`으로 기록합니다.
- `frontend-app-builder`, `product-design:ideate`, `product-design:image-to-code` 같은 Skill은 실제 사용했을 때만 기록합니다.
- Reference 링크은 원본 URL, 조회일, License·이용 조건, 적용 영역을 함께 기록합니다.

## 디자인 다양성 Gate

세 후보는 다음 중 최소 네 축이 달라야 합니다.

1. 정보 우선순위
2. Navigation·탐색 방식
3. Section 순서
4. Content Density
5. Card·List·Canvas 구성
6. 이미지 사용 방식
7. CTA 위치
8. 모바일 작업 흐름
9. Motion 역할
10. Typography Rhythm

색상·그림자·Radius만 다른 후보는 FAIL입니다. 후보 수가 많더라도 같은 Design DNA의 변형이면 다양성으로 계산하지 않습니다.

## 다양성 Source Pool

- `UI UX Pro Max`: 업종·UX 규칙·레이아웃·색상·Typography 지식
- `Product Design ideate + built-in ImageGen`: 구조적으로 다른 Visual Target 탐색
- `frontend-app-builder`: 승인된 Visual Target의 디자인 시스템 추출과 Fidelity 구현
- `Storybook`: Component 상태·Responsive·접근성 검증 후보
- `Style Dictionary`: Token Source of Truth 후보
- `shadcn/ui registry`: 재사용 가능한 Component·Block 후보. 복사 전 License·의존성·디자인 적합성 검증
- `Penpot`: Figma가 맞지 않을 때 검토할 오픈소스 디자인·프로토타이핑 후보

새 도구는 자동 채택하지 않습니다. 격리 Pilot, 출력 품질, License, 유지관리 상태, 모바일 결과를 비교한 뒤 `candidate → piloted → approved`로 승격합니다.

## 마음에 들지 않을 때의 복구 흐름

```text
현재안 보존
→ 사용자가 싫은 이유를 화면·Section 단위로 표시
→ rejection_reason 기록
→ 유지할 요소와 버릴 요소 분리
→ Reference Source Pool 재조사
→ 구조적으로 다른 세 후보 생성
→ 모바일 390px에서 먼저 비교
→ 선택·혼합
→ 단일 Visual Target 생성
→ 430px·PC 확장
→ 사용자 승인 전 구현 금지
```

거절 사유는 최소한 다음으로 분류합니다.

- `information_hierarchy`
- `layout_structure`
- `visual_tone`
- `content_density`
- `mobile_usability`
- `navigation`
- `trust_and_clarity`
- `reference_mismatch`
- `other_user_reason`

## Layout·부분 수정 환경

- 모든 화면과 주요 Section에 안정적인 ID를 부여합니다.
- `section_order`는 배열로 보존하여 Drag·Move 요청을 명시적 순서 변경으로 변환합니다.
- 부분 수정은 Section ID, 허용 속성, 영향받는 Viewport를 포함합니다.
- Token은 색상·Typography·Spacing·Radius·Border·Motion으로 분리합니다.
- 변경은 `Draft → 모바일 Preview → 영향 범위 검증 → 사용자 적용 → Rollback 가능 상태` 순서입니다.
- 선택한 코드가 디자인 Source of Truth가 된 후에도 이전 Visual Target과 Fidelity Ledger를 삭제하지 않습니다.

## Mobile-First Gate

모든 신규 UI의 제작 순서는 다음으로 고정합니다.

1. `390×844` 구조·핵심 흐름·Touch Target
2. `430×932` 여백·정보량 확장
3. `1440×950` 다단 Layout 확장

PC 시안을 먼저 만들고 모바일로 축소하는 방식은 금지합니다. 기존 PC 전용 화면은 모바일 재설계를 먼저 수행한 뒤 PC를 재파생합니다.

프로젝트 작업실 모바일 규칙:

- 기본 탭은 `미리보기`
- Preview가 첫 화면의 70% 이상을 사용
- 축소된 휴대폰 Mockup을 Preview 안에 다시 넣지 않음
- 요청·진행·Reference·기술 정보는 별도 탭 또는 Bottom Sheet
- 390·430·PC 전환은 Preview 상단에 유지
- 승인 Action은 44px 이상이며 상태를 색상만으로 표시하지 않음

## Docker 메뉴 계약

전역 Navigation에 `Docker`를 추가할 수 있습니다. PM1에서의 역할은 다음으로 제한합니다.

- 프로젝트별 Container 실행 여부
- Image·Container·Port의 읽기 중심 요약
- 충돌·실패·재시작 필요 상태
- 사용자에게 필요한 다음 행동 하나
- 기술 상세 접기

PM1 제외:

- 임의 Image 삭제
- Container 강제 종료
- Compose 파일 자유 편집
- Registry 로그인·Push
- Docker Desktop 전체 대체

실제 제어 Action은 Core `allowed_actions`와 사용자 승인 없이는 표시하지 않습니다.

## 결과 보고 형식

UI 결과 보고에는 항상 다음을 포함합니다.

```yaml
ui_result:
  references_used:
  tools_used:
  skills_used:
  generated_with:
  implemented_with:
  verified_with:
  source_viewport:
  derived_viewports:
  section_ids:
  diversity_gate:
  user_decision:
  files_changed:
  core_run_commit_push_changed:
```

