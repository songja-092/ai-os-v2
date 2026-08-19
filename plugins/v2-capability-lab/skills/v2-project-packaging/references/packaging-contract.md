# 프로젝트 패키징 계약

필수 산출물:

- `source`: 원본 경로, Git HEAD, 원본 상태 Hash
- `preview`: 격리 Entry와 실행 조건
- `manifest`: Module ID, Version, Slot, 권한, Health
- `features`: 기능 ID, 쉬운 이름, `verified | unverified | fixture_only`
- `overlap`: 기존 Skill·Module 기능과 중복 여부
- `verification`: 실행, 상호작용, 오류 격리, Restore 결과
- `decision`: `candidate | adopted | held | discarded`

승격 조건:

1. 원본 불변
2. 실제 Preview 동작
3. 기능별 검증 상태 표시
4. Module 단독 오류 격리
5. 제거 후 Core·다른 Module 정상
6. 사용자 채택

페이지·문서·기능은 기본적으로 Module이 아니다. 독립적인 생명주기, 상태, 권한, 오류 격리와 재사용 가치가 증명될 때만 별도 Module 후보로 분리한다.
