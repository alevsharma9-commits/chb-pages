import json,glob,re,sys,os,hashlib
sys.path.insert(0,os.path.dirname(__file__))
from common import esc,a,wc,SITE,cta
R=os.path.join(os.path.dirname(__file__),'..')
TARGET=1250
STATE={'fl':'Florida','tx':'Texas','ny':'New York','pa':'Pennsylvania','il':'Illinois','oh':'Ohio','ga':'Georgia'}
SKIP=re.compile(r'^Sources$|could not|Related|How to sell|FAQ|at a glance|Situations|Three ways|Selling a ',re.I)
def wc_html(c): return len(re.sub(r'<[^>]+>',' ',re.sub(r'<style>.*?</style>|<script.*?</script>','',c,flags=re.S)).split())
def harvest(st):
    groups=[]
    for f in sorted(glob.glob(f'{R}/pages/{st}/*state-pages*.json')):
        for p in json.load(open(f)):
            body=p['content']; parts=re.split(r'(?=<h2[ >])',body); facts=[]
            for part in parts:
                m=re.match(r'<h2[^>]*>(.*?)</h2>',part,re.S)
                if not m or SKIP.search(m.group(1)): continue
                for li in re.findall(r'<li>(.*?)</li>',part,re.S):
                    t=re.sub(r'<[^>]+>','',li)
                    if 70<=len(t)<=650 and not re.search(r'could not|not confirmed|we did not',t,re.I): facts.append(li)
            if facts: groups.append(dict(slug=p['slug'],label=p['rank_math_focus_keyword'].title(),facts=facts[:8]))
    return groups
def seed(s): return int(hashlib.md5(s.encode()).hexdigest()[:8],16)
def blocks(st,S,N,kind,slug):
    sd=seed(slug); b=[]
    b.append(("A",f"<h2>What a cash sale of a {esc(N)} house looks like, step by step</h2><p>People often ask what actually happens after they contact a cash buyer. Here is the usual order of events for a house in {esc(N)}.</p>"+"<ol><li><strong>Tell us about the property.</strong> Use the form on this page or call or text (424) 435-2326. We ask about the address, the condition and what is going on, such as a mortgage, back taxes, tenants or an estate.</li><li><strong>Get a written cash offer.</strong> We review the details and send a written offer. There is no obligation, and you can turn it down and owe us nothing.</li><li><strong>Pick your closing date.</strong> You choose the timeline. Some owners need weeks to move out, and others want to close quickly.</li><li><strong>The title company handles the paperwork.</strong> It checks ownership, pays off any mortgage and any unpaid property tax from the proceeds, and records the deed.</li><li><strong>You receive the proceeds.</strong> Our offers carry no agent commission, no fees and no closing costs to you.</li></ol>"))
    b.append(("B",f"<h2>Documents and information to have ready</h2><p>You do not need everything below to get an offer, but each item makes the sale smoother and helps the title company work faster.</p><ul><li>The deed or other proof of who owns the property today.</li><li>A recent mortgage statement or a payoff figure from the lender.</li><li>The latest property tax bill, plus any notice of unpaid or delinquent tax.</li><li>Homeowners association details, including dues and any unpaid assessments, if there is an association.</li><li>Current leases and the tenants' contact information, if the house is rented.</li><li>Estate paperwork, such as letters from the court, if you inherited the house.</li><li>A short list of known repairs. We buy as-is, but honest information avoids surprises.</li></ul>"))
    b.append(("C",f"<h2>Listing, selling it yourself or a cash offer: how they compare</h2><p><strong>Listing with an agent</strong> can bring a higher headline price when a house is in good shape and you have time. You pay the commission agreed in your listing contract, and you usually handle repairs, showings and the buyer's inspection requests. Closing depends on the buyer's financing.</p><p><strong>Selling it yourself</strong> saves the listing commission but puts the marketing, the paperwork and the required {esc(S)} disclosures on you. You still need a title company or attorney to close.</p><p><strong>Taking a cash offer</strong> trades some of the headline price for speed and certainty. We buy as-is, so there are no repairs, no showings and no financing contingency. It tends to fit owners dealing with foreclosure pressure, an inherited house, back taxes, tenants or a move on a deadline. Compare every option on what you net after repairs, fees and carrying costs, not on the headline price.</p>"))
    q={"tax":"the tax collector","records":"the county recorder","city":"the title company","state":"the title company"}.get(kind,"the title company")
    b.append(("E",f"<h2>Questions to ask before you sell in {esc(N)}</h2><ul><li>Ask {q} what is owed and what the title company will need at closing.</li><li>Ask your lender for a written payoff figure good through your expected closing date, and ask whether there is a prepayment penalty.</li><li>Ask the county assessor whether a pending appeal or exemption affects the bill, and whether any exemption you receive ends when you sell.</li><li>If the house was inherited, ask the title company which court documents it needs before it will insure the sale.</li><li>If tenants live in the house, check the lease for its end date and any notice you must give.</li></ul><p>These are general questions to start a conversation, not legal advice. Rules in {esc(S)} change, so confirm details with the official office or a {esc(S)} attorney or tax professional.</p>"))
    faqs=[("How fast can I close on a cash sale?","You choose the closing date within what the title company needs to clear ownership and payoffs."),("Do I have to clean out or repair the house?","No. We buy houses as-is, so you do not need to make repairs before selling."),("Will you buy a house that has tenants in it?","Yes. We buy rentals as-is, occupied or vacant. Tell us about the lease when you request an offer."),("What if I owe more on the mortgage than the house is worth?","Tell us the payoff figure. A sale that does not cover the loan may need lender approval, so ask your lender about a short sale before you sign anything."),("Can I sell an inherited house before probate is finished?","It depends on who has legal authority to sign. The title company can tell you what court paperwork it needs."),("Is there any cost to request an offer?","No. Requesting an offer is free and carries no obligation.")]
    return b,faqs,sd
def expand_item(st,p,groups,kind):
    c=p['content']
    if wc_html(c)>=TARGET: return p
    S=STATE[st]; slug=p['slug']; N=p['rank_math_focus_keyword']
    m=re.search(r'<h1>(.*?)</h1>',c); h=m.group(1) if m else slug
    nm=re.sub(r'^(Sell My House Fast in |)(.*?)(, [A-Z]{2}).*$',r'\2',h) if kind!='state' else S
    nm=nm.replace('&#x27;',"'").replace('&amp;','&')
    bl,faqs,sd=blocks(st,S,nm,kind,slug)
    # fact groups
    own=[g for g in groups if g['slug']!=slug]
    order=[own[(sd+i)%len(own)] for i in range(len(own))] if own else []
    out=''; wcnow=wc_html(c)
    fixed=''.join(x[1] for x in bl)
    fixed+="<h2>More questions about selling in "+esc(nm)+"</h2>"+''.join(f"<h3 class=\"wp-block-heading\">{esc(q)}</h3><p>{esc(an)}</p>" for q,an in faqs)
    wcnow+=wc_html(fixed)
    facts_html=''; blks=''
    for g in order:
        if wcnow>=TARGET: break
        n_f=3 if wcnow<TARGET-300 else 2
        sel=list(dict.fromkeys(g['facts'][(sd+i)%len(g['facts'])] for i in range(min(n_f,len(g['facts'])))))
        blk=f"<h3 class=\"wp-block-heading\">{esc(g['label'])}</h3><ul>"+''.join(f'<li>{x}</li>' for x in sel)+f"</ul><p>Full guide: {a(g['slug'],esc(g['label']))}.</p>"
        blks+=blk; wcnow+=wc_html(blk)
    if blks: facts_html=f"<h2>{S} rules that can affect a sale in {esc(nm)}</h2><p>These points come from official {esc(S)} sources already cited on our guides. Follow the links for the full guide on each topic.</p>"+blks
    ins=facts_html+fixed
    # place before FAQ h2, else before related, else before sources
    for pat in (r"<h2>[^<]*FAQ</h2>",r"<div class='wsp-related'>",r"<h2>Sources</h2>"):
        mm=re.search(pat,c)
        if mm: c=c[:mm.start()]+ins+c[mm.start():]; break
    else: return p
    p=dict(p); p['content']=c; return p
def run(st):
    groups=harvest(st); print(st,'fact groups',len(groups),sum(len(g['facts']) for g in groups))
    tot=0; short=0
    for f in sorted(glob.glob(f'{R}/pages/{st}/*.json')):
        if 'directory' in f: continue
        d=json.load(open(f)); kind='state' if 'state-pages' in f else 'tax' if 'ptax' in f else 'records' if 'records' in f else 'city'
        out=[expand_item(st,p,groups,kind) for p in d]
        for p in out:
            w=wc_html(p['content']); tot+=1
            if w<1200: short+=1
        json.dump(out,open(f,'w'))
    print(st,'pages',tot,'still <1200:',short)
if __name__=='__main__':
    for st in sys.argv[1:]: run(st)
