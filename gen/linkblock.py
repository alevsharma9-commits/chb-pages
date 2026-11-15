import json,sys,re
def block(state,pref):
    # state: display name, pref: pages dir code e.g. 'fl'
    import glob
    S='https://cashhomebuyersca.com/'
    groups={'Statewide guides':[], 'Sell my house by city':[], 'Property tax guides by city':[], 'Property tax guides by county':[], 'County records guides':[]}
    for f in sorted(glob.glob(f'pages/{pref}/*.json')):
        for p in json.load(open(f)):
            s=p['slug']; t=p['rank_math_title']
            if 'county' in s and 'property-tax' in s: g='Property tax guides by county'
            elif 'property-records' in s: g='County records guides'
            elif s.startswith('sell-my-house-fast-'): g='Sell my house by city'
            elif 'property-tax-guide' in s and s not in (f'{state.lower().replace(" ","-")}-property-tax-guide',): g='Property tax guides by city'
            else: g='Statewide guides'
            groups[g].append((s,t))
    out=f'<div class="wsp-related"><h2>{state} Guides and Local Pages</h2>'
    for g,items in groups.items():
        if not items: continue
        out+=f'<h3>{g}</h3><p>'+' '.join(f'<a href="{S}{s}/">{t.split(' | ')[0][:60]}</a>' for s,t in items)+'</p>'
    return out+'</div>\n'
if __name__=='__main__':
    print(len(block(sys.argv[1],sys.argv[2])))
