# 스토리 보드 Pilot과 Core 완성 계약 — 2026-08-30

상태: `approved_plan / implementation_not_started`

공식 프로젝트명은 `스토리 보드`입니다. 과거 회의의 `V2 Story Pilot`은 같은 프로젝트의 임시
작업명이었으며, `V2 Story Core`는 외부 브랜드가 아닌 내부 공통 계층으로만 사용합니다.

M1~M8의 제품·사업 병렬 트랙, PPT 양방향 변환, 단계별 Gate의 단일 실행 기준은
`wiki/V2_STORY_M1_M8_EXECUTION_BASELINE_2026-08-30.md`를 사용합니다.

이 문서는 2026-08-30 수익구조 회의의 최종 합의와, 전자명함 제작에서 발견한 반복 수정 병목을
V2 Core의 제품 제작 능력으로 바꾸기 위한 다음 실행 계약입니다. 시장 결제·공개 Runtime·다른 제품의
범용 재현은 아직 `not_proven`이며, 이 문서 자체는 구현·검증·수익 PASS가 아닙니다.

## 1. 쉬운 목표

V2는 사용자의 사진·기억·문서·지식을 받아 공유 가능한 이야기와 콘텐츠로 만들고, 같은 자료에서
디지털 결과·영상·PDF·실물책까지 확장할 수 있어야 합니다. 외부 채널은 홍보에 사용하고, 독립
도메인은 회원·자료·결과·결제가 쌓이는 제품 본체로 사용합니다.

완성 시 정상적인 두 번째 고객부터는 Codex가 고객별 화면을 직접 고치지 않습니다. V2 Core가 등록된
`Product Profile → Adapter → Recipe → Verifier`를 조립해 제작·검사·Version·Restore를 수행하고,
Codex는 새 실패 유형과 Core 결함을 진단하는 하네스 엔지니어 역할만 남깁니다.

## 2. 사업·채널 계약

```text
Threads · Instagram · YouTube · 검색
                  ↓ 홍보
             독립 V2 도메인
     무료 체험 · 작업공간 · 결과 · 결제
            ↙                 ↘
     네이버 카페              카카오톡
   사례 · 질문 · 지식       공지 · 베타 · 재방문
            ↘                 ↙
                 V2 재사용
```

- 독립 도메인은 제품·데이터·결제의 공식 본체입니다.
- 네이버 카페는 사례·질문·Recipe·신뢰를 축적합니다.
- 카카오톡은 업데이트·Pilot·재방문을 빠르게 전달합니다.
- 나머지 SNS와 검색은 홍보 채널이며 제품 상태의 원본이 아닙니다.
- 카페 활동이나 카카오톡 가입을 무료 제품 사용 조건으로 강제하지 않습니다.
- 사용자의 실제 기여에는 Credit·Beta·Pro 체험·수익 배분을 검토할 수 있지만 반복 증거 전에는
  자동 보상이나 Revenue Share를 만들지 않습니다.

## 3. 내부 공통 구조와 외부 제품 분리

`V2 Story Core`는 고객 브랜드가 아니라 내부 공통 제품 계층입니다.

```text
V2 Core
└── V2 Story Core
    ├── Memory Story 서비스 — 사진·기억·가족·기념일
    └── Knowledge Story 서비스 — PPT·PDF·강의·전문지식
```

가족 고객은 감정·보관·선물·개인정보 안전을 사고, 전문가는 업무 활용·반복 제작·성과를 삽니다.
따라서 랜딩·입력·공개 기본값·CTA·가격·분석 퍼널을 분리합니다. 대외 통합 브랜드는 각 Pilot에서
실제 결제 증거가 생기기 전 확정하지 않습니다.

공통 내부 흐름은 다음과 같습니다.

```text
Source Asset → Source Analysis → Story Profile → Scene Contract
→ Reference · Draft Recipe → Static Scene → Motion Preview
→ Product Verifier → Share Artifact → Version · Restore
→ 유료 PDF · MP4 · POD 후보
```

## 4. 좁은 비교 Pilot

### Pilot A — Memory Story

- 첫 입력: 성인 신청자가 권리를 가진 사진 1장, 호칭·별칭, 짧은 기억, 분위기
- 무료 출력: 정적 장면 1개, 6~10초 무음 웹 모션, 비공개 기본 공유 링크
- 행동: 외부 재생과 `우리 이야기도 만들기`
- 첫 유료 제안: 3장면 완성본, MP4, PDF
- 후속 후보: POD 실물책, 영상 QR, 가족 기념일, 반려동물, 부모·조부모 인생 이야기
- 아동 실사진 공개 서비스는 보호자 확인·삭제·Provider 전송·비공개 링크 계약 검증 전 금지합니다.

### Pilot B — Knowledge Story

- 첫 입력: 반복적으로 자료를 만드는 강사·컨설턴트의 프로필과 본인 소유 PPT/PDF 1개
- 무료 출력: 핵심 카드 1개, 6~10초 설명 모션, 공개·제한 공유 선택 링크
- 행동: 외부 방문, CTA, `내 자료도 변환하기`
- 첫 유료 제안: 추가 자료 변환, MP4, 수동 개인 도메인 연결, 월간 자료 업데이트

각 5명의 탐색 결과 후 각 10명 안팎의 행동 Pilot로 승격합니다. 이 표본은 통계적 시장 우승자를
선언하는 용도가 아니라 공유 없음·결제 없음·높은 수작업·감당 불가능한 위험을 조기에 제거하는
용도입니다. 서로 다른 유입 경로의 전환율을 그대로 비교하지 않고 각 퍼널 안에서 판정합니다.

## 5. 첫 수익과 확장 순서

초기 현실적 순서는 `단건 디지털 → 맞춤 제작 → POD → 반복 운영 → B2B 단체 → 구독 →
라이선스·화이트라벨`입니다.

- Memory Story: 3장면 디지털 → MP4·PDF → POD → 복수 가족 주문 → 고가 인생 이야기
- Knowledge Story: 추가 자료 → 맞춤 MP4 → 프로필·도메인 → 월 운영 → 팀·기관
- 광고는 충분한 무료 Traffic과 원가 증거 전 주수익으로 사용하지 않습니다.
- Credit과 구독은 두 번째 구매 또는 반복 사용 증거 뒤에만 만듭니다.
- POD는 PDF 생성 → 샘플 1~3권 → 고객 주문 3건 수동 처리 → 불량·배송·환불 기록 → 반복 시
  API 연결 순서로 진행합니다. 출판사 제휴는 주문 증거 뒤의 확장입니다.

## 6. 전자명함에서 발견한 반복 수정 병목

전자명함의 반복 수정은 단순 마감 부족이 아니라 조사·승인 결과를 구현 가능한 제품 규칙으로
변환하는 중간 계약과 자동 검사가 부족해서 발생했습니다.

| 반복 증상 | 빠진 제품 규칙 | Core 보완 |
|---|---|---|
| 인물과 배경 경계가 매번 어색함 | Asset Slot·배경 면·Crop·Blend 상태 | Portrait/Asset Adapter + 경계 검사 |
| 이름·사진·소개가 배경 이미지에 박힘 | 편집 가능한 Content Schema | Core Content State + 단일 편집 소유권 |
| QR 여백·정렬이 반복해서 틀림 | QR 안전영역·최소 크기·대칭 규격 | QR Verifier + 인쇄·모바일 검사 |
| 소개·경력이 여러 편집 화면에 중복됨 | 필드별 편집 소유 Surface | Screen Manifest + 중복 필드 검사 |
| 시안이 색상만 달라지고 다양성이 줄어듦 | 다양성 축·제품 필수 행동 | Direction Diversity Gate |
| Visual Target과 구현 결과가 달라짐 | Target Hash·Recipe·Fidelity Gate | 구현 전 Hash 확인 + 시각 마감 검사 |
| 작은 수정이 다음 화면을 망가뜨림 | State Matrix·회귀 범위 | 제품별 전체 회귀검사 |
| Codex가 직접 고쳐야만 완료됨 | Core Action·Artifact·Restore 경로 | Codex-only 결과 차단 |

### 반복 수정 방지 공식 흐름

```text
조사·인터뷰
→ Product Contract
  - 사용자 결과·편집 가능한 Content Schema·Screen Manifest
  - State Matrix·Asset/Theme/Layout 규칙·자동 검사와 사람 승인
→ Draft Design Recipe
→ Profile·Adapter·Verifier 조립
→ 구현 → 제품별 회귀·Visual QA
→ 실패 이유를 제품 규칙 후보로 기록
→ 서로 다른 실제 입력에서 반복 성공 후 Core 승격
```

사용자의 한 번성 수정은 바로 공통 Core 규칙으로 올리지 않습니다. 제품별 Adapter에서 정상·실패·복구
증거를 확보하고 다른 제품에서도 반복되는 규칙만 공통 Core 후보로 승격합니다.

## 7. 최종 완성까지의 과정

### 단계 0 — 계약·환경 준비

1. Memory/Knowledge Product Contract와 입력·출력 Schema
2. 임시 파일 TTL, 공개·비공개, 삭제, 외부 Provider 전송 계약
3. 공통 Story Recipe와 제품별 Verifier
4. 비용·사람 시간·재시도·실패 이유 Event 계약
5. 가상 자료로 정상·실패·Restore Fixture

### 단계 1 — 가상 샘플

1. 가상 Memory 샘플 1개와 공개 허가 자료 Knowledge 샘플 1개
2. 360px·390px·430px 모바일과 PC Preview
3. 정적 장면·모션·공유·삭제·복구 검사
4. Codex 수동 보정 횟수 기록

### 단계 2 — 탐색 Pilot

1. 각 5명 이내 신청
2. 기존 V2 Run으로 실행하고 사람 시간·수정·원가 기록
3. 실제 공유·외부 방문·유료 요청 측정
4. 반복된 수작업만 Adapter·Verifier 후보로 등록

### 단계 3 — 행동·결제 Pilot

1. 각 10명 안팎으로 확대하고 실제 가격과 외부 결제 링크 제시
2. 최소 유료 결제·두 번째 사용·지원시간 측정
3. Memory/Knowledge 실패 격리와 동일 Core Run 재현 확인

### 단계 4 — 제한 공개 Beta

1. 회원·작업공간·안정적 Object Storage
2. 사용량 Meter·관리자 Run 목록·오류 추적
3. 수동 도메인·MP4·POD 주문 운영
4. 네이버 카페 사례와 카카오 재방문은 수동·승인형으로 시작

### 단계 5 — 반복매출과 자동화

1. 반복 결제 뒤 Credit·구독·갱신
2. 반복 주문 뒤 MP4·POD Queue/API
3. 성공 데이터 뒤 유료 추천·FAQ·공지 변환
4. 기관 반복 계약 뒤 팀·화이트라벨

### 단계 6 — V2 Core 범용 완성 검증

Story 제품만으로 범용 완료를 선언하지 않습니다. 전자명함과 성격이 다른 실제 Story 제품이 다음 전체
경로를 고객별 코드 수정 없이 반복해야 합니다.

```text
자연어 요청 → 조사·인터뷰 → Requirements → Product Contract
→ Reference·Draft Recipe → 제품 조립 → 구현 → Product Harness
→ PM6 → 사용자 승인 → 공개 배포 → 운영 확인 → 재검증·복구
```

## 8. 필요한 환경과 도구

| 역할 | 우선 도구·방식 | 도입 시점 | 경계 |
|---|---|---|---|
| 도메인·정적 배포 | Cloudflare 계열 후보 | 샘플 공개 전 | 실제 계정·비용은 사용자 승인 |
| 초기 저장 | 기존 V2 Run + 단일 저장소 | 즉시 | 일반 회원 플랫폼 금지 |
| 안정적 파일 저장 | Cloudflare R2 후보 | 결제·공유 증거 후 | TTL·삭제·비공개 권한 필수 |
| 회원·DB | Supabase 후보 | 제한 Beta | Auth·권한·삭제 격리 Pilot 필요 |
| 분석 | PostHog 후보 또는 최소 Event Log | Pilot 시작 | 개인정보 없는 Event 우선 |
| 작업 Queue | 기존 V2 Run 우선 | 즉시 | 이중 상태 엔진 금지 |
| 장기 Queue | Trigger.dev 후보 | 장기 작업 병목 후 | Core Run이 상태 원본 유지 |
| 웹 모션 | CSS/Web Animations API | 첫 Pilot | Product Adapter가 Recipe 소유 |
| 복합 모션 | Canvas/Lottie | 반복 Template 후 | 고정 모션 재사용에 제한 |
| MP4 | FFmpeg | 실제 구매 후 | Queue·실패·라이선스 확인 |
| 고급 영상 | 교체 가능한 외부 Provider | 선결제 증거 후 | 비용 상한·권리·Fallback |
| TTS | 상업 라이선스 Provider | 유료 Pilot 후 | 본인·가족 음성 동의 필수 |
| PDF·POD | 공급사별 Print Adapter | 수동 샘플 후 | 판형·bleed·DPI·폰트·QR 검사 |
| 결제 | 외부 결제 링크 | 첫 Pilot | 자체 정기결제는 보류 |
| 국내 정기결제 | PG/PortOne 후보 | 반복 결제 후 | 계약·환불·세금 확인 |
| 오류 추적 | 서버 로그 → Sentry 후보 | 제한 Beta | 민감 원본 로그 금지 |
| 고객지원 | 문의 폼 + Run ID | 즉시 | 자동 답변은 데이터 후 |

외부 Skill·Plugin·오픈소스는 `조사 → License·유지관리 확인 → Capability Lab 격리 → 기존 방식 비교
→ 사용자 채택 → 실제 제품 → 반복 성공`을 통과해야 합니다. 설치됐다는 이유로 Core 능력이 되지 않습니다.

## 9. Skill·오픈소스 조사 우선순위

1. `Story Profile/Scene Recipe`를 구조화하는 Skill 또는 Schema
2. 이미지 안전영역·텍스트 Overflow·모바일 재생을 검사하는 Verifier
3. CSS/Web Animations·Lottie 기반 저비용 Motion Adapter
4. FFmpeg 기반 MP4 Export Adapter
5. PDF preflight·DPI·폰트·bleed·QR 검사기
6. 안전한 Object Storage TTL·삭제·서명 URL Adapter
7. Product Analytics Event 계약
8. POD 주문·배송 Adapter

조사 결과가 없거나 품질이 낮으면 작은 연결부만 직접 만듭니다. V2 Core·Secret·사용자 원본을 외부
Skill에 자동 전송하지 않습니다.

## 10. 자동화 지도

### 즉시 자동화 가능

- 파일 종류·용량·페이지·해상도 검사
- 임시 파일 TTL과 삭제
- Product Type 판정과 Profile 초안
- 등록된 Adapter·Recipe 검색
- 비용·시간·재시도 상한
- 모바일·텍스트·Asset 로드·QR·공개 범위 Verifier
- Version·Restore
- 채널·공유 Event 기록
- 실패 Run과 사용자 문의 연결

### 데이터가 쌓인 뒤 자동화

- 성과 좋은 Story/Content Recipe 추천
- 두 번째 제품·유료 기능 추천
- 반복 질문 답변 초안
- 우수 사례와 Core 승격 후보
- 휴면 사용자 재방문
- 카페·카카오·SNS 형식별 공지 초안
- 실패 패턴에서 새 검사 규칙 후보 생성

### 승인 후에만 실행

- 결과 공개·외부 게시·메시지·도메인 연결
- MP4·POD 주문·결제·환불·Credit 지급
- 사례 홍보 활용과 Product Recipe의 Core 승격

### 사람에게 유지

- 사업·투자·가격 정책
- 개인정보·저작권·가족 권리 예외와 미성년자·민감정보 판단
- 고액 맞춤 견적과 감정적·미학적 최종 품질
- 환불·배송·인쇄 분쟁
- 새 Product Contract와 공통 Core 규칙 최종 승인

## 11. 사용자 개입 최소 계약

사용자에게 기본적으로 남기는 판단은 다음 네 번입니다.

1. 첫 요청과 실제 자료·외부 전송·비용 승인
2. 서로 다른 Visual Target 중 최종 방향 승인
3. Pilot 결과의 실제 사용·공개·결제 범위 승인
4. 배포와 PM 잠금 최종 승인

이미 승인된 자료·방향·Recipe는 Hash를 확인해 재사용합니다. 로그인·비용·개인정보·외부 쓰기·잠금
충돌이 없으면 조사, 계약 초안, 조립, 구현, 일반 오류 수정, 동일 검사 재실행, 회귀·복구는 V2와
Codex가 연속 처리합니다. 사람 판단이 필요한 항목은 여러 번 끊어 묻지 않고 한 번의 승인 목록으로
모읍니다.

## 12. Codex 개입 감소 Gate

| 단계 | Codex 역할 | 통과 조건 |
|---|---|---|
| 첫 Fixture | 계약·Adapter·검사기 제작 | 정상·실패·Restore 증거 |
| 첫 실제 사용자 | 실패 원인 진단·최소 보완 | 수작업과 비용 기록 |
| 두 번째 사용자 | Core 재현 감시 | 고객별 코드 수정 0회 |
| 5~10명 Pilot | 예외만 진단 | 사용자당 사람 작업 목표 이하 |
| 제한 Beta | Core 결함만 수정 | 정상 Run 자동 완료·실패 격리 |
| 완성 | 감사·새 능력 Pilot만 수행 | 정상 제작에 Codex 개입 불필요 |

Codex가 결과 파일을 직접 수정해 통과시킨 Run은 제품 PASS로 계산하지 않습니다. 수정이 필요하면
먼저 Core 상태·Action·Adapter·Verifier·Recipe 중 빠진 소유 지점을 보완하고 동일 입력으로 새 Run을
재실행합니다.

## 13. 성공·중단 기준

### 공통 기술 PASS

- 같은 Core Run·Gate·Artifact·Version 구조
- Family/Knowledge 입력·실패 격리
- 고객별 코드 수정 없이 Adapter 교체
- 두 번째 사용자부터 기존 Recipe 재사용
- 제품별 정상·실패·Restore 검사
- 비용·시간·재생성·지원 기록
- Codex 수동 결과가 아니라 Core Artifact로 재현

### 시장 증거

- 결과 완성·실제 외부 공유 또는 업무 사용
- 외부 방문·재생과 `나도 만들기`
- 실제 가격이 제시된 유료 요청
- 최소 실제 결제와 두 번째 사용
- 사람 시간과 전체 변동비를 포함한 마진 후보

### 중단·재설계

- 공유·업무 사용이 거의 없거나 유료 제안에 실제 결제 0건
- 결과당 사람 작업이 반복적으로 40분 초과
- 고객별 코드 예외가 공통 Recipe보다 많음
- 개인정보·권리·품질 사고를 통제하지 못함
- 정적 결과보다 Motion의 추가 가치가 없음
- 두 번째 제품·자료 사용이 없음

## 14. 완료 정의

- `Core PASS`: 등록된 계약·Adapter·Verifier가 제품을 재현·검사·복구했습니다.
- `Product PASS`: 사용자가 결과를 실제로 완성·공유·재사용했습니다.
- `Revenue PASS`: 실제 결제·반복·지원 포함 마진 증거가 있습니다.

V2 Core 완성은 Story 수익 성공만으로 선언하지 않습니다. 전자명함과 성격이 다른 Story 제품에서
배포·운영·재검증·복구까지 반복되고 정상 고객 Run에 Codex 개입이 필요 없을 때 범용 MVP 완성 후보로
올립니다. 수익모델은 최소 결제와 반복 증거가 생길 때만 확정합니다.
