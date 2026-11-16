import json,sys
def w(slug,sections,faqs):
    o=json.load(open(f'/home/claude/chb-pages/gen/rw/{slug}.json'))
    json.dump({'slug':slug,'sections':[{'h2':h,'html':t} for h,t in sections],'faqs':[{'q':q,'a':a} for q,a in faqs],'sources':o['sources']},open(f'/home/claude/chb-pages/gen/rw/polish/{slug}.json','w'),indent=1)
