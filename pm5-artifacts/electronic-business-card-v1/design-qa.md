# PM5 전자명함 Design QA

- source visual truth: `pm4-artifacts/project-collector-mvp-v1/design-candidates/direction-2-full-flow-visual-target.png`
- source pixels: 1536 × 1024
- implementation: `http://127.0.0.1:8228/pm5-scope-review.html`
- implementation capture: `pm5-artifacts/electronic-business-card-v1/implementation-1440.png`
- combined comparison: `pm5-artifacts/electronic-business-card-v1/design-qa-comparison.png`
- viewport: 1440 × 1000 CSS px, browser density 1
- state: PM5 test fixture, approval pending

## Full-view comparison

- 승인 시안의 흰색 바탕, 검정 하단, 라임 강조, 세로형 화면, 4열 비교 구성을 유지했습니다.
- 승인된 `direction-2.png` 인물과 전체 흐름 시안의 QR 영역을 실제 이미지 자산으로 사용했습니다.
- PM4 화면 8개 뒤에 PM5 파생 화면인 `9. 최종 완료`를 추가했습니다.

## Focused region comparison

- 메인 프로필: 최초 구현의 작은 얼굴형 이미지를 큰 상반신 중심 이미지로 수정했습니다.
- QR·NFC: 임시 CSS 무늬를 제거하고 승인 시안 QR 자산으로 교체했습니다.
- 프로필·사진 편집: 동일한 승인 인물 자산을 사용해 화면 간 인물 불일치를 제거했습니다.
- 완료 화면: 검정 바탕과 라임 완료 표시를 사용해 기존 디자인 언어를 유지했습니다.

## Fidelity surfaces

- Fonts and typography: 시스템 한글 글꼴을 사용하며 굵은 제목·작은 설명의 위계가 승인 시안과 일치합니다.
- Spacing and layout rhythm: 데스크톱 4열, 중간 2열, 모바일 1열로 구성하고 세로형 카드 비율을 유지합니다.
- Colors and visual tokens: 흰색·검정·라임을 공통 Token으로 사용합니다.
- Image quality and asset fidelity: 승인된 PNG 원본을 직접 사용하며 임시 인물·QR 도형은 제거했습니다.
- Copy and content: PM4에서 승인한 사회복지사 전자명함 문구와 테스트 정보를 사용합니다.

## Comparison history

1. P1 — 최초 화면은 인물과 QR이 임시 도형이었고 카드 밀도가 승인 시안과 달랐습니다.
2. Fix — PM4 승인 이미지 두 개에 제한된 읽기 경로를 연결하고 4열·세로형 화면으로 수정했습니다.
3. P2 — 메인 인물이 얼굴 중심으로 작게 잘렸습니다.
4. Fix — 메인 화면만 큰 상반신 구도로 바꾸고 다른 화면의 프로필 구도는 유지했습니다.

## User-found regression

- P1: 1번 인물 이미지가 잘렸습니다.
- P1: 3번 QR이 잘렸습니다.
- P1: 6번 정보 편집의 인물 뒤에 원본 화면 배경이 함께 보였습니다.
- P1: 8번 테마·행동 순서가 무엇을 바꾸는지 설명되지 않았습니다.
- P1: 9번 완료 화면이 승인된 Visual Target 없이 텍스트 카드로 임의 제작됐습니다.

기존 `passed` 판정은 기능 PASS를 디자인 PASS로 잘못 확대했으므로 취소했습니다.

## Post-fix comparison

- 1번: 동적 CSS Crop을 제거하고 PM4에서 승인된 메인 프로필 Visual Target 전체를 표시했습니다.
- 3번: QR을 별도 205 × 205 승인 Crop 자산으로 분리해 네 모서리와 코드 전체가 보이도록 수정했습니다.
- 6·7번: 원본 화면 배경이 섞이지 않는 520 × 520 인물 자산을 사용했습니다.
- 8번: 대표 색상이 메인 화면·주요 버튼에 적용되고, 행동 순서가 메인 화면의 연락 버튼 순서를 정한다는 설명을 추가했습니다.
- 9번: 기존 텍스트 완료 카드를 제거하고 1~8번 디자인 언어로 생성한 별도 완료 Visual Target을 연결했습니다.
- 수정 후 결합 비교 증거는 `design-qa-comparison-fixed.png`입니다.

## Verification

- 9개 화면 DOM 표시 PASS
- 승인·파생 이미지 6개 로딩 PASS
- PM5 입력·복원 Runtime PASS
- PM4 잠금 Hash 보존 PASS
- 제품 변경·배포 없음

## Latest user review

- P1: 4번과 6번의 작은 원형 얼굴 Crop이 부자연스럽습니다.
- P1: QR 배경과 카드의 중심·대칭이 맞지 않습니다.
- P1: 8번은 설명만 있고 실제 테마 변경 Runtime이 연결되지 않았습니다.

기능 연결 PASS는 유지하지만 시각 품질과 테마 동작은 아직 증명되지 않았습니다.

## Latest repair evidence

- 4·6번: 작은 원형 Crop 대신 545 × 715 상반신 비율 자산과 직사각형 프레임을 사용했습니다.
- 3번: QR을 흰색 정사각형 Quiet Zone 안에 중앙 정렬했습니다.
- 8번: 실제 Runtime 미연결 상태를 화면에 명시해 동작하는 기능처럼 보이지 않게 했습니다.
- 새 자산은 재시작한 Runtime에서 원본 Hash와 같은 파일로 응답했습니다.
- 기존 PM5 기능 Fixture는 재검증 PASS이며 PM4 잠금은 보존됐습니다.

사용자 시각 승인과 테마 변경 Runtime은 아직 남아 있으므로 디자인 PASS로 승격하지 않습니다.

final result: blocked
