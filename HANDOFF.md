# HANDOFF: cashhomebuyersca.com thin-page rewrite (written Nov 15, 2026, about 11:35 am PT)

Read this whole file before doing anything. It is written so a new Claude chat can take over without prior context. Do not assume anything not written here; ask the user (Alev Sharma) when unsure.

## 1. The project
cashhomebuyersca.com is a WordPress site (theme Kadence, SEO plugin Rank Math, code snippets via WPCode, managed through WPVibe tools). It is a nationwide SEO build of seller-lead pages for 46 states (all except CA, HI, AK, RI): cities 25K+ and counties, only where the main query is above 100 monthly searches. About 5,000 older California pages also exist and are untouched.

Current phase: rewrite ALL thin pages. 3,670 built pages are in scope: city "sell-my-house-fast-<city>-<st>" pages, county property-tax guides, city property-tax guides, county clerk/records pages, state-topic pages (foreclosure, sheriff sale, squatters rights, transfer tax and similar), and state directories.

Targets per page:
- Over 1,200 words (agents write 1,300 to 1,800 words of new text).
- At least 80% unique by a Google-style measure: 5-word shingles over body text; score = share of shingles that appear on no other page.
- AI-friendly structure: question-led H2s, a direct first sentence under each, bullet lists, one sourced table, a FAQ with FAQPage JSON-LD.
- Humanizer style: no "not X but Y", no stock closers, no hype words, no em or en dashes anywhere in page content.
- Facts only from opened official pages. Pages may go beyond real estate (city facts, geography, history, economy, local rules) when tied to selling a house there.
- Sample/reference: the Los Angeles pages (29 are live and rewritten).
- Sources sections are NOT wanted on pages. The user asked to remove the "Sources / resources" H2 list from all pages that have it.

## 2. Standing rules from the user (obey exactly)
- "Never remove existing pages. Never noindex. Resolve overlap by page-type query groups; canonicals allowed for overlapping pairs."
- "Do not point any page to another page, start with uniqueness." "Do not merge any pages - keep all pages."
- Official sources only (state statutes, courts, state tax agencies, Census, FHFA, county assessor/recorder). No invented figures. No Zillow/Redfin numbers. Say plainly when something is not officially sourced.
- No curl or stealth proxy against government sites. Do not hunt for stored credentials.
- Do not get past captchas or bot detection (the user said I could; it is not permitted, so decline politely and use another source).
- Snippets are written OFF; the owner enables them in wp-admin.
- The Census API key the user supplied must never be repeated, written to files, or echoed. It is not in this repo. Do not ask for it again unless truly needed.
- User preferences: do not tell them all findings, only give built page links and ask if you need anything; finish quickly; keep working; short status messages.
- Firecrawl: the user wants to move away from it and it is out of credits. Do not use it.
- Permission prompts: the user already chose auto-accept and "Always allow" but per-site approval prompts persisted. This cannot be changed from inside the session. Tell the user if they come back.

## 3. Repository and pipeline
- Working copy: /home/claude/chb-pages (if the new chat has no such folder, clone the public repo alevsharma9-commits/chb-pages from GitHub; push with `git -c push.negotiate=true push -q origin HEAD`).
- Pages: pages/<st>/<name>.json, each item {slug,title,content,status,rank_math_title,rank_math_description,rank_math_focus_keyword}. manifest.json: {"version":1,"batches":[{"file":...}]}; the 97 files that contain rewritten pages are first.
- Baseline (original text) commit: 4a402a7. merge_rw.py always rebuilds pages from this baseline, so re-merging is idempotent.
- Agent drafts: gen/rw/<slug>.json = {slug, sections[{h2,html}], faqs[{q,a}], sources[{title,url}]}. 527 draft files exist.
- Batches: gen/rw/batches/b0001..b0916.txt (916 batches, 4 pages each; lines are "slug | keyword | title | file"). gen/rw/worklist.json lists all pages.
- gen/rw/finished.txt lists merged batches (merge_rw.py only merges slugs in these batches). Merged so far: b0001 to b0130 except those listed as pending below, plus b0115, b0118, b0121 to b0130 as listed in the file, b0123, b0127 (last).
- To merge a finished batch: `cd /home/claude/chb-pages && echo "bNNNN" >> gen/rw/finished.txt && gen/rw/cycle.sh "short commit message"`. The cycle runs, in order: gen/rw/dashfix.py (removes dashes in drafts) then gen/merge_rw.py (inserts a `<div class='chb-rw'>` block plus sections before `<div class='wsp-related'>`, appends a "More questions about X" FAQ and FAQPage JSON-LD) then gen/polish.py (removes old duplicated paragraphs) then gen/nosrc.py (removes Sources H2 lists) then gen/fixes.py (removes outdated old lines contradicted by new research) then gen/measure.py (prints median, counts) then gen/finish.py (validator: expects "3670 dups [] bad 0"), then git add/commit/push. Commits end with the attribution lines the harness gives.
- Latest cycle result: ">=80 uniq 490  >=1200 words 526", "3670 dups [] bad 0", pushed.
- gen/measure.py writes /tmp/measure.json with per-page words and uniqueness.

## 4. Live site updater (how pages reach the live site)
- WPCode snippet #43678 "CHB Page Updater": WP cron `chb_up_cron` every 5 minutes (fires on site visits), updates 15 pages per run from the GitHub repo. Option `chb_up_done` = list of repo files already processed; `chb_up_last` = last stats.
- Other snippets: #43263 Auto Builder, #44074 Hub Linker, #44075 Style Fix.
- NEVER edit a snippet: editing turns it OFF and the owner must re-enable it. Only change options via WP-CLI (`option update chb_up_done '[]' --format=json` resets it) and read via `db query`. Table prefix wp_58jtuq7go8_, site_url https://cashhomebuyersca.com.
- Count live rewritten pages: `SELECT COUNT(*) FROM wp_58jtuq7go8_posts WHERE post_type='page' AND post_status='publish' AND post_content LIKE '%chb-rw%'`. Last check: 29 LA pages live. Many merged pages (526 total) are not yet confirmed live; check and, if the updater skipped files, reset `chb_up_done` so rewritten files are reprocessed (manifest order puts rewritten files first).
- WPVibe tools: mcp__WPVibe_for_WordPress__run_wp_cli, rest_api, rest_api_write, get_page_html, site_info, code_snippet (read only; see snippet warning).

## 5. Status (about 11:35 am PT, Nov 15, 2026)
- 526 of 3,670 pages are over 1,200 words; 490 of those are at least 80% unique. About 3,150 pages remain.
- Roughly 30 rewritten pages sit at 72 to 79% unique and need a cleanup pass (examples: berkeley-county-wv 73%, fargo, grand-forks and bismarck ND about 79%). polish.py reduces overlap; some remain. Fix by removing or rewriting the remaining shared paragraphs in the rewritten block or old text.
- Stalled batches that wrote nothing because WebFetch hit its hourly cap: b0131, b0132, b0134, b0135 (and check b0133: an agent a2f2ccee2b6065ec3 may still be running; do not start a duplicate until it finishes or you confirm no files were written). Check others by testing whether gen/rw/<slug>.json exists for every line in the batch file. Batches b0136 to b0916 have not been started.
- A scheduled task (trigger trig_01J1BHEAiuijrdNsnsVau67T, 12:02 pm PT Nov 15) fires a fresh run to merge finished batches, relaunch stalled ones, and launch new ones. If you are the new chat, check list_triggers to avoid double-launching.
- Quality flags agents raised (pages tell readers to confirm with the office): SD security deposit 21 days vs 2 weeks; Dover NH tax interest 12%/18% vs state 8%; Concord NH installment dates; Arkansas homestead credit $675 vs $500/$600; Arkansas estate tax repeal source; thin or conflicting items for Oklahoma, Louisiana, Maryland; Iowa county pages with differing protest dates (Cass and Clayton counties; statute is Iowa Code 441.37, April 2 to April 30); Carroll County IA missing Census figures; Dallas County IA treasurer name may be out of date. Nebraska stamp tax was corrected to $3.32 per $1,000 (from July 18, 2026) in two county drafts. Outdated old lines removed: Iowa capital gains 10-year hold, Arkansas 2013 repeal.

## 6. Agent workflow
- Launch background general-purpose agents (sonnet works), at most 20 at once. Each gets: "Read /home/claude/chb-pages/gen/rw/TASK.md and follow it. Your batch id is bNNNN." TASK.md points them to gen/rw/BRIEF.md (page types, uniqueness rules, research tools, site preference) and their batch file.
- Agents write gen/rw/<slug>.json (1,300 to 1,800 words each) and report a table of slug, words, sources, facts left out. When one finishes, verify the files exist, then merge with cycle.sh.
- BRIEF.md research rules: WebSearch and WebFetch only for the web; prefer Wikipedia, Census, state .gov, official county sites (at most two or three county/city sites per page). HasData may be used only for non-government, non-captcha pages.
- Do not use the Composio workbench or any proxy for government pages.

## 7. Research tools and limits
- WebSearch returns titles/URLs; WebFetch reads pages. WebFetch has an hourly rate limit (RATE_LIMIT_EXCEEDED) that resets at the next UTC hour (20:00 UTC = noon PT). That cap is the bottleneck: roughly 60 to 100 pages of research per hour.
- HasData (mcp__HasData__hasdata_web_scraping_web_scraping_scrapeWebPage, tools load via ToolSearch with query "+hasdata"): the user connected it. It refuses all .gov URLs (422 notGovernmentUrl), Wikipedia returned 429 on the shared proxy, Justia returned a captcha. Use datacenter proxy and jsRendering false. It may work for city/county .com or .org sites, chambers of commerce and local news.
- Claude in Chrome extension: works in the user's own Chrome while open; slow; per-site permission prompts.
- Firecrawl: out of credits; user wants away from it.

## 8. Next steps in order
1. Wait for the WebFetch reset (noon PT), then relaunch b0131 to b0135 and start b0136 onward, up to 20 agents at a time.
2. Merge each finished batch with cycle.sh; confirm ">=1200 words" count rises and the validator prints "3670 dups [] bad 0".
3. Check the live site: rewritten-page count via the SQL above, and spot check with get_page_html that the Sources list is gone and the new sections render.
4. Re-measure uniqueness; fix rewritten pages under 80% (see section 5).
5. Give the user a short list of hyperlinks to rewritten live pages (they asked for links, not findings). Use hyperlink format.
6. Ask the user (do not assume) about: stripping Sources from the roughly 5,000 older California pages (offered, not confirmed); CA humanizer rewrite; county/city traffic opportunity research; chb-new-topic-pages.csv (116 pages); and the accuracy flags in section 5.

## 9. Things to avoid
- Do not remove, merge, noindex or redirect any page. Do not add links that point one page to another as a fix for overlap.
- Do not edit WPCode snippets. Do not echo the Census key or any credentials.
- Do not claim a page is live without checking the live site. Do not claim the rewrite is complete until the counts say so.
- No dashes in page text. No invented numbers. If an official page cannot be opened, leave the fact out or say it is unconfirmed.
