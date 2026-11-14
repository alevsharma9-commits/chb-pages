import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
from fl_city import ns,n,CD
R=os.path.join(os.path.dirname(__file__),'..')
D=json.load(open('/home/claude/chb/fl_city_ptax.json'))
EXCERPT={'Jacksonville','Orlando','Tallahassee','Fort Lauderdale','Gainesville','Ocala'}
BAD=re.compile(r'search excerpt|link seen|not opened|page not opened|excerpt|http|phone|amendment|ballot|fraud|not verified|not confirmed|not stated|not opened',re.I)
def good(notes): return [clean_txt(x) for x in notes if not BAD.search(x) and len(x)<420 and '—' not in x][:5]
def page(c,v):
    slug=f"{ns(c)}-fl-property-tax-guide"; cty=v['county']+' County'
    ap,co,m=v['appraiser'],v['collector'],v['millage']
    bill=[f"<a href='{ap['url']}' target='_blank' rel='noreferrer noopener nofollow'>{esc(ap['name'])}</a> sets the assessed value and handles exemptions such as homestead.",f"<a href='{co['url']}' target='_blank' rel='noreferrer noopener nofollow'>{esc(co['name'])}</a> sends the bill and collects the tax."]
    if v['clerk_records_url']: bill.append(f"The clerk's <a href='{v['clerk_records_url']}' target='_blank' rel='noreferrer noopener nofollow'>Official Records search</a> shows recorded deeds, liens and mortgages.")
    mill=''
    if m.get('rate') and c not in EXCERPT:
        mill=(f"<h2>The city millage rate</h2><p>The official page we opened lists the {esc(c)} millage rate as {m['rate']} mills for {m['year']}. That is the city's own rate. Your bill also includes the county, the school district and other taxing authorities, so it is not your total rate. A mill is $1 of tax per $1,000 of taxable value. Read the full chart on the <a href='{m['url']}' target='_blank' rel='noreferrer noopener nofollow'>official page</a> and use the tax collector's parcel lookup for your actual bill.</p>")
    else:
        mill=f"<h2>The city millage rate</h2><p>We could not confirm the current {esc(c)} millage rate on an opened official page, so we do not state one. Use the property appraiser's millage chart and the tax collector's parcel lookup for your bill.</p>"
    sec=f"<h2>Who bills what in {esc(c)}</h2><p>{esc(c)} is in {esc(cty)}.</p>"+ul(bill)
    cn=good(co['notes']); an=good(ap['notes'])
    sec+="<h2>Due dates and discounts</h2><p>Florida taxes are due November 1, or when the certified roll reaches the tax collector, and become delinquent April 1. Early payment discounts run 4 percent in November, 3 percent in December, 2 percent in January and 1 percent in February (Fla. Stat. 197.162 and 197.333). Real property is assessed as of January 1."+(" Local notes from the county offices:</p>"+ul([esc(x) for x in cn]) if cn else "</p>")
    nt=[esc(clean_txt(x)) for x in v['notable'] if not BAD.search(x)][:3]
    if an or nt: sec+="<h2>Homestead and local notes</h2>"+(ul([esc(x) for x in an]) if an else '')+(ul(nt) if nt else '')
    sec+=mill
    unc=[clean_txt(x) for x in v['unconfirmed'] if len(x)<260][:3]
    sell=ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded document that shows who owns it today.","Ask the tax collector for the amount due in the month you expect to close. Unpaid tax is paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.","If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is. See "+a(f"sell-my-house-fast-{ns(c)}-fl",f"selling a house in {esc(c)}")+" and "+a('we-buy-houses-in-florida','we buy houses in Florida')+"."])
    faqs=[(f"When are property taxes due in {c}, FL?","Florida taxes are due November 1 or when the certified roll reaches the tax collector, and become delinquent April 1 (Fla. Stat. 197.333)."),
      (f"What discounts apply in {cty}?","The statute provides 4 percent in November, 3 percent in December, 2 percent in January and 1 percent in February (Fla. Stat. 197.162). Check the tax collector's page for the exact dates in the current year."),
      ("When is the homestead exemption deadline?","March 1 each year with the county property appraiser (Fla. Stat. 196.011)."),
      (f"What happens to unpaid {c} property tax when I sell?","The title company pays the unpaid tax from the sale proceeds at closing.")]
    body=(f"<p><em>Last updated {DATE}. Citations come from the Florida statutes and the official county and city pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p>"
      f"<p><strong>{esc(c)} property tax is billed by the {esc(cty)} tax collector, and Florida bills are due November 1 and delinquent April 1.</strong> This guide points you to the official {esc(cty)} offices and explains what happens to the tax when you sell.</p>"
      +sec+cta(f"Behind on {c} property tax?",f"We buy {c} houses as-is, and the title company pays unpaid tax from the proceeds.")
      +(f"<h2>What we could not confirm</h2>"+ul([esc(x) for x in unc]) if unc else '')
      +f"<h2>How to sell a house in {esc(c)} when you owe property tax</h2>"+sell+f"<h2>{esc(c)} property tax FAQ</h2>"+faq_html(faqs)
      +related('Florida',[('we-buy-houses-in-florida','We buy houses in Florida','How a cash offer works.'),(f"sell-my-house-fast-{ns(c)}-fl",f"Sell my house in {c}",'Options, costs and cash offers.'),('florida-property-tax-guide','Florida property tax guide','Dates, discounts and caps.'),('florida-homestead-exemption','Florida homestead exemption','Amounts and the March 1 deadline.'),('florida-tax-deed-sales','Florida tax deed sales','Certificates and redemption.'),('florida-property-tax-appeal','Florida property tax appeal','VAB deadlines.')])
      +sources([(ap['name'],ap['url']),(co['name'],co['url'])]+([('Official millage page',m['url'])] if m.get('rate') and c not in EXCERPT else [])+[("Florida Statutes, Chapter 197","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/0197.html")])
      +DISCLAIM('Florida','tax professional')+schema(faqs,[('Home',SITE),('Florida',SITE+'we-buy-houses-in-florida/'),(f"{c} property tax guide",SITE+slug+'/')]))
    h1=f"{c}, FL Property Tax Guide: Offices, Dates and Selling With Tax Due"
    rt=f"{c}, FL Property Tax Guide: Dates and Discounts"
    if len(rt)>62: rt=f"{c}, FL Property Tax Guide"
    rd=f"{c}, FL property tax: the {cty} appraiser and tax collector, Nov 1 due date, discounts, April 1 delinquency, homestead and selling with tax due."
    if len(rd)>155: rd=f"{c}, FL property tax: {cty} offices, Nov 1 due date, discounts, April 1 delinquency, homestead and what happens when you sell."
    return wrap(slug,h1,hero('Florida',h1,f"Owe {c} Property Tax? Get a Cash Offer",f"We buy {c} houses as-is. The title company pays unpaid tax from the proceeds."),body,rt,rd,f"{c.lower()} property tax")
if __name__=='__main__':
    out=[page(c,v) for c,v in D.items()]
    for i in out: print(i['slug'],wc(i),len(i['rank_math_description']))
    json.dump(out,open(R+'/pages/fl/florida-city-ptax-1.json','w'))
