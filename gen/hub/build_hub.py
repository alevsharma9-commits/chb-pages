import json,glob,os,re,sys
sys.path.insert(0,'/home/claude/chb-pages/gen')
from common import *
R='/home/claude/chb-pages'
NAMES={}
for k in json.load(open(R+'/data/hub-links.json')): NAMES[k[17:]]=None
def title_of(s): return ' '.join(w.capitalize() if w!='of' else w for w in s.split('-'))
def build(code):
    fx=json.load(open(f'{R}/gen/hub/facts/{code}.json')); d=json.load(open(f'{R}/gen/hub/out/{code}.json'))
    sl=fx['state_slug']; St=title_of(sl); hub='we-buy-houses-in-'+sl
    allslugs={s for k in('city_pages','city_tax_guides','county_pages','state_topic_pages') for s,_ in fx[k]}
    tl={s:t for k in('city_pages','city_tax_guides','county_pages','state_topic_pages') for s,t in fx[k]}
    body="<style>.wsp-directory{margin-top:1rem;}.wsp-directory h2{font-size:1.4rem;font-weight:700;margin-bottom:1.5rem;}.wsp-directory h3{font-size:1.05rem;font-weight:700;margin:1.75rem 0 .85rem;color:#1A202C;border-bottom:2px solid #e2e8f0;padding-bottom:.4rem;}.wsp-directory-grid{display:flex;flex-wrap:wrap;gap:.55rem;margin:0;}.wsp-directory-grid a{display:inline-block;background:#f8fafc;border:1px solid #e2e8f0;border-radius:20px;padding:.4rem 1rem;font-size:.88rem;font-weight:600;color:var(--global-palette1, #3182CE);text-decoration:none;white-space:nowrap;}.wsp-directory-grid a:hover{background:var(--global-palette1, #3182CE);color:#fff;border-color:var(--global-palette1, #3182CE);}.wsp-directory h3{background:none;border:0;border-bottom:2px solid #e2e8f0;border-radius:0;padding:0 0 .4rem;}.wsp-directory h3+div{margin:0}</style>"+f"<p><em>Last updated {DATE}.</em></p>"
    secs=d['sections']
    body+=secs[0]['html'] if False else ''
    first=secs[0]; body+=f"<h2>{esc(first['h2'])}</h2>"+first['html']
    body+=cta(f'Selling in {St}?',f'We buy {St} houses as-is, with no commission, no repairs and no closing costs to you.')
    # directory
    dh=f"<div class='wsp-directory'><h2>Counties and Cities We Buy Houses In Across {St}</h2>"
    placed=set()
    for c in d['counties']:
        links=[]
        for s in c.get('county_slugs',[]):
            assert s in allslugs,(code,s); placed.add(s)
            links.append(f"<a href='{SITE}{s}/'>{esc(re.sub(r':.*','',tl[s]))}</a>")
        for ci in c.get('cities',[]):
            assert ci['slug'] in allslugs,(code,ci['slug']); placed.add(ci['slug'])
            links.append(f"<a href='{SITE}{ci['slug']}/'>{esc(ci['name'])}</a>")
        if links: dh+=f"<h3>{esc(c['name'])}</h3><div class='wsp-directory-grid'>{' '.join(links)}</div>"
    un=[]
    for ci in d.get('unplaced',[]):
        assert ci['slug'] in allslugs,(code,ci['slug']); placed.add(ci['slug']); un.append(f"<a href='{SITE}{ci['slug']}/'>{esc(ci['name'])}</a>")
    rest=[s for s,_ in fx['city_pages']+fx['city_tax_guides']+fx['county_pages'] if s not in placed]
    for s in rest: un.append(f"<a href='{SITE}{s}/'>{esc(re.sub(r':.*','',tl[s]))}</a>")
    if un: dh+=f"<h3>More {esc(St)} places</h3><div class='wsp-directory-grid'>{' '.join(un)}</div>"
    dh+='</div>'
    body+=dh
    for s in secs[1:]: body+=f"<h2>{esc(s['h2'])}</h2>"+s['html']
    topics=[(s,t) for s,t in fx['state_topic_pages']][:8]
    if topics: body+=f"<div class='wsp-related'><h2>{esc(St)} guides for homeowners</h2><div class='wsp-related-grid'>"+''.join(f"<div class='wsp-related-card'><a href='{SITE}{s}/'>{esc(re.sub(r':.*','',t))}</a></div>" for s,t in topics)+"</div></div>"
    faqs=[(f['q'],f['a']) for f in d['faqs']]
    body+='<h2>Frequently asked questions</h2>'+faq_html(faqs)
    if d.get('sources'): body+=sources([(x['title'],x['url']) for x in d['sources']])
    body+=f"<div class='wsp-back'><a href='{SITE}where-we-buy/'>&larr; Back to all states</a></div>"
    body+=schema(faqs,[('Home',SITE),(St,f'{SITE}{hub}/')])
    h1=f"We Buy Houses for Cash in {St}"
    hh=hero(St,h1,f'Sell Your {St} House for Cash',f'Tell us about your {St} house.')
    rt=f"We Buy Houses in {St} | Cash Offer"[:62]
    rd=f"We buy houses for cash in {St}. Browse every {St} county and city we cover, with property tax, probate and selling guides."
    rd=rd if len(rd)<=155 else rd[:152].rsplit(' ',1)[0]+'.'
    item=wrap(hub,h1,hh,body,rt,rd,f"we buy houses in {St.lower()}")
    n=len(re.sub(r'<[^>]+>',' ',re.sub(r'<style>.*?</style>|<script.*?</script>','',item['content'],flags=re.S)).split())
    return item,n
if __name__=='__main__':
    for code in sys.argv[1:]:
        it,n=build(code); fx=json.load(open(f'{R}/gen/hub/facts/{code}.json'))
        os.makedirs(f'{R}/pages/{code}',exist_ok=True)
        json.dump([it],open(f"{R}/pages/{code}/{fx['state_slug']}-hub-1.json",'w'))
        print(code,n,'words')
