# Rebuild the related-links blocks on every city, county and state topic page.
# Uses the county maps in gen/hub/out/<code>.json: state hub -> counties -> cities, and back up.
# Idempotent: strips existing wsp-related blocks and re-inserts fresh ones at the same spot.
import json, glob, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
SITE = 'https://cashhomebuyersca.com/'
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace("'", '&#39;')
def short(t): return re.split(r'[:|]', t)[0].strip()

files = {f: json.load(open(f)) for f in sorted(glob.glob('pages/*/*.json'))}
P = {p['slug']: p for ps in files.values() for p in ps}
EXTRA = {'for-sale-by-owner-florida': 'fl', 'lady-bird-deed-texas': 'tx', 'for-sale-by-owner-texas': 'tx'}

home = {}   # slug -> (code, county index) for county and city pages
topic = {}  # slug -> code
ST = {}
for f in sorted(glob.glob('gen/hub/out/*.json')):
    code = f.split('/')[-1][:-5]
    d = json.load(open(f)); fx = json.load(open(f'gen/hub/facts/{code}.json'))
    sl = fx['state_slug']; name = ' '.join(w.capitalize() for w in sl.split('-'))
    titles = {s: t for k in ('city_pages', 'city_tax_guides', 'county_pages', 'state_topic_pages') for s, t in fx[k]}
    dirs = [p['slug'] for f2, ps in files.items() if f2.startswith(f'pages/{code}/') and 'directory' in f2 for p in ps]
    topics = [s for s, _ in fx['state_topic_pages'] if s in P and s not in dirs] + [s for s, c in EXTRA.items() if c == code and s in P]
    ST[code] = dict(name=name, hub='we-buy-houses-in-' + sl, counties=d['counties'], titles=titles, topics=topics, dirs=dirs)
    for i, c in enumerate(d['counties']):
        for s in c.get('county_slugs', []): home[s] = (code, i)
        for ci in c.get('cities', []): home[ci['slug']] = (code, i)
    for s in topics: topic[s] = code

def label(code, s, cityname=None):
    st = ST[code]
    if s.startswith('sell-my-house-fast-'): return f'Sell a house in {cityname}', 'Cash offer and local selling guide'
    if s.endswith('-property-tax-guide') and cityname: return cityname, 'Tax bills, dates and appeals'
    t = short(st['titles'].get(s) or P[s]['rank_math_title'])
    if 'property-tax' in s: return t, 'Tax offices, due dates and appeals'
    if 'record' in s or 'deeds' in s or 'recorder' in s or 'clerk' in s: return t, 'Deeds, records and recording fees'
    return t, 'Statewide rules for sellers'

def block(h2, cards):
    if not cards: return ''
    return (f"<div class='wsp-related'><h2>{esc(h2)}</h2><div class='wsp-related-grid'>" +
            ''.join(f"<div class='wsp-related-card'><a href='{SITE}{s}/'>{esc(t)}</a><p>{esc(d)}</p></div>" for s, t, d in cards) +
            '</div></div>')

def state_cards(code, me, n=5):
    st = ST[code]
    cards = [(st['hub'], f"We buy houses in {st['name']}", 'All counties and cities we cover')]
    cards += [(s, 'All ' + st['name'] + ' pages', 'Full list of local guides') for s in st['dirs']]
    cards += [(s, *label(code, s)) for s in st['topics'] if s != me][:n]
    return cards

def build(slug):
    if slug in home:
        code, i = home[slug]; st = ST[code]; c = st['counties'][i]
        cities = [(ci['slug'], ci['name']) for ci in c.get('cities', []) if ci['slug'] in P]
        county = [(s, *label(code, s)) for s in c.get('county_slugs', []) if s != slug and s in P]
        if slug in c.get('county_slugs', []):  # county page: link down to every city
            out = block(f"Cities and towns in {c['name']}", [(s, *label(code, s, n)) for s, n in cities])
            out += block(f"More {c['name']} guides", county)
        else:  # city page: link up to its county, its sibling page, then nearby cities
            base = re.sub(r'^sell-my-house-fast-|-property-tax-guide$', '', slug)
            pair = [(s, *label(code, s, n)) for s, n in cities if s != slug and re.sub(r'^sell-my-house-fast-|-property-tax-guide$', '', s) == base]
            sib = [(s, n) for s, n in cities if s.startswith('sell-my-house-fast-') and s != slug and (s, n) not in [(p[0], None) for p in pair]]
            k = next((j for j, (s, _) in enumerate(sib) if s > slug), len(sib))
            sib = (sib[k:] + sib[:k])[:10]
            out = block(f"{c['name']} guides", pair + county)
            out += block(f"Other cities in {c['name']}", [(s, *label(code, s, n)) for s, n in sib if s not in [p[0] for p in pair]])
        return out + block(f"{st['name']} seller guides", state_cards(code, slug))
    if slug in topic:
        code = topic[slug]; st = ST[code]
        big = sorted(st['counties'], key=lambda c: -len(c.get('cities', [])))[:8]
        cc = [(c['county_slugs'][0], *label(code, c['county_slugs'][0])) for c in big if c.get('county_slugs') and c['county_slugs'][0] in P]
        return block(f"{st['name']} seller guides", state_cards(code, slug, 12)) + block(f"County guides in {st['name']}", cc)
    return None

RX = re.compile(r"<div class=.wsp-related.>(?:<h2>.*?</h2>)?<div class=.wsp-related-grid.>(?:\s*<div class=.wsp-related-card.>.*?</div>)*\s*</div></div>", re.S)
done = 0
for f, ps in files.items():
    ch = False
    for p in ps:
        new = build(p['slug'])
        if new is None: continue
        c = p['content']; m = list(RX.finditer(c))
        assert m, p['slug']
        c2 = c[:m[0].start()] + new + RX.sub('', c[m[0].end():])
        for l in re.findall(r"href='" + SITE + r"([^/']+)/'", new): assert l in P, (p['slug'], l)
        if c2 != c: p['content'] = c2; ch = True; done += 1
    if ch: json.dump(ps, open(f, 'w'))
print('interlinked', done)
