def sub(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        a=a.replace('"','\\"'); b=b.replace('"','\\"')
        assert a in t,(f,a[:50])
        t=t.replace(a,b)
    open(f,'w').write(t)
sub('w3.py',[("65 or older, or totally and permanently disabled, income up to $38,800","Age 65 plus, or fully and permanently disabled, with income to $38,800"),
("65 or older or disabled, five years owned and occupied, income under $58,200","Same age or disability test, five years of ownership and residence, income under $58,200"),
("Owners with a high-value home in a good neighborhood and owners with a house needing repairs see very different tax pictures, because the city figures are an average over many areas.","These are city-wide figures, so a house on one street can sit far from the averages, and a seller with a home needing repairs may find the assessed value above what a buyer will pay. That mismatch is a reason to review the assessment before listing."),
("so renters hold a large share of the city's stock.","which leaves nearly half the homes in rental use."),
("Ask the tax office for the dates that apply to the current year, as they can shift in a reappraisal year.","Dates can differ in a reappraisal year, so confirm them with the tax office before you file."),
])
sub('w4.py',[("It is 336-849-7903, and the office is open Monday to Friday from 8:00 am to 5:00 pm per the county's tax page.","The number is 336-849-7903, and the county's tax page lists weekday counter hours of 8:00 am to 5:00 pm."),
("65 or older or totally and permanently disabled, income at or below $38,800 for 2026","Age 65 plus or fully and permanently disabled, income no higher than $38,800 for 2026"),
("65 or older or disabled, five years of owner occupancy, income up to $58,200","Same age or disability test, five years living in the home, income up to $58,200"),
("Owners occupy 76.9% of homes for 2020 to 2024.","Owners occupy 76.9% of homes, the 2020 to 2024 rate, which suggests many households stay in place."),
("Start with the tax office by phone or email, since the office handles value changes, and take a formal case","Start with a call or email to the tax office, which handles value changes, and take a formal case"),
("A reappraisal year has a longer board calendar than other years, so ask which dates apply.","In a reappraisal year the board calendar runs longer than usual, so ask which dates apply. Owners with a stronger case should bring recent sale prices of similar homes nearby, photographs and repair estimates."),
])
