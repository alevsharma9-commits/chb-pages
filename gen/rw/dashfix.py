import glob,re
for p in glob.glob('gen/rw/*.json'):
    t=open(p).read()
    t2=re.sub(r'\s*(—|\\u2014|&mdash;)\s*',', ',t);t2=re.sub(r'(–|\\u2013|&ndash;)',' to ',t2)
    if t2!=t:open(p,'w').write(t2);print('dashfix',p)
