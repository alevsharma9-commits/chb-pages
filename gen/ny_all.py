import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..')
H='/home/claude/chb/'
FS=json.load(open(H+'ny_fact_sheet.json'))['topics']
CITIES=json.load(open(H+'ny_cities.json'))
CP=json.load(open(H+'ny_city_ptax.json'))
CT={**json.load(open(H+'ny_cty_A.json')),**json.load(open(H+'ny_cty_B.json'))}
VOL=json.load(open(H+'ny_vol.json')) if os.path.exists(H+'ny_vol.json') else {}
BAD=re.compile(r'excerpt|not opened|not confirmed|not stated|unconfirmed|http|phone',re.I)
def ns(c): return re.sub(r'[^a-z0-9]+','-',c.lower().replace('.','').replace("'",'')).strip('-')
def n(x): return f"{x:,}"
def L(u,t): return f"<a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>{esc(t)}</a>"
def facts(topic,kw=None,neg=None):
    out=[]
    for x in FS[topic]['facts']:
        if not x.get('opened'): continue
        c=clean_txt(x['claim'])
        if kw and not re.search(kw,c,re.I): continue
        if neg and re.search(neg,c,re.I): continue
        if 'search excerpt' in c or 'metadata' in c.lower(): continue
        out.append(f"{esc(c.rstrip('.'))}. ({esc(clean_txt(x['cite']))}; <a href='{x['url']}' target='_blank' rel='noreferrer noopener nofollow'>source</a>)" if x.get('url') else f"{esc(c.rstrip('.'))}. ({esc(clean_txt(x['cite']))})")
    return out
NYS=[('NY Real Property Tax Law, Article 11 (tax liens)','https://www.nysenate.gov/legislation/laws/RPT/A11'),('NY RPAPL Article 13 (foreclosure)','https://www.nysenate.gov/legislation/laws/RPA/A13'),('NYS Dept of Taxation and Finance: Real estate transfer tax','https://www.tax.ny.gov/bus/transfer/rett.htm'),('NYS Dept of Taxation and Finance: Property tax','https://www.tax.ny.gov/pit/property/default.htm')]
def faqh(f): return faq_html(f)
def mk(slug,st,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from New York statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body
      +f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('New York',cards)+sources(srcs)+DISCLAIM('New York','attorney or tax professional')
      +schema(faqs,[('Home',SITE),('New York',SITE+'we-buy-houses-in-new-york/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('New York',h1,h2,hp),full,rt,rd,fk)
HOW=lambda extra:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or court paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",extra])
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-new-york','we buy houses in New York')+"."
CARDS=[('we-buy-houses-in-new-york','We buy houses in New York','How a cash offer works.'),('new-york-property-tax-guide','New York property tax guide','STAR, grievance day and tax liens.'),('new-york-transfer-tax','New York transfer tax','State, NYC and local rates.'),('new-york-star-exemption','New York STAR exemption','Basic and Enhanced STAR.')]
def state_pages():
    P=[]
    tt=facts('property-transfer-tax')
    mans=facts('property-transfer-tax','mansion|1,000,000|1%')
    star=facts('property-tax-star-grievance','STAR')
    grv=facts('property-tax-star-grievance','Grievance|SCAR|certiorari')
    lien=facts('back-taxes-tax-lien')
    rec=facts('recording-deeds','TP-584|RP-5217')
    def sec(t,items): return f"<h2>{t}</h2>"+ul(items) if items else ''
    sell=lambda x:f"<h2>How to sell a New York house when this applies to you</h2>"+HOW(CASH)
    P.append(mk('new-york-transfer-tax','NY','New York Transfer Tax: State, NYC and Local Rates, and Who Pays','New York Transfer Tax: Rates and Who Pays','New York real estate transfer tax: the state rate, NYC taxes, Yonkers, who pays, TP-584 filing and which transfers are exempt. Official sources.','new york transfer tax','Selling a New York House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',
      "<p><strong>New York charges a state real estate transfer tax of $2 for each $500 of consideration, and the seller pays it.</strong> Some places add their own taxes. This guide lists only what we confirmed on official pages.</p>"+sec('What the official sources say',tt)+cta('Selling in New York?','We buy New York houses as-is, with no commission, no repairs and no closing costs to you.')+sec('Filing and recording',rec)+f"<h2>What we could not confirm</h2><ul><li>The actual local transfer tax rates in Mount Vernon and Peekskill. State law only sets the maximum.</li></ul>"+sell(0),
      [('Who pays the New York transfer tax?','The seller pays the base state tax. The buyer pays the mansion tax and the NYC supplemental tax, as described on the Department of Taxation and Finance page.'),('How do I file the transfer tax return?','Outside New York City, file Form TP-584 with the county clerk where the property sits. It is due no later than the 15th day after the deed is delivered.'),('Is an inherited house taxed on transfer?','State law excludes conveyances by devise, bequest or inheritance. NYC treats an executor deed given in connection with a sale as taxable.')],'New York transfer tax',CARDS+[('new-york-mansion-tax','New York mansion tax','The 1% tax at $1 million.')],NYS+[('Tax Law Article 31','https://www.nysenate.gov/legislation/laws/TAX/A31')]))
    P.append(mk('new-york-mansion-tax','NY','New York Mansion Tax: 1% at $1 Million and Who Pays','New York Mansion Tax: 1% at $1 Million','New York mansion tax: the 1% tax on residential sales of $1 million or more, who pays it, the NYC supplemental tax and filing. Official sources.','new york mansion tax','Selling a New York House? Get a Cash Offer','We buy as-is. Tell us about the property.',
      "<p><strong>The New York mansion tax is 1 percent of the price on residential sales of $1,000,000 or more, and the buyer pays it.</strong> Here is what the official sources say.</p>"+sec('What the official sources say',mans or tt[:4])+cta('Selling in New York?','We buy New York houses as-is, with no commission, no repairs and no closing costs to you.')+sell(0),
      [('Who pays the mansion tax?','The buyer pays it. If the buyer fails to pay or is exempt, the seller can become liable, according to the Department of Taxation and Finance.'),('What price triggers the mansion tax?','One percent applies when the consideration for the whole conveyance of residential property is $1,000,000 or more.')],'New York mansion tax',CARDS[:3]+[CARDS[3]],NYS))
    P.append(mk('new-york-star-exemption','NY','New York STAR Exemption: Basic and Enhanced STAR, Income Limits and Registering','New York STAR Exemption: Basic and Enhanced','New York STAR: Basic and Enhanced eligibility, income limits, how to register and what happens when you sell. Official sources only.','new york star exemption','Behind on New York Property Tax? Get a Cash Offer','We buy as-is, and the title company pays unpaid tax from the proceeds.',
      "<p><strong>New York's STAR program lowers school property taxes for owner-occupied primary residences, and homeowners register with the state.</strong> Here is what the Department of Taxation and Finance says.</p>"+sec('What the official sources say',star)+cta('Behind on property tax?','We buy New York houses as-is, and the title company pays unpaid tax from the proceeds.')+f"<h2>What we could not confirm</h2><ul><li>What happens to your STAR benefit when you sell. Ask the Department of Taxation and Finance or the assessor.</li></ul>"+sell(0),
      [('Do I need to register for STAR?','Yes. The state tells homeowners to register once through the Homeowner Benefit Portal, and new homeowners should register as soon as the home becomes their primary residence.'),('What is the Basic STAR income limit?','The Department of Taxation and Finance lists $500,000 for the Basic STAR credit and $250,000 for the exemption.')],'New York STAR exemption',CARDS[:2]+[CARDS[2]],NYS))
    P.append(mk('new-york-property-tax-guide','NY','New York Property Tax Guide: Grievance Day, STAR, Tax Liens and Selling With Tax Due','New York Property Tax Guide: Grievance and Liens','New York property tax: grievance day and appeals, STAR, delinquent tax liens and the two-year redemption period, and selling a house with tax due.','new york property tax','Behind on New York Property Tax? Get a Cash Offer','We buy as-is, and the title company pays unpaid tax from the proceeds.',
      "<p><strong>New York property tax is set and collected locally, so due dates and assessors differ by town, city and county.</strong> This guide covers the statewide rules we confirmed and points to local guides.</p>"+sec('Grievance and appeals',grv)+sec('STAR',star[:2])+cta('Behind on property tax?','We buy New York houses as-is, and the title company pays unpaid tax from the proceeds.')+sec('Tax liens and unpaid tax',lien)+"<h2>Local property tax guides</h2>"+ul([a('new-york-city-ny-property-tax-guide','New York City property tax guide')]+[a(f"{ns(c)}-ny-property-tax-guide",f"{c}, NY property tax guide") for c in CPT if c!='New York'][:19])+sell(0),
      [('When is Grievance Day in New York?','In most communities it is the fourth Tuesday in May. Suffolk and Westchester use different days, and NYC uses its own Tax Commission dates.'),('What is the redemption period on a New York tax lien?','RPTL 1110 sets a two-year redemption period for a delinquent tax lien, starting from the lien date.')],'New York property tax',CARDS[2:]+[CARDS[0]],NYS))
    return P
CPT=['Albany','Amherst','Brookhaven','Buffalo','East Hampton','Greenburgh','Hempstead','Huntington','Islip','New Rochelle','New York','North Hempstead','Rochester','Schenectady','Smithtown','Southampton','Syracuse','Tonawanda','White Plains','Yonkers']
CPT=[c for c in CPT if c in CP and all(CP[c].get(k,{}).get('name') and CP[c].get(k,{}).get('url') for k in('assessor','collector'))]
print('ptax cities',CPT)
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-ny"
    nyc=c=='New York'; cty=d['county']+' County'
    kind={'city':'city','town':'town','village':'village'}.get(d['type'],'place')
    lead=f"<strong>Selling a house in {esc(c)}, New York comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under New York law. The Census Bureau estimates {n(d['pop'])} residents in the {kind} of {esc(c)} as of July 1, 2025. We did not use listing-site price data."
    body=(f"<p>{lead}</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau).",f"{esc(c)} is in {esc(cty)}."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> You still file transfer tax and recording paperwork. See "+a('new-york-transfer-tax','the New York transfer tax guide')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> New York lenders must send a 90-day notice before starting a foreclosure on a home loan (RPAPL 1304), and the court holds a mandatory settlement conference within 60 days after proof of service is filed (CPLR 3408).</p>"
     f"<p><strong>Inherited house.</strong> Real property passes to the decedent's distributees at death, and the Surrogate's Court issues letters of administration when there is no will. Transfer tax excludes conveyances by devise or inheritance.</p>"
     f"<p><strong>Unpaid property tax.</strong> A delinquent tax lien can be redeemed for two years under RPTL 1110. See {a('new-york-property-tax-guide','the New York property tax guide')}"+(f" and {a('new-york-city-ny-property-tax-guide','the New York City guide')}" if nyc else (f" and {a(ns(c)+'-ny-property-tax-guide',esc(c)+' property tax')}" if c in CPT else ''))+".</p>"
     f"<h2>Taxes on the sale itself</h2><p>New York's transfer tax is $2 per $500 of consideration and the seller pays it. See {a('new-york-transfer-tax','the transfer tax guide')}. The IRS lets you exclude up to $250,000 of gain on your main home, or $500,000 if married filing jointly, if you meet its tests. We did not confirm New York income tax treatment on an official page.</p>"
     f"<h2>How to sell a house in {esc(c)}</h2>"+HOW(CASH))
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing."),("Who pays New York's transfer tax?","The seller pays the base state tax of $2 per $500 of consideration.")]
    cards=[CARDS[0],CARDS[1],CARDS[2],('new-york-star-exemption','New York STAR exemption','Basic and Enhanced STAR.')]
    srcs=NYS+[('Census Bureau population estimates',d['pop_source_url']),('IRS Publication 523','https://www.irs.gov/publications/p523')]
    h1=f"Sell My House Fast in {c}, NY: Options, Costs and Cash Offers"
    rt=f"Sell My House Fast in {c}, NY | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, NY"
    rd=f"Sell your {c}, NY house: list, sell yourself or take a cash offer. New York foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, NY house: list, sell it yourself or take a cash offer. New York foreclosure and tax rules. No commission."
    it=mk(slug,'NY',h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",cards,srcs)
    return it
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:|Opened table:)\s*','',clean_txt(t))
def good(v):
    return v and v.get('opened') and not BAD.search(v.get('text','') or '')
def ptax(c,v):
    nyc=c=='New York'; slug='new-york-city-ny-property-tax-guide' if nyc else f"{ns(c)}-ny-property-tax-guide"
    nm=c; ap,co=v['assessor'],v['collector']
    o=[]
    def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
    bill=[f"{L(ap['url'],nm_(ap))} handles assessment."+("" if ap.get('opened') else ""),f"{L(co['url'],nm_(co))} bills and collects the tax."]
    sec=f"<h2>Who bills what in {esc(nm)}</h2>"+ul(bill)
    dd=v.get('due_dates') or {}
    if dd.get('opened') and not BAD.search(dd.get('text','')): sec+=f"<h2>Due dates</h2><p>{esc(pre(dd['text']))[:600]} See the {L(dd['url'],'official page')}.</p>"
    else: sec+=f"<h2>Due dates</h2><p>We could not confirm {esc(nm)} due dates on an opened official page. Ask the collector for the current bill schedule.</p>"
    g=v.get('grievance') or {}
    if g.get('opened') and not BAD.search(g.get('text','')): sec+=f"<h2>Challenging your assessment</h2><p>{esc(pre(g['text']))[:600]} See the {L(g.get('filing_page_url') or g['url'],'official page')}. The statewide rules are in the {a('new-york-property-tax-guide','New York property tax guide')}.</p>"
    else: sec+=f"<h2>Challenging your assessment</h2><p>Grievance Day in most New York communities is the fourth Tuesday in May. We could not confirm the {esc(nm)} date on an opened page, so check with the assessor. See the {a('new-york-property-tax-guide','New York property tax guide')}.</p>"
    r=v.get('rate'); eq=v.get('equalization_rate')
    if r and r.get('opened'): sec+=f"<h2>Tax rate</h2><p>The official page we opened lists a rate of {r['value']} for {r['year']}. See the {L(r['url'],'official page')}. Your bill can include county, school and other levies, so this is not necessarily your total rate.</p>"
    else: sec+=f"<h2>Tax rate</h2><p>We could not confirm the current {esc(nm)} tax rate on an opened official page, so we do not state one.</p>"
    if eq and eq.get('opened') and eq.get('value'): sec+=f"<h2>Assessment ratio</h2><p>The state's 2025 equalization rate for {esc(nm)} is listed as {eq['value']} percent of full value. It was parsed from a state report, so confirm it in the {L('https://www.tax.ny.gov/research/property/assess/default.htm','state assessment data')}.</p>"
    sec+=f"<h2>STAR</h2><p>Homeowners with a primary residence can register for STAR through the state. See the {a('new-york-star-exemption','New York STAR guide')}.</p>"
    unc=[clean_txt(x) for x in v.get('unconfirmed',[]) if 25<len(x)<200 and not BAD.search(x)][:3]
    faqs=[(f"When is Grievance Day in {nm}?","Grievance Day in most New York communities is the fourth Tuesday in May. Check with the local assessor for the exact date and any local exception."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing."),("How long can I redeem a delinquent tax lien?","RPTL 1110 sets a two-year redemption period.")]
    body=(f"<p><strong>{esc(nm)} property tax is billed by the local collector named below, and the schedule varies by municipality.</strong> This guide points to the official offices and explains what happens to unpaid tax when you sell.</p>"+sec+cta(f"Behind on {nm} property tax?",f"We buy {nm} houses as-is, and the title company pays unpaid tax from the proceeds.")
      +("<h2>What we could not confirm</h2>"+ul([esc(x) for x in unc]) if unc else '')+f"<h2>How to sell a house in {esc(nm)} when you owe property tax</h2>"+HOW(CASH))
    cards=[('we-buy-houses-in-new-york','We buy houses in New York','How a cash offer works.'),(f"sell-my-house-fast-{ns(c)}-ny",f"Sell my house in {c}",'Options, costs and cash offers.'),CARDS[1],CARDS[3]]
    srcs=[(nm_(ap),ap['url']),(nm_(co),co['url'])]+NYS[:1]+NYS[3:]
    h1=f"{c}, NY Property Tax Guide: Offices, Dates and Selling With Tax Due"
    rt=f"{c}, NY Property Tax Guide"
    rd=f"{c}, NY property tax: assessor and collector offices, grievance day, STAR, tax liens and what happens to unpaid tax when you sell."
    if len(rd)>155: rd=f"{c}, NY property tax: offices, grievance day, STAR and unpaid tax when you sell."
    return mk(slug,'NY',h1,rt,rd,f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",cards,srcs)
CNT=['Nassau','Suffolk','Westchester','Rockland','Orange','Erie','Monroe','Onondaga','Saratoga','Oswego','Jefferson','Wayne','Madison','Fulton','Montgomery','Queens']
def county(cn,v):
    slug=f"{ns(cn)}-county-ny-property-tax-guide"; nm=cn+' County'
    ap,co=v.get('assessor',{}),v.get('collector',{})
    bill=[]
    if co.get('url'): bill.append(f"{L(co['url'],clean_txt(co['name']).split('(')[0].strip())} handles delinquent tax and collection for the county.")
    if ap.get('url') and 'not confirmed' not in ap.get('name',''): bill.append(f"{L(ap['url'],clean_txt(ap['name']).split('(')[0].strip())} handles assessment.")
    op=[clean_txt(x['claim']) for k in ('assessor','collector') for x in v.get(k,{}).get('facts',[]) if x.get('opened') and not BAD.search(x['claim'])][:4]
    gv={'Suffolk':'Suffolk County Grievance Day is the third Tuesday in May.','Westchester':'Westchester Grievance Day is the third Tuesday in June.','Nassau':'Nassau County has its own assessment review process, so use the county assessment department.'}.get(cn,'Grievance Day in most New York communities is the fourth Tuesday in May. Assessments are set by the town or city assessor, so confirm the date locally.')
    sec=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else f"<p>We could not confirm the {esc(nm)} offices on an opened page.</p>")
    if op: sec+=f"<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op])
    sec+=f"<h2>Assessment and grievance</h2><p>{esc(gv)} See the {a('new-york-property-tax-guide','New York property tax guide')} for the statewide process, including small claims assessment review.</p><h2>Tax liens</h2><p>A delinquent tax lien can be redeemed for two years under RPTL 1110, per the state statute. The county may run its own lien or foreclosure schedule. Ask the treasurer for current dates.</p>"
    sec+=f"<h2>Tax rate</h2><p>We could not confirm a current county tax rate on an opened official page, so we do not state one. New York rates vary by town, school district and village.</p>"
    unc=[clean_txt(x) for x in v.get('unconfirmed',[]) if 25<len(x)<200 and not BAD.search(x)][:3]
    faqs=[(f"Who collects property tax in {nm}?","In New York, town, city or village collectors bill most property tax, and the county treasurer handles delinquent tax. Confirm which applies to your parcel on your bill."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing."),("How long can I redeem a delinquent tax lien?","RPTL 1110 sets a two-year redemption period.")]
    body=(f"<p><strong>{esc(nm)}, New York property tax is billed locally and delinquent tax goes to the county.</strong> This guide lists the offices we confirmed and the statewide rules.</p>"+sec+cta(f"Behind on {nm} property tax?",f"We buy {nm} houses as-is, and the title company pays unpaid tax from the proceeds.")+("<h2>What we could not confirm</h2>"+ul([esc(x) for x in unc]) if unc else '')+f"<h2>How to sell a house in {esc(nm)} when you owe property tax</h2>"+HOW(CASH))
    srcs=([(clean_txt(co['name']).split('(')[0].strip(),co['url'])] if co.get('url') else [])+NYS[:1]+NYS[3:]
    h1=f"{nm}, NY Property Tax Guide: Offices, Liens and Selling With Tax Due"
    rt=f"{nm}, NY Property Tax Guide"
    rd=f"{nm}, NY property tax: county offices, grievance day, STAR, tax liens and what happens to unpaid tax when you sell."
    return mk(slug,'NY',h1,rt,rd,f"{cn.lower()} county property tax",f"Owe {nm} Property Tax? Get a Cash Offer",f"We buy {nm} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{nm} property tax guide",CARDS,srcs)
if __name__=='__main__':
    seen=set(); cities=[]
    for d in CITIES:
        k=ns(d['city'])
        if k in seen: continue
        seen.add(k); cities.append(d)
    out=state_pages(); json.dump(out,open(R+'/pages/ny/new-york-state-pages-1.json','w')); print('state',[(i['slug'],wc(i)) for i in out])
    out=[city_page(d['city'],d) for d in cities]; json.dump(out,open(R+'/pages/ny/new-york-city-pages-1.json','w')); print('city',len(out),min(map(wc,out)))
    out=[ptax(c,CP[c]) for c in CPT if c in CP]; json.dump(out,open(R+'/pages/ny/new-york-city-ptax-1.json','w')); print('ptax',len(out),min(map(wc,out)))
    out=[county(c,CT[c]) for c in CNT if c in CT]; json.dump(out,open(R+'/pages/ny/new-york-county-ptax-1.json','w')); print('county',len(out),min(map(wc,out)))
