#!/usr/bin/env python3
"""Collect visual references for one confirmed PM4 project request.

This adapter only captures and normalizes evidence. It never installs source
code, executes downloaded content, or applies a design to a product.
"""

import argparse
import hashlib
import html
import json
import mimetypes
import os
import shutil
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ALLOWED_CONTENT_TYPES = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/webp": ".webp",
    "image/avif": ".avif",
}
MAX_IMAGE_BYTES = 8 * 1024 * 1024
MIN_IMAGE_BYTES = 10 * 1024


def read_json(path):
    with open(path, "r", encoding="utf-8") as source:
        return json.load(source)


def write_json(path, payload):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as target:
        json.dump(payload, target, ensure_ascii=False, indent=2)
        target.write("\n")


def detect_local_type(path):
    guessed = mimetypes.guess_type(path)[0]
    if guessed in ALLOWED_CONTENT_TYPES:
        return guessed
    with open(path, "rb") as source:
        prefix = source.read(12)
    if prefix.startswith(b"\x89PNG"):
        return "image/png"
    if prefix.startswith(b"\xff\xd8"):
        return "image/jpeg"
    if prefix.startswith(b"RIFF") and prefix[8:12] == b"WEBP":
        return "image/webp"
    raise ValueError("지원하지 않는 로컬 이미지 형식입니다.")


def fetch_image(seed, image_dir):
    source_path = seed.get("local_image_path")
    if source_path:
        source_path = os.path.abspath(source_path)
        if not os.path.isfile(source_path):
            raise ValueError("로컬 이미지가 존재하지 않습니다.")
        size = os.path.getsize(source_path)
        content_type = detect_local_type(source_path)
        data_source = open(source_path, "rb")
    else:
        image_url = seed.get("image_url", "")
        if not image_url.startswith("https://"):
            raise ValueError("원격 이미지는 HTTPS만 허용합니다.")
        request = urllib.request.Request(image_url, headers={"User-Agent": "AI-OS-V2-PM4/1.0"})
        response = urllib.request.urlopen(request, timeout=20)
        content_type = response.headers.get_content_type()
        size = int(response.headers.get("Content-Length") or 0)
        data_source = response
    try:
        if content_type not in ALLOWED_CONTENT_TYPES:
            raise ValueError(f"이미지 Content-Type이 아닙니다: {content_type}")
        if size and not MIN_IMAGE_BYTES <= size <= MAX_IMAGE_BYTES:
            raise ValueError("이미지 크기가 허용 범위를 벗어났습니다.")
        data = data_source.read(MAX_IMAGE_BYTES + 1)
    finally:
        data_source.close()
    if not MIN_IMAGE_BYTES <= len(data) <= MAX_IMAGE_BYTES:
        raise ValueError("다운로드된 이미지 크기가 허용 범위를 벗어났습니다.")
    digest = hashlib.sha256(data).hexdigest()
    extension = ALLOWED_CONTENT_TYPES[content_type]
    filename = f"{seed['reference_id']}-{digest[:12]}{extension}"
    destination = os.path.join(image_dir, filename)
    os.makedirs(image_dir, exist_ok=True)
    with open(destination, "wb") as target:
        target.write(data)
    return destination, content_type, len(data), digest


def render_review(output_path, collection_path, payload):
    cards = []
    for item in payload["items"]:
        relative_image = "/pm4-visual-reference-images/" + os.path.basename(item["local_image_path"])
        cards.append(f"""
        <article class="card" data-reference-id="{html.escape(item['reference_id'])}">
          <img src="{html.escape(relative_image)}" alt="{html.escape(item['source_name'])} Reference">
          <div class="body"><span>{html.escape(item['source_type'])}</span>
          <h2>{html.escape(item['source_name'])}</h2>
          <p>{html.escape(item['natural_summary_ko'])}</p>
          <p><strong>참고할 부분</strong> · {html.escape(' · '.join(item['traits']))}</p>
          <div class="card-actions"><a href="{html.escape(item['source_url'])}" target="_blank" rel="noreferrer">원문 보기</a>
          <div class="decisions" aria-label="Reference 판정">
            <button type="button" data-decision="adopt">채택</button><button type="button" data-decision="hold">보류</button><button type="button" data-decision="discard">폐기</button>
          </div></div></div>
        </article>""")
    bootstrap = json.dumps({
        "request_id": payload["request_id"],
        "decisions": payload.get("decisions", {}),
        "refill": payload.get("refill", {}),
    }, ensure_ascii=False).replace("<", "\\u003c")
    document = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>전자명함 시각 Reference</title>
<style>:root{{--accent:#087a53;--ink:#172019;--line:#d8ddd9}}*{{box-sizing:border-box}}body{{margin:0;background:#f4f1eb;color:var(--ink);font-family:system-ui,sans-serif}}button{{font:inherit}}main{{max-width:1280px;margin:auto;padding:40px 24px}}.top{{display:flex;justify-content:space-between;align-items:end;gap:24px;margin-bottom:28px}}h1{{font-size:clamp(28px,4vw,52px);margin:0 0 12px}}.lead{{color:#57635b;margin:0}}.refill{{border:0;border-radius:10px;padding:14px 20px;background:#13251e;color:#fff;font-weight:800;white-space:nowrap;cursor:pointer}}.refill:disabled{{opacity:.55;cursor:wait}}.status{{min-height:24px;margin:10px 0 20px;color:#415248}}.tabs{{display:flex;gap:8px;margin-bottom:20px}}.tabs button{{border:1px solid #b7c2bc;background:white;border-radius:999px;padding:10px 16px;cursor:pointer}}.tabs button[aria-selected=true]{{background:#13251e;color:white;border-color:#13251e}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}}.card{{background:white;border:1px solid var(--line);border-radius:18px;overflow:hidden}}img{{width:100%;height:360px;object-fit:contain;background:#edf1ee}}.body{{padding:20px}}span{{font-size:12px;color:var(--accent)}}h2{{font-size:20px}}p{{line-height:1.6}}a{{color:#075e43;font-weight:700}}.card-actions{{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}}.decisions{{display:flex;gap:5px}}.decisions button{{border:1px solid #c6d0ca;background:#fff;border-radius:7px;padding:7px 9px;cursor:pointer}}.decisions button.active{{background:#daf3e8;border-color:#087a53;color:#075e43;font-weight:800}}.note{{margin-top:28px;padding:18px;border-radius:12px;background:#fff4cc}}.functional{{display:none}}.functional-list{{display:grid;gap:12px}}.functional article{{background:white;border:1px solid var(--line);border-radius:14px;padding:18px}}.functional h2{{margin:0 0 8px}}.functional p{{margin:6px 0;color:#4d5a52}}@media(max-width:640px){{main{{padding:24px 16px}}.top{{display:block}}.refill{{width:100%;margin-top:20px}}img{{height:300px}}}}</style></head>
<body><main><div class="top"><div><h1>전자명함 Reference</h1><p class="lead">실제 화면과 출처를 수집한 PM4 증거입니다. 아직 시안·Visual Target·제품 적용이 아닙니다.</p></div><button class="refill" id="refill" type="button">추가 탐색</button></div>
<p id="status" class="status" aria-live="polite"></p>
<nav class="tabs" aria-label="자료 종류"><button type="button" data-tab="visual" aria-selected="true">디자인 참고 <b>{len(payload['items'])}</b></button><button type="button" data-tab="functional" aria-selected="false">기능 참고</button></nav>
<section id="visual" class="grid">{''.join(cards)}</section><section id="functional" class="functional"><div id="functional-list" class="functional-list"><p>기능 자료를 불러오는 중입니다.</p></div></section>
<p class="note">추가 탐색은 기존 자료와 판정을 지우지 않고, 검색 범위를 넓혀 중복되지 않은 새 후보 3~5개만 붙입니다. Instagram·Threads 로그인 자료는 아직 연결 대기입니다.</p></main>
<script>const initial={bootstrap};const requestId=initial.request_id;const statusEl=document.querySelector('#status');
function paintDecisions(decisions){{document.querySelectorAll('[data-reference-id]').forEach(card=>{{const value=decisions[card.dataset.referenceId];card.querySelectorAll('[data-decision]').forEach(button=>button.classList.toggle('active',button.dataset.decision===value));}})}}
paintDecisions(initial.decisions||{{}});
fetch('/api/pm4/visual-reference-ui-state?request_id='+encodeURIComponent(requestId)).then(response=>response.json()).then(data=>paintDecisions(data.decisions||{{}})).catch(()=>{{}});
document.addEventListener('click',async event=>{{const decision=event.target.closest('[data-decision]');if(decision){{const card=decision.closest('[data-reference-id]');const active=decision.classList.contains('active');const payload={{request_id:requestId,action:active?'visual-reference.decision.clear':'visual-reference.decision.set',reference_id:card.dataset.referenceId}};if(!active)payload.decision=decision.dataset.decision;const response=await fetch('/api/pm4/visual-reference-ui-action',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify(payload)}});const data=await response.json();if(!response.ok){{statusEl.textContent=data.error||'판정을 저장하지 못했습니다.';return}}paintDecisions(data.state.decisions);statusEl.textContent='판정을 저장했습니다.';}}
const tab=event.target.closest('[data-tab]');if(tab){{document.querySelectorAll('[data-tab]').forEach(button=>button.setAttribute('aria-selected',String(button===tab)));document.querySelector('#visual').style.display=tab.dataset.tab==='visual'?'grid':'none';document.querySelector('#functional').style.display=tab.dataset.tab==='functional'?'block':'none';}}}});
document.querySelector('#refill').addEventListener('click',async event=>{{const button=event.currentTarget;button.disabled=true;button.textContent='새 자료 찾는 중…';statusEl.textContent='기존 자료와 겹치지 않는 후보를 찾고 있습니다.';try{{const response=await fetch('/api/pm4/visual-reference-ui-action',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify({{request_id:requestId,action:'visual-reference.refill'}})}});const data=await response.json();if(!response.ok)throw new Error(data.error||'추가 탐색에 실패했습니다.');const count=data.state.refill?.added_count||0;statusEl.textContent=`새 후보 ${{count}}개를 추가했습니다. 화면을 새로 불러옵니다.`;location.reload();}}catch(error){{statusEl.textContent=error.message;button.disabled=false;button.textContent='추가 탐색';}}}});
fetch('/api/pm4/project-ui-state?request_id='+encodeURIComponent(requestId)).then(response=>response.json()).then(data=>{{const list=document.querySelector('#functional-list');list.innerHTML=(data.items||[]).map(item=>`<article><h2>${{item.direction_label}}</h2><p>${{item.direction_summary_ko}}</p><p><strong>확인된 기능</strong> · ${{(item.capabilities||[]).join(' · ')}}</p><a href="${{item.url}}" target="_blank" rel="noreferrer">구현 자료 보기</a></article>`).join('')||'<p>연결된 기능 자료가 없습니다.</p>';}}).catch(()=>{{document.querySelector('#functional-list').innerHTML='<p>기능 자료를 불러오지 못했습니다. 디자인 자료는 그대로 사용할 수 있습니다.</p>';}});
</script></body></html>"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as target:
        target.write(document)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--seed-file", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--image-dir", required=True)
    parser.add_argument("--review-output")
    args = parser.parse_args()

    receipt = read_json(args.receipt)
    if not receipt.get("request_id") or not receipt.get("user_confirmed") or receipt.get("status") != "user_confirmed":
        raise SystemExit("확정된 인터뷰 명세가 아닙니다.")
    seed_payload = read_json(args.seed_file)
    if seed_payload.get("request_id") != receipt["request_id"]:
        raise SystemExit("탐색 결과와 인터뷰 명세가 일치하지 않습니다.")
    seeds = seed_payload.get("references", [])
    items, failures, seen_urls, seen_hashes = [], [], set(), set()
    for seed in seeds:
        try:
            required = {"reference_id", "source_name", "source_url", "source_type", "region", "natural_summary_ko", "traits", "do_not_copy"}
            if not required.issubset(seed):
                raise ValueError("필수 Reference 필드가 없습니다.")
            if seed["source_url"] in seen_urls:
                raise ValueError("중복 원문 URL입니다.")
            path, content_type, size, digest = fetch_image(seed, args.image_dir)
            if digest in seen_hashes:
                os.unlink(path)
                raise ValueError("중복 이미지입니다.")
            seen_urls.add(seed["source_url"])
            seen_hashes.add(digest)
            items.append({
                **{key: seed[key] for key in required},
                "discovery_evidence": seed.get("discovery_evidence"),
                "local_image_path": os.path.abspath(path),
                "image_url": seed.get("image_url"),
                "content_type": content_type,
                "byte_size": size,
                "sha256": digest,
                "reuse_policy": "reference_only",
                "collected_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            })
        except Exception as exc:
            failures.append({"reference_id": seed.get("reference_id", "unknown"), "reason": str(exc)})
    payload = {
        "schema_version": "1.0",
        "request_id": receipt["request_id"],
        "collector_mode": "visual_reference_seed_capture",
        "evidence_scope": receipt.get("project_type", "confirmed_request_only"),
        "items": items,
        "source_failures": failures,
        "coverage": {
            "total": len(items),
            "korean": sum(item["region"] == "korea" for item in items),
            "actual_service": sum("actual_service" in item["source_type"] for item in items),
            "user_provided": sum(item["source_type"] == "user_provided" for item in items),
        },
        "decisions": {},
        "visual_target_created": False,
        "implementation_allowed": False,
        "product_changed": False,
        "limitations": [
            "후보 발견은 이번 실제 요청에서 사람이 고정한 Seed를 사용했습니다.",
            "이 실행은 범용 자동 Reference 검색을 증명하지 않습니다.",
            "화면은 참고 전용이며 원본 브랜드·문구·인물을 복제하지 않습니다.",
        ],
    }
    write_json(args.output, payload)
    if args.review_output:
        render_review(args.review_output, args.output, payload)
    print(json.dumps({"collected": len(items), "failed": len(failures), "output": args.output}, ensure_ascii=False))


if __name__ == "__main__":
    main()
