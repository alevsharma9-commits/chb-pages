import json,re
S=[]
def sec(h,html): S.append({"h2":h,"html":html})
sec("What is Washoe County and how is it laid out?",
"<p>Washoe County is in the northwest corner of Nevada, and Reno is its county seat. It covers 6,542 square miles, of which 6,302 are land, and its 2020 census population was 486,492, which makes it the second most populous county in the state.</p>"
"<p>Only two cities are incorporated here, Reno and Sparks. The rest of the county is made up of unincorporated communities. The Wikipedia article on the county lists Cold Springs, Crystal Bay, Empire, Gerlach, Golden Valley, Incline Village, Lemmon Valley, Mogul, Nixon, Spanish Springs, Sun Valley, Sutcliffe, Verdi, Wadsworth and Washoe Valley as census-designated places. The highest point is Mount Rose at 10,785 feet, and Pyramid Lake lies in the north.</p>"
"<p>That layout matters for property tax. A house in Incline Village, one in Sun Valley and one in downtown Reno are all billed by the same Treasurer, and the Assessor publishes tax district maps and neighborhood maps for the county.</p>")
sec("How did Washoe County come about?",
"<p>Washoe County was created on November 25, 1861, as one of the nine original counties of Nevada Territory, and it is named after the Washoe people. It was consolidated with Roop County in 1864. Washoe City was the first county seat, and Reno replaced it in 1871.</p>"
"<p>The Truckee Meadows drew settlers in the 1850s, and the Junction House was established south of the Truckee River in 1850. Pyramid Lake was named by Lieutenant John C. Fremont in January 1844. A 2010 ballot question asked whether the Reno and Washoe County governments should consolidate; unofficial results showed 54 percent of voters approving it.</p>")
sec("What drives the Washoe County economy?",
"<p>Washoe County mixes tourism, logistics, manufacturing and technology. Between 2020 and 2025 the number of jobs in the county rose 13.1 percent, compared with 10.6 percent nationally. In the Lake Tahoe Basin, more than 40 percent of jobs were related to tourism in 2013.</p>"
"<p>The county school district, the University of Nevada, Reno, Renown Regional Medical Center and several large casinos are the biggest employers in Reno. Sierra Nevada Corporation is based in Sparks, and the Tesla Gigafactory at the Tahoe Reno Industrial Center, just outside Washoe in Storey County, employs about 11,000 people.</p>"
"<p>For an owner thinking about selling, the county's own statistics are worth knowing. The Assessor posts Sales Reports, a Median Sales Chart and Current Statistical Reports on its online data pages, so you can see recorded sale prices for your area before you compare them with an offer.</p>")
sec("What hazards should Washoe County sellers watch?",
"<p>The county is wildfire prone, and most of that risk is in southern Reno and just outside the city limits. Many fires in southwest Reno have spread quickly, including the Caughlin Fire in 2011. Structures are also being built in forested areas.</p>"
"<p>The Assessor's office answers questions about whether a property is within a FEMA floodplain and can provide elevation certificates. Both questions come up when a buyer's lender or insurer asks.</p>"
"<ul><li>Disclose known fire damage, burn scars or smoke damage on the Nevada disclosure form</li>"
"<li>Ask the Assessor for the floodplain status of the parcel</li>"
"<li>Check whether unpermitted additions need a Washoe County Building review</li></ul>")
sec("Who bills and who values property in Washoe County?",
"<p>Washoe County divides the work between three offices, and sellers deal with each at a different stage. The Assessor values the property and handles appeals and exemptions, the Treasurer bills and collects tax, and the Recorder records the deed and collects the real property transfer tax.</p>"
"<table><thead><tr><th>Office</th><th>What it does</th><th>Contact</th></tr></thead><tbody>"
"<tr><td>Assessor</td><td>Values, tax cap status, exemptions, Board of Equalization appeals</td><td>(775) 328-2277</td></tr>"
"<tr><td>Treasurer</td><td>Bills, collections, delinquent parcels, online payments</td><td>775.328.2510, tax@washoecounty.gov, 1001 E 9th Street, Room D140, Reno</td></tr>"
"<tr><td>Recorder</td><td>Recording deeds, Declaration of Value, transfer tax</td><td>(775) 328-3661 for transfer tax questions</td></tr>"
"</tbody></table>"
"<p>The Treasurer cannot take payments by telephone, so pay online or by mail. Customer service runs Monday through Friday, 8am to 5pm.</p>")
sec("What deadlines matter for a Washoe County property tax year?",
"<p>The county fiscal year runs from July 1 through June 30, with July 1 as the lien date. These are the dates the Assessor lists, besides the installment dates already shown above.</p>"
"<ul><li>December 18: value notices mailed to owners</li>"
"<li>January 1: the real property roll closes</li>"
"<li>January 15: deadline to appeal to the County Board of Equalization</li>"
"<li>March 10: deadline to appeal a County Board decision to the State Board</li>"
"<li>June 15: deadline to renew or apply for most exemptions, and for rental owners to file the tax cap form for the next fiscal year</li>"
"<li>June 30: deadline to appeal a tax cap determination for the current year</li>"
"<li>July 5: deadline to apply for an exemption on property acquired after June 15 and before July 1</li></ul>"
"<p>If January 15 falls on a weekend or holiday, the appeal may be filed on the next business day.</p>")
sec("How does the 3 percent tax cap work when a house sells?",
"<p>The tax cap limits the growth of the tax bill, not the assessed value. Under Assembly Bill 489, signed in 2005, a primary residence has a 3 percent cap on its bill, and other property has a higher cap. Some rental dwellings may also qualify for 3 percent. The only property with no cap is property new to the roll, such as new construction, new parcels or a parcel with a change in use.</p>"
"<p>Washoe County mails an affidavit to residential rental owners in early May that must be returned by June 15, and it sends affidavits to non-rental properties after a change in ownership. Until a qualifying affidavit is filed, the property sits at the higher general abatement. The Assessor has 30 days to answer an appeal of a tax cap decision. The Assessor's phone number is (775) 328-2277.</p>"
"<p>A buyer of a primary residence who files promptly can have the 3 percent cap applied, while an investor buying a rental may see a different cap. Telling a buyer this early can head off a surprise on the first bill.</p>")
sec("What happens to the tax bill at closing?",
"<p>Taxes for the fiscal year are a lien from July 1, and the Washoe County Treasurer will advertise parcels that are delinquent. Owners have 2 years from the date the lien is filed to redeem by paying all taxes, penalties and costs. Penalties follow NRS 361.483, and the county billing page gives no percentages.</p>"
"<p>One detail often missed: the supplemental tax bill is not sent to the mortgage company. A seller who is paying off a loan should check whether a supplemental bill was issued for a recent improvement or new construction.</p>"
"<p>Real property transfer tax is separate. The Washoe County rate is $2.05 per $500 of value, which is the $1.95 statewide rate plus $0.10. On a $500,000 sale that is $2,050. The Recorder collects it when the deed is recorded, using the Declaration of Value, and the base is either the price or the estimated fair market value, which uses the assessor's taxable value or a prior purchase price within five years, whichever is higher. Exemptions under NRS 375.090 include transfers between former spouses under a divorce decree and transfers into a trust without consideration.</p>")
sec("Can you sell a Washoe County house for cash when taxes are owed?",
"<p>Yes. Owing property tax does not by itself stop a sale, but the unpaid amount has to be dealt with in the deal. We buy Washoe County houses as-is, including houses behind on taxes, inherited houses and rentals. We give a written offer and you owe nothing if you decline.</p>"
"<p>Before you sell, request the tax balance from the Treasurer, check your tax cap status with the Assessor and ask the Recorder about the Declaration of Value. NRS 113.130 still requires a disclosure form at least 10 days before conveyance.</p>")
faqs=[
("Who collects property tax in Washoe County?","The Washoe County Treasurer bills and collects it. Bills are mailed by August 1 and taxes are due on the third Monday in August, with installments allowed when a parcel's tax exceeds $100. Payments cannot be taken over the phone."),
("When do I have to appeal my Washoe County assessment?","Appeals to the County Board of Equalization are due by January 15, or the next business day if that falls on a weekend or holiday. You can appeal a County Board decision to the State Board of Equalization by March 10."),
("What is the Washoe County transfer tax rate?","It is $2.05 per $500 of value, made up of the $1.95 statewide rate plus $0.10 for Washoe County. The Recorder collects it when the deed is recorded. A $500,000 sale carries $2,050."),
("How does the 3 percent tax cap apply to a new buyer?","The cap applies to the tax bill of a primary residence. After a change in ownership the Assessor mails an affidavit, and the property stays at the higher cap until a qualifying affidavit is returned."),
("How long do I have to redeem a delinquent Washoe County parcel?","Owners have two years from the date the lien is filed to redeem by paying all taxes, delinquencies and costs. Delinquent properties are advertised in the local newspaper."),
("Does a supplemental tax bill go to my mortgage company?","No. The Washoe County Treasurer says the supplemental bill is not sent to the mortgage company, so the owner should watch for it."),
]
src=[
("Washoe County Treasurer: Billing Information","https://www.washoecounty.gov/treas/Billing.php"),
("Washoe County Treasurer","https://www.washoecounty.gov/treas/"),
("Washoe County Assessor: Important Dates","https://www.washoecounty.gov/assessor/ImportantDates.php"),
("Washoe County Assessor: Tax Cap/Abatement","https://www.washoecounty.gov/assessor/taxcap/index.php"),
("Washoe County Assessor: Assessment Notices","https://www.washoecounty.gov/assessor/real_property/AssessmentNotices.php"),
("Washoe County Recorder: Real Property Transfer Tax","https://www.washoecounty.gov/recorder/real_property_transfer_tax.php"),
("Nevada Department of Taxation: Real Property Transfer Tax FAQs","https://tax.nv.gov/faqs/real-property-transfer-tax-faqs/"),
("Justia: NRS 113.130","https://law.justia.com/codes/nevada/chapter-113/statute-113-130/"),
("Wikipedia: Washoe County, Nevada","https://en.wikipedia.org/wiki/Washoe_County,_Nevada"),
("Wikipedia: Reno, Nevada","https://en.wikipedia.org/wiki/Reno,_Nevada"),
]
json.dump({"slug":"washoe-county-nv-property-tax-guide","sections":S,"faqs":[{"q":q,"a":a} for q,a in faqs],"sources":[{"title":t,"url":u} for t,u in src]},open('/home/claude/chb-pages/gen/rw/washoe-county-nv-property-tax-guide.json','w'),indent=1)
wc=lambda h: len(re.sub(r'<[^>]+>',' ',h).split())
print(sum(wc(s['h2'])+wc(s['html']) for s in S)+sum(wc(q)+wc(a) for q,a in faqs))
