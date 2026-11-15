import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'nc_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'nc_cities.json'))
CP=json.load(open(H+'nc_city_ptax.json')); CT={}
for _k in 'ABCDEF': CT.update(json.load(open(H+f'nc_cty_{_k}.json')))
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
SRC=[('North Carolina Department of Revenue','https://www.ncdor.gov/'),('North Carolina General Statutes','https://www.ncleg.gov/Laws/GeneralStatutes'),('North Carolina Judicial Branch','https://www.nccourts.gov/')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-north-carolina','we buy houses in North Carolina')+"."
HOW=lambda:ol(["Find out what the closing attorney needs. North Carolina closings run through an attorney, and for an inherited or transferred house that means the recorded deed or the estate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('north-carolina-property-tax-guide','North Carolina property tax guide','Appeals and exemptions.'),('north-carolina-homestead-exemption','North Carolina homestead exemption','Eligibility and filing.'),('north-carolina-excise-tax','North Carolina excise tax','Who pays at closing.'),('we-buy-houses-in-north-carolina','We buy houses in North Carolina','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    full=(f"<p><em>Last updated {DATE}. Citations come from North Carolina statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('North Carolina',cards)+sources(srcs)+DISCLAIM('North Carolina','attorney or tax professional')+schema(faqs,[('Home',SITE),('North Carolina',SITE+'we-buy-houses-in-north-carolina/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('North Carolina',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in North Carolina?','We buy North Carolina houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+(sec('What the official sources say',items) if items else '')+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell a North Carolina house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling a North Carolina House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    T=lambda k:facts(k) if k in FS else []
    pt=T('property-tax-appeals'); pr=T('probate-and-inherited-property'); tt=T('property-transfer-tax'); tl=T('tax-liens')+T('tax-sales'); te=T('eviction-process')+T('tenant-occupied-sale'); dr=T('deeds-recording'); hs=T('homestead-exemption'); qd=T('quitclaim-deed'); cc=T('closing-costs'); cg=T('capital-gains')
    sp('north-carolina-property-tax-guide','North Carolina Property Tax Guide: Appeals, Homestead and Selling With Tax Due','North Carolina Property Tax Guide: Appeals','North Carolina property tax: board of equalization and review, appeals, homestead exclusion and selling a house with tax due. Official sources.','north carolina property tax','North Carolina counties assess and collect property tax, and owners can appeal to the county board of equalization and review.',pt+tl[:3],[('Who hears property tax appeals in North Carolina?','The county board of equalization and review hears appeals, according to the statutes cited above.'),('What happens to unpaid property tax when I sell?','The closing attorney pays unpaid tax from the sale proceeds at closing.')],'North Carolina property tax',['The Property Tax Commission appeal deadline.'])
    sp('north-carolina-homestead-exemption','North Carolina Homestead Exclusion: Elderly and Disabled Owners and How to Apply','North Carolina Homestead Exclusion: Who Qualifies','North Carolina property tax homestead exclusion for owners 65 and older or disabled: eligibility, the exclusion amount and how to apply.','north carolina homestead exemption','North Carolina offers a property tax exclusion for qualifying elderly or disabled homeowners.',hs,[('Where do I apply for the homestead exclusion?','With the county tax office. Confirm the application window with your county.')],'North Carolina homestead exemption',['The current income limit, which we did not confirm on an opened page.'])
    sp('north-carolina-eviction-process','North Carolina Eviction Process (Summary Ejectment) and Selling a Rented House','North Carolina Eviction Process and Tenants','North Carolina summary ejectment and what it means when you sell a house with tenants. Official sources only.','north carolina eviction process','North Carolina evictions are called summary ejectment and run through the register of deeds and magistrates.',te,[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'North Carolina eviction process',['Whether a voluntary sale ends a lease.'])
    sp('north-carolina-quitclaim-deed','North Carolina Quitclaim Deed: Who Can Prepare It, Excise Tax and Recording','North Carolina Quitclaim Deed: Rules and Fees','North Carolina quitclaim deed: attorney preparation, excise tax exemptions and recording with the register of deeds. Official sources only.','north carolina quitclaim deed','North Carolina deeds are recorded with the register of deeds, and preparing them is the practice of law.',qd+dr[:3],[('Do I need an attorney for a deed in North Carolina?','The statutes cited above treat preparing a deed as the practice of law.')],'North Carolina quitclaim deed',['A statute defining a quitclaim deed.'])
    sp('north-carolina-closing-costs','North Carolina Closing Costs for Sellers: Excise Tax, Attorney and Recording','North Carolina Closing Costs for Sellers','North Carolina seller closing costs: the excise tax, attorney involvement and what a cash sale saves. Official sources.','north carolina closing costs','The main North Carolina seller closing cost we can source is the excise tax on the deed.',cc+tt[:3],[('Who pays the North Carolina excise tax?','The seller pays it to the register of deeds before recording.')],'North Carolina closing costs',['Typical total seller cost figures.'])
    sp('north-carolina-probate-process','North Carolina Probate Process and Small Estate Affidavit for Real Estate','North Carolina Probate and Small Estates','North Carolina probate: the register of deeds, letters of administration and selling an inherited house. Official sources only.','north carolina probate','North Carolina probate runs through the elected register of deeds.',pr+T('estate-tax'),[('Who handles probate in North Carolina?','The register of deeds acts as probate judge.')],'North Carolina probate',['Small estate affidavit steps for real property.'])
    sp('north-carolina-excise-tax','North Carolina Excise Tax on Deeds: $1 Per $500 and Who Pays','North Carolina Excise Tax on Deeds','North Carolina excise tax on conveyances: the rate, who pays and exemptions when you sell a house. Official sources only.','north carolina excise tax','North Carolina charges an excise tax on conveyances of real property.',tt,[('What is the North Carolina excise tax rate?','The statute cited above sets it at $1 per $500 of consideration.')],'North Carolina excise tax',['County level exceptions.'])
    sp('north-carolina-capital-gains-tax','North Carolina Capital Gains Tax When You Sell a House','North Carolina Capital Gains Tax on a House','North Carolina income tax treatment when you sell a house: what the Department of Revenue says.','north carolina capital gains tax','North Carolina taxes income at a flat individual rate, and we only state what official pages confirm.',cg,[('Does North Carolina have a separate capital gains tax?','We confirmed only the flat individual income tax rate on an official page.')],'North Carolina capital gains tax',['Federal rules and the home sale exclusion are outside this guide.'])
    sp('north-carolina-transfer-on-death-deed','North Carolina Transfer on Death Deed: What We Could and Could Not Confirm','North Carolina Transfer on Death Deed','North Carolina transfer on death deed: what we found on official pages and what we could not confirm.','north carolina transfer on death deed','We could not confirm a North Carolina transfer on death deed statute on an official page.',[],[('Does North Carolina allow transfer on death deeds?','We could not confirm that on an official page, so we do not state it.')],'North Carolina transfer on death deed',['Whether any North Carolina statute authorizes a transfer on death deed.'])
    sp('north-carolina-register-of-deeds','North Carolina Register of Deeds: Recording Fees and What to Bring','North Carolina Register of Deeds Guide','North Carolina register of deeds: where deeds are recorded, statewide recording fees and the excise tax. Official sources.','north carolina register of deeds','Each North Carolina county has a register of deeds who records deeds and deeds of trust.',dr+tt[:2],[('Where do I record a deed in North Carolina?','With the register of deeds in the county where the property is located.')],'North Carolina register of deeds',['E-recording authority.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-nc"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, North Carolina comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under North Carolina law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> A seller handling the sale directly still needs a deed, a closing attorney and to account for the real estate transfer tax. See "+a('north-carolina-closing-costs','North Carolina closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> North Carolina power-of-sale foreclosures need a hearing before the clerk of superior court, and a 10-day upset bid period follows the sale. See "+a('north-carolina-property-tax-guide','the North Carolina property tax guide')+" for tax issues that can come up.</p><p><strong>Inherited house.</strong> The clerk of superior court handles estates, and North Carolina repealed its estate tax for deaths on or after January 1, 2013. See "+a('north-carolina-probate-process','probate')+".</p><p><strong>Unpaid property tax.</strong> See "+a('north-carolina-property-tax-guide','the North Carolina property tax guide')+(f" and {a(ns(c)+'-nc-property-tax-guide',esc(c)+' property tax')}" if c in PTCOK else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, NC: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, NC | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, NC"
    rd=f"Sell your {c}, NC house: list, sell yourself or take a cash offer. North Carolina foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, NC house: list it, sell it yourself or take a cash offer. North Carolina foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=["Durham", "Charlotte", "Raleigh", "Greensboro", "Winston-Salem", "Fayetteville", "Cary", "Wilson"]
PTCOK=[c for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')]
def ptax(c,v):
    slug=f"{ns(c)}-nc-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>In North Carolina, property tax appeals go to the county board of equalization and review (see the N.C.G.S. cited in the statewide guide). Confirm with your county.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str(r['value'])))} for {r.get('year')}. See the {L(r['url'],'official page')}.</p>" if r and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, NC Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, NC Property Tax Guide",f"{c}, NC property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-nc",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=json.load(open(H+'nc_cty_list.json'))['ptax']
REC=json.load(open(H+'nc_cty_list.json'))['rec']
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
        slug=f"{ns(cn)}-county-nc-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} bills and collects the tax and handles delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>In North Carolina, property tax appeals go to the county board of equalization and review (see the N.C.G.S. cited in the statewide guide). See the "+a('north-carolina-property-tax-guide','North Carolina property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. North Carolina bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, NC Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, NC Property Tax Guide"
        rd=f"{nm}, NC property tax: county offices, assessment appeals, county tax collector and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, North Carolina property tax involves the county assessment office and the county tax collector."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","Appeals go to the county board of equalization and review."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-nc-register-of-deeds"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, NC Register of Deeds: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, NC Register of Deeds Guide"
        rd=f"{nm}, NC register of deeds: where to record a deed, real estate transfer tax, and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} register of deeds records North Carolina deeds and mortgages."; fk=f"{cn.lower()} county register of deeds"; crumb=f"{nm} register of deeds"
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
    os.makedirs(R+'/pages/nc',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/nc/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('north-carolina-state-pages-1',state_pages(),'state')
    dump('north-carolina-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('north-carolina-city-ptax-1',[ptax(c,CP[c]) for c in PTCOK],'ptax')
    dump('north-carolina-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('north-carolina-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
