import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'pa_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'pa_cities.json'))
CP=json.load(open(H+'pa_city_ptax.json')); CT={**json.load(open(H+'pa_cty_A.json')),**json.load(open(H+'pa_cty_B.json'))}
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
SRC=[('Pennsylvania Department of Revenue: Realty transfer tax','https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/realty-transfer-tax'),('Pennsylvania Consolidated Statutes','https://www.palegis.us/statutes/consolidated'),('Pennsylvania Department of Revenue: Inheritance tax','https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/inheritance-tax')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-pennsylvania','we buy houses in Pennsylvania')+"."
HOW=lambda:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or the Register of Wills paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('pennsylvania-property-tax-guide','Pennsylvania property tax guide','Appeals, homestead and rebate.'),('pennsylvania-inheritance-tax','Pennsylvania inheritance tax','Rates and the 3 month discount.'),('pennsylvania-homestead-exclusion','Pennsylvania homestead exclusion','Filing and eligibility.'),('we-buy-houses-in-pennsylvania','We buy houses in Pennsylvania','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from Pennsylvania statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Pennsylvania',cards)+sources(srcs)+DISCLAIM('Pennsylvania','attorney or tax professional')+schema(faqs,[('Home',SITE),('Pennsylvania',SITE+'we-buy-houses-in-pennsylvania/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Pennsylvania',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Pennsylvania?','We buy Pennsylvania houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None,extra=''):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+sec('What the official sources say',items)+extra+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell a Pennsylvania house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling a Pennsylvania House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    pt=facts('property-tax-appeals'); hx=facts('property-tax-appeals','homestead|farmstead'); rb=facts('property-tax-appeals','rebate|rent')
    pr=facts('probate-and-inherited-property'); inh=facts('probate-and-inherited-property','inherit|tax|rate|discount')
    sp('pennsylvania-property-tax-guide','Pennsylvania Property Tax Guide: Appeals, Homestead Exclusion and Selling With Tax Due','Pennsylvania Property Tax Guide: Appeals, Homestead','Pennsylvania property tax: assessment appeal deadlines, the homestead exclusion, the Property Tax/Rent Rebate program and selling with tax due.','pennsylvania property tax','Pennsylvania property tax is set by counties, school districts and municipalities, and assessment appeals follow a statutory calendar.',pt+facts('tax-sales')[:3],[('When is the assessment appeal deadline in Pennsylvania?','The statutory default is September 1, and a county may set a date no earlier than August 1 under 53 Pa.C.S. 8844. Check your county board.'),('What happens to unpaid property tax when I sell?','The title company pays unpaid tax from the sale proceeds at closing.')],'Pennsylvania property tax',['Tax sale redemption steps beyond what is cited above.'])
    sp('pennsylvania-inheritance-tax','Pennsylvania Inheritance Tax: Rates, the Discount and Selling an Inherited House','Pennsylvania Inheritance Tax: Rates and Discount','Pennsylvania inheritance tax: who pays, the rate by relationship, the 3 month 5 percent discount, due dates and selling an inherited house.','pennsylvania inheritance tax','Pennsylvania imposes an inheritance tax on property passing at death, and heirs who sell an inherited house still have to deal with it.',inh or pr,[('Is there a discount for paying inheritance tax early?','The Department of Revenue says a 5 percent discount applies if the tax is paid within three months of death.'),('Can I sell an inherited house before the estate closes?','It depends on who has authority. The personal representative signs after the Register of Wills issues letters. Ask the title company what it needs.')],'Pennsylvania inheritance tax',['The 72 P.S. 9116 statute text was not opened; rates come from Department of Revenue pages.'])
    sp('pennsylvania-homestead-exclusion','Pennsylvania Homestead Exclusion: Filing, Eligibility and Selling the Home','Pennsylvania Homestead Exclusion: Filing','Pennsylvania homestead and farmstead exclusion: who qualifies, how to file with the county and what happens when you sell. Official sources.','pennsylvania homestead exclusion','Pennsylvania homeowners apply for the homestead exclusion with their county, and the benefit reduces the assessed value used for school taxes.',hx or pt[:3],[('How do I apply for the homestead exclusion?','File with your county assessment office. Filing dates and forms are set by the county.')],'Pennsylvania homestead exclusion',['Current exclusion amounts by school district.'])
    sp('pennsylvania-property-tax-rent-rebate','Pennsylvania Property Tax/Rent Rebate Program: Eligibility and Deadlines','Pennsylvania Property Tax Rebate Program','Pennsylvania Property Tax/Rent Rebate: who qualifies, income limits, how to apply and the deadline. Official Department of Revenue sources.','pennsylvania property tax rebate','Pennsylvania runs a Property Tax/Rent Rebate program for older adults, widows and widowers, and people with disabilities.',rb or pt[:3],[('Who runs the rebate program?','The Pennsylvania Department of Revenue administers it, based on the sources we reviewed.')],'Pennsylvania property tax rebate',['Current income limits and the filing deadline unless shown above.'])
    sp('pennsylvania-quitclaim-deed','Pennsylvania Quitclaim Deed: Recording, Transfer Tax and When It Works','Pennsylvania Quitclaim Deed: Recording and Tax','Pennsylvania quitclaim deed: recording at the county recorder of deeds, realty transfer tax and the statement of value. Official sources only.','pennsylvania quitclaim deed','A Pennsylvania deed is recorded with the county recorder of deeds, and realty transfer tax and a statement of value can apply.',facts('deeds-recording')+facts('property-transfer-tax')[:4],[('Does a quitclaim deed avoid transfer tax?','Not automatically. The Department of Revenue lists specific exemptions, and value rules apply.')],'Pennsylvania quitclaim deed',['Official deed form rules and recording fees were not confirmed.'])
    sp('pennsylvania-sheriff-sale','Pennsylvania Sheriff Sale: Foreclosure Steps, Notices and Your Options','Pennsylvania Sheriff Sale: Foreclosure Steps','Pennsylvania mortgage foreclosure and sheriff sale: Act 6 notice, court rules, timing and your options before the sale. Official sources.','pennsylvania sheriff sale','Pennsylvania mortgage foreclosures go through county courts, and the property is sold at a sheriff sale.',facts('foreclosure'),[('Can I sell my house before a sheriff sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask your attorney or the lender for a payoff.')],'Pennsylvania sheriff sale',['Act 91 notice details and statewide sheriff-sale notice timing were not opened from official text.'])
    sp('pennsylvania-closing-costs','Pennsylvania Closing Costs: Transfer Tax, Recording and Who Pays','Pennsylvania Closing Costs for Sellers','Pennsylvania closing costs: realty transfer tax, who pays, statement of value and what a cash sale saves. Official sources.','pennsylvania closing costs','The main Pennsylvania seller closing cost we can source is realty transfer tax.',facts('property-transfer-tax'),[('Who pays Pennsylvania transfer tax?','Liability is joint and several, so parties usually agree who pays in the sales contract.')],'Pennsylvania closing costs',['The Philadelphia total rate is not confirmed on an opened page.'])
    sp('pennsylvania-probate-process','Pennsylvania Probate Process: Register of Wills, Letters and Selling Inherited Property','Pennsylvania Probate Process Explained','Pennsylvania probate: Register of Wills, letters, the $50,000 small estate limit and selling an inherited house. Official statutes.','pennsylvania probate','Pennsylvania probate runs through the county Register of Wills.',pr,[('Who can sell a house in probate?','The personal representative named by the Register of Wills signs for the estate.')],'Pennsylvania probate',['Real estate procedure details beyond what is cited.'])
    sp('pennsylvania-tax-sales','Pennsylvania Tax Sales: Upset Sales, Judicial Sales and Redemption','Pennsylvania Tax Sales: Upset and Judicial','Pennsylvania tax sales: upset and judicial sales, redemption and what to do if your property is at risk. Official sources only.','pennsylvania tax sale','Pennsylvania counties can sell property for unpaid real estate tax through tax claim bureaus.',facts('tax-sales'),[('Can I stop a tax sale?','Paying the delinquent amount or selling before the sale can pay the tax from the proceeds. Ask the county tax claim bureau for exact amounts.')],'Pennsylvania tax sales',['Redemption periods and upset sale timelines are not stated in the sources we opened.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-pa"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Pennsylvania comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Pennsylvania law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau).",f"{esc(c)} is in {esc(cty)}."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> Pennsylvania sellers owe the buyer a property disclosure and realty transfer tax applies. See "+a('pennsylvania-closing-costs','Pennsylvania closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> Pennsylvania mortgage foreclosures go through court and end in a sheriff sale. See "+a('pennsylvania-sheriff-sale','the Pennsylvania sheriff sale guide')+".</p><p><strong>Inherited house.</strong> The Register of Wills issues letters, and the inheritance tax applies. See "+a('pennsylvania-probate-process','probate')+" and "+a('pennsylvania-inheritance-tax','inheritance tax')+".</p><p><strong>Unpaid property tax.</strong> See "+a('pennsylvania-property-tax-guide','the Pennsylvania property tax guide')+" and "+a('pennsylvania-tax-sales','tax sales')+(f" and {a(ns(c)+'-pa-property-tax-guide',esc(c)+' property tax')}" if c in PTC else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, PA: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, PA | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, PA"
    rd=f"Sell your {c}, PA house: list, sell yourself or take a cash offer. Pennsylvania foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, PA house: list it, sell it yourself or take a cash offer. Pennsylvania foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=['Philadelphia','Pittsburgh']
def ptax(c,v):
    slug=f"{ns(c)}-pa-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>The statutory appeal deadline is September 1 unless the county sets a date no earlier than August 1 (53 Pa.C.S. 8844). Confirm with your county board.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, PA Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, PA Property Tax Guide",f"{c}, PA property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-pa",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=['Philadelphia','Allegheny','Montgomery','Bucks','Delaware','Chester','Lancaster','Northampton','Luzerne','Dauphin','Westmoreland','Erie']
REC=['Philadelphia','Allegheny','Montgomery','Bucks','Delaware','Chester','Lancaster','York','Berks','Lehigh','Northampton','Luzerne','Lackawanna','Dauphin','Cumberland','Westmoreland','Washington','Erie','Beaver','Butler','Centre','Monroe','Schuylkill','Lebanon','Franklin','Fayette','Cambria','Blair','Lycoming','Northumberland','Adams','Carbon','Pike','Mercer','Clearfield','Somerset','Indiana','Armstrong','Lawrence','Wayne','Columbia','Huntingdon','Union','Clarion','Venango','Crawford','Elk','Wyoming','Bedford']
BLOCK=('alleghenycountytreasurer.us','luzernecountytaxclaim.com','schuylkillcountytaxclaim.com','ncpub.org','property.co.fayette.pa.us','lasncasterdeeds.com')
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
        slug=f"{ns(cn)}-county-pa-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} handles collection and delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>The statutory default appeal deadline is September 1, and a county may set a date no earlier than August 1 (53 Pa.C.S. 8844). See the "+a('pennsylvania-property-tax-guide','Pennsylvania property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Pennsylvania bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, PA Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, PA Property Tax Guide"
        rd=f"{nm}, PA property tax: county offices, assessment appeals, tax claim bureau and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Pennsylvania property tax involves the county assessment office and the tax claim bureau."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","The county assessment or appeals board handles them. The statutory default deadline is September 1."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-pa-recorder-of-deeds"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax','statement of value|1%|joint')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, PA Recorder of Deeds: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, PA Recorder of Deeds Guide"
        rd=f"{nm}, PA recorder of deeds: where to record a deed, realty transfer tax, statement of value and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} recorder of deeds records Pennsylvania deeds and mortgages."; fk=f"{cn.lower()} county recorder of deeds"; crumb=f"{nm} recorder of deeds"
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
    os.makedirs(R+'/pages/pa',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/pa/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('pennsylvania-state-pages-1',state_pages(),'state')
    dump('pennsylvania-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('pennsylvania-city-ptax-1',[ptax(c,CP[c]) for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')],'ptax')
    dump('pennsylvania-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('pennsylvania-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
