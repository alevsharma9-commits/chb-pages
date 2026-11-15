import json,re
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("Does Delaware have an estate tax or inheritance tax today?",
"<p>No. Delaware has neither tax for people who die after December 31, 2017. The Division of Revenue's estate tax summary records that the estate tax was repealed for individuals dying after that date, under 81 Del. Laws c. 52 (HB 16).</p>"
"<p>The inheritance tax went first. Chapter 13 of Title 30 of the Delaware Code, the inheritance tax chapter, now carries the label \"Repealed.\" The Division's legislative history says a 1998 law repealed the inheritance tax effective January 1, 1999 and revised the estate tax to apply to estates large enough to need a federal estate tax return.</p>"
"<p>For heirs who plan to sell a Delaware house, that is good news about one cost and no news about the others. The state does not tax the inheritance itself, but the sale can still trigger realty transfer tax, county property tax and possibly federal rules.</p>")
sec("How did Delaware's estate tax work before the repeal?",
"<p>For deaths before January 1, 2018, Delaware taxed the value of an estate at death, using the federal estate tax as its starting point. It is worth knowing if the person who owned your house died in 2017 or earlier.</p>"
"<p>The Division of Revenue explains that a resident's Delaware taxable estate was the modified federal taxable estate, reduced but not below zero by the federal applicable exclusion amount. For 2017 that exclusion was $5,490,000 for an individual. The Division's rate table was graduated, and Morris Nichols reports a top rate capped at 16%.</p>"
"<table><thead><tr><th>Date</th><th>Change</th></tr></thead><tbody>"
"<tr><td>July 1, 1998 (effective January 1, 1999)</td><td>Inheritance tax repealed; estate tax revised to follow the federal return requirement</td></tr>"
"<tr><td>July 1, 2009</td><td>Estate tax effectively reinstated with a four-year sunset</td></tr>"
"<tr><td>March 28, 2013</td><td>Sunset eliminated</td></tr>"
"<tr><td>July 2, 2017 (effective January 1, 2018)</td><td>Estate tax repealed for individuals dying after December 31, 2017</td></tr>"
"</tbody></table>"
"<p>Source: Delaware Division of Revenue, Estate Tax summary, legislative history.</p>")
sec("What if the owner died before 2018 and the estate is still open?",
"<p>Then the old rules may still matter, and you should ask the Register of Wills or an estate attorney. The repealed sections of Chapter 15 of Title 30 carry notes pointing to 81 Del. Laws c. 52, section 2 about how the repeal applies.</p>"
"<p>The Division's filing rules for the old tax were these:</p>"
"<ul>"
"<li>The return and the tax were due within nine months after the date of death.</li>"
"<li>The Division could extend filing and payment time on written request. If the federal return was extended, the Delaware return was extended for a like period.</li>"
"<li>Interest ran at one-half of one percent per month on late tax, and penalties could include a failure-to-pay penalty of 1% per month up to 25%.</li>"
"<li>For nonresidents, a special lien attached to Delaware real and tangible property until the tax was paid.</li>"
"</ul>"
"<p>The Sussex County Register of Wills publishes form NDETRR99, an affidavit that no Delaware estate tax return is required, for decedents who died from January 1, 1999 through December 31, 2017. It is signed before a notary by the personal representative or a surviving joint tenant, lists any Delaware real property, and cites 30 Del. C. 1505. An older estate that never cleared title may need that paper before a buyer will close.</p>")
sec("Could federal estate tax still apply to a Delaware house?",
"<p>Federal estate tax applies only to very large estates. The IRS says the basic exclusion amount is $15,000,000 for calendar year 2026, up from $13,990,000 for 2025.</p>"
"<p>The IRS also says a surviving spouse can elect to take over the decedent's unused exclusion on a timely filed estate tax return. That election has been available since January 1, 2011.</p>"
"<p>The statewide median home value is far below the exclusion, so a federal return is rarely the issue for one house. We are not tax preparers. If the estate holds many assets or you are unsure, ask a CPA or estate attorney.</p>")
sec("Do heirs owe realty transfer tax when a Delaware house changes hands?",
"<p>Sometimes. Delaware's realty transfer tax is a separate tax from the estate tax, and some transfers within families are excluded from it. The rules are in Chapter 54 of Title 30.</p>"
"<p>Section 5401(1) says a taxable \"document\" does not include a will or a transfer on death deed. It also excludes conveyances between spouses, between parent and child or the child's spouse, between siblings, half siblings or step siblings, and between grandparent and grandchild or the grandchild's spouse.</p>"
"<p>A sale to an outside buyer is a different matter. Under section 5402, the rate is 3% of value unless the county or municipality has enacted the full 1.5% local tax, in which case it is 2.5%. The Division's instructions put the combined state and local total at 4%, with 2.5% to the state and 1.5% to the county or municipality. The tax is apportioned equally between grantor and grantee, and under section 5412, absent a contrary agreement, the burden of paying falls on the grantor.</p>"
"<p>The instructions list estates and trusts among grantor categories but, in the text we reviewed, do not describe a special estate exemption. If a personal representative is signing the deed, confirm the treatment with the county Recorder of Deeds.</p>")
sec("What does selling an inherited Delaware house usually involve?",
"<p>The steps run through probate, title and the county. Delaware's three counties, New Castle, Kent and Sussex, each have their own Register of Wills and Recorder of Deeds, so the office depends on where the house sits.</p>"
"<ul>"
"<li>Open the estate with the Register of Wills in the county, and have the personal representative appointed.</li>"
"<li>Resolve any open estate tax paperwork if the death was before 2018.</li>"
"<li>Pay or settle county and school property taxes. Under Title 9, taxes in New Castle and Sussex are due July 1 and in Kent June 1.</li>"
"<li>Sign a deed and pay realty transfer tax at recording, with proof of payment on the document. A deed without it cannot be recorded under section 5408.</li>"
"<li>Deliver the house in the condition the contract requires. A cash sale can be as-is.</li>"
"</ul>"
"<p>Late county taxes cost money. In New Castle County the collecting authority adds a 6% penalty after September 1 plus 1% a month on the unpaid balance. In Kent and Sussex a penalty of 1.5% per month starts after September 30 of the year the tax duplicate is delivered.</p>")
sec("What do Delaware housing numbers look like for heirs?",
"<p>Delaware is mostly owner-occupied, and nearly a quarter of residents are 65 or older. The Census Bureau supplies the basics.</p>"
"<table><thead><tr><th>Measure</th><th>Delaware</th></tr></thead><tbody>"
"<tr><td>Population estimate, July 1, 2025</td><td>1,059,952</td></tr>"
"<tr><td>Persons 65 and over</td><td>22.8%</td></tr>"
"<tr><td>Housing units, July 1, 2025</td><td>483,447</td></tr>"
"<tr><td>Owner-occupied housing unit rate, 2020 to 2024</td><td>73.0%</td></tr>"
"<tr><td>Median value of owner-occupied units, 2020 to 2024</td><td>$352,000</td></tr>"
"</tbody></table>"
"<p>Source: U.S. Census Bureau QuickFacts. The median value is a statewide figure for owner-occupied homes, not an appraisal of any one house.</p>"
"<p>If you inherited a Delaware house you do not want to keep, a cash buyer can close as-is, which spares repairs and clean-out on a property in a distant county. Terms vary by house, and we recommend you have an attorney review the estate side.</p>")
F=[
("Is there a Delaware inheritance tax?","No. Chapter 13 of Title 30, the inheritance tax chapter, is marked repealed, and the Division of Revenue records the inheritance tax repeal as effective January 1, 1999."),
("When was the Delaware estate tax repealed?","It was repealed for individuals dying after December 31, 2017. The repeal was approved July 2, 2017 as 81 Del. Laws c. 52 (HB 16)."),
("What is the federal estate tax exclusion for 2026?","The IRS lists $15,000,000 as the basic exclusion amount for calendar year 2026, compared with $13,990,000 for 2025."),
("Do I pay realty transfer tax if I inherit a Delaware house?","A will and a transfer on death deed are not taxable documents, and conveyances between parent and child, siblings, and grandparent and grandchild are also excluded under 30 Del. C. 5401. A sale to an outside buyer is taxed at a combined 4%, split equally between buyer and seller unless the contract says otherwise."),
("Where do I record the deed for an inherited Delaware house?","Record it with the Recorder of Deeds in the county where the property is located. Proof of realty transfer tax payment, or an affidavit explaining why none is owed, must accompany the document."),
]
src=[("Delaware Division of Revenue, Estate Tax summary (PDF)","https://financefiles.delaware.gov/docs/estate_tax.pdf"),
("Delaware Code Title 30, Chapter 13 (Inheritance, repealed)","https://delcode.delaware.gov/title30/c013/index.html"),
("Delaware Code Title 30, Chapter 15 (Estate tax, repealed sections)","https://delcode.delaware.gov/title30/c015/index.html"),
("Morris Nichols, Delaware Estate Tax Repeal","https://www.morrisnichols.com/insights-delaware-estate-tax-repeal"),
("Sussex County Register of Wills, Form NDETRR99","https://sussexcountyde.gov/sites/default/files/PDFs/NDETRR99.pdf"),
("IRS, What's new: Estate and gift tax","https://irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax"),
("Delaware Code Title 30, Chapter 54 Subchapter I (Realty transfer tax)","https://delcode.delaware.gov/title30/c054/sc01/index.html"),
("Delaware Realty Transfer Tax return instructions","https://revenuefiles.delaware.gov/2023/RTT-TAX_2021-02_Instructions.pdf"),
("Delaware Code Title 9, Chapter 86 (Tax billing and penalties)","https://delcode.delaware.gov/title9/c086/index.html"),
("U.S. Census Bureau QuickFacts, Delaware","https://www.census.gov/quickfacts/fact/table/DE/PST045224")]
slug="delaware-estate-tax"
d={"slug":slug,"sections":S,"faqs":[{"q":q,"a":a} for q,a in F],"sources":[{"title":t,"url":u} for t,u in src]}
txt=" ".join(re.sub(r'<[^>]+>',' ',s['h2']+' '+s['html']) for s in S)+" "+" ".join(q+' '+a for q,a in F)
print(len(txt.split()), '—' in txt, '–' in txt)
json.dump(d,open(f'/home/claude/chb-pages/gen/rw/{slug}.json','w'),ensure_ascii=False,indent=1)
