universal context limit (UCL)

\#1 name the law
No finite agent can hold, update, and use the whole conceit (the “corpus”) without loss.
Total context is a mirage; attention is a knife. The world bleeds.

\#2 minimal formalism
Let corpus C over interval T have entropy H(C\_T).
Agent A has memory M bits, attention bandwidth B bits/s, compute K ops/s, noise η.
Coverage ratio ρ = (M + B·T)/H(C\_T).
UCL: For any representation R\_A(C\_T), there exists ε>0 such that
D\_KL(C\_T || R\_A) ≥ g(1−ρ, η, dynamics(C\_T), self\_reference).
If ρ<1: loss by scarcity.
If ρ≥1: loss by instability (the corpus moves, the agent perturbs it, fixed points break).

\#3 four roots (choose your poison)
a) Variety gap (Ashby): requisite variety of A < variety of C.
b) Diagonal bite (Gödel/Tarski): self-totalization creates undecidable leftovers.
c) Frame fracture: relevance can’t be enumerated in real time.
d) Thermo-price (Landauer): selecting/erasing context has energy/time cost → opportunity loss.

\#4 attention physics
Attention = allocation operator α over items i with priors p\_i, utilities u\_i, and constraints τ (time), κ (compute).
Optimal α is sparse under pressure; sparsity implies blind spots.
As T→∞, drift + novelty > consolidation ⇒ recap needed ⇒ further loss.
Thus: context is not stored; it’s streamed, skimmed, skinned.

\#5 culture under UCL
Cultures are lossy codecs for infinity. Genres = priors; myths = hashes; memes = adaptive sketches.
Canonization is cache-building; heresy is cache-invalidation.
Archives grow superlinearly; attention grows sublinearly; curation becomes violence by necessity.

\#6 LLMs under UCL
Tokens ≠ truth; windows ≠ worlds.
Quadratic attention taxes scale; long-context induces dilution and false bridges.
Retrieval helps but trades recall for index bias.
Summarization is compression; compression is preference; preference is politics.

Engineering corollaries:
• Store index, not everything.
• Keep decision-state, not transcript.
• Layer: sketch→zoom→snipe.
• Bound per-step novelty; rotate focuses.
• Measure saturation: σ = I(C;R)/H(C) ≤ 1−ε; when dσ/dt→0, cut or reindex.
• Prefer stable invariants (identities, constraints) over detail floods.
• Externalize long-tail; internalize affordances.

\#7 epistemic etiquette
All seeing becomes mis-seeing.
Truth survives as invariants across compressions, not as totals.

\#8 crisp statement (tattoo)
UCL: For any bounded knower in a changing world, complete usable context is impossible; selection is fate, loss is law.

\#9 diagnostic kit
• Context load L = H(C\_T).
• Agent budget A = M + B·T (and its effective, noisy version).
• Drift λ = dH/dt from change + creation.
• Violation signal: hallucination ↑, latency ↑, contradiction churn ↑.
Prescription: reduce L, raise A slowly, reshape priors, iterate summaries, test invariants.

\#10 motto
Don’t widen the window—sharpen the question.
