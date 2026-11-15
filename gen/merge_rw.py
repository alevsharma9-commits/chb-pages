import json,glob,re,html,os
def esc(s):return html.escape(s,quote=False)
RW={}
for f in glob.glob('gen/rw/*.json'):
    try:d=json.load(open(f));RW[d['slug']]=d
    except Exception as e:print('bad',f,e)
n=0
for f in sorted(glob.glob('pages/*/*.json')):
    items=json.load(open(f));ch=False
    for p in items:
        d=RW.get(p['slug'])
        if not d or 'chb-rw' in p['content']:continue
        c=p['content']
        secs=''.join(f"<h2>{esc(s['h2'])}</h2>{s['html']}" for s in d['sections'])
        blk=f"<div class='chb-rw'>{secs}</div>"
        # faqs: append to FAQ section or create
        faqs=d.get('faqs',[])
        if faqs:
            fh=''.join(f'<h3 class="wp-block-heading">{esc(q["q"])}</h3><p>{esc(q["a"])}</p>' for q in faqs)
            blk+=f"<h2>More questions about {esc(re.sub(r'<[^>]+>','',re.search(r'<h1>(.*?)</h1>',c).group(1)).split(':')[0].replace('Sell My House Fast in ',''))}</h2>"+fh
            ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q['q'],"acceptedAnswer":{"@type":"Answer","text":q['a']}} for q in faqs]}
            blk+='<script type="application/ld+json">'+json.dumps(ld)+'</script>'
        i=c.find("<div class='wsp-related'>")
        if i<0:i=c.find('<h2>Sources</h2>')
        c=c[:i]+blk+c[i:]
        # sources
        src=''.join(f"<li><a href='{s['url']}'>{esc(s['title'])}</a></li>" for s in d.get('sources',[]))
        m=re.search(r'(<h2[^>]*>Sources</h2>\s*<ul>)',c)
        if m and src:c=c[:m.end()]+src+c[m.end():]
        p['content']=c;ch=True;n+=1
    if ch:json.dump(items,open(f,'w'))
print('merged',n,'of',len(RW))
