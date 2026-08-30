# 전자명함 실제 사용·배포 계약

이 문서는 전자명함 1차 시험 제품을 실제 정보와 공개 주소로 전환할 때 사용하는 제품 전용 기준입니다. 현재 Runtime은 사용자 승인 시험용 Fixture이며 실제 배포 완료 증거가 아닙니다.

## 권장 사용 방식

하나의 공개 HTTPS 주소를 문자·카카오톡·이메일·QR·NFC가 함께 사용합니다.

1. 전화 상담 후에는 상대에게 전송 의사를 확인하고 `명함 공유하기`로 보냅니다.
2. 대면 상황에서는 NFC 태그를 우선 사용하고 같은 위치에 QR을 함께 제공합니다.
3. 온라인 대화에서는 전자명함 주소를 직접 공유합니다.
4. 상대방은 전자명함에서 연락처 저장·전화·문자·이메일·웹 연결을 선택합니다.

권장 메시지:

```text
안녕하세요, 김하은 사회복지사입니다.
연락처와 업무 안내입니다.
https://card.example.com/haeun
```

모르는 번호의 수신 전화에 자동 문자를 보내지 않습니다. 오발송·스팸 인식·OS 권한·광고성 정보 규정 위험이 있으므로 사용자가 확인하고 전송하는 방식만 허용합니다.

## 문자에서 명함 이미지 제공

기본 경로는 공개 페이지의 Open Graph 이미지입니다. `og:title`, `og:description`, `og:image`를 서버가 반환하는 HTML에 직접 포함해 지원 메시지 앱에서 링크 미리보기를 표시합니다. JavaScript 실행에 의존하지 않습니다.

보조 경로는 `명함 이미지로 공유`입니다. 현재 프로필로 PNG를 생성하고 `navigator.canShare({files})`가 통과한 기기에서 시스템 공유창을 엽니다. 지원되지 않으면 문구와 링크만 공유합니다. 이미지에는 작은 QR을 포함할 수 있지만 공개 URL을 본문에도 유지합니다.

참조:

- Apple Messages Rich Preview: https://developer.apple.com/documentation/technotes/tn3156-create-rich-previews-for-messages
- Web Share API: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share
- Apple NFC Background Reading: https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading
- Android NFC: https://developer.android.com/develop/connectivity/nfc/nfc

## 실제 배포 순서

1. 시험용 이름·사진·기관·연락수단을 실제 정보로 교체합니다.
2. 공개할 개인정보와 선택 정보를 사용자가 승인합니다.
3. 한 사람용 정적 배포인지 여러 사용자용 로그인·데이터 저장 제품인지 범위를 선택합니다.
4. 공개 HTTPS 주소와 도메인을 확보합니다.
5. 페이지별 Open Graph 제목·설명·고해상도 미리보기 이미지를 생성합니다.
6. 공개 주소로 QR을 다시 생성하고 기존 시험 QR과 구분합니다.
7. 동일 공개 주소를 NDEF URL로 NFC 태그에 기록합니다.
8. iPhone·Android에서 링크·QR·NFC·연락처 저장·전화·문자·이메일을 실기기 검사합니다.
9. 배포 Version·Rollback·백업·오류 확인 경로를 기록합니다.
10. 실제 정보가 들어간 화면과 외부 연결을 사용자가 최종 승인한 뒤 배포합니다.

## 배포 Gate

- 로컬 주소 `127.0.0.1`로 QR·NFC를 최종 생성하지 않습니다.
- 공개 HTTPS 주소 전에는 Rich Preview·실제 QR·NFC를 `NOT_PROVEN`으로 기록합니다.
- 실제 정보 입력 전에는 현재 Fixture를 실사용 명함으로 표현하지 않습니다.
- 로그인·결제·분석·고객 관리 기능은 별도 범위 승인 없이 추가하지 않습니다.
- 자동 문자 발송과 자동 배포는 사용자 별도 승인 없이 구현하지 않습니다.

## 현재 상태

- 로컬 1차 제품: 기술 회귀 PASS
- 실제 개인정보: 시험 Fixture
- 공개 HTTPS 주소: NOT_PROVEN
- Rich Preview: NOT_PROVEN
- 공개 주소 QR·NFC: NOT_PROVEN
- 배포·운영·Rollback: NOT_PROVEN
- 사용자 최종 제품 승인: PENDING
