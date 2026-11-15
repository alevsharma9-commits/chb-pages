import json,sys,os,re,glob
sys.path.insert(0,os.path.dirname(__file__))
from common import *
from fl_city import ns,CD
R=os.path.join(os.path.dirname(__file__),'..')
FSH=json.load(open('/home/claude/chb/fl_fact_sheet.json'))['topics']['florida-property-records']['facts']
PTAX_IDX=json.load(open(R+'/data/fl/county_sets.json')) if os.path.exists(R+'/data/fl/county_sets.json') else {}
BAD=re.compile(r'search excerpt|not opened|http|phone|amendment|ballot|fraud|not verified|not confirmed|not stated',re.I)
def D():
    d={}
    for f in sorted(glob.glob('/home/claude/chb/fl_cty_*.json')): d.update(json.load(open(f)))
    return d
def ok(facts): return [clean_txt(f['text']) for f in facts if f.get('opened') and not BAD.search(f['text']) and len(f['text'])<380][:5]
def link(u,t): return f"<a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>{esc(t)}</a>"
def cities_in(county):
    return [(c,d) for c,d in CD.items() if county+' County' in d['counties']]
def tax_page(co,v):
    cn=co; slug=f"{ns(co)}-county-fl-property-tax-guide"; ap,tc,cl,m=v['appraiser'],v['collector'],v['clerk'],v['millage']
    bill=[link(ap['url'],ap['name'])+" sets the assessed value and handles exemptions such as homestead.",link(tc['url'],tc['name'])+" sends the bill and collects the tax."]
    if cl.get('records_url'): bill.append("The clerk's "+link(cl['records_url'],'Official Records search')+" shows recorded deeds, liens and mortgages.")
    cf=ok(tc['facts']); af=ok(ap['facts'])
    sec=f"<h2>Who bills what in {esc(cn)} County</h2>"+ul(bill)
    sec+="<h2>Due dates and discounts</h2><p>Florida taxes are due November 1, or when the certified roll reaches the tax collector, and become delinquent April 1. Early payment discounts run 4 percent in November, 3 percent in December, 2 percent in January and 1 percent in February (Fla. Stat. 197.162 and 197.333). Real property is assessed as of January 1."+(" What the county tax collector's pages state:</p>"+ul([esc(x) for x in cf]) if cf else "</p>")
    if af: sec+="<h2>Homestead and exemptions</h2><p>Homestead applications go to the county property appraiser by March 1 (Fla. Stat. 196.011). What the appraiser's pages state:</p>"+ul([esc(x) for x in af])
    if m.get('rate') and m.get('opened'):
        sec+=f"<h2>County millage rate</h2><p>An official page we opened lists the {esc(cn)} County government millage as {m['rate']} mills for {m['year']}. That is one taxing authority's rate. Your bill adds the school district, cities and special districts, so it is not your total. A mill is $1 of tax per $1,000 of taxable value. See the <a href='{m['url']}' target='_blank' rel='noreferrer noopener nofollow'>official page</a> and use the parcel lookup for your bill.</p>"
    else:
        sec+=f"<h2>County millage rate</h2><p>We could not confirm the current {esc(cn)} County millage rate on an opened official page, so we do not state one. Use the property appraiser's millage chart and the parcel lookup for your bill.</p>"
    cs=cities_in(cn)
    if cs:
        sec+=f"<h2>Selling in {esc(cn)} County cities</h2>"+ul([a(f"sell-my-house-fast-{ns(c)}-fl",f"Selling a house in {esc(c)}") for c,_ in cs])
    unc=sorted([clean_txt(x) for x in v['unconfirmed'] if len(x)<260],key=len)[:3]
    faqs=[(f"When are property taxes due in {cn} County, FL?","Florida taxes are due November 1 or when the certified roll reaches the tax collector, and become delinquent April 1 (Fla. Stat. 197.333)."),("What early payment discounts apply?","The statute provides 4 percent in November, 3 percent in December, 2 percent in January and 1 percent in February (Fla. Stat. 197.162). Check the tax collector's page for this year's exact dates."),("When is the homestead exemption deadline?","March 1 each year with the county property appraiser (Fla. Stat. 196.011)."),(f"What happens to unpaid {cn} County property tax when I sell?","The title company pays the unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><em>Last updated {DATE}. Citations come from the Florida statutes and the official county pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"
      f"<p><strong>{esc(cn)} County property tax is billed by the county tax collector, and Florida bills are due November 1 and delinquent April 1.</strong> This guide points you to the official {esc(cn)} County offices and explains what happens to the tax when you sell a house there.</p>"
      +sec+cta(f"Behind on {cn} County property tax?",f"We buy {cn} County houses as-is, and the title company pays unpaid tax from the proceeds.")
      +(f"<h2>What we could not confirm</h2>"+ul([esc(x) for x in unc]) if unc else '')
      +f"<h2>How to sell a house in {esc(cn)} County when you owe property tax</h2>"+ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded document that shows who owns it today.","Ask the tax collector for the amount due in the month you expect to close. Unpaid tax is paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.","If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is. See "+a('we-buy-houses-in-florida','we buy houses in Florida')+"."])
      +f"<h2>{esc(cn)} County property tax FAQ</h2>"+faq_html(faqs)
      +related('Florida',[('we-buy-houses-in-florida','We buy houses in Florida','How a cash offer works.'),('florida-property-tax-guide','Florida property tax guide','Dates, discounts and caps.'),('florida-homestead-exemption','Florida homestead exemption','Amounts and the March 1 deadline.'),('florida-tax-deed-sales','Florida tax deed sales','Certificates and redemption.'),('florida-property-tax-appeal','Florida property tax appeal','VAB deadlines.')])
      +sources([(ap['name'],ap['url']),(tc['name'],tc['url'])]+([('Official millage page',m['url'])] if m.get('rate') and m.get('opened') else [])+[("Florida Statutes, Chapter 197","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/0197.html")])
      +DISCLAIM('Florida','tax professional')+schema(faqs,[('Home',SITE),('Florida',SITE+'we-buy-houses-in-florida/'),(f"{cn} County property tax guide",SITE+slug+'/')]))
    h1=f"{cn} County, FL Property Tax Guide: Offices, Dates and Selling With Tax Due"
    rt=f"{cn} County, FL Property Tax Guide"
    rd=f"{cn} County, FL property tax: appraiser and tax collector offices, Nov 1 due date, discounts, April 1 delinquency and selling with tax due."
    if len(rd)>155: rd=f"{cn} County, FL property tax: offices, Nov 1 due date, discounts, April 1 delinquency and selling with tax due."
    return wrap(slug,h1,hero('Florida',h1,f"Owe {cn} County Property Tax? Get a Cash Offer",f"We buy {cn} County houses as-is. The title company pays unpaid tax from the proceeds."),body,rt,rd,f"{cn.lower()} county property tax")
def rec_page(co,v):
    cn=co; slug=f"{ns(co)}-county-fl-property-records"; cl=v['clerk']
    fee=ok(cl['facts'])
    stat=[esc(clean_txt(FSH[i]['text']))+' ('+esc(clean_txt(FSH[i]['cite']))+').' for i in (0,3,4,7)]
    sec=f"<h2>Where to search {esc(cn)} County records</h2>"+ul([link(cl['url'],cl['name'])+" is the county recorder."]+([ "Search deeds, mortgages, liens and other instruments in the "+link(cl['records_url'],'Official Records search')+"."] if cl.get('records_url') else [])+([ "Recording fees are on the clerk's "+link(cl['fee_url'],'fee page')+"."] if cl.get('fee_url') else []))
    if fee: sec+=f"<h2>What the {esc(cn)} County clerk's pages state</h2>"+ul([esc(x) for x in fee])
    sec+="<h2>What Florida law says about recording</h2>"+ul(stat)
    unc=sorted([clean_txt(x) for x in v['unconfirmed'] if len(x)<260],key=len)[:3]
    faqs=[(f"Who records deeds in {cn} County, FL?","The clerk of the circuit court is the recorder and keeps the Official Records (Fla. Stat. 28.222)."),("Are Official Records public?","Yes. Instruments recorded in the Official Records stay open to public inspection and copying."),("What is the statewide recording fee?","For an instrument up to 14 by 8.5 inches the statute lists $5.00 for the first page and $4.00 for each additional page, plus other charges (Fla. Stat. 28.24). Check the clerk's fee page for the current total.")]
    body=(f"<p><em>Last updated {DATE}. Citations come from the Florida statutes and the official {esc(cn)} County pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"
      f"<p><strong>In {esc(cn)} County the clerk of the circuit court is the recorder, and deeds, mortgages and liens are kept in the Official Records.</strong> This guide shows where to search them and what Florida law says about recording.</p>"
      +sec+cta(f"Need to sell a {cn} County house?",f"We buy {cn} County houses as-is. A title company searches the records at closing.")
      +(f"<h2>What we could not confirm</h2>"+ul([esc(x) for x in unc]) if unc else '')
      +f"<h2>{esc(cn)} County property records FAQ</h2>"+faq_html(faqs)
      +related('Florida',[('we-buy-houses-in-florida','We buy houses in Florida','How a cash offer works.'),(f"{ns(co)}-county-fl-property-tax-guide",f"{cn} County property tax guide",'Offices and dates.'),('florida-property-records','Florida property records','Statewide recording rules.'),('florida-warranty-deed','Florida warranty deed','Signing and recording.'),('florida-mechanics-lien-home','Florida mechanic\'s lien','Lien deadlines.')])
      +sources([(cl['name'],cl['url'])]+([('Official Records search',cl['records_url'])] if cl.get('records_url') else [])+[("Florida Statutes, Chapter 28 (Clerks of the circuit court)","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0028/0028.html")])
      +DISCLAIM('Florida','attorney')+schema(faqs,[('Home',SITE),('Florida',SITE+'we-buy-houses-in-florida/'),(f"{cn} County property records",SITE+slug+'/')]))
    h1=f"{cn} County, FL Property Records: Official Records Search, Fees and Recording Rules"
    rt=f"{cn} County, FL Property Records Guide"
    rd=f"{cn} County, FL property records: where to search deeds, mortgages and liens, recording fees and what Florida law says about recording."
    return wrap(slug,h1,hero('Florida',h1,f"Selling a {cn} County House? Get a Cash Offer",f"We buy {cn} County houses as-is. Tell us about the property."),body,rt,rd,f"{cn.lower()} county property records")
RECS="Pinellas Miami-Dade Pasco Manatee Seminole Broward Hillsborough St. Lucie Palm Beach Orange Duval Polk Volusia Sarasota St. Johns Lee Collier Marion Brevard Lake Osceola Escambia".split()
if __name__=='__main__':
    d=D(); out=[];rec=[]
    for co,v in d.items():
        cn=co.replace(' County','')
        out.append(tax_page(cn,v))
        if cn in RECS: rec.append(rec_page(cn,v))
    json.dump(out,open(R+'/pages/fl/florida-county-ptax-1.json','w')); json.dump(rec,open(R+'/pages/fl/florida-county-records-1.json','w'))
    print(len(out),len(rec),[ (i['slug'],wc(i)) for i in out[:3]])
