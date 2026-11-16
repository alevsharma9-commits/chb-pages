"""Copy every polish/<slug>.json that passes polishcheck over gen/rw/<slug>.json. Prints how many were applied and which failed."""
import subprocess,glob,os,shutil,sys
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/../..')
os.environ['CHB_ROOT']=os.getcwd()+'/'
import json
slugs=sorted(os.path.basename(f)[:-5] for f in glob.glob('gen/rw/polish/*.json') if not os.path.basename(f).startswith('_'))
if len(sys.argv)>1:  # batch numbers: only apply drafts of agents that have finished (an agent may still be editing others)
    B=json.load(open('gen/rw/polish_batches.json')); want={x for i in sys.argv[1:] for x in B[int(i)]}
    slugs=[x for x in slugs if x in want]
ok=[];bad=[]
for i in range(0,len(slugs),40):
    chunk=slugs[i:i+40]
    out=subprocess.run([sys.executable,'gen/rw/polishcheck.py']+chunk,capture_output=True,text=True,env=os.environ).stdout
    for l in out.splitlines():
        if l.startswith(tuple(chunk)) and ' OK ' in l: ok.append(l.split()[0])
        elif l and not l.startswith(' '): bad.append(l)
os.makedirs('gen/rw/polish_done',exist_ok=True)
for s in ok:
    shutil.copy(f'gen/rw/polish/{s}.json',f'gen/rw/{s}.json'); shutil.move(f'gen/rw/polish/{s}.json',f'gen/rw/polish_done/{s}.json')
print('applied',len(ok),'still failing',len(bad)); [print(' ',b) for b in bad[:10]]
