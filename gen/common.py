import html,json,re,os
HERE=os.path.dirname(__file__)
CSS=open(os.path.join(HERE,'assets','css.txt')).read()
SITE='https://cashhomebuyersca.com/'
DATE='November 14, 2026'
def esc(s): return html.escape(s,quote=True)
def wc(it): return len(re.sub(r'<[^>]+>',' ',re.sub(r'<style>.*?</style>|<script.*?</script>','',it['content'],flags=re.S)).split())
def ul(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def ol(items): return '<ol>'+''.join(f'<li>{i}</li>' for i in items)+'</ol>'
def a(slug,txt): return f"<a href='{SITE}{slug}/'>{txt}</a>"
def hero(state,h1,h2,p):
    return (f"<div class='wsp-hero'><div class='wsp-hero-inner'><div class='wsp-hero-left'><h1>{esc(h1)}</h1><div class=wsp-kicker>Cash Home Buyers in {state}</div><div class=wsp-speed><span>Cash Offer in 24 Hours</span></div><ul class=wsp-checks><li>Inherited, behind on payments, tenants, repairs: we buy it as-is</li><li>Zero fees, zero commissions, zero closing costs</li><li>No obligation: turn the offer down and owe us nothing</li></ul><h2>{esc(h2)}</h2><p>{esc(p)}</p><p><a class='wsp-btn-outline wsp-btn-call' href='tel:424-435-2326'>Call or Text <strong>&nbsp;(424) 435-2326</strong></a></p></div><div class='wsp-hero-right'><iframe src='https://connect.cashhomebuyersca.com/widget/form/zKzKbSeB3aqwWwE8NNxO' data-form-id='zKzKbSeB3aqwWwE8NNxO' title='Cash Offer Form'></iframe><br /><script src='https://connect.cashhomebuyersca.com/js/form_embed.js' async></script></div></div></div>")
def cta(k,t):
    return ('<div class="chb-cta" style="margin:32px 0;border-radius:10px;background:linear-gradient(120deg,#0F1C2E 0%,#16293F 100%);padding:28px 32px;display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;color:#fff;"><div style="max-width:600px;"><div style="font-size:12px;font-weight:800;letter-spacing:2px;color:#E0A83C;text-transform:uppercase;margin-bottom:6px;">'+esc(k)+'</div><div style="font-weight:800;font-size:20px;line-height:1.35;color:#fff;">'+esc(t)+'</div></div><a href="#" onclick="var f=document.querySelector(\'iframe[data-form-id]\');if(f){f.scrollIntoView({behavior:\'smooth\',block:\'center\'});return false;}" style="flex-shrink:0;padding:14px 24px;border-radius:8px;background:#E0A83C;color:#16203A;font-size:14px;font-weight:800;text-decoration:none;white-space:nowrap;">Get My Cash Offer &rarr;</a></div>')
def faq_html(faqs):
    return ''.join(f'<h3 class="wp-block-heading">{esc(q)}</h3><p>{esc(an)}</p>' for q,an in faqs)
def related(state,cards):
    return f"<div class='wsp-related'><h2>Related {state} guides</h2><div class='wsp-related-grid'>"+''.join(f"<div class='wsp-related-card'><a href='{SITE}{s}/'>{esc(t)}</a><p>{esc(d)}</p></div>" for s,t,d in cards)+'</div></div>'
def sources(items):
    return '<h2>Sources</h2><ul>'+''.join(f"<li><a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>{esc(t)}</a></li>" for t,u in items)+'</ul>'
def schema(faqs,crumbs):
    f={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":an}} for q,an in faqs]}
    b={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(crumbs)]}
    return '<script type="application/ld+json">'+json.dumps(f)+'</script><script type="application/ld+json">'+json.dumps(b)+'</script>'
def wrap(slug,title,hero_html,body,rm_title,rm_desc,fk):
    c='<!-- wp:html -->\n'+CSS+hero_html+"<div class='wsp-wrap'>"+body+'</div>\n<!-- /wp:html -->'
    assert '—' not in c and '–' not in c,slug
    assert len(rm_title)<=62 and len(rm_desc)<=155,(slug,len(rm_title),len(rm_desc))
    return dict(slug=slug,title=title,content=c,status='publish',rank_math_title=rm_title,rank_math_description=rm_desc,rank_math_focus_keyword=fk)
DISCLAIM=lambda st,prof:f"<p><em>This guide is general information, not legal or tax advice. Laws, forms and fees change, so confirm details with the official office or a {st} {prof}.</em></p>"
def clean_txt(t):
    return t.replace('—',', ').replace('–','-').replace('“','"').replace('”','"').replace('’',"'").strip()
