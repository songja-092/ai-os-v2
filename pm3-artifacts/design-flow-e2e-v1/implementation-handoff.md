# 온담 커뮤니티 디자인 흐름 E2E 구현 Handoff

## 목적

승인 방향의 Recipe 계보를 실제 제품 구현·독립 검증·복구까지 연결하는 격리 Pilot입니다. 상업 배포나 최종 디자인 승인이 아닙니다.

## 고정 입력

- Recipe ID: `ondam-home-community-reference-adoption-v1`
- Recipe SHA-256: `b7f6c3637ec8452120ac443e51714254443472f1d2c0af1971c9a9624a809d84`
- Selection SHA-256: `1c22a0435105405c79cc98584650110bd57a9f0fc4ff134a7f23437ee0d75310`
- Visual Target HTML SHA-256: `4ef41536af08855398f705d08a981fde5d516b09d81cc42c5f6f8d42e9ec1062`
- PC Target SHA-256: `78086e45eabec1afd9c3cb3a7d5a5b62f87531d05e752062e7294164121d5edb`
- Mobile Target SHA-256: `f7d0ccca4f3af9fbae7861bb2d75ef2f46692a4c241d06de67dda30fb8ed25e7`
- 격리 제품 저장소: `/home/user/바탕화면/ondam_design_flow_e2e`
- 격리 Base Commit: `eafcf3a55d8479b66b6189b365ab1c0ef5e827ec`

## 구현 범위

- `navigation`, `hero`, `live-topics`, `community-feed`, `questions`
- PC 1440×950, 모바일 430×932
- 검색, 글쓰기, Hero 행동, Filter, 좋아요·저장 기본 상호작용
- Keyboard Focus, alt, status, reduced-motion
- 외부 CDN·Analytics·로그인·결제·네트워크 요청 없음
- `design-lineage.json`에 Recipe·Section·Source 계보 기록

## 역할

- Antigravity: 격리 제품 구현과 자체 제한 보고
- Codex: Input Hash, Fidelity, 기능, 접근성, 회귀, Commit, Restore 독립 검증
- 사용자: 구현 결과 최종 승인·수정·폐기

## 금지

- 기존 V2·제품·Dirty Worktree 수정
- 입력 파일 수정
- 외부 배포·패키지 설치·Git Commit
- 구현자가 자신의 결과를 최종 PASS 처리
