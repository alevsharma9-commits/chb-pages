"""Usage: python3 gen/rw/polishcheck.py slug [slug...]  Checks gen/rw/polish/<slug>.json against the original gen/rw/<slug>.json."""
import json,re,sys,glob,os,collections
R=os.environ.get('CHB_ROOT','/home/claude/chb-pages/')
def words(t):
    t=re.sub(r"<[^>]+>"," ",t);return re.findall(r"[a-z0-9']+",t.lower())
def sh(w):return {" ".join(w[i:i+5]) for i in range(len(w)-4)}
def txt(d):return ' '.join(s['h2']+' '+s['html'] for s in d['sections'])+' '+' '.join(f['q']+' '+f['a'] for f in d['faqs'])
BAD=[(r'Wikipedia|QuickFacts|Quick Facts','source name-drop'),
 (r'\b(could not|couldn\'t|did not|didn\'t) (confirm|find|verify|open|locate)|\bunconfirmed\b|we (left|have left) out|not (publish|list|state|say|give|name)(ed|s)?\b[^.]{0,60}\b(official|county|city|page|site|source)|does not (say|list|give|state|match)|do(es)? not (publish|name)|still lists|out of date','research-gap or conflict note'),
 (r'\b(has|have) passed\b','expired item'),
 (r'than in [A-Z][\w ]+ (County|Parish)|of the (four|three|five|six) (cities|counties|towns)|in this series|other (cities|counties) covered','sibling comparison'),
 (r'[–—]','dash'),(r'\blicensed\b','"licensed"'),
 (r'it is worth (noting|knowing)|keep in mind|\bnavigat|\blandscape\b|\bcrucial\b|\brobust\b|\bseamless|delve|in today','filler word'),
 (r'(?i)<th>\s*Sources?\s*</th>|The table (below )?(collects|gathers|lists|shows|pulls)|<th>\s*(Item|Fact)\s*</th>','table style'),
 (r'(?i)\b(veterans|broadband|poverty|bachelor|labor force|payroll)\b','Census trivia'),
 (r'(?i)\baccording to\b|\bper the\b','attribution')]
def nums(t):return set(re.findall(r'\d[\d,.]*\d|\d',re.sub(r'<[^>]+>',' ',t)))
mine=set(sys.argv[1:]);df=collections.Counter();loaded=False
def build():
    global loaded
    for f in glob.glob(R+'pages/*/*.json'):
        for p in json.load(open(f)):
            if p['slug'] in mine:continue
            c=re.sub(r"<script.*?</script>|<style.*?</style>","",p['content'],flags=re.S)
            df.update(sh(words(c)))
    loaded=True
for s in sys.argv[1:]:
    probs=[]
    try:
        n=json.load(open(R+f'gen/rw/polish/{s}.json'));o=json.load(open(R+f'gen/rw/{s}.json'))
    except Exception as e:
        print(s,'FAIL cannot read/parse:',e);continue
    t=txt(n);w=len(words(t))
    if w<1300:probs.append(f'only {w} words (need 1300+)')
    if len(n['faqs'])!=5:probs.append(f"{len(n['faqs'])} faqs (need 5)")
    if n.get('sources')!=o.get('sources'):probs.append('sources changed')
    for r,name in BAD:
        m=re.search(r,t)
        if m:probs.append(f'{name}: "...{t[max(0,m.start()-30):m.end()+30]}..."'.replace('\n',' '))
    new=[x for x in nums(t)-nums(txt(o)) if len(re.sub(r'\D','',x))>=2]
    if new:probs.append('new numbers not in original: '+', '.join(sorted(new)[:8]))
    hs=[x['h2'] for x in n['sections']];q=sum(h.strip().endswith('?') for h in hs)
    if hs and q/len(hs)>.6:probs.append(f'{q} of {len(hs)} headings are questions (aim for about half)')
    if sum('<table' in x['html'] for x in n['sections'])!=1:probs.append('need exactly one table')
    if not loaded:build()
    S=sh(words(t));u=100*sum(1 for x in S if not df[x])/max(1,len(S))
    if u<82:probs.append(f'only {u:.0f}% unique (need 82+); reword place-specific passages')
    print(s,'OK' if not probs else 'FIX',f'words={w} unique={u:.0f}%')
    for p in probs:print('   -',p)
