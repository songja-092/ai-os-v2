#!/usr/bin/env node
/** Render a local, decision-only review page for ranked social references. */
import fs from "node:fs/promises";
import path from "node:path";

const inputIndex = process.argv.indexOf("--input");
const outputIndex = process.argv.indexOf("--output");
if (inputIndex < 0 || outputIndex < 0) throw new Error("--input and --output are required");
const data = JSON.parse(await fs.readFile(path.resolve(process.argv[inputIndex + 1]), "utf8"));
const escape = (value) => String(value ?? "").replace(/[&<>\"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char]));
const metric = (label, value) => `<span><b>${label}</b> ${Number.isFinite(value) ? value.toLocaleString("ko-KR") : "확인 불가"}</span>`;
const cards = data.items.map((item, index) => `
  <article class="card" data-url="${escape(item.post_url)}">
    <div class="rank">${index + 1}</div>
    <div class="body">
      <div class="top"><strong>${escape(item.username)}</strong><span class="score">인기 근거 ${item.popularity.score ?? "산정 안 함"}</span></div>
      <p>${escape(item.v2_feedback)}</p>
      <div class="metrics">${metric("조회", item.metrics.views)}${metric("좋아요", item.metrics.likes)}${metric("댓글", item.metrics.comments)}${metric("공유", item.metrics.reposts)}</div>
      <small>${escape(item.popularity.warning)} · 수치 신뢰: ${escape(item.metric_confidence)}</small>
      <div class="actions"><a href="${escape(item.post_url)}" target="_blank" rel="noreferrer">원문 보기</a><button data-value="adopt">채택</button><button data-value="hold">보류</button><button data-value="discard">폐기</button></div>
    </div>
  </article>`).join("");
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>소셜 자료 10개 검토</title><style>
*{box-sizing:border-box}body{margin:0;background:#f5f7f6;color:#17251f;font-family:system-ui,-apple-system,"Noto Sans KR",sans-serif}.wrap{max-width:1120px;margin:auto;padding:32px}.head{display:flex;justify-content:space-between;gap:24px;align-items:end;margin-bottom:20px}.head h1{margin:0 0 8px;font-size:28px}.head p{margin:0;color:#607068}.notice{padding:14px 16px;border:1px solid #b9d4c9;background:#eaf7f1;border-radius:12px;margin-bottom:16px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.card{display:flex;gap:14px;padding:18px;background:white;border:1px solid #d8e1dd;border-radius:14px}.rank{display:grid;place-items:center;flex:0 0 38px;height:38px;border-radius:50%;background:#0a8f62;color:white;font-weight:800}.body{min-width:0;flex:1}.top{display:flex;justify-content:space-between;gap:12px}.score{font-size:13px;color:#0a7553}.body p{min-height:44px;color:#405149}.metrics{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}.metrics span{padding:6px 9px;background:#f0f4f2;border-radius:8px;font-size:13px}.body small{display:block;color:#738078}.actions{display:flex;gap:8px;margin-top:14px}.actions a,.actions button{border:1px solid #bdcbc5;background:white;color:#17342a;border-radius:8px;padding:8px 11px;text-decoration:none;cursor:pointer}.actions button.selected{background:#0a8f62;color:white;border-color:#0a8f62}.actions button[data-value=discard].selected{background:#b9493f;border-color:#b9493f}@media(max-width:760px){.grid{grid-template-columns:1fr}.wrap{padding:18px}.head{display:block}}
</style></head><body><main class="wrap"><div class="head"><div><h1>소셜 자료 10개 검토</h1><p>${escape(data.request)} · ${escape(data.platform)}</p></div><b>최종 판단은 사용자</b></div><div class="notice">조회·좋아요가 공개되지 않으면 인기 순위를 만들지 않습니다. 각 원문을 확인한 뒤 채택·보류·폐기를 선택하세요.</div><section class="grid">${cards}</section></main><script>
const key='v2-social-decisions:'+location.pathname;const saved=JSON.parse(localStorage.getItem(key)||'{}');
document.querySelectorAll('.card').forEach(card=>{const url=card.dataset.url;const paint=v=>card.querySelectorAll('button').forEach(b=>b.classList.toggle('selected',b.dataset.value===v));const select=v=>{if(saved[url]===v){delete saved[url];paint(null)}else{saved[url]=v;paint(v)}localStorage.setItem(key,JSON.stringify(saved))};if(saved[url])paint(saved[url]);card.querySelectorAll('button').forEach(button=>button.onclick=()=>select(button.dataset.value))});
</script></body></html>`;
await fs.mkdir(path.dirname(path.resolve(process.argv[outputIndex + 1])), { recursive: true });
await fs.writeFile(path.resolve(process.argv[outputIndex + 1]), html, "utf8");
console.log(JSON.stringify({ status: "rendered", items: data.items.length }));
