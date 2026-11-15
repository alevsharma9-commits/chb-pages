import json,re,sys
D='/tmp/claude-tool-results/97e78538-3276-512e-9b86-9d23bf3bf4f0/'
F={'34':'mcp-Firecrawl-firecrawl_scrape-1794718935189-m4hbap-e708acf1.txt','1':'toolu_01S3R1HV8SK8t9ADryuoxosr-2b67d33e.txt','39':'mcp-Firecrawl-firecrawl_scrape-1794718978723-7ub2as-e6f24e27.txt','2':'mcp-Firecrawl-firecrawl_scrape-1794718980512-kkotn6-41242798.txt','18':'mcp-Firecrawl-firecrawl_scrape-1794719073904-291tjh-2fcdb1bd.txt','20':'mcp-Firecrawl-firecrawl_scrape-1794719105480-4jm6xi-dcaaba27.txt','33':'mcp-Firecrawl-firecrawl_scrape-1794719084402-m1mzbu-7b6db534.txt'}
t=sys.argv[1]
raw=open(D+F[t]).read()
try: s=json.loads(raw)['markdown']
except Exception as e:
    s=raw.replace('\\n','\n')
n=int(sys.argv[3]) if len(sys.argv)>3 else 1500
for sec in sys.argv[2].split(','):
    for m in re.finditer(r'(?m)^\W*'+re.escape(sec)+r'\.',s):
        print('=====',sec,len(s)); print(s[m.start():m.start()+n]); break
    else: print('=====',sec,'NOT FOUND')
