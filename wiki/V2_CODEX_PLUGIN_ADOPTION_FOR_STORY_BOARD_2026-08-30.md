# V2·스토리 보드 Codex 플러그인 적용 판단 — 2026-08-30

상태: `review_complete / adoption_order_decided / runtime_integration_not_proven`

## 결론

Codex 플러그인과 Skill은 V2 Core가 아닙니다. 제작·검사·배포를 담당하는 교체 가능한 Adapter이며,
V2 Core는 입력·계약·상태·승인·Artifact·Hash·검증·Version·복구를 계속 소유합니다.

```text
Codex Plugin·Skill → 교체 가능한 작업 Adapter
V2 Core → 실행 계약·증거·승인·복구의 소유자
```

플러그인이 결과를 한 번 생성한 사실만으로 V2 Capability가 되지 않습니다. 동일 입력을 Core가 호출하고
정상·실패·비용·결과 Hash·복구를 재현한 격리 Pilot 증거가 있어야 Registry 승격 후보가 됩니다.

## 적용 우선순위

| 시점 | 도구 | 제한된 역할 | 현재 판정 |
|---|---|---|---|
| Story M2 | Presentations | PPT 읽기·생성·렌더링·시각검사 | 즉시 사용 Adapter |
| Story M2·PM1 | Product Design + ImageGen | Reference 후보·Visual Target 제작 | 필요할 때만 사용 |
| PM2 | Build Web Apps | 승인된 Design Recipe의 웹 구현 | 기존 운영 계약 유지 |
| PM6 | Browser + Frontend Testing | Route·Console·상호작용·반응형·회귀검사 | 기본 검증 Adapter |
| PM6 | Product Design Audit | 마감·접근성·Visual Target 비교 | 기능 검사와 분리 |
| M2 이후 | PDF·Documents | PDF·문서 입력을 Story 구조로 변환 | 별도 Import Pilot 필요 |
| 웹 구현 시 | React Best Practices·shadcn | 성능 규칙·검증된 UI 재사용 | 제품 Stack과 맞을 때만 |
| Story M3 | Sites | 공개 샘플·스토리 웹·랜딩·공유 링크 | 격리 Pilot 후보 |
| M5 | Stripe | 실제 결제·환불 흐름 | 첫 결제 Gate에서만 검토 |
| M7 | Supabase·Cloudflare | Auth·DB·Storage·독립 운영 | 운영 수요 확인 후 |
| M8 | Runway·Higgsfield 계열 | 유료 영상 생성 | 영상 결제·원가 확인 후 |

Gamma는 현재 Presentations와 역할이 겹치므로 우선 연결하지 않습니다. Figma는 팀 협업·디자인 전달이
실제 병목으로 확인될 때 검토합니다. Airtable·Trello·Asana는 고객·운영 작업량이 늘어난 뒤의 운영
Adapter 후보이며 지금 Core 의존성으로 만들지 않습니다.

## Sites 적용 경계

현재 저장소에는 `.openai/hosting.json`이 없으므로 Sites가 연결됐거나 배포 준비가 완료됐다고 표현하지
않습니다. Story M2는 PPT 양방향 변환과 Visual Target 검증 단계이므로 Sites를 도입하지 않습니다.

M3에서 다음 범위로 격리 비교합니다.

```text
Story Profile + Scene Contract
→ 승인된 Draft Design Recipe
→ Sites로 정적 웹 이야기·랜딩 제작
→ 공유 링크·삭제·모바일·복구 검사
→ V2가 Artifact·Hash·Version·Event를 기록
```

### Sites 우선 후보

- 개인정보·결제 없는 공개 Story 샘플
- 무료 체험 랜딩페이지
- 전자명함·개인 프로필
- 신청 안내 페이지
- 간단한 콘텐츠 허브

### Sites 자동 확대 금지

- 로그인·회원·결제·중요 개인정보
- 복잡한 권한·관리자·Migration·다중 사용자
- V2 Core 상태를 Sites가 직접 변경하는 구조
- 사용자 승인 없는 공개·도메인 연결·배포

위 항목이 필요하면 기존 구현 경로와 Sites Capability Pilot을 비교한 뒤 별도 승인합니다.

## 다음 세션 실행 규칙

1. M2에서는 `Presentations → Product Design` 순서만 우선 적용합니다.
2. Product Design·ImageGen은 기존 승인 Recipe와 Reference로 충분하면 생략합니다.
3. Build Web Apps는 Visual Target 승인 전 실행하지 않습니다.
4. Sites는 M3 이전에 설치·초기화·배포하지 않습니다.
5. 외부 플러그인이 실패해도 원본·기존 Artifact·다른 Adapter가 손상되지 않아야 합니다.
6. 성공 결과를 수동 복사해 Core PASS로 만들지 않습니다. Core 입력·출력·Hash·검증·Restore를 연결합니다.
7. 반복 성공과 시간·품질·비용 개선 증거가 없으면 Registry에 정식 승격하지 않습니다.

## 증거 경계

- 현재 설치 환경에서 Sites, Product Design, Build Web Apps, Browser, Presentations, PDF·Documents,
  Figma 관련 Skill 존재를 확인했습니다.
- V2 저장소에 Sites Hosting Marker가 없음을 확인했습니다.
- 이 문서는 도구 선택 판단이며 Sites Runtime·배포·결제·스토리 제품 완료 증거가 아닙니다.
- Codex 환경의 기능·가용성·정책은 변경될 수 있으므로 실제 Pilot 시작 시 현재 Skill과 공식 문서를
  다시 확인합니다.
