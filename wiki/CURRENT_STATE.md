# Current State

현재 단계는 V2 개발 기반과 최초 파일럿 작업을 확정하는 단계입니다. Kernel, Planner, Collector, Multi-Agent 및 V2 UI는 구현하지 않습니다.

이전 지식 연결 시험 기록은 존재하지만, 파일럿 시작 기준인 네 연결의 Repository, Branch, Commit SHA와 실제 증거를 한 보고서에서 최종 확인해야 합니다.

## Spec Kit 도입 상태

- 🔨 구현됨: `codex/spec-kit-pilot` 브랜치에 GitHub Spec Kit `v0.16.1` 기반을 설치했습니다.
- 🔨 구현됨: 기존 V2 원칙을 `.specify/memory/constitution.md`에 연결했습니다.
- ✅ 검증됨: Spec Kit Codex 통합의 관리 파일 상태 검사가 오류와 누락 없이 통과했습니다.
- 확인 필요: 완전히 새로운 Codex 세션에서 프로젝트 Skill 자동 인식 확인.
- 미실행: 실제 기능의 Spec → Plan → Tasks → Implement 왕복 시험.

## 공식 기억 동기화 상태

- 확인 필요: 현재 로컬 Wiki 수정본을 사용자 승인 후 Commit/Push하여 GitHub `main`과 일치시켜야 합니다.
- 확인 필요: 파일럿 시작 시 ChatGPT, Codex, Antigravity가 같은 `Base Memory Commit`을 읽었다는 증거를 남겨야 합니다.

## 디자인 파일럿 상태

- 📝 승인됨: UI UX Pro Max를 디자인 단계 핵심 파일럿 부품으로 채택했습니다.
- 미설치: 별도 파일럿 브랜치와 도입 전 복구점을 확인한 뒤 고정 버전으로 시험합니다.
- 미실행: 디자인 시스템 제안, 사용자 디자인 선택과 Target Environment 실제 결과 검증.

## Ponytail 도입 상태

- 🔨 구현됨: `codex/ponytail-pilot` 브랜치에 공식 Ponytail Skill을 프로젝트 단위로 설치했습니다.
- 설치 기준: `DietrichGebert/ponytail` Commit `2ed6c52c9d7e5e56942508591085fd45dea277d3`.
- 적용 수준: 첫 파일럿은 `lite`로 사용합니다.
- 확인 필요: 새로운 Codex 작업에서 프로젝트 Skill 자동 인식과 실제 코드 변경 품질 검증.
- 제작자 자체 벤치마크 수치는 V2에서 독립 검증된 사실로 취급하지 않습니다.

## 현재 확정된 운영 방식

- 웹 ChatGPT는 아이디어 대화와 외부 자료 조사·정리를 담당합니다.
- Codex는 실제 저장소를 기준으로 구조 조사, 설계, 작업 지시서 작성과 독립 검증을 담당합니다.
- Antigravity는 사용자가 전달한 승인된 지시서에 따라 수동으로 구현합니다. 파일 수정, 명령 실행과 보안 권한은 사용자 확인을 거칩니다.
- 구현 Agent가 보고한 완료를 그대로 공식 사실로 저장하지 않습니다. 실제 결과와 검증 증거를 확인한 뒤 승인된 변경만 Git에 저장합니다.
- 기존 `ai_os`는 참고 자료이며 V2 코드 재사용 원본이 아닙니다.

## 다음 검증 대상

- 작은 실제 프로젝트 한 개에서 `요청 → Spec → 구현 지시 → Antigravity 구현 → 실행/브라우저 검증 → 승인 → Commit → Rollback` 왕복 시험
- 첫 실제 코딩 Task에서 Ponytail `lite`가 불필요한 파일·코드·의존성을 줄이면서 완료 조건과 안전 기준을 유지하는지 확인
- Spec Kit 파일럿 결과를 근거로 `main` 채택 또는 롤백 결정
