exec(open('patch1.py').read().split("sub('w1.py'")[0])
def add(f,before,sec):
    t=open(f).read(); sec=sec.replace('"','\\"') if False else sec
    assert before in t; t=t.replace(before,sec+before,1); open(f,'w').write(t)
add('w1.py','{"h2":"What happens if I sell a Wilson County house with tax unpaid?"','''{"h2":"What else can appear on a Wilson County tax bill?","html":"<p>Besides the county levy, a parcel may carry a municipal tax, a fire district tax, a special district tax or a solid waste charge, because the county collects for all of them. Which ones apply depends on where the house stands, so read the bill line by line.</p><p>Since 2024 the county has split personal property from real estate, which means a seller with a vehicle, boat or business equipment may receive two separate bills. For homes outside a municipality, the new solid waste permit arrives with the annual bill, so a buyer taking over such a house should ask the seller to hand it over at closing.</p><p>A house inside the city of Wilson is billed for city tax through the same office, and the tax calculator on the county site lets owners test the combined result with their assessed value.</p>"},
''')
sub('w1.py',[("Wilson County covers about 373 square miles east of Raleigh, and the county seat, the city of Wilson, holds","Roughly 373 square miles east of Raleigh make up the county. Its seat, the city of Wilson, holds"),
("With six in ten homes lived in by their owners, many local sellers are also long-time residents.","Six in ten occupied homes have owner residents."),
("What are the ways to pay Wilson County tax?","How can I send a payment to the Wilson County tax office?"),
("Whoever owned the parcel on the first day of the year receives the bill, and","The person on the deed as of January 1 receives the bill, and"),
])
add('w2.py','{"h2":"What mistakes slow down a deed in Wilson County?"','''{"h2":"How do I get a copy of a recorded Wilson County deed?","html":"<p>Search the online index first, since it lists real estate documents back to 1974, then request an image or a certified copy from the office. Under G.S. 161-10 a certified copy costs $5.00 for the first page and $2.00 for each added page.</p><p>Deeds before the online coverage may be missing from the images, and in that case a phone call to 252-399-2935 gets a clerk looking for the book and page. Sellers who inherited a house often need the vesting deed to prove how title reached them, so ordering a certified copy early prevents a delay in the contract period.</p>"},
''')
sub('w2.py',[("The county keeps one half and the state gets the other half monthly.","Half stays with the county and half goes to the state each month."),
("Pull the parcel number from the tax records.","Find the parcel number in the county tax records."),
("The office's phone line is 252-399-2935","The phone line is 252-399-2935"),
("The Register of Deeds is the keeper of","The Register of Deeds keeps"),
])
sub('w3.py',[("65 or older, or totally and permanently disabled, income up to $38,800","Age 65 plus, or fully and permanently disabled, with income to $38,800"),
("65 or older or disabled, five years owned and occupied, income under $58,200","Same age or disability test, five years of ownership and residence, income under $58,200"),
("The Board of Equalization and Review.","The board."),
("Owners with a high-value home in a good neighborhood and owners with a house needing repairs see very different tax pictures, because the city figures are an average over many areas.","These are city-wide figures, so a house on one street can sit far from the averages, and a seller with a home needing repairs may find the assessed value above what a buyer will pay. That mismatch is a reason to review the assessment before listing."),
("so renters hold a large share of the city's stock.","which leaves nearly half the homes in rental use."),
("so ask the office for the date","so ask the office for the date") if False else ("Ask the tax office for the dates that apply to the current year, as they can shift in a reappraisal year.","Dates can differ in a reappraisal year, so confirm them with the tax office before you file."),
])
sub('w4.py',[("the office is open","the office is open") if False else ("It is 336-849-7903, and the office is open Monday to Friday from 8:00 am to 5:00 pm per the county's tax page.","The number is 336-849-7903, and the county's tax page lists weekday counter hours of 8:00 am to 5:00 pm."),
("65 or older or totally and permanently disabled, income at or below $38,800 for 2026","Age 65 plus or fully and permanently disabled, income no higher than $38,800 for 2026"),
("65 or older or disabled, five years of owner occupancy, income up to $58,200","Same age or disability test, five years living in the home, income up to $58,200"),
("Owners occupy 76.9% of homes for 2020 to 2024.","Owners occupy 76.9% of homes, the 2020 to 2024 rate, which suggests many households stay in place."),
("Monday to Friday","Monday to Friday") if False else ("Start with the tax office by phone or email, since the office handles value changes, and take a formal case","Start with a call or email to the tax office, which handles value changes, and take a formal case"),
("A reappraisal year has a longer board calendar than other years, so ask which dates apply.","In a reappraisal year the board calendar runs longer than usual, so ask which dates apply. Owners with a stronger case should bring recent sale prices of similar homes nearby, photographs and repair estimates."),
])
