# V2 Story M1~M8 실행 기준 — 2026-08-30

상태: `design_complete / implementation_not_started / revenue_not_proven`

이 문서는 `V2 Story Pilot과 Core 완성 계약`을 실제 마일스톤으로 나눈 실행 기준입니다. M1~M8은
새 PM 번호가 아닙니다. 마일스톤은 제품·사업이 어디까지 도달했는지를 표시하고, 기존 PM0~PM6은
각 마일스톤에서 조사·디자인·조립·구현·의도·품질을 검사하는 반복 절차로 사용합니다.

## 1. 프로젝트 한 문장

고객이 가진 PPT·PDF·사진·텍스트를 공통 `Story Profile·Scene Contract`로 변환하고, 같은 원본에서
개선 PPT·카드·웹 이야기·짧은 모션·MP4·PDF·책으로 확장하는 V2 기반 제작 플랫폼입니다.

## 2. 공통 원본과 PPT의 관계

PPT는 입력이자 출력이며 내부 원본이 아닙니다. 내부 원본은 매체와 독립적인 Story 구조입니다.

```text
PPT · PDF · 사진+텍스트 · 문서
              ↓ Import Adapter
       Story Profile + Scene Contract
              ↓ Export Adapter
PPT · 카드 · 웹 이야기 · 모션 · MP4 · PDF · 책
```

### Story Profile 최소 필드

- 소유자·대상 독자·목적·핵심 메시지·분위기
- 등장인물 또는 주제·사실 출처·금지 표현
- 공개 범위·자료 권리·외부 Provider 전송 동의
- 원하는 결과 형식·예산·기한·CTA

### Scene Contract 최소 필드

- Scene ID·순서·목적·제목·본문
- 연결 Asset와 Crop/대체 규칙
- Layout 의도·안전영역·모바일 우선순위
- 예상 시간·Motion·Audio Slot
- 사실 검증 상태·편집 소유 Surface
- 출력별 Mapping: slide/card/web/shot/page

### PPT 양방향 모드

1. `extract_content`: 디자인을 버리고 내용만 구조화
2. `preserve_and_polish`: 순서와 의미를 유지하며 가독성·디자인 개선
3. `restructure`: 목적과 독자에 맞게 Scene을 다시 구성
4. `export_storyboard`: Scene을 발표·검토용 PPT로 출력

SmartArt·차트·수식·동영상·발표자 노트·누락 글꼴은 별도 Capability로 판정합니다. 지원하지 못하는
요소는 조용히 손실하지 않고 원본 보존과 경고 Artifact를 남깁니다.

## 3. 두 병렬 트랙

```text
Product & Core Track ── 제작·검증·복구 ─┐
                                       ├─ 같은 Milestone Gate
Revenue & Distribution Track ─ 유입·가격·결제·재사용 ┘
```

- 제품 트랙만 PASS하면 좋은 Demo일 수 있지만 사업 PASS는 아닙니다.
- 사업 트랙만 PASS하고 제품 재현이 안 되면 수작업 대행이며 Core PASS가 아닙니다.
- 각 마일스톤은 두 트랙의 필수 증거가 모두 있어야 승격합니다.

## 4. M1~M8

| 단계 | Product & Core Track | Revenue & Distribution Track | Gate·산출물 | 사용자 개입 |
|---|---|---|---|---|
| M1 기반 준비 | Story/Profile/Scene Schema, Product Contract, Resolver, Verifier, Version·Restore Fixture | 고객·문제·가격 가설, 원가 항목, 중단 기준 | 정상·실패·Restore Fixture, 고객별 코드 0 목표 | 실제 자료·비용·외부 전송 경계 승인 |
| M2 내부 Fixture | PPT Import/Export 격리 시험, Memory·Knowledge 가상 Run, 모바일·PC 검사 | 브랜드·도메인 후보 조사, 무료/유료 상품 문구 | 두 입력의 Core Artifact, 손실 경고, 수동 보정 횟수 | 서로 다른 Visual Target 중 방향 승인 |
| M3 공개 샘플 | 정적 결과·6~10초 무음 모션·공유 링크·삭제 | 저비용 도메인, 랜딩, 최소 Event, 신청 폼 | 외부 열람·삭제·재생·복구 PASS | 도메인 구매·공개 범위 승인 |
| M4 탐색 Pilot | 실제 입력 각 5명 이내, 실패 격리, 사람 시간 측정 | 카페·카카오·관계 채널 수동 모집, 무료 체험 | 완성·공유·수정·지원·원가 기록 | 민감 예외와 실제 사용 승인 |
| M5 첫 결제 | 개선 PPT·3 Scene PDF 또는 웹 결과 전달 | 실제 가격·외부 결제 링크·환불 기준 | 결제, 총원가, 마진, 지원시간 | 가격·결제·환불 최종 승인 |
| M6 반복 검증 | 두 번째 자료 재생성, Recipe 재사용, Restore | 재구매·추천·카카오 재방문 | 고객별 코드 수정 0, 두 번째 사용 또는 추천 | 반복 상품·공개 사례 승인 |
| M7 제한 Beta | 회원·Object Storage·운영 콘솔·사용량·오류 추적 | 카페 사례 축적, 제한 모집, 수동 도메인·MP4·POD | 권한·TTL·삭제·비용 상한·장애 복구 | 계정·개인정보·운영 정책 승인 |
| M8 확장 | Queue, MP4, TTS, POD, 팀·화이트라벨 Adapter | 구독·기관·광고·제휴 시험 | 반복 수요와 마진이 확인된 Capability만 연결 | 투자·정기결제·제휴·Core 승격 승인 |

## 5. 단계별 금지선

- M1 Fixture PASS 전 회원·구독·고급 영상 기능을 만들지 않습니다.
- M2 양방향 PPT 손실 검사가 없으면 고객 원본을 덮어쓰지 않습니다.
- M3 실제 공유가 없으면 광고·SNS 자동 게시를 만들지 않습니다.
- M4 실제 사용이 없으면 회원 플랫폼을 확장하지 않습니다.
- M5 실제 결제 전 고급 영상 Provider·TTS·POD API에 투자하지 않습니다.
- M6 두 번째 사용 전 정기구독을 만들지 않습니다.
- M7 운영·삭제·복구 PASS 전 공개 대량 모집을 하지 않습니다.

## 6. 자동화와 사람 판단

### Core가 자동 수행할 범위

- 입력 형식·용량·해상도·페이지·권리 필드 검사
- PPT 요소 분류와 지원·경고·차단 판정
- Story Profile·Scene 초안과 등록 Recipe 추천
- Layout·Overflow·Asset·모바일·공개 범위 검사
- 비용·시간·재시도 상한, Artifact·Version·Restore
- Run Event, 실패 이유, 수동 보정 횟수 기록

### 증거가 쌓인 뒤 자동화할 범위

- 반복 성공 Recipe 추천과 유료 출력 제안
- 채널별 홍보 초안·FAQ·재방문 초안
- MP4 Queue·POD 주문·TTS 생성
- 실패 패턴에서 Verifier 후보 생성

### 사람 승인 유지

- 실제 자료·외부 Provider 전송·비용
- Visual Target과 감정적·미학적 최종 판단
- 공개·결제·환불·POD·음성권·미성년자·저작권 예외
- 배포·PM 잠금·공통 Core 승격·투자

## 7. TTS 위치

M1에는 `Audio Slot`과 Provider 중립 Adapter 계약만 둡니다. M5 실제 결제와 음성 수요가 확인되기 전
TTS Provider를 연결하지 않습니다. 기본 TTS는 M8 승격 후보이며, 본인·가족 음성 복제는 별도 동의·
삭제·사칭 방지 계약을 통과한 고위험 Capability로 분리합니다.

## 8. 반복 수정 방지 Gate

1. 구현 전에 Content Schema·Screen Manifest·State Matrix를 완성합니다.
2. Reference 선택을 Design DNA와 Draft Design Recipe로 변환해 Hash로 잠급니다.
3. 모든 필드는 한 편집 Surface만 소유합니다.
4. 사진 없음·비율 차이·긴 글·빈 값·오류·모바일·PC 상태를 Fixture에 포함합니다.
5. 결과를 직접 고치지 않고 Contract·Adapter·Recipe·Verifier 중 빠진 지점을 수정합니다.
6. 동일 입력으로 Core Run을 재실행하고 전체 회귀·Restore를 통과합니다.
7. 한 제품의 규칙은 제품 Adapter에 두고 서로 다른 제품에서 반복된 규칙만 공통 Core로 승격합니다.

## 9. 필요한 최소 환경

- 즉시: 기존 V2 Run, Git/Wiki, Product Registry, Schema, Verifier, Event Log
- M2: 격리된 PPT Parser/Renderer Capability Lab과 원본 불변 Hash 검사
- M3: 독립 도메인·정적 배포·공유 Event·삭제 기능
- M4~M5: 신청 폼·Run ID·외부 결제 링크·원가/지원시간 기록
- M7: Object Storage·Auth/DB·운영 콘솔·오류 추적
- M8: 장기 Queue·FFmpeg·TTS·POD·정기결제 Adapter

외부 Skill·오픈소스는 License·유지관리·원본 보존·실패·복구를 Capability Lab에서 비교한 뒤 연결합니다.
도구 설치나 샘플 성공만으로 Core Capability가 되지 않습니다.

## 10. 설계 완료와 실제 완료의 구분

- Storyboard 공통 구조: `design_complete`
- M1~M8 단계·Gate·두 트랙: `design_complete`
- Story Profile·Scene Schema 파일: `not_implemented`
- PPT Import/Export Adapter: `not_implemented`
- Memory/Knowledge Fixture와 Runtime: `not_started`
- 독립 도메인·결제·Pilot·수익: `not_started / not_proven`

다음 실행은 M1이며, M1 PASS 전 M2 제품 화면을 먼저 만들지 않습니다.

## 11. Milestone Result Snapshot·전체 동기화 계약

각 Story M1~M8은 파일 수정이 끝났다고 종료하지 않습니다. 해당 마일스톤의 코드·계약·입력 Hash·
산출물·검증·사용자 판정·미해결 한계·복구 방법을 하나의 `Milestone Result Snapshot`으로 고정해야
종료됩니다.

### 마일스톤 종료 순서

```text
작업 완료
→ 전체 회귀·실패·Restore 검사
→ 사용자 판단이 필요한 항목 일괄 확인
→ Milestone Result Manifest 생성
→ Result Commit 생성
→ 불변 Milestone Tag 생성
→ GitHub main Fast-forward
→ Obsidian·공통 Wiki Fast-forward
→ local / origin main / Obsidian SHA 일치 확인
→ CURRENT_STATE가 최신 Snapshot을 가리키게 갱신
→ 다음 마일스톤 시작
```

### Result Manifest 필수 내용

- 프로젝트명 `스토리 보드`, 마일스톤 ID, Run ID, 완료 시각
- Base Commit·Result Commit·Milestone Tag
- 승인된 Product/Design/Revenue/Privacy Contract Hash
- 입력 원본 Hash와 원본 불변 여부
- 생성 Artifact 경로·Hash·Runtime 주소
- 실행한 Verifier·명령·종료 코드·판정
- 사용자 승인 원문 또는 승인 Artifact
- 자동화된 부분·사람 개입·Codex 개입 횟수
- 비용·소요시간·재시도·알려진 한계
- 이전 Snapshot과 Restore 절차

### Commit·Tag 규칙

- Commit은 문서 파일만이 아니라 마일스톤에서 승인된 저장소 전체 상태의 기준점입니다.
- 권장 Tag는 `story-board-m1-result-v1`처럼 마일스톤과 Version을 포함합니다.
- 검사 실패·사용자 승인 미완료·동기화 SHA 불일치 상태에서는 Result Tag와 완료 판정을 금지합니다.
- 이미 만든 Result Tag를 다른 Commit으로 강제 이동하지 않습니다. 변경은 `v2`, `v3` 새 Tag로 남깁니다.
- 미완성 중간 Commit은 허용하지만 `Milestone Result Snapshot`으로 표현하지 않습니다.

### 최신 기록과 회귀

- `wiki/CURRENT_STATE.md`는 항상 가장 최근 완료 Snapshot과 현재 진행 중인 마일스톤을 함께 표시합니다.
- 과거 Snapshot은 삭제하거나 최신 파일로 덮지 않고 Commit·Tag·Manifest로 보존합니다.
- 회귀는 현재 Worktree를 강제 초기화하지 않고 과거 Tag에서 새 Branch/Worktree를 만들어 검사합니다.
- 회귀 결과를 채택하면 새 Result Commit과 새 Tag를 만들며 과거 Snapshot은 그대로 유지합니다.
- 사용자 자료·Secret·대용량 외부 Artifact는 Git에 직접 넣지 않고 Hash·권한·보존 위치·복구 증거를
  Manifest에 기록합니다.

### 동기화 PASS

다음 네 값이 같아야 `synced`로 기록합니다.

1. 활성 작업 저장소 Result Commit
2. GitHub `origin/main`
3. Obsidian Vault HEAD
4. Milestone Result Manifest의 `result_commit`

웹 GPT에는 GitHub `main`의 Commit과 필수 문서 경로를 전달합니다. 직접 GitHub Commit을 확인하지
못한 AI는 최신 상태를 확인했다고 표현할 수 없습니다.
