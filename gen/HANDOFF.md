# Handoff: cashhomebuyersca.com page rewrite project

Written Nov 15 2026, about 13:50 PT. Read this top to bottom before touching anything.

## 1. Goal

Rewrite every built page on cashhomebuyersca.com (WordPress, nationwide SEO build) so each page meets all of these:

- More than 1,200 words.
- At least 80% unique by 5-word shingles against the other pages.
- Question-led H2s.
- One sourced table.
- FAQ section with FAQPage JSON-LD.
- Humanizer style: no "not X but Y" contrasts, no stock closers, no hype words, no em or en dashes.
- Facts only from official pages that were actually opened (state statutes, county and city sites). Leave a topic out and tell the reader to ask the office when no official page can be opened.
- No "Sources" section on live pages (the merge pipeline strips it).

Standing rules from the owner (Alev Sharma, signs as Victoria Sharma):

- Never remove pages. Never noindex. Do not merge pages. Do not point pages to other pages. Canonicals are allowed only for overlapping pairs.
- Never call the company "licensed". No disclaimer lines on website pages. Site phone is (424) 435-2326.
- Use Chrome (Claude in Chrome) for browser work, plus HasData as a research fallback.
- Replies to the owner: short, human, tell her about optimizations, and give hyperlinks of completed pages.

## 2. Where things live

- Repo: github.com/alevsharma9-commits/chb-pages. Working copy: /home/claude/chb-pages. Branch main.
- Page files: pages/<state code>/*.json (3,716 pages total). manifest.json lists them in update order.
- Rewrite drafts (agent output): gen/rw/<slug>.json = {slug, sections[{h2,html}], faqs[{q,a}], sources[{title,url}]}.
- Batches: gen/rw/batches/bNNNN.txt, 4 pages each, lines "slug | keyword | title | file". 916 batches exist.
- Agent instructions: gen/rw/TASK.md (points to gen/rw/BRIEF.md). Hub instructions: gen/hub/BRIEF.md.
- Finished list: gen/rw/finished.txt (233 ids merged so far, through b0267).
- Merge script: gen/rw/cycle.sh. Other tools in gen/rw: dashfix.py, merge_rw.py, polish.py, nosrc.py, fixes.py, measure.py, finish.py, _count.py.

## 3. Current state (Nov 15, about 14:05 PT, final for this session)

- 1,204 of 3,716 pages are over 1,200 words (1,158 originals plus 46 state hubs).
- 254 batch ids are in gen/rw/finished.txt (all merged and pushed, last commit 8d9fcc2 "Rewrite b0288").
- 628 batches still have no draft: b0289 onward (b0268 to b0288 are all done). That is about 2,512 pages.
- The 80% unique count is 754 pages. It moves up and down as batches merge because the Virginia and Arizona pages share statute wording. Rework the pages under 80% after the bulk rewrite.
- All 46 out-of-state hubs are done and live (spot checked SC, TX, FL, OH).
- NO agents are running. No new agents were launched after the user asked to stop. The user is handing this to a Claude Code session.
- Known quality issue: 27 merged drafts still contain process-commentary wording (see section 10). Fix before or during the next pass.
- Research limits seen this session: WebFetch hits its hourly cap on the first call, WebSearch has a small per-turn budget. Agents read pages through Claude in Chrome (own tab, text only). Many official county and city sites were blocked in Chrome ("could not verify safety category") or returned 404 on guessed URLs. Expect thin local sourcing: pages tell readers to ask the Treasurer, Assessor or Clerk.

## 4. The loop (repeat until no batches are left)

1. Find batches without drafts. A batch is done when every slug in it has gen/rw/<slug>.json:
   ```
   cd /home/claude/chb-pages && python3 - <<'E'
   import os,glob
   for f in sorted(glob.glob('gen/rw/batches/b*.txt')):
       if any(l.strip() and not os.path.exists('gen/rw/'+l.split('|')[0].strip()+'.json') for l in open(f)):
           print(os.path.basename(f)[:-4])
   E
   ```
2. Launch up to 20 background agents at once (the concurrency cap). Model sonnet, one batch each, with this prompt (change the id):
   "Read /home/claude/chb-pages/gen/rw/TASK.md and follow it. Your batch id is bNNNN. Note: BRIEF.md's CURRENT research section allows HasData and Chrome fallbacks when WebFetch is rate limited (it has an hourly cap), and WebSearch has a per-turn budget, so use it for finding pages and WebFetch for reading them. Leave out any fact you cannot confirm from an opened official page, do not rely on news blogs or commercial legal sites as sole sources, and where you cannot open a city or county official page for a topic, leave that topic out and tell the reader to ask the office. Report what you left out."
3. When an agent reports done and its 4 draft files exist, merge: `cd /home/claude/chb-pages && echo "bNNNN" >> gen/rw/finished.txt && gen/rw/cycle.sh "message"`. You can append several ids and run cycle.sh once. Success means the output shows "dups [] bad 0" and then "pushed". If finish.py fails, read what it flags (dashes, broken internal links, rank_math_title over 62, rank_math_description over 155) and fix the draft, not the validator.
4. Launch the next batch into the freed slot. Never launch a duplicate agent for a batch that is still running.
5. Commit trailers on every commit: "Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>" and "Claude-Session: https://claude.ai/code/session_01XzVF5gGxAc3JvRFXnQXt9Y" (cycle.sh already adds them).

## 5. How pages go live

- A WPCode snippet (#43678 "CHB Page Updater", never edit it) runs through WP cron `chb_up_cron` every 5 minutes, 15 pages per run. It reads the manifest and page JSON from the GitHub raw main branch.
- It updates an existing page by slug only when the live content contains "wsp-hero" and the md5 differs. It never creates or deletes pages. Option `chb_up_done` lists processed files.
- Last observed run: updated 60, unchanged 62, missing 12, remaining 174. Check progress with the WPVibe run_wp_cli tool (site https://cashhomebuyersca.com). Read commands need no approval. Writes need approval from the owner.
- Always verify a sample of pages live after a push (fetch the URL, look for the new H2s and word count) before telling the owner a page is live. Do not claim live status from the push alone.

## 6. Hub pages (done, but know how they work)

- Facts files gen/hub/facts/<code>.json, agent output gen/hub/out/<code>.json, builder `python3 gen/hub/build_hub.py <codes>`, and `gen/hub/addhubs.sh <codes>` builds and prepends to the manifest. To change a hub, edit gen/hub/out/<code>.json and rebuild that code, then push.

## 7. Open problems to work on next (in priority order)

1. Uniqueness: about 76+ rewritten pages are under 80% unique. Run measure.py, list the worst, and have agents rewrite sections with state or city specific content, not shared boilerplate. The hub directory text also lowered the count; consider varying the intro and FAQ wording per state.
2. Fact check pass: several hub and rewrite agents used the site's own topic pages or Nolo, HomeLight or Wikipedia without opening the primary source (examples: ID, WY, KY, CT, AZ, CO, ND, MO transfer tax; SC 27-37-30 came via a summary). Re-verify those against statutes or county pages, or remove the claim.
3. Contradictions with older live pages: SC squatters page (adverse possession subsections), NC probate (register of deeds vs clerk), Alexandria due date (Nov 15 vs Nov 16), and the deed excise rate ($2 vs $2.28 per $500). Decide the right value from the official page and make pages agree.
4. Thin local sourcing on many city pages (AL, MA, CT). Where no official page was opened, the page should say to ask the office.
5. Stale dates: some SC tax-sale dates for 2026 have already passed. Pages should say the date has passed or be updated.

## 8. Questions to ask the owner, not assume

- Stripping Sources sections from the roughly 5,000 older California pages.
- A humanizer rewrite of the California pages.
- Traffic research and the file chb-new-topic-pages.csv.
- The accuracy flags in section 7.

## 9. Tool notes and gotchas

- Agent cap is 20 concurrent. Some Agent calls ran foreground in this session ("Background agents cannot be started right now"); if that happens, expect them to block.
- WebFetch has an hourly cap and WebSearch has a per-turn budget. HasData scrape and Chrome work when those fail.
- Pushing: if GitHub push is blocked, add the repo to the session with the add_repo tool (owner alevsharma9-commits, repo chb-pages, access push), then register_repo_root.
- The user's schedule trigger list had a stale reminder meant for another account; do not recreate it.
- Report to the owner in a few short sentences: pages done, pages left, anything risky. Include hyperlinks to completed pages when asked.

## 10. Added later: process-commentary cleanup (important)

Some agents wrote sentences about their own research ("We did not open a city page", "What we left out", "the source we reviewed") into page text. The owner does not want disclaimer-style lines on website pages. Reword each to a plain instruction ("Ask the county treasurer for current rates") or drop it. Find them with: grep -l -i -E "we did not (open|review)|what we left out|did not open|source we reviewed" gen/rw/*.json. Fixed so far: Portsmouth, Richmond, Roanoke (b0277). Others (for example arizona-property-tax-guide, arizona-quitclaim-deed, arizona-recording-deeds, arizona-squatters-rights-adverse-possession, several Virginia pages) still need a pass, then rerun cycle.sh. Also add this rule to gen/rw/BRIEF.md so new agents stop writing it.
