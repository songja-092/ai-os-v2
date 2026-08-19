---
name: v2-project-packaging
description: "이미 제작된 로컬 프로젝트 결과물을 AI OS V2의 제거 가능한 Module 후보로 포장하고 격리 Preview·기능 목록·검증 초안을 만든다. 새 제품 제작이나 사용자 승인 없는 Core Registry 등록에는 사용하지 않는다."
---

# 프로젝트 패키징

이미 만들어진 프로젝트 결과를 V2 보드에서 열 수 있는 Module 후보로 바꾼다. 원본 제품과 Git 상태는 수정하지 않는다.

## 처리 순서

1. 원본 경로와 프로젝트 이름을 확인한다.
2. `scripts/project_packaging.py inspect`로 공개 가능한 파일 구조와 실행 후보만 읽는다.
3. 기능은 파일명만으로 완료 판정하지 않는다. 실제 Preview에서 확인된 기능만 `verified`, 나머지는 `unverified`로 기록한다.
4. Module Manifest 초안, 기능 목록, 원본 Hash, 격리 Preview 경로를 만든다.
5. V2 Core에 등록하기 전에 원본 불변·Preview 실행·오류 격리·금지 Action을 검사한다.
6. 사용자에게 `채택`, `보류`, `폐기`만 요청한다.
7. `채택` 후에만 Core Registry에 연결한다. Registry 등록과 Commit은 별도 사용자 승인 범위로 취급한다.

## 반드시 지킬 경계

- 프로젝트는 Module 후보이고 V2는 Module을 장착하는 보드다.
- 프로젝트 하나에는 기본 Preview 하나를 둔다. 여러 페이지와 기능은 같은 Module 내부에서 관리한다.
- `.git`, `.env`, Token, Cookie, SSH Key, 브라우저 프로필은 읽거나 패키지에 넣지 않는다.
- 외부 전송·패키지 설치·원본 변경·자동 채택을 하지 않는다.
- 기존 Module과 중복되는 기능은 새 기능처럼 표시하지 않고 `overlap`에 기록한다.
- 스크립트 출력은 초안이며 작동 증거가 아니다.

Manifest와 판정 필드는 [패키징 계약](references/packaging-contract.md)을 따른다.
