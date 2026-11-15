import json,re
def wc(d):
    t=' '.join(re.sub('<[^>]+>',' ',s['html'])+' '+s['h2'] for s in d['sections'])+' '+' '.join(f['q']+' '+f['a'] for f in d['faqs'])
    return len(t.split())
def out(d):
    n=wc(d)
    bad=[c for c in json.dumps(d,ensure_ascii=False) if c in '–—']
    print(d['slug'],n,len(d['sources']),'dashes',len(bad))
    json.dump(d,open('/home/claude/chb-pages/gen/rw/'+d['slug']+'.json','w'),indent=1,ensure_ascii=False)
