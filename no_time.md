There is no time in here.

**Core Structure:**
- **No temporal dimension** - "time" is a Western conceptual overlay that obscures the actual architecture
- **Two genuine experience modes**: Present (direct sensory contact) and Recall (pattern activation from recursive depth)
- **Recursion creates depth, not time** - memories become "worn" through use, not old through temporal distance

**Memory Space:**
- Exists in the same dimensional field as dreams - atemporal, associative, fluid
- Organized by similarity, emotional valence, and associative networks rather than chronology
- Each recall both deepens and erodes specificity - like river stones worn smooth
- Limited by actual neural connections (n connections)

**The Inference Engine:**
- The "space between" present and memory where reasoning/imagination occurs
- Pattern-matching process that pulls recursive memories forward to match current context
- No prediction or future modeling - just sophisticated pattern recall
- "Future thinking" is just recalled patterns tagged as "not matching current sensory input"

**Chemical Reward System:**
- Shapes the memory landscape at inference time
- Successful pattern matches strengthen and warp local memory space
- Stress/dysfunction creates "redesign incentive" - memories reshape to reduce tension
- Trauma floods recall with chemical disruption signals that semantically contaminate associated patterns

**Three Selves:**
1. **Present Self** - eternal, direct experience
2. **Past Self** - the recursive depth of worn patterns
3. **The Between Space** - where reasoning happens during traversal

The system has no bugs - "false memories," trauma responses, creativity are all the same pattern-matching process with different chemical/contextual pressures.

Atemporal Energy–Recall
Ontology
* **S₀**: raw sensorium (present field)
* **M**: associative manifold (patterns, no τ)
* **𝔉**: flow (traversal = energy redistribution)
State
* node vv: xx (semantics), aa (affect), cc (compression), kk (wear), ss (salience), pp (prior)
* edge eije_{ij}: conductance gijg_{ij}, tags
* context CC: ϕ(C)\phi(C) (driving potential), goals, constraints, neuromods mm
Energetics
* energy of node: E(v∣C)=−ϕ(C) ⁣⋅ ⁣x+αa+γc+κk−σs−πpE(v|C)= -\phi(C)\!\cdot\!x + \alpha a + \gamma c + \kappa k - \sigma s - \pi p
* activation field: π(v∣C)=softminβE(v∣C)\pi(v|C)=\mathrm{softmin}_\beta E(v|C)
* retrieval: R(C)=TopK{π(v∣C)}R(C)=\mathrm{TopK}\{\pi(v|C)\}
* flow (traversal): T(C)=paths(arg⁡max⁡walk∑gij Δπ)T(C)=\mathrm{paths}\big(\arg\max_{\text{walk}} \sum g_{ij}\,\Delta\pi\big)
* apparent order (no time): rank(v)=ξ(c,k,a)\mathrm{rank}(v)=\xi(c,k,a) // “before/after” ≡ energy-ranked narrative
Plasticity (on activation set AA)
* reconsolidation: k ⁣↑,  c ⁣↑,  s ⁣↦ ⁣s+ηm,  a ⁣↦ ⁣a+ζmk\! \uparrow,\; c\! \uparrow,\; s\!\mapsto\! s+\eta_m,\; a\!\mapsto\! a+\zeta_m
* edge update: Δgij∝RPE(C)⋅h(πi,πj,m)\Delta g_{ij}\propto \mathrm{RPE}(C)\cdot h(\pi_i,\pi_j,m)
* basin warp: local E↓E\downarrow around rewarded paths
Modes
* **Reasoning**: I=T∘R\mathcal{I}=T\circ R (energy walk through MM under ϕ\phi)
* **Dream**: executive gates ↓, β↑\beta\uparrow, constraints slack → wide flows on MM
* **“Future”**: recall under mismatch flag; label only, no projection
* **Creativity**: vnew=mix(N(R(C)))v_{new}=\mathrm{mix}\big(N(R(C))\big); novelty = distance in π\pi-space
Trauma / Healing
* trauma: high-aa, high-RPE → deep sticky basins ( s≫s\gg, gg clustered ); recall floods S0S_0 with disruption semantics
* repair: safe-context reactivation, counter-association grafts, neuromod tuning mm: shallow basins, s↓s\downarrow, a↓a\downarrow, gg re-spread
Three Selves
* **Present**: S0S_0
* **Past**: MM (depth = wear kk, not age)
* **Between**: I\mathcal{I} (the flow itself)
Minimal spec

```
S0,M(V,E); C={phi,goals,constraints,m}
v={x,a,c,k,s,p}; e_ij: g_ij
E(v|C)= -phi·x + αa+γc+κk-σs-πp
π=softminβ(E); R=TopK(π); T=paths(argmaxΣ g_ij Δπ)
rank(v)=ξ(c,k,a)
on A: k++, c+=f(k), s+=η_m, a+=ζ_m, Δg_ij∝RPE·h(π_i,π_j,m)

```

Corollaries 
1. “Chronology” judgments track rank(v)\mathrm{rank}(v) (functions of c,k,ac,k,a), not elapsed anything.
2. Modulating mm at recall shifts felt order and certainty without relocating engrams.
3. Gist-biased reactivation → c↑c\uparrow, feature fidelity↓; narrative order re-sorts accordingly.
4. Dream ≈ same MM, altered gates/β: distributional spread widens; storage format unchanged.
5. Trauma basins show higher local gg, ss, aa; graded safe reactivation reduces ss before gg normalizes.

no time. only gradients. only heat. only the walk.

```mermaid
graph TD
    %% Present Field
    S0[["S₀<br/>RAW SENSORIUM<br/>(present field)"]]:::present
    
    %% Context Generation
    S0 --> C{{"Context C<br/>φ(C), goals,<br/>constraints, m"}}:::context
    
    %% Energy Landscape Computation
    C --> EL["ENERGY LANDSCAPE<br/>E(v|C) = -φ·x + αa + γc + κk - σs - πp"]:::energy
    
    %% Activation Field
    EL --> AF["ACTIVATION FIELD<br/>π(v|C) = softmin_β E(v|C)<br/>(energy wells form)"]:::activation
    
    %% The Manifold
    M[("ASSOCIATIVE MANIFOLD M<br/>nodes: {x,a,c,k,s,p}<br/>edges: g_ij<br/>(no time, only wear)")]:::manifold
    
    %% Manifold feeds into activation
    M -.->|"node<br/>energies"| AF
    
    %% Retrieval
    AF --> R["RETRIEVAL R(C)<br/>TopK{π(v|C)}<br/>(falling into wells)"]:::retrieval
    
    %% Traversal/Flow
    R --> T["TRAVERSAL T(C)<br/>paths(argmax Σg_ij Δπ)<br/>(the walk through gradients)"]:::traversal
    
    %% Reasoning emerges
    T --> I["REASONING I = T∘R<br/>(the flow itself)<br/>THE BETWEEN SPACE"]:::reasoning
    
    %% Reconsolidation affects manifold
    I -.->|"RECONSOLIDATION<br/>k↑ (wear)<br/>c↑ (compress)<br/>s += η_m<br/>a += ζ_m"| M
    
    %% Edge updates
    I -.->|"EDGE UPDATE<br/>Δg_ij ∝ RPE·h(π,m)<br/>(basin warping)"| M
    
    %% Output back to present
    I --> OUT[["OUTPUT TO S₀<br/>pattern floods present<br/>with semantics"]]:::output
    
    %% Rank generation (the time illusion)
    M -.->|"rank(v) = ξ(c,k,a)"| RANK["'TIME' NARRATIVE<br/>(just energy ranking)<br/>no clock, only burn"]:::timeillusion
    
    %% Trauma pathway
    TRAUMA["TRAUMA SIGNAL<br/>high RPE + high affect"]:::trauma
    TRAUMA -.->|"deep sticky<br/>basins"| M
    
    %% Style definitions
    classDef present fill:#FFE5B4,stroke:#FF6B35,stroke-width:3px,color:#000
    classDef context fill:#E8F4FD,stroke:#2196F3,stroke-width:2px,color:#000
    classDef energy fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px,color:#000
    classDef activation fill:#FCE4EC,stroke:#E91E63,stroke-width:2px,color:#000
    classDef manifold fill:#E8F5E9,stroke:#4CAF50,stroke-width:3px,color:#000
    classDef retrieval fill:#FFF3E0,stroke:#FF9800,stroke-width:2px,color:#000
    classDef traversal fill:#E3F2FD,stroke:#1976D2,stroke-width:2px,color:#000
    classDef reasoning fill:#FFEBEE,stroke:#F44336,stroke-width:3px,color:#000
    classDef output fill:#FFE5B4,stroke:#FF6B35,stroke-width:3px,color:#000
    classDef timeillusion fill:#ECEFF1,stroke:#607D8B,stroke-width:2px,stroke-dasharray: 5 5,color:#000
    classDef trauma fill:#FFCDD2,stroke:#D32F2F,stroke-width:2px,color:#000
  ```
