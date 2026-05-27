# Te Ara Tika — Responsible AI from the Ground Up
**A practical framework for AI in Aotearoa, built from tikanga and manaakitanga**
*Draft 0.1 — offered as koha, not crown*

---

## He Whakataukī

> *"Ehara tāku toa i te toa takitahi, engari he toa takitini"*
> My strength is not that of one, but that of many.

AI built without community is not intelligence — it is extraction.

---

## Why This Document Exists

The Ministry for Regulation's *Responsible AI in Action* (May 2026) names the right risks but cannot resolve them, because it begins from the wrong place. It starts with the state and works toward people. This document starts with people and works toward systems.

Three material failures in the current guidance:

**1. No SOTA model runs on NZ soil.**
Every frontier LLM inference endpoint is offshore — US or EU hyperscalers. There is no architecture by which a regulator can tick "data sovereignty" and also use GPT-4, Claude, or Gemini for anything sensitive. These are mutually exclusive. The guidance does not say this.

**2. Te Tiriti compliance is structurally impossible under current LLM pipelines.**
Foundation models ingest data at scale without consent, provenance, or the ability to withdraw. Māori data, once absorbed into training, cannot be corrected, removed, or governed. "Engage Māori early" cannot fix a model that has already consumed data without authority. Te Tiriti obligations require control *before* ingestion, not consultation *after* deployment.

**3. The cost floor is artificial.**
Current token pricing is venture-subsidised market capture. When subsidies end — and they will — government agencies locked into frontier model pipelines will face pricing they cannot sustain. Sovereignty requires the ability to exit.

---

## The Framework: He Aho Matua

Rather than bolt ethics onto a procurement checklist, this framework makes tikanga the load-bearing structure.

### Manaakitanga — the obligation of care

*Before any AI system touches a person, ask: does this increase or decrease their mana?*

- does the system treat the person as a subject with authority over their own information, or as a data point?
- can the person see what the system knows about them, correct it, and withdraw consent?
- does the system's error mode *protect* the person (false negative = ask a human) or *process* them (false positive = flag for action)?

Systems that cannot answer these questions affirmatively should not be deployed on people.

### Whakapapa — traceability all the way down

Every AI output in a regulatory context must have a whakapapa: where did this conclusion come from, and who is responsible for it at each step?

This means:
- **model provenance**: what was this model trained on? Is the training data documented?
- **prompt provenance**: what instructions shaped this output? Are they versioned and auditable?
- **decision provenance**: which human read this output, and what did they actually do with it?

"The AI suggested it and a human approved it" is not whakapapa. It is a gap in accountability dressed as a process.

### Kaitiakitanga — stewardship, not ownership

Data about people does not belong to the agency that holds it. Agencies are kaitiaki — guardians with responsibilities, not owners with rights.

Operational implications:
- data should be held in the minimum form necessary for the minimum time necessary
- AI systems should not retain or learn from interactions with the public unless explicitly consented to
- agencies should be able to account for every data flow to every third party, including cloud inference providers

For Māori data specifically: Te Mana Raraunga's CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) are not compatible with how foundation model training works. The only currently honest position is: **do not send Māori personal data to foundation models you do not control.**

### Kotahitanga — collective benefit, not efficiency extraction

The frame of "AI reduces administrative burden" optimises for the agency. Kotahitanga asks: does this reduce burden for the *person* navigating the system?

These are often opposite. A triage model that routes 80% of applications automatically is efficient for the agency and opaque and unaccountable for the applicant. Kotahitanga would require: the applicant understands why they were routed this way, can challenge it, and receives a response from a person who has actually read their case.

---

## What Viable Responsible AI Actually Looks Like

### The sovereignty stack

For any AI system touching NZ public data, viable means:

| Layer | Requirement | Current reality |
|---|---|---|
| Inference | On NZ soil or Five Eyes minimum with data processing agreement | Unavailable for frontier models |
| Model | Open weights, auditable, self-hostable | Available (Llama, Qwen, Mistral) at reduced capability |
| Training data | Provenance documented, consent frameworks in place | Not available for any foundation model |
| Fine-tuning | Agency-controlled, on agency infrastructure | Achievable with modest investment |
| Retrieval | Local vector/BM25 index over agency documents | Achievable now |

**The honest tier for current NZ government use:** retrieval-augmented generation over agency documents using locally-hosted open-weight models. Not GPT-4. Not Claude. Smaller, auditable, controllable. The capability gap is real but the sovereignty gap is worse.

### The human pipeline

The current guidance says "human in the loop." This is insufficient. The requirement is:

**Humans first, second, and last.**

Specifically:
- a domain expert — not a generalist reviewer — reads source material, not just AI summaries
- AI is permitted to surface, not to synthesise for decision
- the human's independent assessment is documented *before* they see the AI output, where practicable
- the final decision references the source material, not the summary

This costs more. That is the point. If the cost of genuine human judgment is too high, the answer is more resourcing, not AI substitution.

### Token cost is not efficiency

There is no stable efficiency metric for LLM use. Output quality is non-linear with token spend. A 0-shot prompt and a 1000-token engineered prompt can produce equivalent outputs or wildly divergent ones depending on factors the agency does not control and cannot audit. "30 minutes per person per day" savings claims are not reproducible, not comparable across agencies, and will not survive vendor pricing changes.

Efficiency claims in AI procurement should require: controlled trials, counterfactual comparison, and a cost model that includes the real token price when subsidies end.

---

## What to Build Instead

If Aotearoa wants AI infrastructure that can actually honour its obligations, the investment required is:

**1. A sovereign compute layer**
NZ universities and Crown Research Institutes already have GPU infrastructure. A shared national inference cluster running open-weight models, operated under NZ law, is achievable. It requires coordination and political will, not new technology.

**2. Iwi-participatory data governance**
Not consultation. Governance. Iwi representatives with decision-making authority over what data is used to train or fine-tune models that will affect their communities. This exists as a concept (Te Mana Raraunga). It needs institutional teeth.

**3. Open-source first procurement**
Any AI system procured by a government agency should default to open weights, local hosting, and published system prompts. Closed, offshore, proprietary systems require a positive case — not the other way around.

**4. Honest capability scoping**
A government agency using a locally-hosted Qwen 7B for document retrieval is doing something responsible and auditable. A government agency routing case decisions through a closed frontier API is not, regardless of what the contract says. Name the difference.

---

## The Checklist This Document Would Generate

Before deploying any AI system in a regulatory context:

- [ ] Can inference run on NZ-controlled infrastructure? If not, document why not and what data is excluded.
- [ ] Is the model's training data provenance documented? For Māori data: is there any possibility this model was trained on data without iwi authority? If yes, do not use it for decisions affecting Māori.
- [ ] Can a domain expert — not a generalist — independently assess the AI's source material without the AI's summary?
- [ ] Is the system's error mode set to protect the subject (conservative false negative) rather than process them?
- [ ] Can the person affected see the full decision trail, including the AI's output and the human's independent assessment?
- [ ] Does the cost model include post-subsidy token pricing? What is the exit path?
- [ ] Has an iwi representative with decision-making authority (not advisory role) reviewed the data governance for any system touching Māori data?
- [ ] Can this system be paused, rolled back, and fully replaced without operational disruption within 48 hours?

---

## He Mihi Whakamutunga

This document is living. Incomplete and currently naive as it should be. A framework built from tikanga does not arrive finished — it arrives in relationship, and it grows through use and correction.

The current guidance is not malicious, but that doesn't make it not dangerous. It is written by people working within constraints they cannot name. Those constraints — offshore infrastructure dependency, vendor capture, a procurement culture that treats "responsible AI" as a compliance checkbox — are the actual problem.

The path forward is not better checklists. It is infrastructure we control, governance with actual teeth, and the honest admission that some uses of AI are not responsible at any level of governance sophistication.

*Nō reira, tēnā koutou, tēnā koutou, tēnā koutou katoa.*

---

*Draft 0.1 — May 2026. Offered for critique, correction, and koha.*
*Not crown copyright. Commons.*
