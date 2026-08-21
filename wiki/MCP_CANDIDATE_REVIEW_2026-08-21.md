# V2 MCP 후보 조사 — 2026-08-21

## 목적

PM3의 작은 편집기만 교체하는 조사가 아니다. V2 전체의 디자인 탐색·구현·편집·검증·
3D 제작 병목을 외부 MCP로 보완할 수 있는지 확인한다. 후보는 V2 Core의 주인이 되지 않고
제거 가능한 Adapter여야 하며, 설치·제품 수정·외부 전송은 사용자 선택 뒤 격리 Pilot에서만
수행한다.

## 로컬 확인

- Codex Desktop Node: `22.22.2`
- npm: `10.9.7`
- pnpm: `11.19.0`
- Docker: 설치됨
- Blender: 설치되지 않음
- V2/PM3에 `components.json`과 Storybook 설정: 없음
- 실제 MCP 설정: `node_repl`만 확인됨
- Puck·React Grid Layout·Motion: 별도 PM3 격리 Pilot에만 설치됨

## 기존 다섯 후보

### 1. shadcn MCP

- 공식 shadcn MCP가 존재하며 Registry의 Component·Block 검색과 설치를 지원한다.
- Codex 설정 경로가 공식 문서에 제공된다.
- 장점: 구현 가능한 실제 소스와 의존성을 바로 확인할 수 있다.
- 위험: 읽기 전용 Reference 도구가 아니라 대상 프로젝트에 코드를 설치·수정할 수 있다.
- 현재 V2에는 `components.json`이 없으므로 바로 연결해도 사용할 프로젝트 계약이 없다.
- 판정: `isolated_pilot_recommended`, 전역 자동 설치 금지.

### 2. Storybook MCP

- `storybookjs/mcp`는 Storybook 공식 조직의 MCP·Codex Plugin 프로젝트다.
- Component Story·문서·상태를 AI가 조회하는 데 적합하다.
- 프로젝트는 실험적이며 API·구조가 변경될 수 있다고 명시한다.
- 현재 개발 저장소 요구사항은 Node 24+이며 V2 Node 22와 맞지 않는다.
- V2에 Storybook 설정과 충분한 재사용 Component Story가 아직 없다.
- 판정: `hold_until_component_library_and_node24`.

### 3. Raven MCP

- 개인 오픈소스 MCP이며 공식 표준기관 제품은 아니다.
- Apache-2.0, 로컬 stdio `npx -y raven-mcp`를 제공한다.
- URL·HTML·Screenshot의 Contrast·Typography·Spacing·Responsive·Content Audit 기능이 있다.
- UI UX Pro와 원칙·Checklist는 중복되지만 실제 렌더 URL Audit과 전후 비교는 보완 가능하다.
- 로컬 실행과 원격 실행을 구분해야 하며 비공개 화면은 원격 endpoint에 보내지 않는다.
- 판정: `read_only_audit_pilot_recommended`, UI UX Pro와 같은 화면 비교 후 채택 결정.

### 4. Penpot MCP

- Penpot 공식 MCP가 존재하고 조회·생성·수정 작업을 지원한다.
- Node 22에서 시험된 공식 안내가 있어 현재 Runtime과 맞는다.
- MCP 서버, Plugin 서버, Penpot Plugin UI 연결이 모두 필요해 운영이 단순하지 않다.
- Plugin UI를 열어 둬야 하며 Plugin API 안에서 AI 생성 JavaScript를 실행한다.
- 과거 2.15.0 미만 MCP의 무인증 REPL 원격 코드 실행 취약점이 공개됐다.
- 판정: `security_gated_isolated_pilot`; 최신 2.15.0+ 고정, localhost, 임시 Penpot 파일,
  비공개 고객 자산 미연결 조건. Puck 대체로 사전 확정하지 않는다.

### 5. Blender MCP

- Blender 공식 Lab MCP가 존재하지만 Blender 자체 내장 기능은 아니며 Add-on·Client·Server가
  필요하다.
- 공식 안내도 LLM 생성 Python 코드를 보호 장치 없이 실행한다고 경고하고 VM 또는 민감
  자료가 없는 시스템을 권장한다.
- 현재 Blender가 설치되지 않았고 PM3 운영 UI에 3D 요구가 없다.
- 판정: `defer_until_real_3d_customer_project`; 현재 설치 금지.

## 추가로 찾은 V2 후보

### Chrome DevTools MCP

- Google 공식이며 현재 Stable로 안내된다.
- Antigravity를 포함한 MCP Client에서 실제 Chrome의 DOM·Console·Network·Performance를
  검사할 수 있다.
- 현재 Codex에는 Browser Plugin이 있어 Codex 쪽에서는 중복이다.
- Antigravity 구현 뒤 실제 화면 검증과 현재 `antigravity_execution` 문제 해결 후의 독립
  디버깅에는 가치가 높다.
- 로그인 Browser 연결은 Cookie·화면 내용을 Agent가 볼 수 있으므로 깨끗한 격리 Profile만
  사용한다.
- 판정: `antigravity_verification_candidate`, 현재 Blocker 해결 후 Pilot.

### Context7 MCP 또는 CLI

- React·Puck·Motion 등 Version별 최신 문서와 예제를 가져와 존재하지 않는 API 사용을
  줄이는 보조 도구다.
- Node 20.18.1+ 조건은 충족한다.
- 문서 Query는 외부 서비스로 전송되며 Backend 전체가 오픈소스는 아니다.
- V2 코드를 보내지 않고 Package명·Version·질문만 보내야 한다.
- MCP가 꼭 필요하지 않으며 제거가 쉬운 CLI·Skill 방식도 제공한다.
- 판정: `optional_docs_accuracy_candidate`; MCP보다 일회성 CLI/Skill 우선.

## 중복으로 추가하지 않을 후보

- Playwright MCP: Microsoft 공식이고 강력하지만 현재 Codex Browser Plugin과 기존 Browser
  검증 흐름이 해결하는 역할과 겹친다. 별도 실패 증거 전 추가하지 않는다.
- Figma MCP: 현재 Codex에 Figma Plugin·Skill이 이미 제공되므로 새 MCP를 중복 설치하지
  않는다. 실제 Figma 파일을 사용할 프로젝트에서 기존 연결부터 검증한다.
- GitHub MCP: 현재 Codex GitHub Plugin이 있어 후보 조사·Repo 조회 목적의 중복 설치는 하지
  않는다.

## 우선순위

1. Raven 로컬 읽기 전용 Audit Pilot — 기존 URL 한 개, 파일 수정 금지
2. shadcn 격리 구현 Pilot — 가짜 React 프로젝트, Component 하나, Diff 확인
3. Penpot 보안 격리 Pilot — 임시 디자인 파일, 최신 고정 Version, localhost
4. Chrome DevTools MCP — Antigravity 실행 Blocker 해결 뒤 검증용
5. Storybook MCP — 실제 Component Library와 Node 24 Runtime이 준비된 뒤
6. Blender MCP — 실제 3D 고객 프로젝트가 생긴 뒤

## 현재 판정

```yaml
installation_performed: false
config_changed: false
core_changed: false
five_candidate_review: PASS_WITH_GATES
additional_candidates:
  chrome_devtools_mcp: conditional_high_value
  context7: optional_cli_or_skill_first
next_user_decision: choose_first_isolated_pilot
```

## 공식 출처

- shadcn MCP: https://ui.shadcn.com/docs/mcp
- Storybook MCP: https://github.com/storybookjs/mcp
- Raven MCP: https://github.com/rhinocap/raven-mcp
- Penpot MCP: https://github.com/penpot/penpot/tree/develop/mcp
- Penpot 보안 권고: https://github.com/penpot/penpot/security/advisories/GHSA-22qr-rp27-j9wm
- Blender MCP: https://www.blender.org/lab/mcp-server/
- Chrome DevTools MCP: https://developer.chrome.com/docs/devtools/agents/get-started
- Context7: https://github.com/upstash/context7
- Playwright MCP: https://github.com/microsoft/playwright-mcp
- Figma MCP: https://developers.figma.com/docs/figma-mcp-server/
