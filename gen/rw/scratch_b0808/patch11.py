def sub(f,pairs):
    t=open(f).read()
    for a,b in pairs:
        a=a.replace('"','\\"'); b=b.replace('"','\\"')
        assert a in t,(f,a[:50])
        t=t.replace(a,b)
    open(f,'w').write(t)
sub('w3.py',[
("Close to 4 in 10 adults over 25 hold a four-year degree.","Nearly 40% of adults age 25 and up hold a bachelor's degree or more."),
("The statutes are <a href=\"@S@GS_105-277.1.html\">G.S. 105-277.1</a> and G.S. 105-277.1B, and the application is at the Tax Office or online.","The statutes behind these are <a href=\"@S@GS_105-277.1.html\">G.S. 105-277.1</a> and G.S. 105-277.1B. The county's notice adds that the circuit breaker is aimed at owners with several non-spouse owners who all meet the standards, and applications come from the Tax Office or online."),
("The form is available online and at the Tax Office, and appeals go to the board that sits under","The form is online and at the Tax Office, and it goes to the board that sits under"),
])
