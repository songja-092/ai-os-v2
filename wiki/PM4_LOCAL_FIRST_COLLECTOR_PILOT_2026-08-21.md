# PM4 로컬 우선 Collector Pilot — 2026-08-21

## 목적

PM4 조사를 모든 요청마다 대량 실행하지 않고, V2가 이미 가진 성공 Recipe·Design DNA·Block·Skill·검증 문서를 먼저 검색합니다. 필요한 근거가 없을 때만 부족한 범위를 외부 조사 요청으로 만듭니다.

사용자 원문 `pm4 더 잘할수 있는 방법이 있는지 조사하고 시작해봐`는 로컬 우선 Collector 최소 Pilot과 공식 자료 조사 승인입니다. 새 패키지 설치, 자동 Skill 채택, 비공개 프로젝트 외부 전송, PM4 최종 PASS는 포함하지 않습니다.

## 검증된 흐름

```text
사용자 요청
→ V2 로컬 성공 자산 검색
→ 필요한 증거 종류가 충분한지 확인
→ 충분: 기존 자산 재사용
→ 부족: 부족 항목만 외부 조사 요청 생성
→ 출처·접근·라이선스·구현 가능성 기록
→ 사용자 채택·보류·폐기
→ 채택 후에만 기존 Capability Lab 격리 시험
```

Collector는 추천·설치·채택을 대신하지 않습니다. 흔한 단어가 여러 문서에서 발견됐다는 이유만으로 충분하다고 판정하지 않고, 요청이 지정한 필수 용어·증거 조건까지 충족해야 합니다.

## 구현

- `plugins/v2-capability-lab/scripts/pm4_collector.py`: 허용된 로컬 폴더 검색, 충분·부분·부족 판정, 제한 외부 Query 초안, Source URL 정규화·중복 제거
- `tools/verify-pm4-collector`: 로컬 충분 사례와 외부 조사 필요 사례를 Network 없이 검증
- `pm4-review.html`: 초보자가 두 분기를 눈으로 비교하는 읽기 전용 Pilot 화면

## 외부 도구 역할 판정

| 도구 | PM4 역할 | 기본 실행 |
|---|---|---|
| GitHub REST API | 공개 Repository의 활동·보관 상태·License 확인 | 부족한 후보 조사 시만 |
| OSV | 선택된 Package Version·Commit의 알려진 취약점 확인 | 후보 선택 후만 |
| 기존 Capability Lab | 공개 후보를 격리 설치·시험하고 제거 가능성 확인 | 사용자 채택 후만 |
| 대형 Crawler·Vector DB | 이번 Pilot에 필요 없음 | 금지 |

공식 근거:

- GitHub Repository API: <https://docs.github.com/en/rest/repos/repos>
- OSV API: <https://google.github.io/osv.dev/api/>

## 검증 결과

`tools/verify-pm4-collector`: `7/7 PASS`

1. 로컬 자산 우선 검색
2. 충분한 로컬 사례에서 외부 조사 생략
3. 부족 사례에서 제한 조사 요청 생성
4. 외부 Network 자동 실행 금지
5. 비공개 Project 외부 전송 금지
6. 사용자 없이 자동 채택 금지
7. 설치·활성화·Core 변경 없음

브라우저 검증 URL은 `http://127.0.0.1:8211/pm4-review.html`입니다. 두 분기 표시와 가로 넘침 없음은 PASS했고, 앱 Console 오류는 없습니다. Electron 개발환경 공통 CSP 경고는 페이지 코드 오류가 아닙니다.

## 정확한 상태

```yaml
pm4_status: started
local_first_collector_pilot: pass
real_research_request: not_yet_verified
user_adopt_hold_discard: not_yet_verified
capability_lab_handoff: not_yet_verified_in_pm4
pm4_final_pass: false
new_package_installation: false
core_changed: false
```

## 다음 Gate

실제 PM4 조사 요청 한 건으로 올바른 분기, 실제 출처·License·접근 상태, 사용자 `채택·보류·폐기`, 채택 후에만 Capability Lab으로 넘기는지를 확인합니다.
