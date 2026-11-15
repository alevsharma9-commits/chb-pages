# Remove old lines that newer sourced sections contradict. (slug, substring that identifies the <p>/<li> to drop)
import json,glob,re
FIX=[('iowa-capital-gains-tax','requires holding at least 10 years'),
     ('arkansas-estate-tax','2013')]
n=0
for f in glob.glob('pages/*/*.json'):
    items=json.load(open(f));ch=False
    for p in items:
        for slug,key in FIX:
            if p['slug']!=slug:continue
            c=p['content'];a=c.find("<div class='chb-rw'>")
            if a<0:continue
            head=c[:a]
            head2=re.sub(r"<(p|li)\b[^>]*>(?:(?!</\1>).)*"+re.escape(key)+r"(?:(?!</\1>).)*</\1>","",head,flags=re.S)
            if head2!=head:p['content']=head2+c[a:];ch=True;n+=1
    if ch:json.dump(items,open(f,'w'))
print('fixes',n)
