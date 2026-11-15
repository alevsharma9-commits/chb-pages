import json,glob,re,collections,html
def body(c):
    c=re.sub(r"<div class='wsp-hero'>.*?</iframe>",'',c,flags=re.S)
    return c
def ss(c):
    s=set()
    t=re.sub(r'<style>.*?</style>|<script.*?</script>','',c,flags=re.S)
    t=re.sub(r"<div class='wsp-related'>.*",'',t,flags=re.S);t=re.sub(r'<h2[^>]*>Sources</h2>.*','',t,flags=re.S)
    for blk in re.sub(r'<[^>]+>','\n',t).split('\n'):
        for x in re.split(r'(?<=[.!?])\s+',blk.strip()):
            if len(x.split())>=6:s.add(x)
    return s
F=sorted(glob.glob('pages/*/*.json'));D=[(f,json.load(open(f))) for f in F]
df=collections.Counter()
for f,d in D:
    for p in d: df.update(ss(p['content']))
DROP=sorted([s for s,n in df.items() if n>=25 and s[-1] in '.!?' and not s.startswith('Confirm details')],key=len,reverse=True)
print(len(DROP))
tot=0
for f,d in D:
    for p in d:
        c=p['content']
        # only touch the body before the related block and outside script/style
        head,sep,tail=c.partition("<div class='wsp-related'>")
        parts=re.split(r'(<script.*?</script>|<style.*?</style>|<h[1-3][^>]*>.*?</h[1-3]>)',head,flags=re.S)
        for i in range(0,len(parts),2):
            t=parts[i]
            for s in DROP:
                for v in {s,html.escape(s,quote=False),html.escape(s,quote=True),s.replace("'","&#x27;"),s.replace("'","&#039;")}:
                    if v in t: t=t.replace(' '+v,'').replace(v,'');tot+=1
            parts[i]=t
        head=''.join(parts)
        head=re.sub(r'<(p|li)>\s*</\1>','',head);head=re.sub(r'<(p|li)><strong>[^<]{0,50}</strong>\s*</\1>','',head)
        head=re.sub(r'<ul[^>]*>\s*</ul>|<ol[^>]*>\s*</ol>','',head)
        p['content']=head+sep+tail
    json.dump(d,open(f,'w'))
print('removals',tot)
