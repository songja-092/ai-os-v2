# 스토리 보드 M1 완료 보고서 — 2026-08-30

판정: `PASS_M1_FOUNDATION / PRODUCT_RUNTIME_NOT_STARTED / REVENUE_NOT_PROVEN`

## 완료한 것

- 공식 프로젝트명 `스토리 보드`, Core 식별자 `story-board`
- 회의 Decision Schema와 `v2 storyboard intake`
- 확정 답변 재질문 방지와 최대 8개 질문 Budget
- Story Profile·Scene Contract Schema
- 가상 Knowledge Story PPTX 3장 생성·전체 렌더·개별 시각 확인·Overflow PASS
- PPTX 읽기 전용 Import Draft와 원본 SHA-256 불변 검사
- 손상 PPTX·중복 Decision·불완전 Result Manifest 차단 Fixture
- Story Board Product Contract Draft
- 기존 Product Harness Registry·Resolver에 Story M1 Profile·Adapter·Verifier 연결
- Visual Target·최종 승인 전 `execution_allowed: false` 차단
- Evidence Commit·Seal Commit·불변 Tag 방식의 Milestone Snapshot Gate
- Open XML SDK·Apache POI·PptxGenJS·LibreOffice와 현재 Bundle 환경 비교

## Core가 직접 재현한 증거

- `v2 storyboard intake`가 확정 Decision 12개를 재사용하고 후속 질문 3개만 남김
- `tools/verify-storyboard-m1-foundation`: 정상·중복·손상·불완전 Fixture PASS
- `tools/verify-product-contract`: Draft Contract PASS
- `tools/resolve-product-harness`: Story Profile·Adapter·Verifier Coverage 완료
- 별도 Detached Worktree에서 Evidence Commit 동일 검사 PASS

## 사용자 개입

- M1 중 새 질문: 0개
- 기존 회의에서 승인한 기본값을 사용했습니다.
- 실제 고객 자료·외부 유료 도구·도메인·공개·결제는 사용하지 않았습니다.

## 발견하고 Core에 반영한 병목

1. 임시 출력이 저장소 내부라고 가정한 경로 처리
2. Manifest가 자기 Commit Hash를 담을 수 없는 Snapshot 순환 구조
3. Fixture Slide에 내부 제작 문구가 노출되는 품질 문제
4. Resolver의 전자명함 한계 문구 하드코딩

Codex 수동 보완 4회, 고객별 코드 0회로 기록합니다. 네 가지 보완은 결과 파일 땜질로 남기지 않고 Core
도구·Schema·Resolver·계약 규칙으로 반영했습니다.

## 아직 하지 않은 것

- 사용자 Visual Target 선택과 Design Recipe
- 기존 PPTX의 복합 요소 완전 보존·편집
- Story Profile·Scene에서 PPTX를 다시 생성하는 정식 Export Adapter
- 웹 이야기·Motion·MP4·TTS·POD
- 실제 고객·도메인·공개·결제·수익

## 다음 단계

`스토리 보드 M2 내부 Fixture`에서 PPT 양방향 변환 세 모드와 서로 다른 Visual Target을 검증합니다.
M2의 첫 사용자 개입은 실제 디자인 방향을 선택할 때 한 번만 요청합니다.
