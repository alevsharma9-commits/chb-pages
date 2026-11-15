import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'il_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'il_cities.json'))
CP=json.load(open(H+'il_city_ptax.json')); CT={**json.load(open(H+'il_cty_A.json')),**json.load(open(H+'il_cty_B.json'))}
BAD=re.compile(r'ilmarion|illinoistreasurers|excerpt|not opened|not confirmed|not stated|unconfirmed|http|phone',re.I)
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
SRC=[('Illinois Department of Revenue: Real estate transfer tax','https://tax.illinois.gov/localgovernments/property.html'),('Illinois Compiled Statutes','https://www.ilga.gov/Legislation/ILCS/ILCS'),('Illinois Department of Revenue: Property tax','https://tax.illinois.gov/localgovernments/property.html')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-illinois','we buy houses in Illinois')+"."
HOW=lambda:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('illinois-property-tax-guide','Illinois property tax guide','Appeals and exemptions.'),('illinois-homestead-exemption','Illinois homestead exemption','Eligibility and filing.'),('illinois-quitclaim-deed','Illinois quitclaim deed','Recording and transfer tax.'),('we-buy-houses-in-illinois','We buy houses in Illinois','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from Illinois statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Illinois',cards)+sources(srcs)+DISCLAIM('Illinois','attorney or tax professional')+schema(faqs,[('Home',SITE),('Illinois',SITE+'we-buy-houses-in-illinois/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Illinois',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Illinois?','We buy Illinois houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+sec('What the official sources say',items)+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell an Illinois house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling an Illinois House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    pt=facts('property-tax-appeals'); pr=facts('probate-and-inherited-property'); tt=facts('property-transfer-tax'); ts=facts('tax-sales'); te=facts('tenant-occupied-sale'); dr=facts('deeds-recording')
    sp('illinois-property-tax-guide','Illinois Property Tax Guide: Board of Review Appeals, Exemptions and Selling With Tax Due','Illinois Property Tax Guide: Appeals, Exemptions','Illinois property tax: board of review appeal deadlines, homestead and senior exemptions, tax sales and selling a house with tax due.','illinois property tax','Illinois property tax is set by county and township assessors, and appeals go first to the county board of review.',pt+ts[:3],[('When are Illinois board of review complaints due?','Complaints are generally due within 30 days after publication of the assessment list (35 ILCS 200/16-55). Confirm the date with your county.'),('What happens to unpaid property tax when I sell?','The title company pays unpaid tax from the sale proceeds at closing.')],'Illinois property tax',['PTAB filing deadline and exemption amounts not shown above.'])
    sp('illinois-homestead-exemption','Illinois Homestead Exemption: General, Senior and Senior Freeze','Illinois Homestead Exemption: General and Senior','Illinois homestead exemptions: general, senior and senior freeze eligibility, the income limit and how to file with the county. Official sources.','illinois homestead exemption','Illinois offers homestead exemptions that reduce the assessed value of an owner-occupied home, including senior exemptions.',pt,[('Where do I apply for a homestead exemption?','With the county chief county assessment officer. Dates and forms are set locally.')],'Illinois homestead exemption',['Exemption dollar amounts by county.'])
    sp('illinois-senior-exemption','Illinois Senior Exemption and Senior Freeze: Eligibility and Income Limit','Illinois Senior Exemption and Senior Freeze','Illinois senior homestead exemption and senior freeze: age and income rules, the income limit and how to apply. Department of Revenue sources.','illinois senior exemption','Illinois has a senior homestead exemption and a senior citizens assessment freeze, each with its own rules.',facts('property-tax-appeals','senior|freeze') or pt,[('What is the senior freeze income limit?','The Department of Revenue lists $75,000 for tax year 2026 in its PIO-74 publication, as we reviewed it.')],'Illinois senior exemption',['County filing deadlines.'])
    sp('illinois-estate-tax','Illinois Estate Tax and Inheritance Tax: What Heirs Owe When Selling','Illinois Estate Tax and Inheritance Tax','Illinois estate tax and inheritance tax: what Illinois imposes, what heirs owe and how it affects selling an inherited house. Official sources only.','illinois estate tax','Illinois has an estate tax, and heirs who sell an inherited house should know what is and is not taxed.',pr,[('Does Illinois have an inheritance tax?','We did not confirm an Illinois inheritance tax on an official page. Illinois does impose an estate tax; check with the Attorney General estate tax page.')],'Illinois estate tax',['Estate tax thresholds and rates were not opened.'])
    sp('illinois-inheritance-tax','Illinois Inheritance Tax: What Applies When You Inherit a House','Illinois Inheritance Tax: What Applies','Illinois inheritance tax: what we could confirm, how the Illinois estate tax differs and how to sell an inherited house. Official sources only.','illinois inheritance tax','This guide covers what we could confirm about Illinois tax on inherited property.',pr,[('Can I sell an inherited house in Illinois?','Yes, if you have authority to sign. Authority comes from the estate representative or from title that passed to you. Ask the title company.')],'Illinois inheritance tax',['Whether Illinois imposes an inheritance tax was not confirmed on an official page.'])
    sp('illinois-small-estate-affidavit','Illinois Small Estate Affidavit: Limit and Selling an Inherited Home','Illinois Small Estate Affidavit: $150,000 Limit','Illinois small estate affidavit: the $150,000 personal property limit, what it covers and what it means for selling an inherited home.','illinois small estate affidavit','Illinois lets heirs collect small estates by affidavit when personal property is within the statutory limit.',pr,[('What is the small estate limit?','The limit is $150,000 in personal property under 755 ILCS 5/25-1 as amended, according to the statute text the research opened.')],'Illinois small estate affidavit',['Whether the affidavit can convey real estate was not confirmed.'])
    sp('illinois-probate-process','Illinois Probate Process: Independent Administration and Selling Inherited Property','Illinois Probate Process Explained','Illinois probate: letters, small estates and selling an inherited house. Official statutes only.','illinois probate','Illinois probate runs through the circuit court in the county where the decedent lived.',pr,[('Who can sell a house in probate?','The executor or administrator with court authority signs for the estate.')],'Illinois probate',['Independent administration steps were not opened.'])
    sp('illinois-quitclaim-deed','Illinois Quitclaim Deed: Recording, Transfer Tax and When It Works','Illinois Quitclaim Deed: Recording and Tax','Illinois quitclaim deed: recording with the county recorder, transfer declaration and transfer tax. Official sources only.','illinois quitclaim deed','An Illinois deed is recorded with the county recorder of deeds, and transfer tax can apply.',dr+tt[:4],[('Does a quitclaim deed avoid transfer tax?','Not automatically. The statutes list specific exemptions.')],'Illinois quitclaim deed',['Recording fees and the exact deed form rules were not fully confirmed.'])
    sp('illinois-transfer-tax','Illinois Transfer Tax: State, County and Chicago Rates','Illinois Transfer Tax: State and Chicago Rates','Illinois real estate transfer tax: the state rate, optional county tax, Chicago rates, who pays and exemptions. Official sources only.','illinois transfer tax','Illinois charges a state transfer tax of 50 cents per $500, and some counties and cities add their own.',tt,[('Who pays the Chicago transfer tax?','Chicago says the buyer pays $3.75 per $500 and the seller pays $1.50 per $500 for the CTA portion.')],'Illinois transfer tax',['Who pays the state tax and the Cook County and other municipal rates were not confirmed.'])
    sp('illinois-tax-sales','Illinois Tax Sales: Redemption Periods and Tax Deeds','Illinois Tax Sales: Redemption and Tax Deeds','Illinois tax sales: the redemption period, the 3 year rule for newer certificates and what to do if your property is at risk. Official statutes.','illinois tax sale','Illinois counties sell delinquent property tax at annual tax sales, and owners can redeem during a statutory period.',ts,[('How long is the redemption period?','For certificates issued on or after January 1, 2024, residential property has 3 years under 35 ILCS 200/21-350, with shorter periods for some property types.')],'Illinois tax sales',['Tax deed procedure under 35 ILCS 200/22-30 was not opened.'])
    sp('illinois-foreclosure-process','Illinois Foreclosure Process: Redemption, Mediation and Your Options','Illinois Foreclosure Process and Redemption','Illinois foreclosure: judicial process, the redemption period, Cook County mediation and selling before the sale. Official statutes.','illinois foreclosure process','Illinois foreclosures go through court, and owners have a statutory redemption period.',facts('foreclosure'),[('Can I sell my house during foreclosure?','Yes. A cash sale can pay the lender from the proceeds if it closes in time. Ask for a payoff figure.')],'Illinois foreclosure',['Illinois deficiency rules were not confirmed.'])
    sp('illinois-eviction-process','Illinois Eviction Process and Selling a Rented House','Illinois Eviction Process and Tenants','Illinois eviction under the Eviction Act and what it means when you sell a house with tenants. Official statutes only.','illinois eviction process','Illinois evictions go through the Eviction Act and the courts.',te,[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'Illinois eviction process',['Chicago RLTO sale provisions were not opened.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-pa"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Illinois comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Illinois law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> Illinois sellers owe the buyer a property disclosure and realty transfer tax applies. See "+a('illinois-closing-costs','Illinois closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> Illinois mortgage foreclosures go through court and end in a foreclosure sale. See "+a('illinois-sheriff-sale','the Illinois foreclosure sale guide')+".</p><p><strong>Inherited house.</strong> The probate court issues letters, and the inheritance tax applies. See "+a('illinois-probate-process','probate')+" and "+a('illinois-inheritance-tax','inheritance tax')+".</p><p><strong>Unpaid property tax.</strong> See "+a('illinois-property-tax-guide','the Illinois property tax guide')+" and "+a('illinois-tax-sales','tax sales')+(f" and {a(ns(c)+'-il-property-tax-guide',esc(c)+' property tax')}" if c in PTC else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, IL: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, IL | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, IL"
    rd=f"Sell your {c}, IL house: list, sell yourself or take a cash offer. Illinois foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, IL house: list it, sell it yourself or take a cash offer. Illinois foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=['Chicago','Peoria','Rockford','Champaign','Naperville','Bloomington','DeKalb','McHenry','Evanston']
def ptax(c,v):
    slug=f"{ns(c)}-il-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>Board of review complaints are generally due within 30 days after the assessment list is published (35 ILCS 200/16-55). Confirm with your county board.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, IL Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, IL Property Tax Guide",f"{c}, IL property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-pa",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=['Adams','Boone','Bureau','Champaign','Coles','Cook','DuPage','Effingham','Franklin','Fulton','Grundy','Henry','Iroquois','Jackson','Jefferson','Jersey','Jo Daviess','Johnson','Kane','Kankakee','Kendall','Knox','Lake','Lee','Logan','Macon','Macoupin','Madison','Marion','Montgomery','Morgan','Ogle','Peoria','Rock Island','Saline','Sangamon','Scott','St. Clair','Stephenson','Tazewell','Vermilion','Washington','Whiteside','Will','Williamson','Winnebago','Woodford']
REC=['Cook','DuPage','Lake','Will','Kane','Kendall','Champaign','Lee','Madison','Peoria','Sangamon','St. Clair','Wayne','Winnebago']
BLOCK=('ilmarion.com','illinoistreasurers.org','illinoisfixandfliploan.com')
def clean_urls(v):
    for k in ('assessor','collector','recorder'):
        x=v.get(k)
        if isinstance(x,dict) and any(b in (x.get('url') or '') for b in BLOCK): x['url']=''
        if isinstance(x,dict):
            x['facts']=[f for f in x.get('facts',[]) if not any(b in (f.get('url') or '') for b in BLOCK)]
    return v
def cf(v,k): return [clean_txt(x['claim']) for x in (v.get(k) or {}).get('facts',[]) if x.get('opened') and not BAD.search(x['claim'])][:4]
def county(cn,v,kind):
    v=clean_urls(v); nm=cn+' County'; ap,co,rc=v.get('assessor',{}),v.get('collector',{}),v.get('recorder',{})
    unc=[clean_txt(x) for x in v.get('unconfirmed',[]) if 25<len(x)<200 and not BAD.search(x)][:3]
    ap_dl=[clean_txt(x['claim']) for x in (v.get('appeal_deadline') or []) if isinstance(x,dict) and x.get('opened')][:2]
    if kind=='tax':
        slug=f"{ns(cn)}-county-il-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} handles collection and delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>Board of review complaints are generally due within 30 days after the assessment list is published (35 ILCS 200/16-55). See the "+a('illinois-property-tax-guide','Illinois property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Illinois bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, IL Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, IL Property Tax Guide"
        rd=f"{nm}, IL property tax: county offices, assessment appeals, county treasurer and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Illinois property tax involves the county assessment office and the county treasurer."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","The county board of review handles them, and complaints are generally due within 30 days after publication of the assessment list."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-il-recorder-of-deeds"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax','statement of value|1%|joint')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, IL Recorder of Deeds: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, IL Recorder of Deeds Guide"
        rd=f"{nm}, IL recorder of deeds: where to record a deed, realty transfer tax, statement of value and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} recorder of deeds records Illinois deeds and mortgages."; fk=f"{cn.lower()} county recorder of deeds"; crumb=f"{nm} recorder of deeds"
        faqs=[(f"Where do I record a deed in {nm}?","At the county recorder of deeds. Confirm submission rules on the county page."),("Do I owe realty transfer tax?","Realty transfer tax can apply to deeds. The Department of Revenue lists the exemptions.")]
    body=(f"<p><strong>{lead}</strong> This guide lists what we confirmed on official pages.</p>"+s+cta(f"Selling in {nm}?",f"We buy {nm} houses as-is, with no commission, no repairs and no closing costs to you.")+(UNC(unc) if unc else '')+f"<h2>How to sell a house in {esc(nm)}</h2>"+HOW())
    srcs=([(nm_(co if kind=='tax' else rc),(co if kind=='tax' else rc)['url'])] if (co if kind=='tax' else rc).get('url') else [])+SRC[:2]
    return mk(slug,h1,rt,rd,fk,f"Selling in {nm}? Get a Cash Offer",f"We buy {nm} houses as-is and reply with a written cash offer.",body,faqs,crumb,SP,srcs)
if __name__=='__main__':
    seen=set(); cities=[]
    for d in CITIES:
        k=ns(d['city'])
        if k in seen: continue
        seen.add(k); cities.append(d)
    os.makedirs(R+'/pages/il',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/il/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('illinois-state-pages-1',state_pages(),'state')
    dump('illinois-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('illinois-city-ptax-1',[ptax(c,CP[c]) for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')],'ptax')
    dump('illinois-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('illinois-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
