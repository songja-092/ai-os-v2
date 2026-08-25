#!/usr/bin/env node
/** Collect public channel-first results from YouTube, Reddit, or Threads via authenticated Chrome. */
import fs from "node:fs/promises";
import path from "node:path";

const config = { cdp: "http://127.0.0.1:9225", limit: 10 };
for (let i = 2; i < process.argv.length; i += 1) {
  const key = process.argv[i];
  if (key === "--platform") config.platform = process.argv[++i];
  else if (key === "--query") config.query = process.argv[++i];
  else if (key === "--output") config.output = process.argv[++i];
  else if (key === "--cdp") config.cdp = process.argv[++i];
  else if (key === "--limit") config.limit = Number(process.argv[++i]);
  else if (key === "--memory") config.memory = process.argv[++i];
  else if (key === "--channel-url") config.channelUrl = process.argv[++i];
  else throw new Error(`unknown argument: ${key}`);
}
if (!["youtube", "reddit", "threads"].includes(config.platform) || !config.query || !config.output) throw new Error("--platform, --query and --output are required");

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
async function connect(url) {
  const socket = new WebSocket(url); await new Promise((yes, no) => { socket.onopen = yes; socket.onerror = no; });
  let id = 0; const pending = new Map();
  socket.onmessage = (event) => { const message = JSON.parse(event.data); const resolve = pending.get(message.id); if (resolve) { pending.delete(message.id); resolve(message); } };
  return { call(method, params = {}) { return new Promise((resolve) => { const requestId = ++id; pending.set(requestId, resolve); socket.send(JSON.stringify({ id: requestId, method, params })); }); }, close() { socket.close(); } };
}
async function evaluate(cdp, expression) { const result = await cdp.call("Runtime.evaluate", { expression, returnByValue: true }); if (result.result?.exceptionDetails) throw new Error(`browser_evaluation_failed:${result.result.exceptionDetails.text || "unknown"}`); return result.result?.result?.value; }

const targets = await (await fetch(`${config.cdp}/json/list`)).json();
const expectedHost = { youtube: "youtube.com", reddit: "reddit.com", threads: "threads.com" }[config.platform];
const target = targets.find((item) => item.type === "page" && item.url.includes(expectedHost)) || targets.find((item) => item.type === "page");
if (!target) throw new Error("chrome_page_missing");
const cdp = await connect(target.webSocketDebuggerUrl);
try {
  const encoded = encodeURIComponent(config.query);
  const urls = {
    youtube: `https://www.youtube.com/results?search_query=${encoded}`,
    reddit: `https://www.reddit.com/search/?q=${encoded}&sort=top&t=month`,
    threads: `https://www.threads.com/search?q=${encoded}`
  };
  await cdp.call("Page.navigate", { url: config.channelUrl || urls[config.platform] });
  await sleep(config.platform === "threads" ? 5000 : (config.platform === "reddit" ? 3500 : 2600));
  const loginBlocked = JSON.parse(await evaluate(cdp, `JSON.stringify({url:location.href,text:(document.body?.innerText||'').slice(0,1200),login:!!document.querySelector('input[type="password"]')})`));
  if (config.platform === "threads" && (/Log in or sign up|Instagram으로 계속하기|로그인/.test(loginBlocked.text) || loginBlocked.login)) throw new Error("threads_login_required");
  const expressions = {
    youtube: `(()=>{const rows=[...document.querySelectorAll('a[href*="watch?v="]')].map(video=>{const card=video.closest('ytd-video-renderer, ytd-rich-item-renderer')||video.parentElement;const channel=card?.querySelector('ytd-channel-name a,a[href^="/@"]');const href=new URL(video.href,location.origin).href.split('&')[0];return [href,{platform:'youtube',channel_name:(channel?.textContent||'').trim(),channel_url:channel?new URL(channel.href,location.origin).href:null,title:(video.getAttribute('title')||video.textContent||'').trim(),url:href,public_text:(card?.innerText||'').trim().slice(0,900)}]});return JSON.stringify([...new Map(rows).values()].filter(x=>x.title).slice(0,${config.limit}))})()`,
    reddit: `(()=>{const rows=[...document.querySelectorAll('a[href*="/comments/"]')].map(a=>{const box=a.closest('article,shreddit-post')||a.parentElement;const href=new URL(a.href,location.origin).href;const parts=new URL(href).pathname.split('/');const rIndex=parts.indexOf('r');const sub=rIndex>=0?(parts[rIndex+1]||''):'';const text=(box?.innerText||'').trim();const age=text.match(/(\\d+)\\s*([mhd])\\s*ago/i);const unit=age?.[2]?.toLowerCase();const ms=age?(Number(age[1])*(unit==='d'?86400000:unit==='h'?3600000:60000)):0;return [href,{platform:'reddit',channel_name:sub,channel_url:sub?'https://www.reddit.com/r/'+sub:null,title:(a.textContent||'').trim().slice(0,240),url:href,published_at:ms?new Date(Date.now()-ms).toISOString():null,public_text:text.slice(0,900)}]});return JSON.stringify([...new Map(rows).values()].filter(x=>x.title).slice(0,${config.limit}))})()`,
    threads: `(()=>{const rows=[...document.querySelectorAll('a[href*="/post/"]:not([href$="/media"])')].map(a=>{const href=new URL(a.href,location.origin).href;let card=a;for(let i=0;i<8&&card?.parentElement;i++){if((card.innerText||'').trim().length>80)break;card=card.parentElement}const text=(card?.innerText||'').trim();const parts=new URL(href).pathname.split('/');const user=(parts.find(part=>part.startsWith('@'))||'').slice(1);const dateText=(a.textContent||'').trim();const dm=dateText.match(/^(\\d{2})\\/(\\d{2})\\/(\\d{2})$/);const parsed=dm?new Date(Date.UTC(2000+Number(dm[3]),Number(dm[1])-1,Number(dm[2]))).toISOString():null;return [href,{platform:'threads',channel_name:user,channel_url:user?'https://www.threads.com/@'+user:null,title:text.split('\\n').filter(Boolean).slice(1,4).join(' ').slice(0,240),url:href,published_at:parsed,public_text:text.slice(0,900),source_mode:'authenticated_aside_browser'}]});const unique=[...new Map(rows).values()].filter(x=>x.title).sort((a,b)=>Date.parse(b.published_at||0)-Date.parse(a.published_at||0));const now=Date.now(),windows=[30,90,365];let picked=[],used=365;for(const days of windows){picked=unique.filter(x=>x.published_at&&Date.parse(x.published_at)>=now-days*86400000);used=days;if(picked.length>=${config.limit})break}return JSON.stringify({items:picked.slice(0,${config.limit}),used_period_days:used})})()`
  };
  const extracted = JSON.parse(await evaluate(cdp, expressions[config.platform]));
  const items = Array.isArray(extracted) ? extracted : extracted.items;
  const usedPeriodDays = Array.isArray(extracted) ? 30 : extracted.used_period_days;
  let preferredChannels = [];
  if (config.memory) {
    try { preferredChannels = JSON.parse(await fs.readFile(path.resolve(config.memory), "utf8")).preferred_channels?.filter((x) => x.platform === config.platform).map((x) => x.channel) || []; } catch {}
  }
  items.sort((a, b) => Number(preferredChannels.includes(b.channel_name)) - Number(preferredChannels.includes(a.channel_name)));
  const result = { schema_version: "1.0", platform: config.platform, collected_at: new Date().toISOString(), query: config.query, channel_url: config.channelUrl || null, requested_period_days: 30, used_period_days: usedPeriodDays, period_expanded: usedPeriodDays > 30, discovery_strategy: config.channelUrl ? "direct_professional_channel" : "adopted_channel_first_then_search_result", preferred_channels_applied: preferredChannels, role: "collection_only", items, adoption_decision: null };
  await fs.mkdir(path.dirname(path.resolve(config.output)), { recursive: true });
  await fs.writeFile(path.resolve(config.output), `${JSON.stringify(result, null, 2)}\n`, "utf8");
  console.log(JSON.stringify({ status: items.length ? "collected" : "partial", platform: config.platform, items: items.length }));
} finally { cdp.close(); }
