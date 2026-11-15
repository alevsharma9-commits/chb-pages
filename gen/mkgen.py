import json,re,sys,os
G=open(os.path.join(os.path.dirname(__file__),'ga_all.py')).read()
CAT={
 'property-tax':('property-tax-guide','{ST} Property Tax Guide: Appeals, Exemptions and Selling With Tax Due','{ST} Property Tax Guide: Appeals','{ST} property tax: appeals, exemptions, delinquent tax and selling a house with tax due. Official sources.','{st} property tax','{ST} property tax is assessed and collected at the local level, and owners can appeal an assessment.',['property-tax-appeals','tax-sales:2'],'What happens to unpaid property tax when I sell?','The closing agent pays unpaid tax from the sale proceeds at closing.'),
 'homestead':('homestead-exemption','{ST} Homestead Exemption: Eligibility, Filing and Selling the Home','{ST} Homestead Exemption Guide','{ST} homestead exemption: who qualifies, how to apply and what happens when you sell. Official sources only.','{st} homestead exemption','{ST} offers property tax relief for qualifying homeowners, and official sources explain the rules.',['homestead-exemption'],'Where do I apply for the homestead exemption?','Apply with the local assessor or county office named in the sources above. Confirm the deadline with your county.'),
 'estate-tax':('estate-tax','{ST} Estate and Inheritance Tax: What Heirs Owe When Selling','{ST} Estate and Inheritance Tax','{ST} estate and inheritance tax rules and how they affect heirs selling an inherited house. Official sources only.','{st} estate tax','This guide covers what official sources say about {ST} estate and inheritance tax.',['estate-tax'],'Does {ST} have an estate tax?','See the official sources above. We state only what we could confirm on official pages.'),
 'eviction':('eviction-process','{ST} Eviction Process and Selling a Rented House','{ST} Eviction Process and Tenants','{ST} eviction process and what it means when you sell a house with tenants. Official sources only.','{st} eviction process','{ST} evictions follow notice and court steps set by state law.',['eviction-process','tenant-occupied-sale'],'Can I sell a house with tenants?','Yes. A cash buyer can purchase tenant-occupied property as-is.'),
 'quitclaim':('quitclaim-deed','{ST} Quitclaim Deed: Recording, Fees and When It Works','{ST} Quitclaim Deed: Recording and Fees','{ST} quitclaim deed: how it works, recording and transfer tax rules. Official sources only.','{st} quitclaim deed','A {ST} deed is recorded with the county office named in the sources below.',['quitclaim-deed','deeds-recording:3'],'Where do I record a deed in {ST}?','With the county recording office where the property is located.'),
 'tod':('transfer-on-death-deed','{ST} Transfer on Death Deed: How It Works','{ST} Transfer on Death Deed Explained','{ST} transfer on death deed: what official sources say and what we could not confirm.','{st} transfer on death deed','This guide covers what official sources say about {ST} transfer on death deeds.',['transfer-on-death-deed','probate-and-inherited-property:3'],'What is a transfer on death deed?','A recorded deed that names who receives the property when the owner dies. Confirm the {ST} rules with an attorney.'),
 'closing-costs':('closing-costs','{ST} Closing Costs for Sellers: Transfer Tax, Recording and What You Pay','{ST} Closing Costs for Sellers','{ST} seller closing costs: transfer tax, recording and what a cash sale saves. Official sources only.','{st} closing costs','The {ST} seller closing costs we can source are the taxes and fees below.',['closing-costs','property-transfer-tax:3'],'Who pays the transfer tax?','See the statute cited above for who owes it.'),
 'transfer-tax':('transfer-tax','{ST} Real Estate Transfer Tax: Rates, Exemptions and Who Pays','{ST} Real Estate Transfer Tax Explained','{ST} real estate transfer tax: rates, exemptions and who pays when you sell a house. Official sources only.','{st} transfer tax','{ST} charges a tax or fee on real estate transfers, as described below.',['property-transfer-tax'],'Who pays the transfer tax?','See the statute cited above for who owes it.'),
 'tax-lien':('tax-lien','{ST} Tax Liens and Delinquent Property Tax','{ST} Tax Liens and Delinquent Tax','{ST} delinquent property tax: tax liens, redemption and what to do before a tax sale. Official sources only.','{st} tax lien','{ST} counties pursue delinquent property tax through liens and tax sales.',['tax-liens','tax-sales'],'Can I stop a tax sale?','Paying the delinquent amount or selling before the sale can pay the tax from the proceeds. Ask the county for exact figures.'),
 'tax-sale':('tax-sale','{ST} Tax Sales: Redemption and Selling Before the Sale','{ST} Tax Sales and Redemption','{ST} tax sales: how they work, redemption and selling a house with delinquent tax. Official sources only.','{st} tax sale','{ST} counties hold tax sales of delinquent property.',['tax-sales','tax-liens'],'Can I redeem after a tax sale?','See the redemption rules above and confirm exact amounts with your county.'),
 'probate':('probate-process','{ST} Probate Process and Selling Inherited Property','{ST} Probate Process Explained','{ST} probate: the court process, small estates and selling an inherited house. Official sources only.','{st} probate','{ST} probate runs through the courts named in the sources below.',['probate-and-inherited-property'],'Who can sell a house in probate?','The personal representative with court authority signs for the estate.'),
 'capital-gains':('capital-gains-tax','{ST} Capital Gains Tax When You Sell a House','{ST} Capital Gains Tax on a House Sale','{ST} income tax treatment when you sell a house: what we could confirm on official pages.','{st} capital gains tax','This guide covers what official sources say about {ST} tax on a house sale.',['capital-gains'],'Does {ST} tax capital gains?','See the official sources above. Federal rules are outside this guide.'),
 'land-contract':('land-contract','{ST} Land Contracts and Contracts for Deed: Seller Rules','{ST} Land Contracts: Seller Rules','{ST} land contracts and contracts for deed: what sellers should know. Official sources only.','{st} land contract','{ST} land contracts have rules set by statute, summarized below.',['land-contracts'],'What is a land contract?','A contract where the buyer pays over time while the seller keeps title until a set point.'),
 'foreclosure':('foreclosure-process','{ST} Foreclosure Process: Notice, Sale and Your Options','{ST} Foreclosure Process Explained','{ST} foreclosure process: notice, sale and what you can do before the sale. Official sources only.','{st} foreclosure process','This guide covers how {ST} mortgage foreclosure works according to official sources.',['foreclosure','sheriff-sale'],'Can I sell my house before a foreclosure sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask for a payoff figure.'),
 'sheriff-sale':('sheriff-sale','{ST} Sheriff Sales: Foreclosure Sale Steps and Redemption','{ST} Sheriff Sale Explained','{ST} sheriff sale: how a foreclosure sale works and what you can do first. Official sources only.','{st} sheriff sale','This guide covers {ST} foreclosure sales according to official sources.',['sheriff-sale','foreclosure'],'Can I sell my house before a sheriff sale?','Yes. A cash sale can pay the lender from the proceeds if it closes before the sale. Ask for a payoff figure.'),
 'recording':('recording-deeds','{ST} Recording a Deed: Fees, Where to File and What to Bring','{ST} Recording a Deed Guide','{ST} deed recording: where to record, fees and what to bring. Official sources only.','{st} deed recording','Deeds are recorded with the county office named in the sources below.',['deeds-recording'],'Where do I record a deed in {ST}?','With the county recording office where the property is located.'),
 'seller-disclosure':('seller-disclosure','{ST} Seller Disclosure Rules When Selling a House','{ST} Seller Disclosure Rules','{ST} seller disclosure rules: what sellers must tell buyers and what a cash sale changes. Official sources only.','{st} seller disclosure','This guide covers {ST} seller disclosure rules according to official sources.',['seller-disclosure','short-sale-cash-as-is'],'Do I have to disclose problems when I sell?','See the statute cited above for what {ST} requires.'),
}
def build(cfg):
    code=cfg['code'];ST=cfg['ST'];low=ST.lower().replace(' ','-');ab=code
    s=G
    a=s.index("SRC=["); b=s.index("def mk(")
    sp=",".join(f"('{low}-{CAT[k][0]}','{ST} {CAT[k][2].replace('{ST} ','')}','x')" for k in cfg['topics'][:3])
    SPB=f'''SRC={cfg['src']!r}
CASH="If you want a fast, simple closing, ask for a written cash offer. We buy houses as-is, with no repairs and no agent commission. See "+a('we-buy-houses-in-{low}','we buy houses in {ST}')+"."
HOW=lambda:ol(["Find out what the {cfg.get('closer','title company')} needs. For an inherited or transferred house, that usually means the recorded deed or the probate paperwork that shows who owns it today.","Get a payoff for any mortgage and the amount of any unpaid property tax. Both are paid from the sale proceeds at closing.","Compare offers on what you net after repairs, commissions and closing costs, not on the headline price.",CASH])
SP=[{",".join(f"('{low}-{CAT[k][0]}','{CAT[k][2].format(ST=ST)}','Official sources.')" for k in cfg['topics'][:3])},('we-buy-houses-in-{low}','We buy houses in {ST}','How a cash offer works.')]
'''
    s=s[:a]+SPB+s[b:]
    lines=["def state_pages():","    P=[]",
      "    def sp(slug,h1,rt,rd,fk,lead,items,faqs,crumb,unc=None):",
      "        body=f\"<p><strong>{lead}</strong> Here is what the official sources say.</p>\"+(sec('What the official sources say',items) if items else '')+CTAA+(UNC(unc) if unc else '')+\"<h2>How to sell a "+ST+" house when this applies to you</h2>\"+HOW()",
      "        P.append(mk(slug,h1,rt,rd,fk,'Selling a "+ST+" House? Get a Cash Offer','We buy as-is. Tell us about the property and the timeline.',body,faqs,crumb,[c for c in SP if c[0]!=slug][:4],SRC))",
      "    def F(spec):",
      "        out=[]",
      "        for t in spec:",
      "            k,_,n_=t.partition(':')",
      "            if k in FS:",
      "                x=facts(k); out+=x[:int(n_)] if n_ else x",
      "        return out"]
    for k in cfg['topics']:
        slug,h1,rt,rd,fk,lead,ft,fq,fa=CAT[k]
        fm=lambda x:x.format(ST=ST,st=ST.lower())
        h1,rt,rd,fk,lead,fq,fa=map(fm,(h1,rt,rd,fk,lead,fq,fa))
        rt=rt if len(rt)<=62 else rt[:62]
        if len(rd)>155: rd=rd[:152].rsplit(' ',1)[0]+'.'
        unc=cfg.get('unc',{}).get(k,["Details we could not confirm on an official page are not stated."])
        lines.append(f"    sp({f'{low}-{slug}'!r},{h1!r},{rt!r},{rd!r},{fk!r},{lead!r},F({ft!r}),[({fq!r},{fa!r})],{fm(CAT[k][2])!r},{unc!r})")
    lines.append("    return P\n")
    a=s.index("def state_pages():"); b=s.index("def city_page")
    s=s[:a]+"\n".join(lines)+s[b:]
    # replacements
    for o,n_ in [('ga_fact_sheet',f'{code}_fact_sheet'),('ga_cities',f'{code}_cities'),('ga_city_ptax',f'{code}_city_ptax'),('ga_cty_',f'{code}_cty_'),('pages/ga',f'pages/{code}'),('georgia-',f'{low}-'),("'georgia",f"'{low}"),('Georgia',ST),(', GA',f', {code.upper()}'),('-ga-',f'-{code}-'),('-ga"',f'-{code}"'),("-ga'",f"-{code}'"),('{c}, GA',f'{{c}}, {code.upper()}'),('GA property',f'{code.upper()} property'),(' GA ',f' {code.upper()} ')]:
        s=s.replace(o,n_)
    # role/appeal text
    r=cfg['roles']
    for o,n_ in [("clerk-of-superior-court",r['rec_slug']),("Clerk of Superior Court",r['rec']),("clerk of superior court",r['rec'].lower()),("county tax commissioner",r['coll'].lower()),("Owners generally have 45 days from the date the assessment notice was mailed to appeal to the county Board of Tax Assessors (O.C.G.A. 48-5-311).",r['appeal']),("Appeals go to the county Board of Tax Assessors, generally within 45 days of the date the assessment notice was mailed.",r['appeal_short']),("Georgia bills combine county, city and school district millage.",r['bill'])]: s=s.replace(o,n_)
    s=s.replace("A seller handling the sale directly still needs a deed, a closing attorney and to account for the real estate transfer tax.","A seller handling the sale directly still needs a deed, a closing agent and to account for any transfer tax. See "+"\"+a('"+low+"-"+CAT[cfg['topics'][0]][0]+"','the "+ST+" "+CAT[cfg['topics'][0]][2].replace('{ST} ','').lower()+"')+\".")
    # city paragraph
    i=s.index('<h2>Situations we see with {esc(c)} houses</h2>'); j=s.index('+f"<h2>How to sell a house in {esc(c)}</h2>"',i)
    P0=f"{low}-{CAT['property-tax'][0]}"; 
    links=[k for k in cfg['topics'] if k in ('probate','foreclosure','sheriff-sale','tax-lien')]
    para=f"<h2>Situations we see with {{esc(c)}} houses</h2><p><strong>Behind on the mortgage.</strong> We can often close before a foreclosure sale and pay the lender from the proceeds."+(f" See \"+a('{low}-{CAT['foreclosure'][0]}','the {ST} foreclosure guide')+\"." if 'foreclosure' in cfg['topics'] else (f" See \"+a('{low}-{CAT['sheriff-sale'][0]}','the {ST} sheriff sale guide')+\"." if 'sheriff-sale' in cfg['topics'] else ""))+"</p><p><strong>Inherited house.</strong> We buy houses that are still in probate or newly inherited."+(f" See \"+a('{low}-{CAT['probate'][0]}','the {ST} probate guide')+\"." if 'probate' in cfg['topics'] else "")+"</p><p><strong>Unpaid property tax.</strong> The closing agent pays unpaid tax from the proceeds."+(f" See \"+a('{P0}','the {ST} property tax guide')+\"" if 'property-tax' in cfg['topics'] else "\"")+("+(f\" and {a(ns(c)+'-"+code+"-property-tax-guide',esc(c)+' property tax')}\" if c in PTCOK else '')+\".</p>" if 'property-tax' in cfg['topics'] else "+\"</p>")
    s=s[:i]+para+'"\n     '+s[j:]
    s=re.sub(r"PTC=\[[^\]]*\]","PTC=%s"%json.dumps(cfg['ptc']),s,count=1)
    s=s.replace("for _k in 'ABCDEF'","for _k in %r"%cfg['batches'])
    s=s.replace("(Census Bureau)","(Census Bureau)")
    # cf with excerpt facts
    old=re.search(r"def cf\(v,k\):.*\n",s).group(0)
    new='''def cf(v,k):
    out=[]; ex=[]
    for x in (v.get(k) or {}).get('facts',[]):
        if BAD.search(x['claim']): continue
        if x.get('opened'): out.append(clean_txt(x['claim']))
        elif not re.search(r'deeds\\.com|facebook|twitter|zillow|redfin|justia',x.get('url') or '',re.I) and x.get('url','').startswith('http'): ex.append(clean_txt(x['claim'])+' (from the county site listing; confirm with the office)')
    return (out+ex)[:4]
'''
    s=s.replace(old,new)
    s=s.replace("')+\"+(f\" and","')+(f\" and")
    s=s.replace("def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):\n","def mk(slug,h1,rt,rd,fk,h2,hp,body,faqs,crumb,cards,srcs):\n    rd=rd if len(rd)<=155 else rd[:152].rsplit(' ',1)[0]+'.'\n    rt=rt if len(rt)<=62 else rt[:62].rsplit(' ',1)[0]\n",1)
    s=s.replace("r['value']","(r.get('value') or r.get('text'))").replace("if r and r.get('opened') else","if isinstance(r,dict) and r.get('opened') else").replace(" for {r.get('year')}.",".")
    open(f'gen/{code}_all.py','w').write(s)
if __name__=='__main__': build(json.load(open(sys.argv[1])))
