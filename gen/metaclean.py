# Page-level pass of the research-note cleanup (gen/rw/metafix.py) for text that does not come from rewrite drafts:
# state hubs, untouched topic pages and FAQ schema. Runs every cycle after cleanbase.py. Idempotent.
import json, glob, re, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
sys.path.insert(0, 'gen/rw'); os.environ['METAFIX_IMPORT'] = '1'
META = re.compile(r"(?:(?<=[>.!?\"])|^)\s*[^<>.!?\"]*?\b(?:we|this page|this guide|our (?:check|review|research)|pages we opened)\b[^<>.!?\"]{0,60}?\b(?:could not|couldn't|did not|didn't|do not have|cannot|can't|were unable|was unable|does not|doesn't|confirmed|verified|checked|found no|have not|haven't)\b(?!\s+(?:charge|buy|need|ask|require))[^<>\"]*?[.!?](?=\s|<|\"|$)", re.I)
SAFE = re.compile(r"\bwe (?:buy|pay|close|cover|charge|make|handle|can|will|also|do not charge|don't charge)\b|what we can and cannot do", re.I)
def clean(s):
    s = META.sub(lambda m: m.group(0) if SAFE.search(m.group(0)) else '', s)
    s = re.sub(r'<li>\s*</li>', '', s); s = re.sub(r'<p[^>]*>\s*</p>', '', s); s = re.sub(r'<ul>\s*</ul>', '', s)
    return s
n = 0
for f in sorted(glob.glob('pages/*/*.json')):
    ps = json.load(open(f)); ch = False
    for p in ps:
        c = p['content']
        parts = re.split(r'(<style.*?</style>)', c, flags=re.S)
        c2 = ''.join(x if x.startswith('<style') else clean(x) for x in parts)
        c2 = re.sub(r'What We Could and Could Not Confirm', 'What Sellers Should Know', c2)
        for k in ('title', 'rank_math_title'):
            if p.get(k): p[k] = p[k].replace('What We Could and Could Not Confirm', 'What Sellers Should Know')
        if c2 != c: p['content'] = c2; ch = True; n += 1
    if ch: json.dump(ps, open(f, 'w'))
print('meta lines cleaned on', n)
