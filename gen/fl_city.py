import json,sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
from common import *
R=os.path.join(os.path.dirname(__file__),'..')
CD=json.load(open(R+'/data/fl/city_data.json'))
EXIST=set("""boca-raton boynton-beach brandon cape-coral clearwater coral-springs fort-lauderdale fort-myers gainesville hialeah hollywood jacksonville kissimmee largo miami miami-gardens naples orlando pembroke-pines pensacola pompano-beach port-st-lucie sanford sarasota st-petersburg tallahassee tampa west-palm-beach winter-park""".split())
def ns(c): return re.sub(r'[^a-z0-9]+','-',c.lower().replace('.','').replace("'",'')).strip('-')
def n(x): return f"{x:,}"
def city_page(c,d):
    slug=f"sell-my-house-fast-{ns(c)}-fl"
    cty=d['counties'][0] if len(d['counties'])==1 else ' and '.join(d['counties'])
    bul=[f"Estimated population, July 1, 2025: {n(d['pop'])} (Census Bureau)."]
    if d['value']: bul.append(f"Median value of owner-occupied homes: ${n(d['value'])} (American Community Survey, 2019-2023).")
    if d['own'] and d['rent_occ'] and d['occ']: bul.append(f"Owner-occupied homes: {n(d['own'])}. Renter-occupied homes: {n(d['rent_occ'])}, so about {round(100*d['own']/d['occ'])}% of occupied homes are owner-occupied.")
    if d['rent']: bul.append(f"Median gross rent: ${n(d['rent'])} a month.")
    if d['yb']: bul.append(f"Median year homes were built: {d['yb']}.")
    if d['vac'] is not None and d['units']: bul.append(f"Vacant housing units: {n(d['vac'])} of {n(d['units'])} total.")
    intro=f"{c} had an estimated {n(d['pop'])} residents in 2025"+(f", and the Census Bureau puts the median value of an owner-occupied home at ${n(d['value'])} in its 2019-2023 survey." if d['value'] else ".")+" We did not use listing-site price data."
    lead=f"<strong>Selling a house in {c}, Florida comes down to a choice between listing it, selling it yourself and taking a cash offer.</strong> Each route has different costs and timelines under Florida law, and this guide lays them out with official sources. {intro}"
    body=(f"<p><em>Last updated {DATE}. Citations come from the Florida statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we say so.</em></p><p>{lead}</p>"
     f"<h2>{c} housing at a glance</h2><p>These figures come from the Census Bureau. They describe the city as a whole, not your street or your house. {c} is in {esc(cty)}.</p>"+ul(bul)
     +f"<h2>Three ways to sell a house in {c}</h2><p><strong>List with an agent.</strong> We did not find a Florida statute that sets a commission rate, so the rate is whatever your listing agreement says. You also pick up closing costs, repairs and showings. See {a('florida-real-estate-commission','Florida real estate commission')} and {a('florida-closing-costs','closing costs')}.</p>"
     f"<p><strong>Sell it yourself.</strong> A Florida owner selling their own property is generally outside the broker licensing law. You still owe the buyer a flood disclosure at or before contract signing, a property tax disclosure summary and, for buildings, a radon notice. Details are in {a('for-sale-by-owner-florida','for sale by owner in Florida')} and {a('florida-real-estate-contract-inspection-period','Florida seller disclosures')}.</p>"
     "<p><strong>Take a cash offer.</strong> We buy houses as-is, with no agent commission, no fees and no closing costs charged to you. You choose the closing date, and the title company pays any mortgage and unpaid property tax from the proceeds.</p>"
     +cta(f"Selling in {c}?",f"We buy {c} houses as-is, with no commission, no repairs and no closing costs to you.")
     +f"<h2>Situations we see with {c} houses</h2>"
     f"<p><strong>Behind on the mortgage.</strong> Florida foreclosures go through court. After a final judgment, the court directs the clerk to hold a public sale on a set day, generally 20 to 35 days later, and the owner can redeem until the clerk files the certificate of sale (Fla. Stat. 45.031 and 45.0315). Read {a('florida-foreclosure-process','the Florida foreclosure process')} before you decide.</p>"
     f"<p><strong>Inherited house.</strong> Who can sell depends on whether there is a will and how the estate is administered. Florida homestead also has devise limits. See {a('florida-probate-process','probate')}, {a('florida-intestate-succession','intestate succession')}, {a('florida-lady-bird-deed','lady bird deeds')} and {a('florida-homestead-protection-selling','homestead protection')}.</p>"
     f"<p><strong>Unpaid property tax.</strong> Florida property tax is due November 1 and delinquent April 1. See {a('florida-property-tax-guide','the Florida property tax guide')} and {a('florida-tax-deed-sales','tax deed sales')}.</p>"
     f"<p><strong>Tenants or squatters.</strong> {a('florida-eviction-process','Eviction')}, {a('florida-landlord-tenant-selling-rented-house','selling a rented house')} and {a('florida-squatters-rights-adverse-possession','squatter')} cases follow different Florida rules. Condo and HOA sellers should read about {a('florida-condo-hoa-selling','estoppel certificates')}.</p>"
     f"<h2>Property tax when you sell in {c}</h2><p>Florida taxes are due November 1, or when the certified roll reaches the tax collector, and become delinquent April 1. Early payment discounts run 4 percent in November, 3 percent in December, 2 percent in January and 1 percent in February (Fla. Stat. 197.162 and 197.333). Real property is assessed as of January 1. We did not find an official source that gives one tax rate for all of {c}, so we do not state one. Ask the county tax collector for the amount due in the month you expect to close, and give that figure to the title company.</p>"
     f"<p>Homeowners must apply for the homestead exemption with the county property appraiser by March 1, and a change of ownership ends the Save Our Homes cap. See {a('florida-homestead-exemption','the homestead exemption')} and {a('florida-property-tax-appeal','property tax appeals')}.</p>"
     f"<h2>Taxes on the sale itself</h2><p>Florida does not impose a personal income tax, but federal capital gains rules can apply. The IRS lets you exclude up to $250,000 of gain on your main home, or $500,000 if married filing jointly, if you meet the ownership and use tests. Documentary stamp tax on a deed is 70 cents per $100 of consideration (Fla. Stat. 201.02). See {a('florida-capital-gains-tax-home-sale','capital gains on a home sale')}.</p>"
     f"<h2>How to sell a house in Florida when you are in {c}</h2>"+ol(["Find out what the title company needs. For an inherited or transferred house, that usually means the recorded document that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.","If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See how "+a('we-buy-houses-in-florida','we buy houses in Florida')+"."]))
    faqs=[(f"Can I sell my {c} house as-is?","Yes. Florida law does not require a seller to make repairs before listing, though you must give the required disclosures. A cash buyer purchases as-is."),
      (f"How much is a house worth in {c}?",(f"The Census Bureau's 2019-2023 survey puts the median value of owner-occupied homes in {c} at ${n(d['value'])}. " if d['value'] else "")+"Your house will differ, so get a written offer or an appraisal."),
      ("Do I pay a commission to sell for cash to you?","No. Our offers carry no agent commission, fees or closing costs to you."),
      (f"Can I sell a {c} house with a mortgage or unpaid taxes?","Yes. The title company pays the mortgage payoff and any unpaid property tax from the proceeds at closing."),
      ("Does Florida have a state income tax?","No. The Florida Department of Revenue says Florida does not impose a personal income tax. Federal tax rules can still apply to your gain.")]
    cards=[('we-buy-houses-in-florida','We buy houses in Florida','How a cash offer works for Florida sellers.')]
    if ns(c) in EXIST: cards.append((f"we-buy-houses-in-{ns(c)}-fl",f"We buy houses in {c}, FL",f"Our {c} cash offer page."))
    cards+=[('florida-foreclosure-process','Florida foreclosure process','Sale dates and redemption.'),('florida-probate-process','Florida probate process','Selling an inherited home.'),('florida-property-tax-guide','Florida property tax guide','Dates, discounts and caps.'),('florida-closing-costs','Florida closing costs','What a sale costs.')]
    srcs=[("Florida Statutes, Chapter 45 (Foreclosure sales)","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0000-0099/0045/0045.html"),("Florida Statutes, Chapter 197 (Tax collection)","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0100-0199/0197/0197.html"),("Florida Statutes, Chapter 201 (Excise tax on documents)","https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0200-0299/0201/0201.html"),("Florida Department of Revenue: Florida FAQ on personal income tax","https://floridarevenue.com/faq/Pages/FAQDetails.aspx?FAQID=1466"),("IRS Publication 523: Selling Your Home","https://www.irs.gov/publications/p523"),("Census Bureau: Population estimates and American Community Survey","https://www.census.gov/data.html")]
    body+=f"<h2>Selling a house in {c} FAQ</h2>"+faq_html(faqs)+related('Florida',cards)+sources(srcs)+DISCLAIM('Florida','attorney or tax professional')+schema(faqs,[('Home',SITE),('Florida',SITE+'we-buy-houses-in-florida/'),(f"Sell my house {c}",SITE+slug+'/')])
    h1=f"Sell My House Fast in {c}, FL: Options, Costs and Cash Offers"
    rt=f"Sell My House Fast in {c}, FL | Cash Offer"
    if len(rt)>62: rt=f"Sell My House Fast in {c}, FL"
    rd=f"Sell your {c}, FL house: list, sell yourself or take a cash offer. Florida rules on foreclosure, probate and tax, plus Census housing data. No commission"
    if len(rd)>155: rd=f"Sell your {c}, FL house: list, sell yourself or take a cash offer. Florida foreclosure, probate and tax rules plus Census data. No commission"
    if len(rd)>155: rd=f"Sell your {c}, FL house: list, sell yourself or take a cash offer. Florida foreclosure, probate and tax rules. No commission"
    return wrap(slug,h1,hero('Florida',h1,f"Sell Your {c} House for Cash",f"Tell us about your {c} house. We buy as-is and reply with a written cash offer."),body,rt,rd,f"sell my house {c.lower()}")
if __name__=='__main__':
    out=[city_page(c,d) for c,d in CD.items()]
    for it in out[:3]: print(it['slug'],wc(it),it['rank_math_title'],len(it['rank_math_description']))
    print(len(out),min(wc(i) for i in out),max(wc(i) for i in out),len({i['slug'] for i in out}))
    json.dump(out,open(R+'/pages/fl/florida-city-pages-1.json','w'))
