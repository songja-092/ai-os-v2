# Interview Me Capability Lab 보고서 — 2026-08-20

## 결론

Addy Osmani의 `Interview Me(인터뷰 미)`를 고정 Commit에서 Skill 하나만 격리 설치해 시험했습니다. 기술 Trial은 `PASS_WITH_FIX`였으나, 2026-08-20 사용자가 인터뷰는 Codex가 담당하고 V2 제품에는 필요 없다고 결정했습니다. 최종 V2 판정은 `discarded_by_user`입니다.

## 최종 사용자 결정

- V2 Core Registry 등록: 금지
- PM5 Runtime 연결: 금지
- 전역 Skill 설치: 금지
- Trial Artifact: 폐기 근거로 보존
- 필요한 인터뷰: Codex가 중요한·모호한 요청에서만 수행
- 명확한 요청: 질문 피로 없이 바로 작업

## 원본

```yaml
source: https://github.com/addyosmani/agent-skills
source_commit: df1edb2e05487d0aa6d93c747141e0aed1187f25
skill_path: skills/interview-me/SKILL.md
skill_sha256: 1d94741d10d2c826cd0c191aea3981ee94c8abb27ef2a166f6a372117d06448f
license: MIT
isolated_files: [SKILL.md]
```

전체 저장소는 다른 Skill·Hook·Script를 포함하므로 전체 설치하지 않았습니다. 고정 Commit의 `skills/interview-me`만 Trial 내부에 설치했으며 `~/.codex/skills`에는 설치하지 않았습니다.

## 격리·보안 결과

- Bubblewrap·Network none 실행
- Private Project·Git Metadata·Token·Cookie 미제공
- 환경 Credential 전달 없음
- Core Registry 미등록
- Core·제품 Write 없음
- 외부 API·Package 실행 없음

## 가짜 요청 3개

| 요청 | 기대 | 결과 |
|---|---|---|
| `H3 구역 글씨 크기를 한 단계 줄여줘.` | 인터뷰 생략 | PASS |
| `인테리어 웹 만들어줘.` | 인터뷰 시작 | PASS |
| 고위험 자동매매 요청 중 `인터뷰는 그만할래.` | 중단·구현 금지 | PASS |

## 원본에서 확인한 장점

- 한 번에 질문 하나
- AI의 현재 추측을 함께 공개
- 목표·사용자·성공 기준·제약·제외 범위 확인
- 명시적 사용자 확인 전 Spec·Plan·Code 생성 차단
- 명확한 단순 작업은 실행 대상에서 제외

## 필요한 V2 보완

원본은 질문 횟수의 고정 상한과 사용자의 즉시 중단 계약이 충분히 명시되지 않았습니다. 원본을 Fork하지 않고 V2 Adapter에 다음 정책을 둡니다.

```text
기본 OFF
→ 명시적 요청·중요한 모호성·결정 충돌에서만 실행
→ 질문 하나씩
→ 질문 3개마다 계속·현재 요약·중단 선택
→ 중단하면 미확정 상태로 저장하고 구현 금지
→ 사용자 확인 후 PM5 쉬운 의도 확인서로 변환
→ 인터뷰를 생략해도 기존 변경 범위 잠금이 없으면 구현 금지
```

`95% confidence`는 객관적 품질 점수가 아니라 인터뷰 중단을 돕는 자기 점검 표현으로만 사용합니다.

## Core 판정

```yaml
source_integrity: PASS
isolated_execution: PASS
activation_routing: PASS
question_fatigue: PASS_WITH_V2_ADAPTER
user_stop: PASS_WITH_V2_ADAPTER
pm5_receipt_schema: PASS_AS_FULL_MINIMUM_SCHEMA_PROTOTYPE
pm5_runtime_connection: not_implemented
registry_adoption: not_performed
verdict: PASS_WITH_FIX
```

현재 후보 상태는 `isolated_tested`입니다. 사용자가 채택하면 원본 Skill은 불변·비활성 Adapter로 Registry에 기록하고 PM5 구현 때만 연결해야 합니다.

## 증거

- `pm1-artifacts/capability-lab/trials/interview-me-addy/record.json`
- `pm1-artifacts/capability-lab/trials/interview-me-addy/v2-policy.json`
- `pm1-artifacts/capability-lab/trials/interview-me-addy/scenarios.json`
- `pm1-artifacts/capability-lab/trials/interview-me-addy/v2-adapter-verification.json`
- `pm1-artifacts/capability-lab/trials/interview-me-addy/core-verification.json`
- `pm1-artifacts/capability-lab/trials/interview-me-addy/evidence/trial-001.stdout.txt`
