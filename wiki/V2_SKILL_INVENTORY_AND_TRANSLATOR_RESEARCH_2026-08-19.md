# AI OS V2 — 사용자 제작 Skill 목록과 초보자 번역 Skill 조사

- 작성일: 2026-08-19
- 조사 상태: 설치 없이 읽기 전용 확인

## 1. V2용으로 직접 제작한 Skill

### V2 Beginner Technical Translator

- 경로: `.agents/skills/v2-beginner-translator/`
- 역할: 초보자 표현을 개발 작업 설명으로 바꾸고 기술 결과를 쉬운 말로 다시 설명
- 주요 기능:
  - 사용자의 원래 표현을 먼저 보존
  - 바뀌는 부분·유지되는 부분·확인 방법 정리
  - 영어 기술 용어의 한글 발음 제공
  - 용어의 쉬운 뜻·현재 역할·사용 시점 제공
  - 번역을 승인이나 코드 변경 권한으로 사용하지 않음
- 상태: Repo-local Skill 구현 및 구조 검사 PASS. Codex 대화 전용이며 V2 제품 기능·Module·Core 연결 대상이 아닙니다.

### V2 Design Finish

- 경로: `.agents/skills/v2-design-finish/`
- 역할: 디자인 요청을 Brief부터 Visual Target·구현·마감 검사까지 진행
- 주요 기능:
  - 기존 Recipe·Block 우선 재사용
  - UI UX Pro 규칙과 품질 검사 활용
  - 반복 A/B/C 대신 구현 가능한 Visual Target 하나 제작
  - Reference·Prompt·도구·Design DNA 기록
  - 사용자 승인 전 구현 차단
  - Browser·Playwright 기반 실제 화면 검사
  - 디자인 PASS와 기술 PASS 분리
- 상태: Repo-local Skill과 실행 증거가 존재한다. V2 Core에 자동 연결된 Runtime 기능은 아니다.

### V2 Capability Lab

- 경로: `plugins/v2-capability-lab/skills/v2-capability-lab/`
- 역할: 외부 Skill·Plugin·CLI·오픈소스 후보를 비공개 프로젝트와 분리해 시험
- 주요 기능:
  - 공개 GitHub 후보 준비
  - 정적 감사
  - 가짜 Fixture 생성
  - Bubblewrap 격리 실행
  - 기본 Network 차단
  - 채택·보류·폐기 기록
  - 제거 가능한 Adapter 결정 기록
  - Design Intelligence 후보 Queue 생성
- 상태: Impeccable과 Taste 후보의 격리 시험 증거가 있다. V2 Core 자동 설치·자동 적용 기능은 아니다.

### 프로젝트 패키징

- 경로: `plugins/v2-capability-lab/skills/v2-project-packaging/`
- 역할: 이미 제작된 로컬 프로젝트 결과를 V2에 장착 가능한 Module 후보로 포장
- 주요 기능:
  - 민감 파일을 제외한 프로젝트 구조 읽기
  - 원본 상태 Hash와 실행 Entry 후보 기록
  - Manifest·기능 목록·중복 기능 초안 생성
  - 격리 Preview와 검증 상태 연결
  - 사용자 채택 전 Registry 등록 차단
  - 채택·보류·폐기 및 제거 가능성 유지
- 상태: Repo-local Skill 구조 검사와 병원 웹 폴더 대상 읽기 전용 초안 생성 시험 PASS. 자동 기능 판정이나 자동 Registry 등록은 구현하지 않으며 실제 작동 검증과 사용자 채택이 필요합니다.

### V2 Design Director

- 위치: `plugins/v2-capability-lab/skills/v2-design-director/`
- 쉬운 이름: `디자인 총괄`
- 기능: 동일한 V2 시험 화면을 기준으로 디자인 공급원 후보를 하나씩 탐색하고, 실제 사용 부분·총괄 수정·구현 가능성·사용자 판정을 기록합니다.
- 안전 경계: `OS`를 화면 스타일로 강제하지 않고 `조립형 제작 작업공간`으로 시험합니다. 비공개 프로젝트를 외부 후보에 전달하지 않으며 Core·Design Recipe를 직접 변경하지 않습니다.
- 현재 상태: `repo_local_verified_reference_trace` — 디자인 공급원 10개 비교와 사용자 판정을 기록했고, 채택 Trial→역할별 Section→Draft Design Recipe→HTML 출처 표시 자동 검사를 PASS했습니다. 디자인 품질 자동 판정·Core 자동 적용·제품 적용은 포함하지 않습니다.

## 2. 저장소에 추가된 보조 Skill

### Ponytail

- 경로: `.agents/skills/ponytail/`
- 역할: 과설계를 막고 기존 코드·표준 기능·최소 변경을 우선
- 주요 기능:
  - 필요 없는 기능은 만들지 않음
  - 기존 코드·표준 Library·Native 기능 우선
  - 새 Dependency 최소화
  - 증상이 아니라 공통 원인 수정
  - 최소한의 실행 검사 유지
- 구분: V2 전용 제작 Skill이라기보다 저장소에 추가된 개발 보조 Skill이다.

### Spec Kit Skill 묶음

- 경로: `.agents/skills/speckit-*`
- 역할: 요구사항·명세·계획·작업 목록·정합성 검토
- 구분: V2에서 새로 발명한 Skill이 아니라 외부 공식 Workflow Skill을 저장소에 연결한 것이다.

## 3. 외부에서 사용 중이거나 검증한 도구와 구분

다음은 사용자 제작 Skill로 표현하지 않는다.

- UI UX Pro Max: 디자인 규칙·접근성·금지 Pattern 제안과 검사
- Impeccable: 디자인 마감의 선택형 2차 의견
- Frontend App Builder: Frontend 구현 보조
- Browser 검증: 실제 화면·상호작용·Console 검사
- shadcn/ui: 구현용 Component·Block 공급원

## 4. 초보자 표현과 코딩 용어를 서로 번역하는 도구 조사

### 확인한 후보

#### Aider

- 공식 저장소: https://github.com/Aider-AI/aider
- 자연어로 코드 변경을 요청하고, Repository Map으로 코드 구조를 LLM에 전달한다.
- Ask Mode에서 코드를 변경하지 않고 질문할 수 있다.
- 판정: 강력한 Coding Agent지만 Codex·V2와 역할이 크게 겹친다. 번역 기능 하나를 위해 추가 설치하기에는 과하다.

#### OpenHands

- 공식 저장소: https://github.com/OpenHands/OpenHands
- 자연어 작업을 계획하고 코드·Shell·Browser 도구로 실제 Software 작업을 수행하는 Open Source Agent다.
- 판정: 전체 Coding Agent이므로 단순 용어 번역용으로는 과하다. 향후 V2 Agent Runtime 비교 후보는 될 수 있다.

#### Continue

- 공식 저장소: https://github.com/continuedev/continue
- 자연어 기반 Coding Agent·IDE·CLI 기능과 Source-controlled Check를 제공한다.
- 판정: Coding Agent와 CI Check가 중심이며 초보자 번역 전용 Skill이 아니다. 현재 V2에 추가하면 Codex·기존 검사와 중복된다.

#### ExplainShell 계열

- Shell 명령을 구성 요소별로 쉬운 설명으로 풀어주는 좁은 범위의 성공 사례다.
- 판정: `기술 명령 → 쉬운 설명`의 좋은 UX 사례지만 웹·디자인·React·V2 전체 용어를 다루지 못한다.

### 최종 판정

다음 두 방향을 동시에 안정적으로 제공하는 검증된 단일 오픈소스 Skill은 이번 조사에서 확인하지 못했다.

- 초보자 표현 → 저장소 근거가 포함된 개발 작업 설명
- 코드·오류·기술 용어 → 초보자가 선택할 수 있는 쉬운 설명

Aider·OpenHands·Continue를 설치하면 자연어 Coding은 가능하지만 이미 Codex와 V2가 담당하는 범위와 중복되고 설치·모델·외부 전송 부담이 커진다.

## 5. V2 권장안

새 대형 Coding Agent를 설치하지 않고 Repo-local `V2 Beginner Technical Translator` Skill을 만든다.

입력:

- 사용자 원문
- 현재 프로젝트 파일과 결정
- 현재 PM
- 허용된 변경 범위
- V2 용어집

사용자에게 보여줄 출력:

```text
내가 이해한 요청:
실제로 바뀌는 부분:
유지되는 부분:
개발자가 부르는 이름:
확인 방법:
```

반대 방향 출력:

```text
기술 결과:
쉬운 설명:
사용자에게 미치는 영향:
지금 할 일:
문제 시 되돌리는 방법:
```

안전 규칙:

- 번역만 하고 코드·Core·Git을 직접 수정하지 않음
- 저장소에서 확인하지 않은 기능을 존재한다고 말하지 않음
- 기술 용어를 사용자 승인으로 오해하지 않음
- 의미가 여러 개인 요청은 적용하지 않고 질문 하나만 함
- 사용자가 확인한 번역 결과만 다음 제작 단계 입력으로 전달

상태:

```yaml
dedicated_verified_external_skill: not_found
large_coding_agent_install: not_recommended
repo_local_translator_skill: recommended
implementation_status: implemented_repo_local
```
