import json,re
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("Where is Reno and what is it known for?",
"<p>Reno is the county seat and largest city of Washoe County, in northwest Nevada along the California border. It sits in the Truckee River valley on the eastern side of the Sierra Nevada, about 23 miles northeast of Lake Tahoe, at an elevation near 4,400 feet.</p>"
"<p>The city is named for Union Major General Jesse L. Reno. For much of the twentieth century it drew people who came for Nevada's divorce laws, and it was the state's largest city until the 1960 census showed Las Vegas ahead. Today it is the home of the University of Nevada, Reno, and a gaming and tourism center. The 2020 census counted 264,165 residents.</p>"
"<p>Downtown Reno and Sparks share a valley called the Truckee Meadows. The Reno-Sparks metro area covers Washoe, Lyon and Storey counties.</p>")
sec("What does Reno's weather mean for a house?",
"<p>Reno has a cold semi-arid climate with moderately cold winters and hot summers, so a house here deals with freezing temperatures, wind and dry heat in the same year. The temperature reaches or falls below freezing on 122 days a year, and there are about 65 days with highs of 90 degrees or more. The record low is minus 17 degrees and the record high is 108 degrees.</p>"
"<p>Most precipitation comes in fall, winter and spring. Western parts of the city can get three to four times as much as areas to the east. Summer thunderstorms can occur from April to October, and the region is windy throughout the year.</p>"
"<ul><li>Freeze and thaw cycles put stress on pipes, hose bibs and exterior paint</li>"
"<li>Wind and temperature swings wear roofing and fencing</li>"
"<li>Western neighborhoods see much more precipitation than eastern ones</li></ul>"
"<p>A seller who has put off maintenance on any of these is not obliged to fix it before a cash sale, but known defects go on the Nevada disclosure form.</p>")
sec("How much wildfire and earthquake risk does Reno have?",
"<p>Wildfire is the most serious hazard for Reno houses, particularly on the southwest side. Roughly 80 percent of homes in the area carry some risk of being affected by a wildfire.</p>"
"<table><thead><tr><th>Event</th><th>What happened</th></tr></thead><tbody>"
"<tr><td>November 2011 Caughlin fire</td><td>Powerline arcing started a fire in southwest Reno that destroyed 26 homes</td></tr>"
"<tr><td>January 2012 Washoe Drive fire</td><td>Fireplace ashes started a fire that destroyed 29 homes; about 10,000 people were evacuated</td></tr>"
"<tr><td>September 2024 Davis Fire</td><td>Burned forested areas of southwest Reno; 14 structures burned and about 20,000 people were evacuated</td></tr>"
"<tr><td>February 2008 earthquake swarm</td><td>Largest event about magnitude 4.9, centered near Somersett, Mogul and Verdi; many homes were damaged</td></tr>"
"</tbody></table>"
"<p>Wikipedia's Washoe County article also calls the county wildfire prone, with the risk concentrated in southern Reno and just outside the city limits. If your house is near a forested edge, say so on the disclosure form.</p>")
sec("Who are the biggest employers in Reno?",
"<p>Education, health care and casinos lead the list. According to Reno's 2025 annual financial report, as summarized by Wikipedia, the city's top employers are as follows.</p>"
"<ul><li>Washoe County School District, about 7,500 employees</li>"
"<li>Renown Regional Medical Center, about 7,500</li>"
"<li>Peppermill Reno, Grand Sierra Resort, Saint Mary's Regional Medical Center, Eldorado Resort Casino, Silver Legacy, University of Nevada, Reno, U-Haul Holding Company and Circus Circus Reno, about 3,000 each</li></ul>"
"<p>Outside the city limits, the Tesla Gigafactory at the Tahoe Reno Industrial Center employs roughly 11,000 people, which is more than any single employer in Reno. Data centers at the same industrial center and at Reno Technology Park, along with distribution facilities for Amazon, Walmart and PetSmart, have widened the region's economy beyond gaming. Ormat Technologies, a geothermal company, is headquartered in Reno.</p>"
"")
sec("How do roads, transit and schools serve Reno homes?",
"<p>Interstate 80 runs through downtown Reno, and US 395 and Interstate 580 are the main north-south route. The Regional Transportation Commission of Washoe County runs the bus system, with its main terminal on 4th Street downtown. Amtrak's California Zephyr stops at Reno station, and Reno-Tahoe International Airport is the second busiest commercial airport in Nevada.</p>"
"<p>The Washoe County School District serves the whole county. The University of Nevada, Reno, founded as a state college in 1886 and now enrolling about 21,000 students, anchors the north side of downtown. Truckee Meadows Community College has about 13,000 students.</p>")
sec("What city rules can affect a Reno sale?",
"<p>The City of Reno enforces property maintenance through its Code Enforcement department, and an unresolved violation can be recorded against your house. The Reno Municipal Code covers things such as inoperable vehicles, trash and debris, overgrown landscaping, work done without permits and zoning violations.</p>"
"<p>The process goes in steps:</p>"
"<ul><li>A warning of violation letter gives a compliance date, generally about 30 days</li>"
"<li>If the problem remains, an administrative citation follows: $100 for the first, $250 for the second, $500 for the third on residential property</li>"
"<li>A notice of intent to record can lead to a recorded notice of violation lien with the Washoe County Recorder</li>"
"<li>The lien is released only after the problem is fixed and all fines and fees are paid</li></ul>"
"<p>Owners may appeal through the City Clerk's office, and the city says code officers cannot waive or reduce fines. Complaints and questions go to Reno Direct at 775-334-4636. Other rules sellers run into: vehicles cannot be parked in the front yard, inoperable vehicles must be screened, and items such as couches, mattresses and appliances cannot be stored in view in a front or side yard. Clear these before photos or a walkthrough, and check whether a lien is already recorded.</p>"
"<p>The city adopted its 2024 building codes on July 1, 2025. If you are finishing unpermitted work before a sale, ask Building about permit status first.</p>")
sec("What does Nevada require from a Reno seller?",
"<p>A Reno seller must complete the state disclosure form at least 10 days before conveyance, and the rule does not exempt cash sales. NRS 113.130 says the seller, not the agent, completes it, and that the buyer cannot waive it. Exceptions include foreclosure sales, sales between spouses or close relatives, and certain sales by fiduciaries such as trustees and personal representatives.</p>"
"<p>Washoe County adds $0.10 to the statewide real property transfer tax rate, so the rate is $2.05 per $500 of value. On a $450,000 sale that is $1,845. The Recorder collects it when the deed is recorded. A Declaration of Value form must accompany any document that transfers title. The basis is the sale price or the estimated fair market value, which comes from the assessor's taxable value or a prior purchase price within the last five years, whichever is higher. The Property Transfer Compliance Recorder takes questions at (775) 328-3661. Under state guidance both buyer and seller are liable for the tax, so your contract should say who pays.</p>"
"<p>Homeowners association sales require the resale package described in NRS 116.4109, and the buyer has five calendar days after receiving it to cancel.</p>")
sec("How does Washoe County property tax work for a Reno seller?",
"<p>The Washoe County Treasurer bills property tax. Bills go out by August 1, and the 2026-27 installments fall on August 17, October 5, January 4 and March 1. A parcel with more than $100 of tax can pay in four installments. Delinquent property is advertised and owners have two years from the lien filing to redeem it.</p>"
"<p>The Assessor handles values and a tax cap. Nevada's 2005 law, Assembly Bill 489, caps the increase in the tax bill, not the assessed value, at 3 percent on a primary residence, with a higher cap on other property. After a change of ownership the Assessor mails an affidavit, and until a qualifying one is filed the status stays at the higher cap. That is a point to raise with a buyer. Appeals of value go to the County Board of Equalization by January 15.</p>")
sec("How does selling a Reno house for cash work?",
"<p>A cash purchase skips lender underwriting, so the timeline is driven by title work and the recording step at the Washoe County Recorder. You can ask for an offer with only the address and a description of condition, and we do not charge fees or commissions. If you decline the offer you owe nothing.</p>"
"<p>Expect to provide the disclosure form, clear any recorded code liens, and confirm the tax status. We buy Reno houses as-is, including houses with deferred maintenance, tenants or probate issues.</p>")
faqs=[
("Is Reno at risk of wildfire?","Yes. Wikipedia's Reno article says roughly 80 percent of homes in the area have some risk, and the Davis Fire in September 2024 burned 14 structures and led to about 20,000 evacuations. Southwest Reno carries the most risk."),
("What is the transfer tax on a Reno home sale?","Washoe County's rate is $2.05 per $500 of value, which is the $1.95 statewide rate plus $0.10. A $450,000 sale carries $1,845. The County Recorder collects it at recording, and the buyer and seller are both liable under state guidance."),
("Can Reno code enforcement put a lien on my house?","Yes. After warnings and citations, the city can record a notice of violation lien with the Washoe County Recorder. It is released only after the violation is fixed and all fines and fees are paid. Residential citations are $100, $250 and $500 on the escalating scale."),
("Do I have to make repairs before a cash sale in Reno?","No repair is required by the sale itself. You must disclose known defects on the Nevada seller's disclosure form at least 10 days before conveyance, and open code violations or unpermitted work are worth raising with the buyer."),
("When is the Washoe County appeal deadline?","Appeals to the County Board of Equalization must be filed by January 15, or the next business day if that date falls on a weekend or holiday. A decision can be appealed to the State Board of Equalization by March 10."),
("Does the Nevada disclosure rule apply to cash sales?","Yes. NRS 113.130 applies to residential property whatever the financing, with specific exceptions such as foreclosure sales and sales between close relatives."),
]
src=[
("Wikipedia: Reno, Nevada","https://en.wikipedia.org/wiki/Reno,_Nevada"),
("Wikipedia: Washoe County, Nevada","https://en.wikipedia.org/wiki/Washoe_County,_Nevada"),
("City of Reno: Code Enforcement","https://www.reno.gov/government/departments/code-enforcement/"),
("City of Reno: Building Permits","https://www.reno.gov/business-development/development-services/building-permits.php"),
("Washoe County Recorder: Real Property Transfer Tax","https://www.washoecounty.gov/recorder/real_property_transfer_tax.php"),
("Nevada Department of Taxation: Real Property Transfer Tax FAQs","https://tax.nv.gov/faqs/real-property-transfer-tax-faqs/"),
("Justia: NRS 113.130","https://law.justia.com/codes/nevada/chapter-113/statute-113-130/"),
("Justia: NRS 116.4109","https://law.justia.com/codes/nevada/chapter-116/statute-116-4109/"),
("Washoe County Treasurer: Billing Information","https://www.washoecounty.gov/treas/Billing.php"),
("Washoe County Assessor: Tax Cap/Abatement","https://www.washoecounty.gov/assessor/taxcap/index.php"),
("Washoe County Assessor: Important Dates","https://www.washoecounty.gov/assessor/ImportantDates.php"),
]
json.dump({"slug":"sell-my-house-fast-reno-nv","sections":S,"faqs":[{"q":q,"a":a} for q,a in faqs],"sources":[{"title":t,"url":u} for t,u in src]},open('/home/claude/chb-pages/gen/rw/sell-my-house-fast-reno-nv.json','w'),indent=1)
wc=lambda h: len(re.sub(r'<[^>]+>',' ',h).split())
print(sum(wc(s['h2'])+wc(s['html']) for s in S)+sum(wc(q)+wc(a) for q,a in faqs))
