# Strip "research notes" sentences from rewrite drafts: lines where the text talks about our own checking
# ("We could not find...", "We did not open...", "This page does not state...", "We confirmed X only...").
# Readers do not need them. Also drops "sourced" from headings ("X at a glance: sourced numbers").
import json, glob, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
META = re.compile(r"(?:(?<=[>.!?])|^)\s*[^<>.!?]*?\b(?:we|this page|this guide|our (?:check|review|research))\b[^<>.!?]{0,60}?\b(?:could not|couldn't|did not|didn't|do not have|cannot|can't|were unable|was unable|does not|doesn't|confirmed|verified|checked|found no|have not|haven't)\b(?!\s+(?:charge|buy|need|ask|require))[^<>]*?[.!?](?=\s|<|$)", re.I)
SAFE = re.compile(r"\bwe (?:buy|pay|close|cover|charge|make|handle|can|will|also|do not charge|don't charge)\b", re.I)
def clean(s):
    def rep(m):
        t = m.group(0)
        return t if SAFE.search(t) else ''
    s = META.sub(rep, s)
    s = re.sub(r'<li>\s*</li>', '', s); s = re.sub(r'<p>\s*</p>', '', s); s = re.sub(r'<ul>\s*</ul>', '', s)
    return re.sub(r'  +', ' ', s)
n = cut = 0
for f in glob.glob('*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    if not isinstance(d, dict) or not d.get('sections'): continue
    before = json.dumps(d)
    d['sections'] = [s for s in d['sections'] if not re.search(r'did we leave out|we left out', s['h2'], re.I)]
    for s in d['sections']:
        s['html'] = s['html'].replace('<th>What we confirmed</th>', '<th>Detail</th>')
        s['h2'] = re.sub(r':?\s*sourced (numbers|figures|facts)', '', s['h2'], flags=re.I).strip()
        old = s['html']; s['html'] = clean(old); cut += old != s['html']
    for q in d.get('faqs', []):
        q['a'] = clean(q['a']).strip() or q['a']
    if json.dumps(d) != before: json.dump(d, open(f, 'w'), ensure_ascii=False, indent=1); n += 1
print('drafts cleaned', n, 'sections changed', cut)
