# 스토리 보드 M2 다음 세션 단일 인계 지시서

이 문서는 `스토리 보드` 프로젝트를 M1 이후 다른 Codex 세션에서 이어가기 위한 **단일 실행 진입점**입니다.
다음 세션은 작업 전에 이 문서를 끝까지 읽고, 아래의 `이해 확인 응답`을 먼저 출력한 뒤 실행합니다.

## 1. 시작 위치

- 저장소: `/home/user/바탕화면/ai_os_v2_pm3`
- 공식 프로젝트명: `스토리 보드`
- Core 식별자: `story-board`
- M1 불변 결과 Tag: `story-board-m1-result-v1`
- M1 Seal Commit: `edd0d299974b33d571c3f212188efa4ad2a7e0d3`
- 현재 단계: `M1_foundation_pass / M2_not_started`
- 다음 작업: `M2 내부 Fixture`

먼저 다음을 실행합니다.

```bash
git fetch origin --prune --tags
./tools/session-preflight
./tools/verify-story-board-next-session-handoff
./tools/verify-storyboard-m1-foundation
./tools/verify-product-contract story-board-artifacts/m1/product-contract.draft.json
```

현재 Worktree·`origin/main`·Obsidian SHA가 다르거나 Dirty 변경이 있으면 자동 Reset·Stash·Merge하지
않습니다. 차이를 먼저 보고하고 사용자 파일을 보존합니다.

## 2. 다음 세션이 정확히 알아야 할 사실

1. M1에서 완료한 것은 적응형 Intake, Story Profile·Scene Contract Schema, PPTX Import Draft,
   Product Contract Draft, Product Harness Resolver, Verifier, Version·Restore 기반입니다.
2. M1은 Story 제품 Runtime, 정식 PPT Export, Visual Target, 외부 공개, 결제, 수익을 증명하지 않습니다.
3. `PPT`는 입력·출력 형식이고 내부 원본은 `Story Profile + Scene Contract`입니다.
4. M2는 `Memory Story`와 `Knowledge Story` 가상 입력을 사용해 PPT 양방향 변환과 서로 다른
   Visual Target을 격리 시험하는 단계입니다.
5. M2에서도 사용자 승인 전 `implementation_allowed: false`를 유지합니다.
6. 실제 고객 자료·유료 Provider·도메인 구매·공개·결제·TTS·POD는 승인 없이 실행하지 않습니다.
7. 정상 결과를 Codex가 직접 고쳐 끝내지 않습니다. 실패 원인을 Contract·Profile·Adapter·Recipe·
   Verifier·수집기 중 올바른 계층에 반영하고 동일 Core Run을 다시 실행합니다.
8. 두 번째 고객부터 고객별 코드 수정 0회가 장기 목표이며, 정상 제작에서 Codex 개입은 점차
   줄어야 합니다.

## 3. M2 실행 순서

1. M1 Tag와 현재 Core 계약을 읽고 M1 결과를 다시 해석하거나 덮어쓰지 않습니다.
2. PPT Capability Lab에서 `extract_content`, `preserve_and_polish`, `restructure`,
   `export_storyboard` 네 모드를 정의하고 원본 불변 Hash를 유지합니다.
3. SmartArt·차트·수식·동영상·발표자 노트·누락 글꼴을 지원·경고·차단으로 분류합니다.
4. Memory Story·Knowledge Story Fixture 각각에서 Story Profile·Scene Contract·손실 경고·PPT 출력
   Artifact를 Core가 생성하게 합니다.
5. Reference 수집 → 후보 다양성 검사 → Design DNA → Draft Design Recipe → 서로 다른 Visual Target
   순서로 진행합니다.
6. 모바일·PC, 긴 글·빈 값·사진 있음/없음·비율 차이·오류 상태를 검사합니다.
7. 자동 검사와 Restore가 끝난 뒤에만 사용자에게 서로 다른 Visual Target의 방향 선택을 한 번
   요청합니다.
8. 선택 전 실제 제품 구현과 M3 공개 샘플 제작은 금지합니다.

## 4. 수집기 개선 계약

스토리 보드 조사에서는 Codex가 외부에서 확인한 결과와 V2 수집기가 낸 결과를 반드시 비교합니다.
비교 항목은 검색어 범위, 플랫폼·공급원, 국내외 균형, 시각적 다양성, 제품 기능 근거, 최신성,
중복 제거, 요약 정확성, 출처 추적성입니다.

차이가 확인되면 빠진 자료를 Codex 결과로 수동 추가하고 종료하지 않습니다.

```text
차이 기록
→ 누락 원인 분류(query/source/ranking/dedup/summary/adapter)
→ V2 수집 Contract·Adapter·Verifier 중 해당 계층 수정
→ 같은 입력으로 V2 수집기 재실행
→ Codex 결과와 Coverage 재비교
→ 개선 전·후와 남은 한계를 Artifact로 기록
```

- 사용자 제공 URL·이미지는 최고 우선순위입니다.
- 채택 Reference의 특징과 작성자·검색어는 다음 Run에 우선 반영합니다.
- 폐기 화면과 유사 후보는 제외하고 폐기 이유를 다음 검색어에 반영합니다.
- 기존 결과를 갈아엎지 않고 새 후보만 추가하며 URL·Hash·시각 유사도로 중복을 제거합니다.
- 수집기가 못 찾은 사실을 찾았다는 이유만으로 Core가 개선됐다고 표현하지 않습니다. 동일 입력의
  재실행 증거가 있어야 수집기 개선입니다.
- 도구 하나의 실패는 다른 공급원과 기존 채택 결과를 손상시키지 않아야 합니다.

## 5. 사용자 개입을 요청할 때

M2에서 사용자의 기본 개입은 **서로 다른 Visual Target 중 방향 승인 한 번**입니다. 다음 항목만
그보다 먼저 묻습니다.

- 실제 개인정보·가족·미성년자 자료 사용
- 외부 Provider 전송 또는 비용 발생
- 로그인·계정·법적 권리·저작권 판단
- 공개·배포·결제·도메인 구매
- 기존 잠금 파일과 충돌하는 변경

디자인 후보 추천, 기술 도구 선택, Fixture 값, 실패 수정, 회귀검사는 증거 기반 기본값으로 진행하고
승인 상태를 위조하지 않습니다.

## 6. M2 완료 조건

- 두 Story Fixture와 PPT 네 모드의 Core Artifact
- 원본 불변 Hash와 지원·경고·차단 손실 보고서
- 수집기 비교와 필요 시 Core 수집기 개선 전·후 증거
- 서로 실질적으로 다른 Visual Target과 Draft Design Recipe
- 모바일·PC·상태 Matrix·전체 회귀검사
- 별도 Worktree Restore PASS
- 사용자 방향 승인 Artifact
- Evidence Commit → Milestone Result Manifest → Seal Commit → 새 불변 Tag
- 현재 Worktree·GitHub `origin/main`·Obsidian SHA 동기화

위 조건 전에는 `M2 완료`, `제품 구현 완료`, `수익 검증`, `V2 범용성 증명`이라고 표현하지 않습니다.

## 7. 이해 확인 응답

다음 세션은 작업을 시작하기 전에 아래 여섯 줄을 현재 파일·검사 결과에 맞게 채워 사용자에게
간단히 보고합니다.

```text
프로젝트: 스토리 보드 (story-board)
확인한 기준점: <현재 HEAD> / M1 Tag story-board-m1-result-v1
완료 범위: M1 Foundation만 완료
현재 작업: M2 내부 Fixture
첫 사용자 개입: Visual Target 방향 승인
금지 오해: Runtime·공개·결제·수익은 아직 not_proven
```

검사기가 PASS해도 세션이 이 여섯 항목을 다르게 이해하거나 M1 결과를 새 승인으로 확대 해석하면
작업을 시작하지 않습니다.
