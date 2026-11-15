import json,glob,re,collections,html
END=re.compile(r"<h2[ >]|<div class='wsp-related'>|<div class=\"chb-cta\"|<div class='wsp-back'>")
DROPH=re.compile(r"(to sell a (house|[A-Za-z .'-]+ house) in |ways to sell a house in |we see with |when this applies to you| appeals$| and transfer tax|tax when you sell in |to sell a house when|rules that can affect)",re.I)
HERO=["Inherited, behind on payments, tenants, repairs: we buy it as-is","Zero fees, zero commissions, zero closing costs","No obligation: turn the offer down and owe us nothing"]
def label(c,slug):
    m=re.search(r'<h1>(.*?)</h1>',c);h=re.sub(r'<[^>]+>','',m.group(1)) if m else slug
    return h.split(':')[0].replace('Sell My House Fast in ','').strip()
def cut_sections(c):
    out=[];i=0;n=0
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>',c,re.S):
        if m.start()<i: continue
        h=re.sub(r'<[^>]+>','',m.group(1))
        if DROPH.search(h) and 'FAQ' not in h and 'Sources' not in h:
            e=END.search(c,m.end());e=e.start() if e else len(c)
            out.append(c[i:m.start()]);i=e;n+=1
    out.append(c[i:]);return ''.join(out)
def faq_rebuild(c,keep):
    m=re.search(r'(<h2[^>]*>[^<]*FAQ</h2>)(.*?)(?=<div class=.wsp-related|<h2|<script)',c,re.S)
    if not m: return c
    pairs=re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>',m.group(2),re.S)
    kept=[(q,a) for q,a in pairs if q.strip() and keep(re.sub(r'<[^>]+>','',a))]
    if kept:
        body=''.join(f'<h3 class="wp-block-heading">{q}</h3><p>{a}</p>' for q,a in kept)
        c=c[:m.start()]+m.group(1)+body+c[m.end():]
        ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":html.unescape(re.sub(r'<[^>]+>','',q)),"acceptedAnswer":{"@type":"Answer","text":html.unescape(re.sub(r'<[^>]+>','',a))}} for q,a in kept]}
        new='<script type="application/ld+json">'+json.dumps(ld)+'</script>'
        c,k=re.subn(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>',lambda _:new,c,flags=re.S)
        if not k: c=c.replace('</div></div><script',new+'</div></div><script',1) if False else c
    else:
        c=c[:m.start()]+c[m.end():]
        c=re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>','',c,flags=re.S)
    return c
files=sorted(glob.glob('pages/*/*.json'));D=[(f,json.load(open(f))) for f in files]
# answer df for FAQ keep
adf=collections.Counter()
for f,d in D:
    for p in d:
        for q,a in re.findall(r'<h3[^>]*>(.*?)</h3>\s*<p>(.*?)</p>',p['content'],re.S): adf[re.sub(r'<[^>]+>','',a)]+=1
for f,d in D:
    for p in d:
        c=p['content'];L=label(c,p['slug']);st=re.search(r"we-buy-houses-in-([a-z-]+)/",c)
        c=cut_sections(c)
        c=faq_rebuild(c,lambda a:adf[a]<=2 and len(a.split())>=8)
        c=c.replace(HERO[0],f"{L}: inherited, behind on payments, tenants or repairs, we buy the house as-is")
        c=c.replace(HERO[1],f"No fees, commissions or closing costs on a {L} sale")
        c=c.replace(HERO[2],f"Turn the {L} offer down and you owe us nothing")
        c=re.sub(r"(<p><em>Last updated [A-Za-z]+ \d+, \d{4}\.)[^<]*(</em></p>)",r"\1\2",c)
        c=re.sub(r'<p><em>This guide is general information[^<]*</em></p>',f'<p><em>General information for {L}, not legal or tax advice. Confirm details with the official office or a licensed professional.</em></p>',c)
        c=re.sub(r'<(p|li)>\s*</\1>','',c)
        p['content']=c
    json.dump(d,open(f,'w'))
