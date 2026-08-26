#!/usr/bin/env python3
"""Render a local decision-only page for one PM4 evidence-router result."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    ready_items = [item for item in data.get("items", []) if item.get("review_ready")]
    omitted_count = len(data.get("items", [])) - len(ready_items)
    cards = []
    for index, item in enumerate(ready_items, 1):
        cards.append(f"""
        <article class="card" data-reference-id="{esc(item.get('candidate_id'))}" data-url="{esc(item.get('url'))}">
          <div class="cover"><span>{esc(item.get('platform'))}</span><strong>{esc(item.get('evidence_label_ko'))}</strong></div>
          <div class="body"><span class="lane">{index}. {esc(item.get('evidence_label_ko'))}</span>
          <h2>{esc(item.get('title'))}</h2>
          <p>{esc(item.get('summary_ko'))}</p>
          <div class="actions"><a href="{esc(item.get('url'))}" target="_blank" rel="noreferrer">원문 보기</a><button data-value="adopt">채택</button></div></div>
        </article>""")
    request = data.get("request", {})
    document = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PM4 자료 후보 검토</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f4f1eb;color:#172019;font-family:system-ui,-apple-system,"Noto Sans KR",sans-serif}}main{{max-width:1280px;margin:auto;padding:40px 24px 64px}}header{{display:flex;justify-content:space-between;gap:24px;align-items:end;margin-bottom:28px}}h1{{font-size:clamp(30px,4vw,52px);margin:0 0 12px}}header p{{margin:0;color:#57635b}}.status{{color:#087a54;font-weight:800}}.notice{{background:#fff4cc;border-radius:12px;padding:15px 17px;margin:0 0 22px;line-height:1.55}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:20px}}.card{{background:white;border:1px solid #d8ddd9;border-radius:18px;overflow:hidden;display:flex;flex-direction:column}}.cover{{height:180px;background:#e8efeb;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;gap:7px}}.cover span{{font-size:13px;color:#087a53}}.cover strong{{font-size:23px;line-height:1.25}}.body{{padding:20px;display:flex;flex:1;flex-direction:column}}.lane{{font-size:12px;color:#087a53}}h2{{font-size:20px;line-height:1.4;margin:14px 0 10px}}.card p{{color:#495d54;line-height:1.65;margin:0 0 18px;flex:1}}.actions{{display:flex;align-items:center;gap:9px}}.actions a,.actions button{{appearance:none;border:1px solid #b9c9c1;background:white;color:#153b2d;border-radius:8px;padding:9px 12px;text-decoration:none;cursor:pointer;font-weight:800}}.actions button.selected{{background:#13251e;color:white;border-color:#13251e}}footer{{margin-top:20px;color:#65766e;font-size:13px}}@media(max-width:640px){{main{{padding:24px 16px 44px}}header{{display:block}}.status{{display:block;margin-top:12px}}.cover{{height:145px}}}}
</style></head><body><main><header><div><h1>Reference 선택</h1><p>{esc(request.get('topic'))}</p></div><span class="status">마음에 드는 자료만 채택</span></header><div id="status" class="notice">내용과 참고 이유를 한국어로 설명할 수 있는 후보만 표시했습니다. 설명이 부족한 {omitted_count}개는 화면에서 제외했으며, 채택만으로 제품에 자동 적용되지는 않습니다.</div><section class="grid">{''.join(cards)}</section><footer>표시 후보 {len(ready_items)}개 · 설명 부족 제외 {omitted_count}개 · 단일 주제 제한 Runtime</footer></main><script>
const requestId={json.dumps(request.get('request_id'), ensure_ascii=False)};const statusEl=document.querySelector('#status');
function paint(adopted){{const ids=new Set(adopted||[]);document.querySelectorAll('[data-reference-id]').forEach(card=>card.querySelector('button[data-value="adopt"]').classList.toggle('selected',ids.has(card.dataset.referenceId)))}}
fetch('/api/pm4/evidence-reference-ui-state?request_id='+encodeURIComponent(requestId),{{cache:'no-store'}}).then(async response=>{{const data=await response.json();if(!response.ok)throw new Error(data.error||'Core 상태를 불러오지 못했습니다.');paint(data.adopted_reference_ids);statusEl.textContent='채택 결과가 Core에 연결되었습니다. 마음에 드는 자료만 선택하세요.';}}).catch(error=>{{statusEl.textContent='Core 연결 오류: '+error.message;}});
document.querySelectorAll('button[data-value="adopt"]').forEach(button=>button.addEventListener('click',async()=>{{const card=button.closest('[data-reference-id]');const action=button.classList.contains('selected')?'evidence-reference.clear':'evidence-reference.adopt';try{{const response=await fetch('/api/pm4/evidence-reference-ui-action',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify({{request_id:requestId,action,reference_id:card.dataset.referenceId}})}});const data=await response.json();if(!response.ok)throw new Error(data.error||'채택을 저장하지 못했습니다.');paint(data.state.adopted_reference_ids);statusEl.textContent='채택 결과를 Core에 저장했습니다.';}}catch(error){{statusEl.textContent='저장 오류: '+error.message;}}}}));
</script></body></html>"""
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(json.dumps({"status": "rendered", "items": len(cards), "output": str(output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
