#!/usr/bin/env node
/** Rank collected public social posts without inventing unavailable metrics. */

import fs from "node:fs/promises";
import path from "node:path";

function parseArgs(argv) {
  const out = { limit: 10, days: 30 };
  for (let i = 2; i < argv.length; i += 1) {
    if (argv[i] === "--input") out.input = argv[++i];
    else if (argv[i] === "--output") out.output = argv[++i];
    else if (argv[i] === "--request") out.request = argv[++i];
    else if (argv[i] === "--limit") out.limit = Number(argv[++i]);
    else if (argv[i] === "--days") out.days = Number(argv[++i]);
    else throw new Error(`unknown argument: ${argv[i]}`);
  }
  if (!out.input || !out.output || !out.request) throw new Error("--input, --output and --request are required");
  return out;
}

function compactNumber(value) {
  if (typeof value === "number" && Number.isFinite(value)) return value;
  if (typeof value !== "string") return null;
  const text = value.replace(/,/g, "").trim();
  const match = text.match(/(\d+(?:\.\d+)?)\s*(만|천|[KMB])?/i);
  if (!match) return null;
  const multiplier = { "만": 10000, "천": 1000, k: 1000, m: 1000000, b: 1000000000 }[match[2]?.toLowerCase()] || 1;
  return Math.round(Number(match[1]) * multiplier);
}

function extractVisibleMetrics(item) {
  const metrics = { ...item.metrics };
  const evidence = `${item.metric_evidence?.like_context || ""}\n${item.metric_evidence?.comment_context || ""}`;
  const labelled = {
    views: evidence.match(/(?:조회|views?)\s*([\d.,]+\s*(?:만|천|[KMB])?)/i),
    likes: evidence.match(/(?:좋아요|likes?)\s*([\d.,]+\s*(?:만|천|[KMB])?)/i),
    comments: evidence.match(/(?:댓글|comments?)\s*([\d.,]+\s*(?:만|천|[KMB])?)/i),
    reposts: evidence.match(/(?:재게시|reposts?|shares?)\s*([\d.,]+\s*(?:만|천|[KMB])?)/i)
  };
  for (const [key, match] of Object.entries(labelled)) {
    if (metrics[key] == null && match) metrics[key] = compactNumber(match[1]);
  }
  const ordered = (item.metric_evidence?.comment_context || "")
    .split(/\s+/)
    .map(compactNumber)
    .filter(Number.isFinite);
  const likeOrdered = (item.metric_evidence?.like_context || "")
    .split(/\s+/)
    .map(compactNumber)
    .filter(Number.isFinite);
  if (metrics.likes == null && likeOrdered.length) metrics.likes = likeOrdered[0];
  if (metrics.comments == null && ordered.length > 1) metrics.comments = ordered[1];
  if (metrics.reposts == null && ordered.length > 2) metrics.reposts = ordered[2];
  return {
    metrics,
    confidence: labelled.views || labelled.likes || labelled.comments || labelled.reposts
      ? "labelled_public_ui"
      : ((likeOrdered.length || ordered.length > 1) ? "low_instagram_action_order_heuristic" : "unavailable")
  };
}

function percentile(items, key, value) {
  const values = items.map((item) => item.metrics[key]).filter(Number.isFinite).sort((a, b) => a - b);
  if (!Number.isFinite(value) || values.length === 0) return null;
  if (values.length === 1) return 1;
  return values.filter((candidate) => candidate <= value).length / values.length;
}

function mainFeedback(item, request) {
  const stopWords = new Set(["요즘", "인기", "있는", "알려줘", "찾아줘"]);
  const terms = request.toLowerCase().split(/\s+/).filter((term) => term.length > 1 && !stopWords.has(term));
  const haystack = `${item.source_label || ""}`.toLowerCase();
  const matched = terms.filter((term) => haystack.includes(term));
  if (matched.length) return `요청어와 연결되는 공개 문구가 있습니다: ${matched.slice(0, 3).join(", ")}`;
  return "반응 수치는 비교할 수 있지만 요청과의 관련성은 사용자가 원문에서 확인해야 합니다.";
}

const config = parseArgs(process.argv);
const source = JSON.parse(await fs.readFile(path.resolve(config.input), "utf8"));
const cutoff = Date.now() - config.days * 24 * 60 * 60 * 1000;
const items = (source.items || []).filter((item) => {
  const timestamp = Date.parse(item.published_at || "");
  return Number.isFinite(timestamp) && timestamp >= cutoff;
}).map((item) => {
  const extracted = extractVisibleMetrics(item);
  return { ...item, metrics: extracted.metrics, metric_confidence: extracted.confidence };
});
const weights = { views: 0.5, likes: 0.3, comments: 0.15, reposts: 0.05 };
for (const item of items) {
  const components = Object.entries(weights)
    .map(([key, weight]) => ({ key, weight, percentile: percentile(items, key, item.metrics[key]) }))
    .filter((entry) => entry.percentile != null);
  const usedWeight = components.reduce((sum, entry) => sum + entry.weight, 0);
  const hasPrimaryMetric = Number.isFinite(item.metrics.views) || Number.isFinite(item.metrics.likes);
  item.popularity = {
    score: usedWeight && hasPrimaryMetric
      ? Math.round(components.reduce((sum, entry) => sum + entry.percentile * entry.weight, 0) / usedWeight * 100)
      : null,
    basis: components.map((entry) => entry.key),
    scope: `${source.platform}_result_set_only`,
    warning: usedWeight && hasPrimaryMetric
      ? "공개된 수치의 상대 순위이며 절대 인기나 품질을 뜻하지 않음"
      : "조회수·좋아요 중 하나가 없어 인기 순위를 매기지 않음"
  };
  item.v2_feedback = mainFeedback(item, config.request);
  item.user_decision = null;
}
items.sort((a, b) => (b.popularity.score ?? -1) - (a.popularity.score ?? -1));
const result = {
  schema_version: "1.0",
  request: config.request,
  platform: source.platform,
  period_days: config.days,
  ranking_policy: "platform_local_public_metrics_only",
  weights,
  items: items.slice(0, config.limit),
  final_decision_owner: "user",
  allowed_decisions: ["adopt", "hold", "discard"]
};
await fs.mkdir(path.dirname(path.resolve(config.output)), { recursive: true });
await fs.writeFile(path.resolve(config.output), `${JSON.stringify(result, null, 2)}\n`, "utf8");
console.log(JSON.stringify({ status: "analyzed", items: result.items.length, output: path.resolve(config.output) }));
