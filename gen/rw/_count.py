import json,re,sys
for s in sys.argv[1:]:
    d=json.load(open(f'/home/claude/chb-pages/gen/rw/{s}.json'))
    t=' '.join(x['h2']+' '+re.sub(r'<[^>]+>',' ',x['html']) for x in d['sections'])+' '+' '.join(f['q']+' '+f['a'] for f in d['faqs'])
    print(s,len(t.split()),len(d['sources']), 'dash' if re.search('[–—]',json.dumps(d,ensure_ascii=False)) else 'nodash')
