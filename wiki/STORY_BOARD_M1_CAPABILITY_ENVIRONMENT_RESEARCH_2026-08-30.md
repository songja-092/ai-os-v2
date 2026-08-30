# 스토리 보드 M1 Capability·환경 조사 — 2026-08-30

상태: `environment_ready_for_fixture / external_candidates_not_installed`

## 결론

M1 Fixture에는 새 패키지 설치가 필요하지 않습니다. 현재 Workspace Bundle에 PPTX 생성용
`@oai/artifact-tool`, 전체 Slide 렌더러, Montage, Overflow 검사기와 Headless `soffice`가 있습니다.
이를 먼저 사용해 `Story Profile·Scene → PPTX → Render → Overflow` 경로를 검증합니다.

PPTX Import는 단순 내용 추출과 원본 구조 보존을 분리합니다. 첫 Fixture에서는 OOXML Package를
읽기 전용으로 검사하고 원본 Hash를 보존합니다. 복잡한 SmartArt·Chart·수식·영상은 지원으로 위장하지
않고 `unsupported_or_preserve_only` 경고를 생성합니다.

## 현재 환경

| 역할 | 부품 | 판정 |
|---|---|---|
| PPTX 생성 | Workspace Bundle `@oai/artifact-tool` | `available / fixture_candidate` |
| Slide 렌더 | Presentations Skill `render_slides.py` | `available / fixture_candidate` |
| 전체 흐름 확인 | `create_montage.py` | `available / review_only` |
| Overflow 검사 | `slides_test.py` | `available / fixture_candidate` |
| Headless 변환 | Bundle `soffice` | `available / fidelity_must_be_tested` |
| Core 상태·복구 | 기존 V2 Run·Git·Verifier | `available / reuse_required` |

환경 경로는 시스템에 고정하지 않고 Workspace Dependency Loader의 반환값을 Run마다 사용합니다.
Bundle 외부의 전역 Node·Python Package를 자동 설치하지 않습니다.

## 외부 Skill·오픈소스 후보

| 후보 | 적합 역할 | 장점 | 한계·판정 |
|---|---|---|---|
| Microsoft Open XML SDK | PPTX Package·Part 정밀 검사 | OOXML 저수준 API·Validation, MIT | 고수준 디자인 엔진 아님·.NET 필요. `candidate_not_installed` |
| Apache POI XSLF | PPTX 읽기·그림·텍스트 | Java 기반 읽기·생성·수정 | 공식 문서가 초기 개발·호환 변경 가능으로 설명. `comparison_candidate` |
| PptxGenJS | JS 기반 PPTX Export | Node·Browser에서 생성 | Import 원본 보존 도구가 아님. `candidate_not_installed` |
| LibreOffice/soffice | Headless 렌더·PDF 변환 | 현재 환경에 존재 | PowerPoint와 표현 차이 가능. Fidelity 기준 원본으로 사용 금지 |

공식 근거:

- https://github.com/dotnet/Open-XML-SDK
- https://learn.microsoft.com/en-us/office/open-xml/about-the-open-xml-sdk
- https://poi.apache.org/components/slideshow/index.html
- https://poi.apache.org/components/slideshow/xslf-cookbook.html
- https://github.com/gitbrent/PptxGenJS
- https://help.libreoffice.org/latest/en-US/text/shared/guide/start_parameters.html

## M1 Capability Lab 순서

1. 작은 가상 PPTX 생성
2. 원본 SHA-256 기록
3. OOXML Part·Slide·Text·Image·Notes·관계 목록 추출
4. Story Profile·Scene Draft 생성
5. `extract_content / preserve_and_polish / restructure` 비교
6. `export_storyboard`로 새 PPTX 생성
7. 모든 Slide 렌더·개별 시각 확인·Overflow 검사
8. 원본 Hash 불변·손실 경고·실패·Restore 검사
9. 번들 방식이 부족하다는 증거가 있을 때만 외부 후보 격리 설치 승인 요청

## 금지

- 원본 PPTX 덮어쓰기
- 지원하지 않는 요소를 조용히 삭제
- 렌더 성공만으로 PowerPoint Fidelity PASS 선언
- License·고정 Version·실패 Fixture 없이 Package 설치
- Story Profile보다 PPTX를 내부 상태 원본으로 사용
