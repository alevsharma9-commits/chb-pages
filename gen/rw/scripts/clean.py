import json,re,sys
src,dst=sys.argv[1:3]
t=open(src).read()
try:
    j=json.loads(t)
    if isinstance(j,list): j=json.loads(j[0]['text'])
    t=j.get('markdown',t)
except Exception: pass
t=t.replace('\\n','\n')
t=re.sub(r'!\[[^\]]*\]\([^)]*\)','',t)
t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)
t=re.sub(r'\n\s*\n+','\n',t)
open(dst,'w').write(t)
print(dst,len(t))
