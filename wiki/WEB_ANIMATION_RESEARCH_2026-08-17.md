# AI OS V2 웹 애니메이션 조사

작성일: 2026-08-17  
상태: 조사 완료·도입 전  
범위: V2가 제작하는 고객 웹의 Motion Reference·구현 도구·검증 규칙

## 1. 결론

V2는 애니메이션 도구 하나를 모든 화면에 강제하지 않습니다.

```text
CSS·Web Animations API
→ Motion for React
→ Anime.js Adapter
→ 특수 프로젝트에서만 GSAP 검토
```

- 단순 Hover·색상·Opacity·짧은 전환은 CSS를 우선합니다.
- React 상태·Card 이동·Layout 전환·Modal·Gesture는 `Motion`을 기본 후보로 둡니다.
- 복잡한 Timeline·SVG·Text·Canvas·Three.js 연출은 `Anime.js`를 제거 가능한 Adapter 후보로 둡니다.
- `Kokonut UI`, `Magic UI`, `Animate UI`, `React Bits`는 엔진이 아니라 눈으로 고르고 코드를 검토하는 Animated Component Reference 창고입니다.
- GSAP은 강력하고 고객 웹 제작에는 사용할 수 있지만 V2가 시각적 Animation Builder로 발전할 때 라이선스 경계가 생기므로 기본 엔진으로 채택하지 않습니다.

설치와 제품 적용은 아직 하지 않습니다.

### 검증 우선 도입 원칙

사용자는 실험적 도구 비교를 선호하지 않습니다. 따라서 V2는 여러 Engine을 동시에 설치·시험하지 않고 다음 순서를 고정합니다.

```text
검증된 Browser 기본 기능으로 구현
→ 실제 요구를 충족하면 그대로 종료
→ 부족한 기능이 증거로 확인될 때 Motion 하나만 도입
→ Motion으로 해결되지 않는 SVG·Timeline 요구가 생길 때만 Anime.js 검토
→ 새로운 도구는 안정적인 기본 방식이 운영된 뒤 별도 격리 Pilot
```

- PM1에서는 Library를 설치하는 실험 대신 실제 운영 사례와 완성 Demo를 보고 Motion 강도와 사용할 패턴만 선택합니다.
- PM2의 React Stack이 확정되면 일반 UI용 Motion 하나만 작은 실제 기능에 적용하고 Build·모바일·접근성·제거를 검증합니다.
- AutoAnimate는 카드 순서 이동만 필요하고 Motion을 도입하지 않았을 때의 단순 후보입니다. Motion과 동시에 중복 설치하지 않습니다.
- Anime.js·dotLottie·GSAP은 실제 프로젝트 요구가 생기기 전에는 설치하지 않습니다.
- 실험 후보는 기본 기능·Recipe·Core 상태를 소유할 수 없으며 `feature_flag: false`와 Package 제거로 완전히 분리할 수 있어야 합니다.

## 2. 방식별 비교

| 방식 | 기능 | 장점 | 단점·위험 | V2 판정 |
|---|---|---|---|---|
| CSS·WAAPI | Hover, Fade, Transform, 간단한 Scroll·View Transition | 추가 의존성 없음, 빠름, 제거 쉬움 | 복잡한 Timeline·React 상태 연동은 관리가 어려움 | 기본 1단계 |
| Motion for React | React 상태 기반 전환, Layout, Reorder, Gesture, Scroll, Exit | React와 자연스럽고 MIT, Layout 조립 보드와 잘 맞음 | 고급 연출을 남용하면 Bundle·복잡도 증가 | 기본 엔진 후보 |
| Anime.js | Timeline, Stagger, SVG, Text, Draggable, Layout, WAAPI, Three.js Adapter | 모듈별 Import, 프레임워크 독립, 정교한 연출 | React 상태와 직접 연결할 때 생명주기 관리 필요 | 특수 연출 Adapter 후보 |
| GSAP | ScrollTrigger, SplitText, MorphSVG, Timeline 등 고급 연출 | 업계 사용 경험과 기능 범위가 넓음 | V2의 시각적 Animation Builder 목표와 라이선스 제한 충돌 가능 | 기본 제외·프로젝트별 법적 검토 |
| Kokonut UI | Motion이 적용된 React·Tailwind·shadcn Component | MIT, 복사·수정 가능, 결과를 눈으로 고르기 쉬움 | Next·Tailwind 전제와 품질을 Component별 재검증해야 함 | PM1 Reference 창고 후보 |
| Magic UI | Animated Component·Effect Registry | MIT, 큰 커뮤니티, shadcn 방식으로 코드 소유 가능 | 장식 효과가 많아 정보 UI에 과사용 위험 | PM1 Reference 창고 우선 후보 |
| Animate UI | Motion 기반 Primitive·Component·Icon | Copy-first, 접근성·유지보수 목표, shadcn 호환 | 비교적 새 프로젝트라 Component별 검증 필요 | PM1 Reference 창고 후보 |
| React Bits | Text·Background·UI 애니메이션 110개 이상 | 다양성이 매우 크고 React/Vite 선택지가 많음 | MIT 단독이 아닌 Commons Clause 포함, 화려한 효과 과사용 위험 | 시각 Reference 우선·코드 재사용 별도 검사 |

## 3. 사용자가 조사한 두 도구

### Kokonut UI

- 종류: 애니메이션 엔진이 아니라 완성 Component 모음
- 기반: React, Tailwind CSS, shadcn/ui, Motion
- 라이선스: MIT
- 적합한 용도: 버튼·Card·Dialog·Hero·Micro-interaction을 실제 화면으로 보고 선택
- V2 사용법: 전체 Library를 설치하지 않고 선택 Component의 코드·의존성·접근성을 검사한 뒤 Candidate로 가져옵니다.

### Anime.js

- 종류: 애니메이션 엔진
- 기능: Animation, Timeline, Draggable, Layout, SVG, Text, WAAPI와 Adapter
- 적합한 용도: 도면 기호 강조, SVG Path, 숫자·Text Sequence, 복잡한 Landing Page Timeline, 이후 Three.js 연동
- V2 사용법: `animation_adapter: animejs`로 표시하고 해당 Section에만 연결합니다. 제거 시 정적 상태와 핵심 기능은 그대로 유지해야 합니다.

## 4. GitHub·커뮤니티 신호

- Motion GitHub는 약 32.1k Star와 MIT License를 보이며 React 공식 문서는 Layout·Gesture·Scroll을 직접 지원합니다.
- React Bits는 약 40.1k Star, Magic UI는 약 21.1k Star, Kokonut UI는 약 2.0k Star입니다. Star는 발견 우선순위일 뿐 품질 PASS가 아닙니다.
- Reddit에서는 React UI에 Motion이 자연스럽다는 의견과 GSAP의 고급 제어력을 높게 보는 의견이 반복됩니다.
- 모바일 끊김은 Library 이름보다 `width`, `height`, `top`, `left`처럼 Layout·Paint를 일으키는 속성 사용이 원인이라는 실무 의견이 강합니다. 공식 성능 지침도 기본적으로 `transform`과 `opacity`를 우선합니다.
- 애니메이션 Component 소개 글의 긍정 반응과 함께 `prefers-reduced-motion` 누락을 지적하는 의견도 확인됐습니다. Reddit은 성공 증거가 아니라 위험 발견 신호로만 사용합니다.

## 5. V2에 필요한 Motion 계약

```yaml
motion_recipe:
  motion_id: string
  section_id: string
  purpose: feedback | transition | hierarchy | storytelling
  trigger: load | hover | press | focus | in_view | state_change | scroll
  adapter: css | waapi | motion | animejs
  preset: fade | slide | scale | layout | stagger | custom
  duration_token: instant | fast | normal | slow
  easing_token: standard | emphasized | spring
  properties: [opacity, transform]
  reduced_motion: none | fade_only | instant
  mobile_enabled: boolean
  source_reference_id: string
```

규칙:

- 애니메이션은 목적이 있어야 하며 장식만을 이유로 기본 활성화하지 않습니다.
- `prefers-reduced-motion`을 반드시 지원합니다.
- 기본 속성은 `transform`과 `opacity`이며 다른 속성은 Performance 검증이 필요합니다.
- 자동 재생·무한 반복·큰 Parallax는 기본 금지합니다.
- Animation Adapter를 제거해도 Content·Action·Layout의 최종 상태가 유지돼야 합니다.
- 사용자 승인 전 고객 제품에 적용하지 않습니다.

## 6. PM 연결

### PM1 — 디자인 탐색·채택

- Reference Board에 정적 디자인과 Motion Reference를 분리해 표시합니다.
- Hover·전환·Scroll·Layout 등 사용할 움직임을 짧은 실제 Demo로 확인합니다.
- Kokonut UI·Magic UI·Animate UI·React Bits에서 최소 10개를 조사하되 전체 화면을 화려하게 만드는 후보만 모으지 않습니다.
- 디자인 방향과 Motion 강도(`없음`, `절제`, `표현적`)를 별도로 선택합니다.

### PM2 — 조립식 V2 보드

- Motion은 Module이 아니라 제거 가능한 Renderer·Adapter입니다.
- Module 이동과 상태 변화에는 Motion 후보를 사용하되 Core 상태를 소유하지 않습니다.

### PM3 — 부분 수정

- 사용자는 마우스로 Motion Preset, 속도, 강도, 끄기를 선택합니다.
- 자연어는 “더 빠르게”, “움직임 줄여줘” 정도의 보조 입력만 담당합니다.
- 수정은 `Motion Recipe Diff`와 새 Version으로 저장합니다.

### PM6 — 통합 검증

- Reduced Motion, Keyboard·Focus, 모바일 성능, CPU Throttling, Layout Shift, Console을 검증합니다.
- 디자인 품질 PASS와 Motion 성능·접근성 PASS를 분리합니다.

## 7. Skill과 자동화 판단

현재 설치된 도구 중 Figma Motion Skill은 Figma에서 정의된 Motion을 코드로 옮길 때만 사용합니다. 일반 웹 애니메이션을 자동 선택하는 검증된 전용 Skill로 확대 해석하지 않습니다.

GitHub에는 Animated Component를 찾아주는 Agent Skill 사례가 있지만, 그대로 설치하기보다 다음 읽기 전용 Workflow가 V2에 더 안전합니다.

```text
화면 목적과 Motion 강도 선택
→ Registry에서 후보 검색
→ Source·License·Dependency 확인
→ Reduced Motion·성능 규칙 검사
→ 실제 Demo 3개 추천
→ 사용자 선택
→ 격리 Preview
→ 적용 또는 완전 제거
```

효과가 검증되면 이 Workflow를 `motion-reference-collector` Skill 후보로 만들 수 있습니다. 설치·코드 복사·제품 적용·Commit은 계속 사용자 승인 대상으로 둡니다.

## 8. 최종 판정

```yaml
kokonut_ui:
  role: animated_component_reference
  adoption: candidate
animejs:
  role: advanced_motion_adapter
  adoption: candidate
motion:
  role: default_react_motion_engine_candidate
  adoption: requires_PM2_pilot
css_waapi:
  role: default_simple_motion
  adoption: recommended
gsap:
  role: exceptional_project_adapter
  adoption: deferred_license_boundary
motion_skill_install_now: false
pm1_motion_reference_research: allowed
product_code_changed: false
adoption_policy: proven_default_first
parallel_library_experiment: prohibited
```

다음 한 작업은 PM1 Reference Board 안에 `정적 구조`와 `Motion Demo`를 분리하고, Kokonut UI·Magic UI·Animate UI·React Bits에서 목적이 다른 실제 후보 10개를 구성하는 것입니다.
