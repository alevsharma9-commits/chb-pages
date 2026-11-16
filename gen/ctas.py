# Add mid-page CTA bands to every rebuilt page (same look as the top CTA).
# Inserted before every 3rd body H2 (max 3), never inside FAQs or link blocks.
# Idempotent: bands carry class chb-cta-x and are removed before re-inserting.
# Copy and button sit in ONE inner div so measure.py's chb-cta strip removes it (template text, not page text).
import json, glob, re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
BTN = ("<a href=\"#\" onclick=\"var f=document.querySelector('iframe[data-form-id]');if(f){f.scrollIntoView({behavior:'smooth',block:'center'});return false;}\" "
       "style=\"flex-shrink:0;padding:14px 24px;border-radius:8px;background:#E0A83C;color:#16203A;font-size:14px;font-weight:800;text-decoration:none;white-space:nowrap;\">{b} &rarr;</a>")
BOX = ('<div class="chb-cta chb-cta-x" style="margin:32px 0;border-radius:10px;background:linear-gradient(120deg,#0F1C2E 0%,#16293F 100%);padding:24px 28px;'
       'color:#fff;"><div style="display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;"><span style="display:block;max-width:600px;font-weight:800;font-size:19px;line-height:1.35;color:#fff;">'
       '<span style="display:block;font-size:12px;letter-spacing:2px;color:#E0A83C;text-transform:uppercase;margin-bottom:6px;">{k}</span>{t}</span>' + BTN + '</div></div>')
COPY = [('Free, no-obligation offer', 'Tell us about your {p} house and get a written cash offer within 24 hours.', 'Get My Cash Offer'),
        ('Sell as-is', 'No repairs, no cleaning and no showings. We buy {p} houses in any condition.', 'See My Cash Offer'),
        ('You pick the closing date', 'Close in as little as 7 days or on the date that works for you, with no fees or commissions.', 'Get My Cash Offer')]
RX_OLD = re.compile(r'<div class="chb-cta chb-cta-x".*?&rarr;</a></div>(</div>)?', re.S)
n = 0
for f in sorted(glob.glob('pages/*/*.json')):
    ps = json.load(open(f)); ch = False
    for p in ps:
        c = RX_OLD.sub('', p['content'])
        m = re.search(r'Selling in ([^<?]+)\?', c)
        place = m.group(1).strip() if m else 'your'
        place = 'your' if len(place) > 40 else place
        top = c.find('chb-cta"')
        end = min([x for x in (c.find('>Frequently'), c.find('>Common questions'), c.find("<div class='wsp-related'"), c.find('application/ld+json')) if x > 0] or [len(c)])
        h2 = [h.start() for h in re.finditer(r'<h2[ >]', c) if top < h.start() < end]
        spots = h2[3::3][:3]
        for i, pos in reversed(list(enumerate(spots))):
            k, t, b = COPY[i % 3]
            c = c[:pos] + BOX.replace('{k}', k).replace('{t}', t.replace('{p}', place).replace('your your', 'your').replace('buy your houses', 'buy houses')).replace('{b}', b) + c[pos:]
        if c != p['content']: p['content'] = c; ch = True; n += 1
    if ch: json.dump(ps, open(f, 'w'))
print('ctas on', n)
