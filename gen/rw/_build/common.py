import json,re
def emit(slug,S,F,src):
    t=lambda s:len(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',s)).split())
    n=sum(t(x)+t(h) for h,x in S)+sum(t(q)+t(x) for q,x in F)
    json.dump({"slug":slug,"sections":[{"h2":h,"html":x} for h,x in S],"faqs":[{"q":q,"a":x} for q,x in F],"sources":[{"title":a,"url":b} for a,b in src]},open(f'/home/claude/chb-pages/gen/rw/{slug}.json','w'),indent=1)
    print(slug,n,len(src))
