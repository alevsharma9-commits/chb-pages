import json,re
slug="nevada-squatters-rights-adverse-possession"
S=[]
def sec(h,html): S.append({"h2":h,"html":html})

sec("Do squatters have rights to a house in Nevada?",
"""<p>A squatter has no automatic right to a Nevada house. Title can pass by adverse possession only after a long, open and continuous claim that meets several statutes at once, and an unauthorized occupant can be removed through a court process the law spells out.</p>
<p>People use the word squatter for very different situations: someone who walked into a vacant house, a former tenant who stayed after a lease ended, an heir living in a parent's home, or a person who was let in by a fake landlord. Nevada treats these differently. A tenant who stays after notice falls under the landlord-tenant chapters, while a person who never had permission is handled as an unlawful or unauthorized occupant.</p>
<p>For a seller, the first question is which of these you are dealing with, because it decides the notice and the court.</p>""")

sec("What does it take to win title by adverse possession in Nevada?",
"""<p>The claimant has to meet requirements in more than one section of NRS chapter 11, and tax payment is one that many people overlook.</p>
<ul>
<li>Five years of occupation. NRS 11.150 requires, in addition to the requirements of NRS 11.120 or 11.140, that the land was occupied and claimed for 5 years, continuously.</li>
<li>Payment of taxes. The same section requires that the claimant or predecessors paid all state, county and municipal taxes levied and assessed for that period, or tendered payment.</li>
<li>Possession in a recognized form. For a claim not founded on a written instrument, NRS 11.140 deems land possessed only when it has been protected by a substantial enclosure or has been usually cultivated or improved.</li>
</ul>
<p>NRS 11.070 supports the five year frame from the owner's side. It says no cause of action founded on title to real property is effective unless the party or a predecessor was seized or possessed of the premises within 5 years before the act in question. An owner who pays the tax and keeps watch over the property makes the claimant's job much harder, because the claimant must show the taxes were paid or tendered.</p>
<p>None of this is easy to meet for someone who simply moved into a vacant house last month. Still, a claim can cloud title, and a clouded title is hard to sell.</p>""")

sec("How can an owner remove an unauthorized occupant in Nevada?",
"""<p>Use the court. The Civil Law Self-Help Center, a Clark County nonprofit legal service, describes a civil removal process that an owner can use whether or not anyone has been arrested, built around a 4 day notice to surrender.</p>
<table>
<thead><tr><th>Step</th><th>What the Self-Help Center describes</th></tr></thead>
<tbody>
<tr><td>1. Notice to Surrender</td><td>A 4 judicial day notice, which does not count the day of service, Fridays, Saturdays, Sundays or holidays</td></tr>
<tr><td>2. Service</td><td>Personally in front of a witness; or with a person of suitable age and discretion plus mailing; or posting plus mailing, in that order</td></tr>
<tr><td>3. Occupant responds</td><td>Leaves, or files an affidavit with a legal defense by the end of the fourth judicial day</td></tr>
<tr><td>4. Owner's complaint</td><td>Filed with the Justice Court with the notice and proof of service attached; the Center lists a $71 filing fee</td></tr>
<tr><td>5. Court review</td><td>A hearing within 7 judicial days if a defense is raised; otherwise a removal order, carried out by the constable or sheriff within 24 hours</td></tr>
</tbody>
</table>
<p>The notice must name the court, tell the occupant about the right to oppose it by affidavit, warn that a summary order could lead to removal within 24 hours, and say that the owner will provide safe storage of belongings for 21 days at the occupant's cost. An occupant can ask the court for up to 20 more days to move, but only in the answer filed within the four day window.</p>""")

sec("When can an owner change the locks after an arrest?",
"""<p>NRS 40.412 gives an owner a faster route in one narrow case: all known unlawful or unauthorized adult occupants have been arrested for housebreaking or unlawful occupancy, and any minor occupants have been taken into State custody. Only then may the owner retake possession and change the locks.</p>
<p>The statute attaches strict conditions. At the time the locks are changed, the owner or an authorized representative must post a written notice on the dwelling that identifies the address, the court with jurisdiction, and the date possession was retaken. The notice stays posted at least 21 calendar days, and a copy goes to the court within 1 day after the locks change, with an address for service.</p>
<ul>
<li>The occupant has 21 calendar days to contest by filing a verified complaint for reentry.</li>
<li>Reentry without a court order is a criminal offense, punishable by up to 4 years in prison.</li>
<li>The owner must provide safe storage of remaining personal property and can dispose of it after 21 calendar days unless the occupant files an affidavit under NRS 40.414.</li>
<li>The section does not apply if any unlawful or unauthorized occupant is still occupying the dwelling.</li>
</ul>
<p>The last point is the one owners miss. If someone is still living there, this section does not authorize a lock change.</p>""")

sec("How is a tenant who stays different from a squatter?",
"""<p>A tenant is someone who entered with permission under a lease or agreement, and the notice rules differ. Under NRS 40.2516, a tenant who fails to perform a condition of the lease and does not comply within 5 days after written notice is guilty of an unlawful detainer, and the landlord may then seek possession under the summary eviction statutes.</p>
<p>That is a different clock and a different notice from the 4 judicial day surrender notice for an unauthorized occupant. Use the notice that matches the occupant's status. Our <a href="/nevada-landlord-tenant-law-tenant-rights/">Nevada landlord tenant guide</a> covers the tenant side.</p>
<p>When the occupant is a relative who has moved into an inherited house, or someone who says they were promised the property, treat it as a question for an attorney. Those claims sometimes rest on documents or payments, and the quick removal process is built for people with no right at all.</p>""")

sec("How does an occupied house affect a sale?",
"""<p>An occupied house can still sell, but the buyer needs a clear path to possession. A traditional buyer with a lender usually wants an appraisal, an inspection and a vacant property at closing, and an unauthorized occupant can stall every one of those steps.</p>
<p>Owners often have three questions at this point: who is living there, what paper they hold, and what the county shows as the owner of record. A look at the recorder's records and the treasurer's account tells you whether the tax is current, which matters because the five year tax requirement in NRS 11.150 works in the owner's favor when the owner has paid.</p>
<ol>
<li>Document the occupancy with photos, dates and any police report numbers.</li>
<li>Keep the property taxes current, and keep the receipts.</li>
<li>Choose the right notice, civil removal or tenant eviction, and serve it exactly as the court rules require.</li>
<li>Do not turn off utilities, remove belongings or change locks outside NRS 40.412 without legal advice.</li>
</ol>
<p>We buy Nevada houses as-is, including houses with occupants or damage left behind. If you are weighing a removal case against a direct sale, we can talk through both and look at your timeline without any obligation.</p>""")

F=[
("How long does adverse possession take in Nevada?",
"The statute requires 5 years of continuous occupation and claim, plus payment of all taxes levied for that period, or a tender of payment (NRS 11.150). Possession must also meet NRS 11.140 if no written instrument is involved."),
("Can a squatter claim my Nevada house if I pay the property taxes?",
"The claimant must show that taxes for the 5 year period were paid by the claimant or predecessors, or tendered. If the owner paid them, that requirement is hard to meet (NRS 11.150)."),
("Can I change the locks on an occupied Nevada house?",
"Not under NRS 40.412 while any unlawful or unauthorized occupant is still living there. The section applies only after all known adult occupants have been arrested and minors taken into State custody, and reentry without a court order can be a crime."),
("How fast can an unauthorized occupant be removed in Nevada?",
"After the 4 judicial day notice and a Justice Court complaint, the Civil Law Self-Help Center says the constable serves a removal order requiring the occupant to leave within 24 hours. A hearing may be set within 7 judicial days if the occupant raises a defense."),
("Who stores belongings left in the home after a Nevada removal?",
"The owner must provide safe storage for 21 days, and the occupant pays reasonable inventory, moving and storage costs before getting the property back (NRS 40.412; Civil Law Self-Help Center)."),
]
SRC=[
("NRS 11.150 Additional requirements for adverse possession","https://law.justia.com/codes/nevada/chapter-11/statute-11-150/"),
("NRS 11.070 Seizure or possession within 5 years","https://law.justia.com/codes/nevada/chapter-11/statute-11-070/"),
("NRS 11.140 What constitutes adverse possession (no written instrument)","https://law.justia.com/codes/nevada/chapter-11/statute-11-140/"),
("NRS 40.412 Housebreaking and unlawful occupancy; retaking possession","https://law.justia.com/codes/nevada/chapter-40/statute-40-412/"),
("NRS 40.2516 Unlawful detainer: possession after failure to perform conditions of lease","https://law.justia.com/codes/nevada/chapter-40/statute-40-2516/"),
("Civil Law Self-Help Center: Civil Removal Process","https://www.civillawselfhelpcenter.org/self-help/removals/civil-removal-process"),
]
exec(open('/home/claude/chb-pages/gen/rw_scripts/tail.py').read())
