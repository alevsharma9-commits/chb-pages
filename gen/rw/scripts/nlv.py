import json,re,sys
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("Where is North Las Vegas and how did it become a city?",
"<p>North Las Vegas is a suburban city in Clark County that sits northeast of Las Vegas in the Mojave Desert. It covers about 101 square miles and is the fourth most populous city in Nevada.</p>"
"<p>The town began in 1919, when Thomas L. Williams moved his family onto a 160-acre piece of land about a mile from Las Vegas and started building wells, roads and irrigation ditches. Workers from the Hoover Dam project settled there between 1928 and 1935. The city was incorporated on May 1, 1946. Locals still use the nicknames Old Town and North Town.</p>"
"<p>Newer parts of the city include the master-planned communities of Aliante and Eldorado, so a house here can be anything from an older lot near the original townsite to a recent subdivision home.</p>")
sec("What are the basic facts about North Las Vegas?",
"<p>The table below pulls together the figures a seller is most likely to be asked about. Population history comes from the decennial census, with the 2025 figure being the Census Bureau estimate.</p>"
"<table><thead><tr><th>Item</th><th>Detail</th></tr></thead><tbody>"
"<tr><td>Incorporated</td><td>May 1, 1946</td></tr>"
"<tr><td>County</td><td>Clark County</td></tr>"
"<tr><td>Total area</td><td>About 101 square miles</td></tr>"
"<tr><td>Elevation</td><td>2,205 feet</td></tr>"
"<tr><td>Population, 2000</td><td>115,488</td></tr>"
"<tr><td>Population, 2010</td><td>216,961</td></tr>"
"<tr><td>Population, 2020</td><td>262,527</td></tr>"
"<tr><td>ZIP codes</td><td>89030 to 89033, 89036, 89081, 89084 to 89087</td></tr>"
"<tr><td>City government</td><td>Council-manager, a mayor and four council members</td></tr>"
"</tbody></table>"
"<p>Growth is the main story. The city roughly doubled between 2000 and 2010, then kept adding residents through 2020.</p>")
sec("What does the desert climate mean for a North Las Vegas house?",
"<p>North Las Vegas has a desert climate, so heat is the main stress on a house here. Mean daily highs reach about 105 degrees in July, and the record high is 119 degrees. Average yearly precipitation is only about 4.6 inches.</p>"
"<p>Winters are mild during the day, but nights often fall below freezing, and snow shows up only once every few years. In summer, monsoon storms can bring heavy rain and thunderstorms.</p>"
"<p>Items buyers and inspectors tend to look at first in this climate:</p>"
"<ul><li>The age and condition of the air conditioning system, since it runs for most of the year</li>"
"<li>Roof membranes and tile, which take direct sun for months</li>"
"<li>Block walls and fences, which the city lists as a code enforcement concern when they are damaged</li></ul>"
"<p>You do not have to repair any of this to sell for cash, but you do have to disclose what you know.</p>")
sec("Who employs people in North Las Vegas?",
"<p>The local economy leans on warehousing, distribution and manufacturing. Amazon opened an 850,000-square-foot fulfillment center in the city on May 12, 2019, and it employs more than 1,500 people. Sephora opened a 715,000-square-foot distribution center in October 2019.</p>"
"<p>Bigelow Aerospace is headquartered in North Las Vegas, and the Apex Industrial Park is now part of the city. In June 2024, PCM Railone AG announced a production facility for concrete ties and a North American headquarters in the city, tied to the Brightline West high-speed rail project. The Clark County School District is also a major employer across the county.</p>"
"")
sec("Which schools, roads and services serve North Las Vegas homes?",
"<p>Public schools are run by the Clark County School District, which the Wikipedia article on the city describes as the fifth largest in the country. High schools inside North Las Vegas include Canyon Springs, Cheyenne, Legacy, Mojave and Rancho. The Cheyenne Campus of the College of Southern Nevada is also in the city.</p>"
"<p>The city itself provides police and fire protection, parks and recreation, and water and wastewater service. It maintains 34 parks on more than 475 acres of developed park land. RTC Transit runs buses across the Las Vegas area, and North Las Vegas Airport, established on December 7, 1941, handles tour flights.</p>"
"")
sec("What city rules can slow a North Las Vegas sale?",
"<p>Open code enforcement problems and short-term rental permits are the two local rules that most often complicate a sale. Both are handled at the city level, not by Clark County.</p>"
"<p>The Code Enforcement Division says it focuses on the following problems:</p>"
"<ul><li>Boarding and securing vacant structures</li>"
"<li>Junk, litter, garbage and overgrown weeds</li>"
"<li>Junk vehicles and illegally posted signs</li>"
"<li>Illegal home businesses</li>"
"<li>Obstructed streets or sidewalks and damaged fences or block walls</li></ul>"
"<p>The division aims for voluntary compliance through notices and education, and it can abate nuisances or issue criminal citations when that fails. The city has an appeal and hearing process. Clear any open case before closing or tell the buyer about it.</p>"
"<p>Short-term rentals need more. The city adopted Ordinance 3127 in June 2022, and an owner must win a Conditional Use Permit before applying for a business license. The application requires a notarized letter from the homeowners association, a 660-foot separation from other short-term rentals and a 2,500-foot separation from resort hotels. Planning and Zoning answers questions at (702) 633-1537.</p>")
sec("What does Nevada require when you sell a house in North Las Vegas?",
"<p>Nevada requires the seller to complete a disclosure form at least 10 days before the property is conveyed, and that duty applies to a cash sale as well. Under NRS 113.130, the seller completes the form and the seller or the agent serves it on the buyer or the buyer's agent. An agent may not fill it out for you. If you later find a new defect, or learn that a listed defect got worse, you must tell the buyer in writing before closing.</p>"
"<p>The statute lists exceptions, including sales by foreclosure, sales between co-owners, spouses or close relatives, the first sale of a house built by a licensed contractor, and certain sales by fiduciaries such as a personal representative or trustee. A buyer cannot waive the requirement.</p>"
"<p>Real property transfer tax is the other fixed cost. In Clark County the rate is $2.55 per $500 of value, which is the statewide $1.95 plus a $0.60 Clark County add-on, according to the Nevada Department of Taxation. On a sale at $400,000, that works out to $2,040. The tax is collected by the County Recorder when the deed is recorded, and the state says the buyer and the seller are responsible together and individually. Who actually pays is a matter for the purchase contract. Exemptions under NRS 375.090 include a transfer between former spouses under a divorce decree and a deed that takes effect on death.</p>"
"<p>If the house is in a homeowners association, the owner must furnish a resale package under NRS 116.4109. It includes the governing documents, a statement of unpaid assessments and fines, and the budget. The buyer can cancel until midnight of the fifth calendar day after receiving it.</p>")
sec("How are property taxes handled when a North Las Vegas house sells?",
"<p>The Clark County Treasurer bills real property tax once a year, and taxes are due the third Monday in August. If the bill is more than $100, you may pay in four installments. Those are the third Monday in August, and the first Mondays in October, January and March. The payments are not quarterly.</p>"
"<p>Payment must arrive within 10 days of the due date to avoid a penalty. For one late installment the penalty is 4 percent of the installment. Unpaid taxes at the end of April are advertised as delinquent, and if the amount is still owed on the first Monday in June, the county holds the property for a two-year redemption period, with interest at 10 percent a year.</p>"
"<p>If you are behind, ask the Treasurer for a payoff figure early. The office is at 500 S Grand Central Pkwy, phone (702) 455-4323, open Monday through Thursday.</p>")
sec("How does a cash sale of a North Las Vegas house work?",
"<p>A cash sale replaces the lender with the buyer's own funds, which removes the loan approval and most of the appraisal delay. Everything else on the Nevada side still applies: the disclosure form, the recorded deed, the transfer tax and any association paperwork.</p>"
"<p>Typical steps run in this order:</p>"
"<ul><li>You send the address and condition of the house and receive a written offer</li>"
"<li>A title company opens escrow and searches for liens, unpaid taxes and judgments</li>"
"<li>You complete the Nevada seller's disclosure and any HOA package</li>"
"<li>The deed is signed and recorded with the Clark County Recorder, with a Declaration of Value</li>"
"<li>Payoffs and fees are paid from proceeds and you receive the balance</li></ul>"
"<p>We buy North Las Vegas houses as-is. We cannot promise a price before we see the property, and you are free to compare our written offer with a listing.</p>")
faqs=[
("Do I have to disclose problems if I sell my North Las Vegas house for cash?","Yes. NRS 113.130 requires the seller to complete a disclosure form at least 10 days before the property is conveyed, and the exceptions do not include cash sales. You only have to disclose defects you know about, and you must update the buyer in writing if you learn of a new one before closing."),
("How much is the transfer tax on a North Las Vegas sale?","In Clark County the rate is $2.55 per $500 of value, which is $1.95 statewide plus $0.60 for Clark County. A $400,000 sale would carry $2,040 of tax. The County Recorder collects it when the deed is recorded, and the contract decides who pays."),
("Can a North Las Vegas buyer turn my house into a short-term rental?","Only with a Conditional Use Permit from the city, which must come before a business license. The application needs a 660-foot separation from other short-term rentals, a 2,500-foot separation from resort hotels and a notarized letter from the HOA where one applies."),
("What happens if code enforcement has an open case on my house?","Code Enforcement can abate a nuisance or issue citations when notices are ignored. You can appeal through the city. Resolve the case before closing where you can, and tell the buyer about anything still open."),
("When are Clark County property taxes due?","Taxes are due the third Monday in August. If the bill exceeds $100 you can pay in installments on the third Monday in August and the first Mondays in October, January and March. Late payments carry penalties, starting at 4 percent for one late installment."),
("Does my HOA have to give the buyer documents when I sell?","Yes. NRS 116.4109 requires a resale package with the governing documents, a statement of what you owe, the budget and pending legal actions. The buyer may cancel within five calendar days of receiving it, and the association must respond to your written request within 10 calendar days."),
]
src=[
("Wikipedia: North Las Vegas, Nevada","https://en.wikipedia.org/wiki/North_Las_Vegas,_Nevada"),
("City of North Las Vegas: Code Enforcement","https://www.cityofnorthlasvegas.com/residents/code-enforcement"),
("City of North Las Vegas: Short-Term Rentals","https://www.cityofnorthlasvegas.com/business/short-term-rentals"),
("Nevada Department of Taxation: Real Property Transfer Tax FAQs","https://tax.nv.gov/faqs/real-property-transfer-tax-faqs/"),
("Clark County Recorder: Declaration of Value packet","https://www.clarkcountynv.gov/assets/documents/government/elected_officials/county_recorder/dv-packet.pdf"),
("Justia: NRS 113.130","https://law.justia.com/codes/nevada/chapter-113/statute-113-130/"),
("Justia: NRS 116.4109","https://law.justia.com/codes/nevada/chapter-116/statute-116-4109/"),
("Clark County Treasurer: Real Property Tax Information","https://www.clarkcountynv.gov/government/elected_officials/county_treasurer/real-property-tax-information"),
]
json.dump({"slug":"sell-my-house-fast-north-las-vegas-nv","sections":S,"faqs":[{"q":q,"a":a} for q,a in faqs],"sources":[{"title":t,"url":u} for t,u in src]},open('/home/claude/chb-pages/gen/rw/sell-my-house-fast-north-las-vegas-nv.json','w'),indent=1)
def wc(h): return len(re.sub(r'<[^>]+>',' ',h).split())
n=sum(wc(s['h2'])+wc(s['html']) for s in S)+sum(wc(q)+wc(a) for q,a in faqs)
print(n)
