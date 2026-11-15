import json,re
slug="nevada-tax-sale"
S=[]
def sec(h,html): S.append({"h2":h,"html":html})

sec("How does a Nevada tax sale work from missed payment to auction?",
"""<p>A Nevada tax sale is the last step of a county process that starts with an unpaid bill and runs through a two-year redemption period, a deed to the county treasurer and a public sale. The owner keeps the right to pay and stop the process at nearly every stage.</p>
<p>The lien comes first. NRS 361.450 makes every property tax a perpetual lien that attaches on July 1 of the tax year and ranks ahead of other liens. When installments go unpaid, the tax receiver publishes and mails delinquency notices under NRS 361.5648 and 361.565, then issues a certificate for each unpaid property. Under NRS 361.570, that certificate lets the county treasurer, acting as trustee for the State and county, hold the property for 2 years after the first Monday in June of the certificate year, unless it is redeemed sooner.</p>
<table>
<thead><tr><th>Stage</th><th>What happens</th><th>Source</th></tr></thead>
<tbody>
<tr><td>July 1</td><td>Tax lien attaches to the property</td><td>NRS 361.450</td></tr>
<tr><td>Third Monday of August onward</td><td>Taxes due; installments follow in October, January and March</td><td>NRS 361.483</td></tr>
<tr><td>First Monday in June</td><td>Delinquent property goes onto a certificate held by the treasurer as trustee</td><td>NRS 361.570; Clark County Treasurer</td></tr>
<tr><td>Two years later</td><td>Redemption period ends; deed goes to the treasurer in trust</td><td>NRS 361.570, 361.585</td></tr>
<tr><td>After the deed</td><td>County commissioners can order a sale; notice by certified mail at least 90 days ahead</td><td>NRS 361.595</td></tr>
</tbody>
</table>""")

sec("How long do I have to redeem my Nevada property?",
"""<p>The base period is two years from the date of the certificate, and during it the owner can redeem by paying everything owed. The Clark County Treasurer states that the redemption payment includes the taxes, accruing taxes, penalties and costs, plus interest on the taxes at 10 percent per year from the original due date.</p>
<p>NRS 361.570 adds a point that surprises owners: the property keeps being assessed during the redemption period. Before redeeming, the owner must also pay taxes, penalties and costs that accrue after the certificate date, with the same 10 percent interest, assessed monthly. The payoff therefore grows each year.</p>
<p>There is a shorter path for abandoned property. Under NRS 361.567 the tax receiver may use an expedited procedure for property found to be abandoned, and the certificate then gives only 1 year of redemption. Clark County's treasurer notes that this election is available after a one year period for such properties.</p>
<ul>
<li>Normal certificate: 2 years to redeem.</li>
<li>Abandoned property under the expedited procedure: 1 year.</li>
<li>Notice by certified mail before a trustee sale: at least 90 days, or at least 45 days in the expedited case (NRS 361.595).</li>
</ul>""")

sec("Can I still get my property back after the deed goes to the county?",
"""<p>Yes, for a short window. Even after the county treasurer holds the deed as trustee, NRS 361.585 lets certain people have the property reconveyed by paying the taxes, costs, penalties and interest, until 5 p.m. on the third business day before the sale. The Washoe County Treasurer repeats this deadline on its auction page and adds that the treasurer may withdraw a property before or at the auction.</p>
<p>The statute does not limit reconveyance to the owner. The people who may redeem include:</p>
<ul>
<li>The owner and the person to whom the property was assessed.</li>
<li>A beneficiary under a deed of trust or a mortgagee.</li>
<li>A judgment creditor.</li>
<li>A person holding a contract to purchase the property before it was conveyed to the county treasurer.</li>
<li>The Director of the Department of Health and Human Services if the owner has received Medicaid benefits.</li>
<li>A municipality that holds a lien, and any successor in interest.</li>
</ul>
<p>The purchase-contract line matters to sellers. A buyer who signed a contract before the deed to the treasurer can pay what is owed and take the property back out of trust. A lender or a family member with a recorded interest has similar rights.</p>""")

sec("How do Nevada counties actually run the auction?",
"""<p>Each county treasurer runs its own sale, so the format and calendar vary. Washoe County says it holds one real estate tax auction a year, usually in April, and lists the next one as April 2027. Bidders register before the sale, and the treasurer records a quitclaim deed within 30 days of the auction.</p>
<p>The opening bid is set by the county. Washoe explains that it is the delinquent taxes, assessments, costs, interest and penalties, or the assessed valuation, whichever is greater. The assessed value is about 35 percent of appraised value, so in some cases it exceeds the tax debt. The county says its sole interest is to recover what is owed and that buyers must investigate the property for themselves.</p>
<p>Nye County lists 2026 online-only tax sale auctions, and the Clark County Treasurer publishes a trustee auction parcel list that it updates often, with some parcels crossed out when they are no longer eligible. Those pages show how quickly a parcel can drop off the list when someone pays.</p>
<p>NRS 361.595 sets the sale notice rules. Notice must be posted in at least three public places, including the courthouse and the property, at least 20 days ahead, or published for four weeks. Separately, the owner and any lienholders of record get certified mail at least 90 days before the sale. The buyer receives a quitclaim deed, and the treasurer records it at the buyer's expense.</p>""")

sec("What happens to the money if the property sells for more than the tax debt?",
"""<p>The surplus belongs to the former owner or lienholders, but only if someone claims it in time. NRS 361.610 sets the order of payment, and a missed deadline sends the money to the county.</p>
<ol>
<li>The treasurer pays the taxes and costs on that parcel first.</li>
<li>From the excess, the county general fund takes the first $300 and 10 percent of the next $10,000.</li>
<li>The remainder goes into a separate interest-bearing account.</li>
<li>A written claim must be made within 1 year after the treasurer's deed is recorded. After that, the money goes to the county general fund and cannot be refunded to the former owner.</li>
</ol>
<p>The treasurer must approve or deny a claim within 30 days after the claim period ends. Lienholders such as lenders and certain associations rank ahead of the owner in the payment order. If more than one person claims, the matter goes to mediation, then to a hearing or an interpleader action. An aggrieved person has 90 days to seek judicial review in district court.</p>
<p>Be careful with people who offer to recover surplus funds for a fee. A recovery agreement must be in writing and signed, and for a natural person's primary residence the fee cannot exceed 10 percent of the remaining excess proceeds.</p>""")

sec("Can a city or county take the property without a sale?",
"""<p>In some cases, yes. NRS 361.603 lets a local government or the Nevada System of Higher Education apply to the board of county commissioners to acquire property held in trust, if a public purpose is served. The treasurer then sends notice of intent to sell to the last known owner or heirs.</p>
<p>The owner has 90 days after that notice to redeem by paying the delinquent taxes, penalties, interest and costs. If the owner does not, the treasurer transfers the property to the local government for the amount of the delinquent taxes. When the transfer is for street, sewer or drainage use, for a program to rehabilitate abandoned residential properties, or for open space, the delinquent taxes need not be paid at all.</p>
<p>The 90 day notice goes to the last known owner or heirs, so an outdated mailing address is a real risk. Keep the treasurer's records current if you own a house you are not living in.</p>""")

sec("How can I sell a Nevada house before the tax sale?",
"""<p>The cleanest way is to close a sale while the property is still in your name or in redemption, and pay the county from the proceeds. Because the tax lien outranks other liens, a title company will require the balance cleared before it insures a buyer.</p>
<p>A cash purchase can move on a shorter clock than a financed one, since it avoids a lender appraisal and underwriting. The sequence is straightforward:</p>
<ul>
<li>Ask the county treasurer for a written payoff figure, with the interest and costs through your expected closing date.</li>
<li>Find out whether the property is still in the redemption period or already deeded to the treasurer as trustee, because the deadline and the people who can redeem differ.</li>
<li>Sign the purchase contract and date it clearly, because the redemption right for a contract holder applies to a contract made before the property was conveyed to the treasurer.</li>
<li>Close, pay the treasurer, and collect what is left of your equity.</li>
</ul>
<p>If the sale price is above the debt, you keep the difference. At auction, the surplus claim process described above applies instead, with a one year claim limit and county fees taken off first. We buy Nevada houses as-is and will give you a straight read on whether the timeline can work.</p>""")

F=[
("What does a Nevada county tax sale sell?",
"It sells property that the county treasurer holds in trust after the redemption period ends. The treasurer delivers a quitclaim deed to the buyer under NRS 361.595, and the county's goal is to recover the delinquent taxes, penalties, interest and costs."),
("Can I stop a Nevada tax sale by paying?",
"Yes. Under NRS 361.585 the owner and certain others can have the property reconveyed by paying the taxes, costs, penalties and interest until 5 p.m. on the third business day before the sale."),
("How much interest accrues on delinquent Nevada property tax?",
"NRS 361.570 states interest on the taxes accrues at 10 percent per year, assessed monthly, from the date due until paid. The Clark County Treasurer describes the same rate."),
("Do I get money if my Nevada house sells at a tax auction for more than I owed?",
"Possibly. After taxes and costs, the county takes the first $300 and 10 percent of the next $10,000, and the rest is held for claims. A written claim must be filed within 1 year after the deed is recorded (NRS 361.610)."),
("Is the Nevada tax sale redemption period always two years?",
"No. The certificate allows 2 years to redeem, but NRS 361.570 gives only 1 year for property determined to be abandoned under the expedited procedure in NRS 361.567."),
]
SRC=[
("NRS 361.450 Liens for taxes","https://law.justia.com/codes/nevada/chapter-361/statute-361-450/"),
("NRS 361.570 Trustee's certificate; redemption","https://law.justia.com/codes/nevada/chapter-361/statute-361-570/"),
("NRS 361.585 Deeds to county treasurer as trustee; reconveyance","https://law.justia.com/codes/nevada/chapter-361/statute-361-585/"),
("NRS 361.595 Conveyances of property held in trust","https://law.justia.com/codes/nevada/chapter-361/statute-361-595/"),
("NRS 361.603 Acquisition by local government","https://law.justia.com/codes/nevada/chapter-361/statute-361-603/"),
("NRS 361.610 Disposition of proceeds; excess proceeds claims","https://law.justia.com/codes/nevada/chapter-361/statute-361-610/"),
("NRS 361.483 Time for payment of taxes; penalties","https://law.justia.com/codes/nevada/chapter-361/statute-361-483/"),
("Clark County Treasurer: Real Property Tax Information","https://www.clarkcountynv.gov/government/elected_officials/county_treasurer/real-property-tax-information"),
("Washoe County Treasurer: Tax Auction","https://www.washoecounty.gov/treas/TaxSale.php"),
("Washoe County Treasurer: Real Property Tax Sales FAQ","https://www.washoecounty.gov/treas/faq/faq-category_Real_Property_Tax_Sales.php"),
("Nye County Treasurer: Prior Trust Property Auction Information","https://www.nyecountynv.gov/254/Prior-Trust-Property-Auction-Information"),
]
exec(open('/home/claude/chb-pages/gen/rw_scripts/tail.py').read())
