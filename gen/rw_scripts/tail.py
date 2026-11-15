def wc(t): return len(re.sub(r'<[^>]+>',' ',t).split())
n=sum(wc(s['h2'])+wc(s['html']) for s in S)+sum(wc(q)+wc(a) for q,a in F)
out={"slug":slug,"sections":S,"faqs":[{"q":q,"a":a} for q,a in F],"sources":[{"title":t,"url":u} for t,u in SRC]}
bad=[c for c in json.dumps(out,ensure_ascii=False) if c in '–—']
json.dump(out,open(f'/home/claude/chb-pages/gen/rw/{slug}.json','w'),ensure_ascii=False,indent=1)
print(slug,n,len(SRC),'dashes',len(bad))
