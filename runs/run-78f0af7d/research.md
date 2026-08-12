# 조사 결과

## 공식 자료

### 확인된 사실

- FullCalendar 공식 Touch Support 문서는 터치 기기에서 장기 누르기로 이벤트 이동과 크기 변경을 시작할 수 있다고 명시한다. `longPressDelay`와 `eventLongPressDelay`로 대기 시간을 조정할 수 있다. https://fullcalendar.io/docs/touch
- 공식 `eventResizableFromStart` 문서는 이벤트의 시작 가장자리를 크기 변경할 수 있으며 기본값은 `false`라고 설명한다. 시작일과 종료일 양쪽을 바꾸려면 이 옵션과 이벤트 편집 기능을 함께 켜야 한다. https://fullcalendar.io/docs/eventResizableFromStart
- 공식 `eventResize` 문서는 변경 뒤의 이벤트, 변경 전 이벤트, 시작·종료 변화량과 `revert()`를 제공한다. 저장 실패 또는 유효하지 않은 날짜일 때 화면 변경을 되돌릴 수 있다. https://fullcalendar.io/docs/eventResize
- 공식 Plugin Index에 따르면 무료 Standard의 `/daygrid`가 월 달력을, `/interaction`이 이벤트 드래그와 크기 변경을 제공한다. 공사별 자원 행이 있는 Gantt형 Timeline은 Premium이다. https://fullcalendar.io/docs/plugin-index
- 공식 Event Object 문서는 `end`가 배타적이라고 명시한다. 예를 들어 화면에서 9월 2일까지 보이는 막대의 내부 종료 값은 9월 3일이다. 저장 형식에서 이 차이를 명시적으로 변환해야 한다. https://fullcalendar.io/docs/event-object
- FullCalendar Standard 비프리미엄 플러그인은 MIT 라이선스다. https://fullcalendar.io/license

### 한계

- 공식 지원이 있다는 사실은 이 대상 프로젝트와 Galaxy/iPhone 실기기에서 터치 조작이 검증됐다는 뜻이 아니다.
- 월 달력의 좁은 날짜 칸에서는 양끝 손잡이가 작아질 수 있고, 장기 누르기와 세로 스크롤이 경쟁할 수 있다.
- 공정별 행과 가로 시간축을 가진 전문 Gantt/Resource Timeline 화면은 무료 Standard 범위가 아니다. 이번 요청은 먼저 월 달력의 기간 막대로 제한하는 것이 안전하다.

## GitHub

### 확인된 사실

- 공식 저장소는 `fullcalendar/fullcalendar`이며 JavaScript용 드래그·드롭 이벤트 달력으로 유지되고 있다. https://github.com/fullcalendar/fullcalendar
- 공식 Releases에는 최신 릴리스와 6.x 유지 릴리스가 함께 게시되어 있어 방치된 저장소로 보이지 않는다. 확인 당시 최신 표시는 `v7.0.2`였다. https://github.com/fullcalendar/fullcalendar/releases
- 공식 변경 기록에는 터치 장기 누르기 기반 이동·크기 변경 도입, 터치 선택 영역 개선, 터치 크기 변경 중 선택 유실 수정 같은 실제 수정 이력이 있다. https://github.com/fullcalendar/fullcalendar/blob/main/CHANGELOG.md

### 대상 프로젝트 확인

- 대상 Git 기준점은 `master`의 `c9703520ff9a7a6ce95f64918ada4ce08160175d`이며 수집 시 작업트리 변경이 없었다.
- 실제 앱은 Vite + TypeScript의 순수 브라우저 앱이다. 설치된 직접 의존성은 `typescript`, `vite`뿐이며 달력 패키지는 없다.
- 현재 코드는 병원 소개·예약 요청 화면이며 공사 일정 자료 구조, 달력 화면, 기간 막대 편집, 영구 저장 기능이 없다.
- V2 Wiki와 기존 Run에서 달력 기간 막대와 터치 양끝 변경을 실제 환경에서 검증한 레시피는 발견되지 않았다. 따라서 이번 결과는 `researched`이며 검증 레시피가 아니다.

## 성공·실패 사례

### 성공 근거

- 공식 Touch Support와 `eventResize` 문서는 터치 장기 누르기 후 크기 변경 및 변경 결과 처리 흐름을 제품 기능으로 제공한다. 이는 최소 Preview를 만들 수 있다는 직접 근거다. https://fullcalendar.io/docs/touch https://fullcalendar.io/docs/eventResize
- 공식 변경 기록은 과거 터치 크기 변경 문제를 릴리스에서 수정한 내역을 남긴다. 기능이 단순 예제가 아니라 테스트와 유지보수 대상임을 보여준다. https://github.com/fullcalendar/fullcalendar/blob/main/CHANGELOG.md

### 실패·주의 근거

- 같은 변경 기록에는 `Resizing on touch devices loses selection (#5706)` 같은 실제 실패와 수정 이력이 있다. 터치 크기 변경은 브라우저·버전 회귀 가능성이 있으므로 390px/430px와 실제 Android/iOS에서 확인해야 한다. https://github.com/fullcalendar/fullcalendar/blob/main/CHANGELOG.md
- 월 달력에서 일정이 많으면 `+more`로 접히거나 여러 날짜 기간 막대가 잘릴 수 있다. 공식 `dayMaxEventRows`와 `eventSlicing` 문서도 이 동작을 별도 옵션으로 다룬다. https://fullcalendar.io/docs/dayMaxEventRows https://fullcalendar.io/docs/eventSlicing
- 대안으로 Mobiscroll Eventcalendar는 공식 문서에서 마우스와 터치로 양끝 크기 변경을 직접 지원하지만 상용 제품이며, 현재 프로젝트에 없는 의존성과 라이선스 결정을 추가한다. 무료 Standard로 요청을 충족할 수 있으므로 최종 추천에서는 제외한다. https://demo.mobiscroll.com/docs/javascript/eventcalendar/drag-and-drop/

## 확인 일자

- 2026-08-12 (Asia/Seoul)
- 소스의 현재 상태는 이 날짜에 확인했다. 이후 버전·가격·라이선스·브라우저 동작은 Preview 직전에 다시 확인해야 한다.
