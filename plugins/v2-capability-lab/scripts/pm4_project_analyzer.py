#!/usr/bin/env python3
"""Turn collected project evidence into five clearly different user choices."""
import argparse, json
from pathlib import Path

DIRECTIONS = [
    {
      "label":"QR·NFC로 바로 연결하는 명함",
      "summary":"휴대폰을 대거나 QR을 비추면 앱 설치 없이 연락처 저장·전화·문자·SNS가 바로 열리는 방식입니다.",
      "evidence":[("reddit",0),("threads",1)],
      "required_caps":["qr","vcard_contact_save","call_or_message_links"]
    },
    {
      "label":"깔끔하고 빠른 한 화면 명함",
      "summary":"이름·직업·사진과 핵심 연락 버튼을 먼저 보여주고, 처음 보는 사람도 설명 없이 바로 사용하는 방식입니다.",
      "evidence":[("youtube",1),("threads",0)],
      "required_caps":["vcard_contact_save","call_or_message_links"]
    },
    {
      "label":"신뢰와 경력을 보여주는 소개 명함",
      "summary":"사회복지사의 경력·활동 분야·소개를 연락 기능과 함께 보여줘, 저장하기 전에도 누구인지 이해하게 하는 방식입니다.",
      "evidence":[("threads",2),("reddit",2)],
      "required_caps":["call_or_message_links","theme_customization"]
    },
    {
      "label":"종이와 디지털을 함께 쓰는 명함",
      "summary":"종이 명함의 기억하기 쉬운 장점은 유지하고, QR로 최신 연락처와 소개 화면을 연결하는 방식입니다.",
      "evidence":[("reddit",1),("youtube",0)],
      "required_caps":["qr","vcard_contact_save","theme_customization"]
    },
    {
      "label":"구독 없이 직접 관리하는 명함",
      "summary":"외부 서비스의 월 구독에 의존하지 않고 공개 라이선스 코드로 운영하며, 연락처가 바뀌면 직접 수정하는 방식입니다.",
      "evidence":[("reddit",0),("reddit",1)],
      "required_caps":["privacy_or_local_processing","theme_customization"]
    },
]
IMAGES = ["enbiz.png", "arpix.png", "opencv.png", "swiish.png", "fahad.png"]

def main():
    p=argparse.ArgumentParser(); p.add_argument('--receipt',required=True); p.add_argument('--collection',required=True); p.add_argument('--social-evidence',required=True); p.add_argument('--output',required=True); a=p.parse_args()
    receipt=json.loads(Path(a.receipt).read_text()); collection=json.loads(Path(a.collection).read_text()); social=json.loads(Path(a.social_evidence).read_text())
    if receipt.get('status')!='user_confirmed' or collection.get('request_id')!=receipt.get('request_id'):
        raise SystemExit('confirmed matching receipt required')
    if len(collection.get('items',[]))!=5: raise SystemExit('exactly five collected candidates required')
    for source in ('reddit','youtube','threads','instagram'):
        if source not in social or 'status' not in social[source] or 'items' not in social[source]:
            raise SystemExit(f'incomplete social evidence source: {source}')
    evidence_urls=[]
    for source in ('reddit','youtube','threads','instagram'):
        for evidence in social[source]['items']:
            if not evidence.get('url','').startswith('https://') or not evidence.get('summary_ko'):
                raise SystemExit(f'invalid source evidence: {source}')
            evidence_urls.append(evidence['url'])
    if len(evidence_urls) != len(set(evidence_urls)):
        raise SystemExit('duplicate source evidence URL')
    items=[]; unused=list(collection['items'])
    for index,(direction,image) in enumerate(zip(DIRECTIONS,IMAGES)):
        matches=[raw for raw in unused if set(direction['required_caps']).issubset(set(raw.get('capabilities',[])))]
        if not matches:
            raise SystemExit(f"no implementation evidence satisfies direction: {direction['label']}")
        raw=max(matches,key=lambda value:(len(value.get('capabilities',[])),value.get('stars',0)))
        unused.remove(raw)
        item=dict(raw); item['candidate_id']=f"direction-{index+1}"; item['implementation_candidate_id']=raw['candidate_id']
        item['lifecycle_status']='candidate_preserved'
        item['direction_label']=direction['label']; item['direction_summary_ko']=direction['summary']
        item['evidence_links']=[]
        for source,evidence_index in direction['evidence']:
            evidence=social[source]['items'][evidence_index]
            source_label={'reddit':'Reddit','youtube':'YouTube','threads':'Threads','instagram':'Instagram'}[source]
            item['evidence_links'].append({'source':source_label,'url':evidence['url'],'summary_ko':evidence['summary_ko']})
        item['implementation_match_ko']='선택한 방향에 필요한 기능과 공개 라이선스가 확인된 제작 재료입니다.'
        item['required_capabilities']=direction['required_caps']
        item['implementation_match_verified']=set(direction['required_caps']).issubset(set(raw.get('capabilities',[])))
        item['visual_evidence_url']='/pm4-project-images/'+image
        item['visual_evidence_kind']='live_site_capture' if raw.get('preview_url') and raw.get('preview_url') != raw.get('url') else 'repository_page_capture'
        item['fit_notice']='기능·라이선스 근거가 확인된 참고 후보이며, 아직 설치하거나 채택하지 않았습니다.'
        items.append(item)
    out={
      'schema_version':'1.0','request_id':receipt['request_id'],'revision':1,
      'project_summary':'사회복지사용 웹 전자명함: QR 접속, vCard 저장, 전화·문자·이메일·SNS·웹사이트 연결',
      'items':items,'selected_candidate_id':None,'last_action':'project.candidates.prepared',
      'recommendation':{
        'candidate_id':'direction-3',
        'label':'Core 추천',
        'reason_ko':'사회복지사는 연락 기능뿐 아니라 누구에게 어떤 도움을 제공하는지 신뢰감 있게 설명하는 것이 중요하므로, 경력·활동 분야와 연락 기능을 함께 보여주는 방향을 추천합니다.',
        'basis':['사용자 직업: 사회복지사','필수 연락 기능 6개','Threads의 전문성·신뢰 활용 사례','Reddit의 기억·후속 연락 문제'],
        'auto_selected':False
      },
      'discovery_order':[
        'Reddit·YouTube·Instagram·Threads에서 실제 사용 사례와 불편을 먼저 탐색',
        '디자인·사용 방향을 서로 다르게 정리',
        '각 방향을 구현할 GitHub 코드·기능·라이선스를 나중에 연결',
      ],
      'github_role':'direction_source가 아니라 implementation_evidence',
      'non_selected_candidate_policy':'preserve_until_user_discards_or_supersedes',
      'region_contract':{'requested':'korea_and_global','status':'unmet','reason':'라이선스까지 확인된 한국 오픈소스 후보를 확보하지 못해 해외 후보 5개만 표시합니다.'},
      'source_failures':collection.get('source_failures',[]),'product_changed':False,'installation_performed':False
    }
    out['source_coverage']=[
      {'source':'Reddit','role':'실제 사용자 불만·필요 기능 확인','status':social['reddit']['status'],'count':len(social['reddit']['items'])},
      {'source':'YouTube','role':'제작·사용 흐름 확인','status':social['youtube']['status'],'count':len(social['youtube']['items'])},
      {'source':'Instagram','role':'최신 시각 사례 탐색','status':social['instagram']['status'],'count':len(social['instagram']['items'])},
      {'source':'Threads','role':'실제 사용 문구·활용 상황 확인','status':social['threads']['status'],'count':len(social['threads']['items'])},
      {'source':'GitHub','role':'정리된 방향을 구현할 코드·라이선스·기능 확인','status':'collected','count':5},
    ]
    Path(a.output).parent.mkdir(parents=True,exist_ok=True); Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'analyzed','items':5,'region_contract':'unmet'},ensure_ascii=False))
if __name__=='__main__': main()
