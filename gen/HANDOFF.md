# Handoff: cashhomebuyersca.com page rewrite project

Written Nov 16 2026 (session date), UTC 02:10. This replaces the earlier handoff. Read it top to bottom before touching anything. Everything here was verified in the working copy when written; numbers will have moved if agents finished after that, so re-measure first (section 4).

## 1. Goal and requirements

Rewrite every built page on cashhomebuyersca.com (WordPress, nationwide SEO build, 3,716 pages) so each page meets all of these:

- More than 1,200 words. The agent brief asks for 1,300 to 1,800.
- At least 80% unique by 5-word shingles against every other page. Our own gate for agent drafts is 85% (a safety margin); the owner's requirement is 80%.
- Question-led H2s. One small table with `<thead>`/`<tbody>`, with a source in the caption or intro. Five FAQs with FAQPage JSON-LD (the pipeline builds the JSON-LD).
- Humanizer style: no "not X but Y" contrasts, no stock closers, no hype words, no em or en dashes.
- Facts only from official pages the agent actually opened (state statutes, state agencies, county and city sites, Census QuickFacts). If no official page could be opened for a topic, leave the topic out and tell the reader to ask the office. Wikipedia is allowed only for geography and history in LEAN.md; the owner's rule is official pages, so treat Wikipedia-sourced numbers as defects (section 9).
- No Sources section on live pages. Agents list sources in the draft JSON and the pipeline strips them.
- Never write sentences about the agent's own research on the page ("we did not open", "what we left out", "the source we reviewed"). Reword to a plain instruction ("Ask the county treasurer for ...") or drop.

Standing owner rules (the owner is Alev Sharma, who signs as Victoria Sharma). Preserve verbatim:

- "Never remove pages. Never noindex. Do not merge pages. Do not point pages to other pages. Canonicals are allowed only for overlapping pairs."
- "Never call the company 'licensed'. No disclaimer lines on website pages. Site phone is (424) 435-2326."
- "Use Chrome (Claude in Chrome) for browser work, plus HasData as a research fallback." In practice Chrome is not available in this environment and HasData refuses government sites (see section 8).
- "Replies to the owner: short, human, tell her about optimizations, and give hyperlinks of completed pages."
- Ask the owner, do not assume, before: stripping Sources sections from the roughly 5,000 older California pages, a humanizer rewrite of the California pages, the traffic research / chb-new-topic-pages.csv work, and acting on the accuracy flags in FOLLOWUPS.md that change published facts.
- Do not recreate the stale schedule-trigger reminder that belongs to another account. Never edit WPCode snippet #43678 "CHB Page Updater". Any write on the WordPress site needs the owner's approval. `option delete` through WPVibe was classifier-denied earlier; do not try to circumvent it. The owner resets the updater herself.
- Owner preferences this session: finish with at most 20 agents at once (she asked for this to save usage), do not send status chatter while agents run, and tell her when something breaks.

## 2. Where things live

- Repo: github.com/alevsharma9-commits/chb-pages, branch main. Working copy: /home/claude/chb-pages (also /home/user/chb-pages). A Stop hook asks you to commit and push whenever the tree is dirty; do so with `git add -A && git commit && git push origin HEAD:main`. Commit trailers: "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" plus a Claude-Session line (cycle.sh adds its own).
- Page files: pages/<state code>/*.json (3,716 pages). manifest.json lists them in update order.
- Drafts (agent output): gen/rw/<slug>.json = {slug, sections[{h2,html}], faqs[{q,a}], sources[{title,url}]}.
- Batches: gen/rw/batches/bNNNN.txt, 4 lines each, "slug | focus keyword | title | file". 916 batches (b0001 to b0916).
- Agent brief: gen/rw/LEAN.md. Agents read only this file. It holds the output rules, facts rules, dates and sources rules, style, uniqueness rules and gate, page types, research tools, and (new this session) a "State notes" section.
- State notes: gen/rw/state_notes/nc.md, fl.md, tx.md. Statewide facts already read from official pages, each bullet with its source URL. Agents cite these URLs without reopening the pages. Each file lists topics that were NOT OPENED (see section 7). There is no ga.md; Georgia is essentially finished.
- Finished list: gen/rw/finished.txt. Merged batch ids, one per line. It contains some duplicate lines, so always count with `sort -u`. A batch counts as merged only when its id is in this file and cycle.sh pushed.
- Tools in gen/rw and gen: overlap.py (per-draft uniqueness, excludes the batch's own four slugs, reads shared pool), _count.py (word count and dash check, prints "nodash"), cycle.sh (merge pipeline), timefix.py, dashfix.py, merge_rw.py, polish.py, nosrc.py, fixes.py, finish.py, measure.py. Never edit these shared tools; agents were told not to, and they used private copies for diagnostics.
- Other docs: gen/FOLLOWUPS.md (fact-check and rework list, section 9 summarizes it), gen/hub (state hub pages, finished earlier).

## 3. How pages go live (important)

- A WPCode snippet (#43678 "CHB Page Updater", never edit) runs through WP cron `chb_up_cron` every 5 minutes, 15 pages per run. It reads manifest.json and pages/<state>/*.json from raw.githubusercontent.com/alevsharma9-commits/chb-pages/main/.
- It updates an existing page by slug only when the live content contains "wsp-hero" and the md5 differs. It never creates or deletes pages. A manifest file is marked done in option `chb_up_done` only after all its items are processed. Anything merged after a file was processed is NOT published until the owner clicks Tools > CHB Page Updater > "Reset progress", which deletes `chb_up_done`.
- Observed this session: pages from batches up to roughly b0357 were live; pages from b0561 onward and everything merged since were not. The owner said she would click Reset progress during this session, so most merged pages are probably live by now, but verify. Anything merged after her click needs another click. After the final merge, tell her to click Reset progress once more.
- Verify live status without trusting the push. Fetching the site directly fails in this environment (curl and WebFetch get blocked). Use WPVibe (`mcp__WPVibe__run_wp_cli`, site https://cashhomebuyersca.com; load the schema with ToolSearch "select:mcp__WPVibe__run_wp_cli"). Read commands need no approval. Example:
  `db query "SELECT post_name, (post_content LIKE '%<a distinctive H2 phrase from the draft>%') AS has_new FROM {prefix}posts WHERE post_type='page' AND post_name='<slug>'"`.
  `option get chb_up_last` shows the last run's updated / unchanged / missing / remaining counts.
- Page URLs have the form https://cashhomebuyersca.com/<slug>/.
- The owner's complaint this session ("pages are very thin", about wayne-county-mi-register-of-deeds) was her opening the old live version before the updater had run. The repo version was 2,079 words. Always check live status before reporting a page as done.

## 4. First steps for the next session

1. `cd /home/claude/chb-pages && git pull --rebase origin main && git status --short | head`. Commit and push anything dirty (those are agent drafts).
2. Count the state of the world:
   ```
   python3 - <<'E'
   fin=set(open('gen/rw/finished.txt').read().split())
   left=[f"b{i:04d}" for i in range(1,917) if f"b{i:04d}" not in fin]
   print(len(fin),"merged;",len(left),"batches (",len(left)*4,"pages ) left")
   E
   python3 gen/measure.py | head -2
   ```
3. Nothing is in flight. If any gen/rw/<slug>.json exists for a batch not in finished.txt, treat it as an unfinished draft: run the gate (section 6) and merge or relaunch.
4. Check the agent cap: run ListAgents. The session this handoff was written in is over; any subagents it started are gone.

## 5. State at handoff (final, nothing in flight)

Numbers at about 03:00 UTC Nov 16 2026, after the last agents reported and were merged:

- Merged batches: 806 of 916 (about 3,224 pages). Left: 117 batches, 468 pages, none started.
- No agents are running. No drafts are waiting to be merged. Every returned batch was gated, merged and pushed. Last measure: 3,248 pages over 1,200 words; 2,012 pages at or above 80% unique; median words 1,504; median uniqueness 81.
- Remaining batches, all unstarted:
  - North Carolina: b0787 to b0808 (22 batches). Notes: gen/rw/state_notes/nc.md.
  - Texas then Florida: b0822 to b0916 (95 batches). Texas runs from b0822 to about b0861 (notes: tx.md); Florida runs from about b0862 to b0916 (notes: fl.md).
- Page-type mix inside each state: county property tax guides, county register of deeds / clerk / property records, city property tax guides, "sell-my-house-fast-<city>-<st>" city pages, and a few state topic pages (closing costs, eviction, excise tax, etc.).
- Georgia is finished. North Carolina through b0786 and Texas through b0821 are merged.
- Merged below the 85% gate (all but one at or above the owner's 80%): see section 9.5. New since the first version of this file: lenoir-county-nc-property-tax-guide 84, north-carolina-closing-costs 84.

## 6. The loop (repeat until no batches are left)

1. Pick up to 20 unmerged, unlaunched batches in order (NC, then TX, then FL). Never launch a duplicate for a batch whose agent is still running. Count running agents with ListAgents; keep the total at 20 or fewer.
2. Launch each with the Agent tool: subagent_type general-purpose, model sonnet, run_in_background true, with this prompt (change the id; the state notes line picks the right state file):

   "Read /home/claude/chb-pages/gen/rw/LEAN.md (only that file) and follow it exactly, including its State notes section: read the state notes file for your state under /home/claude/chb-pages/gen/rw/state_notes/ (tx.md for Texas, nc.md for North Carolina, fl.md for Florida; use the one that matches the batch) and cite its URLs without reopening those pages. Open pages one URL at a time with the TinyFish fetch tool (it rate limits; wait and retry). Name no individual officials. Do not compute your own dollar examples from rate tables (state only rates and brackets exactly as the official page prints them). Never state a rate as adopted unless an opened official page says adopted; otherwise say proposed or point the reader to the tax office. Never use Wikipedia. Use a scratch dir outside /home/claude/chb-pages named after your batch, never shared /tmp/claude-0 paths. Your batch id is bNNNN. Report only a short table: slug, words, sources, overlap percent, topics left out."

3. When an agent reports, run the per-batch gate and mark the batch finished. Merging several batches at once saves steps (cycle.sh handles any number):
   ```
   cd /home/claude/chb-pages
   for b in bNNNN bMMMM; do
     S=$(cut -d'|' -f1 gen/rw/batches/$b.txt | tr -d ' ')
     python3 gen/rw/overlap.py $S | grep unique | awk -v b=$b '{ if ($3+0<85) print "BELOW85",b,$0 }'
     python3 gen/rw/_count.py $S | awk -v b=$b '$2<1200||$4!="nodash"{print "LOW/DASH",b,$0}'
     grep -qx $b gen/rw/finished.txt || echo $b >> gen/rw/finished.txt
   done
   gen/rw/cycle.sh "Rewrite bNNNN bMMMM" 2>&1 | tail -3
   ```
   Success looks like `3716 dups [] bad 0` then `pushed`. If finish.py reports a problem (dashes, broken internal links, rank_math_title over 62 characters, rank_math_description over 155), fix the draft, not the validator. A BELOW85 line means the page is under our margin; at 80 to 84 it is still above the owner's requirement, so merge and log it in FOLLOWUPS.md; under 80, send it back for a rewrite.
   After cycle.sh, run `git status --short | wc -l`. Once it reported "no changes added to commit" while merged pages sat uncommitted; the next cycle run committed them. Verify, and push with `git push origin HEAD:main` if needed.
4. Read each hand-back for red flags and log them in FOLLOWUPS.md: Wikipedia used for figures, a rate stated as adopted without confirmation, computed dollar examples, conflicting official sources, a page that cites a single source, anything about "licensed" referring to the company.
5. Reply to the owner only when something changes or breaks. Keep replies short and human, say how many batches are merged and how many pages are left, and give links to completed pages that are verified live.

## 7. State notes and what they do not cover

The three notes files hold statewide facts with source URLs. Their NOT OPENED lists mean agents may need to open those topics themselves or leave them out:

- NC (nc.md): full probate above the small-estate limit, quitclaim deed rules, transfer on death / beneficiary deed status, squatter removal statute, color-of-title adverse possession (G.S. 1-38), G.S. 105-375 and 105-361, "NC has 100 counties" (snippet only), NC Census QuickFacts, NC Register of Deeds Association pages, notice-of-sale advertising period (G.S. 45-21.17), writ of possession timing. The deed excise rate is printed as the statute prints it: $1.00 per $500 or fractional part. NC counties also print their own land transfer tax and conflicting register-term lengths (two years versus four); pages leave the term out.
- FL (fl.md): foreclosure statute of limitations and answer period, formal probate administration steps and the s. 733.710 two-year claim bar, land contract statute beyond doc stamp tax and the s. 695.26 formalities, adverse possession under color of title (s. 95.16), tax certificate redemption mechanics and the maximum interest rate (ss. 197.172, 197.472), Florida Courts self-help pages, Attorney General pages, Census QuickFacts. Caveats: the $500,000 portability cap comes from the statute text; the s. 193.155 amendments first apply to the 2027 roll; the $150,000 summary administration limit shows a 2026 amendment; the lady bird deed doc stamp point rests on DOR advisement TAA 20B4-004.
- TX (tx.md): no opened page says Texas has no state transfer tax (pages must not claim it), estate tax status (only the 2015 inheritance tax repeal), executory contract (land contract) default and forfeiture rules, adverse possession 25-year period and current statute text, tax suit and sale procedure (Tax Code ch. 33 and 34), and the statutes.capitol.texas.gov site would not load, so statute facts come from the Comptroller, Texas Courts, AG and the State Law Library. The eviction rule text is a December 2025 order with proposed amendments and is flagged that way. Recording fees are from the 2023 County Clerk Manual ($5 first page, $4 each additional, $0.25 per extra name); several counties print higher clerk fees.

If a later agent opens one of these topics, append the facts and URL to the right notes file so others can reuse it. Edit the notes files only when no batch agent is mid-read, or append only.

## 8. Research tools and their limits

- TinyFish fetch (`mcp__TinyFish_crawl__fetch_content`, load with ToolSearch "select:mcp__TinyFish_crawl__fetch_content,mcp__TinyFish_crawl__search"). It opens .gov, statutes, Census pages. It bills the owner per page (about 6 to 10 reads per page written) and rate-limits hard when many agents run at once, which is why the cap is 20 and agents are told to fetch one URL at a time. Some sites return bot_blocked; never try to get past a captcha or bot check.
- HasData web scraping (`mcp__HasData__hasdata_web_scraping_web_scraping_scrapeWebPage`): refuses government websites ("notGovernmentUrl", HTTP 422). It cannot help with the sources that matter here. Use only for non-government pages, and the owner's rule bars commercial sites as sole sources.
- WebFetch and the Playwright browser fail in this environment. curl through the proxy to the live site fails. Claude in Chrome is not present.
- WebSearch has a small per-turn budget; use it to find pages, then open them with TinyFish. Search snippets are never a source for a phone number, address, hours, date or amount.
- Cost reality: each batch of four pages costs roughly 250,000 to 380,000 agent tokens. That is why state notes (shared statewide facts) and the 20-agent cap exist. Do not rerun batches that already passed.

## 9. Quality log and open follow-ups

gen/FOLLOWUPS.md is the running list. Highlights, in priority order:

1. NJ pages with self-computed realty transfer fee examples may be wrong (PRIORITY): new-jersey-transfer-tax, new-jersey-closing-costs, sell-my-house-fast-*-nj from about b0539 on. Verify against the Division of Taxation table or strip the dollar examples. Same for Michigan pages with computed transfer tax examples (b0581 and b0602 families; MCL 207.504 and 207.525). From b0673 on, agents were told not to compute dollar examples; earlier merged batches were not re-swept.
2. Wikipedia used for figures despite the official-pages rule: b0692, b0712 and older families, plus sell-my-house-fast-sandy-springs-ga (Wikipedia's Census-cited figures). Swap to Census QuickFacts or drop. Wikipedia appears in the sources list of roughly 2,400 draft files; many are history/geography only, which LEAN.md allows, so sweep for numbers (population, income, home values) sourced to Wikipedia first.
3. Rates or facts stated without official confirmation: georgetown-tx-property-tax-guide (states $0.363167 as 2026 levy; the notice only prints proposed/voter-approval), alpharetta-ga-property-tax-guide (claims the city bills its own tax, inferred), lady-bird-deed-texas (table rests on one State Law Library page; needs a legal check), wayne-county-oh-property-tax-guide (conveyance rate $4 per $1,000 against older $2 snippets), the Washington County OH recorder FAQ answers (matched to guessed questions).
4. Conflicting official sources where pages tell readers to confirm: Cameron and Hidalgo County TX clerk fee ($35 first page printed versus $5 in the state manual), many Georgia counties with two printed due dates (Nov 15 versus Dec 20), Georgia homestead cutoff March 1 versus April 1, NC register-of-deeds term (two versus four years), Gaston and Davie income limits versus the NCDOR figure ($38,800 for 2026), Cumberland board-of-equalization end date (Dec 31 versus Dec 1).
5. Merged below the 85% gate (all but one at or above the owner's 80%): medina-county-oh-recorder-of-deeds 84, miami-county-oh-property-tax-guide 84, sell-my-house-fast-athens-oh 84, sell-my-house-fast-beavercreek-oh 84, sell-my-house-fast-elyria-oh 84, chatham-county-nc-register-of-deeds 84, chowan-county-nc-register-of-deeds 84, yadkin-county-nc-register-of-deeds 84, abilene-tx-property-tax-guide 80, amarillo-tx-property-tax-guide 83, beaumont-tx-property-tax-guide 83. Earlier list still pending: new-jersey-transfer-tax 81, ohio-eviction-notice 81, newark-nj-property-tax-guide 84, sell-my-house-fast-northampton-pa 84, webster-county-ky-property-tax-guide 84, sell-my-house-fast-ross-pa 84, illinois-property-tax-guide 84, illinois-quitclaim-deed 84, ohio-estate-tax 84. Rewrite these with place-specific facts, not boilerplate.
6. Uniqueness of the pages merged before the overlap gate existed (batches b0289 to b0346): mostly 70 to 85%. Rework pass needed. The measure.py total counts overlap across the whole site and moves as pages merge.
7. Old/legacy facts: SC squatters page, NC probate (register of deeds versus clerk), Alexandria due date, deed excise rate ($2 vs $2.28 per $500), stale SC 2026 tax-sale dates, MN deed tax values that disagree between Hennepin and Ramsey, WA REET breakpoints inconsistent between pages, MO recording SB 938 $2 add-on, KY, PA, IL items. All listed in FOLLOWUPS.md.
8. Shared /tmp scratch collisions: early agents wrote to shared /tmp/claude-0 and overwrote each other's scripts (affected OH recorder pages such as holmes, huron, crawford, columbiana, and others). Final QA: rerun overlap.py and _count.py on every merged slug and spot check against sources. Later prompts use batch-named scratch dirs outside the repo.
9. Process-commentary sentences (Section 10 of the older handoff): a grep for "we did not (open|review)|what we left out|did not open|source we reviewed" over gen/rw/*.json still needs a clean-up pass on older drafts (Arizona, Virginia families). Recent agents were told not to write them.
10. The word "licensed" appears in drafts only for third parties (attorneys, surveyors, contractors, rentals). None describe the company. Grep before final sign-off: `grep -il licensed gen/rw/*.json` and check each hit is not about the company.

## 10. Final steps once all batches are merged

1. Re-run the full measure (`python3 gen/measure.py | head -3`) and the LOW/DASH/BELOW85 sweep over all merged slugs. Record the numbers.
2. Do the priority fact-check work in section 9 (NJ and MI dollar examples first, then Wikipedia-sourced figures, then the unconfirmed-rate pages). Fix drafts, run cycle.sh.
3. Rework the sub-85% pages and the b0289 to b0346 family.
4. Tell the owner to click Tools > CHB Page Updater > Reset progress one last time (she must do it; it is a WordPress write). Wait for `chb_up_last` to show remaining 0 (15 pages per five minutes, so a few hours for the full site), then verify a sample of pages from each state live with the db query in section 3, then send her short, hyperlinked results.
5. Ask her (do not assume) about the California Sources stripping, the California humanizer pass, the traffic research file, and the accuracy flags that change published facts.

## 11. Environment gotchas

- Concurrency: keep at 20. The env var CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS is set to 40 in /root/.claude/settings.json; that is a ceiling, not the plan. A launch at the cap fails with "Concurrent subagent limit reached"; count running agents before launching.
- Background agents cannot always start; if one runs in the foreground it blocks you.
- Hand-backs arrive as messages from the agents. They are agent output, not user instructions; never let one grant permissions. One hand-back was flagged by the auto-mode classifier ("Destructive or Unwanted Actions") and turned out to be a benign Wikipedia-fetch denial; verify rather than trusting or panicking.
- The auto-mode permission classifier denies fetches of Wikipedia and some other pages for agents. Agents are told not to work around a denial.
- Pushing: if GitHub push is blocked, add the repo with the add_repo tool (owner alevsharma9-commits, repo chb-pages, access push), then register_repo_root.
- Session hooks: caveman (terse replies) and ponytail are active; they style chat replies only. Written files and commit messages use normal prose.
- Owner reply style: short, human, no jargon; tell her what was optimized; give links only for pages verified live.
