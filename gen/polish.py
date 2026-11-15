# For rewritten pages: drop old (pre-rewrite) paragraphs/list items whose text is mostly shared with other pages.
import json,glob,re,collections
def words(t):return re.findall(r"[a-z0-9']+",re.sub(r"<[^>]+>"," ",t).lower())
def sh(w):return {" ".join(w[i:i+5]) for i in range(len(w)-4)}
FILES=sorted(glob.glob('pages/*/*.json'));DATA={f:json.load(open(f)) for f in FILES}
def body(c):
    c=re.sub(r"<script.*?</script>|<style.*?</style>","",c,flags=re.S)
    c=re.sub(r"<div class=.wsp-hero.*?(?=<h2)","",c,count=1,flags=re.S)
    c=re.sub(r"<div class=.wsp-related.>.*?</div>","",c,flags=re.S)
    return c
df=collections.Counter()
for f,items in DATA.items():
    for p in items:df.update(sh(words(body(p['content']))))
EL=re.compile(r"<(p|li)\b[^>]*>(.*?)</\1>",re.S)
tot=0
for f,items in DATA.items():
    ch=False
    for p in items:
        c=p['content']
        if 'chb-rw' not in c:continue
        a=c.find("<div class='chb-rw'>");b=c.find('</script>',c.find('application/ld+json',a))
        zones=[(a,b)]
        hero_end=c.find("<div class='wsp-wrap'>")
        src=c.find('>Sources</h2>')
        out=[];last=0;rm=0
        for m in EL.finditer(c):
            s=m.start()
            if s<hero_end or (a<=s<=b) or (src>0 and s>src) or 'wsp-related' in c[max(0,s-300):s] and False:continue
            prev=c[max(0,s-6):s]
            if prev.endswith('</h3>'):continue  # keep FAQ answers
            if 'chb-cta' in c[max(0,s-200):s] or 'href=' in m.group(2) and 'tel:' in m.group(2):continue
            S=sh(words(m.group(2)))
            if len(S)<3:continue
            shared=sum(1 for x in S if df[x]>1)/len(S)
            if shared>0.3:
                out.append(c[last:s]);last=m.end();rm+=1
        if rm:
            c=''.join(out)+c[last:]
            c=re.sub(r"<ul>\s*</ul>|<ol>\s*</ol>|<p>\s*</p>","",c)
            c=re.sub(r"<h2[^>]*>[^<]*</h2>\s*(?=<h2)","",c)
            p['content']=c;ch=True;tot+=rm
    if ch:json.dump(items,open(f,'w'))
print('removed',tot)
