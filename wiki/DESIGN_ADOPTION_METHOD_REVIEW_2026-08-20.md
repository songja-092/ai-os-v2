# 디자인 탐색·채택 방식 검토 — 2026-08-20

## 결론

V2의 흐름은 현재 널리 쓰이는 디자인 사고방식과 방향이 같습니다. 다만 모든 조직이 같은 도구나 순서를 쓰는 것은 아니며, V2만의 이름인 `디자인 총괄`, `Visual Target`, `Design Recipe`를 업계 표준 제품명처럼 표현하면 안 됩니다.

## 보편적인 흐름과 V2 대응

| 보편적 단계 | V2 방식 |
|---|---|
| 사용자·문제 이해 | 쉬운 요청과 제작 Brief |
| 사례 조사·영감 수집 | 성공 Recipe 우선 검색, 부족할 때 Reference 조사 |
| 문제와 방향 정의 | 디자인 총괄이 목적·정보 우선순위·제외 요소 정리 |
| 서로 다른 방향 탐색 | 공급원별 방향 비교와 전체·부분 선택 |
| Prototype·Feedback | 실제 데이터 Visual Target 하나와 사용자 승인 |
| 규칙·Component 정리 | Draft Design Recipe를 승인 Version으로 승격 |
| 구현·검증·반복 | 별도 구현·마감·최종 승인·Version·Restore |

Design Council의 Double Diamond는 `Discover·Define·Develop·Deliver`로 탐색과 수렴을 반복합니다. IBM Enterprise Design Thinking도 사용자 결과를 기준으로 관찰·성찰·제작을 반복하고 Playback을 통해 진행 중인 결과를 사용자와 확인합니다. 따라서 V2가 Reference를 모은 뒤 총괄 방향을 정하고 실제 화면으로 확인하는 구조는 검증된 큰 흐름과 맞습니다.

## V2에서 유지할 차별점

- 기존 성공 Recipe·Block으로 해결되면 수집기를 실행하지 않습니다.
- 사용자는 전문용어보다 이미지·마우스·간단한 선택으로 결정합니다.
- 여러 완성 시안을 반복 생성하지 않고 방향 비교 후 실제 데이터 Visual Target 하나를 제작합니다.
- Reference의 전체 화면을 복제하지 않고 Section과 적용 속성을 기록합니다.
- 사용자가 선택하지 않은 색상·문구·Logo·브랜드 자산은 잠급니다.
- 실패·보류·채택 이유와 Version·Restore 지점을 보존합니다.

## 디자인 탐색부터 채택까지 권장 최종 흐름

```text
사용자 요청
→ 제작 Brief 확인
→ 기존 성공 Recipe·Block 검색
→ 부족할 때만 실제 Reference 제한 조사
→ 디자인 총괄이 구조적으로 다른 방향 2~3개 정리
→ 사용자가 전체 또는 Section 선택
→ 선택·제외·출처를 Draft Design Recipe로 기록
→ 실제 데이터가 들어간 Visual Target 하나 제작
→ 사용성·접근성·구현 가능성 사전 검사
→ 사용자 채택 · 부분 수정 · 다른 방향 · 현재안 유지 · 중단
→ 채택 시 Recipe 승인 Version과 성공 근거 저장
```

`UI Remix` 연구는 실제 UI 사례를 검색하고 전체·Component 수준으로 선택·적용하는 방식이 비전문가의 목표 달성과 반복 탐색에 도움을 줄 수 있음을 24명 연구로 보였습니다. `Misty` 연구는 Screenshot의 특정 구역과 Layout·Color·Content 같은 속성을 선택해 현재 UI에 적용하고 Semantic Diff로 조절하는 방식을 14명의 Frontend 개발자와 시험했습니다. 둘 다 유용한 근거지만 V2 전체 성공을 증명한 것은 아니므로, 사용자가 부담스럽다고 판정한 대형 Reference Board를 기본 화면으로 되살리지 않습니다.

## 디자인을 더 잘하기 위해 추가할 방법

1. **한 명의 결정권자**: 디자인 총괄이 Reference를 모으는 사람이 아니라 프로젝트 인상·정보 우선순위·금지 요소를 일관되게 결정합니다.
2. **실제 내용으로 일찍 확인**: 빈 Wireframe보다 실제 제목·이미지 길이·상태가 들어간 Visual Target을 사용합니다.
3. **구조적으로 다른 방향만 비교**: 색상만 다른 3안은 만들지 않습니다. 정보 구조·밀도·이미지·Motion 가설이 달라야 합니다.
4. **사용자 작업으로 평가**: 예쁜지뿐 아니라 사용자가 핵심 행동을 찾고 완료하는지 확인합니다.
5. **정기 Playback**: 완성 직전에만 묻지 않고 방향·실제 Preview·마감의 세 지점에서 짧게 확인합니다.
6. **성공 자산만 축적**: 채택되고 실제 결과까지 검증된 Recipe·Block만 다음 프로젝트의 기본 재료로 승격합니다.
7. **기술 PASS와 디자인 PASS 분리**: Build·접근성·회귀검사와 정보 우선순위·마감·사용자 시각 승인을 따로 판정합니다.

## 현재 한계

이 방식이 최신 연구와 산업 방법에 정합하다는 것은 확인했지만, V2가 자동으로 디자인 회사 수준 결과를 반복 생산한다는 증거는 아닙니다. 서로 다른 실제 프로젝트에서 Reference 선택 정확도, 수정 횟수, 사용자 작업 성공, 구현 Fidelity와 복구를 반복 측정해야 합니다.

## 참고 자료

- Design Council, The Double Diamond: https://www.designcouncil.org.uk/resources/the-double-diamond/
- IBM, Enterprise Design Thinking Framework: https://www.ibm.com/training/enterprise-design-thinking/framework
- UI Remix, ACM IUI 2026: https://doi.org/10.1145/3742413.3789154
- Misty, ACM CHI 2025: https://doi.org/10.1145/3706598.3713924
