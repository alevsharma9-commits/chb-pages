import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'ga_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'ga_cities.json'))
CP=json.load(open(H+'ga_city_ptax.json')); CT={}
for _k in 'ABCDEF': CT.update(json.load(open(H+f'ga_cty_{_k}.json')))
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
SRC=[('Georgia Department of Revenue: Property tax','https://dor.georgia.gov/local-government-services/digest-compliance/property-tax-reform'),('Georgia Department of Revenue: Homestead exemption','https://dor.georgia.gov/taxes/property-tax'),('Official Code of Georgia Annotated','https://www.legis.ga.gov/')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-georgia','we buy houses in Georgia')+"."
HOW=lambda:ol(["Find out what the closing attorney needs. Georgia closings are usually handled by an attorney, and for an inherited or transferred house that means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('georgia-property-tax-guide','Georgia property tax guide','Appeals and exemptions.'),('georgia-homestead-exemption','Georgia homestead exemption','Eligibility and filing.'),('georgia-foreclosure-process','Georgia foreclosure process','Sale steps.'),('we-buy-houses-in-georgia','We buy houses in Georgia','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from Georgia statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Georgia',cards)+sources(srcs)+DISCLAIM('Georgia','attorney or tax professional')+schema(faqs,[('Home',SITE),('Georgia',SITE+'we-buy-houses-in-georgia/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Georgia',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Georgia?','We buy Georgia houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+sec('What the official sources say',items)+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell a Georgia house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling a Georgia House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    T=lambda k:facts(k) if k in FS else []
    pt=T('property-tax-appeals'); pr=T('probate-and-inherited-property'); tt=T('property-transfer-tax'); ts=T('tax-sales'); te=T('tenant-occupied-sale')+T('eviction-process'); dr=T('deeds-recording'); fc=T('foreclosure')+T('sheriff-sale'); hs=T('homestead-exemption'); et=T('estate-tax'); qd=T('quitclaim-deed'); cc=T('closing-costs'); tl=T('tax-lien'); cg=T('capital-gains')
    sp('georgia-property-tax-guide','Georgia Property Tax Guide: 45-Day Appeals, Homestead and Selling With Tax Due','Georgia Property Tax Guide: Appeals and Homestead','Georgia property tax: the 45-day appeal window, homestead exemption, delinquent tax and selling a house with tax due. Official sources.','georgia property tax','Georgia property tax is assessed by the county board of tax assessors and collected by the county tax commissioner.',pt+ts[:2],[('How long do I have to appeal my Georgia assessment?','The Department of Revenue says an owner may appeal within 45 days of the date the assessment notice was mailed.'),('What happens to unpaid property tax when I sell?','The closing attorney pays unpaid tax from the sale proceeds at closing.')],'Georgia property tax',['Statewide millage rates, which vary by county, city and school district.'])
    sp('georgia-homestead-exemption','Georgia Homestead Exemption: Eligibility, April 1 Deadline and Filing','Georgia Homestead Exemption: Eligibility and Filing','Georgia homestead exemption: who qualifies, the filing deadline, senior and disabled veteran exemptions and what happens when you sell. Official sources.','georgia homestead exemption','Georgia homeowners can claim a homestead exemption on their legal residence, and the Department of Revenue explains the rules.',hs,[('Where do I apply for the homestead exemption?','With the county tax commissioner, or the assessor in some counties. Confirm your county rules.')],'Georgia homestead exemption',['Exact local exemption amounts, which differ by county.'])
    sp('georgia-foreclosure-process','Georgia Foreclosure Process: Power of Sale, First Tuesday Sales and Your Options','Georgia Foreclosure Process Explained','Georgia non-judicial foreclosure: notice, the first Tuesday sale at the courthouse and what you can do before the sale. Official sources.','georgia foreclosure process','Most Georgia foreclosures use a power of sale and happen on the first Tuesday of the month.',fc,[('Can I sell my house before a foreclosure sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask for a payoff figure.')],'Georgia foreclosure process',['Deficiency confirmation and post-sale redemption details were not confirmed on official pages.'])
    sp('georgia-estate-tax','Georgia Estate Tax: No State Estate or Inheritance Tax','Georgia Estate Tax: What Heirs Owe','Georgia has no state estate or inheritance tax. See what the Department of Revenue says and how it affects selling an inherited house.','georgia estate tax','Georgia has no state estate tax, according to the Department of Revenue.',et,[('Does Georgia have an estate tax?','The statute cited by the Department of Revenue says no state estate tax is levied on or after July 1, 2014.')],'Georgia estate tax',['Federal estate tax is outside this guide.'])
    sp('georgia-eviction-process','Georgia Eviction Process (Dispossessory) and Selling a Rented House','Georgia Eviction Process and Tenants','Georgia eviction process and what it means when you sell a house with tenants. Official sources only.','georgia eviction process','Georgia evictions are called dispossessory actions and run through county courts.',te,[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'Georgia eviction process',['Whether a sale ends a lease was not confirmed on an official page.'])
    sp('georgia-quitclaim-deed','Georgia Quitclaim Deed: Recording, Transfer Tax and When It Works','Georgia Quitclaim Deed: Recording and Fees','Georgia quitclaim deed: recording with the Clerk of Superior Court, the transfer tax and who pays. Official sources only.','georgia quitclaim deed','A Georgia deed is recorded with the Clerk of Superior Court in the county where the land sits.',qd+dr[:3]+tt[:3],[('Where do I record a Georgia deed?','With the Clerk of Superior Court of the county where the property is located.')],'Georgia quitclaim deed',['A county by county recording fee table was not retrieved.'])
    sp('georgia-transfer-on-death-deed','Georgia Transfer on Death Deed: How It Works','Georgia Transfer on Death Deed Explained','Georgia transfer on death deed under O.C.G.A. 44-17: how it works, who signs and what beneficiaries do. Official sources only.','georgia transfer on death deed','Georgia allows an owner to name beneficiaries for real estate through a transfer on death deed.',pr,[('What is a transfer on death deed?','A recorded deed that names who receives the property at the owner death.')],'Georgia transfer on death deed',['Whether the 2026 bill text was signed into law was not confirmed.'])
    sp('georgia-closing-costs','Georgia Closing Costs: Transfer Tax, Recording and What Sellers Pay','Georgia Closing Costs for Sellers','Georgia seller closing costs: the real estate transfer tax, recording and what a cash sale saves. Official sources.','georgia closing costs','The main Georgia seller closing cost we can source is the real estate transfer tax.',cc+tt,[('Who pays the Georgia transfer tax?','Check the Department of Revenue page cited above for the rule.')],'Georgia closing costs',['Local recording fees by county.'])
    sp('georgia-tax-lien','Georgia Tax Liens: Tax Executions and Delinquent Property Tax','Georgia Tax Liens and Delinquent Tax','Georgia delinquent property tax: tax liens, executions and tax sales. Official sources only.','georgia tax lien','Georgia counties pursue delinquent property tax through liens and executions.',tl+ts[:3],[('Can I stop a tax sale?','Paying the delinquent amount or selling before the sale can pay the tax from the proceeds. Ask the county tax commissioner for exact figures.')],'Georgia tax lien',['Statute text for some tax sale rules appears only on non-official sites.'])
    sp('georgia-probate-process','Georgia Probate Process: Year Support and Selling Inherited Property','Georgia Probate Process Explained','Georgia probate: probate court, year support, TOD deeds and selling an inherited house. Official sources only.','georgia probate','Georgia probate runs through the county probate court.',pr,[('Who can sell a house in probate?','The executor or administrator with court authority signs for the estate.')],'Georgia probate',['Other estate release procedures.'])
    sp('georgia-capital-gains-tax','Georgia Capital Gains Tax on Selling a House','Georgia Capital Gains Tax on a House Sale','Georgia capital gains tax: how the Department of Revenue treats gains when you sell a house.','georgia capital gains tax','Georgia does not tax capital gains differently than other income, according to the Department of Revenue.',cg,[('Does Georgia tax capital gains?','The Department of Revenue says capital gains are not taxed differently than other income.')],'Georgia capital gains tax',['Federal rules and the home sale exclusion are outside this guide.'])
    sp('georgia-tax-sale','Georgia Tax Sales: Redemption and Selling Before the First Tuesday Sale','Georgia Tax Sales and Redemption','Georgia tax sales: redemption period, premium and selling a house with delinquent tax. Official sources only.','georgia tax sale','Georgia counties hold tax sales of delinquent property, usually on the first Tuesday.',ts+tl,[('Can I redeem after a tax sale?','County tax commissioner pages describe a redemption period and premium. Confirm exact amounts with your county.')],'Georgia tax sale',['Statute text appears on non-official sites, so county pages are cited instead.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-ga"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Georgia comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Georgia law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> A seller handling the sale directly still needs a deed, a closing attorney and to account for the real estate transfer tax. See "+a('georgia-closing-costs','Georgia closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> Most Georgia foreclosures use a power of sale outside court, with sales held at the courthouse on the first Tuesday of the month. See "+a('georgia-foreclosure-process','the Georgia foreclosure guide')+".</p><p><strong>Inherited house.</strong> The probate court handles the estate, and Georgia has no state estate or inheritance tax. See "+a('georgia-probate-process','probate')+" and "+a('georgia-estate-tax','estate tax')+".</p><p><strong>Unpaid property tax.</strong>  See "+a('georgia-property-tax-guide','the Georgia property tax guide')+" and "+a('georgia-tax-sale','tax sales')+(f" and {a(ns(c)+'-ga-property-tax-guide',esc(c)+' property tax')}" if c in PTCOK else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, GA: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, GA | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, GA"
    rd=f"Sell your {c}, GA house: list, sell yourself or take a cash offer. Georgia foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, GA house: list it, sell it yourself or take a cash offer. Georgia foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=['Savannah','Atlanta','Decatur','Columbus','Augusta','Marietta','Smyrna','Athens','Gainesville','Warner Robins','Alpharetta','Albany','Kennesaw','Macon','Lawrenceville']
PTCOK=[c for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')]
def ptax(c,v):
    slug=f"{ns(c)}-ga-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>Owners generally have 45 days from the date the assessment notice was mailed to appeal to the county Board of Tax Assessors (O.C.G.A. 48-5-311). Confirm with your county.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, GA Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, GA Property Tax Guide",f"{c}, GA property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-ga",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=json.load(open(H+'ga_cty_list.json'))['ptax']
REC=json.load(open(H+'ga_cty_list.json'))['rec']
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
        slug=f"{ns(cn)}-county-ga-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} bills and collects the tax and handles delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>Owners generally have 45 days from the date the assessment notice was mailed to appeal to the county Board of Tax Assessors (O.C.G.A. 48-5-311). See the "+a('georgia-property-tax-guide','Georgia property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Georgia bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, GA Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, GA Property Tax Guide"
        rd=f"{nm}, GA property tax: county offices, assessment appeals, county tax commissioner and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Georgia property tax involves the county assessment office and the county tax commissioner."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","Appeals go to the county Board of Tax Assessors, generally within 45 days of the date the assessment notice was mailed."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-ga-clerk-of-superior-court"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, GA Clerk of Superior Court: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, GA Clerk of Superior Court Guide"
        rd=f"{nm}, GA clerk of superior court: where to record a deed, real estate transfer tax, and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} clerk of superior court records Georgia deeds and mortgages."; fk=f"{cn.lower()} county clerk of superior court"; crumb=f"{nm} clerk of superior court"
        faqs=[(f"Where do I record a deed in {nm}?","With the Clerk of Superior Court. Confirm submission rules on the county page."),("Do I owe real estate transfer tax?","Real estate transfer tax can apply to deeds. The Department of Revenue explains the rule.")]
    body=(f"<p><strong>{lead}</strong> This guide lists what we confirmed on official pages.</p>"+s+cta(f"Selling in {nm}?",f"We buy {nm} houses as-is, with no commission, no repairs and no closing costs to you.")+(UNC(unc) if unc else '')+f"<h2>How to sell a house in {esc(nm)}</h2>"+HOW())
    srcs=([(nm_(co if kind=='tax' else rc),(co if kind=='tax' else rc)['url'])] if (co if kind=='tax' else rc).get('url') else [])+SRC[:2]
    return mk(slug,h1,rt,rd,fk,f"Selling in {nm}? Get a Cash Offer",f"We buy {nm} houses as-is and reply with a written cash offer.",body,faqs,crumb,SP,srcs)
if __name__=='__main__':
    seen=set(); cities=[]
    for d in CITIES:
        k=ns(d['city'])
        if k in seen: continue
        seen.add(k); cities.append(d)
    os.makedirs(R+'/pages/ga',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/ga/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('georgia-state-pages-1',state_pages(),'state')
    dump('georgia-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('georgia-city-ptax-1',[ptax(c,CP[c]) for c in PTCOK],'ptax')
    dump('georgia-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('georgia-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
