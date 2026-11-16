# Follow-ups found during the rewrite run (check before final sign-off)
- MN deed tax: hennepin-county-mn-county-recorder uses .0034 / $1.70 (county page); ramsey-county-mn-county-recorder uses .0033 / $1.65 (statute text). Pick the current official value and make both agree.
- WA REET: many Washington pages cite the Jan 1 2027 breakpoints ($551,000 / $1,551,000 / $3,051,000); earlier breakpoints ($525,000 / $1,525,000 / $3,025,000) are given on some pages only. Make consistent.
- MO recording: SB 938 added $2 to recorder fees from Aug 28 2026; counties differ on whether the posted $26 already includes it. Re-check Missouri recorder pages.
- Pages that name individual officials from county pages (Missouri property tax pages: Camden, Cape Girardeau, Cass, Callaway): names go stale; consider removing.
- Uniqueness: pages merged before the overlap gate (batches b0289 to b0346) are mostly 70 to 85% unique. Rework pass needed.
- Publishing: the live updater (WPCode #43678) processes each manifest file once. After the last merge, reset chb_up_done again (Tools > CHB Page Updater > Reset progress).
- tennessee-eviction-notice has a single source (Tennessee Courts presentation).
- luzerne-county-pa-recorder-of-deeds: fees from Nov 2025 schedule; July 1 2026 schedule unopened. Recheck. pennsylvania-eviction-notice: one source.
- sell-my-house-fast-lebanon-pa: Lebanon County Sept 1 appeal deadline from a 2013 PDF; recheck.
- pennsylvania-landlord-tenant-law-tenant-rights: one source (AG guide). sell-my-house-fast-north-huntingdon-pa: tax figures from proposed 2026 budget; recheck.
- bullitt-county-ky-property-tax-guide: rate unit (cents per $100) inferred; recheck. boyle/bracken closing-tax sentences borrowed from other counties' sheriff pages; recheck.
- kentucky-transfer-on-death-deed: says no KY TOD statute exists (2024 HB 50, 2026 SB 34 stalled); verify. larue-county-ky: 2026 payment table from a newspaper notice; verify.
- grant-county-ky-property-tax-guide: sheriff page says 21% penalty Feb 1-Apr 15 vs KRS 10%; page reports both. graves-county-ky-county-clerk: address conflicts across sources. Recheck.
- new-jersey-eviction-notice: rests on 2008 reprint, newer amendments unchecked. new-jersey-homestead-exemption: closing-credit rule from older guide. new-jersey-transfer-tax: computed examples ($3,695 on $450k, $3,215 on $400k); verify.
- marshall-county-ky-property-tax-guide: 2026 delayed-billing schedule from a local newspaper; swap for sheriff page. webster-county-ky-property-tax-guide at 85%.
- NJ pages with computed transfer-fee examples (manchester, maplewood, marlboro, medford, monroe-middlesex etc): own arithmetic from state rate schedule; verify.
- PRIORITY: NJ pages with self-computed realty transfer fee examples may be wrong (agents assumed marginal brackets; one example $3,695 on $450k does not match my own marginal check). Before final reset, verify against the Division of Taxation RTF table or strip the dollar examples: new-jersey-transfer-tax, new-jersey-closing-costs, sell-my-house-fast-*-nj pages from b0539 on (grep 'transfer fee').
- michigan-estate-tax: official page unopened; verify. michigan-tax-deed-and-tax-lien-sales covers forfeiture/foreclosure only.
- MI pages with self-computed transfer tax examples (b0581 houghton/huron/ingham register pages, b0602 hamtramck/holland/jackson/kalamazoo): verify against MCL 207.504/207.525 or strip dollar examples.
- Danville IL (sell-my-house-fast-danville-il) vacant-building rules from 2011 ordinance; Normal IL rental code 2016 PDF; recheck.
- Shared /tmp scratch collisions: agents overwrote each other's gen scripts; holmes/huron/crawford/columbiana OH recorder pages may have been regenerated from another agent's script. Final QA: rerun overlap.py + _count.py on every merged slug and diff vs sources.

## Added on resume (merge of b0673-b0715)
- Merged below 85% gate (rework later, all still >=80%): medina-county-oh-recorder-of-deeds 84, miami-county-oh-property-tax-guide 84, sell-my-house-fast-athens-oh 84, sell-my-house-fast-beavercreek-oh 84, sell-my-house-fast-elyria-oh 84.
- Wikipedia cited for census figures on many drafts (b0692, b0712 and older). Owner rule says official pages only: swap to Census QuickFacts or drop.
- alpharetta-ga-property-tax-guide: claims city bills its own property tax, inferred not stated by an opened page. Verify.
- Agents wrote to shared /tmp/claude-0 (b0683, b0714 and others): QA scripts-collision pages.
- wayne-county-oh-property-tax-guide: conveyance rate $4 per $1,000 vs older $2 snippets; recheck.
- Washington County OH recorder FAQ answers matched to guessed questions; recheck.
- sell-my-house-fast-sandy-springs-ga: demographics taken from Wikipedia's Census-cited figures. Swap to QuickFacts or drop.
- lady-bird-deed-texas: table rests on one State Law Library page; needs legal check before relying on it.
- georgetown-tx-property-tax-guide: states $0.363167 as 2026 levy, adoption not confirmed on an official page (notice prints proposed/voter-approval rate). Verify or reword.
- TX clerk fee conflicts: cameron-county-tx and hidalgo-county-tx pages quote a clerk-printed $35 first-page fee vs state manual $5; pages tell readers to confirm. Recheck against current clerk fee schedules.
- north-carolina-closing-costs 84, north-carolina-eviction-process 85 (merged); old NC probate page said register of deeds acts as probate judge, new page says clerk of superior court: check other NC pages for the old claim.
- merged below gate: lenoir-county-nc-property-tax-guide 84.

Added this session (NC b0787-b0808, TX b0822-b0839 merges)

* Merged below 85% gate: sell-my-house-fast-mcallen-tx 84.
* Rates stated as adopted from an official page: sell-my-house-fast-killeen-tx (73.01 cents, city home page), sell-my-house-fast-leland-nc (FY26-27 7.4% reduction), wake-county-nc-property-tax-guide (53.71 cents), sell-my-house-fast-league-city-tx, leander-tx, lewisville-tx (two printed rates .419009 and .422435), deer-park-tx, hurst-tx. Verify.
* Conflicting official figures: pitt-county-nc-register-of-deeds ($56 county page vs $64 statute for deeds of trust), pender-county-nc-property-tax-guide (appeal deadline Dec 31 2026 vs old June 30), wilson-county-nc-property-tax-guide (Jan 6 vs old Jan 5), warren-county-nc-register-of-deeds (county fee page dated vs G.S. 161-10).
* Dated figures on pages: sell-my-house-fast-frisco-tx (fiscal 2021 report), sell-my-house-fast-grand-prairie-tx (FY2024-25 rates), sell-my-house-fast-high-point-nc (older city report), sell-my-house-fast-garland-tx (STR ordinance hearing Oct 20 2026 outcome unknown).
* Census QuickFacts was bot_blocked for most agents; many new city pages carry no Census figures.
* Merged below 85%: sell-my-house-fast-mission-tx 84. Rate stated adopted: sell-my-house-fast-missouri-city-tx (0.578363, city page). Unsourced edge sentences possible: new-braunfels-tx, nacogdoches-tx (flood, tree-storm remarks).
* texas-eviction-notice and texas-eviction-process rest on 2 sources (Dec 2025 Rule 510 order, SLL). texas-deed-of-trust 6 sources from tx.md only. Verify.
* Merged below 85%: texas-eviction-notice 84.
* sell-my-house-fast-paris-tx: protest deadline conflict (Lamar CAD May 31/30 days vs state May 15); page defers to reader's notice.
* texas-mechanics-lien-home rests on 2 sources; texas-community-property-home-sale 4 sources; texas-intestate-succession and landlord-tenant-selling-rented-house 5 sources. Royse City figures from FY2025 budget (dated).
* texas-1031-exchange: no Texas-specific rules, 5 sources. sell-my-house-fast-weslaco-tx: building codes from 2017 listing (dated); TSHA history figures through 2000.
* Thin sourcing (2-3 sources): texas-security-deposit-rules (2), texas-real-estate-commission (3). texas-squatters-rights-adverse-possession 3/5-year rows from 1999 opinion, 25-year period not opened. texas-tax-deed-sales lacks Tax Code ch. 33/34 steps. texas-small-estate-affidavit statute text unopened. tarrant-county-tx-property-records merged at 84.
* TX recording fee conflict: travis-county-tx-property-records and texas-warranty-deed use Travis $25 first page vs state manual $5. tyler-tx-property-tax-guide states 2026 rates adopted (Smith County Truth in Taxation table). texas-transfer-on-death-deed, texas-warranty-deed have 4 sources. texas-housing-market: no median price data. texas-inheritance-and-estate-tax: no page stating no state estate tax.
* Rate stated adopted: sell-my-house-fast-schertz-tx (FY2026-27, no number). texas-property-tax-protest has 4 sources; texas-property-records says clerk/title co. re transfer tax (not confirmed). Waco and Tyler pages: county tax office vs city page conflict on tax sale format. Rockwall page I-30 dates from 2022 era.
* sell-my-house-fast-the-colony-tx cites 2022-23 rate (flagged past on page).
* FL: florida-foreclosure-process lacks SOL and answer period; eviction pages 4 sources. Brevard/Broward pages lack millage and fee schedules (sites bot_blocked). alachua-county-fl and boca-raton-fl 2026 millage labelled proposed. washington-county-tx-property-records: clerk fee $25 vs state $5 conflict. victoria-tx-property-tax-guide: rate called proposed.
* FL: florida-lady-bird-deed and florida-transfer-on-death-deed: lady bird description rests on a Florida Bar Journal reader letter (not official). florida-condo-hoa-selling 4 sources, no HOA/milestone statute. florida-1031-exchange: Pub 544 unopened. florida-tax-deed-sales lacks max certificate interest. Merged below 85: escambia-county-fl-property-tax-guide 84.
* florida-reverse-mortgage-selling-inheriting cites HUD 2019 PDF (dated). florida-real-estate-contract-inspection-period covers disclosures only. fort-myers-fl-property-tax-guide: Amendment 3 stated as passed per Lee tax collector (verify).
* florida-property-tax-appeal 5 sources; florida-property-tax-guide lacks certificate redemption/max interest; florida-housing-market has no sale price data.
* Merged below 85%: jefferson-county-fl-property-tax-guide 84.
* FL conflicts: highlands-county-fl-property-tax-guide homestead deferral Jan 31 (collector) vs Mar 31 (DOR). hillsborough pages: 2026 homestead amendment status unclear (appraiser says proposed); 3% interest and 18% certificate bid from collector FAQ.
* Miami-Dade pages state 2026 millage as adopted (county chart); miami-beach-fl two millage lines (18.6681 and 19.4045) deferred to bill.
* cape-coral-fl-property-tax-guide states 5.1471 mills adopted (city news). citrus-county-fl: installment penalty omitted (collector pages disagree). Manatee 2026 discount window ends Dec 3 per collector page.
* Rates: port-st-lucie-fl 4.8750 mills = approved at July workshop (not final). orlando-fl 0.00665 as printed. An agent edited gen/rw/overlap.py (env N); reverted.
* sell-my-house-fast-altamonte-springs-fl history from 2009 county profile (dated). sell-my-house-fast-casselberry-fl and boynton-beach-fl thin city sources. sell-my-house-fast-cape-coral-fl rests on Lee appraiser dates + state notes only. pinellas pages cite Escambia page for Amendment 3.
* sell-my-house-fast-apopka-fl uses FY2022-23 city profile (dated); boca-raton-fl uses 2020 comp plan.
