# Page rewrite brief (lean, current). Read only this file.

Your batch file is /home/claude/chb-pages/gen/rw/batches/<batch id>.txt, 4 lines: slug | focus keyword | title | file holding the current page. Read each current page (the file field) so you do not repeat it. Write one file per page with the Write tool: /home/claude/chb-pages/gen/rw/<slug>.json

{"slug": "...", "sections": [{"h2": "question-led heading", "html": "<p>..</p><ul>..</ul>"}], "faqs": [{"q": "...", "a": "..."}], "sources": [{"title": "...", "url": "https://..."}]}

## Output rules
- 1,300 to 1,800 words across sections + faqs (check with python3 /home/claude/chb-pages/gen/rw/_count.py if it accepts a file; otherwise count yourself).
- Every H2 is a plain question. The first sentence under it answers it in one or two sentences. Paragraphs 2 to 4 sentences.
- At least two bullet lists and exactly one small sourced <table> with <thead>/<tbody>, no styling attributes. 5 FAQs, each answer starts with a direct answer.
- Use the place name often. You may link official pages inline with <a href="https://...">. List every page you used in "sources" (the pipeline strips the list from the live page).
- Do not mention Firecrawl, subagents, AI, this brief, or your research process.

## Facts
- Every number, date, name and claim comes from a page you opened this session. Official sources first: state statutes (law.lis, legislature sites), state agencies, county and city sites, Census QuickFacts. Wikipedia only for geography and history. No Zillow, Redfin, Realtor.com, Nolo, HomeLight, news blogs or commercial legal sites as sole source.
- If you cannot open an official page for a topic, leave the topic out. Where it matters to the reader, say plainly "Ask the county treasurer (or assessor, clerk) for ..." as an instruction.
- NEVER write sentences about your own research or what you left out on the page ("we did not open", "what we left out", "the source we reviewed", "could not be confirmed"). Reword to a plain instruction or drop it.
- Check dates against today (Nov 15 2026). Say a date has passed, or leave it out. Do not promise offers or prices.

## Style (humanizer)
Plain, specific, varied sentence length. No em or en dashes (use commas, periods, colons). No "not X but Y" contrasts. No "in today's market", "it is important to note", triads for rhythm, stock closers, or hype words (nestled, vibrant, bustling, tapestry, hidden gem). Never call the company "licensed". No disclaimer lines. Do not paste the site's sales line ("no fees, commissions or closing costs...").

## Uniqueness
Each page is checked for 5-word phrase overlap with every other page: 80% of phrases must appear nowhere else. State rules repeat across a state's pages, so phrase them freshly and briefly on each page and spend most words on facts specific to this city, county or topic. Write each page fresh. Do not reuse sentences across your 4 pages or from the current page text.

## Uniqueness gate (required before you finish)
Run: python3 /home/claude/chb-pages/gen/rw/overlap.py <slug> <slug> ... (your 4 slugs). It prints the share of your phrases found on no other page. Every page must reach 85% or more. For any page below that, it lists phrases found elsewhere: rewrite those passages with this place's own facts and wording (edit the JSON), then run it again. Typical culprits: the Census sentence ("the Census Bureau puts the median value of owner occupied homes at ..."), FAQ openers ("How long do I have to ..."), "the second half is due ...", "from the sale proceeds at closing". Give the table caption, the Census facts and every state-rule sentence fresh, place-specific wording on each page, and keep state-rule sentences to one short sentence each.

## Page types
- City page (sell-my-house-fast-<city>-<st>): the city (layout, history in brief, economy, climate effects on a house if sourced, schools by district name, roads, neighborhoods, local rules for permits, rental or short-term rental, recording and transfer steps) tied to selling a house there.
- County property tax page: county geography and towns plus assessment, tax dates, appeals, relief programs, paying tax at closing. Cite the assessor/treasurer pages.
- City property tax page: the city and the county that bills it.
- State topic page (<state>-probate, -foreclosure, -estate-tax, -squatters-rights, -landlord-tenant, -eviction-notice, -tax-sale, -property-tax-guide, etc.): the state law with statute citations from the official legislature site, plus state agency and court self-help pages. Add regions, largest counties and county differences where sourced.
- Directory page (<state>-guides-by-city-and-county): state overview for sellers. Do not list links.

## Research tools (this session, in order)
1. WebSearch to find pages (small per-turn budget).
2. mcp__TinyFish_crawl__fetch_content to open pages (it opens .gov, statutes, Census and Wikipedia; WebFetch and the Playwright browser fail here). Load with ToolSearch "select:mcp__TinyFish_crawl__fetch_content,mcp__TinyFish_crawl__search". It bills the owner per page: about 6 to 10 reads per page you write, batch several URLs per call when the tool allows, never re-read a page you already have.
3. mcp__HasData__hasdata_web_scraping_web_scraping_scrapeWebPage (datacenter proxy, jsRendering false, markdown) for non-government pages only.
Never use Firecrawl, curl, Bash or proxies to fetch. Never get past a captcha or bot check. Do not run git commands.

## Finish
Print a short table: slug, words, sources, topics left out. Nothing else.
