# Solution — MILAN: *Koi Maalik* (an owner, a clock, a receipt for every broken community asset)

**Companion to:** `docs/demo/PROBLEM_STATEMENT.md` (Jharia night classes, Dhanbad) ·
**Upload spec for the industry side:** `docs/demo/INDUSTRY_UPLOAD_SPEC.md`

---

## 1. Solution title

**Primary (recommended):**

> **MILAN — Koi Maalik: an AI-routed assignment engine that turns citizen problems into funded university research**

Alternates for different field limits:

| Title | Chars | Use when |
|---|---|---|
| MILAN — Koi Maalik: an AI-routed assignment engine that turns citizen problems into funded university research | 110 | unconstrained field, or your own college's form |
| MILAN — Koi Maalik: routing citizen problems to labs, with a clock and a credit ledger | 86 | general submission |
| MILAN: an owner, a clock and a receipt for every broken community asset | 71 | **safe default** — fits an 80-char limit |
| Koi Maalik — restoring the night school by giving the lamp an owner | 67 | if you want the story in the title |

Counts are measured, not estimated, because the SIH idea form truncates silently and a title cut mid-word
in the reviewers' list is a needless loss. If you are unsure of the limit, use the 71-character row.

*"Koi maalik"* is the Hindi a judge in this room will already be thinking: *koi maalik nahi tha* — nobody
owned it. Naming the intervention after the absence is the whole pitch in two words.

## 2. Abstraction

### 2.1 Portal abstract — 150 words exactly (measured; meets a 150-word cap)

> Five hundred working children in Jharia block stopped attending night school when the solar lights broke.
> Nobody repaired them in fourteen months — not for want of parts, but because no department owns a lamp.
> MILAN closes that gap. A citizen files the problem in Hindi with two photographs; an AI pipeline triages it,
> separates a grievance someone already owes from an unsolved problem, classifies it across eleven domains,
> merges duplicates as corroboration, and scores priority with six deterministic weighted terms, printed on
> the public page. It is then pushed to the three departments best matched on capability, distance, capacity
> and track record, each with a written reason the model may not invent. Every state carries an SLA clock that
> escalates in public, every contribution is sealed in an append-only hash-chained ledger. Universities
> research and publish; industry funds the pilot with auditor-grade evidence. Impact counts only when the
> community confirms it.

### 2.2 Extended abstract

**The insight.** Every stakeholder in this story is behaving correctly. The education department funds
teachers, not lamps. The Panchayat inherited 46 poles with no repair line item. The installing contractor's
defect-liability period expired in month eleven. The scheme portal reports *lights installed*, which is
true. Each organisation is right, and the school is closed — which is the definition of an institutional
gap rather than an engineering one. No repair backlog in India lacks for spare controllers; it lacks for an
owner, a deadline, and a record that survives the person who cared.

**What MILAN does.** It is a **routing and accountability layer** placed over the gap, not another asset
registry, and not a grievance portal. CPGRAMS and JharSewa route a complaint with a known fix to an
accountable officer. There is no officer here — the fix is unknown and the ownership has expired, so the
report has nowhere to go. MILAN routes *unsolved problems to laboratories*, with a time-bound assignment,
and forwards the ones that were actually grievances to the right portal, telling the citizen exactly where
the file went.

**How it works end to end for this instance.** A washery worker files it: Hindi, two photos, a pin on the
lane. The six-stage pipeline runs in about eight seconds (P0 language → S1 safety/grievance triage ∥ S2
domain/severity → S3 dedup → S4 priority → S5 routing). Six neighbours and a teacher report the same four
dark centres; S3 merges them into corroboration rather than six competing tickets and credits both sides.
S4 scores it **66/100**, above the routing bar, and the breakdown — severity, children affected, Jharia's
vulnerability index, corroborations, chronic recurrence, no endorsement yet — is visible to everyone with no
login. Severity 0.82 is over the 0.70 threshold, so nothing is sent until the District Collector releases it
at the human gate. It routes to **NIT Jamshedpur's Power Systems Lab**, **BIT Mesra's Power and Energy
Systems Lab**, and **BIT Sindri's Embedded Systems & IoT Lab** — chosen on capability, distance and
declared capacity, not on name — with BIT Sindri claiming within the 7-day window. The deliverable is not
"reinstall 40 lights." It is a field-fixable failure taxonomy, a sub-₹500 telemetry retrofit that lets a
Panchayat see *which poles drew current last night*, a costed repair corpus and a local electrician protocol
the Panchayat will actually sign, and a policy brief on writing O&M into the scheme at sanction time —
published as a hashed artifact that becomes prior art nobody can patent over. **Damodar Valley Corporation**
sees a live, citizen-endorsed need inside its own district focus, funds the retrofit through the industry
module, and files an evidence pack (Part C). It marks the work *implemented*. That is a **claim, not an
outcome**: the counter moves only when the teacher and the children's families answer *yes, class is
running again* on a signed link that needs no login.

**Why it is fair.** Jharia's 500 children lose to any town's 6,000 under linear scoring, so `people-affected`
is log-normalised and block vulnerability carries 18% of the weight — the two design choices that make a
small, chronically broken thing in a high-vulnerability block reach a lab at all. A duplicate report is
signal, never noise. An unclaimed problem escalates in public instead of expiring quietly. And a student who
credited a night-school pilot cannot have their name edited out by whoever funds it next.

**Why it is deployable.** One Next.js 15 deployable on Vercel (Mumbai), one Postgres 17 with pgvector doing
the work of rows, vectors, full-text search and the event outbox, three AI providers falling to a
deterministic rules tier that makes **zero network calls** — demonstrated offline at fallback level 2 for
every one of 53 model calls. No blockchain, no Kafka, no separate vector database, no fine-tuned model: a
SHA-256 hash chain plus a public timestamp gives the same non-repudiation for free, and we say so on the
slide rather than hiding it.

## 3. The instance, walked through the platform

| Step | Where it happens | What is true afterwards |
|---|---|---|
| 1 · File | `/submit` (or `POST /api/intake`) | Row created at `SUBMITTED`; photos blurred on-device, EXIF stripped, objects keyed by content hash; tracking ID sayable on the phone; credit edge + `PROBLEM_TEXT` ledger entry + SLA deadline written in the same transaction |
| 2 · Language | P0 | `body_en` working copy added **beside** `body_original`, never replacing it |
| 3 · Triage | S1 → `lib/ai/triage.ts` | Verdict `CONTINUE`. Not a grievance: there is no live work order and no sanctioned repair, so it is not forwarded to CPGRAMS. Had the report named a sanctioned scheme with a pending contractor, it would have been `FORWARDED_EXTERNAL` with the exact payload rendered publicly |
| 4 · Classify | S2 | Domain `EDUCATION`, severity **0.82**, solvability high, capital-works flag **false** → a research question, not a tender |
| 5 · Embed + dedup | S3 | cosine ≥ 0.86 auto-merge, 0.72–0.86 one adjudication call; 6 reports merge into the oldest survivor; `corroboration_count = 6`; both sides credited; nothing discarded |
| 6 · Score | S4 (`packages/scoring`) | **66.43/100**, zero model calls, six terms below, `SCORING_VERSION 2.0.0` stamped |
| 7 · Route | S5 → gate | Shortlist computed; severity ≥ 0.70 → offers written with `notified_at = null`; `/gov/gate` releases → `ROUTED`, 7-day claim clock |
| 8 · Claim | `/hei/.../claim` | `projects` row, 4 students credited **by name**, mentor edge, and the reporter on the team as *Domain Informant*; other two offers expire; capacity decrements |
| 9 · Research | `/hei/projects/[id]` | `PROPOSAL_APPROVED → IN_RESEARCH`; every write resets `last_activity_at`, which is what the silence ladder measures |
| 10 · Publish | artifact panel | File keyed by its own SHA-256, `REPORT` ledger entry; title and abstract public **regardless of licence**; RESTRICTED files served only against a logged, purpose-stated request |
| 11 · Fund | `/industry/...` | EOI → acceptance → `FUNDER` credit edge → MoU generated, hashed into the ledger, explicitly an unsigned draft |
| 12 · Deploy | `markImplemented()` | `IMPLEMENTED` = a claim. Renders grey as *claimed, not confirmed* everywhere, including the §135 export |
| 13 · Verify | `/me/verify/[token]` | YES → `CITIZEN_VERIFIED`, the **only** event that moves the impact counter; PARTLY → its own bucket; NO → `DISPUTED`, Collector notified, counter unmoved |
| 14 · Close | 7 days later | `CLOSED` by the reaper — bookkeeping is on a clock too |

### 3.1 The priority score, as the public page shows it

```
SEVERITY        raw 0.82 (S2)          ×0.28  =  22.96
PEOPLE AFFECTED raw 550 (bucket 100–1,000)      → log(1+550)/log(1+100000) = 0.5482  ×0.20 = 10.96
BLOCK VULNER.   raw 0.87 (Jharia, seeded)        ×0.18  =  15.66
CORROBORATIONS  raw 6, mean trust 0.50 → ×1.00   → √6/√50 = 0.3464  ×0.14 =  4.85
RECURRENCE      raw "constant" = 1.00            ×0.12  =  12.00
ENDORSEMENT     raw 0 (no block officer yet)     ×0.08  =   0.00
                                        TOTAL  =  66.43 / 100
```

Add one field endorsement at `/gov/verification` and the number becomes **74.43** — eight points, visible,
computed by hand on the page. That is the answer to *"how do we know the score isn't arbitrary?"*: it is not
objective, it is six declared weights on a versioned, unit-tested pure function, and a state authority can
change them without a redeploy.

### 3.2 Why these three labs (S5, indicative)

| # | Lab | Sem | Ovl | Dist | Cap | Hist | Reason sentence the guardrail allowed |
|---|---|---|---|---|---|---|---|
| 1 | **NIT Jamshedpur** · Power Systems Lab (`energy\|solar\|micro-grid\|rural-electrification\|load-monitoring`) | 0.79 | 0.62 | 0.64 (110 km) | 0.40 | 0.55 | *"Strongest fit on solar and rural electrification, 110 km away, 2 slots open."* |
| 2 | **BIT Mesra** · Power and Energy Systems Lab (`renewable\|power-electronics`) | 0.76 | 0.55 | 0.66 (105 km) | 0.40 | 0.45 | *"Matches solar and power-electronics specialisation, 105 km away, 2 slots."* |
| 3 | **BIT Sindri** · Embedded Systems & IoT Lab (`iot\|low-cost-sensors\|telemetry\|lora`) | 0.68 | 0.48 | **0.95 (12 km)** | 0.40 | 0.35 | *"Closest at 12 km, with low-cost telemetry capability for the retrofit."* |
| — | *near-miss:* Ranchi University · Dept of Education (`dropout\|pedagogy`) | 0.41 | 0.71 | 0.63 | 0.40 | 0.30 | ranked 4th: highest pedagogy overlap, insufficient electrical capability |

Weights: semantic 0.45 · specialisation overlap 0.20 · distance 0.15 (`exp(-km/250)`) · declared capacity
0.12 · track record 0.08 (Laplace-smoothed, prior 3). Top **3 distinct organisations**, never two labs from
one college. The model writes only the sentence, and only around the top three contributing terms;
`guardReason()` rejects any number in that sentence that is not in the facts it was handed, falling back to a
template. The near-miss row is the demo's best slide: the platform can explain a fourth place as honestly as
a first.

## 4. What the university actually delivers (so the assignment is gradeable)

1. **Failure taxonomy + field diagnostic protocol** for the three lighting architectures present in the
   block, derived from teardown of the failed units — the deliverable a Panchayat electrician can use.
2. **A ≤ ₹500 retrofit controller** (current-draw or Hall-sense + LoRa/GSM one-bit heartbeat) proving that
   "did pole 17 light last night?" is answerable without a human walking 46 poles; bill of materials,
   firmware, and the failure modes it cannot detect, stated.
3. **A costed O&M model:** spares corpus vs AMC vs SHG-run repair crew, at block scale, with the number that
   makes the difference — the ₹-per-pole-per-year that a Panchayat has previously never been asked to budget.
4. **The evidence that darkness, not disinterest, caused the dropout**: attendance registers against a
   lighting timeline, with the girls-only effect isolated.
5. **A policy brief**: O&M corpus and asset-ledger fields written into the *sanction*, not the handover.
6. **Published artifact**, hashed into the ledger, licence `CC_BY` (recommended) or `RESTRICTED` — and under
   either, the existence of the work stays public.

## 5. Design commitments this instance exercises

| Invariant | What it does here |
|---|---|
| 1 · nothing dies silently | 22 non-terminal states all carry a deadline row; a CI query fails the build if one is missing. 14 months of *nobody owns it* is precisely the failure this CI check exists for |
| 3 · AI proposes, code decides | 0.82 severity is a model output; the 66.43 that routes it is arithmetic in `packages/scoring` |
| 5 · human gate | the collector, not the model, decides that a child-labour-adjacent education claim goes public |
| 7 · counter moves at `CITIZEN_VERIFIED` | DVC's "lights restored" is grey until the community says class is running |
| 9 · duplicates are signal | six reports → one survivor with six corroborations and six credits |
| 10 · every number clickable | the table in §3.1 is on the public challenge page, no login |
| 8 · offline-safe | village-level connectivity in the coalfield is not assumed anywhere on the demo path |

## 6. Novelty — and the honest comparison

| What exists | What it does | Why this is different |
|---|---|---|
| CPGRAMS / JharSewa | complaint → accountable officer with a defined remedy | here there is **no** accountable officer and **no** defined remedy; MILAN detects that case and forwards the ones where it *is* a grievance |
| Asset portals / smart-city dashboards | record installation and outages of assets | they measure the **asset**, not the **outcome the asset was bought to produce** (class-nights held) |
| SIH/ISFC-style innovation events | episodic challenges, prize at the end | the challenge has a lifecycle, a clock, and a verification loop; the assignment outlives the demo |
| CSR project reports | self-reported beneficiaries and spend | three separate counters — confirmed / partly / claimed-not-confirmed — never summed into one flattering number |
| A university's own consultancy cell | institution-initiated, supply-driven | demand-driven: the community's problem, scored and pushed, with the citizen on the team |

## 7. Feasibility, scale and cost

- **Build status:** this is a working application, not a plan — 4 roles + admin, 5 seeded accounts, a
  six-stage pipeline with per-call receipts in `ai_runs`, an append-only ledger enforced by a database
  trigger, an SLA reaper with four ladders, a §135 export, and a judge console at `/demo` that drives the
  lifecycle with the production server actions.
- **Marginal cost per challenge:** ~53 model calls across five stages, all flash-tier or cheaper; embeddings
  cached on input hash so a replay is free; the rules tier costs nothing. Storage is content-addressed, so a
  duplicate upload is not a second object.
- **Scale:** one deployable; `pgvector` HNSW handles millions of rows; modules are folder-local so pipeline,
  ledger, SLA and notifications split into services without a rewrite. Multi-state is a data load
  (districts/blocks/orgs), not a migration.
- **This instance at state scale:** 263 blocks × ~20–50 community assets each is the addressable ledger; the
  platform only ever needs the *reports*, not the inventory, to start.

## 8. Declared limits (say them before someone finds them)

No native app or offline PWA sync (responsive web at 320px + `localStorage` drafts) · no video attachments
(≤3 photographs) · SMS/WhatsApp delivery and IVR intake are seams with mock inboxes, not gateways · Hindi
and Santali copy unverified by a native speaker for this demo · attendance and asset figures in this
document are seeded, not surveyed · Jharia block resolution is nearest-centroid inside a polygon-resolved
district, and no PMTiles basemap is loaded, so the map says so on screen · e-signature and payment rails are
out; the MoU is generated, hashed and labelled an unsigned draft on its own face.

## 9. Next, if this is funded

**v1.1** — asset-class ontology so "which pole" joins to a public registry; a *repairability score* as a
seventh scoring term; a native-language ASR path in production (the stage exists, the demo uses a seeded
transcript); self-serve institution and CSR onboarding. **v2** — block-level boundary geometry, real CPGRAMS
write API, a third-party timestamp on the ledger anchor, and the O&M-corpus instrument itself with the
Panchayat as counterparty — which is the point: the research output becomes a budget line, or it was a
poster.
