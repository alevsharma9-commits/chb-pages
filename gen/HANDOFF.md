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

## 3. Current state (Nov 15, 13:50 PT)

- 1,120 of 3,716 pages are over 1,200 words. That is 1,074 originals plus 46 state hubs.
- About 2,596 pages (649 batches, b0268 to b0916) have no draft yet.
- The 80% unique count is 735 pages, down from about 750 because the hubs repeat directory text. Roughly 76 or more rewritten pages are under 80% unique and need rework.
- All 46 out-of-state hubs are rewritten, built, pushed, and spot checked live (SC, TX, FL, OH). Each hub lists counties as H3 headings with county guide links and city links, like the California hub.
- 20 rewrite agents were launched at 13:40 for b0268 to b0287 (sonnet, background). They are not merged yet. Their drafts will appear as gen/rw/<slug>.json.
- Last git commit: 11faac5 "Add final 10 state hubs".

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
