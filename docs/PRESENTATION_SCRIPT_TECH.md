# Your 2 minutes — tech stack · workflow · architecture · AI pipeline

Target: **120 seconds.** The script is **277 words** = **1:58** at a calm 140 wpm, **2:08** at a
relaxed 130. Rehearse with a timer. The one real risk in a 4-in-2-minute slot is running long on section one
and then rushing the pipeline — which is the part they're scoring.

**Do not explain what a tool is.** Name the choice, give the reason, move on. The reason is what scores.

---

## THE SCRIPT

### 1. Tech stack — 0:00 → 0:27

> One deployable: Next.js 15, React 19, strict TypeScript, Tailwind and shadcn/ui. One database: Supabase
> Postgres 17 — Drizzle and Zod give one shared schema, pgvector holds the embeddings. Better Auth for five
> roles, Supabase Storage keyed by SHA-256. Gemini Flash, then Groq, then deterministic rules; SSE for the
> live trace. Four exclusions on purpose: no blockchain, no vector database, no Kafka, no fine-tuning.

### 2. Workflow — 0:27 → 0:49

> Spec-first. `CLAUDE.md` holds ten invariants — correctness rules, not preferences. Two: the ledger is
> append-only, and the AI never decides a score. Task by task: implement, verify, commit. CI enforces
> typecheck, build, the full test suite, and a required check that no challenge sits without an SLA clock. "Done"
> means it runs with the wifi off.

### 3. Architecture — 0:49 → 1:18

> Four audiences, one set of server actions. Above the database: the AI pipeline. Below it, one state
> machine — the only writer of challenge status. Every transition writes the status, ledger entry, SLA
> deadlines and outbox event in one transaction, or none of them. If nobody claims a challenge, a ladder
> escalates: widen at seven days, open to every college at fourteen, bounty board at twenty-one. Nothing
> dies quietly.

### 4. AI pipeline — 1:18 → 1:59

> Six stages: P0 language, S1 safety and triage, S2 domain and severity, S3 duplicate clustering, S4
> priority score, S5 routing. Three things make it defensible. Concurrency: the embedding and S2 run in
> parallel with S1 — seven seconds was measured, not assumed. S4 makes zero model calls: six weighted terms,
> sum 1.00, and the citizen sees the arithmetic. Every call writes a receipt — provider, model, fallback
> level, confidence — so a rules-level answer never overwrites a classification; it goes to a human. Above
> severity 0.7, nothing routes until an officer confirms at the gate.

---

## IF YOU RUN LONG — cut in this order
1. Architecture: *"and the outbox event"* → keep the rest of the sentence.
2. Workflow: *"Task by task: implement, verify, commit."*
3. Tech stack: *"Better Auth for five roles, Supabase Storage keyed by SHA-256."*

## IF YOU RUN SHORT — closer (7 s)
> "One idea holds all of it: the model proposes, deterministic code decides, and a human owns anything
> irreversible."

## OPENING LINE (say it, then go straight into the stack)
- "Everything I name in the next two minutes is a decision we can defend."
- "Four slides, one idea: the AI proposes, the code decides."

---

## DELIVERY CUES

| Section | Do / emphasise | Don't |
|---|---|---|
| Tech stack | Land hard on the four *exclusions* — that's the credibility, not the logo row | Don't read the stack table |
| Workflow | Pause after "the AI never decides a score" | Don't name CI tools beyond the check it runs |
| Architecture | One hand left→right across the diagram, then top→bottom for the ladder | Don't say "microservices" |
| AI pipeline | Slow right down for **"S4 makes zero model calls"** | Don't add stage detail you can't defend |

Pronounce numbers plainly: **"point seven"**, **"one point zero zero"**, **"seven, fourteen,
twenty-one days"**. Avoid the `PARK` routing-bar figure — the docs disagree with themselves (55 in
§6.6 vs 85 in §13.4). If pressed: "under the routing bar it's parked, with the full breakdown public at
`/flagged`."

---

## Q&A — the seven questions this section invites

**Q1. Why no blockchain for the ledger?**
A SHA-256 hash chain plus a daily public timestamp anchor gives the same non-repudiation at zero cost and
zero latency, and `/ledger` lets anyone re-verify the chain in their own browser. A chain you can't verify
locally is a dependency, not a guarantee.

**Q2. Why pgvector instead of a dedicated vector database?**
We have thousands of rows, not billions, and pgvector with an HNSW index serves millions. A separate store
buys a second system to keep in sync and a second secret to leak, with nothing user-visible for it.

**Q3. Why an outbox table instead of Kafka or a queue?**
Events only matter at state changes, and they must be atomic *with* the change. A queue gives "maybe
delivered"; the outbox gives "written in the same transaction as the fact itself." Drained nightly by cron.

**Q4. Why no fine-tuning?**
No labelled data, no GPU budget. So: few-shot prompts plus an embedding kNN prior over already-classified
challenges. Every override at `/gov/gate` and `/admin/triage` lands in `training_corrections` — human
corrections become the labelled set, so the prior improves without shipping a checkpoint.

**Q5. If the AI decides nothing, what is it for?**
It reads messy Hindi or English and returns structured facts — domain, severity, safety,
is-this-a-grievance, candidate duplicates — each with a confidence. Branching, scoring, merging and routing
are plain TypeScript. Facts from the model, judgement from code, authority from a human.

**Q6. What if Gemini dies mid-demo?**
The chain falls to Groq, then to `lib/ai/providers/rules.ts`, which makes no network calls at all. It answers
at confidence 0.45 — below the floor — so the stage goes amber and the item goes to the human queue instead
of guessing. Proven offline: 53 of 53 calls at fallback level 2, with zero calls to Gemini, Groq, Supabase
or Resend.

**Q7. Who chose those six score weights?**
We did, and we say so on the slide. What makes it defensible: they're versioned (`SCORING_VERSION` 2.0.0
stamped on every stored score), a test asserts they sum to 1.00, the breakdown renders on the public
challenge page, and the state authority can change them without a redeploy or a migration. `peopleAffected`
is log-normalised deliberately so a hamlet of 300 isn't outranked by a town of 6,000.

---

## FACTS YOU MAY BE ASKED FOR VERBATIM
- **Stack:** Next.js 15.5.25 · React 19.1 · TS strict · Tailwind v4 + shadcn/Radix · MapLibre + Protomaps
  PMTiles · Recharts · Better Auth · Drizzle + Zod · Supabase Postgres 17 (pgvector HNSW, FTS, pg_trgm) ·
  Supabase Storage · Gemini 2.5 Flash → Groq `openai/gpt-oss-120b` → rules · 768-d embeddings · SSE ·
  Vercel `bom1` + Vercel Cron · GitHub Actions · pnpm workspaces.
- **Pipeline:** `P0 → S1 ∥ S2 → embed → S3 → S4 → S5`, every stage individually try/caught, so a broken S5
  never costs the citizen their S1 triage.
- **S3 bands:** ≥0.86 auto-merge, no model call · 0.72–0.86 exactly one adjudication call, on the nearest
  ambiguous candidate only · <0.72 distinct. The survivor is always the *older* report. Roll-up: 3+
  challenges across 2+ blocks at ≥0.62 → a routable `BLOCK_SYSTEMIC` parent.
- **S4 weights:** severity .28 · people affected .20 · block vulnerability .18 · corroborations .14 ·
  recurrence .12 · official endorsement .08 — scaled 0–100, `weight × normalised` rounded before
  multiplication so the arithmetic on screen checks out by hand.
- **S5 match:** semantic fit .45 · specialisation overlap .20 · distance .15 (`exp(-km/250)`) · declared
  capacity .12 · track record .08 (Laplace-smoothed) → top **3 distinct organisations**, never two labs at
  one college. `guardReason()` rejects any sentence containing a number that wasn't in the facts given.
- **Human gate:** severity ≥ 0.70 → `persistRoutes()` writes `notified_at = null`; only `releaseGate()` at
  `/gov/gate` sends anything. Overrides require a ≥10-character reason.
- **Ledger:** a Postgres trigger refuses UPDATE/DELETE on `ledger_entries`;
  `entryHash = sha256({seq, contentHash, prevHash, authorId, createdAt})`; an advisory transaction lock
  stops two concurrent appends forking the tip.
- **Reaper:** `SELECT … FOR UPDATE SKIP LOCKED`, one transaction per row; slow work (the S5 re-run at
  WIDEN, the annual rescore) is computed *before* the transaction opens so a model call never holds a lock.
  Vercel Hobby can't do sub-daily cron — documented, not hidden, and `/demo` triggers a sweep manually.
- **Offline:** `docker compose up -d` (pgvector Postgres 17, MinIO, Mailpit) + `AI_PROVIDER_CHAIN=rules`.
- **Testing:** `tests/invariant.test.ts` is the required CI check — "fix the table, never the test." **Don't
  quote a test count you haven't measured:** README says 113 (91 without a database) but the 14 test files
  contain 127 `it()` blocks — the README number looks stale. Run `pnpm vitest run` in the morning and say
  whatever it prints, or just say "the full suite".
- **Seed:** 24 districts, 263 blocks, 20 orgs, 25 challenges — real Jharkhand names, enforced in CI by
  `pnpm verify:seedguard`, because one "Test University" discredits the other 24 rows.
