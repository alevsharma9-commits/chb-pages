import json,glob,re,sys
DROP=re.compile(r"^(What a cash sale of a |Documents and information to have ready|Listing, selling it yourself or a cash offer|Questions to ask before you sell in |More questions about selling in |.* rules that can affect a sale in )")
END=re.compile(r"<h2[ >]|<div class='wsp-related'>|<div class=\"chb-cta\"|<div class='wsp-back'>")
def trim(c):
    out=[];i=0;n=0
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>',c,re.S):
        if m.start()<i: continue
        if DROP.search(re.sub(r'<[^>]+>','',m.group(1))):
            e=END.search(c,m.end()); e=e.start() if e else len(c)
            out.append(c[i:m.start()]); i=e; n+=1
    out.append(c[i:]); return ''.join(out),n
tot=0;pages=0
for f in sorted(glob.glob('pages/*/*.json')):
    d=json.load(open(f));ch=False
    for p in d:
        c,n=trim(p['content'])
        if n: p['content']=c; tot+=n; pages+=1; ch=True
    if ch: json.dump(d,open(f,'w'))
print('pages trimmed',pages,'sections removed',tot)
