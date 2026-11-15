import json,glob,re
def title(s):return ' '.join(w.capitalize() for w in s.split('-'))
n=0
for f in sorted(glob.glob('pages/*/*.json')):
    d=json.load(open(f))
    for p in d:
        c=p['content'];o=c
        c=re.sub(r'<(p|li)>[^<]*(failed to scrape|not captured|scrape failed|could not be scraped)[^<]*</\1>','',c,flags=re.I)
        for _ in range(3):
            c=re.sub(r'<h2[^>]*>[^<]*</h2>\s*(?=<h2|<div class=.wsp-related|<div class=.wsp-back|$)','',c)
            c=re.sub(r'<h3[^>]*>[^<]*</h3>\s*(?=<h2|<h3|<div class=.wsp-related)','',c)
        m=re.match(r'(.+)-county-([a-z]{2})-',p['slug']) or re.match(r'sell-my-house-fast-(.+)-([a-z]{2})$',p['slug']) or re.match(r'(.+)-([a-z]{2})-[a-z-]+$',p['slug'])
        if m:
            nm=title(m.group(1))+(' County' if '-county-' in p['slug'] else '')
            c=re.sub(r'<p><em>General information for [^<]*?, not legal or tax advice\.',f'<p><em>This is general information about {nm}, not legal or tax advice.',c)
        c=re.sub(r'<(p|li)>\s*</\1>','',c)
        if c!=o:p['content']=c;n+=1
    json.dump(d,open(f,'w'))
print('changed',n)
