# Part C — What an industry partner uploads, and why

**For:** the CSR / sustainability team of a company responding to a MILAN challenge (worked example:
Damodar Valley Corporation funding the Jharia night-school lighting retrofit, or BCCL / SAIL / JSPL /
Tata Steel Foundation on any in-district challenge).

> **The principle in one line:** the platform accepts **evidence, not marketing**. Every file a funder uploads
> either (a) commits money, (b) describes what was installed, (c) proves it works, or (d) names the person
> who will keep it working. Anything else is a press release, and it belongs nowhere near a §135 report.

---

## 0. Before you can upload anything (gate 0)

| Requirement | Why |
|---|---|
| An `INDUSTRY` account whose **organisation is admin-approved** (`orgVerificationStatus = APPROVED`) | Uploads attributed to an unverified company are worthless in an audit. Verification needs your proof of affiliation — institutional authorisation letter / GST / CIN, PDF or JPG/PNG, ≤5 MB, hashed at upload, never reprocessed |
| A named person with authority to commit (designation recorded: *General Manager (CSR)*, *Head – CSR (Jharkhand)*, *CEO*) | `FUNDER` credit edges and MoU drafts cite a person, not a logo |
| District focus and domain interests on your org record | This is what makes a live Jharia `EDUCATION` challenge appear in *your* discover feed |

## 1. Upload by stage

Four columns rather than seven, because a stage table that needs a landscape page is a
stage table nobody reads. Each row names the `artifacts.kind` the file lands as, and the
licence, in the second column.

| # · stage | What you file (kind · licence) | Format | What the platform does with it |
|---|---|---|---|
| **1 · Expression of interest** — `/industry/challenges/[trackingId]` | No file. 20–3,000 characters saying what you will fund, the amount band, your constraint (*"only within 25 km of a plant township"*, *"no work with minors directly"*), and who signs | text | `industryInterests` row at `EXPRESSED`; notifies the project lead. Silently rejected if the challenge has not cleared triage |
| **2 · Accepted** | Nothing yet | — | `FUNDER` credit edge on the project; challenge → `INDUSTRY_INTEREST` |
| **3 · Agreement** | Counter-signed MILAN MoU. The platform generates and hashes the draft; you upload the **executed scan** with signature and stamp | `AGREEMENT` · `RESTRICTED` · PDF ≤10 MB | `PROPOSAL` ledger entry carrying the file's own SHA-256; every read of it is logged |
| **4 · Money** | Sanction order or CSR-1 project code, committed ₹ amount, head of account, disbursement schedule, grant vs in-kind (hardware at invoice price) | `FUNDING` · `RESTRICTED` · PDF ≤10 MB | `PROPOSAL` ledger entry. Amounts stay *claims* until the pilot closes; the CSR export shows them beside confirmed outcomes, never summed into one total |
| **5 · Technical basis** | BOM with unit prices, vendor + warranty terms, the datasheets you are buying against, earthing/lightning/IS-compliance notes, and **what you are explicitly not fixing** (*"no new poles; existing 46 only"*) | `SPEC` · `CC_BY` · PDF ≤25 MB | `REPORT` ledger entry. Public by default — a funder's spec is checkable by the university that has to satisfy it |
| **6 · As-built** | Per-pole record: asset tag, GPS of the **pole** (never a home), commissioning date, energisation readings (voltage, lumens or load current), before/after photos with faces and name-boards blurred, contractor sign-off | `REPORT` · `CC_BY` · PDF/JPG ≤10 MB each | `REPORT` per file, each keyed by content hash, so re-uploading the same bytes deduplicates instead of double-counting |
| **7 · Test & acceptance** | 30-day and 90-day uptime logs from the retrofit telemetry, failure count, and the acceptance certificate signed by the school **and** the Panchayat — they are the owner; if they have not accepted it, it is not done | `REPORT` · `CC_BY` · PDF | `REPORT`. This is the file that turns *"installed"* into *"verified by a counterparty"* |
| **8 · Sustainability** | The O&M instrument: AMC order or spares-corpus receipt with ₹/pole/year, the named electrician and phone number, spares stock list, trained-repair register, escalation path when the money runs out | `REPORT` · `CC_BY` · PDF | `REPORT`. File it at sanction, not at close — a plan written after the fact is a footnote |
| **9 · Capacity** | Training record for the repair crew: date, attendance **count** (aggregate, no names), materials issued, refresher schedule | `REPORT` · `CC_BY` · PDF | `REPORT` |
| **10 · Impact claim** | `markImplemented()` — a form, not a file: one sentence on what changed, plus pointers to the evidence above | text | `IMPLEMENTED`; notifies every corroborator and the reporter with a signed `/me/verify/[token]` link needing no login, and opens `IMPACT_UNCONFIRMED_30` so silence is re-asked, never assumed |
| **11 · Close-out** | Third-party or internal audit note; the year's CSR-1 extract; a corrected figure if the community disputed anything | `REPORT` · `RESTRICTED` if it carries financial detail · PDF | `REPORT`. Auditors are the intended reader — say so in the abstract field |

## 2. What the platform refuses (and returns with a reason)

- **Images of identifiable children.** Any photograph where a face is recognisable, in uniform, at a school,
  or at a work site. Faces must be blurred by the uploader before upload. Under the DPDP Act 2023 these are
  personal data of minors processed for a purpose that does not require them, and a CSR report is not a
  consent mechanism.
- **Named beneficiary lists.** Attendance rosters, subsidy beneficiary tables, family names, mobile numbers,
  Aadhaar, bank details, ration-card images. Upload **counts and aggregates**; keep the roster in your own
  audited system and cite it.
- **Home locations.** GPS is welcome for *assets* (the pole, the pump, the classroom). Never for households
  — in a coalfield resettlement context that is a mapping of who lives where, and it will be returned.
- **Anything you don't have the right to publish.** Vendor datasheets and bid documents are typically the
  funder's to share; a contractor's drawing set often is not. Upload what you own or are licensed to
  distribute, and choose `RESTRICTED` when in doubt — a restricted artifact is still readable by a named
  person who states a purpose, and every read is logged.
- **Unverifiable outcome language.** "Transformed the lives of 500 children" in a file titled *evidence*
  fails review; the same sentence belongs in your annual report, not the ledger.
- **Marketing collateral, logos-only PDFs, press clippings.** Not an artifact type.
- **Duplicate bytes under a new title.** Same content hash → same object. Renaming does not create two
  results, and the ledger entry will not say that it did.

## 3. File discipline (six rules that cost you nothing)

1. **Name:** `JH-2026-DHN-####_<stage>_<asset|site>_YYYY-MM-DD.pdf` — the tracking ID first, so a file is
   attributable even after it leaves the platform.
2. **Title field:** plain and specific — *"46-pole lighting retrofit, BOM and unit prices, DVC-CSR/2026/114"*
   beats *"Project report"*.
3. **Abstract field:** three sentences — what it proves, over what period, and what it explicitly does **not**
   cover. Researchers and auditors read this line and nothing else.
4. **Checksum:** let the platform compute it. If you maintain an internal register, record the returned
   SHA-256 — it is what proves your copy and the public copy are the same file.
5. **Dates, not "recent".** Every claim needs an as-of date; the SLA ladder and the annual review both read
   dates.
6. **One claim per file.** A PDF containing the BOM, the invoices and the impact story is three ledger
   entries pretending to be one, and every future correction to the invoices means re-publishing the impact
   story too.

## 4. A good EOI (copy the shape, not the words)

> *DVC CSR wing can fund the lighting component for the four Jharia night-school centres: retrofit
> controllers, batteries for the 20 poles with degraded storage, and a 2-year spares corpus, in the range
> ₹12–18 lakh, subject to the block Panchayat accepting O&M ownership in writing. We can start disbursal
> within 6 weeks of a signed MoU. Our constraint: works only on existing poles — no new civil works, no
> land or ROW questions. Our signatory: GM (CSR), DVC. We would like the university team to carry out the
> 30/90-day uptime measurement so that the acceptance data is not self-generated.*

Twenty seconds to read; four checkable commitments; one honest constraint; and a request that the evaluator
not be the funder. That last clause is why a project lead accepts this one and declines the glossy one.

## 5. What you get back

- **A `FUNDER` credit edge on a citable project** — permanently attached to the artifact set, with a public
  `/credit` trail. It survives staff turnover, which is the entire reason an annual PDF is not an
  alternative.
- **A §135 export an auditor can defend:** confirmed / partly-confirmed / claimed-but-not-confirmed as three
  separate counters, with beneficiary totals never summed. Your spend is not discounted by the honesty — it
  is the only part of the report that survives scrutiny.
- **Defensive publication of the university's design**, hashed: it does not stop someone filing a patent,
  it makes the work prior art, which is what stops one being *granted* over it.
- **A verification trail for the asset you funded** — every state change, every access to a restricted file,
  and every human override in one hash chain, recomputable in a browser.
- **Repeatable targeting:** your domain interests and district focus next year are matched against scored,
  corroborated, citizen-verified demand — not against whoever asks loudest.

## 6. One-line summary for the CSR head who asks why this is worth the effort

> "You upload six PDFs you were going to produce anyway; what you get is that nobody — not a future
> department, not a future government, not your own successor — can quietly make the work, or your
> contribution to it, un-have happened."
