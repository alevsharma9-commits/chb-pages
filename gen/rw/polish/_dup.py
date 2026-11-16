import sys,re,json,glob,collections
sys.argv=[sys.argv[0]]+sys.argv[1:]
R='/home/claude/chb-pages/'
exec(open(R+'gen/rw/polishcheck.py').read().split("mine=set")[0])
mine=set(sys.argv[1:]);df=collections.Counter()
for f in glob.glob(R+'pages/*/*.json'):
    for p in json.load(open(f)):
        if p['slug'] in mine:continue
        c=re.sub(r"<script.*?</script>|<style.*?</style>","",p['content'],flags=re.S);df.update(sh(words(c)))
for s in mine:
    n=json.load(open(R+f'gen/rw/polish/{s}.json'));ws=words(txt(n))
    bad=[i for i in range(len(ws)-4) if df[" ".join(ws[i:i+5])]]
    # merge runs
    runs=[];
    for i in bad:
        if runs and i<=runs[-1][1]:runs[-1][1]=i+5
        else:runs.append([i,i+5])
    for a,b in runs:print(' '.join(ws[a:b]))
