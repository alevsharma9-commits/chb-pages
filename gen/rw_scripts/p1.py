import json,re,sys
slug="nevada-property-tax-guide"
S=[]
def sec(h,html): S.append({"h2":h,"html":html})

sec("How does Nevada decide what a house is worth for tax?",
"""<p>Nevada property tax starts with the county assessor, an elected official who finds, lists and values the real and personal property in the county, according to the <a href="https://tax.nv.gov/wp-content/uploads/2025/03/2025-Property-Tax-Elements-Applications.pdf">Nevada Department of Taxation's guide to the property tax</a>. The state department oversees the system, but the number on your bill begins at the county level.</p>
<p>The state describes taxable value as the full cash value of the land plus the replacement cost new, less depreciation, of the improvements. For a house, that means the lot is valued on what it would sell for, and the building is valued on what it would cost to rebuild today minus a depreciation allowance for age and wear. That is a different method from a sale price, so an assessor's figure and an offer on your house can differ.</p>
<p>The assessed value is a fraction of that taxable value. NRS 361.225 requires all taxable property to be assessed at 35 percent of its taxable value. A notice of assessed value goes to each owner at the same time the tax roll is prepared.</p>
<ul>
<li>Land: full cash value, which is close to market value for the lot.</li>
<li>Improvements: replacement cost new, minus depreciation.</li>
<li>Assessed value: 35 percent of the sum of the two.</li>
<li>Tax bill: assessed value multiplied by the combined local rate, then reduced by any abatement.</li>
</ul>""")

sec("Is there a cap on how much Nevada property tax can rise?",
"""<p>Yes. Two limits apply: a ceiling on the total tax rate, and an abatement that holds down year-over-year increases on homes.</p>
<p>NRS 361.453 sets the total ad valorem levy for all public purposes at no more than $3.64 on each $100 of assessed valuation, with listed exceptions. The Department of Taxation notes the Legislature set that rate in 1979 and added $0.02 for state debt, which brings the total to $3.66. As a ceiling calculation only, a house with an assessed value of $140,000 would top out near $5,096 a year at $3.64 per $100 before any abatement (1,400 units of $100 times $3.64). Your actual rate depends on where the parcel sits, so look at your bill.</p>
<p>The abatement is in NRS 361.4723. The Legislature there found that a bill rising more than 3 percent over the prior year is a hardship, and it directs a partial abatement for an owner-occupied single-family residence. The department's guide describes the effect: the tax bill on these dwellings cannot rise more than 3 percent over the prior year's levy. Other parcels fall under a general abatement that the department describes as reaching up to 8 percent.</p>
<table>
<thead><tr><th>Item</th><th>What the source says</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Assessment ratio</td><td>35 percent of taxable value</td><td>NRS 361.225</td></tr>
<tr><td>Total levy ceiling</td><td>$3.64 per $100 of assessed value, with exceptions</td><td>NRS 361.453</td></tr>
<tr><td>Primary residence abatement</td><td>Bill cannot rise more than 3 percent over the prior year</td><td>NRS 361.4723</td></tr>
<tr><td>Other parcels</td><td>General abatement, described as up to 8 percent</td><td>Department of Taxation guide</td></tr>
</tbody>
</table>""")

sec("When are Nevada property taxes due, and what are the late penalties?",
"""<p>Taxes on the real property roll are due on the third Monday of August, and an owner may pay in four roughly equal installments if the bill is more than $100 (NRS 361.483).</p>
<p>Under that statute the installment dates are the third Monday of August, the first Monday of October, the first Monday of January and the first Monday of March. County treasurers report the same pattern. The Nye County treasurer says bills are prepared and mailed by August 1, for example.</p>
<ul>
<li>One installment unpaid 10 days after its due date: 4 percent penalty.</li>
<li>Two installments unpaid: 5 percent on the two installments due.</li>
<li>Three installments unpaid: 6 percent on the three installments due.</li>
<li>Full amount unpaid 10 days after the first Monday of March: 7 percent of the full amount.</li>
</ul>
<p>The statute also tells the county tax receiver to notify anyone who is penalized about the waiver provisions in NRS 361.4835. That section lets a county treasurer or assessor waive all or part of a late-payment penalty and interest in the circumstances it describes, so ask the treasurer before assuming a penalty is final.</p>""")

sec("What happens to a Nevada house when the taxes are not paid?",
"""<p>The tax stays attached to the property. Under NRS 361.450, every property tax is a perpetual lien until paid, and it is superior to all other liens, claims, encumbrances and titles on the property, whether or not the other lien was filed or perfected first. The lien attaches on July 1 of the year the taxes are levied.</p>
<p>If the bill is still open after the first Monday in June, the Clark County Treasurer explains that the county must hold the property for a two-year redemption period, during which the owner can redeem by paying the taxes, penalties, costs and 10 percent annual interest. If nothing is paid, the property is deeded to the county treasurer as trustee and can be sold at public auction. The <a href="/nevada-tax-sale/">Nevada tax sale guide</a> on this site covers that process in detail.</p>
<p>Two practical points follow from the lien rules. First, a buyer or title company will treat unpaid tax as something that has to be cleared at closing. Second, a short delay costs real money, because the penalty ladder above and the interest after a certificate both add up month by month.</p>""")

sec("What should a Nevada seller check on the tax side before listing?",
"""<p>Start with three documents: the latest tax bill, the notice of assessed value, and the county treasurer's account page showing whether any installment is open.</p>
<ol>
<li>Confirm which installments are paid and which are due. A balance can sit open for months without the owner noticing if the bill went to an old mailing address or to a lender.</li>
<li>Check whether the abatement applies. The residence has to be the owner's designated primary residence and cannot be rented or made available for exclusive occupancy by anyone other than the owner and family (NRS 361.4723).</li>
<li>Compare the assessor's figures with reality. A county board appeal under NRS 361.357 cannot raise your taxable value, and the filing deadline is January 15. The owner must first complete the assessor's form.</li>
<li>Ask whether special assessments are attached. NRS 361.450 treats assessments under chapter 271 as liens with the same priority as tax.</li>
</ol>
<p>Owners of inherited houses should also find out who is on the tax roll. If the former owner has died and the bill still goes to their address, delinquency can build before anyone notices.</p>""")

sec("What transfer tax applies when a Nevada house sells?",
"""<p>Nevada charges a real property transfer tax on each deed, and the rate depends on county size. NRS 375.020 sets $1.25 for each $500 of value in a county with 700,000 or more people, and 65 cents for each $500 in a smaller county, when the value of what is conveyed exceeds $100.</p>
<p>The tax is computed on the value declared on the declaration of value form required by NRS 375.060. For a $400,000 sale, that works out to 800 units of $500: $1,000 at the higher rate and $520 at the lower rate. Check with the county recorder for any additional local charges, because this statute section covers only the base tax.</p>
<p>Who pays is a contract term, so the purchase agreement should say. In a typical sale the transfer tax, prorated property tax and any open delinquency all appear on the settlement statement.</p>""")

sec("Can I sell a Nevada house with property tax owing?",
"""<p>Yes. A house with tax owing can sell, as long as the title company can clear the lien at closing, usually by paying the balance from the sale proceeds.</p>
<p>Cash buyers handle this often because they do not depend on a lender's underwriting timeline. The practical steps are the same either way: get a payoff figure from the county treasurer, include penalties and interest to the closing date, and give the escrow officer enough time to confirm the amount. If a trustee certificate has already been issued, the redemption cost is higher, since it includes interest at 10 percent a year plus costs.</p>
<p>Timing matters most when the house is close to an auction. Nevada law lets an owner, a lender and a person holding a contract to purchase redeem until 5 p.m. on the third business day before the sale (NRS 361.585). A buyer under contract can therefore protect the deal, but only if the money moves in time. We make offers on Nevada houses as-is, and we can review a tax bill with you before you decide anything.</p>""")

F=[
("Who sets my Nevada property tax rate?",
"Several local bodies do, within the state ceiling. The total levy for all public purposes cannot exceed $3.64 per $100 of assessed value except as the statute allows (NRS 361.453). The county assessor sets the value and the county treasurer sends the bill."),
("What is the assessed value of a Nevada house?",
"It is 35 percent of taxable value, under NRS 361.225. Taxable value is the land's full cash value plus the replacement cost of improvements less depreciation, per the Nevada Department of Taxation."),
("Can I pay Nevada property tax in installments?",
"Yes, if the bill is over $100. The four installments are due the third Monday of August, then the first Mondays of October, January and March (NRS 361.483). Penalties start at 4 percent for one late installment."),
("Does a tax lien come ahead of other liens in Nevada?",
"Yes. NRS 361.450 says the property tax lien is superior to all other liens, claims and encumbrances on the property, whether or not the other lien was filed first."),
("Is there a limit on how much my Nevada home tax can increase?",
"For an owner-occupied single-family primary residence, the partial abatement in NRS 361.4723 holds the yearly increase to 3 percent. Other property has a general abatement that the Department of Taxation describes as up to 8 percent."),
]
SRC=[
("Nevada Department of Taxation: Property Tax Elements and Applications (2025)","https://tax.nv.gov/wp-content/uploads/2025/03/2025-Property-Tax-Elements-Applications.pdf"),
("NRS 361.483 Time for payment of taxes; penalties","https://law.justia.com/codes/nevada/chapter-361/statute-361-483/"),
("NRS 361.450 Liens for taxes","https://law.justia.com/codes/nevada/chapter-361/statute-361-450/"),
("NRS 361.453 Limitation on total ad valorem tax levy","https://law.justia.com/codes/nevada/chapter-361/statute-361-453/"),
("NRS 361.4723 Partial abatement, single-family residences","https://law.justia.com/codes/nevada/chapter-361/statute-361-4723/"),
("NRS 361.585 Deeds to county treasurer as trustee; reconveyance","https://law.justia.com/codes/nevada/chapter-361/statute-361-585/"),
("NRS 375.020 Imposition and rate of transfer tax","https://law.justia.com/codes/nevada/chapter-375/statute-375-020/"),
("Clark County Treasurer: Real Property Tax Information","https://www.clarkcountynv.gov/government/elected_officials/county_treasurer/real-property-tax-information"),
("Nye County Treasurer","https://www.nyecountynv.gov/253/Treasurer"),
]
exec(open('/home/claude/chb-pages/gen/rw_scripts/tail.py').read())
