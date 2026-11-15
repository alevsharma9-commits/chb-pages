import json,glob,re,collections,html
def txt(c):
    t=re.sub(r'<style>.*?</style>|<script.*?</script>','',c,flags=re.S);return re.sub(r'<[^>]+>','\n',t)
def sset(c):
    s=set()
    for blk in txt(c).split('\n'):
        for x in re.split(r'(?<=[.!?])\s+',blk.strip()):
            if len(x.split())>=6:s.add(x)
    return s
files=sorted(glob.glob('pages/*/*.json'))
D=[(f,json.load(open(f))) for f in files]
df=collections.Counter()
for f,d in D:
    for p in d: df.update(sset(p['content']))
KEEP=("Laws, forms and fees change","Citations come from","This guide is general information")
DROP=[s for s,n in df.items() if n>=60 and not s.startswith(KEEP) and not s.endswith("Sources.")]
# heading-like / titles must stay: only drop sentences ending with punctuation inside p/li
DROP=[s for s in DROP if s[-1] in '.!?' ]
DROP.sort(key=len,reverse=True)
HERO=["Inherited, behind on payments, tenants, repairs: we buy it as-is","Zero fees, zero commissions, zero closing costs","No obligation: turn the offer down and owe us nothing"]
def label(c,slug):
    m=re.search(r'<h1>(.*?)</h1>',c)
    h=re.sub(r'<[^>]+>','',m.group(1)) if m else slug
    return h.split(':')[0].replace('Sell My House Fast in ','').replace('Sell My House Fast ','').strip()
n=0
for f,d in D:
    for p in d:
        c=p['content'];L=label(c,p['slug'])
        # personalize hero bullets
        c=c.replace(HERO[0],f"{L}: inherited, behind on payments, tenants or repairs, we buy the house as-is")
        c=c.replace(HERO[1],f"No fees, commissions or closing costs on a {L} sale")
        c=c.replace(HERO[2],f"Turn the {L} offer down and you owe us nothing")
        for s in DROP:
            e=html.escape(s,quote=False)
            for v in {s,e,s.replace("'","&#039;"),s.replace("'","&#8217;")}:
                c=c.replace(' '+v,'').replace(v,'')
        c=re.sub(r'<(p|li)>\s*</\1>','',c)
        c=re.sub(r'<(p|li)><strong>[^<]{0,40}</strong>\s*</\1>','',c)
        c=re.sub(r'<ul[^>]*>\s*</ul>|<ol[^>]*>\s*</ol>','',c)
        if c!=p['content']: p['content']=c;n+=1
    json.dump(d,open(f,'w'))
print('pages changed',n,'dropped sentences',len(DROP))
