import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import *
import linkblock
def make(state,pref,slug,code):
    b=linkblock.block(state,pref).replace(f'<h2>{state} Guides and Local Pages</h2>','')
    h1=f"{state} Guides: Property Tax, Probate, Foreclosure and Selling by City and County"
    body=(f"<p><em>Last updated {DATE}.</em></p><p><strong>This is the full directory of our {state} guides.</strong> Every page uses official sources, and where we could not confirm something on an official page, the page says so.</p>"+b+cta(f"Selling in {state}?",f"We buy {state} houses as-is, with no commission, no repairs and no closing costs to you.")+DISCLAIM(state,'attorney or tax professional'))
    rt=f"{state} Guides by City and County | Cash Home Buyers"
    if len(rt)>62: rt=f"{state} Guides by City and County"
    rd=f"Every {state} guide in one place: property tax, probate, foreclosure and selling a house, by statewide topic, city and county. Official sources."
    return wrap(slug,h1,hero(state,h1,f"Sell Your {state} House for Cash",f"Tell us about your {state} house. We buy as-is and reply with a written cash offer."),body,rt,rd,f"{state.lower()} property guides")
if __name__=='__main__':
    state,pref,code=sys.argv[1:4]
    slug=f"{state.lower().replace(' ','-')}-guides-by-city-and-county"
    it=make(state,pref,slug,code)
    json.dump([it],open(f"pages/{pref}/{state.lower().replace(' ','-')}-directory-1.json",'w'))
    m=json.load(open('manifest.json')); f=f"pages/{pref}/{state.lower().replace(' ','-')}-directory-1.json"
    if not any(x['file']==f for x in m['batches']): m['batches'].append({'file':f})
    json.dump(m,open('manifest.json','w'),indent=1); print(slug,wc(it))
