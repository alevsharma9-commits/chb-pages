import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..'); H='/home/claude/chb/'
FS=json.load(open(H+'in_fact_sheet.json'))['topics']; CITIES=json.load(open(H+'in_cities.json'))
CP=json.load(open(H+'in_city_ptax.json')); CT={}
for _k in 'ABC': CT.update(json.load(open(H+f'in_cty_{_k}.json')))
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
SRC=[('Indiana Department of Local Government Finance', 'https://www.in.gov/dlgf/'), ('Indiana Code', 'https://iga.in.gov/laws/2025/ic/titles'), ('Indiana Courts', 'https://www.in.gov/courts/')]
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-indiana','we buy houses in Indiana')+"."
HOW=lambda:ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[('indiana-property-tax-guide','Indiana Property Tax Guide: Appeals','Official sources.'),('indiana-homestead-exemption','Indiana Homestead Exemption Guide','Official sources.'),('indiana-estate-tax','Indiana Estate and Inheritance Tax','Official sources.'),('we-buy-houses-in-indiana','We buy houses in Indiana','How a cash offer works.')]
def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):
    rd=rd if len(rd)<=155 else rd[:152].rsplit(' ',1)[0]+'.'
    rt=rt if len(rt)<=62 else rt[:62].rsplit(' ',1)[0]
    full=(f"<p><em>Last updated {DATE}. Citations come from Indiana statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"+body+f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related('Indiana',cards)+sources(srcs)+DISCLAIM('Indiana','attorney or tax professional')+schema(faqs,[('Home',SITE),('Indiana',SITE+'we-buy-houses-in-indiana/'),(crumb,SITE+slug+'/')]))
    return wrap(slug,h1,hero('Indiana',h1,h2,hp),full,rt,rd,fk)
def sec(t,i): return f"<h2>{t}</h2>"+ul(i) if i else ''
CTAA=cta('Selling in Indiana?','We buy Indiana houses as-is, with no commission, no repairs and no closing costs to you.')
UNC=lambda items:"<h2>What we could not confirm</h2>"+ul(items)
def state_pages():
    P=[]
    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):
        body=f"<p><strong>{lead}</strong> Here is what the official sources say.</p>"+(sec('What the official sources say',items) if items else '')+CTAA+(UNC(unc) if unc else '')+"<h2>How to sell a Indiana house when this applies to you</h2>"+HOW()
        P.append(mk(slug,h1,rt,rd,fk,'Selling a Indiana House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))
    def F(spec):
        out=[]
        for t in spec:
            k,_,n_=t.partition(':')
            if k in FS:
                x=facts(k); out+=x[:int(n_)] if n_ else x
        return out
    sp('indiana-property-tax-guide','Indiana Property Tax Guide: Appeals, Exemptions and Selling With Tax Due','Indiana Property Tax Guide: Appeals','Indiana property tax: appeals, exemptions, delinquent tax and selling a house with tax due. Official sources.','indiana property tax','Indiana property tax is assessed and collected at the local level, and owners can appeal an assessment.',F(['property-tax-appeals', 'tax-sales:2']),[('What happens to unpaid property tax when I sell?','The closing agent pays unpaid tax from the sale proceeds at closing.')],'Indiana Property Tax Guide: Appeals',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-homestead-exemption','Indiana Homestead Exemption: Eligibility, Filing and Selling the Home','Indiana Homestead Exemption Guide','Indiana homestead exemption: who qualifies, how to apply and what happens when you sell. Official sources only.','indiana homestead exemption','Indiana offers property tax relief for qualifying homeowners, and official sources explain the rules.',F(['homestead-exemption']),[('Where do I apply for the homestead exemption?','Apply with the local assessor or county office named in the sources above. Confirm the deadline with your county.')],'Indiana Homestead Exemption Guide',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-estate-tax','Indiana Estate and Inheritance Tax: What Heirs Owe When Selling','Indiana Estate and Inheritance Tax','Indiana estate and inheritance tax rules and how they affect heirs selling an inherited house. Official sources only.','indiana estate tax','This guide covers what official sources say about Indiana estate and inheritance tax.',F(['estate-tax']),[('Does Indiana have an estate tax?','See the official sources above. We state only what we could confirm on official pages.')],'Indiana Estate and Inheritance Tax',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-eviction-process','Indiana Eviction Process and Selling a Rented House','Indiana Eviction Process and Tenants','Indiana eviction process and what it means when you sell a house with tenants. Official sources only.','indiana eviction process','Indiana evictions follow notice and court steps set by state law.',F(['eviction-process', 'tenant-occupied-sale']),[('Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.')],'Indiana Eviction Process and Tenants',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-quitclaim-deed','Indiana Quitclaim Deed: Recording, Fees and When It Works','Indiana Quitclaim Deed: Recording and Fees','Indiana quitclaim deed: how it works, recording and transfer tax rules. Official sources only.','indiana quitclaim deed','A Indiana deed is recorded with the county office named in the sources below.',F(['quitclaim-deed', 'deeds-recording:3']),[('Where do I record a deed in Indiana?','With the county recording office where the property is located.')],'Indiana Quitclaim Deed: Recording and Fees',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-transfer-on-death-deed','Indiana Transfer on Death Deed: How It Works','Indiana Transfer on Death Deed Explained','Indiana transfer on death deed: what official sources say and what we could not confirm.','indiana transfer on death deed','This guide covers what official sources say about Indiana transfer on death deeds.',F(['transfer-on-death-deed', 'probate-and-inherited-property:3']),[('What is a transfer on death deed?','A recorded deed that names who receives the property when the owner dies. Confirm the Indiana rules with an attorney.')],'Indiana Transfer on Death Deed Explained',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-tax-lien','Indiana Tax Liens and Delinquent Property Tax','Indiana Tax Liens and Delinquent Tax','Indiana delinquent property tax: tax liens, redemption and what to do before a tax sale. Official sources only.','indiana tax lien','Indiana counties pursue delinquent property tax through liens and tax sales.',F(['tax-liens', 'tax-sales']),[('Can I stop a tax sale?','Paying the delinquent amount or selling before the sale can pay the tax from the proceeds. Ask the county for exact figures.')],'Indiana Tax Liens and Delinquent Tax',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-capital-gains-tax','Indiana Capital Gains Tax When You Sell a House','Indiana Capital Gains Tax on a House Sale','Indiana income tax treatment when you sell a house: what we could confirm on official pages.','indiana capital gains tax','This guide covers what official sources say about Indiana tax on a house sale.',F(['capital-gains']),[('Does Indiana tax capital gains?','See the official sources above. Federal rules are outside this guide.')],'Indiana Capital Gains Tax on a House Sale',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-tax-sale','Indiana Tax Sales: Redemption and Selling Before the Sale','Indiana Tax Sales and Redemption','Indiana tax sales: how they work, redemption and selling a house with delinquent tax. Official sources only.','indiana tax sale','Indiana counties hold tax sales of delinquent property.',F(['tax-sales', 'tax-liens']),[('Can I redeem after a tax sale?','See the redemption rules above and confirm exact amounts with your county.')],'Indiana Tax Sales and Redemption',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-sheriff-sale','Indiana Sheriff Sales: Foreclosure Sale Steps and Redemption','Indiana Sheriff Sale Explained','Indiana sheriff sale: how a foreclosure sale works and what you can do first. Official sources only.','indiana sheriff sale','This guide covers Indiana foreclosure sales according to official sources.',F(['sheriff-sale', 'foreclosure']),[('Can I sell my house before a sheriff sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask for a payoff figure.')],'Indiana Sheriff Sale Explained',['Details we could not confirm on an official page are not stated.'])
    sp('indiana-land-contract','Indiana Land Contracts and Contracts for Deed: Seller Rules','Indiana Land Contracts: Seller Rules','Indiana land contracts and contracts for deed: what sellers should know. Official sources only.','indiana land contract','Indiana land contracts have rules set by statute, summarized below.',F(['land-contracts']),[('What is a land contract?','A contract where the buyer pays over time while the seller keeps title until a set point.')],'Indiana Land Contracts: Seller Rules',['Details we could not confirm on an official page are not stated.'])
    return P
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-in"; cty=d['county']+' County'; kind=d.get('type','place')
    body=(f"<p><strong>Selling a house in {esc(c)}, Indiana comes down to listing it, selling it yourself or taking a cash offer.</strong> Each route has different costs and timelines under Indiana law. The Census Bureau estimates {n(d['pop'])} residents in {esc(c)} as of July 1, 2025. We did not use listing-site price data.</p><h2>{esc(c)} at a glance</h2>"+ul([f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."])
     +f"<h2>Three ways to sell a house in {esc(c)}</h2><p><strong>List with an agent.</strong> The commission is whatever your listing agreement says. You also pay for repairs, showings and closing costs.</p><p><strong>Sell it yourself.</strong> A seller handling the sale directly still needs a deed, a closing agent and to account for any transfer tax. See "+a('indiana-property-tax-guide','the Indiana property tax guide: appeals')+". See "+a('indiana-closing-costs','Indiana closing costs')+".</p><p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {esc(c)} houses</h2><p><strong>Behind on the mortgage.</strong> We can often close before a foreclosure sale and pay the lender from the proceeds. See "+a('indiana-sheriff-sale','the Indiana sheriff sale guide')+".</p><p><strong>Inherited house.</strong> We buy houses that are still in probate or newly inherited.</p><p><strong>Unpaid property tax.</strong> The closing agent pays unpaid tax from the proceeds. See "+a('indiana-property-tax-guide','the Indiana property tax guide')+(f" and {a(ns(c)+'-in-property-tax-guide',esc(c)+' property tax')}" if c in PTCOK else '')+".</p>"
     +f"<h2>How to sell a house in {esc(c)}</h2>"+HOW())
    faqs=[(f"Can I sell my {c} house as-is?","Yes. A cash buyer purchases as-is, and you do not have to make repairs."),("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),(f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing.")]
    h1=f"Sell My House Fast in {c}, IN: Options, Costs and Cash Offers"; rt=f"Sell My House Fast in {c}, IN | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, IN"
    rd=f"Sell your {c}, IN house: list, sell yourself or take a cash offer. Indiana foreclosure, probate and tax rules. No commission, no fees."
    if len(rd)>155: rd=f"Sell your {c}, IN house: list it, sell it yourself or take a cash offer. Indiana foreclosure and tax rules. No commission."
    return mk(slug,h1,rt,rd,f"sell my house {c.lower()}",f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer.",body,faqs,f"Selling a house in {c}",SP,SRC+[('Census Bureau population estimates',d['pop_source_url'])])
def pre(t): return re.sub(r'^(Opened[^:]{0,30}:)\s*','',clean_txt(t))
def nm_(x): return clean_txt(re.sub(r'\(.*?\)','',x['name'])).split(';')[0].split(',')[0].strip()
PTC=["Indianapolis", "Fort Wayne"]
PTCOK=[c for c in PTC if c in CP and CP[c].get('assessor',{}).get('url') and CP[c].get('collector',{}).get('url')]
def ptax(c,v):
    slug=f"{ns(c)}-in-property-tax-guide"; ap,co=v['assessor'],v['collector']
    sec_=f"<h2>Who bills what in {esc(c)}</h2>"+ul([f"{L(ap['url'],nm_(ap))} handles assessment.",f"{L(co['url'],nm_(co))} bills and collects the tax."])
    dd=v.get('due_dates') or {}
    sec_+="<h2>Due dates</h2>"+(f"<p>{esc(pre(dd['text']))[:500]}. See the {L(dd['url'],'official page')}.</p>" if dd.get('opened') and dd.get('text') else f"<p>We could not confirm {esc(c)} due dates on an opened official page.</p>")
    g=v.get('grievance_appeal') or v.get('grievance') or {}
    sec_+="<h2>Challenging your assessment</h2>"+(f"<p>{esc(pre(g['text']))[:500]}. See the {L(g.get('filing_page_url') or g['url'],'official page')}.</p>" if g.get('opened') and g.get('text') else "<p>Owners can appeal to the county property tax assessment board of appeals, generally by June 15 or within the window on the notice. Confirm with your county. Confirm with your county.</p>")
    r=v.get('rate')
    sec_+="<h2>Tax rate</h2>"+(f"<p>The official page we opened lists {esc(clean_txt(str((r.get('value') or r.get('text')))))}. See the {L(r['url'],'official page')}.</p>" if isinstance(r,dict) and r.get('opened') else f"<p>We could not confirm the current {esc(c)} rate on an opened page, so we do not state one.</p>")
    notes=[clean_txt(x) for x in v.get('notes',[]) if not BAD.search(x) and len(x)<220][:3]
    if notes: sec_+="<h2>Local notes</h2>"+ul([esc(x) for x in notes])
    faqs=[(f"When are {c} property taxes due?","See the due dates section above and confirm with the collector."),(f"What happens to unpaid {c} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><strong>{esc(c)} property tax is billed by the offices named below.</strong> This guide points to them and explains what happens to unpaid tax when you sell.</p>"+sec_+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")+f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+HOW())
    h1=f"{c}, IN Property Tax Guide: Offices, Dates and Selling With Tax Due"
    return mk(slug,h1,f"{c}, IN Property Tax Guide",f"{c}, IN property tax: assessor and collector offices, due dates, appeals and what happens to unpaid tax when you sell.",f"{c.lower()} property tax",f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds.",body,faqs,f"{c} property tax guide",[SP[3],(f"sell-my-house-fast-{ns(c)}-in",f"Sell my house in {c}",'Options and cash offers.'),SP[0],SP[1]],[(nm_(ap),ap['url']),(nm_(co),co['url'])]+SRC[:2])
CNT=json.load(open(H+'in_cty_list.json'))['ptax']
REC=json.load(open(H+'in_cty_list.json'))['rec']
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
        elif not re.search(r'deeds\.com|facebook|twitter|zillow|redfin|justia',x.get('url') or '',re.I) and x.get('url','').startswith('http'): ex.append(clean_txt(x['claim'])+' (from the county site listing; confirm with the office)')
    return (out+ex)[:4]
def county(cn,v,kind):
    v=clean_urls(v); nm=cn+' County'; ap,co,rc=v.get('assessor',{}),v.get('collector',{}),v.get('recorder',{})
    unc=[clean_txt(x) for x in v.get('unconfirmed',[]) if 25<len(x)<200 and not BAD.search(x)][:3]
    ap_dl=[clean_txt(x['claim']) for x in (v.get('appeal_deadline') or []) if isinstance(x,dict) and x.get('opened')][:2]
    if kind=='tax':
        slug=f"{ns(cn)}-county-in-property-tax-guide"; bill=[]
        if co.get('url'): bill.append(f"{L(co['url'],nm_(co))} bills and collects the tax and handles delinquent tax.")
        if ap.get('url'): bill.append(f"{L(ap['url'],nm_(ap))} handles assessment and appeals.")
        s=f"<h2>Who to contact in {esc(nm)}</h2>"+(ul(bill) if bill else "<p>We could not confirm the county offices on an opened page.</p>")
        op=cf(v,'assessor')+cf(v,'collector')+ap_dl
        if op: s+="<h2>What we confirmed on official pages</h2>"+ul([esc(x) for x in op[:6]])
        s+="<h2>Assessment appeals</h2><p>Owners can appeal to the county property tax assessment board of appeals, generally by June 15 or within the window on the notice. Confirm with your county. See the "+a('indiana-property-tax-guide','Indiana property tax guide')+".</p><h2>Tax rate</h2><p>We could not confirm a current county rate on an opened official page. Indiana bills combine county, municipal and school district levies.</p>"
        h1=f"{nm}, IN Property Tax Guide: Offices, Appeals and Selling With Tax Due"; rt=f"{nm}, IN Property Tax Guide"
        rd=f"{nm}, IN property tax: county offices, assessment appeals, county treasurer and what happens to unpaid tax when you sell."
        lead=f"{esc(nm)}, Indiana property tax involves the county assessment office and the county treasurer."; fk=f"{cn.lower()} county property tax"; crumb=f"{nm} property tax guide"
        faqs=[(f"Who handles assessment appeals in {nm}?","Appeals go to the county property tax assessment board of appeals. Confirm your deadline with the county."),(f"What happens to unpaid {nm} property tax when I sell?","The title company pays unpaid tax from the sale proceeds at closing.")]
    else:
        slug=f"{ns(cn)}-county-in-county-recorder"; s=f"<h2>Who records deeds in {esc(nm)}</h2>"+(ul([f"{L(rc['url'],nm_(rc))} records deeds and mortgages."]) if rc.get('url') else "<p>We could not confirm the county recorder's page.</p>")
        op=cf(v,'recorder')
        if op: s+="<h2>What we confirmed on the official page</h2>"+ul([esc(x) for x in op])
        s+="<h2>Recording and transfer tax</h2>"+ul(facts('property-transfer-tax')[:3]+facts('deeds-recording')[:2])+"<h2>Fees</h2><p>County recording fees change, so we do not quote a total. Check the recorder's current fee schedule before you file.</p>"
        h1=f"{nm}, IN County Recorder: Recording a Deed, Fees and Transfer Tax"; rt=f"{nm}, IN County Recorder Guide"
        rd=f"{nm}, IN county recorder: where to record a deed, real estate transfer tax, and fee schedule notes. Official sources."
        lead=f"The {esc(nm)} county recorder records Indiana deeds and mortgages."; fk=f"{cn.lower()} county county recorder"; crumb=f"{nm} county recorder"
        faqs=[(f"Where do I record a deed in {nm}?","With the County Recorder. Confirm submission rules on the county page."),("Do I owe real estate transfer tax?","Real estate transfer tax can apply to deeds. The Department of Revenue explains the rule.")]
    body=(f"<p><strong>{lead}</strong> This guide lists what we confirmed on official pages.</p>"+s+cta(f"Selling in {nm}?",f"We buy {nm} houses as-is, with no commission, no repairs and no closing costs to you.")+(UNC(unc) if unc else '')+f"<h2>How to sell a house in {esc(nm)}</h2>"+HOW())
    srcs=([(nm_(co if kind=='tax' else rc),(co if kind=='tax' else rc)['url'])] if (co if kind=='tax' else rc).get('url') else [])+SRC[:2]
    return mk(slug,h1,rt,rd,fk,f"Selling in {nm}? Get a Cash Offer",f"We buy {nm} houses as-is and reply with a written cash offer.",body,faqs,crumb,SP,srcs)
if __name__=='__main__':
    seen=set(); cities=[]
    for d in CITIES:
        k=ns(d['city'])
        if k in seen: continue
        seen.add(k); cities.append(d)
    os.makedirs(R+'/pages/in',exist_ok=True)
    def dump(name,out,label): json.dump(out,open(R+f'/pages/in/{name}.json','w')); print(label,len(out),min(map(wc,out)) if out else 0)
    dump('indiana-state-pages-1',state_pages(),'state')
    dump('indiana-city-pages-1',[city_page(d['city'],d) for d in cities],'city')
    dump('indiana-city-ptax-1',[ptax(c,CP[c]) for c in PTCOK],'ptax')
    dump('indiana-county-ptax-1',[county(c,CT[c],'tax') for c in CNT if c in CT],'county tax')
    dump('indiana-county-records-1',[county(c,CT[c],'rec') for c in REC if c in CT and CT[c].get('recorder',{}).get('url')],'records')
