import json,re,os,sys,glob
sys.path.insert(0,os.path.dirname(__file__))
from common import *
H='/home/claude/chb/'; R=os.path.join(os.path.dirname(__file__),'..')
N=json.load(open(H+'state_names.json'))
VOL={"sq":"al az ar co ct de fl ga id il in ia ks ky la me md ma mi mn ms mo mt ne nv nj nm ny nc nd oh ok or pa sc tn tx ut vt va wa wv wi wy","ev":"al az ar co fl ga il in ia ks ky la md ma mi mn ms mo ne nh nj ny nc oh ok or pa sc tn tx ut va wa wv wi","pr":"al az ar co fl ga id il in ia ks ky la md ma mi mn mo mt nv nj nm ny nc oh ok or pa sc tn tx ut va wa wi","tx":"al az ar co ct fl ga il in ia md mi ms nj nm ny nc oh pa tn tx ut va","lt":"al az ar co ct de fl ga id il in ia ks ky la me md ma mi mn ms mo mt ne nv nh nj nm ny nc nd oh ok or pa sc sd tn tx ut vt va wa wv wi"}
VOL={k:v.split() for k,v in VOL.items()}
# key: (vol, fact topic, slug suffix, h1, rm title, desc, focus kw, lead, existing-slug regex that means "already covered", faqs)
T={
 'sq':('squatters-adverse-possession','squatters-rights-adverse-possession','{ST} Squatters Rights and Adverse Possession: What Owners Should Know','{ST} Squatters Rights and Adverse Possession','{ST} squatters rights and adverse possession: what the statutes say and how owners remove occupants or sell. Official sources.','{st} squatters rights','{ST} law sets out when a person occupying land can claim title by adverse possession, and how an owner can remove someone who has no right to be there.',r'squatters|adverse-possession',
   [('Can a squatter take ownership of my {ST} house?','Only by meeting every requirement of the adverse possession statute cited above for the full period. Check the statute and talk to a {ST} attorney about your facts.'),('Can I sell a house that has squatters in it?','Yes. We buy houses as-is, including occupied ones. Tell us who is in the property when you request an offer.'),('Should I remove a squatter myself?','No. Use the legal process described in the official sources above. Self-help removal can create liability for the owner.')]),
 'lt':('landlord-tenant','landlord-tenant-law-tenant-rights','{ST} Landlord Tenant Law and Tenant Rights: Rules for Selling a Rental','{ST} Landlord Tenant Law and Tenant Rights','{ST} landlord tenant law and tenant rights: deposits, notices, entry and selling a rented house. Official sources only.','{st} tenant rights','{ST} statutes set the basic rules between landlords and tenants, including deposits, notices and what happens when a rental is sold.',r'landlord-tenant|tenant-rights',
   [('Can I sell my {ST} rental with a tenant living in it?','Yes. A rental can be sold occupied. What happens to the lease depends on its terms and the statutes cited above.'),('Do I have to return the security deposit when I sell?','The deposit rules in the sources above still apply. Ask the title company how the deposit will be transferred or credited at closing.'),('Will you buy a house with tenants who are behind on rent?','Yes. We buy rentals as-is, occupied or vacant. Tell us about the lease and payment history when you request an offer.')]),
 'ev':('eviction-notices','eviction-notice','{ST} Eviction Notice Rules: Notice Types, Days and Selling the House','{ST} Eviction Notice: Types and Days','{ST} eviction notice rules: notice types, required days, which court hears the case and selling a rental. Official sources.','{st} eviction notice','{ST} law requires a landlord to give a specific written notice before filing an eviction, and the number of days depends on the reason.',r'eviction-notice',
   [('How many days notice does a {ST} landlord have to give?','It depends on the reason for the eviction. See the notice periods and statute sections cited above.'),('Can I sell the house during an eviction?','Yes. A buyer can take the property with the case pending. Tell us where the case stands when you request an offer.'),('Can a landlord change the locks without a court order?','Follow the court process in the official sources above. Removal is carried out by the officer named in the statute, not by the landlord.')]),
 'pr':('probate-laws','probate-laws','{ST} Probate Laws: Who Inherits, Small Estates and Selling the House','{ST} Probate Laws: Inheritance and Sales','{ST} probate laws: who inherits without a will, small estate rules, deadlines and selling an inherited house. Official sources.','{st} probate laws','{ST} probate law decides who inherits when there is no will, when a small estate can skip full probate, and who can sign a deed for an inherited house.',r'probate',
   [('Who inherits a {ST} house when there is no will?','The intestate succession statute cited above sets the order. The answer depends on which relatives survive.'),('Can we sell an inherited house before probate is finished?','Often the sale can be signed up while the estate is open, but the title company needs proof of who has authority to sign. Ask what documents it requires.'),('Do you buy inherited houses as-is?','Yes. We buy inherited houses in any condition, and we can wait for the court paperwork the title company needs.')]),
 'tx':('tax-deed-lien-sales','tax-deed-and-tax-lien-sales','{ST} Tax Deed and Tax Lien Sales: Process, Redemption and Selling First','{ST} Tax Deed and Tax Lien Sales','{ST} tax deed and tax lien sales: who runs the sale, interest, redemption periods and selling before the sale. Official sources.','{st} tax deed sales','When property tax goes unpaid in {ST}, the statutes allow the taxing authority to sell a lien or the property itself, and they give the owner a set time to redeem.',r'tax-sale|tax-deed|tax-lien',
   [('Can I sell my {ST} house before a tax sale?','Yes. The unpaid tax, interest and costs are paid from the sale proceeds at closing, which stops the tax sale.'),('Can I get the house back after a tax sale?','Only within the redemption rules in the statutes cited above. Check the deadline with the county office that ran the sale.'),('Do you buy houses with delinquent taxes?','Yes. We buy as-is and the title company pays the tax from the proceeds at closing.')]),
}
BAD=re.compile(r'search excerpt|snippet|metadata|not opened|unconfirmed|could not|inferred|not confirmed|verify|conflict|as introduced|proposed|pre-1985|effective until|effective (january|july) 1, 202[78]|justia',re.I)
def L(u,t): return f"<a href='{u}' target='_blank' rel='noreferrer noopener nofollow'>{esc(t)}</a>"
def run(st,allslugs):
    ST=N[st]; low=ST.lower().replace(' ','-'); fn=H+f'{st}_extra_facts.json'
    if not os.path.exists(fn): return []
    d=json.load(open(fn)); FS=d.get('topics',d); out=[]; made=[]
    plan=[]
    for k,(ft,suf,h1,rt,rd,fk,lead,exist,faqs) in T.items():
        if st not in VOL[k]: continue
        slug=f'{low}-{suf}'
        own=[s for s in allslugs.get(st,[]) if s.startswith(low+'-') and re.search(exist,s) and s!=slug]
        if slug in ALL or (own and k in('sq','lt','pr','tx')): continue
        fl=[]
        srcs=[]
        for x in (FS.get(ft) or {}).get('facts',[]):
            if not x.get('opened') or not x.get('url','').startswith('http'): continue
            c=clean_txt(str(x.get('claim','')))
            cite=clean_txt(str(x.get('cite','')))
            if not c or BAD.search(c) or BAD.search(cite) or 'justia' in x['url']: continue
            fl.append(f"{esc(c.rstrip('.'))}. ({esc(cite)}; {L(x['url'],'source')})")
            if x['url'] not in [u for _,u in srcs]: srcs.append((cite[:70] or 'Official source',x['url']))
        if len(fl)<2: print('skip',st,k,len(fl)); continue
        plan.append((k,slug,fl,srcs))
    slugs=[p[1] for p in plan]
    for k,slug,fl,srcs in plan:
        ft,suf,h1,rt,rd,fk,lead,exist,faqs=T[k]
        f=lambda s:s.format(ST=ST,st=ST.lower())
        h1,rt,rd,fk,lead=map(f,(h1,rt,rd,fk,lead)); faqs=[(f(q),f(an)) for q,an in faqs]
        if len(rt)>62: rt=rt[:62].rsplit(' ',1)[0]
        if len(rd)>155: rd=rd[:152].rsplit(' ',1)[0]+'.'
        crumb=rt
        cards=[(s,f(T[kk][3]),'Official sources.') for kk,s,_,_ in plan if s!=slug][:3]+[(f'{low}-guides-by-city-and-county',f'{ST} guides by city and county','Every local guide we publish.'),(f'we-buy-houses-in-{low}',f'We buy houses in {ST}','How a cash offer works.')]
        cards=[c for c in cards if c[0] in slugs or c[0].startswith('we-buy') or c[0] in ALL]
        how=ol(["Write down who is in the house and on what terms: owner, heirs, tenants or occupants with no lease.","Ask the title company what it needs to insure the sale, such as a recorded deed, court papers or a payoff letter.","Get the payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs. If you want a fast, simple closing, ask for a written cash offer. See "+a(f'we-buy-houses-in-{low}',f'we buy houses in {ST}')+"."])
        body=(f"<p><em>Last updated {DATE}. Citations come from {esc(ST)} statutes and official agency pages linked in Sources. Where we could not confirm something on an official page, we do not state it.</em></p>"
          f"<p><strong>{esc(lead)}</strong> Here is what the official sources say.</p><h2>What the official sources say</h2>"+ul(fl)
          +cta(f'Selling in {ST}?',f'We buy {ST} houses as-is, with no commission, no repairs and no closing costs to you.')
          +"<h2>What we could not confirm</h2>"+ul(["Details we could not confirm on an official page are not stated here. Read the statute sections linked above for the full text, and confirm deadlines with the court or county office."])
          +f"<h2>How to sell a {esc(ST)} house when this applies to you</h2>"+how
          +f"<h2>{esc(crumb)} FAQ</h2>"+faq_html(faqs)+related(ST,cards)+sources(srcs[:8])+DISCLAIM(ST,'attorney')
          +schema(faqs,[('Home',SITE),(ST,SITE+f'we-buy-houses-in-{low}/'),(crumb,SITE+slug+'/')]))
        out.append(wrap(slug,h1,hero(ST,h1,f'Selling a {ST} House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.'),body,rt,rd,fk))
    if out:
        json.dump(out,open(f'{R}/pages/{st}/{low}-state-pages-9.json','w'))
    return [p['slug'] for p in out]
ALL=set()
if __name__=='__main__':
    allslugs={}
    for fpath in glob.glob(f'{R}/pages/*/*.json'):
        if 'state-pages-9' in fpath: continue
        st=fpath.split('/')[-2]
        for p in json.load(open(fpath)): allslugs.setdefault(st,[]).append(p['slug']); ALL.add(p['slug'])
    for st in (sys.argv[1:] or sorted(N)):
        r=run(st,allslugs)
        if r: print(st,len(r),r)
