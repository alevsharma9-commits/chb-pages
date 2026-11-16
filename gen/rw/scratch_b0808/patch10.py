exec(open('patch1.py').read().split("sub('w1.py'")[0])
def add(f,before,sec):
    t=open(f).read(); assert before in t; t=t.replace(before,sec+before,1); open(f,'w').write(t)
add('w4.py','{"h2":"What happens to unpaid Yadkin County tax when I sell?"','''{"h2":"Which Yadkin County desk answers which question?","html":"<p>The tax office page splits its contacts into three email links: one for assessor and payment matters, one for appraisal, and one for exemptions. Use the appraisal link for a value question and the exemptions link for relief forms, so the message reaches the right staff member quickly.</p><p>Owners can also pull printable parcel maps from the county's GIS site and download property record cards from the tax page. A record card shows what the county has on file for a house, so check it for errors in square footage or condition before a buyer's appraiser does. Deed questions belong with an attorney and the Register of Deeds, which the tax page links to separately.</p>"},
''')
sub('w3.py',[
("Close to 4 in 10 adults over 25 hold a four-year degree.","Nearly 40% of adults age 25 and up hold a bachelor's degree or more."),
("The county's real estate page says its appraisal section can answer value questions faster if you have the parcel number, the owner's full name and the street address ready.","The appraisal section answers value questions faster when you bring the parcel number, owner's name and street address, per the county's real estate page."),
("The statutes are <a href=\"@S@GS_105-277.1.html\">G.S. 105-277.1</a> and G.S. 105-277.1B, and the application is at the Tax Office or online.","The statutes behind these are <a href=\"@S@GS_105-277.1.html\">G.S. 105-277.1</a> and G.S. 105-277.1B. The county's notice adds that the circuit breaker is aimed at owners with several non-spouse owners who all meet the standards, and applications come from the Tax Office or online."),
("The form is available online and at the Tax Office, and appeals go to the board that sits under","The form is online and at the Tax Office, and it goes to the board that sits under"),
])
