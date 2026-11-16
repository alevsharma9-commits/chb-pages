# Polish brief (edit pass, NO new research)

You edit existing page drafts so they read like a careful human editor wrote them for a homeowner who may sell a house. The facts stay. The voice changes.
Read each original: /home/claude/chb-pages/gen/rw/<slug>.json  (keys: slug, sections [{h2, html}], faqs [{q, a}], sources).
Write the edited version to: /home/claude/chb-pages/gen/rw/polish/<slug>.json  (same keys; copy "sources" unchanged). Never edit any other file in the repo. Do not use web tools: use only facts already in the draft.

## What to fix
1. Source name-drops in the text. Remove "Wikipedia", "QuickFacts", "the Census Bureau says", "the page lists/notes/says", "according to ...". State the fact plainly ("Population is 62,314.", "The county sells tax liens in May."). One short mention of an official office as the place to call is fine ("Call the Treasurer's office").
2. Research-gap and conflict notes: "does not say", "could not confirm", "does not match", "still lists", "we left out", "no official source publishes". Delete the sentence, or replace it with one plain instruction ("Call the assessor for the current deadline."). Never tell the reader what we failed to find.
3. Expired items: any date already past (today is November 16, 2026) such as "deadline of July 16, 2026 has passed". Delete it, or state the recurring rule instead ("Claims are due each July.").
4. Filler that does not help a seller: Census trivia (veterans, broadband, poverty, bachelor's degree, labor force, payroll), employer lists, school lists, climate, long history, "how big is it". Keep ONE short context paragraph per page (population, housing, anything that affects price or selling). Cut the rest. If an H2 section is mostly filler, merge its one useful fact into another section or delete it.
5. Comparisons to sibling pages ("than in Delta County", "of the four cities covered in this series"). Delete.
6. Tables: keep one small table. Headers must be specific ("Payment option | Due date | Discount"), not "Item | Figure" or "Fact | Detail". No Source column, no "Source:" lines, no "The table below collects..." lead-in sentences. A short plain caption is fine.
7. Headings: today about 89% are questions. Make roughly half plain labels a person would scan for: "Due dates and penalties", "How to appeal your assessment", "Homestead exemption", "Selling with taxes owed". Keep a question heading only when it reads naturally. No heading that names the research ("What the sources say").
8. Tone and style (humanizer): plain, specific, varied sentence length, contractions are fine. Cut filler ("it is worth noting", "keep in mind", "navigate", "landscape", "crucial", "key", "robust", "seamless"), stock closers, bridge sentences ("That matters for a seller because..."), triads for rhythm, "not X but Y", hype. No em dashes or en dashes anywhere. Never call Cash Home Buyers CA "licensed". Do not mention wholesaling. No named officials. No computed dollar examples. No rate called "adopted" unless the draft already says an official page did.
9. FAQs: exactly 5, each answer 1 to 3 sentences, no source name-drops.

## Hard limits (a checker enforces these)
- Total words in sections + faqs: at least 1,300. If trimming filler drops you below, ADD seller-useful content built only from facts already in the draft: how the process works step by step, what to bring to the office, timelines, what happens at closing, what to do if taxes are owed, what a cash sale skips. Do not pad with filler.
- Do not introduce any number, date, dollar amount, rate or name that is not in the original draft.
- Keep each page's own place-specific facts: names, offices, dates, amounts. Do not make pages more alike: use your own fresh wording for each page, not shared boilerplate. At least 82% of 5-word phrases must be unique versus other pages (the checker measures it; aim higher by rewording shared state-rule sentences).
- Output must be valid JSON.

## Check your work
python3 /home/claude/chb-pages/gen/rw/polishcheck.py <slug> <slug> ...
It must print OK for every slug. Fix anything it flags and run it again. Then reply with one short table: slug, words, status. Nothing else.
