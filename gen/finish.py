import json,glob,re,collections,sys,subprocess
codes=sys.argv[1:]
m=json.load(open('manifest.json')); have={b['file'] for b in m['batches']}
for c in codes:
    for f in sorted(glob.glob(f'pages/{c}/*.json')):
        if f not in have: m['batches'].append({'file':f})
json.dump(m,open('manifest.json','w'))
allp={};sl=collections.Counter()
for b in m['batches']:
    for p in json.load(open(b['file'])): sl[p['slug']]+=1; allp[p['slug']]=p
bad=0
for s,p in allp.items():
    if re.search('[—–]',p['content']): bad+=1; print('dash',s)
    for l in set(re.findall(r'href="https://cashhomebuyersca.com/([^/"#]+)/?"',p['content'])):
        if l not in allp: bad+=1; print('broken',s,l)
    if len(p['rank_math_title'])>62 or len(p['rank_math_description'])>155: bad+=1; print('len',s)
print(len(sl),'dups',[k for k,v in sl.items() if v>1][:5],'bad',bad)
