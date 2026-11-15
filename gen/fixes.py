# Remove old lines that newer sourced sections contradict. (slug, substring that identifies the <p>/<li> to drop)
import json,glob,re
FIX=[('iowa-capital-gains-tax','requires holding at least 10 years'),
     ('arkansas-estate-tax','2013'),
     ('oregon-homestead-exemption','up to $150,000'),
     ('polk-county-or-property-tax-guide','loaded blank via Firecrawl')]
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
# drop an empty "What we could not confirm" heading left after list items were removed
m=0
for f in glob.glob('pages/*/*.json'):
    items=json.load(open(f));ch=False
    for p in items:
        c=p['content']
        c2=re.sub(r"<h2[^>]*>What we could not confirm</h2>\s*(?=<h2|<div|$)","",c)
        if c2!=c:p['content']=c2;ch=True;m+=1
    if ch:json.dump(items,open(f,'w'))
print('empty headings removed',m)
