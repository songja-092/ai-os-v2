---
id: interior-tool-community-ecosystem
title: 인테리어 무료 도구·커뮤니티·전문가·자재 생태계
status: strategic_direction
classification: isolated_post_pm_business_strategy
adopted_by_v2: false
implementation_approved: false
auto_resume: false
created: 2026-08-16
resume_trigger: PM 완료 후 사용자가 인테리어 생태계 사업 파일럿 시작을 명시적으로 승인할 때
---

# 인테리어 무료 도구·커뮤니티·전문가·자재 생태계

> [!warning] PM 이후 장기 사업 방향
> 이 문서는 V2 Core, 공식 PM, Run 또는 즉시 구현 지시가 아니다. PM 완료 후 발전 방향을 잃지 않기 위한 전략 기록이며 사용자 승인 없이 개발·설치·배포를 시작하지 않는다.

## 장기 목표

```text
인테리어 현장 문제를 해결하는 무료 도구
→ 반복 사용자와 커뮤니티
→ 전문가 프로필·포트폴리오·구인구직
→ 전문가용 유료 업무 도구
→ 자재·공구 광고와 브랜드관
→ 상품·거래
→ 3D 모델·자재·시공 생태계
```

네이버 카페는 초기 유입과 사용자 조사 채널로 사용하고, 회원·포트폴리오·평판·도구 데이터의 장기 원본은 자체 웹이 소유한다.

## V2의 역할

V2는 초기에는 고객이 직접 사용하는 상품보다 내부 개발·유지보수 엔진으로 사용한다.

```text
현장 요구 수집
→ 조사·분석
→ 작은 기능 Preview
→ 사용자 확인
→ Module·Adapter·Skill 구현
→ 독립 검증
→ 배포
→ 유지보수·복구
→ 검증된 Recipe만 재사용 승격
```

## 검증 사례에서 가져올 구조

### Houzz

- 포트폴리오·전문가 검색·상품·광고·전문가용 업무 도구를 결합한다.
- 가져올 것: 전문가 프로필, 지역·분야 검색, 포트폴리오, 업체·브랜드 홍보.
- 가져오지 않을 것: 품질이 확인되지 않은 리드를 과도하게 유료 판매하는 방식.
- 공식 근거: https://www.houzz.com/advertiseOnHouzz
- 공식 근거: https://www.houzz.com/houzz-pro/pricing?proType=core

### SketchUp 3D Warehouse

- 커뮤니티가 3D 모델을 공유하고 제조사가 실제 상품 카탈로그를 연결한다.
- 가져올 것: 모델·자재 공유, 제조사 카탈로그, 실제 상품 연결.
- 가져오지 않을 것: 초기부터 완성형 3D 편집기 제작.
- 공식 근거: https://sketchup.trimble.com/en/products/3d-warehouse

### HubSpot

- 무료 도구와 Template로 사용자를 유입시키고 반복 업무를 유료 제품으로 연결한다.
- 가져올 것: 무료 도구 → 저장·반복 사용 → 전문가용 유료 기능 흐름.
- 공식 근거: https://www.hubspot.com/free-business-tools
- 공식 근거: https://www.hubspot.com/products/marketing/free

### 네이버 카페

- 초기 구인구직·질문·시공 사례·무료 도구 배포와 사용자 조사에 사용한다.
- 카페 광고 지면과 핵심 회원 데이터에 사업 전체를 의존하지 않는다.
- 공식 근거: https://help.naver.com/service/5622/contents/4299
- 공식 근거: https://help.naver.com/service/5622/contents/24561
- 공식 근거: https://help.naver.com/service/5622/contents/24979

## 추천 진입 분야

현재 검증된 PDF 도면 기호와 가까운 전기·설비·소규모 현장 관리 직군부터 시작한다.

첫 무료 도구 후보는 최대 세 개로 제한한다.

1. 현장 일정 Calendar
2. PDF 도면 기호
3. 현장 사진·체크리스트

기본 기능 사용을 게시글·댓글 활동으로 강제하지 않는다. 활동 조건은 고급 Template, 전문가 배지, 추가 저장 공간, 상단 노출처럼 추가 가치에만 연결한다.

## 단계별 발전

### B1 — 현장 사용자 검증

- 전기·인테리어 실무자 10~30명 인터뷰·사용 시험
- 가장 반복되는 문제 한 가지 확인
- 가입자 수보다 주간 반복 사용과 결과 공유를 측정

### B2 — 무료 도구 공개

- Calendar와 PDF 도면 기호 중 반복 가치가 높은 두 개만 공개
- 로그인 없이 기본 사용
- 저장·재사용이 필요한 시점에만 가입 제안

### B3 — 초기 커뮤니티

- 네이버 카페에서 구인구직, 현장 질문, 시공 사례와 도구 사용법 운영
- 카페 장애·정책 변경이 자체 도구와 데이터에 영향을 주지 않게 분리

### B4 — 자체 전문 웹

- 전문가 프로필
- 포트폴리오
- 지역·기술 분야 검색
- 작업 가능 일정
- 구인·구직
- 무료 도구 진입점

### B5 — 신뢰와 유지보수

- `미확인`, `서류 확인`, `활동 확인`, `거래 완료`, `사용자 후기`를 분리
- V2가 기술 능력을 근거 없이 자동 인증하지 않음
- 신고·차단·분쟁 증거·복구 절차 마련

### B6 — 수익화

권장 순서:

1. V2를 이용한 맞춤 웹·업무 도구 제작과 유지보수
2. 전문가용 프로젝트 관리 도구 구독
3. 포트폴리오·구인글·업체 브랜드관 유료 노출
4. 자재·공구 광고와 제휴
5. 충분한 거래량과 운영 역량 확보 후 거래 수수료

광고와 일반 추천은 사용자 화면에서 명확히 구분한다.

### B7 — 3D·자재 생태계

- 초기에는 3D Viewer, 외부 파일 Preview, 자재 목록과 제조사 링크만 제공
- 반복 사용이 검증된 뒤 모델 공유·제조사 카탈로그·견적·구매 연결 검토
- Figma 수준 편집기나 범용 3D 제작기를 초기 범위에 넣지 않음

## PM 이후 V2 기존 후보와 연결

Obsidian에 이미 존재하는 후보 중 이 전략에 재사용 가능한 것은 다음과 같다.

| 기존 후보·기능 | 현재 상태 | 생태계 적용 위치 |
|---|---|---|
| 정적 Project·Module Registry | PM1 계약, 구현·격리 검증 필요 | 무료 도구와 프로젝트 분리 등록 |
| Direct Partial Edit Panel | PM2 후보 | 업체 포트폴리오·Landing Page 수정 |
| Source Adapter | PM3 후보 | 자재·업무·시장·병목 조사 |
| Intent Packet·Receipt | PM4 후보 | 잘못 이해한 기능 제작 차단 |
| `web_camera_capture` | 후속 미검증 후보 | 현장 사진 촬영 |
| 실제 Galaxy Preview | 후속 미검증 후보 | 현장 모바일 실기기 확인 |
| Supabase Full-stack Recipe | 조건부 후보 | 계정·프로필·포트폴리오·구인구직 데이터 |
| Personal OS 부모·자식 보드 | 격리된 장기 후보 | 직군별 기능 패키지 배포 |
| Package Registry·Runtime Plugin | 보류 | Module Registry 안정화 뒤 재검토 |
| 고객 OS·Marketplace | 보류 | 실제 반복 수요와 운영 역량 확보 뒤 검토 |

Calendar, 견적, 포트폴리오, 구인구직, 광고, 상품 판매와 3D 생태계는 현재 공식 구현 후보로 상세 정의되어 있지 않다. 이 문서에서 사업 Feature 후보로 보존하되 PM에 자동 편입하지 않는다.

## PM 완료 후 반드시 먼저 확인할 세 가지

```yaml
module_adapter_skill_extension: verified_required
module_failure_isolation: verified_required
test_approval_restore_reuse_lifecycle: verified_required
```

세 조건이 실제 PASS한 뒤에만 B1 사업 파일럿을 시작한다. PM 완료 선언만으로 자동 충족된 것으로 간주하지 않는다.

## 성공 지표

- 주간 반복 사용자
- 도구 결과 저장률
- 결과 공유율
- 4주 유지율
- 포트폴리오 등록률
- 실제 구인·지원 발생 건수
- 돈을 지불할 의사가 확인된 기능
- 신고·분쟁·실패 후 복구 가능 여부

회원 수와 게시글 수만으로 성공을 판정하지 않는다.

## 현재 제외

- 처음부터 대형 인테리어 Marketplace 제작
- 자체 결제·정산·분쟁 시스템
- 완성형 3D Editor
- 활동량을 늘리기 위한 무의미한 글·댓글 강제
- 광고를 일반 추천처럼 표시
- 근거 없는 전문가 인증
- 고객 데이터를 네이버 카페에만 보관
- 사용자 승인 없는 기능 자동 배포

## 다음 재개 작업

PM 완료 후 다음 한 작업만 수행한다.

```text
전기·인테리어 현장 사용자 10~30명을 대상으로
Calendar·PDF 도면 기호·현장 사진 중
가장 반복 가치가 높은 무료 도구 하나를 선택하는 조사
```
