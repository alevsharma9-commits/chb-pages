"""Usage: python3 gen/rw/overlap.py slug [slug...]
Share of a draft's 5-word phrases that appear on no other page or unmerged draft. Target: 85+."""
import json,glob,re,collections,sys,os
R='/home/claude/chb-pages/'
def words(t):
    t=re.sub(r"<[^>]+>"," ",t);return re.findall(r"[a-z0-9']+",t.lower())
def sh(w):return {" ".join(w[i:i+5]) for i in range(len(w)-4)}
def draft(d):
    return words(' '.join(s['h2']+' '+s['html'] for s in d['sections'])+' '+' '.join(f['q']+' '+f['a'] for f in d['faqs']))
fin=set(open(R+'gen/rw/finished.txt').read().split());done=set()
for b in fin:
    f=R+f'gen/rw/batches/{b}.txt'
    if os.path.exists(f):done|={l.split('|')[0].strip() for l in open(f) if l.strip()}
mine=set(sys.argv[1:]);df=collections.Counter()
for f in glob.glob(R+'pages/*/*.json'):
    for p in json.load(open(f)):
        if p['slug'] in mine:continue
        c=re.sub(r"<script.*?</script>|<style.*?</style>","",p['content'],flags=re.S)
        c=re.sub(r"<h2[^>]*>Sources</h2>.*?(?=<h2|$)","",c,flags=re.S)
        df.update(sh(words(c)))
for f in glob.glob(R+'gen/rw/*.json'):
    s=os.path.basename(f)[:-5]
    if s in mine or s in done:continue
    try:df.update(sh(draft(json.load(open(f)))))
    except Exception:pass
for s in sys.argv[1:]:
    S=sh(draft(json.load(open(R+f'gen/rw/{s}.json'))))
    rep=[x for x in S if df[x]]
    print(s,'unique %.0f%%'%(100*(1-len(rep)/len(S))))
    if len(sys.argv)==2 or 1-len(rep)/len(S)<.85:
        print('  repeated phrases elsewhere (sample):',sorted(rep,key=lambda x:-df[x])[:60])
