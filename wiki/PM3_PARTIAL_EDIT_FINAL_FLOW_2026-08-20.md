# PM3 부분수정 최종 흐름 — 2026-08-20

## 목적

PM1에서 승인한 디자인 방향과 PM2에서 잠근 Module 구조를 훼손하지 않고, 사용자가 마우스로 필요한 부분만 바꾸고 언제든 이전 상태로 돌아가게 합니다.

## 사용자에게 보이는 흐름

```text
수정할 화면 열기
→ PC 또는 모바일 선택
→ 바꿀 Section·Card 클릭
→ 마우스로 이동하거나 오른쪽 설정에서 값 변경
→ 변경 전후 Preview 확인
→ 계속 수정 · 적용 · 이번 수정 버리기 · 이전 Version 복구
```

기본 입력은 `Drag & Drop → 이동 버튼·Keyboard → Property Panel → 자연어` 순서입니다. 자연어는 보조 수단이며 같은 Recipe Diff로 변환할 수 있을 때만 사용합니다.

## 수정 가능한 범위

- Section·Card 순서와 Manifest가 허용한 Slot 이동
- 폭·높이·여백·글자 크기의 제한된 단계값
- Section·Card·강조 요소의 Color Token과 단색·투톤 Palette
- 이미지 Slot의 자산 교체와 표시·숨김
- Motion Preset의 없음·절제·표현적 선택과 강도 조절
- Manifest가 허용한 Module 인스턴스 복제
- 현재 Draft 배치에서 Section 제거와 Undo

코드·Registry·Manifest 자체 삭제, Core 필수 Module 제거, 허용 범위를 넘는 복제와 이동은 하지 않습니다.

## 내부 처리 순서

```text
승인된 Recipe Version 불러오기
→ 원본을 덮어쓰지 않고 새 Draft 생성
→ Viewport와 안정적인 Section ID 선택
→ 직접 조작을 Recipe Diff로 변환
→ 즉시 Preview와 넘침 경고 표시
→ Schema·권한·Slot·반응형·Motion·Reference Trace 검사
→ 사용자 적용 승인
→ 새 Recipe Version 저장
→ 필요 시 과거 Version을 복사한 새 Restore Draft 생성
```

모든 Diff에는 `target_section_id`, `target_viewport`, `property`, `before`, `after`, `source`를 기록합니다. PC 수정은 모바일 Override를 조용히 바꾸지 않습니다. 390px·430px은 별도 디자인이 아니라 하나의 모바일 규칙을 검증하는 Viewport입니다.

자동 정리는 Layout·줄바꿈·Palette 후보를 만드는 **Draft 제안**입니다. 사용자 확인 없이 실제 제품이나 승인 Version에 적용하지 않습니다.

## 적용 전 필수 확인

- 선택하지 않은 Section의 값이 유지됨
- Desktop·Mobile Override가 의도대로 분리됨
- Text·Image Overflow가 없거나 경고가 표시됨
- Motion이 목적을 가지며 `prefers-reduced-motion` 경로가 존재함
- Reference 공급원·적용 Section·Trial Hash 추적이 유지됨
- 변경 전후 Preview가 같은 데이터·Viewport·상태에서 비교됨
- 적용 뒤 새 Version과 Restore 지점이 존재함

## 현재 검증 상태

- 카드 3개 격리 Pilot에서 순서·크기·글씨 독립성·넘침 경고·PC/모바일 분리·Undo를 확인했습니다.
- Puck과 React Grid Layout 모드 전환, 이미지 Slot, 단색·투톤 Palette, 자동 Layout·줄바꿈 Draft를 확인했습니다.
- 여러 채택 공급원을 하나의 Draft Recipe와 HTML Section에 연결하고 SHA-256을 대조했습니다.
- 실제 병원 웹 전체 Section 적용, PM3 수정 뒤 Reference 방향 보존, Core Registry 승격, 고객 제품 자동 적용은 아직 증명하지 않았습니다.

## PM3 완료 조건

위 흐름을 실제 고객 결과물 하나에 적용하고, 선택하지 않은 영역 보존·PC/모바일 회귀·Reference Trace·새 Version·Restore를 모두 확인한 뒤 사용자가 PASS해야 합니다.
