import json,re
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("How is Delaware laid out for a home seller?",
"<p>Delaware is a small state with three counties, and each one runs its own tax office, recorder and assessment process. From north to south they are New Castle, Kent and Sussex, so the first question for any seller is which county the house sits in.</p>"
"<p>According to Wikipedia, Dover is the capital and Wilmington is the largest city. The northern tip sits on the Piedmont Plateau, with hills and rolling surfaces. The Atlantic Seaboard fall line roughly follows the Robert Kirkwood Highway between Newark and Wilmington, and south of it lies the flat, sandy and in places swampy Atlantic Coastal Plain. Delaware was the first state to ratify the Constitution, on December 7, 1787.</p>"
"<p>For a seller, the geography decides the paperwork more than the terrain does. The county holds the deed, the tax account and the assessment, and a house on the coastal plain is billed by a different office than a house on the Piedmont. A buyer who pays cash and takes the house as-is does not need the seller to make repairs, but the owner still has to know what the county will want at closing.</p>")
sec("What does the Delaware economy mean for sellers?",
"<p>Delaware's economy leans on corporate law, finance, chemicals and science, farming and beach tourism. Wikipedia says over half of New York Stock Exchange-listed corporations and over three-fifths of the Fortune 500 are legally incorporated in the state.</p>"
"<ul>"
"<li>Banking names include Bank of America, M&amp;T Bank, JPMorgan Chase, Citigroup and Deutsche Bank.</li>"
"<li>Chemical, pharmaceutical and technology employers include DuPont de Nemours, AstraZeneca, Syngenta and Agilent Technologies.</li>"
"<li>Agricultural output consists of poultry, nursery stock, soybeans, dairy products and corn.</li>"
"<li>Delaware's beaches generate $6.9 billion annually and over $711 million in tax revenue, according to SeaGrant Delaware as quoted on Wikipedia.</li>"
"</ul>"
"<p>Tourism alone generated $3.1 billion in 2015, which Wikipedia says made up five percent of the state's GDP. We do not publish price figures for any town on this page.</p>")
sec("What do the Census numbers say about Delaware housing?",
"<p>Delaware has just over one million residents and about 402,000 households. Nearly three in four households own their homes.</p>"
"<table><thead><tr><th>Measure</th><th>Delaware</th></tr></thead><tbody>"
"<tr><td>Population estimate, July 1, 2025</td><td>1,059,952</td></tr>"
"<tr><td>Population change, April 2020 to July 2025</td><td>7.1%</td></tr>"
"<tr><td>Households, 2020 to 2024</td><td>402,038</td></tr>"
"<tr><td>Persons per household, 2020 to 2024</td><td>2.48</td></tr>"
"<tr><td>Median household income, 2020 to 2024</td><td>$84,954</td></tr>"
"<tr><td>Mean travel time to work</td><td>26.0 minutes</td></tr>"
"<tr><td>Land area</td><td>1,948.55 square miles</td></tr>"
"<tr><td>Building permits, 2025</td><td>6,468</td></tr>"
"</tbody></table>"
"<p>Source: U.S. Census Bureau QuickFacts. The Census Bureau also reports a population density of 508 people per square mile for 2020, and 22.8% of residents are 65 or older.</p><p>The same table puts the median value of owner-occupied housing units at $352,000 for 2020 to 2024. Median selected monthly owner costs are $1,816 with a mortgage and $562 without one. Those are statewide medians and say nothing about any single house or town.</p>")
sec("How does Delaware property tax work across the three counties?",
"<p>Each county assesses, levies and collects its own property tax, and the dates differ. The statutes are in Title 9 of the Delaware Code.</p>"
"<table><thead><tr><th>County</th><th>Assessment roll open by</th><th>County tax levied by</th><th>Tax due</th><th>Collecting authority</th></tr></thead><tbody>"
"<tr><td>New Castle</td><td>March 1</td><td>June 1</td><td>July 1</td><td>Chief Financial Officer</td></tr>"
"<tr><td>Kent</td><td>April 1</td><td>June 30</td><td>June 1</td><td>Receiver of Taxes and County Treasurer</td></tr>"
"<tr><td>Sussex</td><td>February 15</td><td>July 1</td><td>July 1</td><td>Director of Finance</td></tr>"
"</tbody></table>"
"<p>The assessment dates are from 9 Del. C. Chapter 83, the levy dates from Chapter 80 and the due dates and collecting authorities from Chapter 86. Counties mail the bill within 30 days after taxes are due, and the statute says a missed bill does not excuse late payment.</p>"
"<p>A lien matters at sale. Under Chapter 87, county taxes continue as a lien for 10 years from July 1 of the levy year, and longer if the same owner still holds the property. In Kent and Sussex the statute says the lien has priority over all other liens.</p>")
sec("How do I challenge a Delaware assessment?",
"<p>Start with the county. In Sussex County, the Board of Assessment Review hears appeals from March 1 through May 31, or until all appeals are heard in a reassessment year, and appointments are made through the county Assessment Division.</p>"
"<p>The Board decides whether the assessment is correct after hearing the owner. If it finds an error, it orders the Director of Finance to correct it. New Castle and Kent have their own boards and schedules, so check the county's assessment office for current dates before you plan around a deadline.</p>"
"<p>The Board also reviews the methods the Director of Finance used to set assessments and can recommend improvements to the County Administrator. An owner who plans to sell should ask for a copy of the current assessment before the contract is signed, so any dispute is on the record.</p>")
sec("What does Delaware's realty transfer tax cost, and who pays?",
"<p>The combined realty transfer tax is 4% of value, made up of 2.5% for the state and 1.5% for the county or municipality. The Division of Revenue's instructions say the tax is split equally between grantor and grantee.</p>"
"<p>The statute is more detailed. Under 30 Del. C. 5402 the state rate is 3% unless the local government has enacted the full 1.5%, in which case it is 2.5%. A first-time home buyer's share can be reduced by one-half percent of the lesser of the value or $400,000. Section 5412 puts the burden on the grantor in the absence of a contrary agreement, and section 5404 gives the tax priority out of the proceeds of a judicial sale.</p>"
"<ul>"
"<li>Proof of payment must appear on the document before a Recorder of Deeds can record it (section 5408).</li>"
"<li>Every document must state the true, full value, or come with an affidavit explaining why it is exempt (section 5409).</li>"
"<li>A conveyance to a lender with a genuinely defaulted mortgage, by sheriff's sale or deed in lieu, is excluded (section 5401(1)p).</li>"
"<li>Transfers between spouses, parent and child, siblings, and grandparent and grandchild are excluded.</li>"
"</ul>")
sec("What other Delaware rules affect a sale?",
"<p>The state has no estate or inheritance tax for deaths after 2017, which is covered on our estate tax page, and it has a code for residential rentals. The code requires 60 days' written notice to end a month-to-month tenancy and sends eviction cases to the Justice of the Peace Court in the county.</p>"
"<p>A few practical points follow for sellers in any county:</p>"
"<ul>"
"<li>Find out which county office holds the deed, the tax account and any open estate file.</li>"
"<li>Ask the county for the current balance, including penalties, before you sign a contract.</li>"
"<li>Collect the lease, rent roll and any notices if tenants live in the house.</li>"
"<li>Have a title company or attorney confirm what must be recorded.</li>"
"</ul>"
"<p>We buy Delaware houses for cash in any of the three counties, as-is. Local city and county guides on this site go into the details of each place, and nothing here replaces advice from a Delaware attorney or tax professional.</p>")
F=[
("How many counties does Delaware have?","Three: New Castle, Kent and Sussex. Each one assesses and collects its own property tax and has its own recorder of deeds."),
("What is the realty transfer tax in Delaware?","The combined rate is 4% of value, with 2.5% going to the state and 1.5% to the county or municipality. It is apportioned equally between buyer and seller, and the grantor bears it by default if the parties do not agree otherwise."),
("When are Delaware property taxes due?","In New Castle and Sussex Counties, July 1. In Kent County, June 1. Bills are mailed within 30 days after the due date, and not receiving one does not excuse payment."),
("Is there a Delaware estate tax?","No, not for people who died after December 31, 2017. The estate tax was repealed for those deaths, and the old inheritance tax was repealed effective January 1, 1999."),
("Where do I record a Delaware deed?","With the Recorder of Deeds in the county where the property sits. Proof that realty transfer tax was paid has to appear on the document or an exemption affidavit must accompany it."),
]
src=[("Delaware, Wikipedia","https://en.wikipedia.org/wiki/Delaware"),
("U.S. Census Bureau QuickFacts, Delaware","https://www.census.gov/quickfacts/fact/table/DE/PST045224"),
("Delaware Code Title 9, Chapter 83 (Assessment)","https://delcode.delaware.gov/title9/c083/sc01/index.html"),
("Delaware Code Title 9, Chapter 80 (County tax levy)","https://delcode.delaware.gov/title9/c080/index.html"),
("Delaware Code Title 9, Chapter 86 (Tax billing and due dates)","https://delcode.delaware.gov/title9/c086/index.html"),
("Delaware Code Title 9, Chapter 87 (Lien of taxes)","https://delcode.delaware.gov/title9/c087/sc01/index.html"),
("Delaware Code Title 9, Chapter 70 (Sussex County assessment)","https://delcode.delaware.gov/title9/c070/index.html"),
("Delaware Code Title 30, Chapter 54 (Realty transfer tax)","https://delcode.delaware.gov/title30/c054/sc01/index.html"),
("Delaware Realty Transfer Tax return instructions","https://revenuefiles.delaware.gov/2023/RTT-TAX_2021-02_Instructions.pdf"),
("Delaware Division of Revenue, Estate Tax summary (PDF)","https://financefiles.delaware.gov/docs/estate_tax.pdf"),
("Delaware Code Title 25, Chapter 51 (Landlord-Tenant general provisions)","https://delcode.delaware.gov/title25/c051/sc01/index.html")]
slug="delaware-guides-by-city-and-county"
d={"slug":slug,"sections":S,"faqs":[{"q":q,"a":a} for q,a in F],"sources":[{"title":t,"url":u} for t,u in src]}
txt=" ".join(re.sub(r'<[^>]+>',' ',s['h2']+' '+s['html']) for s in S)+" "+" ".join(q+' '+a for q,a in F)
print(len(txt.split()), '—' in txt, '–' in txt)
json.dump(d,open(f'/home/claude/chb-pages/gen/rw/{slug}.json','w'),ensure_ascii=False,indent=1)
