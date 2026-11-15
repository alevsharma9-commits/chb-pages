import json,re
OUT='/home/claude/chb-pages/gen/rw/'
def words(d):
    t=' '.join(s['html'] for s in d['sections'])+' '+' '.join(s['h2'] for s in d['sections'])+' '+' '.join(f['q']+' '+f['a'] for f in d['faqs'])
    t=re.sub(r'<[^>]+>',' ',t)
    return len(t.split())
def save(d):
    for s in d['sections']+d['faqs']:
        for v in s.values():
            assert '—' not in v and '–' not in v, v[:60]
    open(OUT+d['slug']+'.json','w').write(json.dumps(d,indent=1,ensure_ascii=False))
    print(d['slug'],words(d),len(d['sources']))

DOR_GUIDE=("2025 Property Owner Appeal Process Guide (SD Department of Revenue)","https://dor.sd.gov/media/0hajl2ya/board-appealprocessguide-2025.pdf")
DOR_PT=("South Dakota Department of Revenue property tax page","https://dor.sd.gov/individuals/taxes/property-tax/")
SDCL=("SDCL 10-21-23, delinquency dates and interest","https://sdlegislature.gov/api/Statutes/10-21-23.html?all=true")
ROD_FEE=("Oglala Lakota County Register of Deeds recording fees (SDCL 43-4-21 transfer fee)","https://oglalalakotacountysd.gov/register-of-deeds/recording-fees/")
def S(t):return {"title":t[0],"url":t[1]}

