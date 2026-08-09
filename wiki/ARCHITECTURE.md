# Architecture

## 현재 기반

```text
Obsidian/Wiki <-> GitHub main -> Archify
사람의 편집       공식 원본       commit 기반 시각화
```

GitHub `main`이 공식 원본입니다. Obsidian은 같은 Markdown을 읽고 편집하는 인터페이스이며 Archify는 원본이 아니라 특정 commit에서 만들어지는 파생 결과입니다.

## V2 작업 운영 구조

```text
사용자
  |
  | 아이디어와 원하는 결과
  v
웹 ChatGPT
  | 조사 결과와 정리된 요구
  v
Codex + Spec Kit
  | 실제 저장소 조사
  | Specify / Clarify
  v
사용자 요구사항 승인
  |
  v
Target Environment 결정
  |
  v
Design 필요 여부
  | UI/UX가 필요한 경우에만
  v
UI UX Pro Max
  | 디자인 시스템 제안
  v
사용자 디자인 승인
  |
  v
Codex
  | Plan / Tasks
  | 기술 검토와 Antigravity 작업 지시서
  v
사용자 승인
  |
  v
Antigravity (수동 구현)
  | 파일 변경과 명령별 사용자 권한 확인
  | Build / Lint / Test 결과
  v
Codex 독립 검증
  | 실제 파일·명령·브라우저 증거
  v
사용자 실물 확인과 최종 승인
  |
  v
Git Commit / Push
  |
  +--> Wiki 현재 상태와 결정
  +--> Archify 구조 시각화
  `--> Rollback 기준점
```

## 사용자에게 보이는 흐름

기술 단계를 그대로 노출하지 않고 다음 다섯 단계로 표현합니다.

1. 원하는 결과 말하기
2. 조사 결과와 선택지 보기
3. 시안과 작업 계획 승인하기
4. 구현 결과를 실제 화면에서 사용해 보기
5. 저장하거나 이전 상태로 되돌리기

## 제작 파이프라인

1. **Intake**: 자연어 요구와 참고 URL을 받습니다.
2. **Research**: 필요한 근거를 공식 문서, GitHub, Web과 실사용 자료에서 조사하고 출처를 남깁니다.
3. **Specify/Clarify**: Spec Kit으로 요구사항, 제외 범위와 완료 조건을 정리하고 사용자가 승인합니다.
4. **Target Environment**: Web, Android, iOS, Desktop, CLI, API, Server 또는 기타 대상 환경을 확정합니다.
5. **Conditional Design**: UI/UX가 필요한 경우에만 디자인 도구를 선택합니다. 현재 기본 파일럿은 UI UX Pro Max이며 사용자가 결과를 승인합니다.
6. **Plan/Tasks**: 승인된 요구사항과 디자인을 실제 구현 계획과 작은 작업으로 변환합니다.
7. **Reuse Decision**: 기존 제품·OSS·Skill·MCP·서비스를 비교 검증합니다.
8. **Handoff**: Codex가 변경 파일, 허용 명령, 금지 범위, 검증 방법과 복구점을 포함한 구현 지시서를 만듭니다.
9. **Implement**: Antigravity가 사용자 승인 아래 한 Task씩 구현합니다.
10. **Verify**: Target Environment에 맞는 실제 실행 검증을 수행합니다. 웹이면 Playwright, CLI면 명령/출력, API면 요청/응답 검증처럼 도구를 조건부로 선택합니다.
11. **Accept**: 사용자가 실제 결과를 확인하고 승인하거나 수정을 요청합니다.
12. **Save**: 승인된 한 변경을 Commit/Push하고 Wiki와 시각화가 해당 SHA를 가리키게 합니다.
13. **Recover**: 이전 Commit을 확인한 뒤 결과 Commit으로 복구하고 재실행합니다.

## 증거 규칙

- 아이디어나 화면 예시는 실제 구현과 분리하여 표시합니다.
- 실제 파일 또는 설정이 있어야 `🔨 구현됨`입니다.
- 해당 기능을 직접 실행한 증거가 있어야 `✅ 검증됨`입니다.
- 구현 Agent의 보고만으로 PASS 처리하지 않습니다.
- 조사 결과에는 원문 URL, 확인 날짜와 채택/탈락 이유를 남깁니다.

## 현재 부품 상태

| 역할 | 부품 | 상태 |
|---|---|---|
| 공식 기억과 버전 | GitHub + Wiki | ✅ 연결 검증 기록 존재 |
| 사람용 편집 | Obsidian | ✅ 연결 검증 기록 존재 |
| 구조 시각화 | Archify | 연결 검증 증거 재확인 필요 |
| 자연어 명세 | Spec Kit | 🔨 시험 브랜치 적용, 실제 기능 왕복 미검증 |
| 디자인 시스템 제안 | UI UX Pro Max | 📝 승인됨, 미설치 |
| 설계·독립 검증 | Codex | 사용 중 |
| 실제 구현 | Antigravity | 수동 운영 방식 확정 |
| 환경별 검증 | 프로젝트별 도구 | 💡 Target Environment에 따라 선택 |
| 자동 오케스트레이션 | 없음 | 현재 필요하지 않음 |

Kernel, Planner, Collector, Multi-Agent와 V2 전용 UI는 현재 아키텍처의 필수 구성요소가 아닙니다. 반복 작업에서 실제 필요가 증명되기 전에는 만들지 않습니다.
