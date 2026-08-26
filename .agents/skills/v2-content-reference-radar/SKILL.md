---
name: v2-content-reference-radar
description: "Collect and rank public Instagram card news, carousel posts, and Threads posts as project-ready references for AI OS V2, then preserve user adopt/hold/discard decisions. Use Shorts and Reels only for an explicit marketing-video request; do not use for automatic posting, private feeds, or product implementation."
---

# V2 콘텐츠 Reference 레이더

프로젝트 명세에 맞는 공개 콘텐츠 후보를 찾아 사용자가 시험할 수 있는 Reference로 정리한다.
이 Skill은 콘텐츠를 자동 제작하거나 게시하지 않는다.

## 시작 조건

- Interview Receipt 또는 Spec Lite에서 `주제`, `대상`, `만들 결과`, `플랫폼`을 읽는다.
- 결과를 크게 바꾸는 정보가 없을 때만 사용자에게 쉬운 말로 한 가지씩 묻는다.
- 기존 채택 채널과 채택 Reference를 먼저 확인하고 부족할 때만 새로 탐색한다.

## 수집 역할

- YouTube: `pm4-artifacts/content-reference-radar-v1/coding-channel-seeds.json`의 공식 채널
  Feed를 먼저 확인한다. 연결된 채널마다 관련 후보 한 건을 먼저 배치한 뒤 최신 후보로
  채우며, 한 채널의 게시 빈도가 전체 결과를 독점하지 않게 한다.
- YouTube 기본 Reference 모드에서는 Shorts를 제외하고 설명·사례 영상만 사용한다.
  Shorts는 `marketer_video` 요청에서만 수집한다.
- 기본 Reference 탐색: Instagram 카드뉴스·슬라이드 게시물과 Threads 공개 글을 우선한다.
- 마케터 역할: 사용자가 Shorts·Reels·영상 마케팅을 요청한 경우에만 YouTube Shorts와 Instagram
  Reels를 우선한다. 영상 후보를 기본 Reference 목록에 섞지 않는다.
- Instagram: 사용자가 로그인한 격리 Browser Adapter에서 공개 게시물만 본다. 마케터 역할일 때만
  영상 후보 상세 화면에 표시된 공개 좋아요·댓글·리포스트를 순위 입력으로 사용한다.
- Threads: 공개 검색이 열리면 로그인 없이 공개 글을 읽고, 막힐 때만 사용자가 로그인한 Browser
  Adapter를 사용한다. 반응 숫자의 지표 이름이 화면에 표시되지 않으면 원시 순서만 보존하고 순위화하지 않는다.
- 개인 메시지, 연락처, 비공개 게시물, 비공개 프로젝트 자료는 수집하지 않는다.
- Cookie·Token·Browser Profile은 Artifact나 Git에 저장하지 않는다.
- 로그인 만료·CAPTCHA·접근 제한은 우회하지 않고 `BLOCKED`로 남긴다.

## 후보 판정

1. 원문 URL·작성자·게시일·공개 수치를 증거로 보존한다.
2. 조회수나 좋아요가 보이지 않으면 추정하지 않는다.
3. 같은 플랫폼 안에서만 반응 속도와 최근성을 비교한다. 플랫폼 간 원시 조회수를 직접 비교하지 않는다.
4. 점수와 프로젝트 적합성을 분리한다. 인기 있어도 명세와 맞지 않으면 추천하지 않는다.
5. 중복 URL과 같은 게시물은 제거하고, 플랫폼 편중 없이 최대 10개만 보여준다.
6. 각 후보에 한글로 `내용`, `참고할 형식`, `공개 근거`, `원문 링크`를 표시한다.

결정형 순위 계산이 필요하면 `scripts/rank_candidates.py`를 사용한다. 입력·출력 계약은
[references/candidate-contract.md](references/candidate-contract.md)를 따른다.

## V2 연결

```text
Interview·Spec
→ 플랫폼별 공개 자료 수집
→ 증거 있는 항목만 순위화
→ 상위 후보 최대 10개
→ 사용자 채택·보류·폐기
→ 채택 후보만 프로젝트 Reference Handoff
```

- 자동 채택·자동 제품 적용·자동 게시를 금지한다.
- 모드를 `reference_default` 또는 `marketer_video`로 기록한다. 명시가 없으면 `reference_default`다.
- 사용자 판정은 기존 PM4 Core 상태 경로에 보존한다.
- 채택 Handoff에는 원문과 참고할 요소를 남기되 원본 콘텐츠 복제를 지시하지 않는다.
- 한 번의 Fixture 성공을 범용 Runtime PASS로 표현하지 않는다.
- 채널 Feed가 열렸다는 사실과 해당 채널에서 현재 명세에 맞는 후보가 발견됐다는 사실을
  분리한다. 연결됐지만 관련 후보가 없으면 후보 수를 꾸며내지 않는다.

주제가 입력되면 `plugins/v2-capability-lab/scripts/pm4_evidence_router.py`로 필요한 증거를
`화면과 표현 방식`, `실제 사용 방식과 반응`, `구현 재료`, `공식 기능과 제한`으로 나눈다.
모든 플랫폼을 강제로 실행하지 않고 해당 증거를 가진 기존 Adapter만 선택한다. 각 증거 종류를
최소 한 건씩 먼저 보여준 뒤 순환 배치하며, 결과가 없거나 Artifact가 없으면 `NOT_PROVEN`으로
남긴다. 빠르게 변하는 주제는 최근 30일을 기본으로 하고 부족할 때는 플랫폼·인접 검색어를 먼저
확장한다. 1년 범위로 자동 확장하지 않는다.

## 원본 연구 경계

`haeun2525/trend-radar`의 공개 설명에서 최근 반응 속도 중심 선별과 로컬 로그인 Profile 개념만
참고했다. 해당 저장소는 확인 시점에 명시적 라이선스가 없으므로 소스 코드를 복사·수정·배포하지
않는다. V2 구현은 기존 V2 Adapter와 독립 작성 코드만 사용한다.
