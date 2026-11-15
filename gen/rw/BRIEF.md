# Page expansion brief (Cash Home Buyers, cashhomebuyersca.com)

For each assigned page, write NEW body sections so the page reaches 1,300+ words of body text (the existing short page stays; your sections are added). Output one JSON file per page at /home/claude/chb-pages/gen/rw/<slug>.json:

{"slug": "...", "sections": [{"h2": "question-led or descriptive heading", "html": "<p>..</p><ul>..</ul>"}, ...], "faqs": [{"q": "...", "a": "..."}], "sources": [{"title": "...", "url": "https://..."}]}

Rules
- Total words across sections + faqs: 1,300 to 1,800. Count them.
- Research with WebSearch and WebFetch only (never Firecrawl, never curl). Every number, date, name and claim must come from a page you opened. Prefer official sources: city/county/state government sites, Census Bureau, state agencies, the local school district, the airport/transit authority, the chamber of commerce. Wikipedia is allowed for history/geography only. NO Zillow, Redfin, Realtor.com or other listing-site numbers. If you cannot confirm something, leave it out. Never invent figures, names or dates.
- Content may go beyond real estate. Cover the place itself around the page keyword: where it is and how it is laid out, history in brief, economy and major employers, climate and what it means for a house (roof, heating, hail, flood, wildfire where sourced), schools and districts (names only unless sourced), roads and transit, neighborhoods or areas, utilities, notable local rules (permits, code enforcement, HOA, rental registration, short-term rental rules, transfer/recording steps), property tax offices and dates, how a sale or a cash sale works here, and what sellers in this specific place usually face. Tie each section back to selling a house (or the property-tax topic of a county page) in this place.
- AI-friendly structure: each H2 is a plain question or clear topic; the first sentence under it answers it directly in one or two sentences; short paragraphs (2 to 4 sentences); at least two bullet lists and one small HTML table of sourced facts (<table> with <thead>/<tbody>, no styling attributes); FAQ answers start with a direct answer. Use the place name often, in natural wording.
- Humanizer style: plain, specific, varied sentence length. No em dashes or en dashes (use commas, periods, colons). No "not X but Y" lines, no "in today's market", no "it is important to note", no triads for rhythm, no stock closers, no hype words (nestled, vibrant, bustling, rich tapestry, hidden gem). No marketing claims you cannot support. Do not promise offers or prices.
- Links: you may link to official pages with <a href="https://...">text</a> inside sections. Also list every page you used in "sources" (title and URL).
- Do not repeat sentences across pages. Write each page fresh, using the facts you found for that place.
- Do not mention Firecrawl, subagents, AI, or this brief. Write as the Cash Home Buyers editorial team.
- Finish by printing: slug, word count, number of sources. Write the JSON files with the Write tool.

## Page types (addendum)
- City page (sell-my-house-fast-<city>-<st>): the city itself plus selling a house there.
- County property tax page (<county>-county-<st>-property-tax-guide): the county (towns, geography, economy) plus assessment, tax dates, appeals, paying tax at closing. Cite the county assessor/treasurer pages.
- City property tax page (<city>-<st>-property-tax-guide): same idea for the city and the county that bills it.
- State topic page (e.g. <state>-probate, -foreclosure, -estate-tax, -squatters-rights, -landlord-tenant, -eviction-notice, -tax-sale, -property-tax-guide): explain the state law with statute citations from the official legislature site (or Justia copies of the statute), state agency pages and court self-help pages. Add state context (regions, largest counties, how the process differs by county) where sourced.
- Directory page (<state>-guides-by-city-and-county): a state overview for sellers (regions, largest cities and counties, state-level transfer/recording rules, how property tax is run in the state). Do not list links; the page already links its city and county pages.
- Every page must read differently from its neighbors in the same state. Do not reuse your own sentences across your pages.


## Research tools (UPDATED, overrides anything above)
Use Firecrawl for all page reads: mcp__Firecrawl__firecrawl_scrape (url, formats ["markdown"], onlyMainContent true) to open a page, and mcp__Firecrawl__firecrawl_search or WebSearch to find pages. mcp__Firecrawl__firecrawl_gov_search is free and good for statutes and county/state government pages. Do NOT use WebFetch. Load Firecrawl tool schemas with ToolSearch first (select:mcp__Firecrawl__firecrawl_scrape,mcp__Firecrawl__firecrawl_search,mcp__Firecrawl__firecrawl_gov_search). Keep scrapes lean: about 6 to 10 page reads per page you write. If Firecrawl reports it is out of credits, stop and report that.

## Uniqueness (UPDATED)
Pages are checked for 5-word phrase overlap with every other page on the site; at least 80% of each page's phrases must appear nowhere else. State rules (due dates, statutes, exemption amounts) are repeated on many pages of the same state, so phrase them in your own fresh wording on each page and keep them short. Spend most of the words on facts specific to this city, county or topic. Do not paste the site's sales line ("no fees, commissions or closing costs...") into your sections; the page already has it.

## Research tools (FINAL, overrides every earlier tool section)
Firecrawl is out of credits: do NOT use any mcp__Firecrawl__ tool. Use WebSearch to find pages and WebFetch to open them. If a WebFetch fails on a page, try another official page; never use curl, Bash or any proxy to fetch pages. About 6 to 10 page reads per page you write.

## Site preference (keeps approval prompts low)
Each new website can trigger an approval prompt for the owner. Do most reading on a small set of sites: en.wikipedia.org, law.justia.com, census.gov, the state's main .gov sites (legislature, tax/revenue agency, courts). Open at most 2 or 3 county or city sites per page, only for facts you cannot get elsewhere (tax dates, office contacts, local rules). Never use Firecrawl.

## HasData (optional, non-government only)
mcp__HasData__hasdata_web_scraping_web_scraping_scrapeWebPage (proxyType datacenter, jsRendering false, outputFormat markdown) works only for non-government pages with no bot challenge (city/county .com or .org sites, chambers, local news). It refuses .gov sites, Wikipedia rate-limits it, Justia serves a captcha. Never use residential proxies or try to get past a captcha. Government pages and statutes: WebFetch only.
