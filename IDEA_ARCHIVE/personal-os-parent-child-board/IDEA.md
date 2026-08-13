---
id: personal-os-parent-child-board
title: 직업별 Personal OS와 부모·자식 보드판
status: deferred
classification: isolated_long_term_idea
adopted_by_v2: false
implementation_approved: false
auto_resume: false
created: 2026-08-13
resume_trigger: 사용자가 이 아이디어를 지정하고 열어서 진행하라고 명시적으로 요청할 때
---

# 직업별 Personal OS와 부모·자식 보드판

> [!warning] V2와 격리된 보류 아이디어
> 이 문서는 AI OS V2의 현재 기능, 공식 로드맵, 마일스톤 또는 구현 지시가 아니다. `wiki/`, `runs/`, `state/`, V2 Core와 자동 연결하지 않으며, 사용자의 명시적 재개 요청 전에는 추가 조사·설계·구현을 시작하지 않는다.

## 한 줄 정의

공통 보드판에 직업·고객별로 필요한 기능만 추가하고, 부모 보드에서 검증한 버전을 고객의 자식 보드에 승인형으로 전달하는 Personal OS 제작·배포 구조 아이디어다.

## 판정

- 현재 기술로 소규모 파일럿 구축은 실현 가능하다.
- 검증된 구성 요소는 기능 패키지, Version 고정, 고객 데이터 격리, 승인형 Update, Snapshot·복구다.
- 범용 Personal OS 사업 전체가 검증된 것은 아니다.
- 자동 Update, Marketplace, 무제한 AI 코드 설치는 초기 범위에서 제외한다.

## 최소 파일럿 후보

```text
부모 보드판 1개
+ 자식 보드판 1개
+ 독립 기능 1개
+ 설치
+ 비활성화 또는 제거
+ 이전 상태 복구
```

## 예상 구조

```text
부모 보드
→ 기능 요청 수집
→ 격리 제작·Preview·검증
→ 불변 Version 발행
→ 변경사항 표시
→ 고객 승인
→ 자식 보드에 설치
→ Health Check
→ 실패 시 이전 Version 복구
```

## 검증 사례에서 가져올 부분

| 필요 기능 | 참고 모델 | 후보 원칙 |
|---|---|---|
| 작은 기능 패키지 | Obsidian Plugin | `manifest.json`, SemVer, Release |
| 설치·비활성화·복구 | Home Assistant | 설치 전 Backup, 장애 격리 |
| 직업별 기능 조합 | Odoo Module | Core + 선택 Module + 의존성 |
| Core 호환성 검사 | WordPress Plugin | 최소 Version·의존성 검사 |
| 고객 데이터 분리 | Multi-tenant + PostgreSQL RLS | `tenant_id`, 권한, 기본 거부 |

## 기능 패키지 최소 정보 후보

- 고정 `id`
- 이름과 설명
- 기능 Version
- 호환 가능한 Core Version 범위
- 필요 권한
- 실행 진입점
- 데이터 Schema Version
- 설치·비활성화·제거 절차
- Checksum
- Release notes
- Snapshot 및 Rollback 조건

## 데이터 안전 원칙 후보

- 기능 코드에 고객 데이터를 포함하지 않는다.
- 고객별 DB 또는 `tenant_id`/`workspace_id` 범위를 적용한다.
- 파일 저장소도 고객별로 분리한다.
- 기능이 DB 전체를 직접 읽지 않고 권한을 검사하는 Core API를 통하게 한다.
- 초기 파일럿은 기능 전용 DB·JSON·SQLite를 사용하여 Core Schema 변경을 피한다.
- 코드 제거와 고객 데이터 삭제를 별도 작업으로 분리한다.

## 배포 단위 후보

```text
개발: 기능 폴더
초기 설치: manifest가 포함된 ZIP
장기 배포: 불변 GitHub Release + SHA-256
```

## 금지·보류 범위

- 기능 Marketplace
- 결제
- 자동 Update
- 다중 고객 관리 시스템
- 복잡한 Plugin SDK
- AI 기능 추천
- 모든 직업용 Template
- AI가 생성한 코드의 무승인 자동 설치

## 재개 조건

다음 모두를 만족할 때만 다시 연다.

1. 사용자가 `직업별 Personal OS`, `부모·자식 보드판` 또는 이 문서의 `id` 중 하나를 지정한다.
2. 사용자가 조사 재개, 파일럿 설계 또는 구현을 명시적으로 요청한다.
3. 현재 V2 작업과 분리된 새 범위·Branch·복구점을 먼저 확정한다.

## 조사 근거

- [Obsidian — Submit your plugin](https://docs.obsidian.md/Plugins/Releasing/Submit%20your%20plugin)
- [Home Assistant — Backups and restore](https://www.home-assistant.io/common-tasks/general/)
- [Home Assistant — Integration manifest](https://developers.home-assistant.io/docs/creating_integration_manifest/)
- [WordPress — Plugin header requirements](https://developer.wordpress.org/plugins/plugin-basics/header-requirements/)
- [Odoo — Module manifests](https://www.odoo.com/documentation/14.0/developer/reference/module.html)
- [PostgreSQL — Row security policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- [GitHub — Artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)

## 원본 자료

- 최초 아이디어 전달서: `/home/user/.codex/attachments/4c508dbe-59d7-41ee-b38e-15d576a4dbfd/pasted-text.txt`
- 조사일: 2026-08-13
