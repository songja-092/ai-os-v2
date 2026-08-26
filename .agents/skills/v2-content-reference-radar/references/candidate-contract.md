# Candidate 계약

입력 JSON:

```json
{
  "request": "AI 바이브 코딩으로 수익화하는 콘텐츠",
  "items": [
    {
      "platform": "youtube",
      "url": "https://example.com/item",
      "author": "channel",
      "published_at": "2026-08-25T00:00:00Z",
      "title": "공개 제목",
      "summary_ko": "한글 내용 요약",
      "format_ko": "참고할 콘텐츠 형식",
      "metrics": {"views": 1000, "likes": 30, "comments": 4, "reposts": null},
      "relevance": 80
    }
  ]
}
```

- `relevance`는 명세와의 관련성 0~100이며 Analyzer가 근거와 함께 제공할 때만 사용한다.
- 보이지 않는 수치는 `null`로 둔다.
- `published_at`과 조회수·좋아요 중 하나가 없으면 인기순위는 `NOT_PROVEN`이다.

출력은 원본 항목, 플랫폼 내부 순위, 사용한 수치, 경고, `user_decision: null`을 보존한다.
상위 목록은 플랫폼별 최대 4개, 전체 최대 10개다.
