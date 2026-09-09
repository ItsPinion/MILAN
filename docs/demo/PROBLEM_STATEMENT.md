# Problem Statement — "The lights went out and the night school closed"

**Demo instance of SIH26043** · A digital platform to crowdsource societal challenges and facilitate
collaborative problem solving through universities and industry partnerships
**Government of Jharkhand · Theme: Smart Education · Category: Software**

> **Status of the numbers in this document.** Everything marked `[demo]` is a seeded figure invented for
> the demonstration and must be replaced with field data (Census child-work tables, NLSS, UDISE+, the
> district LED/SSA asset register, the Panchayat's works records) before this is filed anywhere real. The
> geography, institutions, companies and laboratory capabilities are **not** invented — they are the rows
> this repository actually seeds, and the demo runs against them.

---

## 1. Title

**Night classes for working children stopped when the solar lights broke — and nobody was accountable for
repairing them.**

Working title for the platform record: `Solar lighting and the missing owner: restoring night classes for
working children in Jharia block`.

## 2. Identifiers

| Field | Value |
|---|---|
| Parent problem statement | SIH26043 (Software · Smart Education) |
| Sponsoring organisation | Government of Jharkhand, Department of Higher & Technical Education |
| Instance location | Jharia block (`DHN-JHA`), Dhanbad district, Jharkhand |
| Domain | `EDUCATION` (secondary: `ENERGY`, `ACCESSIBILITY`) |
| Recurrence | `constant` |
| People-affected bucket | `100–1,000` → stored as midpoint **550** |
| Block vulnerability index (seeded) | **0.87** — the highest of the 11 seeded Dhanbad blocks |

## 3. Background

In the Jharia coalfield, school is not the end of a child's day — it is the second shift. Children who
sort coal at the washery chowk, load trucks at dusk, mind goats on the subsidence edge, or work in tea
stalls and domestic service in Dhanbad's wards attend **evening bridge courses** run by volunteer
teachers, an NGO-run night school, and an open-schooling support centre. Four centres, roughly 500
children between them `[demo]`, meet from 18:00 to 20:30.

The only light in those rooms, and on the lanes that lead to them, is **solar**. Street lights installed
under a state/central rural-lighting scheme, plus small rooftop solar kits with battery boxes bolted under
the veranda of two of the four buildings.

Fourteen months ago the lights began failing `[demo]`. First one centre, then the lane, then all four.
The causes were ordinary and identical across the state: charge controllers burned out in the last
pre-monsoon, batteries swelled past end-of-life, two battery boxes were stolen, one pole was hit by a
truck, and no one held the contract any more — the installation agency's one-year defect liability period
had expired in month eleven.

What happened next is the actual problem. Nobody owns a solar street light. The **education** department
owns the children but not the lamps; the **Panchayat / ULB** owns the lamps but budgets nothing for their
repair and holds no asset register that says which pole is where; the **scheme portal** that funded them
records installation, not maintenance; the **electrical contractor** who installed them has moved to
another block. When the children's attendance collapsed, each of those four bodies was correct: *not my
asset, not my budget, not my department.*

By the third month, three of the four centres stopped running after dark entirely `[demo]`. In an
informal coalfield economy, a child with an unlit evening is a child at the chowk. Attendance at the
remaining centre fell and did not recover; the two centres that had enrolled girls — 60% of their roll —
closed first, because the lane is the barrier, not the classroom.

## 4. Statement of the problem

**The broken lamp is not the problem. The missing owner is.**

Jharkhand has thousands of community assets — lights, pumps, water taps, angular-road culverts, solar
kits on school roofs, toilets, anganwadi roofs — that sit in exactly this gap: installed by a scheme,
handed to a body with no repair budget, monitored by nobody, and invisible to every department whose
work they gate. Where a citizen's report has nowhere to go, the asset stays broken and the *outcome the
asset existed to produce* — children in class after dark — quietly dies. No dashboard shows the death,
because no system links the asset to the outcome.

The problem this instance puts to the platform (SIH26043) is therefore **a routing and accountability
problem in a Smart Education setting**:

> How does a platform take a vernacular citizen report — "the night school closed because the lights
> broke and no one repairs them" — categorise it, judge whether it is a *grievance* (a repair someone
> already owes) or an *unsolved problem* (no known fix, no owner), route it to a university team capable
> of producing an answer, put a clock on the whole thing so it cannot die silently, and let industry fund
> the deployment with evidence an auditor can check — while proving every credit and every number?

## 5. What makes it hard (and why it is a research question, not a tender)

1. **Grievance-or-problem ambiguity.** If one light on a Panchayat road is out, that is a complaint with a
   known fix and a defined office. *This* is four centres dark for fourteen months with no live contract —
   there is no officer to complain to, because the accountable thing has expired. The platform must
   separate the two and forward the first while routing the second. (Milan: S1 triage + `FORWARDED_EXTERNAL`.)
2. **The fix is not the lamp.** Replacing 40 lights costs money the block already spent once. The
   defensible answer is a repairability model: which failure modes are field-fixable by a trained local
   electrician, what a ₹-scaled spares corpus looks like, whether a ₹300–500 retrofit controller with
   1 bit of telemetry ("this pole drew current last night") is worth the data plan, and what the Panchayat
   will actually sign up to run. That is a legitimate student research project with a measurable
   dependent variable: **class-nights held after dark**.
3. **Multi-department.** Civil works, solar, school education, ICDS, rural development, the district
   mineral foundation, and CSR money all touch it. No single department can be *routed to*.
4. **Equity visibility.** 500 children across four centres is small in absolute terms. A scoring function
   that rewards headcount linearly will never surface it; the one that does must be log-scaled and must
   weight chronic recurrence and block vulnerability. This instance is the proof case for that design choice.
5. **Darkness is the dropout variable, and it is not in anyone's data.** Nobody records lane lighting and
   night-school attendance in the same table. Establishing the link *is* part of the research.

## 6. Requirements placed on the platform by this instance

| # | Requirement (from SIH26043) | What this instance specifically demands |
|---|---|---|
| R1 | Intake for citizens/local bodies with photos, location, documents | A 24-year-old washery worker must be able to file it in Hindi from a ₹8,000 phone, with two photos of a dead pole, no login required to be believed, and a tracking ID she can say over the phone |
| R2 | AI categorisation by thematic domain | Must land on `EDUCATION` and not `PUBLIC_SERVICE`/`URBAN_INFRA`, with severity above the human-gate threshold and a *low* capital-works flag — or it never reaches a lab |
| R3 | Deduplication as signal | Five neighbours + one teacher reporting the same four dead centres must merge into corroboration, not five competing tickets |
| R4 | Routing by institutional capability | Must find electrical/solar + embedded-systems + education-department labs within reach, not the nearest college with a CS department |
| R5 | University workflow | A multidisciplinary team (EEE + ECE + Education), faculty mentor, milestones, named students |
| R6 | Industry collaboration | Must attract a mining/utility CSR that funds hardware, and hold it to evidence |
| R7 | Lifecycle + SLA | 14 months of silence is the failure being fixed: every state gets a clock and an escalation |
| R8 | Analytics for government | Domain distribution must show that `EDUCATION` items are being *lost*, and the district board must see this one at the top while it is unclaimed |
| R9 | Verification of outcomes | A funder's "lights restored" must not count until the teacher and the children's families say class is happening again |
| R10 | Offline & vernacular | Jharia has dead zones; the pipeline must degrade to deterministic rules rather than fail |

## 7. Expected solution components (mirrors SIH26043, applied)

1. **Citizen engagement module** — multilingual intake with photo evidence, device-side privacy blur,
   GPS or place search, a bucket for scale rather than a fake precise count, and a self-review step where
   the reporter approves the platform's re-framing or rejects it.
2. **AI-enabled problem management** — triage (safety / grievance), classification (11 domains, severity,
   solvability, capital-works flag), dedup+corroboration via embeddings, deterministic priority scoring
   with the arithmetic on screen, capability routing with a written reason per institution.
3. **University collaboration module** — offers pushed to three matched labs, claim window, multidisciplinary
   team formation by *name*, mentor assignment, milestones, publication of the artifact with a content hash.
4. **Industry partnership module** — expression of interest against a live challenge, acceptance by the
   project lead, funded-pilot record, and the implementation claim (see Part C for what industry uploads).
5. **Project lifecycle management** — one state machine owning every transition; SLA ladder; dispute
   handling; closure only after verification.
6. **Visual analytics** — district board, domain funnel, confirmation gap, public bounty board, public
   ledger, §135 CSR export.
7. **Notifications** — push, never browse: each notice points at the one thing to act on.

## 8. Outcomes this instance should be judged on

| Measure | Baseline `[demo]` | Target |
|---|---|---|
| Class-nights held after dark, per month, across the 4 centres | 11 | ≥ 90 |
| Reported-broken → confirmed-repaired median days | not measured; 14 months on record | ≤ 21 days |
| Assets with a named owner + repair contact in a public register | 0 of 46 | 46 of 46 |
| Night-school enrolment (girls) | 40% of prior roll | restored within one term |
| Centres with any functional lighting telemetry | 0 | ≥ 2 ( retrofit, read-only ) |
| Citizen-confirmed impact (not funder-claimed) | 0 | the only number that counts |

## 9. Stakeholders

**Primary:** the ~500 children `[demo]` and their families; the 6 volunteer teachers; the night-school
committee. **Institutional:** Dhanbad district administration; Jharia block/Panchayat samiti; the school
education department's dropout-cell; SCERT (open-schooling support). **Technical:** the coalfield
companies and utility CSR arms operating in-district; BIT Sindri, NIT Jamshedpur, BIT Mesra, IIT (ISM)
Dhanbad labs; the state renewable-energy development agency. **Adjacent:** the electrical works contractor
community; Self-Help Groups that could run a tariffed repair corpus.

## 10. Data, interfaces and constraints

- **Available at filing:** photographs with device GPS (to be stripped on upload), the Panchayat's works
  register if it can be photographed, scheme-era installation records (paper), NGO attendance registers
  (paper), no digital asset register for the lamps.
- **Constraints:** intermittent connectivity; Hindi-dominant (Santali and Bangla present); no assumption
  of a smartphone per household; no government write-API available for asset registers; a citizen cannot
  be asked to know which department owns a pole.
- **Privacy hard line:** the beneficiaries are minors, several of them in child labour situations. No face
  imagery, no named child lists, no home locations. Blurring happens on the reporter's device and the
  unblurred original never leaves the phone.
- **Evaluation criteria a judge should apply to any submission:** correct grievance-vs-problem routing;
  explainable priority (not a black-box score); a clock on every state; a credit ledger nobody can erase;
  an outcome that only the beneficiary can confirm; and a working offline path.
