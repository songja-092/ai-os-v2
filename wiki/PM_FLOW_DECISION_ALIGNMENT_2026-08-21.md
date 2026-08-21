# PM0~PM6 사용자 결정 정합성 감사 — 2026-08-21

## 판정

`PASS_WITH_IMPLEMENTATION_GAPS`

사용자가 확정한 디자인 탐색·채택·부분 수정·명세·통합 검증 흐름을 PM0~PM6 공식
기준에 배치했습니다. 기능 중복은 제거했지만 문서 반영이 실제 Core Runtime 구현을
뜻하지는 않습니다.

## PM별 최종 배치

| 결정 | 소유 PM | 경계 |
| --- | --- | --- |
| Worktree·Port·격리·복구 | PM0 | 외부 Backup 표본 Restore는 사용자 유예 |
| 서로 다른 디자인 방향 3개 | PM1 | 완성 Code Preview 3개를 만들지 않음 |
| 선택된 후보·부분의 7축 Design DNA | PM1 | 선택 전 상세 DNA 생성 금지 |
| Visual Target 하나·디자인 승인 | PM1 | 승인 전 구현·Recipe 승격 금지 |
| 승인 Recipe·Component의 Module 조립 | PM2 | 디자인 품질과 조립 기능 PASS 분리 |
| 편집기→Recipe Diff→Version·Restore | PM3 | 편집기가 Core·Recipe 원본을 소유하지 않음 |
| 기존 Recipe·DNA·Block·Skill 우선 검색 | PM4 | 충분하면 외부 수집하지 않음 |
| 부족한 Reference·Block·Skill·병목 조사 | PM4 | 선택·DNA·디자인 승인은 PM1 소유 |
| 인터뷰·Spec Lite/Full·Scope Lock | PM5 | PM 번호와 무관하게 모든 제작 시작에 호출 |
| 전체 디자인 흐름·제품·모바일·복구 재검증 | PM6 | 디자인 방향을 새로 결정하지 않음 |

## 누락 확인 결과

반영 완료:

- 새 프로젝트 전체 인터뷰, 큰 변경 짧은 인터뷰, 명확한 작은 수정 생략
- 작은 수정이 커지면 인터뷰 또는 Spec Full로 승격
- 기존 성공 자산 우선, 부족할 때만 수집기 실행
- 한국 Reference 우선·해외 보완·원본 링크와 출처 기록
- 구조적으로 다른 방향 3개와 사용자 시각 선택
- 선택 후에만 Design DNA 추출
- Visual Target 하나·Draft/Approved Design Recipe
- UI UX Pro는 품질 검사, 디자인 총괄은 방향 결정
- Antigravity 구현·Codex 독립 검증·사용자 최종 판정
- 마우스 직접 이동·Inline/Panel 글자·자유 Resize·이미지 교체/크기
- PC·모바일 공통 속성과 배치 Override 분리
- 단계 Undo·Draft 전체 폐기·Core Version Restore
- 성공 Recipe·DNA·거절 이유 보존
- PM3 기능을 PM6 실제 고객 결과물에서 다시 검증

남은 실제 구현·검증:

- PM4 Collector가 Core에서 기존 자산을 우선 검색하고 필요할 때만 외부 조사
- PM5 Spec Adapter·Intent Packet·Scope Lock의 Core Runtime 연결
- 선택된 Reference에서 7축 Design DNA 자동 추출
- 편집기 변경을 V2 Design Recipe Diff로 저장하는 Core 연결
- 승인 Recipe→Antigravity 구현→Codex Fidelity→사용자 승인→Restore 전체 E2E

## 보존

Core MVP M1~M7, PM1·PM2 잠금, 실패 Pilot, 기존 Run·Artifact의 당시 판정은 변경하지
않았습니다. 새 계약은 과거 증거가 검증하지 않은 기능을 PASS로 확대하지 않습니다.
