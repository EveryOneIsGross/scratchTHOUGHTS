# Te Ara Tika, Responsible AI from the Ground Up
**A practical framework for AI in Aotearoa, built from tikanga and manaakitanga**
*Draft 0.3, offered as koha, not crown*

---

## He Whakataukī

> *"Ehara tāku toa i te toa takitahi, engari he toa takitini"*
> My strength is not that of one, but that of many.

AI built without community is not intelligence. It is extraction.

---

## Why This Document Exists

The Ministry for Regulation's *Responsible AI in Action* (May 2026) names the right risks but cannot resolve them. It begins with the state and works outward toward people. This document begins with people and works outward toward systems.

Four structural failures in the current guidance:

**1. No SOTA model runs on NZ soil.** Every frontier LLM inference endpoint is offshore, US or EU hyperscalers. There is no architecture by which a regulator can tick "data sovereignty" and also use GPT-4, Claude, or Gemini for sensitive work. These are mutually exclusive. The guidance does not say this.

**2. Te Tiriti compliance is structurally impossible under current LLM pipelines.** Foundation models ingest data at scale without consent, provenance, or the ability to withdraw. Māori data, once absorbed, cannot be corrected, removed, or governed. Consultation after deployment cannot fix a model that has already consumed data without authority. Te Tiriti obligations require control before ingestion.

**3. The cost floor is artificial.** Current token pricing is venture-subsidised market capture. When subsidies end, agencies locked into frontier model pipelines will face pricing they cannot sustain. Sovereignty requires the ability to exit.

**4. Operators sit at the terminus of pipelines they cannot inspect.** Current "human in the loop" framings position the worker at the end of a process they did not design, cannot see inside, and have no authority to modify. This is rubber-stamping dressed as oversight. Responsible AI requires the pipeline be legible and contestable to the people whose work it shapes.

---

## He Aho Matua, The Framework

Tikanga is the load-bearing structure, not a frame around a procurement checklist.

### Manaakitanga, the obligation of care

Before any AI system touches a person, ask whether it increases or decreases their mana.

- The system must treat the person as a subject with authority over their own information, not a data point.
- The person must be able to see what the system knows about them, correct it, and withdraw consent.
- The system's error mode must protect the person, a conservative false negative that routes to a human, not process them through a false positive that flags for action.

Systems that cannot answer these affirmatively are not deployed on people.

### Whakapapa, traceability all the way down

Every AI output in a regulatory context carries a whakapapa. Each layer is documented and each layer has someone responsible.

- **Model provenance**: training data documented and auditable.
- **Prompt provenance**: instructions versioned, accessible, and logged with output.
- **Retrieval provenance**: documents pulled and documents left behind, both visible. Retrieval is a decision.
- **Evaluation provenance**: how the system is known to be fit for purpose, on this data, in this context. Imported evals are imported assumptions.
- **Decision provenance**: which human read what source material independently, and what they did.

"The AI suggested it and a human approved it" is not whakapapa. It is a gap dressed as a process.

**Model lifecycle and the right to be forgotten.** Foundation models cannot be retrained on request. The cost is prohibitive and the architecture does not permit selective forgetting. This is incompatible with the Privacy Act, with Te Tiriti obligations, and with consent withdrawal as a meaningful concept. Agencies deploying such systems must document the post-inference mitigations that honour removal requests, output filtering, retrieval exclusion, refusal scaffolding, and the obsolescence horizon: the date past which continuing to use the model is indefensible. A model trained on data that can never be unlearned has a finite responsible lifespan. That lifespan is named at procurement, in writing.

### Kaitiakitanga, stewardship, not ownership

Data about people does not belong to the agency that holds it. Agencies are kaitiaki, with responsibilities, not owners with rights.

- Data is held in the minimum form necessary for the minimum time necessary.
- AI systems do not retain or learn from interactions with the public without explicit consent.
- Every data flow to every third party, including cloud inference providers, is accounted for.

For Māori data: Te Mana Raraunga's CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) are not compatible with how foundation model training works. The honest position is direct. **Māori personal data is not sent to foundation models the agency does not control.**

### Whakamana Kaimahi, operator sovereignty over the pipeline

The people doing the work hold the only situated knowledge of what correct means in this specific case. Pipelines that hide intermediate layers from operators do not produce oversight. They produce compliance theatre. They reproduce the extraction logic the framework refuses: the public processed at one end, the operator reduced to terminus at the other, the decisions held in a middle nobody is permitted to touch.

Operator sovereignty has four properties:

- **Legibility.** Every intermediate artefact, retrieval set, prompt, model output, confidence signals, discarded alternatives, is visible to the operator handling the case. Synthesis without source is not assistance. It is dictation.
- **Modifiability.** The operator alters prompts, re-runs with different parameters, swaps retrieval scope, substitutes models for their specific case. System prompts are not policy. They are procedure, and procedure is negotiable at the point of application. Modifications log to the decision whakapapa.
- **Contestability.** When an output is wrong, the operator's correction flows back as first-class evaluation data. Not into a complaints queue. Not into a satisfaction survey. Into the eval layer that determines whether the system continues to be deployed. Operators are the eval layer.
- **Protected refusal.** A no-AI path for the same task exists at every point of the workflow, without productivity penalty and without surveillance that makes the AI path coercive. Opt-out under productivity surveillance is not opt-out.

Pipeline opacity is a working condition. Knowledge workers are owed the same legibility over their tools that any tradesperson assumes over theirs.

### Kotahitanga, collective benefit, not efficiency extraction

The frame of "AI reduces administrative burden" optimises for the agency. Kotahitanga asks whether the burden is reduced for the person navigating the system.

These are often opposite. A triage model that routes 80% of applications automatically is efficient for the agency, opaque to the applicant, and unaccountable to the public. Kotahitanga requires the applicant understand the routing, retain the ability to challenge it, and receive a response from a person who has read their case.

Efficiency is a question of for whom, measured how, and surviving what cost curve.

---

## What Viable Responsible AI Looks Like

### The sovereignty stack

For any AI system touching NZ public data:

| Layer | Requirement | Current reality |
|---|---|---|
| Inference | NZ soil, under NZ law | Unavailable for frontier models |
| Model | Open weights, auditable, self-hostable | Available (Llama, Qwen, Mistral) at reduced capability |
| Training data | Provenance documented, consent frameworks in place | Not available for any foundation model |
| Fine-tuning | Agency-controlled, on agency infrastructure | Achievable with modest investment |
| Retrieval | Local vector/BM25 index over agency documents | Achievable now |
| Evaluation | Domain-specific, operator-fed, locally maintained | Almost never done; usually imported from vendor |

The honest tier for current NZ government use: retrieval-augmented generation over agency documents, locally-hosted open-weight models, operator-visible retrieval, operator-fed eval loops. Not GPT-4. Not Claude. Smaller, auditable, controllable. The capability gap is real. The sovereignty gap is worse.

### Pre-registered human judgment

"Human in the loop" is insufficient. The requirement is pre-registered judgment: where practicable, the human's independent assessment is documented before they see the AI output.

Once a reviewer has read the synthesis, their independent assessment is contaminated. Confirmation bias is a known cognitive property of reading summaries before sources, not a personal failing. Pre-registration distinguishes oversight from anchoring.

- A domain expert, not a generalist reviewer, reads source material before the AI output.
- AI surfaces alternatives the human missed. It does not pre-frame the decision.
- The final decision references the source material. The AI output is auxiliary.

This costs more. If the cost of human judgment is too high, the remedy is resourcing, not AI substitution.

### Token cost is not efficiency

There is no stable efficiency metric for LLM use. Output quality is non-linear with token spend. Equivalent prompts produce divergent outputs depending on factors the agency does not control and cannot audit. Per-person time-savings claims are not reproducible, not comparable across agencies, and will not survive vendor pricing changes.

Efficiency claims in AI procurement require: controlled trials, counterfactual comparison, a cost model that includes post-subsidy token pricing, and a clear account of whose time is saved and whose time is absorbed instead. Most efficiency claims are transfers, agency time saved, operator cognitive load increased, applicant burden unchanged or worsened.

---

## What to Build Instead

**1. A sovereign compute layer.** NZ universities and Crown Research Institutes (NeSI, REANNZ, university clusters) hold the substrate. A shared national inference capability running open-weight models under NZ law, with operator-accessible SLAs, does not yet exist. The gap is political and organisational, not technical.

**2. Iwi-participatory data governance.** Not consultation. Governance. Iwi representatives with decision-making authority over what data is used to train or fine-tune models affecting their communities. Te Mana Raraunga holds the concept. The institution needs teeth.

**3. Open-source first procurement.** Any AI system procured by a government agency defaults to open weights, local hosting, and published system prompts. Closed, offshore, proprietary systems require a positive case.

**4. Operator-fed evaluation infrastructure.** Eval is not a vendor deliverable. It is a continuing collaboration between the people doing the work and the people maintaining the system. This requires tooling that treats operator corrections as primary data, time allocation for operators to participate in eval rather than only consume outputs, and a feedback loop short enough that operators see their corrections produce visible system change. Sovereignty over compute without sovereignty over eval is hollow.

**5. Honest capability scoping.** A locally-hosted Qwen 7B for document retrieval, with operator-visible pipeline and operator-fed eval, is responsible and auditable. A closed frontier API routing case decisions is not, regardless of the contract.

---

## Checklist

Before deploying any AI system in a regulatory context.

**Sovereignty and data**
- [ ] Inference runs on NZ-controlled infrastructure, or the exclusions are documented.
- [ ] Training data provenance is documented. For any system touching Māori data: training-data authority is established, or the system is not used.
- [ ] An iwi representative with decision-making authority, not advisory role, has reviewed data governance for any system touching Māori data.
- [ ] For models that cannot be retrained: post-inference mitigations for removal requests are documented (output filtering, retrieval exclusion, refusal scaffolding). The model's obsolescence horizon is named in writing.

**Decision integrity**
- [ ] A domain expert assesses source material independently before being exposed to AI output.
- [ ] The system's error mode protects the subject. False negatives route to humans. False positives do not flag for action.
- [ ] The person affected can see the full decision trail, including AI output and the human's independent assessment.

**Operator sovereignty**
- [ ] The operator inspects every intermediate artefact, retrieval results, prompts, model outputs, discarded alternatives, not only the final synthesis.
- [ ] The operator modifies prompts and re-runs for the specific case. Modifications log to the decision whakapapa.
- [ ] The operator flags wrong outputs into the evaluation layer, not a complaints queue.
- [ ] A no-AI path exists at every point of the workflow, without productivity penalty or surveillance that makes the AI path coercive.

**Sustainability and exit**
- [ ] The cost model includes post-subsidy token pricing. The exit path is documented.
- [ ] The system can be paused, rolled back, and fully replaced without operational disruption within 48 hours.

---

## He Mihi Whakamutunga

This document is living. A framework built from tikanga does not arrive finished. It arrives in relationship and grows through use and correction.

The current guidance is not malicious. It is dangerous. It is written by people working within constraints they cannot name, offshore infrastructure dependency, vendor capture, procurement culture that treats responsibility as a compliance checkbox, an industrial logic that treats operators as the last cheap step in someone else's pipeline.

The path forward is infrastructure we control, governance with teeth, operators with authority over their own tools, and the admission that some uses of AI are not responsible at any level of governance sophistication.

*Nō reira, tēnā koutou, tēnā koutou, tēnā koutou katoa.*

---

*Draft 0.3, May 2026. Offered for critique, correction, and koha.*
*Licensed CC BY-SA 4.0. Not crown copyright. Commons.*
