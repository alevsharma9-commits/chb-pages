import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'oh_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'oh_cities.json'))
CP=json.load(open(H+'oh_city_ptax.json')); CT={}
for _k in 'ABCD': CT.update(json.load(open(H+f'oh_cty_{_k}.json')))
BAD=re.compile(r'ilmarion|ohiotreasurers|excerpt|not opened|not confirmed|not stated|unconfirmed|http|phone',re.I)
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
SRC=[('Ohio Department of Taxation: Real property','https://tax.ohio.gov/individual/resources/property-tax'),('Ohio Revised Code','https://codes.ohio.gov/ohio-revised-code'),('Ohio Department of Taxation: Estate tax','https://tax.ohio.gov/individual/resources/estate-tax')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-ohio','we buy houses in Ohio')+"."
HOW=lambda:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('ohio-property-tax-guide','Ohio property tax guide','Appeals and exemptions.'),('ohio-homestead-exemption','Ohio homestead exemption','Eligibility and filing.'),('ohio-sheriff-sale','Ohio sheriff sale','Foreclosure sale steps.'),('we-buy-houses-in-ohio','We buy houses in Ohio','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from Ohio statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Ohio',cards)+sources(srcs)+DISCLAIM('Ohio','attorney or tax professional')+schema(faqs,[('Home',SITE),('Ohio',SITE+'we-buy-houses-in-ohio/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Ohio',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Ohio?','We buy Ohio houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+sec('What the official sources say',items)+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell an Ohio house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling an Ohio House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    T=lambda k:facts(k) if k in FS else []
    pt=T('property-tax-appeals'); pr=T('probate-and-inherited-property'); tt=T('property-transfer-tax'); ts=T('tax-sales'); te=T('tenant-occupied-sale'); dr=T('deeds-recording'); fc=T('foreclosure'); lc=T('land-contracts')
    sp('ohio-property-tax-guide','Ohio Property Tax Guide: Board of Revision Complaints, Homestead and Selling With Tax Due','Ohio Property Tax Guide: Appeals and Homestead','Ohio property tax: Board of Revision complaint deadline, homestead exemption, delinquent tax and selling a house with tax due. Official sources.','ohio property tax','Ohio property tax is assessed by the county auditor, and owners can file a valuation complaint with the county Board of Revision.',pt+ts[:3],[('When is the Board of Revision complaint deadline?','Under ORC 5715.19, complaints are due by March 31 or the close of first-half collection, whichever is later, according to the statute text the research opened.'),('What happens to unpaid property tax when I sell?','The title company pays unpaid tax from the sale proceeds at closing.')],'Ohio property tax',['Homestead income limits and the current rollback percentages.'])
    sp('ohio-homestead-exemption','Ohio Homestead Exemption: Eligibility, Filing and Selling the Home','Ohio Homestead Exemption: Eligibility and Filing','Ohio homestead exemption for older and disabled homeowners: who qualifies, how to file with the county auditor and what happens when you sell.','ohio homestead exemption','Ohio offers a homestead exemption that reduces taxable value for eligible homeowners, and owners apply with the county auditor.',pt,[('Where do I apply for the homestead exemption?','With the county auditor. Filing dates and forms are set locally.')],'Ohio homestead exemption',['Current income limits and exemption amounts.'])
    sp('ohio-sheriff-sale','Ohio Sheriff Sale: Foreclosure Steps, Appraisal and Redemption','Ohio Sheriff Sale: Foreclosure Steps','Ohio foreclosure and sheriff sale: appraisal, the two-thirds minimum, notice, confirmation and redemption before confirmation. Official statutes.','ohio sheriff sale','Ohio mortgage foreclosures go through the court of common pleas and end in a sheriff sale.',fc,[('Can I sell my house before a sheriff sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask for a payoff figure.')],'Ohio sheriff sale',['Post-confirmation redemption is not expressly stated in the statute text opened.'])
    sp('ohio-estate-tax','Ohio Estate Tax: Repeal and What Heirs Owe When Selling','Ohio Estate Tax: Repeal and What Heirs Owe','Ohio estate tax repeal, what applies to deaths on or after 2013 and how it affects selling an inherited house. Department of Taxation sources.','ohio estate tax','Ohio repealed its estate tax for deaths on or after January 1, 2013, according to the Department of Taxation.',pr,[('Does Ohio have an estate tax?','The Department of Taxation says the estate tax was repealed for deaths on or after January 1, 2013.')],'Ohio estate tax',['Federal estate tax is outside this guide.'])
    sp('ohio-land-contract','Ohio Land Contracts: Rules for Sellers Under ORC 5313','Ohio Land Contracts: Seller Rules','Ohio land contracts under ORC 5313: what they are, key rules for sellers and what to know before selling a house on contract.','ohio land contract','An Ohio land contract lets a buyer pay over time while the seller keeps title until the contract is paid.',lc or dr,[('What is a land contract?','A contract where the buyer pays in installments and the seller keeps legal title until a set point. Chapter 5313 of the Ohio Revised Code governs them.')],'Ohio land contract',['Detailed forfeiture and cure rules were not confirmed.'])
    sp('ohio-eviction-process','Ohio Eviction Process and Selling a Rented House','Ohio Eviction Process and Tenants','Ohio eviction process under ORC 1923 and what it means when you sell a house with tenants. Official statutes only.','ohio eviction process','Ohio evictions follow notice and court steps set by the Revised Code.',te,[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'Ohio eviction process',['Whether a sale ends a lease was not confirmed.'])
    sp('ohio-quitclaim-deed','Ohio Quitclaim Deed: Recording, Conveyance Fee and When It Works','Ohio Quitclaim Deed: Recording and Fees','Ohio quitclaim deed: recording with the county recorder, the conveyance fee and who pays it. Official sources only.','ohio quitclaim deed','An Ohio deed is recorded with the county recorder, and the conveyance fee can apply.',dr+tt[:4],[('Who pays the Ohio conveyance fee?','ORC 319.202 makes the grantor pay the mandatory fee and any county permissive tax.')],'Ohio quitclaim deed',['A county by county conveyance fee table was not retrieved.'])
    sp('ohio-transfer-on-death-affidavit','Ohio Transfer on Death Designation Affidavit: How It Works','Ohio Transfer on Death Affidavit Explained','Ohio transfer on death designation affidavit under ORC 5302.22: how it works, who signs and what heirs do when a TOD owner dies.','ohio transfer on death affidavit','Ohio allows an owner to name a beneficiary for real estate through a transfer on death designation affidavit.',pr,[('What is a TOD designation affidavit?','A recorded affidavit that names who receives the property at the owner death under ORC 5302.22.')],'Ohio transfer on death affidavit',['Steps for beneficiaries after the owner dies were not fully confirmed.'])
    sp('ohio-closing-costs','Ohio Closing Costs: Conveyance Fee, Recording and What Sellers Pay','Ohio Closing Costs for Sellers','Ohio seller closing costs: the conveyance fee, who pays it, recording and what a cash sale saves. Official sources.','ohio closing costs','The main Ohio seller closing cost we can source is the conveyance fee.',tt,[('Who pays the Ohio conveyance fee?','The grantor pays under ORC 319.202.')],'Ohio closing costs',['County permissive rates by county.'])
    sp('ohio-tax-lien','Ohio Tax Liens and Tax Foreclosure: Delinquent Land and Redemption','Ohio Tax Liens and Tax Foreclosure','Ohio delinquent property tax: tax certificates, tax foreclosure and redemption. Official statutes only.','ohio tax lien','Ohio counties pursue delinquent property tax through liens, tax certificates and foreclosure.',ts,[('Can I stop a tax foreclosure?','Paying the delinquent amount or selling before the sale can pay the tax from the proceeds. Ask the county treasurer for exact figures.')],'Ohio tax lien',['Tax certificate sale program details.'])
    sp('ohio-probate-process','Ohio Probate Process: Small Estates and Selling Inherited Property','Ohio Probate Process Explained','Ohio probate: probate court, small estate thresholds, TOD affidavits and selling an inherited house. Official statutes only.','ohio probate','Ohio probate runs through the county probate court.',pr,[('Who can sell a house in probate?','The executor or administrator with court authority signs for the estate.')],'Ohio probate',['Other estate release procedures.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-oh"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Ohio comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Ohio law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> Ohio sellers owe the buyer a property disclosure and realty transfer tax applies. See "+a('ohio-closing-costs','Ohio closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> Ohio mortgage foreclosures go through court and end in a sheriff sale. See "+a('ohio-sheriff-sale','the Ohio foreclosure guide')+".</p><p><strong>Inherited house.</strong> The probate court handles the estate, and Ohio repealed its estate tax for deaths on or after January 1, 2013. See "+a('ohio-probate-process','probate')+" and "+a('ohio-estate-tax','estate tax')+".</p><p><strong>Unpaid property tax.</strong>  See "+a('ohio-property-tax-guide','the Ohio property tax guide')+" and "+a('ohio-tax-lien','tax sales')+(f" and {a(ns(c)+'-oh-property-tax-guide',esc(c)+' property tax')}" if c in PTCOK else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, OH: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, OH | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, OH"
    rd=f"Sell your {c}, OH house: list, sell yourself or take a cash offer. Ohio foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, OH house: list it, sell it yourself or take a cash offer. Ohio foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=['Akron','Cincinnati','Cleveland','Columbus','Dayton','Delaware','Medina','Toledo']
PTCOK=[c for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')]
def ptax(c,v):
    slug=f"{ns(c)}-oh-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>Board of Revision complaints are generally due by March 31 or the close of first-half collection, whichever is later (ORC 5715.19). Confirm with your county board.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, OH Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, OH Property Tax Guide",f"{c}, OH property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-oh",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT='Allen Ashtabula Athens Belmont Butler Clark Clermont Columbiana Cuyahoga Darke Delaware Fairfield Franklin Geauga Greene Hamilton Highland Lake Licking Lorain Lucas Mahoning Medina Miami Montgomery Muskingum Portage Richland Ross Scioto Stark Summit Trumbull Union Warren Wayne Wood'.split()
REC='adams|allen|ashland|ashtabula|athens|auglaize|belmont|brown|butler|carroll|champaign|clark|clermont|clinton|columbiana|coshocton|crawford|cuyahoga|darke|defiance|delaware|erie|fairfield|fayette|franklin|fulton|gallia|geauga|greene|guernsey|hamilton|hancock|hardin|harrison|henry|highland|hocking|holmes|huron|jackson|jefferson|knox|lake|lawrence|licking|logan|lorain|lucas|madison|mahoning|marion|medina|meigs|mercer|miami|monroe|montgomery|morgan|morrow|muskingum|noble|ottawa|paulding|perry|pickaway|pike|portage|preble|putnam|richland|ross|sandusky|scioto|seneca|shelby|stark|summit|trumbull|tuscarawas|union|vinton|warren|washington|wayne|williams|wood|wyandot'.split('|')
REC=[x for x in CT if x.lower() in REC]
BLOCK=()
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
        slug=f"{ns(cn)}-county-oh-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} handles collection and delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>Board of Revision complaints are generally due by March 31 or the close of first-half collection, whichever is later (ORC 5715.19). See the "+a('ohio-property-tax-guide','Ohio property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Ohio bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, OH Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, OH Property Tax Guide"
        rd=f"{nm}, OH property tax: county offices, assessment appeals, county treasurer and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Ohio property tax involves the county assessment office and the county treasurer."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","The county Board of Revision handles them, and complaints are generally due by March 31 or the close of first-half collection, whichever is later."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-oh-recorder-of-deeds"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax','statement of value|1%|joint')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, OH Recorder of Deeds: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, OH Recorder of Deeds Guide"
        rd=f"{nm}, OH recorder of deeds: where to record a deed, realty transfer tax, statement of value and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} recorder of deeds records Ohio deeds and mortgages."; fk=f"{cn.lower()} county recorder of deeds"; crumb=f"{nm} recorder of deeds"
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
    os.makedirs(R+'/pages/oh',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/oh/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('ohio-state-pages-1',state_pages(),'state')
    dump('ohio-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('ohio-city-ptax-1',[ptax(c,CP[c]) for c in PTCOK],'ptax')
    dump('ohio-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('ohio-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
