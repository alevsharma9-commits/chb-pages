import json,glob,re,statistics,hashlib,collections
A='/home/claude/chb/acs2/'
def load(fn,county):
    D={}
    for l in open(A+fn):
        x=l.rstrip('\n').split('|')
        if county: st,sl,pop,units,own,val,yr,inc=x[0],x[1],*map(int,x[2:])
        else: st,sl,pop,own,val,yr=x[0],x[1],*map(int,x[2:]);units=inc=-1
        D.setdefault((st,sl),dict(pop=pop,units=units,own=own,val=val,yr=yr,inc=inc))
    return D
CO=load('counties.txt',True);PL=load('places.txt',False)
def med(D,st,k):
    v=[d[k] for (s,_),d in D.items() if s==st and d[k]>0];return statistics.median(v) if len(v)>=4 else statistics.median([d[k] for d in D.values() if d[k]>0])
def rank(D,st,sl):
    v=sorted([(d['pop'],n) for (s,n),d in D.items() if s==st],reverse=True)
    return [n for _,n in v].index(sl)+1,len(v)
STN=json.load(open('/home/claude/chb/state_names.json'))
def money(n):return '${:,}'.format(n)
def pct(a,b):
    r=(a-b)/b*100
    return 'about level with' if abs(r)<1.5 else f'{abs(round(r))}% {"above" if r>=0 else "below"}'
def v(slug,n):return int(hashlib.md5(slug.encode()).hexdigest(),16)%n
def city_block(st,sl,name,d,slug):
    S=STN.get(st,st);k=v(slug,3)
    mv=med(PL,st,'val');mo=med(PL,st,'own');r,N=rank(PL,st,sl);age=2023-d['yr'];ren=100-d['own']
    s=[]
    s.append([f"The Census Bureau's 2019-2023 survey counts about {d['pop']:,} people in {name}, which makes it the {r}{'th' if 10<=r%100<=20 else {1:'st',2:'nd',3:'rd'}.get(r%10,'th')} largest of the {N} {S} places we cover.",
              f"{name} has roughly {d['pop']:,} residents in the Census Bureau's 2019-2023 survey, and ranks number {r} by population among the {N} {S} places in this guide.",
              f"With about {d['pop']:,} residents, {name} is number {r} of the {N} {S} places in this guide by population (Census Bureau, 2019-2023)."][k])
    if d['val']>0:
        s.append([f"The median value of an owner-occupied home is {money(d['val'])}, {pct(d['val'],mv)} the median of those {N} places.",
                  f"Owner-occupied homes have a median value of {money(d['val'])} here, which is {pct(d['val'],mv)} the middle figure for the {N} {S} places.",
                  f"Census respondents put the median owner-occupied home in {name} at {money(d['val'])}, {pct(d['val'],mv)} the {S} median for these places."][k])
    s.append([f"{d['own']}% of occupied homes are owner-occupied and {ren}% are rented, against a median of {round(mo)}% owner-occupancy across the {S} places.",
              f"About {ren}% of households rent, so {d['own']}% own; the {S} median for these places is {round(mo)}% owner-occupied.",
              f"Renters live in about {ren}% of {name} homes, and owners in {d['own']}%, where the {S} median is {round(mo)}% owners."][k])
    if d['yr']>1900:
        s.append([f"The median home was built in {d['yr']}, about {age} years ago, which matters for roofs, plumbing and inspection requests.",
                  f"Homes here were typically built in {d['yr']}, so the median house is about {age} years old.",
                  f"A median build year of {d['yr']} puts the typical {name} house near {age} years old."][k])
    s.append(f"These numbers describe {name} as a whole, so a given street can sit well above or below them.")
    return s
def county_block(st,sl,name,d,slug):
    S=STN.get(st,st);k=v(slug,3);r,N=rank(CO,st,sl);mv=med(CO,st,'val');inc=med(CO,st,'inc');age=2023-d['yr'];ren=100-d['own']
    s=[[f"{name} County has about {d['pop']:,} residents and {d['units']:,} housing units in the Census Bureau's 2019-2023 survey, number {r} by population among the {N} {S} counties we cover.",
        f"The Census Bureau's 2019-2023 survey counts {d['pop']:,} people and {d['units']:,} housing units in {name} County, which ranks {r} of {N} {S} counties here.",
        f"{name} County ranks {r} of {N} {S} counties in this guide by population, at about {d['pop']:,} people in {d['units']:,} housing units (Census Bureau, 2019-2023)."][k]]
    if d['val']>0:
        s.append([f"The median owner-occupied home is worth {money(d['val'])}, {pct(d['val'],mv)} the median of the {S} counties covered.",
                  f"Median home value is {money(d['val'])}, which is {pct(d['val'],mv)} the middle county in this {S} set.",
                  f"At {money(d['val'])}, the median home value sits {pct(d['val'],mv)} the {S} county median for this guide."][k])
    if d['inc']>0:
        s.append([f"Median household income is {money(d['inc'])}, against {money(round(inc))} for the middle {S} county.",
                  f"Households here earn a median {money(d['inc'])}; the middle {S} county is at {money(round(inc))}.",
                  f"The {S} county median income is {money(round(inc))}, and {name} County reports {money(d['inc'])}."][k])
    s.append([f"Owners live in {d['own']}% of occupied homes and renters in {ren}%.",f"{ren}% of occupied homes are rented, which leaves {d['own']}% owner-occupied.",f"Owner-occupancy is {d['own']}%, so renters hold about {ren}% of occupied homes."][k])
    if d['yr']>1900:s.append(f"The median home was built in {d['yr']}, about {age} years ago.")
    return s
SLUGPAT=[(re.compile(r'^(.+)-county-([a-z]{2})-'),'county'),(re.compile(r'^sell-my-house-fast-(.+)-([a-z]{2})$'),'city'),(re.compile(r'^(.+)-([a-z]{2})-property-tax-guide$'),'city')]
def title(sl):return ' '.join(w.capitalize() for w in sl.split('-'))
n=0;miss=0
for f in sorted(glob.glob('pages/*/*.json')):
    d=json.load(open(f));ch=False
    for p in d:
        c=p['content']
        if 'by the numbers</h2>' in c or 'at a glance</h2>' in c: continue
        for pat,kind in SLUGPAT:
            m=pat.match(p['slug'])
            if m:break
        else: continue
        sl,st=m.group(1),m.group(2)
        if kind=='county' and (st,sl) in CO: dd=CO[(st,sl)];sents=county_block(st,sl,title(sl),dd,p['slug']);nm=title(sl)+' County'
        elif kind=='city' and (st,sl) in PL: dd=PL[(st,sl)];sents=city_block(st,sl,title(sl),dd,p['slug']);nm=title(sl)
        else: miss+=1;continue
        blk=f"<h2>{nm} by the numbers</h2><p>{' '.join(sents)}</p>"
        i=c.find("<div class='wsp-related'>")
        if i<0:i=c.find('<h2>Sources</h2>')
        if i<0:continue
        p['content']=c[:i]+blk+c[i:];n+=1;ch=True
    if ch:json.dump(d,open(f,'w'))
print('injected',n,'no data',miss)
