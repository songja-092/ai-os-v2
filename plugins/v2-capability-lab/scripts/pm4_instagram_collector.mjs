#!/usr/bin/env node
/** Collect Instagram search/profile links through an already-authenticated Chrome CDP session. */

import fs from "node:fs/promises";
import path from "node:path";

function args(argv) {
  const out = { cdp: "http://127.0.0.1:9225", limit: 10 };
  for (let i = 2; i < argv.length; i += 1) {
    const key = argv[i];
    if (key === "--cdp") out.cdp = argv[++i];
    else if (key === "--query") out.query = argv[++i];
    else if (key === "--output") out.output = argv[++i];
    else if (key === "--limit") out.limit = Number(argv[++i]);
    else throw new Error(`unknown argument: ${key}`);
  }
  if (!out.query || !out.output) throw new Error("--query and --output are required");
  if (!Number.isInteger(out.limit) || out.limit < 1 || out.limit > 10) throw new Error("--limit must be 1..10");
  return out;
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function connect(url) {
  const socket = new WebSocket(url);
  await new Promise((resolve, reject) => {
    socket.addEventListener("open", resolve, { once: true });
    socket.addEventListener("error", reject, { once: true });
  });
  let id = 0;
  const pending = new Map();
  socket.addEventListener("message", (event) => {
    const message = JSON.parse(event.data);
    const resolve = pending.get(message.id);
    if (resolve) {
      pending.delete(message.id);
      resolve(message);
    }
  });
  return {
    call(method, params = {}) {
      return new Promise((resolve) => {
        const requestId = ++id;
        pending.set(requestId, resolve);
        socket.send(JSON.stringify({ id: requestId, method, params }));
      });
    },
    close() { socket.close(); },
  };
}

async function evaluate(cdp, expression) {
  const message = await cdp.call("Runtime.evaluate", { expression, returnByValue: true });
  if (message.result?.exceptionDetails) throw new Error("browser evaluation failed");
  return message.result?.result?.value;
}

async function navigate(cdp, url, waitMs = 1800) {
  await cdp.call("Page.navigate", { url });
  await sleep(waitMs);
}

function profileName(url) {
  const match = new URL(url).pathname.match(/^\/([^/]+)\/$/);
  return match?.[1] ?? "";
}

async function main() {
  const config = args(process.argv);
  const targets = await (await fetch(`${config.cdp}/json/list`)).json();
  const target = targets.find((item) => item.type === "page" && item.url.includes("instagram.com"));
  if (!target) throw new Error("instagram_browser_not_running");
  const cdp = await connect(target.webSocketDebuggerUrl);
  try {
    const loginState = JSON.parse(await evaluate(cdp, `JSON.stringify({
      url: location.href,
      hasLoginForm: !!document.querySelector('input[name="username"],input[name="password"]'),
      isChallenge: location.pathname.includes('/auth_platform/') || location.pathname.includes('/challenge/')
    })`));
    if (loginState.hasLoginForm || loginState.isChallenge) throw new Error("instagram_login_required");

    await navigate(cdp, "https://www.instagram.com/");
    await evaluate(cdp, `(() => {
      const icon = [...document.querySelectorAll('[aria-label]')].find((item) => item.getAttribute('aria-label') === '검색' || item.getAttribute('aria-label') === 'Search');
      const trigger = icon?.closest('a');
      if (!trigger) throw new Error('instagram_search_trigger_missing');
      trigger.click();
    })()`);
    await sleep(700);
    const inputExists = await evaluate(cdp, `!!document.querySelector('input[placeholder="검색"],input[placeholder="Search"]')`);
    if (!inputExists) throw new Error("instagram_search_input_missing");
    await evaluate(cdp, `(() => {
      const input = document.querySelector('input[placeholder="검색"],input[placeholder="Search"]');
      input.focus(); input.select();
    })()`);
    await cdp.call("Input.dispatchKeyEvent", { type: "keyDown", key: "Backspace", code: "Backspace", windowsVirtualKeyCode: 8, nativeVirtualKeyCode: 8 });
    await cdp.call("Input.dispatchKeyEvent", { type: "keyUp", key: "Backspace", code: "Backspace", windowsVirtualKeyCode: 8, nativeVirtualKeyCode: 8 });
    await cdp.call("Input.insertText", { text: config.query });
    await sleep(1800);
    const activeQuery = await evaluate(cdp, `document.querySelector('input[placeholder="검색"],input[placeholder="Search"]')?.value || ''`);
    if (activeQuery !== config.query) throw new Error("instagram_search_query_not_applied");
    const profiles = JSON.parse(await evaluate(cdp, `JSON.stringify([...new Map([...document.querySelectorAll('a[href]')]
      .map((a) => ({ url: new URL(a.getAttribute('href'), location.origin).href, label: (a.textContent || '').trim().slice(0, 240) }))
      .filter((item) => /^https:\\/\\/www\\.instagram\\.com\\/[^/]+\\/$/.test(item.url))
      .filter((item) => !['explore','reels','direct','accounts'].includes(new URL(item.url).pathname.split('/')[1]))
      .filter((item) => item.label.length > 0)
      .filter((item) => !['프로필', 'Profile'].includes(item.label))
      .map((item) => [item.url, item])).values()].slice(0, ${config.limit}))`));
    if (profiles.length === 0) throw new Error("instagram_search_results_missing");
    const channelTerms = [config.query, "바이브", "코딩", "coding", "ai", "codex", "claude", "gpt", "개발", "디자인"];
    const relevantProfiles = profiles.filter((profile) => {
      const label = profile.label.toLowerCase();
      return channelTerms.some((term) => label.includes(term.toLowerCase()));
    });
    if (relevantProfiles.length === 0) throw new Error("instagram_relevant_channels_missing");

    const collected = [];
    for (const profile of relevantProfiles) {
      await navigate(cdp, profile.url, 1600);
      const username = profileName(profile.url);
      const details = JSON.parse(await evaluate(cdp, `JSON.stringify({
        profile_text: (document.body?.innerText || '').slice(0, 700),
        posts: [...new Map([...document.querySelectorAll('a[href]')]
          .map((a) => ({ url: new URL(a.getAttribute('href'), location.origin).href, label: (a.innerText || a.querySelector('img')?.alt || '').trim().slice(0, 500) }))
          .filter((item) => item.url.includes('/${username}/p/') || item.url.includes('/${username}/reel/'))
          .map((item) => [item.url, item])).values()].slice(0, 5)
      })`));
      collected.push({ username, profile_url: profile.url, search_label: profile.label, ...details });
    }

    const postCandidates = collected
      .flatMap((profile) => profile.posts.map((post) => ({
        username: profile.username,
        profile_url: profile.profile_url,
        post_url: post.url,
        source_label: post.label
      })))
      .slice(0, config.limit);

    const posts = [];
    for (const candidate of postCandidates) {
      await navigate(cdp, candidate.post_url, 1400);
      const visible = JSON.parse(await evaluate(cdp, `JSON.stringify((() => {
        const bodyText = (document.body?.innerText || '').replace(/\\s+/g, ' ').slice(0, 2600);
        const contextFor = (pattern) => {
          const node = [...document.querySelectorAll('[aria-label]')]
            .find((item) => pattern.test(item.getAttribute('aria-label') || ''));
          let current = node;
          for (let depth = 0; current && depth < 8; depth += 1, current = current.parentElement) {
            const text = (current.innerText || '').trim();
            if (text && /[0-9]/.test(text) && text.length < 240) return text;
          }
          return '';
        };
        return {
          body_text: bodyText,
          like_context: contextFor(/좋아요|Like/i),
          comment_context: contextFor(/댓글 달기|Comment/i),
          published_at: document.querySelector('time')?.getAttribute('datetime') || null
        };
      })())`));
      posts.push({
        ...candidate,
        published_at: visible.published_at,
        public_text: visible.body_text,
        metric_evidence: {
          like_context: visible.like_context,
          comment_context: visible.comment_context
        },
        metrics: {
          views: null,
          likes: null,
          comments: null,
          reposts: null
        },
        metric_status: "raw_ui_evidence_requires_analyzer"
      });
    }

    const result = {
      schema_version: "1.0",
      collected_at: new Date().toISOString(),
      platform: "instagram",
      adapter: "authenticated_chrome_cdp",
      query: config.query,
      role: "collection_only_no_popularity_or_adoption_judgment",
      discovery_strategy: "topic_channel_first_then_public_posts",
      login_status: "verified",
      profiles: collected,
      items: posts,
      collection_scope: ["search_result_profiles", "public_profile_post_links"],
      excluded_scope: ["home_feed", "direct_messages", "contacts", "private_project_data"],
      popularity_judgment: null,
      metric_warning: "공개 화면에서 보이는 수치만 원문 증거로 저장하며, 보이지 않는 조회수나 좋아요를 추정하지 않음",
      sufficiency_judgment: null,
      adoption_decision: null,
      next_owner: "user"
    };
    await fs.mkdir(path.dirname(path.resolve(config.output)), { recursive: true });
    await fs.writeFile(path.resolve(config.output), `${JSON.stringify(result, null, 2)}\n`, "utf8");
    console.log(JSON.stringify({ status: "collected", output: path.resolve(config.output), item_count: collected.length }));
  } finally {
    cdp.close();
  }
}

main().catch((error) => {
  console.error(JSON.stringify({ status: "blocked", error: error.message }));
  process.exitCode = 2;
});
