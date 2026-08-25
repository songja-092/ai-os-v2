#!/usr/bin/env python3
"""Collect YouTube/Reddit Atom feeds with an adaptive 30/90/365-day window."""
import argparse, json, urllib.error, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ATOM = "{http://www.w3.org/2005/Atom}"

def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def main():
    p=argparse.ArgumentParser(); p.add_argument("--platform",choices=["youtube","reddit"],required=True); p.add_argument("--seeds",required=True); p.add_argument("--output",required=True); p.add_argument("--memory"); p.add_argument("--limit",type=int,default=10); a=p.parse_args()
    seeds=[x for x in json.loads(Path(a.seeds).read_text(encoding="utf-8"))["channels"] if x["platform"]==a.platform]
    preferred=[]
    if a.memory and Path(a.memory).exists():
        preferred=json.loads(Path(a.memory).read_text(encoding="utf-8")).get("preferred_channels",[])
    preferred_names={str(x.get("channel","")) for x in preferred if x.get("platform")==a.platform}
    seeds.sort(key=lambda x: (x.get("channel") not in preferred_names, x.get("channel","")))
    collected=[]; failures=[]
    for seed in seeds:
        req=urllib.request.Request(seed["feed"],headers={"User-Agent":"AI-OS-V2-PM4/1.0 (personal research)"})
        try:
            with urllib.request.urlopen(req,timeout=20) as response: root=ET.fromstring(response.read())
        except (urllib.error.HTTPError, urllib.error.URLError, ET.ParseError) as exc:
            failures.append({"channel":seed["channel"],"error":f"{type(exc).__name__}: {exc}"})
            continue
        for entry in root.findall(f"{ATOM}entry"):
            link=next((x.get("href") for x in entry.findall(f"{ATOM}link") if x.get("href")),None)
            published=entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated")
            collected.append({"platform":a.platform,"channel_name":seed["channel"],"channel_url":seed["url"],"title":entry.findtext(f"{ATOM}title") or "","url":link,"published_at":published,"public_text":"","source_mode":"official_or_public_atom_feed"})
    topic_terms=("ai","codex","claude","gpt","agent","vibe","coding","cursor","코딩","개발","자동화","수익","openai")
    relevant=[x for x in collected if any(term in f'{x.get("title","")} {x.get("public_text","")}'.lower() for term in topic_terms)]
    unique={x["url"]:x for x in relevant if x.get("url") and x.get("published_at")}
    values=sorted(unique.values(),key=lambda x:(x.get("channel_name") in preferred_names,x["published_at"]),reverse=True)
    used=365; items=[]
    now=datetime.now(timezone.utc)
    for days in (30,90,365):
        items=[x for x in values if parse_time(x["published_at"]) >= now-timedelta(days=days)]
        used=days
        if len(items)>=a.limit: break
    result={"schema_version":"1.0","platform":a.platform,"collected_at":now.isoformat(),"requested_period_days":30,"used_period_days":used,"period_expanded":used>30,"discovery_strategy":"adopted_channel_first_then_temporary_channel","preferred_channels_applied":sorted(preferred_names),"items":items[:a.limit],"source_failures":failures,"adoption_decision":None}
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":"collected","platform":a.platform,"items":len(result["items"]),"used_period_days":used},ensure_ascii=False))
if __name__=="__main__": main()
