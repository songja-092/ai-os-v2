# PM4 로컬 우선 Collector Pilot — 2026-08-21

## 목적

PM4 조사를 모든 요청마다 대량 실행하지 않고, V2가 이미 가진 성공 Recipe·Design DNA·Block·Skill·검증 문서를 먼저 검색합니다. 필요한 근거가 없을 때만 부족한 범위를 외부 조사 요청으로 만듭니다.

사용자 원문 `pm4 더 잘할수 있는 방법이 있는지 조사하고 시작해봐`는 로컬 우선 Collector 최소 Pilot과 공식 자료 조사 승인입니다. 새 패키지 설치, 자동 Skill 채택, 비공개 프로젝트 외부 전송, PM4 최종 PASS는 포함하지 않습니다.

## 검증된 흐름

```text
사용자 요청
→ V2 로컬 성공 자산 검색
→ 수집된 링크와 짧은 요약 표시
→ Analyzer가 확인 가능한 사실만 정리
→ 사용자에게 `이 정도면 충분한가요?` 인터뷰
→ 자료 더 찾기: 기존 결과를 보존하고 외부 수집 계속
→ 이 정도면 충분: V2 AI·총괄에게 전달
→ 조사 방향 수정: 구체적인 인터뷰 계속
→ 채택 후에만 기존 Capability Lab 격리 시험
```

Collector는 추천·설치·채택을 대신하지 않습니다. Analyzer도 자료의 충분 여부를 확정하지 않습니다. 수집 건수·출처·관련 용어·접근 상태처럼 확인 가능한 사실만 보여주며, 계속 수집할지는 사용자가 결정합니다.

## 구현

- `plugins/v2-capability-lab/scripts/pm4_collector.py`: 허용된 로컬 폴더 검색, Source URL 정규화·중복 제거, 판단 없는 수집 결과 생성
- `plugins/v2-capability-lab/scripts/pm4_analyzer.py`: 링크·짧은 요약·사실표 생성 후 사용자 확인 질문 생성
- `tools/verify-pm4-collector`: 수집·분석·사용자 결정 경계를 Network 없이 검증
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

`tools/verify-pm4-collector`: `9/9 PASS`

1. 인터뷰 확인 후에만 수집
2. Collector는 수집만 수행
3. Analyzer는 사실 요약만 담당하고 충분성 판정 금지
4. 모든 결과에 Link와 짧은 요약 제공
5. 사용자가 계속 수집·종료·방향 수정을 결정
6. 외부 Network 자동 실행 금지
7. 비공개 Project 외부 전송 금지
8. Analyzer 추천·자동 채택 금지
9. 설치·활성화·Core 변경 없음

브라우저 검증 URL은 `http://127.0.0.1:8211/pm4-review.html`입니다. 두 분기 표시와 가로 넘침 없음은 PASS했고, 앱 Console 오류는 없습니다. Electron 개발환경 공통 CSP 경고는 페이지 코드 오류가 아닙니다.

## 정확한 상태

```yaml
pm4_status: started
local_first_collector_pilot: pass
interview_gate: implemented_for_pilot
collector_analyzer_role_split: pass
real_research_request: not_yet_verified
user_adopt_hold_discard: not_yet_verified
capability_lab_handoff: not_yet_verified_in_pm4
pm4_final_pass: false
new_package_installation: false
core_changed: false
```

## 다음 Gate

실제 PM4 조사 요청 한 건으로 Link·짧은 요약 표시, 사용자 `자료 더 찾기·이 정도면 충분·조사 방향 수정`, 실제 출처·접근 상태, 채택 후에만 Capability Lab으로 넘기는지를 확인합니다.

## 자동화와 Skill 경계

자동화할 부분:

- Interview Assistant: 이미 답한 내용은 생략하고 결과가 달라지는 질문을 한 개씩 계속 제시
- Collector Adapter: 각 공급원의 제목·원본 URL·작성자·날짜·인기도·자료 종류를 공통 형식으로 변환
- Deduplicator: Canonical URL과 Source ID로 중복 묶기
- Analyzer: 접근·License·재현 조건·근거 수준을 사실표로 작성
- Evidence Writer: 사용자 결정과 근거를 Wiki·Artifact에 기록
- Capability Lab Handoff: 사용자가 채택한 공개 후보만 격리 시험으로 전달

자동화하지 않을 부분:

- 디자인 총괄의 방향 결정
- V2 AI의 사용자 설명을 승인으로 간주하는 일
- 사용자 대신 채택·보류·폐기
- 승인 없는 설치·제품 적용

기본 외부 공급원 후보는 GitHub·Reddit·YouTube·Threads·Instagram입니다. 현재 실제 Adapter가 확인된 것은 공개 GitHub Metadata 조회뿐입니다. Reddit·YouTube·Threads·Instagram은 아직 `planned_not_connected`입니다. Threads·Instagram은 사용자가 Aside Browser에서 최초 로그인한 사용자 세션을 유효한 동안 읽기 전용으로 재사용할 수 있게 설계하되, 자격증명을 V2에 저장하거나 로그인·접근 차단을 우회하지 않습니다. 만료·차단 시 `access_unavailable`로 표시합니다.

## 일일 탐색 브리핑 자동화

2026-08-21 Codex App Automation `v2`를 `V2 일일 탐색 브리핑` 이름으로 활성화했습니다.

- 실행: 매일 오전 7시, 로컬
- 공급원: Reddit·GitHub·YouTube·Threads·Instagram
- 분류: 참고자료 / V2 적용·격리 시험 후보 / 수익 아이템
- 출력: 원본 Web Link + 초보자용 1~2문장 요약
- 금지: 충분성 단정, 자동 설치·채택, Core 변경, Commit·Push, 로그인·접근 차단 우회
- 종료 질문: `자료 더 찾기 / 이 정도면 충분 / 조사 방향 수정`

Automation 생성 자체는 각 공급원 Adapter의 실제 접근 성공을 증명하지 않습니다. Threads·Instagram Browser Session이 없거나 만료되면 `접근 불가`로 보고해야 합니다.

### 뉴스·브리핑 Module Pilot

`pm4-modules/daily-discovery-briefing`을 PM2 Module 계약을 재사용한 제거 가능한 PM4 Module Draft로 만들었습니다. Codex App Automation `v2`는 사용자가 개인적으로 쓰는 오전 7시 고정 브리핑이며 이 공용 Module과 분리합니다.

- 원본 Web Link와 짧은 요약 표시
- GitHub·Reddit·YouTube·Threads·Instagram 접근 상태 표시
- 조사 주제를 사용자가 입력
- 실행 시간을 `HH:MM`으로 선택
- GitHub·Reddit·YouTube·Threads·Instagram 중 조사 플랫폼을 사용자가 선택
- `briefing.config.update` Action으로 주제·시간·플랫폼 설정을 Core에 승인 요청
- Module이 Automation 설정이나 Core 상태를 직접 변경하지 않음

초기 고정 시간 Module의 Manifest·Fixture 계약과 시간 Action은 검증했지만 사용자가 범용 설정형으로 범위를 수정했습니다. 수정된 Module의 실제 Core 연결·Automation 생성·수집·사용성은 사용자 요청에 따라 PM 마지막에 검증합니다. 현재 Lifecycle은 `candidate`, 기능 상태는 `draft | not_yet_verified`입니다. 개인용 Automation `v2`는 오전 `07:00`으로 별도 유지합니다.
