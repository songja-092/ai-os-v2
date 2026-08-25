# OR0 Preflight Checklist

이 문서는 PM1~PM6 착수 전 운영 준비를 확인하는 체크리스트입니다. 기술 Gate와 사용자 확인이 통과했으며 PM1 디자인 채택 방식 테스트를 시작할 수 있습니다.

## 실행 원칙

- 원격 `main` 기준은 `83ab8deaa504df6c1baf95a3a49ab1df05345653`, OR0 Worktree 기준은 `a7bb70e297147b011bacd2fa5ea038313a2fd124`, 로컬 최신 설계 기준은 `822a218`입니다. 세 기준을 구분해 확인합니다.
- 사용자 Dirty 작업공간 `/home/user/바탕화면/ai_os_v2`를 수정하지 않습니다.
- OR0 작업은 `/home/user/바탕화면/ai_os_v2_or0`에서만 수행합니다.
- 제품 `/home/user/바탕화면/test_project`를 수정하지 않습니다.
- Preflight는 설치·프로세스 종료·Preview 시작·백업 업로드를 수행하지 않습니다.
- 하나라도 필수 항목이 FAIL이면 PM1~PM6은 계속 차단합니다.

## OR0-A — Worktree

- [x] OR0 Worktree가 공식 Commit에서 생성됨
- [x] OR0 전용 Branch를 사용함
- [x] 허용 경로 밖의 변경이 없음
- [x] 검사기와 같은 직렬화 방식으로 원본 Dirty 보존 비교용 Snapshot `592817a3624832c807944a3b02860deb881c31db607acb925915b2ba359ed920` 기록. 이 값 이전 상태는 소급 증명하지 않음

## OR0-B — 환경 문서

- [x] `environment/runtime-baseline.yml` 존재
- [x] `environment/operation-policy.yml` 존재
- [x] `environment/preflight-checklist.md` 존재
- [x] 사용자가 PM 시작을 위한 환경 구성을 승인함

## OR0-C — 읽기 전용 Preflight

- [x] OS·Python·Node·npm·Git·Chrome·Codex·Spec Kit Version 확인
- [x] Antigravity 파일 경로·Version Metadata·Sandbox 권한 확인
- [x] 로컬 기획 HEAD와 원격 `origin/main`을 서로 다른 승인 기준으로 확인
- [x] `origin/main` 조회는 승인된 읽기 요청 1회와 15초 Timeout만 사용
- [x] 사용자 Dirty 변경 목록과 보존 Hash 확인
- [x] 제품 저장소 HEAD와 Clean 상태 확인
- [x] 병원·PDF `package.json`과 Lockfile 확인
- [x] Port `5173`, `5174`, `8200` 사용 여부 확인
- [x] UI UX Pro 경로와 검색 Script 확인
- [x] 필수 Skill 경로 확인
- [~] 외부 백업·Restore는 사용자 결정으로 후속 연기
- [x] `57 PASS / 2 WARN / 0 FAIL`, 종료 코드 `0` 출력

## OR0-D — Antigravity 재현

- [x] 현재 실행 파일 경로와 Version 확인
- [x] 변경 전 격리본 `chrome-sandbox` 소유권 `user:user`·Mode `0755` 기록
- [x] 격리본 한 파일의 시스템 권한 변경을 별도 승인받음
- [x] 대화형 `sudo` 인증으로 공백 없는 격리본을 `root:root`, Mode `4755`로 설정
- [x] 임시 사용자 데이터·확장 폴더와 `--no-sandbox` 없는 표준 명령으로 IDE 실행
- [x] SUID Sandbox 사용, 치명 오류 없음, 격리 프로세스 종료와 임시 데이터 정리 기록

## OR0-E — Preview와 백업

- [x] 병원 웹을 독립 Worktree에서 `5173 --strictPort`로 실행
- [x] 병원 제목·의료진·예약 DOM 의미 확인
- [x] 병원 웹 메뉴 클릭과 Console 치명 오류 없음 — 인앱 브라우저 Timeout 후 기존 번들 Playwright로 대체 검증
- [x] PDF 제품을 독립 Worktree에서 `5174 --strictPort`로 실행
- [x] PDF 열기·도면·스탬프 DOM 의미 확인
- [x] PDF 문자 프리셋 클릭과 Console 치명 오류 없음 — 기존 번들 Playwright로 대체 검증
- [x] 실행 경로와 프로세스가 프로젝트별 독립 Worktree·Port로 분리됨
- [x] PDF 종료 후 병원 웹이 계속 응답하여 장애 격리를 확인함
- [x] 종료 후 해당 Preview 프로세스만 정상 정리되고 `5173`, `5174`가 해제됨
- [~] 외부 백업 위치 선택을 사용자가 후속 작업으로 연기함
- [~] 제품·V2_UI·생성 이미지·Reference·비Git Run·인수인계서 백업은 Production 배포 또는 대체 불가능한 Artifact 생성 전 필수
- [~] Restore 표본 검증은 같은 시점까지 잔여 위험으로 기록

## OR0-F — 새 세션 재현

- [x] 새 임시 Codex 프로세스에서 `tools/or0-preflight` 1회 실행
- [x] 환경 문서와 실제 결과 일치
- [x] 기존 Preview 수동 검증 증거 재조회
- [~] 외부 백업·Restore 연기 상태 재조회
- [x] 사용자 결과 PASS — 외부 백업·Restore만 후속 연기하고 PM1 진행 승인

## PASS 조건

다음 항목이 모두 충족돼야 합니다.

```yaml
or0_pass:
  clean_or0_scope: true
  runtime_inventory_matches: true
  git_and_paths_verified: true
  ports_available_before_preview: true
  product_preview_readiness_verified: true
  antigravity_new_session_verified: true
  external_backup_verified_or_user_deferred_for_pm1_test: true
  new_codex_session_preflight_passed: true
  user_result: pass
```

현재 상태:

```yaml
operational_readiness: pass_with_user_deferred_backup
pm_start_allowed: true
preflight: 57_pass_2_warn_0_fail
active_stage: PM1_design_adoption_method_test
```
