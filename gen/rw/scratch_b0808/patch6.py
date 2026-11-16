exec(open('patch1.py').read().split("sub('w1.py'")[0])
sub('w2.py',[
("One statewide schedule governs. Under <a href=\"@S@Chapter_161/GS_161-10.html\">G.S. 161-10</a>, a general instrument costs $26.00 for the first 15 pages plus $4.00 for each extra page, and a deed of trust or mortgage costs $64.00 for the first 35 pages plus $4.00 for each extra page.","The schedule is statewide, so Wilson County charges what every register charges. <a href=\"@S@Chapter_161/GS_161-10.html\">G.S. 161-10</a> prices an ordinary document at $26.00 and covers 15 pages in that price. A mortgage or deed of trust is priced at $64.00 with 35 pages included. Extra pages on either are $4.00 apiece."),
("Under G.S. 161-10 a certified copy costs $5.00 for the first page and $2.00 for each added page.","The statute prices a certified copy at $5.00 for page one and $2.00 for every page after it."),
("How do I get a copy of a recorded Wilson County deed?","Can I order a certified copy of a Wilson County deed?"),
("Sellers who inherited a house often need the vesting deed to prove how title reached them, so ordering a certified copy early prevents a delay in the contract period.","Heirs often need the deed that put title in the decedent's name, so order early to avoid delay in the contract period."),
("G.S. 161-10 sets $26.00 for 15 pages, then $4.00 per extra page. Deeds of trust run $64.00 for 35 pages.","An ordinary document costs $26.00 with 15 pages included, and each page past that adds $4.00. A deed of trust starts at $64.00."),
("<td>Instrument, first 15 pages</td><td>$26.00, plus $4.00 per added page</td>","<td>Ordinary instrument, 15 pages included</td><td>$26.00 base, $4.00 for each page beyond</td>"),
("<td>Deed of trust or mortgage, first 35 pages</td><td>$64.00, plus $4.00 per added page</td>","<td>Mortgage or deed of trust, 35 pages included</td><td>$64.00 base, $4.00 for each page beyond</td>"),
("<td>Certified copy</td><td>$5.00 first page, $2.00 each added page</td>","<td>Certified copy</td><td>$5.00 for page one, $2.00 per later page</td>"),
("<td>Plat</td><td>$21.00 per sheet</td>","<td>Plat</td><td>$21.00 each sheet</td>"),
("Half stays with the county and half goes to the state each month.","The county keeps half. The state receives the other half every month."),
("The seller does. The state levy is $1.00 per $500 (or part of $500) of value conveyed, and","The seller does. The state levy runs $1.00 for each $500 or fraction of value passing, and"),
("The seller, paid to the register before recording.","The seller, who pays the register before the deed is filed."),
("The office records deeds, deeds of trust","Recording covers deeds, deeds of trust") if False else ("The same office issues marriage licenses and keeps birth, death and marriage records, along with military discharges and notary oaths.","The same office issues marriage licenses and holds the county's birth, death and marriage files, plus military discharges and notary oaths."),
("reports 38,463 housing units in the county and 411 building permits in 2025, so the office handles a steady flow of deeds.","counts 38,463 housing units and 411 building permits in 2025, so deeds move through the office steadily."),
])
t=open('w3.py').read()
a=t.index('{"h2":"What about personal property');b=t.index('{"h2":"How do circuit breaker')
t=t[:a]+'''{"h2":"How has Winston-Salem grown?","html":"<p>The city's population went from 229,617 in the 2010 census to 249,545 in 2020, and Census estimates 257,271 for July 2025. With about 132.7 square miles of land, that is roughly 1,880 people per square mile in 2020.</p><p>Other QuickFacts for the city include 10,986 veterans for 2020 to 2024, a 17.7% poverty rate, and 85.3% of residents living in the same house a year earlier. Veterans in this group may qualify for the $45,000 disabled veteran exclusion if their disability meets the state test, so owners should ask the tax office about it.</p><p>Median monthly owner costs with a mortgage are $1,459, and $486 without one, which is a useful gauge of how much of a typical budget property tax and housing costs claim.</p>"},
'''+t[b:]
open('w3.py','w').write(t)
sub('w3.py',[
("What if I owe back tax on a Winston-Salem house?","What if there is back tax on a Winston-Salem house?"),
("The county can enforce through a foreclosure action in the nature of a mortgage foreclosure, with a public sale at the courthouse door, as set out in G.S. 105-374. A person redeeming before confirmation pays the taxes, penalties, interest and costs. Selling first can avoid that outcome, since the closing agent pays the amount from proceeds.","Collection can reach a court-ordered sale. Selling first avoids that, and the closing agent settles the amount from proceeds."),
(" A further appeal to the Property Tax Commission is due within 30 days after the board mails its decision (<a href=\"@S@GS_105-290.html\">G.S. 105-290</a>).",""),
("Request","Request") if False else ("Obtain the exact owed amount for the parcel from the county.","Get the exact balance for the parcel from the county."),
])
