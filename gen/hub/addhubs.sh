#!/bin/bash
# usage: addhubs.sh code... ; builds hubs and puts them first in manifest
cd /home/claude/chb-pages
python3 gen/hub/build_hub.py "$@" || exit 1
python3 - "$@" <<'P'
import json,sys,glob
m=json.load(open('manifest.json'))
have={b['file'] for b in m['batches']}
new=[]
for c in sys.argv[1:]:
    for f in glob.glob(f'pages/{c}/*-hub-1.json'):
        if f not in have: new.append({'file':f})
m['batches']=new+m['batches']
json.dump(m,open('manifest.json','w'))
P
