def sub(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        a=a.replace('"','\\"'); b=b.replace('"','\\"')
        assert a in t,(f,a[:50])
        t=t.replace(a,b)
    open(f,'w').write(t)
sub('w1.py',[
("How do I appeal a Wilson County assessment?","What is the route for contesting a Wilson County value?"),
("When are Wilson County property taxes due and when do they turn delinquent?","What is the Wilson County payment deadline?"),
("up 2.4% from the April 2020 base.","a 2.4% rise since the 2020 count."),
("The pattern in the statutes is steady. Under <a href=\"@S@GS_105-322.html\">G.S. 105-322</a> the board of commissioners usually serves as the review board, meeting for the first time no earlier than the first Monday in April and no later than the first Monday in May. A further appeal goes to the Property Tax Commission within 30 days of the board's mailed decision, under <a href=\"@S@GS_105-290.html\">G.S. 105-290</a>.",
 "State law sets the outer frame: the commissioners normally sit as the review board in spring (<a href=\"@S@GS_105-322.html\">G.S. 105-322</a>), and a loser at that stage has a month to go on to the state commission (<a href=\"@S@GS_105-290.html\">G.S. 105-290</a>)."),
("Taxes are due September 1, and the county says the last day to pay is January 6, after which unpaid balances are delinquent. State law, in","Bills fall due September 1. The county's published cutoff is January 6, and balances left after it are delinquent. Under"),
(", lets payment at face amount through the day before January 6.",", payment at face amount works up to the day before January 6."),
("Interest then starts at 2% for January 6 to February 1 and runs at three-fourths of a percent per month after that.","Late interest begins at 2% for the first weeks and then climbs by three-fourths of a percent each month."),
("North Carolina offers three relief programs, and an owner can take only one. Applications go to the county tax office, not to the state, and the state's AV-9 form states a June 1 cutoff for the tax year.","Three state relief programs exist, and one owner draws on only one of them. The county tax office takes the application, and the state AV-9 form names June 1 as the cutoff."),
("<strong>Elderly or disabled exclusion:</strong> the greater of $25,000 or half the appraised value of a permanent residence, for owners 65 or older or totally and permanently disabled whose income is at or below the limit, which NCDOR prints as $38,800 for 2026.","<strong>Elderly or disabled exclusion:</strong> shelters the larger of $25,000 or half a home's appraised value for older or fully disabled owners under the income ceiling, printed by NCDOR as $38,800 for 2026."),
("<strong>Disabled veteran exclusion:</strong> the first $45,000 of value, with no age or income test, for qualifying veterans and unmarried surviving spouses.","<strong>Disabled veteran exclusion:</strong> removes $45,000 of value for qualifying veterans, with no age or income test."),
("<strong>Circuit breaker:</strong> tax capped at 4% of income up to the limit and 5% of income above it, up to $58,200, with the excess deferred as a lien.","<strong>Circuit breaker:</strong> holds the bill to 4% or 5% of income, with the $58,200 ceiling, and defers the rest as a lien."),
])
sub('w2.py',[
("What does it cost to record a deed in Wilson County?","Which fees apply at the Wilson County recording counter?"),
("Recording fees are set by state law and are the same in every county. Under","One statewide schedule governs. Under"),
("<p>A deed protects the buyer against outside claims only once it is recorded in the county where the land lies.","<p>Protection against outside claims starts at registration in the land's home county."),
("What does the Wilson County Register of Deeds do?","What is the Wilson County Register of Deeds office for?"),
])
sub('w3.py',[
("Who do I call about Winston-Salem property tax?","Which number reaches Winston-Salem's tax office?"),
("How do I appeal a Winston-Salem assessment?","What is the window to challenge a Winston-Salem value?"),
("The median value of an owner-occupied home is $233,800, and median gross rent is $1,087.","Census lists $233,800 as the typical owned home's value and $1,087 as gross rent."),
("Median household income is $59,268, and mean travel time to work is 21.5 minutes.","Households earn a median $59,268, and workers spend 21.5 minutes getting to work."),
("Roughly 39.5% of adults 25 and older hold a bachelor's degree or higher.","Close to 4 in 10 adults over 25 hold a four-year degree."),
])
sub('w4.py',[
("How are Yadkin County appeals handled?","Where does a Yadkin County value dispute go?"),
("22.4% of residents are 65 or older, which makes the age-based tax relief programs relevant to many owners.","About one resident in four and a half is 65 or older (22.4%), so age-based relief matters here."),
("76.9% of homes are owner-occupied for 2020 to 2024, a higher rate than in most larger NC cities.","Owners occupy 76.9% of homes for 2020 to 2024."),
("The median owner-occupied value is $181,200, and median gross rent is $766.","Owned homes have a median value of $181,200, against gross rent of $766."),
("Median household income is $62,932.","Household income in the middle is $62,932."),
("Yadkin's tax office processes applications for exemptions and exclusions granted under state law. The three programs below use the NCDOR 2026 figures, and an owner may receive only one.","The Yadkin tax office takes applications for state exemptions and exclusions. These three use NCDOR's 2026 figures, and only one can be used at a time."),
("Yes, the tax office's page announces that the 2027 Yadkin County revaluation is underway. North Carolina counties must reappraise all real property on an eight-year cycle, and Yadkin's last notices went out in 2023, which fits the cycle.","Yes. The tax office's page announces that a 2027 revaluation is underway. State law puts every county on a cycle of at most eight years, and the county's 2023 reappraisal notices are posted in its document center."),
])
t=open('w4.py').read()
a=t.index('{"h2":"Where does a Yadkin');b=t.index('{"h2":"What relief programs')
t=t[:a]+'''{"h2":"Where does a Yadkin County value dispute go?","html":"<p>Start with the tax office by phone or email, since the office handles value changes, and take a formal case to the county's review board if that fails. The commissioners usually serve as that board under <a href=\\"@S@GS_105-322.html\\">G.S. 105-322</a>.</p><p>The statute lets a taxpayer ask for a hearing in writing or in person before the board adjourns, and the board mails its decision within 30 days after adjourning. A reappraisal year has a longer board calendar than other years, so ask which dates apply.</p><p>Beyond the county, the Property Tax Commission takes a written notice filed within 30 days of the mailed decision (<a href=\\"@S@GS_105-290.html\\">G.S. 105-290</a>).</p>"},
'''+t[b:]
extra='''{"h2":"How should a Yadkin County seller handle solid waste fees and listing rules?","html":"<p>Treat the $76.00 household fee as part of the property's yearly carrying cost, and ask the tax office whether the current stickers and fees are settled. A buyer's attorney may ask for proof when reviewing the file.</p><p>Business personal property, such as tools or equipment kept at a rental or workshop, is listed in January. <a href=\\"@S@GS_105-307.html\\">G.S. 105-307</a> runs the listing period from the first business day of January to January 31, with commissioner extensions possible and individual extensions for good cause on written request. Anything not listed can draw a penalty, so ask the office how to list.</p>"},
{"h2":"Which Yadkin County timeline matters most before listing a home?","html":"<p>Work back from the September 1 due date. A seller who plans a fall or winter closing should confirm the bill status in August, when the 2% discount applies, and again before the end of the year.</p><table><caption>Yadkin County tax dates from the county page and state law</caption><thead><tr><th>Date</th><th>Event</th></tr></thead><tbody><tr><td>January 1</td><td>Ownership and value fixed for the year</td></tr><tr><td>January 1 to 31</td><td>Personal property listing</td></tr><tr><td>August</td><td>2% early payment discount</td></tr><tr><td>September 1</td><td>Taxes due</td></tr><tr><td>January 6</td><td>Interest begins</td></tr></tbody></table><p>Buyers and sellers usually split the bill by closing date, and the attorney's settlement statement should show the split.</p>"},
'''
t=t.replace('],\n"faqs"',extra+'],\n"faqs"',1)
open('w4.py','w').write(t)
