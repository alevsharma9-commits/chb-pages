import json,glob,re,collections,sys,statistics
def body(c):
    c=re.sub(r"<script.*?</script>|<style.*?</style>","",c,flags=re.S)
    c=re.sub(r"<div class=.wsp-hero.*?(?=<h2)","",c,count=1,flags=re.S)
    c=re.sub(r"<div class=.wsp-related.*","",c,flags=re.S)
    c=re.sub(r"<h2[^>]*>Sources</h2>.*?(?=<h2|$)","",c,flags=re.S)
    t=re.sub(r"<[^>]+>"," ",c)
    return re.findall(r"[a-z0-9']+",t.lower())
def sh(w):return {" ".join(w[i:i+5]) for i in range(len(w)-4)}
P={};
for f in glob.glob('pages/*/*.json'):
    for p in json.load(open(f)):P[p['slug']]=body(p['content'])
S={s:sh(w) for s,w in P.items()}
df=collections.Counter()
for v in S.values():df.update(v)
res={}
for s,v in S.items():
    res[s]=(len(P[s]),(sum(1 for x in v if df[x]==1)/len(v)*100) if v else 0)
json.dump(res,open('/tmp/measure.json','w'))
u=[r[1] for r in res.values()];w=[r[0] for r in res.values()]
print('pages',len(res),'median words',statistics.median(w),'median uniq',round(statistics.median(u)))
print('>=80 uniq',sum(x>=80 for x in u),' >=1200 words',sum(x>=1200 for x in w))
for s in sys.argv[1:]:print(s,res.get(s))
