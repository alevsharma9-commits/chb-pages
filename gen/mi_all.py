import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'mi_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'mi_cities.json'))
CP=json.load(open(H+'mi_city_ptax.json')); CT={}
for _k in 'ABCD': CT.update(json.load(open(H+f'mi_cty_{_k}.json')))
BAD=re.compile(r'excerpt|not opened|not confirmed|not stated|unconfirmed|http|phone',re.I)
def ns(c): return re.sub(r'[^a-z0-9]+','-',c.lower().replace('.','').replace("'",'')).strip('-')
def n(x): return f"{x:,}"
def L(u,t): return f"<a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>{esc(t)}</a>"
def facts(topic,kw=None):
    out=[]
    for x in FS[topic]['facts']:
        if not x.get('opened'): continue
        c=clean_txt(x['claim'])
        if kw and not re.search(kw,c,re.I): continue
        if re.search('search excerpt|metadata',c,re.I): continue
        u=x.get('url'); out.append(f"{esc(c.rstrip('.'))}. ({esc(clean_txt(x['cite']))}"+(f"; <a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>source</a>)" if u else ")"))
    return out
SRC=[('Michigan Department of Treasury','https://www.michigan.gov/treasury'),('Michigan Compiled Laws','https://www.legislature.mi.gov/'),('Michigan Courts','https://www.courts.michigan.gov/')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-michigan','we buy houses in Michigan')+"."
HOW=lambda:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('michigan-property-tax-guide','Michigan property tax guide','Appeals and exemptions.'),('michigan-homestead-exemption','Michigan homestead exemption','Principal residence exemption.'),('michigan-transfer-tax','Michigan transfer tax','Who pays at closing.'),('we-buy-houses-in-michigan','We buy houses in Michigan','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from Michigan statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Michigan',cards)+sources(srcs)+DISCLAIM('Michigan','attorney or tax professional')+schema(faqs,[('Home',SITE),('Michigan',SITE+'we-buy-houses-in-michigan/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Michigan',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Michigan?','We buy Michigan houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+(sec('What the official sources say',items) if items else '')+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell a Michigan house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling a Michigan House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    T=lambda k:facts(k) if k in FS else []
    pt=T('property-tax-appeals'); pr=T('probate-and-inherited-property'); tt=T('property-transfer-tax'); tl=T('tax-liens')+T('tax-sales'); te=T('eviction-process')+T('tenant-occupied-sale'); dr=T('deeds-recording'); hs=T('homestead-exemption'); qd=T('quitclaim-deed'); cc=T('closing-costs'); cg=T('capital-gains'); lc=T('land-contracts'); et=T('estate-tax'); tod=T('transfer-on-death-deed'); fsbo=T('fsbo-closing')
    sp('michigan-property-tax-guide','Michigan Property Tax Guide: Board of Review, Tax Tribunal and Selling With Tax Due','Michigan Property Tax Guide: Appeals','Michigan property tax: board of review, Tax Tribunal deadlines, principal residence exemption and delinquent tax. Official sources.','michigan property tax','Michigan property tax is set locally, and owners can appeal to the March board of review and then the Michigan Tax Tribunal.',pt+tl[:3],[('When does the Michigan board of review meet?','The statute cited above says the second Monday in March, with alternative start dates a city or township may authorize.'),('What happens to unpaid property tax when I sell?','The title company pays unpaid tax from the sale proceeds at closing.')],'Michigan property tax',['Summer and winter tax due dates for each local unit.'])
    sp('michigan-homestead-exemption','Michigan Principal Residence Exemption: Who Qualifies and When to File','Michigan Principal Residence Exemption Guide','Michigan principal residence exemption (homestead): eligibility, the affidavit and filing deadlines. Official sources only.','michigan homestead exemption','Michigan exempts a principal residence from the local school operating tax if the owner files the affidavit.',hs,[('How do I claim the principal residence exemption?','File the affidavit with the local assessor by the deadlines cited above.')],'Michigan homestead exemption',['Anything beyond the statute text on the Treasury page.'])
    sp('michigan-transfer-tax','Michigan Real Estate Transfer Tax: State and County Rates and Who Pays','Michigan Real Estate Transfer Tax Explained','Michigan state and county real estate transfer tax rates, exemptions and who pays when you sell a house. Official sources only.','michigan transfer tax','Michigan charges both a state and a county real estate transfer tax on deeds.',tt+cc[:2],[('What is the Michigan state transfer tax rate?','The statute cited above sets it at $3.75 per $500.')],'Michigan transfer tax',['Closing cost splits between buyer and seller.'])
    sp('michigan-eviction-process','Michigan Eviction Process (Summary Proceedings) and Selling a Rented House','Michigan Eviction Process and Tenants','Michigan summary proceedings and what it means when you sell a house with tenants. Official statutes only.','michigan eviction process','Michigan evictions are summary proceedings in district court.',te,[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'Michigan eviction process',['Whether a sale ends a lease.'])
    sp('michigan-quitclaim-deed','Michigan Quitclaim Deed: Statutory Form, Transfer Tax Exemptions and Recording','Michigan Quitclaim Deed: Form and Fees','Michigan quitclaim deed: the statutory form, transfer tax exemptions and recording with the register of deeds. Official sources only.','michigan quitclaim deed','A Michigan quitclaim deed is recorded with the register of deeds, and some transfers are exempt from transfer tax.',qd+dr,[('Where do I record a Michigan deed?','With the register of deeds in the county where the property is located.')],'Michigan quitclaim deed',['Whether a quitclaim deed is the right tool for your transfer.'])
    sp('michigan-capital-gains-tax','Michigan Capital Gains Tax When You Sell a House','Michigan Capital Gains Tax on a House Sale','Michigan income tax treatment when you sell a house: what we could confirm on official pages.','michigan capital gains tax','Michigan taxes income at a flat individual rate, and we only state what official pages confirm.',cg,[('Does Michigan have a separate capital gains tax?','We confirmed only the flat individual income tax rate, from a search excerpt.')],'Michigan capital gains tax',['Treatment of a home sale gain and the federal exclusion.'])
    sp('michigan-land-contract','Michigan Land Contracts: Forfeiture Rules and Selling a Contract Property','Michigan Land Contracts: Forfeiture Rules','Michigan land contract forfeiture and recovering possession under summary proceedings. Official statutes only.','michigan land contract','Michigan land contracts have forfeiture and possession rules set by statute.',lc,[('How is a land contract forfeited in Michigan?','See the statutes cited above and confirm the notice periods with an attorney.')],'Michigan land contract',['Forfeiture notice periods under MCL 600.5728.'])
    sp('michigan-estate-tax','Michigan Estate and Inheritance Tax: What We Could Confirm','Michigan Estate and Inheritance Tax','Michigan inheritance tax status according to the Department of Treasury and what that means for heirs selling a house.','michigan estate tax','Michigan Treasury says the inheritance tax applies only to deaths on or before September 30, 1993.',et,[('Does Michigan have an estate tax?','We could not confirm a state estate tax rule on an official page, so we do not state one.')],'Michigan estate tax',['Whether Michigan has any state estate tax today.'])
    sp('michigan-lady-bird-deed','Michigan Lady Bird Deed: What We Could and Could Not Confirm','Michigan Lady Bird Deed Explained','Michigan lady bird deed (enhanced life estate deed): what official sources confirm and what they do not.','michigan lady bird deed','We could not find an official Michigan statute for a lady bird deed.',tod,[('Is a lady bird deed in the Michigan statutes?','We did not find one on an official page, so we do not describe how it works.')],'Michigan lady bird deed',['Any official source describing a lady bird or transfer on death deed.'])
    sp('michigan-probate-process','Michigan Probate Process and Small Estate Affidavit for Selling Inherited Property','Michigan Probate and Small Estates','Michigan probate: the probate court, the small estate threshold and selling an inherited house. Official sources only.','michigan probate','Michigan probate runs through the county probate court.',pr,[('Who can sell a house in probate?','The personal representative with court authority signs for the estate.')],'Michigan probate',['Inflation adjustments to the small estate limit.'])
    sp('michigan-property-transfer-affidavit','Michigan Property Transfer Affidavit: Who Files, When and Why','Michigan Property Transfer Affidavit Guide','Michigan Property Transfer Affidavit: the 45-day filing rule with the assessor and what it means when you sell.','michigan property transfer affidavit','A buyer of Michigan property files a transfer of ownership notice with the assessor.',fsbo+pt[:2],[('Who files the Property Transfer Affidavit?','The buyer files it with the assessor within 45 days, according to the statute cited above.')],'Michigan property transfer affidavit',['Penalty amounts.'])
    sp('michigan-tax-tribunal','Michigan Tax Tribunal: Deadlines for Appealing Property Tax Assessments','Michigan Tax Tribunal Appeal Deadlines','Michigan Tax Tribunal petition deadlines for property tax appeals and how they connect to the board of review.','michigan tax tribunal','The Michigan Tax Tribunal hears property tax appeals after the board of review.',pt,[('What is the Tax Tribunal deadline?','The statute text above lists May 31 for some property classes. Confirm the deadline for your class.')],'Michigan Tax Tribunal',['Deadlines for residential property.'])
    sp('michigan-closing-costs','Michigan Closing Costs for Sellers: Transfer Tax and Recording Fees','Michigan Closing Costs for Sellers','Michigan seller closing costs: transfer tax, recording and what a cash sale saves. Official sources only.','michigan closing costs','The Michigan seller closing costs we can source are the state and county transfer tax and the recording fee.',cc,[('What does it cost to record a deed in Michigan?','The statute cited above sets the fee at $30 per document.')],'Michigan closing costs',['Title and escrow fee splits.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-mi"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Michigan comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Michigan law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> A seller handling the sale directly still needs a deed, a closing attorney and to account for the real estate transfer tax. See "+a('michigan-closing-costs','Michigan closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> Most Michigan mortgages with a power of sale are foreclosed by advertisement, with a public sale at the county. See "+a('michigan-property-tax-guide','the Michigan property tax guide')+" for tax issues that can come up.</p><p><strong>Inherited house.</strong> The probate court handles the estate. See "+a('michigan-probate-process','probate')+" and "+a('michigan-estate-tax','estate tax')+".</p><p><strong>Unpaid property tax.</strong> See "+a('michigan-property-tax-guide','the Michigan property tax guide')+(f" and {a(ns(c)+'-mi-property-tax-guide',esc(c)+' property tax')}" if c in PTCOK else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, MI: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, MI | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, MI"
    rd=f"Sell your {c}, MI house: list, sell yourself or take a cash offer. Michigan foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, MI house: list it, sell it yourself or take a cash offer. Michigan foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=["Detroit", "Ann Arbor", "Sterling Heights", "Flint", "Warren", "Lansing", "Grand Rapids", "Livonia", "Saginaw", "Kalamazoo", "Dearborn", "Troy", "Farmington Hills", "Southfield", "Novi", "Royal Oak", "Battle Creek", "Midland", "Rochester Hills", "Westland", "St. Clair Shores", "Holland", "Wyoming", "Portage", "East Lansing", "Muskegon", "Allen Park", "Hamtramck"]
PTCOK=[c for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')]
def ptax(c,v):
    slug=f"{ns(c)}-mi-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>In Michigan, assessment appeals start with the local March board of review, then the Michigan Tax Tribunal. Confirm with your county.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, MI Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, MI Property Tax Guide",f"{c}, MI property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-mi",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=json.load(open(H+'mi_cty_list.json'))['ptax']
REC=json.load(open(H+'mi_cty_list.json'))['rec']
BLOCK=()
def clean_urls(v):
    for k in ('assessor','collector','recorder'):
        x=v.get(k)
        if isinstance(x,dict) and any(b in (x.get('url') or '') for b in BLOCK): x['url']=''
        if isinstance(x,dict):
            x['facts']=[f for f in x.get('facts',[]) if not any(b in (f.get('url') or '') for b in BLOCK)]
    return v
def cf(v,k):
    out=[]; ex=[]
    for x in (v.get(k) or {}).get('facts',[]):
        if BAD.search(x['claim']): continue
        if x.get('opened'): out.append(clean_txt(x['claim']))
        elif not re.search(r'ncard\.us|deeds\.com|facebook|twitter|zillow|redfin|justia',x.get('url') or '',re.I) and x.get('url','').startswith('http'): ex.append(clean_txt(x['claim'])+' (from the county site listing; confirm with the office)')
    return (out+ex)[:4]
def county(cn,v,kind):
    v=clean_urls(v); nm=cn+' County'; ap,co,rc=v.get('assessor',{}),v.get('collector',{}),v.get('recorder',{})
    unc=[clean_txt(x) for x in v.get('unconfirmed',[]) if 25<len(x)<200 and not BAD.search(x)][:3]
    ap_dl=[clean_txt(x['claim']) for x in (v.get('appeal_deadline') or []) if isinstance(x,dict) and x.get('opened')][:2]
    if kind=='tax':
        slug=f"{ns(cn)}-county-mi-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} bills and collects the tax and handles delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>In Michigan, assessment appeals start with the local March board of review, then the Michigan Tax Tribunal. See the "+a('michigan-property-tax-guide','Michigan property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Michigan bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, MI Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, MI Property Tax Guide"
        rd=f"{nm}, MI property tax: county offices, assessment appeals, county treasurer and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Michigan property tax involves the county assessment office and the county treasurer."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","Appeals start with the local March board of review, then the Michigan Tax Tribunal."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-mi-register-of-deeds"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, MI Register of Deeds: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, MI Register of Deeds Guide"
        rd=f"{nm}, MI register of deeds: where to record a deed, real estate transfer tax, and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} register of deeds records Michigan deeds and mortgages."; fk=f"{cn.lower()} county register of deeds"; crumb=f"{nm} register of deeds"
        faqs=[(f"Where do I record a deed in {nm}?","With the Register of Deeds. Confirm submission rules on the county page."),("Do I owe real estate transfer tax?","Real estate transfer tax can apply to deeds. The Department of Revenue explains the rule.")]
    body=(f"<p><strong>{lead}</strong> This guide lists what we confirmed on official pages.</p>"+s+cta(f"Selling in {nm}?",f"We buy {nm} houses as-is, with no commission, no repairs and no closing costs to you.")+(UNC(unc) if unc else '')+f"<h2>How to sell a house in {esc(nm)}</h2>"+HOW())
    srcs=([(nm_(co if kind=='tax' else rc),(co if kind=='tax' else rc)['url'])] if (co if kind=='tax' else rc).get('url') else [])+SRC[:2]
    return mk(slug,h1,rt,rd,fk,f"Selling in {nm}? Get a Cash Offer",f"We buy {nm} houses as-is and reply with a written cash offer.",body,faqs,crumb,SP,srcs)
if __name__=='__main__':
    seen=set(); cities=[]
    for d in CITIES:
        k=ns(d['city'])
        if k in seen: continue
        seen.add(k); cities.append(d)
    os.makedirs(R+'/pages/mi',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/mi/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('michigan-state-pages-1',state_pages(),'state')
    dump('michigan-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('michigan-city-ptax-1',[ptax(c,CP[c]) for c in PTCOK],'ptax')
    dump('michigan-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('michigan-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
