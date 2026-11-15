import json,re
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("Where is Sparks and how did it start?",
"<p>Sparks is a city in Washoe County just east of Reno, founded as a railroad town in 1904 and incorporated on March 15, 1905. It covers about 36.6 square miles at an elevation of 4,413 feet.</p>"
"<p>In 1904 the Southern Pacific Railroad built a switch yard and maintenance sheds there after moving its division point from Wadsworth. The company gave its employees a 50-by-140-foot lot for $1 and offered to move houses from Wadsworth for free. The town was first called Harriman and then renamed for John Sparks, who was governor of Nevada from 1903 to 1908. Its nickname is the Rail City.</p>"
"<p>Sparks stayed small until the 1950s, when growth in Reno set off a housing boom north of the tracks. In the 1970s the area south of the railroad filled with warehouses and light industry.</p>")
sec("What are the basic facts about Sparks?",
"<table><thead><tr><th>Item</th><th>Detail</th></tr></thead><tbody>"
"<tr><td>County</td><td>Washoe County</td></tr>"
"<tr><td>Incorporated</td><td>March 15, 1905</td></tr>"
"<tr><td>Total area</td><td>About 36.6 square miles</td></tr>"
"<tr><td>Elevation</td><td>4,413 feet</td></tr>"
"<tr><td>Population, 2020 census</td><td>108,445</td></tr>"
"<tr><td>Rank in Nevada</td><td>Fifth most populous city</td></tr>"
"<tr><td>ZIP codes</td><td>89431, 89434, 89437</td></tr>"
"<tr><td>Area code</td><td>775</td></tr>"
"<tr><td>City government</td><td>Council-manager</td></tr>"
"</tbody></table>"
"<p>Sparks is part of the Reno-Sparks metropolitan area, and the two cities share a valley, a school district and a bus system.</p>")
sec("What does Sparks weather mean for a house?",
"<p>Sparks has a semi-arid, cold desert climate with wide daily temperature swings. The average January high is 48.2 degrees and the average low is 24.7. The average July high is 92.1 degrees and the average low is 55.4. There are about 59.5 days a year with highs of 90 or more and about 140.6 days with lows at or below freezing.</p>"
"<p>Average precipitation is 8.38 inches a year, spread over about 45 days with measurable precipitation. Average snowfall is 6.8 inches, though the snowiest month on record, February 2010, brought 14 inches. The record low is minus 19 degrees and the record high is 108.</p>"
"<ul><li>With roughly 140 freezing nights a year, pipe insulation and exterior faucets matter</li>"
"<li>Snow and ice management falls on the owner, because the city says the homeowner must keep the sidewalk in front of the house clear</li>"
"<li>Weeds on private property are limited to 8 inches, which matters on a vacant house over the summer</li></ul>")
sec("Which employers anchor the Sparks economy?",
"<p>Sparks combines aerospace, manufacturing, warehousing and casino employment. Sierra Nevada Corporation, an aerospace and defense contractor, has its headquarters in the city, and in 2024 the Air Force awarded it a $13 billion contract to develop a successor to the E-4B command post aircraft. Haws Corporation makes drinking fountains at a 210,000-square-foot plant, and NevadaNano develops gas sensors.</p>"
"<p>Tesla's Gigafactory Nevada, in neighboring Storey County, employed about 11,000 people in 2025, and many of them live in Sparks. The Nugget Casino Resort, finished as a high-rise in 1984, is the city's only high-rise casino. South of Interstate 80, the Union Pacific rail yard sits at the center of the industrial park.</p>"
"")
sec("What do Sparks schools, roads and transit look like?",
"<p>The Washoe County School District runs public schools in Sparks. High schools include Edward C. Reed, Sparks, Spanish Springs and Hug, and middle schools include Sky Ranch, Sparks, Mendive, Dilworth and Yvonne Shaw.</p>"
"<p>Interstate 80 runs east and west through central Sparks. Major north-south streets include Pyramid Way, El Rancho Drive, Sullivan Lane, Rock Boulevard, Sparks Boulevard, Vista Boulevard and McCarran Boulevard. The Southeast Connector, a 5.5-mile expressway, links Sparks to south Reno. The Regional Transportation Commission operates buses serving Reno and Sparks, and Reno-Tahoe International Airport is nearby. Passenger rail service at the Sparks Amtrak station ended in 2009, although the California Zephyr continues to stop in Reno.</p>"
"<p>Victorian Square, an events district downtown, grew out of a redevelopment effort that began in the early 1980s. The Sparks Marina Park is built around a natural aquifer.</p>")
sec("What city rules can affect a Sparks sale?",
"<p>The Sparks Code Enforcement Department enforces the zoning ordinance and related parts of the municipal code. It is separate from the Building and Fire departments. The things it handles include:</p>"
"<ul><li>Weeds on private property, with a maximum height of 8 inches</li>"
"<li>Signs, including signs in the public right-of-way</li>"
"<li>Garage sales, which may not exceed 72 hours or happen at the same location more than twice in any six-month period</li>"
"<li>Disabled vehicles and blight such as old furniture, car parts and appliances</li>"
"<li>Parking on unpaved areas, RV storage and illegal dumping</li>"
"<li>Home occupation permits and temporary use permits</li></ul>"
"<p>The number for the department is (775) 353-4063, and Title 7 of the Sparks Municipal Code, Property Preservation, sets ground cover requirements. If you are cleaning out an inherited or tenant-occupied house before a sale, old furniture, car parts and appliances sit on the city's blight list, and dumping is enforced separately. Signs are not allowed in the public right-of-way, so keep any for-sale signs on the lot.</p>")
sec("What does Nevada require when you sell a house in Sparks?",
"<p>Sparks sellers must follow the same state rules as everyone else, starting with the seller's real property disclosure form. Under NRS 113.130, the seller completes the form and it must be served on the buyer at least 10 days before conveyance. This applies to a cash sale. Foreclosure sales, sales between close relatives and certain fiduciary sales are exempt.</p>"
"<p>Real property transfer tax in Washoe County is $2.05 per $500 of value. A $375,000 sale carries $1,537.50, which is 750 units at $2.05. The Recorder collects the tax when the deed is recorded, and a Declaration of Value form accompanies the deed. The state says buyer and seller are responsible together for the tax, so decide in the contract who pays.</p>"
"<p>If the house is in a homeowners association, NRS 116.4109 requires you to provide the buyer a resale package. The statute allows the association to charge for the certificate, with a cap set in the statute and adjusted for inflation, and lets the buyer cancel for five calendar days after receiving the package.</p>")
sec("How are Sparks property taxes billed and appealed?",
"<p>Washoe County, not the city, bills and collects the property tax on Sparks houses. The county's fiscal year runs from July 1 through June 30, and July 1 is the lien date. The Treasurer mails bills by August 1, and for 2026-27 the installments are due August 17, October 5, January 4 and March 1.</p>"
"<p>The Assessor mails value notices by December 18, and a Sparks owner who disagrees can appeal to the County Board of Equalization by January 15. For a primary residence, the 3 percent tax cap applies to the tax bill rather than the assessed value. When ownership changes, the Assessor sends an affidavit, and the property sits at a higher cap until a qualifying one is returned. A buyer should know that before closing, and you can mention it in the contract.</p>"
"<p>Unpaid taxes become delinquent, and the county advertises such parcels. Owners have two years from the lien filing to redeem. Ask the Treasurer for a balance at (775) 328-2510.</p>")
sec("How does selling a Sparks house for cash work?",
"<p>A cash offer takes lender approval out of the sale, so what remains is title work, your disclosure form and recording the deed with the Washoe County Recorder. We buy Sparks houses as-is, so you do not need to clear out yard blight or repair a roof first, but open code notices should be resolved or disclosed. There are no commissions or closing costs charged to you on our side, and you can decline the offer without owing anything.</p>")
faqs=[
("How big is Sparks and how many people live there?","Sparks covers about 36.6 square miles and had 108,445 residents in the 2020 census, with the Census Bureau estimating 111,902 as of July 1, 2025. It is the fifth most populous city in Nevada."),
("Who handles code enforcement in Sparks?","The City of Sparks Code Enforcement Department, at (775) 353-4063. It covers weeds, signs, garage sales, disabled vehicles, blight, RV storage and illegal dumping. Building and fire code questions go to separate departments."),
("What is the transfer tax when I sell a house in Sparks?","Sparks is in Washoe County, where the rate is $2.05 per $500 of value. A $375,000 sale carries $1,537.50 of tax. The County Recorder collects it at recording, and both buyer and seller are liable under state guidance."),
("Do I need to disclose problems on a cash sale in Sparks?","Yes. NRS 113.130 requires a completed disclosure form at least 10 days before conveyance, with exceptions for foreclosure sales, close relatives and certain fiduciaries. You must update the buyer in writing if you discover a new defect before closing."),
("When can I appeal my Washoe County assessment?","Appeals to the County Board of Equalization are due by January 15. The County Board decision can be appealed to the State Board of Equalization by March 10."),
("Who pays Sparks property tax, the city or the county?","The county bills it. The Washoe County Treasurer sends bills by August 1, and installments for 2026-27 are due August 17, October 5, January 4 and March 1."),
]
src=[
("Wikipedia: Sparks, Nevada","https://en.wikipedia.org/wiki/Sparks,_Nevada"),
("City of Sparks: Code Enforcement","https://www.sparksnv.gov/government/departments/community_services/code_enforcement/index.php"),
("Washoe County Recorder: Real Property Transfer Tax","https://www.washoecounty.gov/recorder/real_property_transfer_tax.php"),
("Nevada Department of Taxation: Real Property Transfer Tax FAQs","https://tax.nv.gov/faqs/real-property-transfer-tax-faqs/"),
("Justia: NRS 113.130","https://law.justia.com/codes/nevada/chapter-113/statute-113-130/"),
("Justia: NRS 116.4109","https://law.justia.com/codes/nevada/chapter-116/statute-116-4109/"),
("Washoe County Treasurer: Billing Information","https://www.washoecounty.gov/treas/Billing.php"),
("Washoe County Assessor: Important Dates","https://www.washoecounty.gov/assessor/ImportantDates.php"),
("Washoe County Assessor: Tax Cap/Abatement","https://www.washoecounty.gov/assessor/taxcap/index.php"),
]
json.dump({"slug":"sell-my-house-fast-sparks-nv","sections":S,"faqs":[{"q":q,"a":a} for q,a in faqs],"sources":[{"title":t,"url":u} for t,u in src]},open('/home/claude/chb-pages/gen/rw/sell-my-house-fast-sparks-nv.json','w'),indent=1)
wc=lambda h: len(re.sub(r'<[^>]+>',' ',h).split())
print(sum(wc(s['h2'])+wc(s['html']) for s in S)+sum(wc(q)+wc(a) for q,a in faqs))
