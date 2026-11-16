def sub(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        a=a.replace('"','\\"'); b=b.replace('"','\\"')
        assert a in t,(f,a[:50])
        t=t.replace(a,b)
    open(f,'w').write(t)
sub('w3.py',[
("Owners with a mortgage report median monthly costs of $1,459, while owners without one report $486.","The Census median for monthly owner costs is $1,459 with a mortgage and $486 without."),
("The city counted 257,271 people in its 2025 estimate, per Census","Census estimates 257,271 residents for 2025,"),
("Ask the office how any city levy appears on your bill, since this page does not state a rate.","Ask the tax office how any city levy appears on your bill, since this page states no rate."),
("so ask the office for the date in the year you are filing.","so check with the office about the year you are filing."),
("Dates can differ in a reappraisal year, so confirm them with the tax office before you file.","A reappraisal year can shift the calendar, so confirm with the office before filing."),
("the bill carries the name of whoever held title on January 1, and a mid-year transfer leaves the seller liable.","the bill is issued to the January 1 titleholder, and selling later in the year leaves that seller liable."),
])
sub('w4.py',[
("The number is 336-849-7903, and the county's tax page lists weekday counter hours of 8:00 am to 5:00 pm.","The number is 336-849-7903. The counter serves walk-ins on weekdays, with the day ending at 5:00 pm."),
("Call 336-849-7903 for the office, which opens at 8:00 am and closes at 5:00 pm on weekdays.","The office line is 336-849-7903."),
("The bill follows the person who held title at the start of the year.","Whoever held title at year start is billed."),
("Before listing, request a payoff amount that includes solid waste fees, and hand it to the closing attorney.","Request a payoff amount that includes solid waste fees before you list, and pass it along to the closing attorney."),
("The closing pays it out of the seller's side.","Settlement takes it from the seller's side."),
("Where is the Yadkin County tax office and how do I pay?","Where is the Yadkin tax counter, and what are the payment options?"),
("Work back from the September 1 due date.","Plan backward from the first day of September."),
])
