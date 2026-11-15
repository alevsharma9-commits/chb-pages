# Follow-ups found during the rewrite run (check before final sign-off)
- MN deed tax: hennepin-county-mn-county-recorder uses .0034 / $1.70 (county page); ramsey-county-mn-county-recorder uses .0033 / $1.65 (statute text). Pick the current official value and make both agree.
- WA REET: many Washington pages cite the Jan 1 2027 breakpoints ($551,000 / $1,551,000 / $3,051,000); earlier breakpoints ($525,000 / $1,525,000 / $3,025,000) are given on some pages only. Make consistent.
- MO recording: SB 938 added $2 to recorder fees from Aug 28 2026; counties differ on whether the posted $26 already includes it. Re-check Missouri recorder pages.
- Pages that name individual officials from county pages (Missouri property tax pages: Camden, Cape Girardeau, Cass, Callaway): names go stale; consider removing.
- Uniqueness: pages merged before the overlap gate (batches b0289 to b0346) are mostly 70 to 85% unique. Rework pass needed.
- Publishing: the live updater (WPCode #43678) processes each manifest file once. After the last merge, reset chb_up_done again (Tools > CHB Page Updater > Reset progress).
- tennessee-eviction-notice has a single source (Tennessee Courts presentation).
- luzerne-county-pa-recorder-of-deeds: fees from Nov 2025 schedule; July 1 2026 schedule unopened. Recheck. pennsylvania-eviction-notice: one source.
