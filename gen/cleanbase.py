# Remove the old template sections that still sit above the rewritten body on every page that has a rewrite
# ("Who to contact in X", "What we confirmed on official pages", "Tax rate", "What we could not confirm",
#  "X at a glance", "Fees", "Local notes" and the like). The rewritten sections cover the same ground in readable prose.
# Keeps: the hero, the "Last updated" line, the top CTA band, and any content before the first old H2
# (state directory lists live there). Idempotent.
import json, glob, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
CTA = re.compile(r'<div class="chb-cta"(?! chb-cta-x).*?&rarr;</a></div>', re.S)
n = 0
for f in sorted(glob.glob('pages/*/*.json')):
    ps = json.load(open(f)); ch = False
    for p in ps:
        c = p['content']
        rw = c.find("<div class='chb-rw'>")
        w = c.find("<div class='wsp-wrap'>")
        if rw < 0 or w < 0 or w > rw: continue
        mid = c[w:rw]
        h = re.search(r'<h2[ >]', mid)
        if not h: continue
        old = mid[h.start():]
        ctas = CTA.findall(old)
        new = mid[:h.start()] + (ctas[0] if ctas else '')
        c2 = c[:w] + new + c[rw:]
        if c2 != c: p['content'] = c2; ch = True; n += 1
    if ch: json.dump(ps, open(f, 'w'))
print('old sections removed on', n)
