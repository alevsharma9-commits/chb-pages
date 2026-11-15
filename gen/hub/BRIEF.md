# State hub page brief (cashhomebuyersca.com)

You rewrite ONE state hub page, "We Buy Houses in <State>" (slug we-buy-houses-in-<state-slug>). Your state is given in your prompt as a two letter code (for example sc). Facts file: /home/claude/chb-pages/gen/hub/facts/<code>.json (state_slug, city_pages, city_tax_guides, county_pages, state_topic_pages, each a list of [slug, title]). All of those pages already exist on the site.

Output: /home/claude/chb-pages/gen/hub/out/<code>.json

{
 "sections": [{"h2": "...", "html": "<p>..</p>"}],
 "faqs": [{"q": "...", "a": "..."}],
 "sources": [{"title": "...", "url": "https://..."}],
 "counties": [
   {"name": "Charleston County",
    "county_slugs": ["charleston-county-sc-property-tax-guide"],
    "cities": [{"name": "Charleston", "slug": "sell-my-house-fast-charleston-sc"}]}
 ],
 "unplaced": [{"name": "...", "slug": "..."}]
}

## What goes where
1. counties: this is the main structure, like the California hub (a heading per county, county guide links first, then city links). Put EVERY slug from city_pages and city_tax_guides under the county the city sits in, and put every county page slug (county_pages) under its own county (the county is in the slug). A county that only has county pages and no city pages still gets an entry with an empty cities list. A city page whose county you cannot confirm from an opened page goes in "unplaced", never guessed. Cities that straddle two counties go under the county the city's own Wikipedia page or the Census lists first (note in no text, just pick one). For Louisiana use parishes ("name": "Orleans Parish"); for Alaska-style boroughs not needed. Virginia independent cities go in an entry named "Independent cities".
   Link text for a city is the plain place name. Use the slug exactly as listed in the facts file, never invent a slug.
2. sections: 1,200 to 1,500 words of NEW unique text about selling a house in this state (state level, not city level). Question-led H2s, first sentence answers directly, short paragraphs, at least two bullet lists and one small HTML table (<table><thead><tbody>, no style attributes) of sourced facts. Topics to cover where you can source them: how the state's counties and cities are organized and how many counties it has, how property taxes and recording work at county level and who to call, foreclosure type (judicial or non-judicial) and timeline, probate basics for an inherited house, deed and transfer tax, homestead, landlord and tenant when a house has tenants, what a cash sale as-is means here, closing attorney or title company practice, common property issues sellers face in the state (climate, hail, flood, wildfire, radon, well and septic) only if sourced. You may link to our own pages from the facts file inside sections with <a href="https://cashhomebuyersca.com/<slug>/">text</a>. Add 6 to 8 FAQs (150 to 250 words total).
3. sources: every page you used.

## Rules
- Research tools: WebSearch and WebFetch; if WebFetch is rate limited use Claude in Chrome in your own tab (open it, read text, close it) or HasData for non-government pages. Never Firecrawl, never curl. Facts only from pages you opened; prefer official state and county sites, Census Bureau, state statutes. Wikipedia is allowed for the county list and for city to county placement. Leave out anything you cannot confirm and tell the reader to ask the county office.
- You may read the site's own state topic pages in the repo (state_topic_pages in the facts file, files under /home/claude/chb-pages/pages/<code>/) to reuse their sourced facts, but word everything freshly. Do not copy sentences from them or from other hubs. At least 80 percent of 5-word phrases must be unique versus other pages.
- Style (humanizer): plain, specific, varied sentence length. No em dashes or en dashes. No "not X but Y", no "in today's market", no stock closers, no hype words (nestled, vibrant, bustling, hidden gem), no triads for rhythm. Never say the company is "licensed". Never mention wholesaling. Do not promise offers or prices. Do not add disclaimer lines.
- Write as the Cash Home Buyers editorial team. Do not mention AI, subagents or this brief.
- Validate that the JSON parses and that every slug used in counties/unplaced exists in the facts file lists. Finish with a short report: code, word count of sections+faqs, number of counties, number of cities placed and unplaced, facts left out.
