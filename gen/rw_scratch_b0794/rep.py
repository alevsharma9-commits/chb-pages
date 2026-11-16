import sys,re,json,runpy
src=open('/home/claude/chb-pages/gen/rw/overlap.py').read().split("for s in sys.argv[1:]:")[0]
exec(src)
for s in sys.argv[1:]:
    w=draft(json.load(open(R+f'gen/rw/{s}.json')))
    flag=[0]*len(w)
    for i in range(len(w)-4):
        if df[" ".join(w[i:i+5])]:
            for k in range(i,i+5): flag[k]=1
    out=[];cur=[]
    for x,f in zip(w,flag):
        if f: cur.append(x)
        elif cur: out.append(' '.join(cur));cur=[]
    if cur: out.append(' '.join(cur))
    print(s); [print('  ',o) for o in out]
