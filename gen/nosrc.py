import json,glob,re
n=0;left=0
for f in glob.glob('pages/*/*.json'):
    items=json.load(open(f));ch=False
    for p in items:
        c=p['content']
        c2=re.sub(r"<h2[^>]*>\s*Sources\s*</h2>\s*(<p>[^<]*</p>\s*)?<(ul|ol)>.*?</\2>","",c,flags=re.S)
        if c2!=c:p['content']=c2;ch=True;n+=1
        if re.search(r">\s*Sources\s*</h[23]>",c2):left+=1
    if ch:json.dump(items,open(f,'w'))
print('sources removed',n,'still present',left)
