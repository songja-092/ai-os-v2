# V2 Capability Lab 자동화 Pilot 보고서

작성일: 2026-08-18
상태: Repo-local Pilot 구현·격리 검증, 사용자 채택 대기

## 목적

좋은 Skill·Plugin·오픈소스를 빠르게 시험하되 비공개 프로젝트, Git 기록, `.env`, Token,
Cookie와 고객 자료가 외부 후보에 노출되지 않도록 합니다.

```text
공개 후보 발견
→ Repo-local Lab에 Clone
→ 정적 위험 신호와 License 기록
→ 가짜 Fixture 생성
→ 원본 프로젝트가 보이지 않는 Sandbox 실행
→ 결과 표시
→ 사용자 승인 시 Registry 채택
→ 거절 시 복구 가능한 discarded 영역으로 이동
```

## 구현 위치

- Plugin: `plugins/v2-capability-lab`
- Skill: `plugins/v2-capability-lab/skills/v2-capability-lab`
- 실행기: `plugins/v2-capability-lab/scripts/capability_lab.py`
- 후보 Registry: `plugins/v2-capability-lab/registry/capabilities.json`
- 격리 증거: `pm1-artifacts/capability-lab`

Codex 전역이나 Marketplace에는 설치하지 않았습니다. V2 Runtime Plugin Marketplace도
만들지 않았습니다. 현재 결과는 PM4 Capability 조사·격리 검증 계약을 앞당겨 시험한
Repo-local 개발 도구입니다.

## 개인정보·프로젝트 보호 방식

- 입력은 Credential이 없는 공개 GitHub 저장소 URL만 허용합니다.
- 시험 대상은 V2가 생성한 가짜 HTML Fixture입니다.
- Bubblewrap에는 후보 폴더와 시스템 Runtime만 Bind합니다.
- `/home/user/바탕화면/ai_os_v2_pm1`과 제품 저장소를 Bind하지 않습니다.
- `HOME=/home/candidate`와 빈 환경을 사용하고 Token·Key·Cookie를 전달하지 않습니다.
- 기본 시험은 Network를 차단합니다.
- 공개 Network 시험은 사용자 승인 Flag가 있어야 합니다.
- 전역 Package·Skill 설치와 Candidate의 Core Write를 허용하지 않습니다.

## 실제 Pilot

후보: `pbakaus/impeccable`
Commit: `f88b2837a7d7c3182e46307bbbb091a1ed547571`

정적 감사:

- Text 파일 3,019개 검사
- 환경·HOME 접근, 프로세스 실행, 삭제, 외부 통신, 설치 Lifecycle 가능성을 위험 신호로 기록
- 위험 신호는 악성 판정이 아니라 실행 전 검토 대상입니다.

격리 시험:

- 가짜 HTML에서 Impeccable Detector 실행: 종료코드 0
- 원본 V2 저장소 경로 표시 여부: `false`
- 전달된 Credential 이름: `[]`
- Sandbox HOME: `/home/candidate`
- Network 연결 결과: 차단
- 승인 없는 `adopt`: 종료코드 2로 거부
- 승인 없는 `discard`: 종료코드 2로 거부
- `http://localhost/private` 후보: 종료코드 2로 거부

## “완전 로컬” 대신 적용한 기준

공개 URL과 공개 GitHub는 외부 Network를 사용할 수 있습니다. 하지만 비공개 프로젝트와
Secret은 후보에게 보이지 않습니다. 따라서 디자인 Reference와 공개 도구 활용 범위는
넓히면서 프로젝트 유출 위험은 파일시스템 격리와 환경 초기화로 줄입니다.

Network 접근이 허용된 후보는 후보 Source와 가짜 Fixture를 외부로 전송할 가능성이
있습니다. 두 자료는 공개 또는 생성 자료이므로 허용할 수 있지만, 해당 도구의 서비스
약관·License·출력 품질은 별도 검토합니다.

## 한계

- 정적 문자열 검사는 악성 동작을 완전히 판별하지 못합니다.
- Kernel·Bubblewrap 취약점까지 무위험이라고 보증하지 않습니다.
- 후보 품질과 V2 적합성은 실제 결과와 사용자 판정이 필요합니다.
- 실제 프로젝트 적용은 채택 뒤 별도 Adapter와 Scope Lock이 필요합니다.
- Package Install Script 자동 실행은 아직 의도적으로 구현하지 않았습니다.

## 판정

```yaml
automation_structure: implemented
plugin_validation: PASS
skill_validation: PASS
private_project_visibility_test: PASS
credential_isolation_test: PASS
offline_network_isolation_test: PASS
public_network_trial: supported_but_requires_user_approval
automatic_global_install: prohibited
impeccable_trial: PASS
impeccable_adoption: awaiting_user_selection
core_or_product_change: false
commit_or_push: false
```
