# Site-wide mechanical readability fixes from the humanizer audit. Runs every cycle after metaclean.py. Idempotent.
import json, glob, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
CAP = lambda m: m.group(m.lastindex).upper()
SRC = r'(?:<a [^>]*>\s*)?(?:Wikipedia|the Census Bureau(?:\'s)? QuickFacts|Census Bureau QuickFacts|Census QuickFacts|QuickFacts)(?:\s*</a>)?'
VERB = r'(?:says|notes|lists|reports|records|states|gives|puts|describes|shows|counts|estimates)'
def body(t):
    # 1. source named mid-sentence: drop the attribution, keep the fact
    t = re.sub(r'\b[Aa]ccording to ' + SRC + r'(?:\'s [\w ]{1,30}?)?, (\w)', lambda m: m.group(1).upper(), t)
    t = re.sub(r',? according to ' + SRC + r'(?:\'s [\w ]{1,30}?)?(?=[.,;])', '', t)
    t = re.sub(r'(?<=[.>!?] )' + SRC + r'(?:\'s (?:entry|article|page))? ' + VERB + r' (?:that )?(\w)', lambda m: m.group(1).upper(), t)
    t = re.sub(r'(?<=>)' + SRC + r'(?:\'s (?:entry|article|page))? ' + VERB + r' (?:that )?(\w)', lambda m: m.group(1).upper(), t)
    t = re.sub(r'\s*\((?:source: )?' + SRC + r'(?:, [^)]{1,40})?\)', '', t)
    t = re.sub(r',? (?:per|from) ' + SRC + r'(?=[.,;])', '', t)
    # 2. worked-example hedge
    t = re.sub(r'As an illustration only, (\w)', lambda m: 'For example, ' + m.group(1).lower(), t)
    t = re.sub(r'\s*This is an illustration only\.', '', t)
    # 3. tables: "The table below collects..." lead-ins, source tags in captions, Source columns, "Source: Wikipedia" lines
    t = re.sub(r'<p>\s*The table (?:below )?(?:collects|gathers|lists|shows|summarizes|pulls together|brings together)[^<]*</p>', '', t)
    t = re.sub(r'(<caption>[^<]*?)\s*\((?:source: )?[^)]*(?:QuickFacts|Census|page|Wikipedia|site)[^)]*\)', r'\1', t)
    t = re.sub(r'<p>\s*(?:<em>)?Source: Wikipedia[^<]*(?:</em>)?</p>', '', t)
    t = re.sub(r'<th>Detail from (?:the source|Wikipedia|the [\w ]+)</th>', '<th>Detail</th>', t)
    t = re.sub(r'<table>.*?</table>', drop_source_col, t, flags=re.S)
    # 4. headings
    t = re.sub(r'<h2([^>]*)>More questions about [^<]+</h2>', r'<h2\1>Frequently asked questions</h2>', t)
    t = re.sub(r'Counties and Cities We Buy Houses In Across ([^<]+)', r'Counties and cities we buy in across \1', t)
    return t
def drop_source_col(m):
    tb = m.group(0)
    hdr = re.search(r'<tr>(.*?)</tr>', tb, re.S)
    if not hdr: return tb
    ths = re.findall(r'<t[hd][^>]*>.*?</t[hd]>', hdr.group(1), re.S)
    idx = [i for i, h in enumerate(ths) if re.fullmatch(r'<th[^>]*>\s*Sources?\s*</th>', h)]
    if not idx or len(ths) < 3: return tb
    k = idx[0]
    def row(r):
        cells = re.findall(r'<t[hd][^>]*>.*?</t[hd]>', r.group(1), re.S)
        if len(cells) != len(ths): return r.group(0)
        return '<tr>' + ''.join(c for i, c in enumerate(cells) if i != k) + '</tr>'
    return re.sub(r'<tr>(.*?)</tr>', row, tb, flags=re.S)
n = 0
for f in sorted(glob.glob('pages/*/*.json')):
    ps = json.load(open(f)); ch = False
    for p in ps:
        c = p['content']
        parts = re.split(r'(<style.*?</style>|<script.*?</script>)', c, flags=re.S)
        c2 = ''.join(x if x.startswith(('<style', '<script')) else body(x) for x in parts)
        if c2 != c: p['content'] = c2; ch = True; n += 1
    if ch: json.dump(ps, open(f, 'w'))
print('humanfix on', n)
