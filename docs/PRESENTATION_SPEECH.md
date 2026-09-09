# The 2-minute speech — pitch version

**276 words → 1:58** at a confident 140 wpm (2:09 if you speak slowly). Line break = breathe. **Bold** = lean on it.
Every buzzword below is *literally true of this codebase* — the defence table at the bottom is how you
keep it that way when a judge pushes back.

---

## THE SPEECH

Two minutes, four sections, and one promise: everything I say has a **receipt** in the repo.

**Stack first.** Monolith-first, on purpose. One Next.js 15 serverless deployable, React 19, strict TypeScript,
Tailwind and shadcn on the front. One Postgres is our system of record *and* our
vector store *and* our event log — zero infrastructure sprawl, zero vendor lock-in. On inference: a
provider-agnostic chain — Gemini, Groq, then a deterministic rules tier — behind one interface, with an
embedding cache and per-call receipts. So cost and latency are **observable**, not vibes.

**How we built it.** Spec-driven. Ten invariants as a shared contract for the humans *and* the AI agents
writing code with us. Every task ships with its own verification; CI is a hard gate — typecheck, build, the suite,
and a gate that fails the deploy if one challenge can go dark.

**Architecture.** Event-sourced at the edge. One state machine owns every transition, and each one commits
the status, a hash-chained ledger entry, the SLA deadline and the outbox event in one **atomic**
transaction. No blockchain — but tamper-evident, and anyone can verify the chain in their browser. Dead
teams, silent departments? A self-healing escalation ladder: seven, fourteen, twenty-one days, and it's
public.

**The AI pipeline.** Six stages, agentic but governed. Language, safety triage, classification on a
retrieval-augmented kNN prior, semantic dedup over pgvector, scoring, capability routing. The
differentiator: **S4 makes zero model calls** — pure deterministic scoring, fully explainable, every
weight on screen. Confidence-gated, human-in-the-loop above severity point seven, with output guardrails
that reject any number the model can't source.

The AI proposes. Deterministic code decides. A human holds the authority.
**That's how you put AI in front of a government.**

---

## THE DEFENCE TABLE — say the buzzword, own the receipt

| You said | If they ask "what does that mean here?" |
|---|---|
| Monolith-first | One Vercel deployable; every module is its own folder, so it splits into services later without a rewrite |
| Zero infra sprawl | Postgres 17 (Supabase) = rows + `pgvector` HNSW + FTS/`pg_trgm` + outbox. No Redis, no Kafka, no second DB, no k8s |
| Provider-agnostic | `lib/ai/providers/chain.ts` — Gemini → Groq → `rules.ts`; `AI_PROVIDER_CHAIN` is config, not code |
| Observable | Every model call writes an `ai_runs` row: provider, model, fallback level, confidence, latency, input hash. `/admin/ai-runs` shows p50/p95 per stage |
| Embedding cache | 768-d vectors keyed on input hash; a cache hit still writes a receipt as `provider: "cache"` so the trace never lies |
| Spec-driven + AI agents | `CLAUDE.md` invariants + `docs/PHASE_N_BUILD.md`; every task ends with a verification block and a commit |
| CI hard gate | `ci.yml`: typecheck, lint, build, vitest, `verify:seedguard` (no placeholder data), and the invariant-1 check |
| Event-sourced at the edge | `stateMachine.ts` is the *only* writer of `challenges.status`; hand-written `UPDATE … SET status` is defined as a bug |
| Hash-chained / tamper-evident | SHA-256 chain, `prevHash → entryHash`, append-only by a **Postgres trigger**, verified client-side at `/ledger` |
| Self-healing escalation | `sla_deadlines` rows + reaper on cron: WIDEN +7d, OPEN_ALL +14d, BREACH +21d → `/bounties`, GRAND_CHALLENGE +45d |
| Agentic but governed | Models return structured facts + confidence; branching, merging, scoring, routing are plain TypeScript |
| Retrieval-augmented kNN prior | S2 classification is seeded by cosine-nearest already-labelled challenges — "learning" without a fine-tune |
| Human-in-the-loop, confidence-gated | severity ≥ 0.70 → `notified_at = null`; only `releaseGate()` at `/gov/gate` sends anything. Low-confidence answers → `/admin/triage` |
| Output guardrails | `guardReason()` rejects a routing sentence containing any number not in the facts it was handed — code, not a prompt instruction |

## DO NOT ADD THESE (they'd be fake depth)
- **"Fine-tuned / custom model"** → we don't. Say: *few-shot plus an embedding prior, and every human
  override becomes labelled training data.*
- **"Blockchain / smart contracts"** → the ledger is deliberately *not* one; say "tamper-evident SHA-256 chain."
- **"Real-time / WebSockets"** → it's SSE over a native `ReadableStream`. Say "live-streamed trace."
- **"Multi-language support"** → Hindi, English, one Santali sample. Say "built for ten, shipped with three."
- **"Kubernetes / microservices at scale"** → one app, one DB. The monolith *is* the flex.

## CLOSER — pick your temperature
- Measured: "The AI proposes. Deterministic code decides. A human holds the authority."
- Louder: "Anybody can bolt an LLM onto a demo. The hard part is making it **auditable** — and that's the
  part we spent the sprint on."
