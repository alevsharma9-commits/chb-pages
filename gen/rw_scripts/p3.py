import json,re
slug="nevada-transfer-on-death-deed"
S=[]
def sec(h,html): S.append({"h2":h,"html":html})

sec("What does Nevada call a transfer on death deed?",
"""<p>Nevada's statutes call it a deed upon death. NRS 111.671 lets the owner of an interest in property convey it to one beneficiary or several, with the deed taking effect only when the owner dies. The rules sit in NRS 111.655 to 111.699.</p>
<p>The statute gives a model form in NRS 111.695. Its wording tells you most of what you need to know: the deed is revocable, it transfers no ownership until the grantor dies, and it revokes all earlier deeds upon death for the same real property. It must be signed, notarized and recorded with the county recorder before the owner dies, or it does nothing.</p>
<p>Because the form lists the county, city and legal description of the property, the safest approach is to copy those details from your current vesting deed. A typo in the legal description is the kind of problem that shows up years later, when the beneficiary tries to sell.</p>""")

sec("What can an owner still do while alive?",
"""<p>Nearly everything. NRS 111.685 says that during the owner's lifetime a deed upon death does not affect the owner's rights, including the right to transfer or encumber the property. The beneficiary gets no legal or equitable interest while the owner is alive.</p>
<p>The same section lists other effects the deed does not have:</p>
<ul>
<li>It does not affect any other permitted method of transferring the property.</li>
<li>It does not reduce the rights of the owner's secured or unsecured creditors, even if they know about it.</li>
<li>It does not affect the owner's or the beneficiary's eligibility for public assistance.</li>
<li>It does not expose the property to claims by the beneficiary's creditors.</li>
</ul>
<p>Two statutes cover changes of plan. Under NRS 111.677, if the owner transfers the property to someone else during life, the deed upon death is void. If the owner records more than one deed upon death for the same property, the last one recorded before death is the effective deed. That makes a new recorded deed a practical way to change beneficiaries.</p>""")

sec("What must happen after the owner dies?",
"""<p>The beneficiary must record a Death of Grantor Affidavit. NRS 111.699 says that on the death of the last grantor, a declaration of value (the form under NRS 375.060) and a copy of each grantor's death certificate must be attached to the affidavit and recorded in the office of the county recorder where the deed was recorded.</p>
<p>The affidavit identifies the deceased as the person named in the deed, gives the recording details of the deed and the property description, and states that the signer is a beneficiary or the beneficiary's authorized representative. It must be sworn before a notary.</p>
<p>Recording matters for a sale. Under NRS 111.689(9), a person who deals in good faith and for valuable consideration with a beneficiary has the same protections as if the beneficiary had been named in a final order of distribution, provided the Death of Grantor Affidavit was recorded. Without that recording, a buyer or title company has less to rely on.</p>
<table>
<thead><tr><th>Step</th><th>Who acts</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Sign, notarize and record the deed</td><td>Owner, before death</td><td>NRS 111.695, 111.681</td></tr>
<tr><td>Record Death of Grantor Affidavit with death certificate and declaration of value</td><td>Beneficiary</td><td>NRS 111.699</td></tr>
<tr><td>Publish notice to creditors and mail it to listed parties</td><td>Beneficiary</td><td>NRS 111.689</td></tr>
<tr><td>Wait for the claim period, then sell or distribute</td><td>Beneficiary</td><td>NRS 111.689</td></tr>
</tbody>
</table>""")

sec("Do creditors and Medicaid still have a claim against a Nevada deed upon death?",
"""<p>Yes. A deed upon death avoids probate for that property, but it does not erase debts. NRS 111.689 says that if the grantor's probate estate cannot cover an allowed claim or a statutory allowance to a surviving spouse or child, the estate may enforce the liability against property that passed by the deed.</p>
<p>The statute puts the notice job on the beneficiary. After the death, the beneficiary must publish a notice to creditors and mail a copy to the grantor's personal representative if known, the Department of Health and Human Services, and known or readily ascertainable creditors. A creditor then has 90 days after mailing or after the first publication to file a claim with the beneficiary, and a late claim is barred.</p>
<p>The Department has its own track. If it receives notice, it must tell the beneficiary within 45 days whether the grantor received public assistance and, if not, give an original waiver of claim for recording. If the beneficiary never gives notice, the property stays subject to the Department's right to recover assistance, and NRS 111.693 adds that the deed statutes do not limit Medicaid recovery.</p>
<p>When a creditor claim is rejected, the beneficiary has 10 days to send written notice by registered or certified mail, and the claimant then has 30 days to sue or the claim is barred.</p>""")

sec("Can a beneficiary sell the house after the owner dies?",
"""<p>Yes, and many do. Once the claim period has run, NRS 111.689(5) lets the beneficiaries sell or distribute the property without personal liability for claims that were not timely filed, as long as they gave written notice to the Department of Health and Human Services and received the waiver of claim the statute describes.</p>
<p>That clause turns the order of tasks into a checklist for anyone planning a sale:</p>
<ol>
<li>Record the Death of Grantor Affidavit with the death certificate and declaration of value.</li>
<li>Publish the creditor notice and mail it to the required parties, including the Department.</li>
<li>Wait out the 90 day claim window and the Department's 45 day response.</li>
<li>Give the title company copies of the recorded documents. The statute says a title company may treat the notices as adequate notice and is not liable for claims it was not told about.</li>
<li>Sign the sale deed. A sale to a buyer is a regular conveyance, so the transfer tax in NRS 375.020 applies at $1.25 per $500 of value in a county of 700,000 or more people and 65 cents per $500 in a smaller county.</li>
</ol>
<p>If the beneficiaries do not want the house, NRS 111.687 allows a beneficiary to disclaim all or part of the interest by recording a disclaimer with the county recorder under chapter 120.</p>""")

sec("What if the deed is missing, defective or has several beneficiaries?",
"""<p>The statutes provide no shortcut around a bad deed. An unrecorded deed does not work, a void deed does not work, and a deed with a wrong legal description invites a title dispute. In those cases the property may have to go through probate instead. Our <a href="/nevada-probate-process/">Nevada probate guide</a> explains that path.</p>
<p>Several beneficiaries bring a separate problem. All of them hold title once the deed takes effect, so a sale needs their agreement and signatures. If one beneficiary lives out of state, is hard to reach or disagrees about price, the sale slows down quickly.</p>
<ul>
<li>Check that the deed was recorded before death and that the recording details match the affidavit.</li>
<li>Gather death certificates for every grantor, not only the last to die.</li>
<li>Make a list of every beneficiary and a way to contact each one.</li>
<li>Ask the title company early what it will require.</li>
</ul>
<p>We buy inherited Nevada houses as-is, including houses that still hold the owner's belongings or need repairs. Because we pay cash, there is no lender appraisal to hold up closing once the paperwork is in order.</p>""")

F=[
("What is the difference between a deed upon death and a will in Nevada?",
"A recorded deed upon death passes the named property directly to the beneficiary when the owner dies, while a will usually goes through probate. The deed only works for real property it describes, and it must be recorded before death (NRS 111.671)."),
("Can I sell my house after recording a deed upon death in Nevada?",
"Yes. The deed does not affect the owner's right to transfer or encumber the property during life (NRS 111.685). A transfer during life makes the deed void under NRS 111.677."),
("Does a Nevada deed upon death avoid creditors?",
"No. If the probate estate is insufficient, the estate can enforce liabilities against the property, and the beneficiary must publish and mail a creditor notice. Creditors have 90 days to file claims (NRS 111.689)."),
("What document does a beneficiary record after death in Nevada?",
"A Death of Grantor Affidavit, with a declaration of value and a death certificate for each grantor, recorded with the county recorder where the deed was recorded (NRS 111.699)."),
("Can a beneficiary refuse a Nevada deed upon death?",
"Yes. NRS 111.687 allows a beneficiary to disclaim all or part of the interest by recording a disclaimer with the county recorder."),
]
SRC=[
("NRS 111.671 Creation of deed upon death","https://law.justia.com/codes/nevada/chapter-111/statute-111-671/"),
("NRS 111.677 Void if interest transferred before death","https://law.justia.com/codes/nevada/chapter-111/statute-111-677/"),
("NRS 111.685 Effect of deed upon death during owner's lifetime","https://law.justia.com/codes/nevada/chapter-111/statute-111-685/"),
("NRS 111.687 Disclaimer by beneficiary","https://law.justia.com/codes/nevada/chapter-111/statute-111-687/"),
("NRS 111.689 Enforcement of liabilities; creditor notice","https://law.justia.com/codes/nevada/chapter-111/statute-111-689/"),
("NRS 111.693 Limitations concerning Medicaid payments","https://law.justia.com/codes/nevada/chapter-111/statute-111-693/"),
("NRS 111.695 Form of deed upon death","https://law.justia.com/codes/nevada/chapter-111/statute-111-695/"),
("NRS 111.699 Death of Grantor Affidavit","https://law.justia.com/codes/nevada/chapter-111/statute-111-699/"),
("NRS 375.020 Imposition and rate of transfer tax","https://law.justia.com/codes/nevada/chapter-375/statute-375-020/"),
]
exec(open('/home/claude/chb-pages/gen/rw_scripts/tail.py').read())
