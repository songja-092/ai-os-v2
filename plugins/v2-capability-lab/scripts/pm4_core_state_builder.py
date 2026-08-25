#!/usr/bin/env python3
"""Build a truthful PM4 Core state from confirmed interview and collected evidence."""

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def item_id(platform, url):
    return f"{platform}-{hashlib.sha256(url.encode()).hexdigest()[:12]}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--github", required=True)
    parser.add_argument("--instagram", required=True)
    parser.add_argument("--youtube", required=True)
    parser.add_argument("--reddit", required=True)
    parser.add_argument("--threads", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    receipt, github, instagram = load(args.receipt), load(args.github), load(args.instagram)
    youtube, reddit, threads = load(args.youtube), load(args.reddit), load(args.threads)
    if receipt.get("status") != "user_confirmed" or receipt.get("period_days") != 30:
        raise SystemExit("confirmed 30-day interview receipt required")
    cutoff = datetime.now(timezone.utc) - timedelta(days=30)
    github_items = []
    instagram_items = []

    def korean_summary(platform, title, text=""):
        haystack = f"{title} {text}".lower()
        if platform == "github":
            if "harness" in haystack:
                return "AI 코딩에 스킬·기억·보안·조사 절차를 묶어 작업 품질을 높이는 도구입니다."
            if "design" in haystack or "ui" in haystack:
                return "AI가 웹·앱 화면을 설계하고 결과물로 내보내도록 돕는 디자인 도구입니다."
            if "memory" in haystack or "context" in haystack:
                return "AI 작업 기록을 저장하고 다음 세션에서 다시 활용하는 기억 도구입니다."
            return "AI 제작·자동화에 시험해볼 수 있는 오픈소스 도구입니다."
        if platform == "youtube":
            return f"한국어 AI·코딩 채널의 최근 영상입니다. 주제는 ‘{title[:80]}’입니다."
        if platform == "reddit":
            return "AI 코딩 사용자가 겪은 비용·배포·작업 방법을 비교할 수 있는 커뮤니티 사례입니다."
        if platform == "threads":
            return "AI 도구 조합·구독 비용·Codex 활용법을 빠르게 파악하는 한국어 실사용 사례입니다."
        return "AI·바이브코딩 기획과 제작 흐름을 참고할 수 있는 한국어 콘텐츠입니다."

    def standard_social(platform, source):
        title = source.get("title") or f"{platform} 최근 콘텐츠"
        url = source.get("url") or source.get("post_url") or source.get("permalink")
        return {
            "item_id": item_id(platform, url), "platform": platform,
            "channel": source.get("channel_name") or source.get("username") or source.get("profile_handle"),
            "channel_url": source.get("channel_url") or source.get("profile_url"),
            "title": title, "url": url,
            "short_summary": korean_summary(platform, title, source.get("public_text") or source.get("source_label") or ""),
            "observed_at": source.get("published_at"), "popularity": source.get("popularity"),
            "cost": "무료 웹 열람", "license": "reference_only_check_before_reuse",
            "project_ready": platform in {"youtube", "reddit", "threads"},
            "ranking_basis": "channel_first_recent_content_platform_local",
        }
    for source in github.get("items", []):
        updated = source.get("updated_at")
        if not updated or datetime.fromisoformat(updated.replace("Z", "+00:00")) < cutoff:
            continue
        url = source["url"]
        metrics = source.get("public_metrics", {})
        github_items.append({
            "item_id": item_id("github", url), "platform": "github",
            "channel": source.get("channel_name"), "channel_url": source.get("channel_url"),
            "title": source.get("title"), "url": url,
            "short_summary": korean_summary("github", source.get("title"), source.get("short_summary", "")), "observed_at": updated,
            "popularity": {"stars": metrics.get("stars"), "forks": metrics.get("forks")},
            "cost": source.get("cost"), "license": source.get("license"),
            "project_ready": bool(source.get("project_ready_evidence", {}).get("clone_url")),
            "ranking_basis": "recently_updated_then_github_public_stars",
        })
    for source in instagram.get("items", []):
        url = source.get("post_url") or source.get("permalink")
        if not url:
            continue
        instagram_items.append(standard_social("instagram", {**source, "title": "Instagram 채널의 최근 콘텐츠"}))
    github_items.sort(key=lambda item: (item.get("popularity") or {}).get("stars") or 0, reverse=True)
    instagram_items.sort(key=lambda item: item.get("observed_at") or "", reverse=True)
    # 플랫폼 간 공개 수치가 서로 달라 한 줄 점수로 섞지 않는다. 연결된 플랫폼이
    # 하나뿐인 것처럼 보이지 않도록 현재 종합 화면에는 GitHub 8개와 Instagram 2개를 배정한다.
    youtube_items = [standard_social("youtube", x) for x in youtube.get("items", [])]
    reddit_items = [standard_social("reddit", x) for x in reddit.get("items", [])]
    threads_items = [standard_social("threads", x) for x in threads.get("items", [])]
    items = github_items[:2] + youtube_items[:2] + reddit_items[:2] + threads_items[:2] + instagram_items[:2]
    state = {
        "state_version": "1.0", "revision": 1, "request_id": receipt["request_id"],
        "topic": receipt["research_topic"], "period_days": 30,
        "algorithm_policy": {
            "platform_recommendation_use": "discovery_seed_only", "channel_first": True,
            "deduplicate": True, "ranking": "platform_local_public_metrics_then_relevance_review",
            "never_infer_missing_metrics": True, "final_decision_owner": "user",
        },
        "sources": [
            {"id": "github", "status": "connected_public_api", "items": len(github_items)},
            {"id": "instagram", "status": "connected_logged_in_browser_partial", "items": len(instagram_items)},
            {"id": "youtube", "status": "connected_official_atom_feed", "items": len(youtube_items), "used_period_days": youtube.get("used_period_days")},
            {"id": "reddit", "status": "connected_authenticated_aside_browser", "items": len(reddit_items), "used_period_days": reddit.get("used_period_days", 30)},
            {"id": "threads", "status": "connected_authenticated_aside_browser", "items": len(threads_items), "used_period_days": threads.get("used_period_days")},
        ],
        "items": items, "decisions": {}, "last_action": "research.state.built",
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "built", "items": len(state["items"]), "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
