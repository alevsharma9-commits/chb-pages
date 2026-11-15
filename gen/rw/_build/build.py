import sys, json, re, runpy
name=sys.argv[1]
ns=runpy.run_path(f'/home/claude/chb-pages/gen/rw/_build/{name}.py')
def wc(h): return len(re.sub(r'<[^>]+>',' ',h).split())
n=sum(wc(s['h2'])+wc(s['html']) for s in ns['sections'])+sum(wc(f['q'])+wc(f['a']) for f in ns['faqs'])
for x in ns['sections']:
    if not x['html'].rstrip().endswith('>'): x['html']=x['html'].rstrip()+'</p>'
body=json.dumps([ns["sections"],ns["faqs"],ns["sources"]],ensure_ascii=False)
assert '—' not in body and '–' not in body
json.dump({"slug":ns['slug'],"sections":ns['sections'],"faqs":ns['faqs'],"sources":ns['sources']},open(f"/home/claude/chb-pages/gen/rw/{ns['slug']}.json",'w'),indent=1,ensure_ascii=False)
print(ns['slug'],n,len(ns['sources']))
