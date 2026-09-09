# The lifecycle speech — citizen → verified impact

**264 words → 1:53** at 140 wpm (2:03 slow). This is a *story*, so drop the buzzwords here and lean on the one named
human. Reserve the tech vocabulary for the other section; if you use both registers in one breath you sound
like a pitch deck reading itself.

Built around the real seeded case in this repo, so you can rehearse against `/demo`: **Sunita Devi,
Gumla, JH-2026-GUM-0001, the South Koel embankment.**

---

## THE SPEECH (2:00)

Everything I just described exists for one path. Let me walk it.

Sunita Devi, Gumla district. She reports in Hindi — the South Koel embankment is cracking. She gets a
tracking ID she can **say over the phone**. And in that same transaction: her report, a credit edge with
her name on it, and a ledger entry. Her words are never replaced — the English sits *beside* them.

Then the machine spends about eight seconds on it. Is it safe? Is it actually a grievance? What domain,
how severe? Three neighbours reported the same crack, so the reports **merge** and the count goes up —
duplicates are corroboration, not noise. Then a score from six weighted terms, no model in the loop, and
she can see the arithmetic. Then three departments whose capability actually matches, each with a written
reason.

Severity is high — so **nothing is sent.** A District Collector reviews it and releases it.
Only then does the clock start: seven days, nobody claims it, widen. Fourteen, every college in
Jharkhand. Twenty-one, that's a breach, and it's public.

BIT Sindri claims it. Every student is credited **by name**, and Sunita joins that team as domain informant.
They research, and they publish — the artifact's hash goes into the ledger. That doesn't stop anyone *filing*
a patent; it's what stops one being **granted** over this work.

Tata Steel Foundation picks it up, funds it, marks it **implemented**. And here's the line I'd defend all
day: that's a claim, not an outcome. The impact number does not move until Sunita — on a link, no login —
says *yes, it's fixed.*

---

## IF THIS SECTION STANDS ALONE (nothing before it)
Swap the first line for: *"Forget the architecture for a second. Here's what a citizen's Tuesday looks
like, start to finish."* Everything after works unchanged.

---

## IF YOU HAVE 3 MINUTES — insert these, don't rewrite

**After "beside them." (+22 s)** — the intake reality:
"She typed into a six-step form that works at three-twenty pixels, because she's on a cheap phone. Photos
are blurred **on her device** before upload — the unblurred original never leaves it. Metadata and GPS are
stripped server-side. There's a moderation pre-filter and a rate limit before a single token is spent, and
and if the photo upload fails she still gets a tracking ID — the page just says the photo didn't store."

**After "public." (+25 s)** — the failure branches, which is where you sound senior:
"And it cuts both ways. If the pipeline halts mid-stage, the citizen keeps her triage — every stage is
isolated, so a broken router never costs a report its safety check. If a team claims and never writes a proposal, the claim is released at twenty-one days — the project is
marked undelivered, **never deleted**, and their credit stays attached. If they go quiet mid-research, they're
flagged at-risk at thirty days and another team gets fork rights at forty-five. A failed team does not lose
its work. We don't erase people's contributions."

**After "no login — says yes." (+18 s)** — the close that lands on stage:
"And if she says no, it goes to **disputed** and the counter doesn't move. That's why the CSR report a
company files shows confirmed, partly-confirmed, and claimed-but-unconfirmed as three numbers that are
never added together. We show you what we haven't proved. That's why you can believe what we have."

## IF YOU ONLY HAVE 60 SECONDS
"She reports in Hindi. One transaction saves her words, her credit and a ledger entry. Eight seconds of
AI: safety, domain, severity, dedup, a score with visible arithmetic, and three matched departments. High
severity means it waits for an officer, not an algorithm. Seven days with no claim and it escalates
publicly. A college takes it, students get credited by name, the citizen gets a hash-stamped publication,
industry funds the pilot. And the impact counter only moves when *she* confirms it. The AI proposes, code
decides, and the citizen has the last word."

---

## THE 15 STATES — memorise the shape, not the list
`SUBMITTED → TRIAGED → CLASSIFIED → CLUSTERED → PRIORITISED → VERIFIED → ROUTED → CLAIMED →
PROPOSAL_APPROVED → IN_RESEARCH → SOLUTION_PUBLISHED → INDUSTRY_INTEREST → IMPLEMENTED →
CITIZEN_VERIFIED → CLOSED`

Four blocks, six stages each, and the story has three hand-offs: **citizen → state → university → market.**
Side doors worth naming if pushed: `MERGED` (duplicate, terminal but credited) · `PARKED` (below the
routing bar, re-reviewed annually) · `FORWARDED_EXTERNAL` (grievance, out to CPGRAMS) · `REJECTED_UNSAFE`
(media purged, helpline shown) · `DISPUTED` (citizen said no) · `BOUNTY_LISTED` / `AT_RISK` / `FORKED`
(the clocks biting).

## SCREEN CUES (matches the runbook order)
| Beat | Show |
|---|---|
| Sunita reports | `/submit`, then `/c/JH-2026-GUM-0001` |
| 8-second pipeline | `/demo` → Run the pipeline, or `#pipeline` on the challenge page |
| Score + reason | the priority breakdown on that page — "this is public, no login" |
| Officer releases | `/gov/gate`, from the **DC session**, not the admin one |
| Escalation | `/demo` → **+21 days**, then `/bounties` |
| Claim | `/hei/challenges/JH-2026-GUM-0001/claim`, then the project's credit chain |
| Publish | the artifact page + `/ledger`, press **Verify chain** |
| Industry | `/industry/interests/[id]`, then `/industry/csr` |
| Last word | the SMS inbox on `/demo`, then `/stats` — the confirmation gap |

## QUESTIONS THIS SECTION INVITES
- **"Why does a citizen confirm it and not the college?"** Because the college grading its own success is
  how every scheme report in the country gets written. She lived with the embankment.
- **"What if she never answers?"** A 30-day `IMPACT_UNCONFIRMED` deadline re-asks. It is never counted as
  success by default — silence is not consent, and it's not impact either.
- **"Isn't 'industry implements' outside your scope?"** We route and evidence it; we don't build it. Funding
  interest, MoU, and the implementation claim are recorded and hashed — the rails beyond that are declared
  stubs, and the CSR export is the product for that buyer.
- **"How is this not just a workflow tool with an LLM on top?"** The clocks. Every non-terminal state carries
  a durable deadline row, and CI fails the build if one doesn't. Workflow tools let things go quiet.
