import json,re,sys
d=json.load(open(sys.argv[1]))
t=' '.join(re.sub(r'<[^>]+>',' ',s['html'])+' '+s['h2'] for s in d['sections'])+' '+' '.join(q['q']+' '+q['a'] for q in d['faqs'])
print(len(t.split()), len(d['sources']), '—' in t or '–' in t)
