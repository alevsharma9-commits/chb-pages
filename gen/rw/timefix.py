"""Drop sentences that pin the text to a specific 'today' (they go stale once live). Usage: python3 gen/rw/timefix.py [slug...] (default: all drafts)"""
import json,re,glob,os,sys
PAT=re.compile(r"\b(today is|today being|as of today|today,? (is|being)|with today|because today|since today|as of (november|nov\.?) 15, 2026|with the date at|on (sunday, )?november 15, 2026|november 15, 2026 (is|was|falls)|in about (two|six|three|four|five|a few) (weeks|days)|right now|this month\b)",re.I)
def fix(s):
    parts=re.split(r'(<[^>]+>)',s);n=0
    for i,p in enumerate(parts):
        if p.startswith('<') or not PAT.search(p):continue
        sents=re.split(r'(?<=[.!?])\s+',p)
        keep=[x for x in sents if not PAT.search(x)]
        n+=len(sents)-len(keep);parts[i]=' '.join(keep)
    out=''.join(parts)
    out=re.sub(r'<p>\s*</p>','',out);out=re.sub(r'<li>\s*</li>','',out)
    return out,n
tot=0;chg=[]
files=[f'gen/rw/{a}.json' for a in sys.argv[1:]] or [f for f in glob.glob('gen/rw/*.json')]
for f in files:
    try:d=json.load(open(f))
    except Exception:continue
    if not isinstance(d,dict) or 'sections' not in d:continue
    n=0
    for sec in d['sections']:
        sec['html'],k=fix(sec['html']);n+=k
    for q in d.get('faqs',[]):
        q['a'],k=fix(q['a']);n+=k
    if n:
        json.dump(d,open(f,'w'),ensure_ascii=False);chg.append((os.path.basename(f)[:-5],n));tot+=n
print('removed',tot,'sentences in',len(chg),'files')
open('/tmp/timefix_changed.txt','w').write('\n'.join(s for s,_ in chg))
