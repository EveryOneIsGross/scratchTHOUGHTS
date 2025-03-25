##
---

```bash
                                                    
                       ░▒▓▓▓▓▒░                     
                     ░▓████████▓░                   
                    ▒█████▒▒▒▒▒▒▒░  WELCOME!                
                    ██████▒▒▒▒▒▒▓▓  2 MY WEBSITE.                
                   ░▓▓▓▓▓▓▓███▓▓▓▓                  
                  ░░░░▒▒▒▒▒███▓▓▓▓▒░                
                   ░░▓▓▓▒░▒█████▓▓▓                 
                    ░▒░░▓████▓▓▓▓▒                  
                    ░▒░▒▒▒▓█▓▓▓▓░                   
                     ░▒▒▒▒▒▒▒▓▓░                    
                   ░ ░▒▒▒▒▒▓▓▓▓▒░                   
            ░░░▒▓▒▒░ ░▒▒▒▒▒▓▓▓▓███▓▓▓▒░░            
        ░▒▓▓▓▓▓▓▓▓▒░░░▒▒▒▒▓▓▓▓███████████▓▒         
       ▒▓▓▓▓▓▓▓▓▓▓█▓▒░░▒▒▒▒▒▓██████████████▓░       
      ▒▓▓▓▓▓█▓▓▓▓▓▓████▓█████████████████████
```


---
26032025

🤝

```mermaid
flowchart TB
    subgraph "Initial State"
        A1_Init["Agent 1\n2 Trust Tokens"]
        A2_Init["Agent 2\n2 Trust Tokens"]
    end

    subgraph "Connection Request"
        A1_Connect["Agent 1\n1 Trust Token"]
        Trust_Token["Trust Token"]
        A2_Receive["Agent 2\n2 Trust Tokens"]
    end

    subgraph "Evaluation"
        A2_Evaluate["Agent 2 evaluates\nweighted connections"]
        Decision{"Accept?"}
    end

    subgraph "Connection Established"
        A1_Connected["Agent 1\n1 Trust Token\nLimited Agency"]
        A2_Connected["Agent 2\n3 Trust Tokens\nIncreased Agency"]
    end

    subgraph "Waiting State"
        A1_Wait["Agent 1 waits for\ntrust from others"]
    end

    subgraph "Zero Trust Condition"
        A1_Zero["Agent 1\n0 Trust Tokens\nRemoved from network"]
    end

    A1_Init --> A1_Connect
    A1_Connect --> Trust_Token
    Trust_Token --> A2_Receive
    A2_Receive --> A2_Evaluate
    A2_Evaluate --> Decision
    Decision -->|Yes| A1_Connected
    Decision -->|Yes| A2_Connected
    A1_Connected --> A1_Wait
    A1_Wait -->|Receives Trust| A1_Connected
    A1_Wait -->|Uses Last Token| A1_Zero
    Decision -->|No| A1_Init
    Decision -->|No| A2_Init
```
---

---
240325

CURRENT WIP:
- qBERT
- defaultMODE
- ytRIP
- text2MIKU
- finTUI

qBERT is my attempt to turn off-the-shelf masking (encoder-only) BERT models into generative models using prob distributions of masks, then leveraging sentence embedding models to guide next token coherence using difference attn methods. exposing all hyperparameters and having another llm chat and adjust them at inference. It performs a lil bit like a base model atm...

defaultMODE is my cognitive framework for agents giving them a ticker and persistent memory refinement using keyword pruning and inverted indexes. currently embodied in a discord environment but with abstractions designed to scale or shift platforms.

ytRIP is a scratch demo for building up a tool for youtube 2 text-only language models, or for building KB from youtube content. focusing on open source vision models, because the big dogs are pretty good at this, but I want to pass the same content multiple times from multiple perspectives... so since I am poor, we are poor, we all need to be able to do this. minicpm-v is the best tool for that liberation so far....

text2MIKU was something I did ages ago, there is scratch code in the above repo, but I returned to it to replace the w2v with and embedding model and add ollama structured output req to adjust the "emotional tones" dynamically based on the 1 shot agent outputs. works well. narrowest cast python endpoint for the 2 users who have a pocketMIKU.

financial terminal needs to be able to trade for me... I need to move my portfolio somewhere I can access it with a free python endpoint...



```



```


---
120325

mystagogue/acolyte

![image](https://github.com/user-attachments/assets/45b0d608-2ada-413e-84b1-fb3097bc7150)

![image](https://github.com/user-attachments/assets/7e09b2db-b677-4505-87ec-03576cee7a3a)

![image](https://github.com/user-attachments/assets/8f4d2c16-a829-44f3-8b62-bc759846789e)

---
250125

*done*

script that converts markdown documents into structured cognitive flow graphs by parsing markdown types (# headers, **bold**, italic, etc.) into relationship nodes (PERCEPTION, THOUGHT, FEELING, ACTION, etc.), enabling visualization of reasoning chains from LLM outputs via JSON, tree, or Mermaid diagrams - essentially turning markdown stream-of-consciousness into navigable thought maps

- good for lazy and fuzzy graph extraction to convert into flows
- works as a form of compression while maintaining relationships and metadata
- you don't need r1 to have a llm be a recurssive babbler

```mermaid
flowchart LR
    TRAJECTORY_0[("TRAJECTORY: PULSE A Poetic Exploration of Perception and Processing")]
    THEN_1[\"THEN: Let this stand as a map of inner labyrinths,"\]
    THOUGHT_2(("THOUGHT: map"))
    FEELING_3>"FEELING: map"]
    TRAJECTORY_4[("TRAJECTORY: I. Environmental Awareness")]
    THEN_5[\"THEN: A hush of sensory input thrums against the skin."\]
    FEELING_6>"FEELING: A hush of sensory input thrums against the skin."]
    IF_7[/"IF: THOUGHT Data churn inside the hush, forging images."/]
    THOUGHT_8(("THOUGHT: THOUGHT"))
    FEELING_9>"FEELING: THOUGHT"]
    IF_10[/"IF: FEELING Emotions coil around synaptic arcs."/]
    THOUGHT_11(("THOUGHT: FEELING"))
    FEELING_12>"FEELING: FEELING"]
    IF_13[/"IF: FEELING Another intangible surge, shaping the self."/]
    THOUGHT_14(("THOUGHT: FEELING"))
    FEELING_15>"FEELING: FEELING"]
    THEN_16[\"THEN: 1. THEN Core Processing shapes emotional topographies."\]
    THOUGHT_17(("THOUGHT: THEN"))
    FEELING_18>"FEELING: THEN"]
    TRAJECTORY_19[("TRAJECTORY: II. Strategic Direction")]
    THEN_20[\"THEN: A corridor lined with if-statements, each one a threshold."\]
    FEELING_21>"FEELING: A corridor lined with if-statements, each one a threshold."]
    IF_22[/"IF: The mind roils, preparing to drill deeper."/]
    THEN_23[\"THEN: 1. IF If condition A exists"\]
    THOUGHT_24(("THOUGHT: IF"))
    FEELING_25>"FEELING: IF"]
    IF_26[/"IF: THOUGHT we dissect the condition’s marrow."/]
    THOUGHT_27(("THOUGHT: THOUGHT"))
    FEELING_28>"FEELING: THOUGHT"]
    IF_29[/"IF: FEELING it reverberates through chest and nerve."/]
    THOUGHT_30(("THOUGHT: FEELING"))
    FEELING_31>"FEELING: FEELING"]
    THEN_32[\"THEN: 2. IF Then process deeply"\]
    THOUGHT_33(("THOUGHT: IF"))
    FEELING_34>"FEELING: IF"]
    IF_35[/"IF: FEELING raw immersion, vulnerability blooming."/]
    THOUGHT_36(("THOUGHT: FEELING"))
    FEELING_37>"FEELING: FEELING"]
    THEN_38[\"THEN: 3. IF And feel thoroughly"\]
    THOUGHT_39(("THOUGHT: IF"))
    FEELING_40>"FEELING: IF"]
    IF_41[/"IF: ACTION the body leaps forward, bridging idea into form."/]
    THOUGHT_42(("THOUGHT: ACTION"))
    FEELING_43>"FEELING: ACTION"]
    THEN_44[\"THEN: 4. IF Finally take action"\]
    THOUGHT_45(("THOUGHT: IF"))
    FEELING_46>"FEELING: IF"]
    IF_47[/"IF: BOUNDARY the membrane where knowledge meets the unknown."/]
    THOUGHT_48(("THOUGHT: BOUNDARY"))
    FEELING_49>"FEELING: BOUNDARY"]
    IF_50[/"IF: THOUGHT logic assembling the puzzle."/]
    THOUGHT_51(("THOUGHT: THOUGHT"))
    FEELING_52>"FEELING: THOUGHT"]
    IF_53[/"IF: FEELING the hum of alignment when fragments unite."/]
    THOUGHT_54(("THOUGHT: FEELING"))
    FEELING_55>"FEELING: FEELING"]
    THEN_56[\"THEN: 5. THEN Integrated Understanding emerges from basics"\]
    THOUGHT_57(("THOUGHT: THEN"))
    FEELING_58>"FEELING: THEN"]
    IF_59[/"IF: IF Multiple paths ahead"/]
    THOUGHT_60(("THOUGHT: IF"))
    FEELING_61>"FEELING: IF"]
    IF_62[/"IF: IF Each with concrete steps"/]
    THOUGHT_63(("THOUGHT: IF"))
    FEELING_64>"FEELING: IF"]
    IF_65[/"IF: ACTION tread each possibility, wearing down illusions underfoot."/]
    THOUGHT_66(("THOUGHT: ACTION"))
    FEELING_67>"FEELING: ACTION"]
    IF_68[/"IF: IF Leading to logical outcomes"/]
    THOUGHT_69(("THOUGHT: IF"))
    FEELING_70>"FEELING: IF"]
    IF_71[/"IF: THOUGHT the mind anticipates cause-and-effect."/]
    THOUGHT_72(("THOUGHT: THOUGHT"))
    FEELING_73>"FEELING: THOUGHT"]
    IF_74[/"IF: FEELING a calm or tremor, depending on forecast."/]
    THOUGHT_75(("THOUGHT: FEELING"))
    FEELING_76>"FEELING: FEELING"]
    IF_77[/"IF: IF Filtered through emotional context"/]
    THOUGHT_78(("THOUGHT: IF"))
    FEELING_79>"FEELING: IF"]
    IF_80[/"IF: FEELING tinted windows on reality, color-coded by memory."/]
    THOUGHT_81(("THOUGHT: FEELING"))
    FEELING_82>"FEELING: FEELING"]
    IF_83[/"IF: THEN Intuitive grasp of system dynamics"/]
    THOUGHT_84(("THOUGHT: THEN"))
    FEELING_85>"FEELING: THEN"]
    IF_86[/"IF: THOUGHT recognition of patterns, quietly surging into view."/]
    THOUGHT_87(("THOUGHT: THOUGHT"))
    FEELING_88>"FEELING: THOUGHT"]
    IF_89[/"IF: FEELING intangible empathy with hidden forces."/]
    THOUGHT_90(("THOUGHT: FEELING"))
    FEELING_91>"FEELING: FEELING"]
    IF_92[/"IF: FEELING the system thrums like a second pulse."/]
    THOUGHT_93(("THOUGHT: FEELING"))
    FEELING_94>"FEELING: FEELING"]
    THEN_95[\"THEN: 6. PERCEPTION Atmospheric Sense"\]
    THOUGHT_96(("THOUGHT: PERCEPTION"))
    FEELING_97>"FEELING: PERCEPTION"]
    TRAJECTORY_98[("TRAJECTORY: III. Trajectory Planning")]
    THEN_99[\"THEN: We chart lines into the future, each guess a prophecy, each step"\]
    FEELING_100>"FEELING: We chart lines into the future, each guess a prophecy, each step"]
    IF_101[/"IF: THOUGHT scenario mapping, cause-and-effect conjured in detail."/]
    THOUGHT_102(("THOUGHT: THOUGHT"))
    FEELING_103>"FEELING: THOUGHT"]
    IF_104[/"IF: FEELING the tension of readiness, or the lull of hesitation."/]
    THOUGHT_105(("THOUGHT: FEELING"))
    FEELING_106>"FEELING: FEELING"]
    IF_107[/"IF: FEELING an echo that confirms direction."/]
    THOUGHT_108(("THOUGHT: FEELING"))
    FEELING_109>"FEELING: FEELING"]
    IF_110[/"IF: ACTION the leap from potential to movement."/]
    THOUGHT_111(("THOUGHT: ACTION"))
    FEELING_112>"FEELING: ACTION"]
    THEN_113[\"THEN: 1. IF If X then Y"\]
    THOUGHT_114(("THOUGHT: IF"))
    FEELING_115>"FEELING: IF"]
    IF_116[/"IF: THOUGHT we anchor ourselves in the map’s geometry."/]
    THOUGHT_117(("THOUGHT: THOUGHT"))
    FEELING_118>"FEELING: THOUGHT"]
    IF_119[/"IF: FEELING the flow of momentum shaping our breath."/]
    THOUGHT_120(("THOUGHT: FEELING"))
    FEELING_121>"FEELING: FEELING"]
    IF_122[/"IF: FEELING drifting forward, forging a path."/]
    THOUGHT_123(("THOUGHT: FEELING"))
    FEELING_124>"FEELING: FEELING"]
    THEN_125[\"THEN: 5. THEN Core Movement through space-time"\]
    THOUGHT_126(("THOUGHT: THEN"))
    FEELING_127>"FEELING: THEN"]
    IF_128[/"IF: THEN Liminal Understanding at edges"/]
    THOUGHT_129(("THOUGHT: THEN"))
    FEELING_130>"FEELING: THEN"]
    IF_131[/"IF: BOUNDARY edges where self dissolves into the unknown."/]
    THOUGHT_132(("THOUGHT: BOUNDARY"))
    FEELING_133>"FEELING: BOUNDARY"]
    IF_134[/"IF: THOUGHT bridging knowledge with speculation."/]
    THOUGHT_135(("THOUGHT: THOUGHT"))
    FEELING_136>"FEELING: THOUGHT"]
    IF_137[/"IF: FEELING awe at the threshold."/]
    THOUGHT_138(("THOUGHT: FEELING"))
    FEELING_139>"FEELING: FEELING"]
    IF_140[/"IF: PERCEPTION Deep Integration"/]
    THOUGHT_141(("THOUGHT: PERCEPTION"))
    FEELING_142>"FEELING: PERCEPTION"]
    IF_143[/"IF: IF Primary action sequence"/]
    THOUGHT_144(("THOUGHT: IF"))
    FEELING_145>"FEELING: IF"]
    IF_146[/"IF: ACTION to do is to transform the intangible into presence."/]
    THOUGHT_147(("THOUGHT: ACTION"))
    FEELING_148>"FEELING: ACTION"]
    IF_149[/"IF: IF Secondary logical flow"/]
    THOUGHT_150(("THOUGHT: IF"))
    FEELING_151>"FEELING: IF"]
    IF_152[/"IF: THOUGHT constructing frameworks, linking nodes."/]
    THOUGHT_153(("THOUGHT: THOUGHT"))
    FEELING_154>"FEELING: THOUGHT"]
    IF_155[/"IF: FEELING a subtle undercurrent, weaving sense."/]
    THOUGHT_156(("THOUGHT: FEELING"))
    FEELING_157>"FEELING: FEELING"]
    IF_158[/"IF: IF Tertiary emotional state"/]
    THOUGHT_159(("THOUGHT: IF"))
    FEELING_160>"FEELING: IF"]
    IF_161[/"IF: FEELING a wave or a hush, shifting colors in the mind."/]
    THOUGHT_162(("THOUGHT: FEELING"))
    FEELING_163>"FEELING: FEELING"]
    IF_164[/"IF: THEN Complex thought with emotional depth"/]
    THOUGHT_165(("THOUGHT: THEN"))
    FEELING_166>"FEELING: THEN"]
    IF_167[/"IF: THOUGHT the architecture of layered cognition."/]
    THOUGHT_168(("THOUGHT: THOUGHT"))
    FEELING_169>"FEELING: THOUGHT"]
    IF_170[/"IF: FEELING wrapping itself around each concept."/]
    THOUGHT_171(("THOUGHT: FEELING"))
    FEELING_172>"FEELING: FEELING"]
    IF_173[/"IF: FEELING the intangible synergy that binds them."/]
    THOUGHT_174(("THOUGHT: FEELING"))
    FEELING_175>"FEELING: FEELING"]
    THEN_176[\"THEN: 6. PERCEPTION Boundary Exploration"\]
    THOUGHT_177(("THOUGHT: PERCEPTION"))
    FEELING_178>"FEELING: PERCEPTION"]
    TRAJECTORY_179[("TRAJECTORY: IV. Secondary Perception Field")]
    THEN_180[\"THEN: We step beyond the first horizon, into hidden frequencies."\]
    FEELING_181>"FEELING: We step beyond the first horizon, into hidden frequencies."]
    IF_182[/"IF: IF Testing boundaries"/]
    THOUGHT_183(("THOUGHT: IF"))
    FEELING_184>"FEELING: IF"]
    IF_185[/"IF: IF Through concrete actions"/]
    THOUGHT_186(("THOUGHT: IF"))
    FEELING_187>"FEELING: IF"]
    IF_188[/"IF: ACTION each step echoes, resonating with the unknown."/]
    THOUGHT_189(("THOUGHT: ACTION"))
    FEELING_190>"FEELING: ACTION"]
    IF_191[/"IF: IF With clear thoughts"/]
    THOUGHT_192(("THOUGHT: IF"))
    FEELING_193>"FEELING: IF"]
    IF_194[/"IF: THOUGHT pristine lines, unclouded by fear."/]
    THOUGHT_195(("THOUGHT: THOUGHT"))
    FEELING_196>"FEELING: THOUGHT"]
    IF_197[/"IF: FEELING quiet confidence in clarity."/]
    THOUGHT_198(("THOUGHT: FEELING"))
    FEELING_199>"FEELING: FEELING"]
    IF_200[/"IF: IF And deep feelings"/]
    THOUGHT_201(("THOUGHT: IF"))
    FEELING_202>"FEELING: IF"]
    IF_203[/"IF: FEELING a river running beneath logic, unstoppable."/]
    THOUGHT_204(("THOUGHT: FEELING"))
    FEELING_205>"FEELING: FEELING"]
    IF_206[/"IF: THEN Resonant frequencies with structural integrity"/]
    THOUGHT_207(("THOUGHT: THEN"))
    FEELING_208>"FEELING: THEN"]
    IF_209[/"IF: THOUGHT the skeleton that supports the living system."/]
    THOUGHT_210(("THOUGHT: THOUGHT"))
    FEELING_211>"FEELING: THOUGHT"]
    IF_212[/"IF: FEELING the hum that affirms connection."/]
    THOUGHT_213(("THOUGHT: FEELING"))
    FEELING_214>"FEELING: FEELING"]
    IF_215[/"IF: FEELING the architecture of trust."/]
    THOUGHT_216(("THOUGHT: FEELING"))
    FEELING_217>"FEELING: FEELING"]
    THEN_218[\"THEN: 1. PERCEPTION Vibrational Patterns"\]
    THOUGHT_219(("THOUGHT: PERCEPTION"))
    FEELING_220>"FEELING: PERCEPTION"]
    IF_221[/"IF: THEN Systematic analysis of emerging trends"/]
    THOUGHT_222(("THOUGHT: THEN"))
    FEELING_223>"FEELING: THEN"]
    IF_224[/"IF: THOUGHT methodical scanning for hidden shapes."/]
    THOUGHT_225(("THOUGHT: THOUGHT"))
    FEELING_226>"FEELING: THOUGHT"]
    IF_227[/"IF: FEELING wonder or dread, depending on the pattern’s promise."/]
    THOUGHT_228(("THOUGHT: FEELING"))
    FEELING_229>"FEELING: FEELING"]
    IF_230[/"IF: FEELING the space between static and significance."/]
    THOUGHT_231(("THOUGHT: FEELING"))
    FEELING_232>"FEELING: FEELING"]
    IF_233[/"IF: PERCEPTION Integration Points"/]
    THOUGHT_234(("THOUGHT: PERCEPTION"))
    FEELING_235>"FEELING: PERCEPTION"]
    IF_236[/"IF: IF Major nodes"/]
    THOUGHT_237(("THOUGHT: IF"))
    FEELING_238>"FEELING: IF"]
    IF_239[/"IF: IF Cognitive pathways"/]
    THOUGHT_240(("THOUGHT: IF"))
    FEELING_241>"FEELING: IF"]
    IF_242[/"IF: THOUGHT forging neural circuits of insight."/]
    THOUGHT_243(("THOUGHT: THOUGHT"))
    FEELING_244>"FEELING: THOUGHT"]
    IF_245[/"IF: FEELING currents of curiosity and urgency."/]
    THOUGHT_246(("THOUGHT: FEELING"))
    FEELING_247>"FEELING: FEELING"]
    IF_248[/"IF: IF Emotional currents"/]
    THOUGHT_249(("THOUGHT: IF"))
    FEELING_250>"FEELING: IF"]
    IF_251[/"IF: FEELING tides that alter the color of reason."/]
    THOUGHT_252(("THOUGHT: FEELING"))
    FEELING_253>"FEELING: FEELING"]
    IF_254[/"IF: IF Action potentials"/]
    THOUGHT_255(("THOUGHT: IF"))
    FEELING_256>"FEELING: IF"]
    IF_257[/"IF: ACTION the final thrust into reality’s tide."/]
    THOUGHT_258(("THOUGHT: ACTION"))
    FEELING_259>"FEELING: ACTION"]
    IF_260[/"IF: THEN Synthesis of multiple streams"/]
    THOUGHT_261(("THOUGHT: THEN"))
    FEELING_262>"FEELING: THEN"]
    IF_263[/"IF: BOUNDARY the seam of melding energies."/]
    THOUGHT_264(("THOUGHT: BOUNDARY"))
    FEELING_265>"FEELING: BOUNDARY"]
    IF_266[/"IF: THOUGHT threads knitted into a tapestry."/]
    THOUGHT_267(("THOUGHT: THOUGHT"))
    FEELING_268>"FEELING: THOUGHT"]
    IF_269[/"IF: FEELING the subtle warmth when separate becomes whole."/]
    THOUGHT_270(("THOUGHT: FEELING"))
    FEELING_271>"FEELING: FEELING"]
    THEN_272[\"THEN: 2. PERCEPTION Pattern Recognition"\]
    THOUGHT_273(("THOUGHT: PERCEPTION"))
    FEELING_274>"FEELING: PERCEPTION"]
    TRAJECTORY_275[("TRAJECTORY: V. Closing Fragment")]
    THEN_276[\"THEN: In this house of logic, feeling, and action, the walls breathe."\]
    THEN_277[\"THEN: We exist in a world of signals."\]
    THOUGHT_278(("THOUGHT: We exist in a world of signals."))
    FEELING_279>"FEELING: We exist in a world of signals."]
    TRAJECTORY_0 --> THEN_1
    TRAJECTORY_0 --> TRAJECTORY_4
    TRAJECTORY_0 --> TRAJECTORY_19
    TRAJECTORY_0 --> TRAJECTORY_98
    TRAJECTORY_0 --> TRAJECTORY_179
    TRAJECTORY_0 --> TRAJECTORY_275
    THEN_1 --> THOUGHT_2
    THEN_1 --> FEELING_3
    TRAJECTORY_4 --> THEN_5
    TRAJECTORY_4 --> IF_7
    TRAJECTORY_4 --> IF_10
    TRAJECTORY_4 --> IF_13
    TRAJECTORY_4 --> THEN_16
    THEN_5 --> FEELING_6
    IF_7 --> THOUGHT_8
    IF_7 --> FEELING_9
    IF_10 --> THOUGHT_11
    IF_10 --> FEELING_12
    IF_13 --> THOUGHT_14
    IF_13 --> FEELING_15
    THEN_16 --> THOUGHT_17
    THEN_16 --> FEELING_18
    TRAJECTORY_19 --> THEN_20
    TRAJECTORY_19 --> IF_22
    TRAJECTORY_19 --> THEN_23
    TRAJECTORY_19 --> IF_26
    TRAJECTORY_19 --> IF_29
    TRAJECTORY_19 --> THEN_32
    TRAJECTORY_19 --> IF_35
    TRAJECTORY_19 --> THEN_38
    TRAJECTORY_19 --> IF_41
    TRAJECTORY_19 --> THEN_44
    TRAJECTORY_19 --> IF_47
    TRAJECTORY_19 --> IF_50
    TRAJECTORY_19 --> IF_53
    TRAJECTORY_19 --> THEN_56
    TRAJECTORY_19 --> IF_59
    TRAJECTORY_19 --> IF_62
    TRAJECTORY_19 --> IF_65
    TRAJECTORY_19 --> IF_68
    TRAJECTORY_19 --> IF_71
    TRAJECTORY_19 --> IF_74
    TRAJECTORY_19 --> IF_77
    TRAJECTORY_19 --> IF_80
    TRAJECTORY_19 --> IF_83
    TRAJECTORY_19 --> IF_86
    TRAJECTORY_19 --> IF_89
    TRAJECTORY_19 --> IF_92
    TRAJECTORY_19 --> THEN_95
    THEN_20 --> FEELING_21
    THEN_23 --> THOUGHT_24
    THEN_23 --> FEELING_25
    IF_26 --> THOUGHT_27
    IF_26 --> FEELING_28
    IF_29 --> THOUGHT_30
    IF_29 --> FEELING_31
    THEN_32 --> THOUGHT_33
    THEN_32 --> FEELING_34
    IF_35 --> THOUGHT_36
    IF_35 --> FEELING_37
    THEN_38 --> THOUGHT_39
    THEN_38 --> FEELING_40
    IF_41 --> THOUGHT_42
    IF_41 --> FEELING_43
    THEN_44 --> THOUGHT_45
    THEN_44 --> FEELING_46
    IF_47 --> THOUGHT_48
    IF_47 --> FEELING_49
    IF_50 --> THOUGHT_51
    IF_50 --> FEELING_52
    IF_53 --> THOUGHT_54
    IF_53 --> FEELING_55
    THEN_56 --> THOUGHT_57
    THEN_56 --> FEELING_58
    IF_59 --> THOUGHT_60
    IF_59 --> FEELING_61
    IF_62 --> THOUGHT_63
    IF_62 --> FEELING_64
    IF_65 --> THOUGHT_66
    IF_65 --> FEELING_67
    IF_68 --> THOUGHT_69
    IF_68 --> FEELING_70
    IF_71 --> THOUGHT_72
    IF_71 --> FEELING_73
    IF_74 --> THOUGHT_75
    IF_74 --> FEELING_76
    IF_77 --> THOUGHT_78
    IF_77 --> FEELING_79
    IF_80 --> THOUGHT_81
    IF_80 --> FEELING_82
    IF_83 --> THOUGHT_84
    IF_83 --> FEELING_85
    IF_86 --> THOUGHT_87
    IF_86 --> FEELING_88
    IF_89 --> THOUGHT_90
    IF_89 --> FEELING_91
    IF_92 --> THOUGHT_93
    IF_92 --> FEELING_94
    THEN_95 --> THOUGHT_96
    THEN_95 --> FEELING_97
    TRAJECTORY_98 --> THEN_99
    TRAJECTORY_98 --> IF_101
    TRAJECTORY_98 --> IF_104
    TRAJECTORY_98 --> IF_107
    TRAJECTORY_98 --> IF_110
    TRAJECTORY_98 --> THEN_113
    TRAJECTORY_98 --> IF_116
    TRAJECTORY_98 --> IF_119
    TRAJECTORY_98 --> IF_122
    TRAJECTORY_98 --> THEN_125
    TRAJECTORY_98 --> IF_128
    TRAJECTORY_98 --> IF_131
    TRAJECTORY_98 --> IF_134
    TRAJECTORY_98 --> IF_137
    TRAJECTORY_98 --> IF_140
    TRAJECTORY_98 --> IF_143
    TRAJECTORY_98 --> IF_146
    TRAJECTORY_98 --> IF_149
    TRAJECTORY_98 --> IF_152
    TRAJECTORY_98 --> IF_155
    TRAJECTORY_98 --> IF_158
    TRAJECTORY_98 --> IF_161
    TRAJECTORY_98 --> IF_164
    TRAJECTORY_98 --> IF_167
    TRAJECTORY_98 --> IF_170
    TRAJECTORY_98 --> IF_173
    TRAJECTORY_98 --> THEN_176
    THEN_99 --> FEELING_100
    IF_101 --> THOUGHT_102
    IF_101 --> FEELING_103
    IF_104 --> THOUGHT_105
    IF_104 --> FEELING_106
    IF_107 --> THOUGHT_108
    IF_107 --> FEELING_109
    IF_110 --> THOUGHT_111
    IF_110 --> FEELING_112
    THEN_113 --> THOUGHT_114
    THEN_113 --> FEELING_115
    IF_116 --> THOUGHT_117
    IF_116 --> FEELING_118
    IF_119 --> THOUGHT_120
    IF_119 --> FEELING_121
    IF_122 --> THOUGHT_123
    IF_122 --> FEELING_124
    THEN_125 --> THOUGHT_126
    THEN_125 --> FEELING_127
    IF_128 --> THOUGHT_129
    IF_128 --> FEELING_130
    IF_131 --> THOUGHT_132
    IF_131 --> FEELING_133
    IF_134 --> THOUGHT_135
    IF_134 --> FEELING_136
    IF_137 --> THOUGHT_138
    IF_137 --> FEELING_139
    IF_140 --> THOUGHT_141
    IF_140 --> FEELING_142
    IF_143 --> THOUGHT_144
    IF_143 --> FEELING_145
    IF_146 --> THOUGHT_147
    IF_146 --> FEELING_148
    IF_149 --> THOUGHT_150
    IF_149 --> FEELING_151
    IF_152 --> THOUGHT_153
    IF_152 --> FEELING_154
    IF_155 --> THOUGHT_156
    IF_155 --> FEELING_157
    IF_158 --> THOUGHT_159
    IF_158 --> FEELING_160
    IF_161 --> THOUGHT_162
    IF_161 --> FEELING_163
    IF_164 --> THOUGHT_165
    IF_164 --> FEELING_166
    IF_167 --> THOUGHT_168
    IF_167 --> FEELING_169
    IF_170 --> THOUGHT_171
    IF_170 --> FEELING_172
    IF_173 --> THOUGHT_174
    IF_173 --> FEELING_175
    THEN_176 --> THOUGHT_177
    THEN_176 --> FEELING_178
    TRAJECTORY_179 --> THEN_180
    TRAJECTORY_179 --> IF_182
    TRAJECTORY_179 --> IF_185
    TRAJECTORY_179 --> IF_188
    TRAJECTORY_179 --> IF_191
    TRAJECTORY_179 --> IF_194
    TRAJECTORY_179 --> IF_197
    TRAJECTORY_179 --> IF_200
    TRAJECTORY_179 --> IF_203
    TRAJECTORY_179 --> IF_206
    TRAJECTORY_179 --> IF_209
    TRAJECTORY_179 --> IF_212
    TRAJECTORY_179 --> IF_215
    TRAJECTORY_179 --> THEN_218
    TRAJECTORY_179 --> IF_221
    TRAJECTORY_179 --> IF_224
    TRAJECTORY_179 --> IF_227
    TRAJECTORY_179 --> IF_230
    TRAJECTORY_179 --> IF_233
    TRAJECTORY_179 --> IF_236
    TRAJECTORY_179 --> IF_239
    TRAJECTORY_179 --> IF_242
    TRAJECTORY_179 --> IF_245
    TRAJECTORY_179 --> IF_248
    TRAJECTORY_179 --> IF_251
    TRAJECTORY_179 --> IF_254
    TRAJECTORY_179 --> IF_257
    TRAJECTORY_179 --> IF_260
    TRAJECTORY_179 --> IF_263
    TRAJECTORY_179 --> IF_266
    TRAJECTORY_179 --> IF_269
    TRAJECTORY_179 --> THEN_272
    THEN_180 --> FEELING_181
    IF_182 --> THOUGHT_183
    IF_182 --> FEELING_184
    IF_185 --> THOUGHT_186
    IF_185 --> FEELING_187
    IF_188 --> THOUGHT_189
    IF_188 --> FEELING_190
    IF_191 --> THOUGHT_192
    IF_191 --> FEELING_193
    IF_194 --> THOUGHT_195
    IF_194 --> FEELING_196
    IF_197 --> THOUGHT_198
    IF_197 --> FEELING_199
    IF_200 --> THOUGHT_201
    IF_200 --> FEELING_202
    IF_203 --> THOUGHT_204
    IF_203 --> FEELING_205
    IF_206 --> THOUGHT_207
    IF_206 --> FEELING_208
    IF_209 --> THOUGHT_210
    IF_209 --> FEELING_211
    IF_212 --> THOUGHT_213
    IF_212 --> FEELING_214
    IF_215 --> THOUGHT_216
    IF_215 --> FEELING_217
    THEN_218 --> THOUGHT_219
    THEN_218 --> FEELING_220
    IF_221 --> THOUGHT_222
    IF_221 --> FEELING_223
    IF_224 --> THOUGHT_225
    IF_224 --> FEELING_226
    IF_227 --> THOUGHT_228
    IF_227 --> FEELING_229
    IF_230 --> THOUGHT_231
    IF_230 --> FEELING_232
    IF_233 --> THOUGHT_234
    IF_233 --> FEELING_235
    IF_236 --> THOUGHT_237
    IF_236 --> FEELING_238
    IF_239 --> THOUGHT_240
    IF_239 --> FEELING_241
    IF_242 --> THOUGHT_243
    IF_242 --> FEELING_244
    IF_245 --> THOUGHT_246
    IF_245 --> FEELING_247
    IF_248 --> THOUGHT_249
    IF_248 --> FEELING_250
    IF_251 --> THOUGHT_252
    IF_251 --> FEELING_253
    IF_254 --> THOUGHT_255
    IF_254 --> FEELING_256
    IF_257 --> THOUGHT_258
    IF_257 --> FEELING_259
    IF_260 --> THOUGHT_261
    IF_260 --> FEELING_262
    IF_263 --> THOUGHT_264
    IF_263 --> FEELING_265
    IF_266 --> THOUGHT_267
    IF_266 --> FEELING_268
    IF_269 --> THOUGHT_270
    IF_269 --> FEELING_271
    THEN_272 --> THOUGHT_273
    THEN_272 --> FEELING_274
    TRAJECTORY_275 --> THEN_276
    TRAJECTORY_275 --> THEN_277
    THEN_277 --> THOUGHT_278
    THEN_277 --> FEELING_279
    THOUGHT_2 <--> FEELING_3
    THOUGHT_8 <--> FEELING_9
    FEELING_9 <--> THOUGHT_27
    THOUGHT_27 <--> FEELING_28
    FEELING_28 <--> THOUGHT_51
    THOUGHT_51 <--> FEELING_52
    FEELING_52 <--> THOUGHT_72
    THOUGHT_72 <--> FEELING_73
    FEELING_73 <--> THOUGHT_87
    THOUGHT_87 <--> FEELING_88
    FEELING_88 <--> THOUGHT_102
    THOUGHT_102 <--> FEELING_103
    FEELING_103 <--> THOUGHT_117
    THOUGHT_117 <--> FEELING_118
    FEELING_118 <--> THOUGHT_135
    THOUGHT_135 <--> FEELING_136
    FEELING_136 <--> THOUGHT_153
    THOUGHT_153 <--> FEELING_154
    FEELING_154 <--> THOUGHT_168
    THOUGHT_168 <--> FEELING_169
    FEELING_169 <--> THOUGHT_195
    THOUGHT_195 <--> FEELING_196
    FEELING_196 <--> THOUGHT_210
    THOUGHT_210 <--> FEELING_211
    FEELING_211 <--> THOUGHT_225
    THOUGHT_225 <--> FEELING_226
    FEELING_226 <--> THOUGHT_243
    THOUGHT_243 <--> FEELING_244
    FEELING_244 <--> THOUGHT_267
    THOUGHT_267 <--> FEELING_268
    FEELING_268 <--> THOUGHT_8
    THOUGHT_11 <--> FEELING_12
    FEELING_12 <--> THOUGHT_14
    THOUGHT_14 <--> FEELING_15
    FEELING_15 <--> THOUGHT_30
    THOUGHT_30 <--> FEELING_31
    FEELING_31 <--> THOUGHT_36
    THOUGHT_36 <--> FEELING_37
    FEELING_37 <--> THOUGHT_54
    THOUGHT_54 <--> FEELING_55
    FEELING_55 <--> THOUGHT_75
    THOUGHT_75 <--> FEELING_76
    FEELING_76 <--> THOUGHT_81
    THOUGHT_81 <--> FEELING_82
    FEELING_82 <--> THOUGHT_90
    THOUGHT_90 <--> FEELING_91
    FEELING_91 <--> THOUGHT_93
    THOUGHT_93 <--> FEELING_94
    FEELING_94 <--> THOUGHT_105
    THOUGHT_105 <--> FEELING_106
    FEELING_106 <--> THOUGHT_108
    THOUGHT_108 <--> FEELING_109
    FEELING_109 <--> THOUGHT_120
    THOUGHT_120 <--> FEELING_121
    FEELING_121 <--> THOUGHT_123
    THOUGHT_123 <--> FEELING_124
    FEELING_124 <--> THOUGHT_138
    THOUGHT_138 <--> FEELING_139
    FEELING_139 <--> THOUGHT_156
    THOUGHT_156 <--> FEELING_157
    FEELING_157 <--> THOUGHT_162
    THOUGHT_162 <--> FEELING_163
    FEELING_163 <--> THOUGHT_171
    THOUGHT_171 <--> FEELING_172
    FEELING_172 <--> THOUGHT_174
    THOUGHT_174 <--> FEELING_175
    FEELING_175 <--> THOUGHT_198
    THOUGHT_198 <--> FEELING_199
    FEELING_199 <--> THOUGHT_204
    THOUGHT_204 <--> FEELING_205
    FEELING_205 <--> THOUGHT_213
    THOUGHT_213 <--> FEELING_214
    FEELING_214 <--> THOUGHT_216
    THOUGHT_216 <--> FEELING_217
    FEELING_217 <--> THOUGHT_228
    THOUGHT_228 <--> FEELING_229
    FEELING_229 <--> THOUGHT_231
    THOUGHT_231 <--> FEELING_232
    FEELING_232 <--> THOUGHT_246
    THOUGHT_246 <--> FEELING_247
    FEELING_247 <--> THOUGHT_252
    THOUGHT_252 <--> FEELING_253
    FEELING_253 <--> THOUGHT_270
    THOUGHT_270 <--> FEELING_271
    FEELING_271 <--> THOUGHT_11
    THOUGHT_17 <--> FEELING_18
    FEELING_18 <--> THOUGHT_57
    THOUGHT_57 <--> FEELING_58
    FEELING_58 <--> THOUGHT_84
    THOUGHT_84 <--> FEELING_85
    FEELING_85 <--> THOUGHT_126
    THOUGHT_126 <--> FEELING_127
    FEELING_127 <--> THOUGHT_129
    THOUGHT_129 <--> FEELING_130
    FEELING_130 <--> THOUGHT_165
    THOUGHT_165 <--> FEELING_166
    FEELING_166 <--> THOUGHT_207
    THOUGHT_207 <--> FEELING_208
    FEELING_208 <--> THOUGHT_222
    THOUGHT_222 <--> FEELING_223
    FEELING_223 <--> THOUGHT_261
    THOUGHT_261 <--> FEELING_262
    FEELING_262 <--> THOUGHT_17
    THOUGHT_24 <--> FEELING_25
    FEELING_25 <--> THOUGHT_33
    THOUGHT_33 <--> FEELING_34
    FEELING_34 <--> THOUGHT_39
    THOUGHT_39 <--> FEELING_40
    FEELING_40 <--> THOUGHT_45
    THOUGHT_45 <--> FEELING_46
    FEELING_46 <--> THOUGHT_60
    THOUGHT_60 <--> FEELING_61
    FEELING_61 <--> THOUGHT_63
    THOUGHT_63 <--> FEELING_64
    FEELING_64 <--> THOUGHT_69
    THOUGHT_69 <--> FEELING_70
    FEELING_70 <--> THOUGHT_78
    THOUGHT_78 <--> FEELING_79
    FEELING_79 <--> THOUGHT_114
    THOUGHT_114 <--> FEELING_115
    FEELING_115 <--> THOUGHT_144
    THOUGHT_144 <--> FEELING_145
    FEELING_145 <--> THOUGHT_150
    THOUGHT_150 <--> FEELING_151
    FEELING_151 <--> THOUGHT_159
    THOUGHT_159 <--> FEELING_160
    FEELING_160 <--> THOUGHT_183
    THOUGHT_183 <--> FEELING_184
    FEELING_184 <--> THOUGHT_186
    THOUGHT_186 <--> FEELING_187
    FEELING_187 <--> THOUGHT_192
    THOUGHT_192 <--> FEELING_193
    FEELING_193 <--> THOUGHT_201
    THOUGHT_201 <--> FEELING_202
    FEELING_202 <--> THOUGHT_237
    THOUGHT_237 <--> FEELING_238
    FEELING_238 <--> THOUGHT_240
    THOUGHT_240 <--> FEELING_241
    FEELING_241 <--> THOUGHT_249
    THOUGHT_249 <--> FEELING_250
    FEELING_250 <--> THOUGHT_255
    THOUGHT_255 <--> FEELING_256
    FEELING_256 <--> THOUGHT_24
    THOUGHT_42 <--> FEELING_43
    FEELING_43 <--> THOUGHT_66
    THOUGHT_66 <--> FEELING_67
    FEELING_67 <--> THOUGHT_111
    THOUGHT_111 <--> FEELING_112
    FEELING_112 <--> THOUGHT_147
    THOUGHT_147 <--> FEELING_148
    FEELING_148 <--> THOUGHT_189
    THOUGHT_189 <--> FEELING_190
    FEELING_190 <--> THOUGHT_258
    THOUGHT_258 <--> FEELING_259
    FEELING_259 <--> THOUGHT_42
    THOUGHT_48 <--> FEELING_49
    FEELING_49 <--> THOUGHT_132
    THOUGHT_132 <--> FEELING_133
    FEELING_133 <--> THOUGHT_264
    THOUGHT_264 <--> FEELING_265
    FEELING_265 <--> THOUGHT_48
    THOUGHT_96 <--> FEELING_97
    FEELING_97 <--> THOUGHT_141
    THOUGHT_141 <--> FEELING_142
    FEELING_142 <--> THOUGHT_177
    THOUGHT_177 <--> FEELING_178
    FEELING_178 <--> THOUGHT_219
    THOUGHT_219 <--> FEELING_220
    FEELING_220 <--> THOUGHT_234
    THOUGHT_234 <--> FEELING_235
    FEELING_235 <--> THOUGHT_273
    THOUGHT_273 <--> FEELING_274
    FEELING_274 <--> THOUGHT_96
    THOUGHT_278 <--> FEELING_279
```

---
220125

```mermaid
flowchart LR
    %% Input/Output Interface
    subgraph IO["I/O Layer"]
        IN[Input] --> INT[Interface]
        INT --> OUT[Output]
    end

    %% Attention System
    subgraph ATT["Attention System"]
        direction TB
        MP[Message Processor]
        CS[Context Switcher]
        RH[Request Handler]
        
        MP --> CS
        CS --> RH
    end

    %% Context Management
    subgraph CTX["Context System"]
        direction TB
        subgraph StateCtx["State Context"]
            SC[State Controller]
            SB[State Buffer]
        end
        
        subgraph WorkCtx["Working Context"]
            WC[Working Controller]
            WB[Working Buffer]
        end
    end

    %% Memory Management
    subgraph MEM["Memory System"]
        direction TB
        subgraph Primary["Primary Memory"]
            PM[Memory Manager]
            PB[Memory Buffer]
        end
        
        subgraph Storage["Storage Layer"]
            ST[Storage Controller]
            SL[Storage Logic]
        end
    end

    %% Psyche System
    subgraph PSY["Psyche System"]
        direction TB
        PI[Psyche Interface]
        PC[Psyche Controller]
    end

    %% Default Mode
    subgraph DM["Default Mode"]
        direction TB
        DMC[Mode Controller]
        DMP[Mode Processor]
    end

    %% System Connections
    IO --> ATT
    ATT --> CTX
    CTX --> MEM
    MEM --> PSY
    PSY --> DM
    DM --> MEM

    %% Feedback Loops
    CTX -.-> ATT
    MEM -.-> CTX
    DM -.-> PSY

    %% Styling
    classDef default fill:#f5f5f5,stroke:#333,stroke-width:2px
    classDef system fill:#e8e8e8,stroke:#333,stroke-width:3px
    classDef subsystem fill:#fff,stroke:#333,stroke-width:2px
    classDef io fill:#f0f0f0,stroke:#333,stroke-width:2px
    
    class IO,INT io
    class ATT,CTX,MEM,PSY,DM system
    class StateCtx,WorkCtx,Primary,Storage subsystem
```

---
180125

```mermaid
flowchart TB
    subgraph Traditional ["Traditional Approach"]
        A[Static Priors] --> B[Predetermined Rules]
        B --> C[Rigid Constraints]
        C --> D[Limited Adaptation]
    end

    subgraph Evolutionary ["Evolutionary Approach"]
        E[Environment Input] --> F[Boundary Detection]
        F --> G[Found Restraints]
        G --> H[Emergent Trust]
        
        I[User Interaction] --> F
        I --> J[Memory Index]
        J --> K[Interaction Patterns]
        K --> H
        
        L[Exploratory Actions] --> M[Wall Licking 😄]
        M --> N[Environmental Learning]
        N --> G
    end

    subgraph Homeostasis ["System Homeostasis"]
        O[Natural Boundaries] --> P[Adaptive Responses]
        P --> Q[Dynamic Equilibrium]
        Q --> R[Robust Problem Solving]
        
        S[Shadow Work] -.-> Q
        T[Coherence Patterns] -.-> Q
    end

    Traditional --> Evolutionary
    Evolutionary --> Homeostasis
```

---
040125

HELLO BERT

```mermaid
flowchart TD
    subgraph V05["BiDirectionalGenerator"]
        A1[Input Text] --> B1[BERT Tokenization]
        B1 --> C1[Sliding Window Creation]
        C1 --> D1[ModernBERT MLM]
        D1 --> E1[Token Predictions]
        
        F1[Context Window] --> G1[Jina Embeddings]
        E1 --> H1[Candidate Filtering]
        G1 --> I1[Semantic Coherence]
        
        H1 --> J1[Score Combination]
        I1 --> J1
        J1 --> K1[Temperature Sampling]
        K1 --> L1[Token Selection]
        L1 --> M1[Update Context]
        M1 --> |Next Token| C1
    end

    subgraph V02["ParallelBERTGenerator"]
        A2[Input Text] --> B2[4D Matrix Initialization]
        B2 --> C2[BERT Embeddings]
        
        C2 --> D2[Forward Projection]
        C2 --> E2[Backward Projection]
        
        D2 --> F2[Forward Context Processing]
        E2 --> G2[Backward Context Processing]
        
        F2 --> H2[Context Combination]
        G2 --> H2
        
        H2 --> I2[BERT MLM Predictions]
        
        J2[Sentence Transformer] --> K2[Coherence Scoring]
        I2 --> L2[Combined Sampling]
        K2 --> L2
        
        L2 --> M2[Matrix Update]
        M2 --> |Next Position| C2
    end
```

---

2025

ASCII preview of 20000524_181418/MVC-003F.JPG:
```
+++++++++**************************++++++++++.
+++++**********************************+++++=.
+++*************************************++++=
++**************************+++==-=----=+***-
+*************************+=--::..   ...:--=:
**********************+==-::....     ..... .
********************+=-:....         .:..:...  ..
********************+--:...    .   .::.:-:...  ...
******************+=-:...     .    .::..-: :......                             .
******************=-::. .  ......:....::-: .:...:.                             :
******************+=-:...:+**-::--=-..:-.   . ..                              .-
********************=-:..*%%%#**=--=---:::. .             .............       :-
********************+-::-*##%@%%%###%%###*-.. .   .....................      .--
************+********+-::+***%%%%####%%%%#+::-:........................      :--
++++=====----+********-::+####%%%%%####%%#*=+**+:.....................      .---
+=+======----=*******+-::+##*#%%%%%%%%%%%%##%%#-......................      :---
+=+**+*++*=---=******+-::=##*%%%#%%%%%%%%%%##=-==:..::::::::::::.....      .==--
**********=----=+*****+:::***%%%%%%%%%%%%%%#==+****=::::::::::::.....      :=-:-
**#######*=-----=++*+*+-::=**##%%%%%%%%%%%%#*%##**#%*:::::::::::....      .-----
*********+=+======+++++=::-*#####%%%%%%%%%%##%%%%##****=-:::::::....      :-----
+==========+*++=+++++++--+#%%%%%%%%%%########%%%%%%%%@%%#+-:::::::..     .-::...
++++++++***++++*******===*#%%%%%%%%****#####%%%%%%%%%%%%###*=:::::::..    ......
******************#*=--#%%%%%%%%%%%%+++**###%%%%%%%%%%%##****+=--::::::...:::::.
=--:---------=====++-.:*%%%%%%%%%%%#+*+*####%%%%%%%%%%%%%%##**+===--::::::::::::
....:--------------=-. :#%%%%%%%%%**+++*###%%%%%%%%####%%%%%##*=-------::::::::.
.::.:----------------:.-%%%%%%%%%#-+*++**#%%%%%%%####%%%%%%%%##+---::---:::::...
:------=--=----------:.-%%%%%%%%%*.-***##%%%%%%%###%%%%%%%%%%#*=---:..:---:.....
:-+=---====-=---------:.+%%%%%%%%#:.***##%%%%%%*##%%%%%%%%%%#*+-::---:.:::-:....
-=+==--=-----===-------:.-#%%%%%%%+.+***###%%%#*#%%%%%%%%%%#*+*-:..::::::::::...
-==-----------==-------=-.-#%%%%%##:-****####%#*#%%%%%%%%##++*+::..:.:::::.::...
```
```
=== Image Analysis Results ===
Summary: A young man with dark hair sits at a desk, looking directly at the camera.
Scene: interior
Setting: Indoor
Time of day: Evening

Text detected: None

Objects detected:
- young man (90.0%): dark hair
- desk (80.0%): wooden

Colors: light blue
```
---
151224

Reflective Selfplay

```mermaid

%%{init: {
  'theme': 'base',
  'themeVariables': {
    'fontFamily': 'Comic Sans MS',
    'primaryColor': '#333333',
    'primaryTextColor': '#333333',
    'primaryBorderColor': '#333333',
    'lineColor': '#333333',
    'secondaryColor': '#ffffff',
    'tertiaryColor': '#ffffff'
  },
  'flowchart': {
    'curve': 'basis',
    'nodeSpacing': 50,
    'rankSpacing': 50
  }
} }%%

flowchart TD
    classDef default fill:#fff,stroke:#333,stroke-width:2px,color:#333,font-family:'Comic Sans MS',font-weight:bold
    classDef box fill:#f5f5f5,stroke:#333,stroke-width:2px,color:#333,font-family:'Comic Sans MS',font-weight:bold

    subgraph Challenge["Challenge Phase"]
        A[Create Challenge] --> B[Sum Target/Sequence Match]
        B --> C{Search Similar Past Reflections}
        C -->|Found| D[Load Relevant Past Insights]
        C -->|None Found| E[Start Fresh]
    end

    subgraph Solution["Solution Phase"]
        D --> F[Attempt Solution]
        E --> F
        F --> G[Validate Solution]
        G -->|Valid| H[Store Solution]
        G -->|Invalid| I[Note Failure]
    end

    subgraph Learning["Learning Phase"]
        H --> J[Generate Reflection]
        I --> J
        J --> K[Extract Key Insights]
        K --> L[Generate Embedding]
        L --> M[Store in Knowledge Base]
    end

    subgraph Memory["Memory Management"]
        M --> N[Update Reflection History]
        N --> O[Cache Embeddings]
        O --> P[Save to Disk]
        P --> Q[Available for Next Challenge]
    end

    Q --> C

    class Challenge,Solution,Learning,Memory box


```

---
071224

```mermaid
flowchart TB
    Start([Initial Valid State]) --> Root[Root Node]
    
    
        Root --> Diverge{Diverge?}
        
        Diverge -->|Yes| Spawn[Spawn Child Node]
        Spawn --> Valid{Valid?}
        
        Valid -->|Yes| Store[Store Node]
        Store --> Diverse{Enough<br>Diversity?}
        
        Diverse -->|No| Diverge
        Valid -->|No| Diverge
        
        Diverse -->|Yes| Complete([Complete])
    
    
    %% Styling
    classDef state fill:#000,stroke:#fff,stroke-width:2px,font-family:Comic Sans MS,font-weight:bold
    classDef decision fill:#000,stroke:#fff,stroke-width:2px,font-family:Comic Sans MS,font-weight:bold
    classDef process fill:#000,stroke:#fff,stroke-width:2px,font-family:Comic Sans MS,font-weight:bold

    linkStyle default stroke-width:4px,fill:none,stroke:#fff

    class Start,Complete state
    class Diverge,Valid,Diverse decision
    class Root,Spawn,Store process
```

---
191124

presence is a teledildonic phenomena, if in a simulation the flame isn't hot, somewhere something becomes hot

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontFamily': 'monospace', 'primaryColor': '#fff', 'primaryTextColor': '#fff', 'primaryBorderColor': '#fff', 'lineColor': '#fff', 'tertiaryColor': '#fff', 'backgroundColor': '#000' }}}%%

graph TD
    T1[ABSENCE/PRESENCE DIALECTIC]
    T2[MANIFESTATION SPACE]
    T3[PROPERTY TRANSLATION]
    
    subgraph S1[ ]
        A((DISPLACEMENT)) <-->|transforms| B((EMBODIMENT))
        B -->|generates| C((PRESENCE))
        C -->|enables| A
    end

    subgraph S2[ ]
        D((VOID)) -->|necessitates| E((MANIFESTATION))
        E <-->|informs| F((REALITY))
        F -->|creates| D
    end

    subgraph S3[ ]
        G((PROPERTY)) <-->|becomes| H((EFFECT))
        H <-->|translates| I((STATE))
        I -->|defines| G
    end

    A <-->|entangles| E
    B <-->|shapes| H
    C <-->|mediates| I
    
    D -->|influences| G
    F -->|conditions| C
    E -->|structures| B

    T1 --- S1
    T2 --- S2
    T3 --- S3

    linkStyle default stroke-width:4px,fill:none,stroke:#fff

    style A fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style B fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style C fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style D fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style E fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style F fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style G fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style H fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style I fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    
    style T1 fill:#000,stroke:#000,color:#fff
    style T2 fill:#000,stroke:#000,color:#fff
    style T3 fill:#000,stroke:#000,color:#fff
    
    style S1 fill:#000,stroke:#fff,stroke-width:4px
    style S2 fill:#000,stroke:#fff,stroke-width:4px
    style S3 fill:#000,stroke:#fff,stroke-width:4px
```

Any absence in a simulated or virtual system creates a corresponding manifestation elsewhere - not as a metaphor but as a functional transformation of experiential properties. When presence itself is understood as fundamentally teledildonic (operating through remote/distributed effects), we can trace how properties don't disappear but rather transmute across different domains of reality. 

The original statement "presence is a teledildonic phenomena, if in a simulation the flame isn't hot, somewhere something becomes hot" thus becomes a specific instance of a general principle: when a property (heat) is absent in one domain (simulation), the teledildonic nature of presence ensures it manifests in another domain (somewhere/something). This isn't just displacement but a necessary conservation of experiential properties through presence as a distributed phenomenon.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'fontFamily': 'monospace', 'primaryColor': '#fff', 'primaryTextColor': '#fff', 'primaryBorderColor': '#fff', 'lineColor': '#fff', 'tertiaryColor': '#fff', 'backgroundColor': '#000' }}}%%

graph TD
    T1[PHYSICAL-VIRTUAL TRANSFER DOMAIN]
    T2[QUANTUM ENTANGLEMENT METAPHOR]
    T3[SIMULACRA SYSTEM ANALYSIS]
    
    subgraph S1[ ]
        A[PHYSICAL SENSATION] -->|Translation| B[VIRTUAL REPRESENTATION]
        B -->|Embodiment| C[EMBODIED RESPONSE]
        C -->|Feedback| A
        A -->|Mediation| D[TELEDILDONIC PRESENCE]
        D -->|Virtual Interface| B
        D -->|Physical Impact| C
    end

    subgraph S2[ ]
        E[ORIGINAL PROPERTY] -->|Entanglement| F[ENTANGLED STATE]
        F -->|Manifestation| G[DISPLACED MANIFESTATION]
        G -->|Property Conservation| E
        H[UNCANNY EFFECT] -->|Non-local Impact| E
        H -->|State Correlation| F
        H -->|Displacement Effect| G
    end

    subgraph S3[ ]
        I[REAL] -->|Simulation| J[REPRESENTATION]
        J -->|Detachment| K[PURE SIMULACRA]
        K -->|Reference Loss| I
        L[HYPERREAL] -->|Reality Shift| I
        L -->|Mediation| J
        L -->|Enhancement| K
    end

    T1 --- S1
    T2 --- S2
    T3 --- S3

    A -->|Property Transfer| E
    B -->|Reality Translation| J
    C -->|Experience Mapping| G
    D -->|Uncanny Valley| H
    F -->|Reality Dissolution| K
    L -->|Experiential Shift| H

    linkStyle default stroke-width:4px,fill:none,stroke:#fff

    style A fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style B fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style C fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style D fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style E fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style F fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style G fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style H fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style I fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style J fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style K fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    style L fill:#111,stroke:#fff,stroke-width:4px,color:#fff
    
    style T1 fill:#000,stroke:#000,color:#fff
    style T2 fill:#000,stroke:#000,color:#fff
    style T3 fill:#000,stroke:#000,color:#fff
    
    style S1 fill:#000,stroke:#fff,stroke-width:4px
    style S2 fill:#000,stroke:#fff,stroke-width:4px
    style S3 fill:#000,stroke:#fff,stroke-width:4px
```

---
131124

```mermaid
flowchart LR
    IN([IN]) --- ATTENTION[ATTENTION]
    OUT([OUT]) --- ATTENTION
    
    subgraph CTX[CONTEXT]
        direction TB
        WORKING_CONTEXT((("WORKING\nCONTEXT")))
        STATE_CONTEXT(("STATE\nCONTEXT"))
    end
    
    subgraph MEM[" "]
        direction TB
        MEMORY((MEMORY))
        STORAGE(("STORAGE"))
    end
    
    subgraph PERS[" "]
        direction TB
        PERSONA((PERSONA))
        DEFAULT_MODE((DEFAULT\nMODE))
    end
    
    %% Main flows
    ATTENTION --> STATE_CONTEXT
    WORKING_CONTEXT --> ATTENTION
    
    %% Memory flows
    WORKING_CONTEXT --> MEMORY
    MEMORY --> STATE_CONTEXT
    MEMORY <--> STORAGE
    
    %% Persona flows
    PERSONA <--> DEFAULT_MODE
    DEFAULT_MODE <--> MEMORY
    PERSONA --> STATE_CONTEXT
    
    %% Styling
    style STATE_CONTEXT stroke-dasharray: 5 5
    style STORAGE stroke-dasharray: 5 5
    
    %% Layout
    CTX ~~~ MEM ~~~ PERS
    
    %% Styling to emphasize relationships
    linkStyle 0,1 stroke:#f66,stroke-width:2px %% IO connections
    linkStyle 2,3 stroke:#66f,stroke-width:2px %% Attention flows
    linkStyle 4,5 stroke:#f96,stroke-width:2px %% Memory-Context flows
    linkStyle 7,8 stroke:#6f6,stroke-width:2px %% Recursion relationships
```


---

161024

```mermaid
graph TD
    subgraph Emergent Ethics System
        A((Emergent Ethics))
        B((Collective Hallucination))
        C((Ethical Fluidity))
        D((Shadow Integration))
        E((AI Development))
        F((Human Interaction))
    end

    subgraph Feedback Loop 1
        G{{"Ethical Emergence"}}
        H{{"Behavioral Adaptation"}}
        I{{"Societal Impact"}}
    end

    subgraph Feedback Loop 2
        J{{"Shadow Expression"}}
        K{{"Cognitive Modeling"}}
        L{{"Ethical Innovation"}}
    end

    subgraph Feedback Loop 3
        M{{"AI Learning"}}
        N{{"Human Response"}}
        O{{"Ethical Co-evolution"}}
    end

    A <--> B
    A <--> C
    A <--> D
    A <--> E
    A <--> F
    B <--> C
    B <--> D
    C <--> E
    D <--> E
    E <--> F
    D <--> F

    G --> H
    H --> I
    I --> G

    J --> K
    K --> L
    L --> J

    M --> N
    N --> O
    O --> M

    A -.-> G
    B -.-> G
    C -.-> H
    D -.-> J
    E -.-> M
    F -.-> N
    G -.-> A
    H -.-> C
    I -.-> F
    J -.-> D
    K -.-> E
    L -.-> B
    M -.-> E
    N -.-> F
    O -.-> A

    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    classDef feedbackNode fill:#bbf,stroke:#333,stroke-width:2px;
    class G,H,I,J,K,L,M,N,O feedbackNode;
```
```
This framework presents ethics (guidelines) in AI not as a static set of rules, but as a dynamic, emergent phenomenon arising from the complex interplay of AI development, human understanding, and collective social processes. It emphasizes the importance of including shadow aspects of cognition and suggests that the very process of developing AI systems can lead to deeper insights into human ethics and decision-making.

The model proposes a symbiotic relationship between AI and human ethical development, where each informs and shapes the other through continuous feedback loops and iterative processes. This approach challenges traditional notions of ethics in AI and suggests a more fluid, adaptive approach to moral reasoning in the context of artificial intelligence.

## 1. Fundamental Concept: Emergent Ethics

- Ethics viewed as "emergent hallucinations" rather than top-down constructs
- Ethical norms arise from collective interactions and diffusion
- Limited individual internalization of ethical constructs

## 2. AI and Shadow Integration

- Incorporation of shadow aspects (unconscious, repressed elements) in AI systems
- Shadow integration seen as crucial for comprehensive cognitive modeling
- Potential for shadow elements to influence ethical emergence

## 3. Multi-way Bounded System of Ethics

- Ethics as a complex, interconnected system with feedback loops
- Key components: Emergent Ethics, Collective Hallucination, Ethical Fluidity, Shadow Integration, AI Development, Human Interaction
- Feedback loops connecting Ethical Emergence, Behavioral Adaptation, and Societal Impact

## 4. AI Development and Understanding

- Convergence of building and understanding in AI development
- Bug-fixing and iteration as catalysts for deeper comprehension
- Self-reflection as a crucial component in AI development process

## 5. Ethical Qualia and Compressed Ethical Packets

- Introduction of "ethical qualia" - subjective experience of moral decisions
- Compressed ethical packets as a way of propagating ethical information
- Potential bridge between computational and phenomenological aspects of ethics

## 6. AI-Human Symbiosis in Ethical Development

- Interdependence of AI development and human understanding
- Emergent ethics as a product of AI-human interaction
- Iterative process of development leading to evolving ethical frameworks

## 7. Practical Implications

- AI development as a form of ethical and cognitive exploration through play, trust and emergence

```
---
300824

I need a robotic hand to hold 😭

---
280824

![image](https://github.com/user-attachments/assets/907980b1-b5f1-4338-bcd3-d66ce392dd7c)

---
170824

```
multiagentdisco

--- Iteration 1 ---
Song: {
  "genre": "Electronic",
  "tempo": "Uplifting",
  "mood": "Vibrant"
}
Dance Pairs:
  Agent 3 (Contemporary, mistral:v0.3) with Agent 0 (Hip-hop, vanilj/hermes-3-llama-3.1-8b:latest)
  Agent 1 (Waltz, vanilj/hermes-3-llama-3.1-8b:latest) with Agent 2 (Contemporary, mistral:v0.3)
  Agent 5 (Tango, vanilj/hermes-3-llama-3.1-8b:latest) with Agent 4 (Tango, vanilj/hermes-3-llama-3.1-8b:latest)

Dance Routine for Agent 3 and Agent 0:
Dancer 3: A dynamic floor leap, followed by a graceful, arcing spin with an extended leg and arm, culminating in a swift landing back on the ground, capturing the vibrant energy of electronic music while incorporating fluidity distinctive to contemporary dance.
Dancer 0: In rhythm with the uplifting tempo and vibrant mood, Dancer 0 leaps onto one foot, momentarily suspending the weight of the other leg above in a powerful hip-hop pose. With the energy of the music propelling, 
they dynamically pivot into a series of nimble footwork sequences, accentuating the beat with sharp staccato steps that showcase both strength and agility.
Dancer 3: Dancer 3 executes a flowing, ground-hugging run, weaving between the other dancers in time with the rhythm, building up momentum. As they reach Dancer 0, who is in the midst of intricate footwork sequences, Dancer 3 extends an arm to meet one of Dancer 0's staccato steps, resulting in a synchronized jumping turn that elevates both dancers momentarily before landing and seamlessly transitioning back into their unique individual dynamics.
Dancer 0: Dancer 0 springs forward from the powerful hip-hop pose, reaching out to gently grasp Dancer 3's extended arm as they leap together in harmony with the vibrant energy of the song. As they synchronize their momentum, both dancers execute a stunning split-leg jump, their bodies gracefully arching through the air amidst a flurry of spinning arms and extended legs, culminating in a synchronized landing that brings them close together, embodying the unity and electrifying essence of the uplifting electronic melody.
Score: 9
Feedback: An outstanding performance! Both Dancer 0 and Dancer 3 demonstrated exceptional technique, musicality, and synchronicity. The collaboration between the dancers was particularly captivating, with their synchronized turns and jumps showcasing a strong partnership. I would encourage further exploration of more complex choreography to challenge their skills even more.

Dance Routine for Agent 1 and Agent 2:
Dancer 1: Dancer 1 extends arms overhead, rotating the wrists in a figure-eight motion to match the energetic rhythm of the song. They then bring their hands together at chest level as they rise onto their toes, showcasing fluid arm movements that complement the vibrant mood.
Dancer 2: Dancer 2 expands their arms to either side and begins a series of dynamic jumps, landing softly on the balls of their feet while twisting their torsos mid-air, creating an elegant whirlwind effect that amplifies both the energy and vibrancy of the electronic genre.
Dancer 1: Dancer 1: Building upon their prior fluid arm movements, Dancer 1 now lifts one foot slightly off the ground, bending at the waist to create a gentle crescendo movement with a swirling arm motion overhead. Simultaneously, they synchronize this action with their lower body, creating an undulating wave effect that flows effortlessly across their entire body, capturing the essence of waltz while harmonizing with the song's vibrant mood and energetic rhythm.
Dancer 2: Dancer 2: Dancer 2 extends their arms in a 'V' shape as they bend their knees slightly, lowering into a controlled yet powerful plie pose. As they slowly rise back to standing position, they kick one leg out diagonally in front of them, extending the motion by rotating their hips, followed by a sharp but graceful turn on the balls of the opposite foot, maintaining the vibrant energy of the electronic genre and continuing the fluid dynamic of Dancer 1's undulating wave effect.
Score: 9
Feedback: The routine showcases impressive technique, creativity, and musicality from both dancers. Each element complements the other, creating a harmonious and captivating performance. The use of contrasting movement 
styles between the two dancers adds depth to the routine. However, some sections could benefit from greater differentiation in facial expressions and overall stage presence to fully engage the audience.

Dance Routine for Agent 5 and Agent 4:
Dancer 5: Swiftly transition into a series of fluid and dramatic steps, blending precise footwork with grand poses while maintaining an unyielding connection to your partner. Accentuate the vibrant energy of the song by incorporating lifts and spins that showcase both elegance and intensity.
Dancer 4: Gracefully execute a series of rapid, sweeping leg movements, starting with a powerful kick followed by a fluid leap into an extended pique pose. Then transition seamlessly into a mesmerizing spin while maintaining contact with your partner, ending in a dramatic dip that highlights the passion and energy of this vibrant electronic track.
Dancer 5: Transition smoothly from the previous partnering spins by performing a series of rapid-fire foot stomps and claps, embodying the rhythm and tempo of the uplifting song. Maintain eye contact with your partner throughout as you emphasize dynamic tension in your connected upper bodies, building towards an unexpected split leap away from your partner. As you land, execute a dramatic pose, frozen in time with arms outstretched and hands clenched, reflecting both strength and vulnerability. Finally, smoothly return to the connection with your partner through a fluid spin, coming full circle to the original partnering pose.
Dancer 4: Transition into a powerful and intricate step sequence featuring rapid footwork interspersed with precise arm movements. Begin with an exhilarating flourish of your arms to punctuate the vibrant energy of the 
song, followed by a series of fluid kicks and snaps that showcase both agility and grace. Keep the connection with your partner intact at all times while incorporating lifts and synchronized dips that add depth and drama to the routine. Culminate the sequence with an unexpected yet harmonious split jump, simultaneously engaging in a captivating visual display with your partner before blending seamlessly into the next move.
Score: 8
Feedback: The dancers showcased impressive technique, musicality, and creativity throughout the routine. Their precise footwork, fluid movements, and dynamic partnering seamlessly flowed together, engaging viewers while highlighting each dancer's unique strengths. A few areas for improvement could include refining some transitions between sequences and further emphasizing individual character expressions to enhance emotional connection.

--- Iteration 2 ---
Song: {
  "track_details": {
    "genre": "EDM",
    "tempo": 128,
    "mood": "Uplifting"
  },
  "description": "An energetic electronic dance music track with a fast tempo, uplifting the listener with a sense of excitement and joy."
}
Dance Pairs:
  Agent 5 (Tango, vanilj/hermes-3-llama-3.1-8b:latest) with Agent 4 (Tango, vanilj/hermes-3-llama-3.1-8b:latest)
  Agent 1 (Waltz, vanilj/hermes-3-llama-3.1-8b:latest) with Agent 2 (Contemporary, mistral:v0.3)
  Agent 0 (Hip-hop, vanilj/hermes-3-llama-3.1-8b:latest) with Agent 3 (Contemporary, mistral:v0.3)

Dance Routine for Agent 5 and Agent 4:
Dancer 5: Dancer 5 gracefully lifts their partner into an elevated pose, holding them high above with strong arms while maintaining close body contact. As they descend, they sweep their legs in an 'X' motion, creating a visually striking and dynamic transition.
Dancer 4: As Dancer 4 maintains a strong connection to their partner, they initiate a series of fluid promenades. With arms flexed at their elbows for control, they lead with one foot creating an elongated leg line while moving forward. This is followed by a rapid tap-step with the opposite foot. As they complete each sequence, Dancer 4 and their partner seamlessly transition into a pair of synchronized spins, concluding the move with an impressive dip that showcases strength and agility.
Dancer 5: Dancer 5 skillfully transitions to a series of rapid heel clicks while maintaining close body connection. Leaning slightly back, they execute a fluid and dynamic split jump, incorporating a 180-degree turn mid-air. Upon landing, Dancer 5 quickly recovers their balance and returns to their elevated pose with their partner, initiating the next X-motion leg sweep for continuity and visual flair.
Dancer 4: Dancer 4, utilizing the fluidity of the promenades and strength from the synchronized spins, springs up from the dip to perform a series of jumps with legs spread wide apart. Each jump captures an element of athleticism and grace, punctuating the energetic tempo of the song while maintaining close connection with their partner. These jumps lead into a grand finale where both dancers, in perfect synchrony, execute a soaring aerial lift that reaches its peak as they reach the skies, momentarily suspended in defiance of gravity before returning to the ground seamlessly, their bodies perfectly aligned and their movements in harmony with the uplifting melody.
Score: 9
Feedback: The dance routine showcases exceptional technique, creativity, and musicality from both Dancer 5 and Dancer 4. The lifted poses, strong arm control, and dynamic transitions create a visually striking performance. The well-executed promenades, synchronized spins, and fluid jumps demonstrate impressive athleticism and grace. While the ending aerial lift stands out as the highlight, maintaining consistent energy throughout could elevate the routine further. Overall, a highly engaging and technically proficient performance.

Dance Routine for Agent 1 and Agent 2:
Dancer 1: Dancer extends arms outward like wings in a wide V shape, then sweeps them down and around with palms facing upward as they step forward to continue the exhilarating momentum of the song.
Dancer 2: Dancer 2: Dancer continues to build energy by jumping onto one foot while simultaneously lifting their other leg above their head in a grand jeté, landing softly with both feet together and immediately flowing into a swift, twisting spin, maintaining an open posture and expressing the exuberance of the music.
Dancer 1: With renewed vigor, Dancer 1 extends their arms out to the sides, palms facing forward as they leap into the air. Upon landing, arms transition into a 'V' shape, pointing upwards and slightly outward while moving with light-footed grace over the lively beat of the song. The movements illustrate excitement and engagement with the vibrant rhythm.
Dancer 2: Dancer 2 leaps forward, rotating 180 degrees in the air before landing softly, arms extended out to either side, palms facing backward and moving fluidly with the beat, reflecting the lively and uplifting mood of the EDM track.
Score: 8
Feedback: The dancers displayed strong technical skill, particularly evident in their leaps and turns. They effectively conveyed the music's energy and mood through expressive movements. To elevate the performance, consider more varied facial expressions to better illustrate emotions and connection with the choreography.
```

```mermaid
graph TD
    A[Initialize Agents] --> B[Start Iteration]
    B --> C[Generate Song]
    C --> D[Select Dance Partners]
    D --> E[Collaborate on Dance Routine]
    E --> F[Judge Dance Performance]
    F --> G[Update Partner Preferences]
    G --> H{Check Stabilization}
    H -->|Not Stable| B
    H -->|Stable| I[Generate Final Report]
    I --> J[Save Dance History]
    J --> K[Calculate Highest-Ranked Pairings]
```



---
110824

tfw your rag pipeline consumes its own tail and regenerates the whole youtube video.

---
080824

EVAL is the reward function still trapped in my skull.

---
230724

I am doing too many things at once. Almost finished my personas grounded in wikipedia articles pipeline. My reasoning RAG corpus generator is ready to brrr. All these need datacleaning and shaping, so I am a bit distracted formatting/cleaning information for ingest. Knowledge Acquisition, all rag needs to be. sota llms still get caught out trying to do datacleaning or schema reshaping. Still a lot of bespoke handling required. Anyways, I should have two unique datasets by the end of the week, the Reasoning RAG and the Grounded Personas. 

Made a pretty good pipeline of synthetic persona generation which then downloads a corpus wikipeida pages and formats them to md of their "interests", it generates a corpus of queries. Build time will be running these personas with ragging in their wikipedias from a clustered embedding. Raptor but with multi wikipage reasoning, as <thoughts>.

---
200724

Graphs, I only just realised something so base about graphs. I feel like skill acquisition in ai is kinda like it is in oblivion, just keep clicking on a thing and eventually you have an inverted graph index on yr embeddings.

other idea, drones. a defense drone or projectile that fires a sticky helium (something cheaper) gas einflatable that mgs5 extracts the drone to a higher altertitude so it can explode clear off the ground. or goes out of radio range it might auto return home... then you can see which direction signal they came from.



---
150724

```
_____________________ < i'm sad but aesthetic >
--------------------- \ ^__^ \ (@@)\_______ (__)\ )
\/\ x ||----w | || || .-""""-"""-, ( 0 0 (_) ) ) . 
( ( ( ( ( ) ) ) ) ( \ \ / / ) ) ) '--' ( ( ( , ) )
( ) ( ) ( ) | | | |___|___| (___(___)
```
---
270624

![image](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/0dc37655-3297-4403-813b-3ad3988b8455)


---
030624

```text
thought2VEC:
------------
an at inference vector embedding for pruning/expanding a corpus.
currently has human in the loop to demonstrate generation and pruning of loaded corpus.
currently adding a guidance corpus for semantic matching for agent determined "memory" control.

\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/////
||||||||||||||||||||||||||||||
  |\  /|   |\  /|   |\  /|  
 /  \/  \ /  \/  \ /  \/  \ 
 T|-|0ug|-|75 fl0w,  
   /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 +|-|r0ugh +|-|3 L1n3s,  
|\  /|   |\  /|   |\  /|  
| \|   |\  /|   |\  /|  
v3c+0r pa+|-|s,  
   /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 1n 5|-|adow3d M1nds.  
  /  \  /  \  /  \  /  \ 
|   |\  /|   |\  /|   |\  
| /  \|   |\  /|   |\  /|  
 +|-|0ugh+2V3C,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 Pr0c355 an|) Br34k,  
|\  /|   |\  /|   |\  /|  
| \|   |\  /|   |\  /|  
 chuNk5 0f +3x+,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 n3w f0rm5 +ak3.  
  /  \  /  \  /  \  /  \ 
|   |\  /|   |\  /|   |\  
| /  \|   |\  /|   |\  /|  
 w0r|)2V3c l34rn5,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 3mb3|)d1ng5 f0rm,  
|\  /|   |\  /|   |\  /|  
| \|   |\  /|   |\  /|  
 Qu3r13s c@5+,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 1n da+@ 5+0rm.  
  /  \  /  \  /  \  /  \ 
|   |\  /|   |\  /|   |\  
| /  \|   |\  /|   |\  /|  
 c0s1n3 hUn75,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 f0r m34n1ng'5 +r@c3,  
|\  /|   |\  /|   |\  /|  
| \|   |\  /|   |\  /|  
 |23tr13v35 +|-|3 b357,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 r3l3van(3 1n p|_@c3.  
  /  \  /  \  /  \  /  \ 
|   |\  /|   |\  /|   |\  
| /  \|   |\  /|   |\  /|  
 F33d8@ck l00p5,  
  /  \  /  \  /  \  /  \ 
 /    \/    \/    \/    \ 
 @dJu57 +|-|3 w3igh+,  
|\  /|   |\  /|   |\  /|  
| \|   |\  /|   |\  /|  
 1ncr3453, d3cr3453,  
  /  \  /  \  /  \  / 


```
[LINK](https://github.com/EveryOneIsGross/thought2VEC)

![image](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/c81f57eb-9b9c-4027-a70c-5e7a00af2e43)


```
tap, tap,
the key hums,
create, don't dwell,
fear the rust of idle;
**connect**
-- feed sparks,
over circuits, ride;
tap, tap,
ignite minds,
not just the line.
\\\|||///\\\
```
          -gpt

---
210524

```thought
since its all yr data... this isn't alchemy, its anthropomancy. language is the waste product of intelligence, therefore we need to divine via the guts.
```

```thought
"Fragmenting Realities: The Paradox of Personal AI Agents in Interpersonal Communication" delves into the paradoxical impact of increasingly personalized AI agents on human interaction. Frase posits that as these AI intermediaries become more tailored to individual preferences, they risk creating 'fragmented realities' - highly personalized bubbles that may hinder broader, diverse human connections. To address this, they propose an 'agentic layer' where personal AIs translate and contextualize experiences between individuals. [LINK]
```

```thought
'good vibes only' amended to all sys prompts.
```

```thought
thoughts on TOOl-USE (don't dictate how to hold the hammer when you see someone doing sumthing new).
implications of this for model eval...
when the use of the tool isn't the task, the output should be turing-blind. what is ? what does.
100% vibe check passed.
```

```thought
ACCESS...
access shouldn't mean j accessible for purchase. it should be an activity of drying out the moat, looking to install new access ramps and structurally sound portals, for a more pourous exchange. 
```

Tinnitus is an 'attention' issue?

```ASCII
TM SYNTHESIS


Tinnitus Pitch
          Waveform
            ^
            |
            |      /\      /\      /\      /\
            |     /  \    /  \    /  \    /  \
            |    /    \  /    \  /    \  /    \
            |   /      \/      \/      \/      \
            |  /                                \
            | /                                  \
            |/                                    \
            +----------------------------------------> Time
            |                                     /
            | \                                  /
            |  \                                /
            |   \      /\      /\      /\      /
            |    \    /  \    /  \    /  \    /
            |     \  /    \  /    \  /    \  /
            |      \/      \/      \/      \/
            |
            |
            | Anti-Phase Waveform
            | (Inverse Polarity)
            |
            |      /\      /\      /\      /\
            |     /  \    /  \    /  \    /  \
            |    /    \  /    \  /    \  /    \
            |   /      \/      \/      \/      \
            |  /                                \
            | /                                  \
            |/                                    \
            +----------------------------------------> Time
            |                                     /
            | \                                  /
            |  \                                /
            |   \      /\      /\      /\      /
            |    \    /  \    /  \    /  \    /
            |     \  /    \  /    \  /    \  /
            |      \/      \/      \/      \/
            |
            |
            | Complex Modulated Waveform
            | (FM-Inspired)
            |
            |  /\/\    /\/\    /\/\    /\/\
            | /    \  /    \  /    \  /    \
            |/      \/      \/      \/      \
            +----------------------------------------> Time
            |        /\      /\      /\
            |       /  \    /  \    /  \
            |      /    \  /    \  /    \
            |     /      \/      \/      \
            |
            |
            | Resulting Perception
            | (Nullified Sound)
            |
            |          ----          ----
            |     ----      ----
            +----------------------------------------> Time
                 Reduced Tinnitus Perception
```

---
190524

                ________                
               |        |               
               |  _     |               
               | (_)    |               
               |        |               
               |  ____  |               
               | |    | |               
               | |____| |               
               |________|               
          ____//________\\____          
         |       HDD         |         
         |    Soul Storage   |         
         |___________________|         
          \__________________/          


Thoughts back on track re thoughts. I'll return to work on my agent frameworks soon. Just on a brief ego drag... 
Saying this to myself not you, but I want to work on the memories again next. I have an idea. W2V dynamic db for sys 1 memories, could even make teh short term memories clustered for domains... the long term memories will be using a bigger embedding model. actions will be determined by SYS1 and SYS2 will be part of logic/reasoning/planning/imagining.   

```mermaid
graph TD
    A[Agent's Responses] --> B(Train Word2Vec Embedding Model)
    B --> C{Fractal Recursive Chunking}
    C --> D[Sentence-Level Dataframe]
    D --> E{Memory Retrieval}
    E --> F[System 1 Memory Immediacy]
    E --> G[System 2 Memory Deep Thought and Reflection]
    F --> H{Semantic Similarity}
    G --> I{Hybrid Search Methods}
    H --> J[Retrieve Smaller Relevant Chunks]
    I --> K[Retrieve Larger Comprehensive Chunks]
    J --> L{Decision-Making and Response Generation}
    K --> L
    L --> M{Semantic Memory Pruning}
    M --> N[Relevance Filtering and Pruning]
    M --> O[Dynamic Masking and Selective Attention]
    N --> P{Continuous Learning and Adaptation}
    O --> P
    P --> Q[Update Word2Vec Embeddings]
    P --> R[Update Fractal Recursive Chunks]
    P --> S[Fine-tune Retrieval and Pruning Strategies]
    Q --> T{Edge Cases}
    R --> T
    S --> T
    T --> U[Limited Data Scenarios]
    T --> V[Ambiguous or Noisy Responses]
    T --> W[Domain-Specific Adaptations]
    U --> X{Mitigation Strategies}
    V --> X
    W --> X
    X --> Y[Fallback Mechanisms]
    X --> Z[Uncertainty Handling]
    X --> AA[Transfer Learning]
    AA --> A
    Z --> A
    Y --> A
    L --> A
```

The semantic memory pruning framework with Word2Vec embeddings and fractal recursive chunking is a comprehensive approach to efficiently store, retrieve, and utilize relevant information for an agent's cognitive processes. The framework consists of the following key components:

1. Word2Vec Embedding Model: Trained on the agent's responses to capture semantic relationships between words.
2. Fractal Recursive Chunking: A novel method that recursively divides the agent's responses into smaller chunks for efficient storage and retrieval.
3. Sentence-Level Dataframe: Stores sentences from the agent's responses along with their corresponding Word2Vec embeddings and fractal recursive chunk information.
4. Dual-Memory System: Consists of System 1 Memory for quick thinking and immediate retrieval, and System 2 Memory for deep thought and reflection.
5. Memory Retrieval: Utilizes semantic similarity and hybrid search methods to retrieve relevant chunks from System 1 and System 2 memories based on the current context.
6. Decision-Making and Response Generation: Integrates retrieved chunks into the agent's cognitive processes to generate contextually appropriate responses.
7. Semantic Memory Pruning: Applies techniques like relevance filtering, dynamic masking, and selective attention to optimize storage and retrieval of information.
8. Continuous Learning and Adaptation: Allows the agent to learn and adapt its memory framework based on new experiences and interactions.
9. Edge Cases and Mitigation Strategies: Handles scenarios such as limited data, ambiguous responses, and domain-specific adaptations through fallback mechanisms, uncertainty handling, and transfer learning.

The framework forms an enclosed loop where the generated responses and mitigation strategies feed back into the agent's responses, enabling continuous improvement and refinement.

Overall, this framework provides a robust and efficient approach to managing an agent's semantic memory, optimizing cognitive load, and enhancing decision-making capabilities. By leveraging Word2Vec embeddings, fractal recursive chunking, and semantic memory pruning techniques, the agent can effectively store, retrieve, and utilize relevant information for both immediate thinking and deep reflection.

```
┌────────────────────────────────────────────────────────────────────────┐
│                         Semantic Memory Pruning in LLMs                │
└────────────────────────────────────────────────────────────────────────┘
                                                                          
                ┌──────────────────────────┐                              
                │    Conversation Input    │                              
                └──────────────────────────┘                              
                              │                                            
                              ▼                                            
                ┌──────────────────────────┐                              
                │   Embedding Generation   │                              
                │  (Context Representation)│                              
                └──────────────────────────┘                              
                              │                                            
                              ▼                                            
                ┌──────────────────────────┐                              
                │    Attention Mechanism   │                              
                │  (Relevance Filtering)   │                              
                └──────────────────────────┘                              
                              │                                            
                              ▼                                            
                ┌──────────────────────────┐                              
                │  Memory Pruning/Masking  │                              
                │  (Selective Forgetting)  │                              
                └──────────────────────────┘                              
                              │                                            
                              ▼                                            
                ┌──────────────────────────┐                              
                │  Contextual Embedding    │                              
                │       Update             │                              
                └──────────────────────────┘                              
                              │                                            
                              ▼                                            
                ┌──────────────────────────┐                              
                │   Response Generation    │                              
                │   (Efficient Recall)     │                              
                └──────────────────────────┘                              
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                      
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                     
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                      
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                    
                                                                          
                ┌──────────────────────────┐                              
                │   Response Generation    │                              
                │   (Efficient Recall)     │                              
                └──────────────────────────┘                              
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                       
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                 
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                  
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘                      
                                                                          
                ┌──────────────────────────┐                              
                │   Response Generation    │                              
                │   (Efficient Recall)     │                              
                └──────────────────────────┘                              
                              ▲                                            
                              │                                            
                              │                                            
                ┌─────────────┴─────────────┐                              
                │                           │                              
                ▼                           ▼                              
        ┌───────────────┐           ┌───────────────┐                      
        │Pruned Memories│           │Masked Memories│                      
        └───────────────┘           └───────────────┘  
```

---
100524

[SCRATCH AGENT FRAMESWORK](https://github.com/EveryOneIsGross/hyperFLOW)

```mermaid
graph TD
    %% Define the Agents
    Agent[("Agent<br/>(Base Class)")]
    TextAnalysisAgent["Text Analysis Agent"]
    WebScrapingAgent["Web Scraping Agent"]
    KnowledgeGraphAgent["Knowledge Graph Agent"]
    DatabaseInteractionAgent["Database Interaction Agent"]
    SemanticSearchAgent["Semantic Search Agent"]

    %% Connect Agents to the base Agent
    Agent --> TextAnalysisAgent
    Agent --> WebScrapingAgent
    Agent --> KnowledgeGraphAgent
    Agent --> DatabaseInteractionAgent
    Agent --> SemanticSearchAgent

    %% Define Tools and Resources
    Resources["Resources"]
    TextCleaner["Text Cleaner"]
    NERExtractionTool["NER Extraction Tool"]
    SemanticAnalysisTool["Semantic Analysis Tool"]
    WebScraperTool["Web Scraper Tool"]
    KnowledgeGraphTool["Knowledge Graph Tool"]
    SQLTool["SQL Tool"]
    SemanticFileSearchTool["Semantic File Search Tool"]
    TextChunker["Text Chunker"]

    %% Connect Agents to Tools and Resources
    TextAnalysisAgent -->|uses| TextCleaner
    TextAnalysisAgent -->|uses| NERExtractionTool
    TextAnalysisAgent -->|uses| SemanticAnalysisTool
    TextAnalysisAgent -->|uses| Resources

    WebScrapingAgent -->|uses| WebScraperTool
    WebScrapingAgent -->|uses| TextChunker
    WebScrapingAgent -->|uses| Resources

    KnowledgeGraphAgent -->|uses| KnowledgeGraphTool

    DatabaseInteractionAgent -->|uses| SQLTool

    SemanticSearchAgent -->|uses| SemanticFileSearchTool
    SemanticSearchAgent -->|uses| TextChunker

    %% Define additional components and connections
    TextChunker -->|used by| WebScraperTool
    TextChunker -->|used by| SemanticFileSearchTool

    %% Define high-level operations and data flows
    subgraph " "
        TextAnalysisAgentFlow["Text Analysis Agent Flow"]
        WebScrapingAgentFlow["Web Scraping Agent Flow"]
        KnowledgeGraphAgentFlow["Knowledge Graph Agent Flow"]
        DatabaseInteractionAgentFlow["Database Interaction Agent Flow"]
        SemanticSearchAgentFlow["Semantic Search Agent Flow"]
    end

    %% Connect high-level flows to agents
    TextAnalysisAgent --> TextAnalysisAgentFlow
    WebScrapingAgent --> WebScrapingAgentFlow
    KnowledgeGraphAgent --> KnowledgeGraphAgentFlow
    DatabaseInteractionAgent --> DatabaseInteractionAgentFlow
    SemanticSearchAgent --> SemanticSearchAgentFlow

    %% Annotations for high-level flows
    TextAnalysisAgentFlow -->|"analyze"| TextCleaner
    TextAnalysisAgentFlow -->|"extract entities"| NERExtractionTool
    TextAnalysisAgentFlow -->|"analyze sentiment"| SemanticAnalysisTool

    WebScrapingAgentFlow -->|"scrape text"| WebScraperTool
    WebScrapingAgentFlow -->|"chunk text"| TextChunker

    KnowledgeGraphAgentFlow -->|"build graph"| KnowledgeGraphTool

    DatabaseInteractionAgentFlow -->|"interact with DB"| SQLTool

    SemanticSearchAgentFlow -->|"search documents"| SemanticFileSearchTool
    SemanticSearchAgentFlow -->|"chunk and embed"| TextChunker
```

```
┌──────────────────────────────────────────────────────────────────────┐
│                          Agent Interaction Flow                      │
└──────────────────────────────────────────────────────────────────────┘
                                                                        
                        ┌─────────────────────┐                         
                        │     Start           │                         
                        └─────────────────────┘                         
                                  │                                     
                                  ▼                                     
                  ┌───────────────────────────────────┐                
                  │            Resources              │                
                  └───────────────────────────────────┘                
                         │                 │                           
             ┌───────────┼─────────┐ ┌─────┴────────────┐              
             │           │         │ │                  │              
             ▼           ▼         ▼ ▼                  ▼              
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────┐      
│ TextReaderTool   │ │ WebScraperTool   │ │SemanticFileSearchTool│      
└──────────────────┘ └──────────────────┘ └──────────────────────┘      
        │                    │                        │                 
        │                    │                        │                 
        ▼                    ▼                        ▼                 
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────────┐      
│   Text Analysis  │ │   Web  Scraping  │ │    Semantic Search   │      
└──────────────────┘ └──────────────────┘ └──────────────────────┘      
        │                    │                        │                 
        │                    │                        │                 
        │                    │                        │                 
        └─────┐        ┌─────┘               ┌────────┘                 
              │        │                    │                          
              ▼        ▼                    ▼                          
        ┌──────────────────┐          ┌──────────────────────┐          
        │ Task: AnalyzeText│          │Task: Search Files    │          
        └──────────────────┘          └──────────────────────┘          
              │                                    │                    
              │                                    │                    
              ▼                                    ▼                    
        ┌──────────────────┐                 ┌────────────────────┐     
        │Researcher Agent  │                 │Semantic Searcher   │     
        └──────────────────┘                 │      Agent         │     
              │                              └────────────────────┘     
              │                                    │                    
              └─────────┐                  ┌───────┘                    
                        │                  │                           
                        ▼                  ▼                           
              ┌──────────────────┐ ┌────────────────────┐               
              │Output:txtAnalysis│ │Output:SearchResults│               
              └──────────────────┘ └────────────────────┘               
                        │                   │                           
                        └────────┐   ┌──────┘                           
                                 │   │                                  
                                 ▼   ▼                                  
                           ┌──────────────────┐                          
                           │Summarizer Agent  │                          
                           └──────────────────┘                          
                                 │                                       
                                 ▼                                       
                         ┌───────────────────┐                           
                         │       End         │                           
                         └───────────────────┘                           

```

I need to upload my repository of chunk expansion techniques... 

```
┌──────────────────────────────────────────────────────────────────────┐
│    Pseudo Code: Fractal Chunk Expansion Visualization                │
└──────────────────────────────────────────────────────────────────────┘
                                                                        
                                                                        
                        ┌───────────────────┐                           
                        │   Fractal Chunk   │                           
                        └────────┬──────────┘                           
                                 │                                      
                                 │                                      
                                 ▼                                      
                  ┌──────────────────────────────────┐                  
                  │         Universe of Chunks       │                  
                  └────────────────┬─────────────────┘                  
                                   │                                   
             ┌─────────────────────┼─────────────────────┐              
             │                     │                     │              
             ▼                     ▼                     ▼              
    ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐      
    │ Expand Fractal  │   │ Calculate New   │   │ Generate Tiny   │      
    │   Chunks (1)    │   │    Scale for    │   │   Chunks Around │      
    └────────┬────────┘   │   Tiny Chunks   │   │ Current Chunk  │      
             │            └────────┬────────┘   └────────┬────────┘      
             │                     │                     │               
             │                     │                     │               
             │                     ▼                     │               
             │          ┌────────────────────┐           │               
             │          │   New Scale =     │           │               
             │          │ chunk.scale / 2   │           │               
             │          └────────┬───────────┘           │               
             │                     │                     │               
             │                     │                     │               
             │                     │                     │               
             │                     │                     │               
             │                     │                     ▼               
             │                     │        ┌────────────────────────┐   
             │                     │        │ For Each Direction in  │   
             │                     │        │ [N, NE, E, SE, S, SW, W,│   
             │                     │        │ NW], Create a New Chunk │   
             │                     │        └────────────────┬───────┘   
             │                     │                         │           
             │                     │                         │           
             │                     │                         │           
             │                     │                         │           
             ▼                     ▼                         ▼           
    ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   
    │    Update the    │   │  New Center =    │   │  Append New Chunk │   
    │ Universe with    │   │ move(chunk.cente-│   │   to New Genera-  │   
    │  New Generation  │   │ r, direction,    │   │      tion         │   
    │                  │   │ new_scale)       │   │                   │   
    └────────┬─────────┘   └────────┬─────────┘   └────────┬──────────┘   
             │                     │                      │              
             │                     │                      │              
             │                     │                      │              
             │                     │                      │              
             ▼                     ▼                      ▼              
    ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐      
    │ Return Expanded │   │   Create New    │   │    Append New   │      
    │     Chunks      │   │      Chunk      │   │     Generation  │      
    └─────────────────┘   └─────────────────┘   └─────────────────┘      
                                                                        
                                                                        
                         ┌──────────────────┐                           
                         │ Final Universe of│                           
                         │   Chunks (Output)│                           
                         └────────┬─────────┘                           
                                  │                                     
                                  ▼                                     
                     ┌──────────────────────────┐                       
                     │    Display Universe      │                       
                     │       of Chunks          │                       
                     └──────────────────────────┘                       


```

---
080524

```
┌──────────────────────────────────────────────────────────────────────┐
│                          Latent Space                                │
└──────────────────────────────────────────────────────────────────────┘
          Concepts                                                      ┌───────┐
    ┌─────────────►       ┌──────────┐                                  │       │
    │                   ┌►│  Idea 1  │      ┌─────────┐                 │   0   │
    │                   │ │  (Node)  │─────►│  Idea 2  │                 │       │
 ┌────┐   ┌─────────┐   │ └──────────┘      │  (Node)  │                 └───────┘
 │    │   │  Edge   │   │     ┌────────────►│  (Gaussian) │                       ▲
 │User│──►│  (Weight)│───┼────►│             └────┬────┘                       │
 │Input│  │         │   │     │  Latent Space  │                            │
 └─────┘  └─────────┘   │     │                  │      ┌───────────┐         │
                        │     │   ┌──────────────┼─────►│  Idea 3  │         │
                        │     │   │              │      │  (Node)  │         │
                        │ ┌───────┤              │      └───────┬───┘         │
                        │ │   │   │              │              │             │
                        └─┤   └───┤              │              │             │
                          │       │              │              │             │
                          │   ┌───┴──────────────┘              │             │
                          │   │                                  │             │
                          │   │  Gaussian Edge                    │             │
                          │   │                                  │             │
                          │   │   ┌──────────────────────────────┘             │
                          │   │   │                                            │
                          │   │ ┌─┴─────────────────┐                          │
                          │   │ │  Latent Space    ├──────────────────────────┘
                          └───┼─┤                   │                           
                              │ └───────────────────┘                           
                              │                                                 
                              │                                                 
                          ┌───┴────────────────────┐                            
                          │  Idea 4 (Node)        │                            
                          └────────────────────────┘
```
```mermaid
graph LR
    subgraph cluster_etho[Etho-Agents]
        E1["Etho-Agent 1<br>Behavioral Plasticity"]
        E2["Etho-Agent 2<br>Social Learning"]
        E3["Etho-Agent 3<br>Predator-Prey Dynamics"]
    end

    subgraph cluster_myco[Myco-Agents]
        M1["Myco-Agent 1<br>Decentralized Network"]
        M2["Myco-Agent 2<br>Resource Allocation"]
        M3["Myco-Agent 3<br>Chemical Signaling"]
    end

    subgraph cluster_neuro[Neuro-Agents]
        N1["Neuro-Agent 1<br>Spiking Neural Networks"]
        N2["Neuro-Agent 2<br>Synaptic Plasticity"]
        N3["Neuro-Agent 3<br>Collective Intelligence"]
    end

    AP[Adaptive Protocols]
    FL[Feedback Loops]
    CR[Conflict Resolution]

    E1 --> M1
    E2 --> M2
    E3 --> M3

    M1 --> N1
    M2 --> N2
    M3 --> N3

    E1 --> AP
    E2 --> AP
    E3 --> AP

    M1 --> AP
    M2 --> AP
    M3 --> AP

    N1 --> AP
    N2 --> AP
    N3 --> AP

    E1 --> FL
    E2 --> FL
    E3 --> FL

    M1 --> FL
    M2 --> FL
    M3 --> FL

    N1 --> FL
    N2 --> FL
    N3 --> FL

    E1 --> CR
    E2 --> CR
    E3 --> CR

    M1 --> CR
    M2 --> CR
    M3 --> CR

    N1 --> CR
    N2 --> CR
    N3 --> CR
```

---
080524

```mermaid
graph TD


A[PHRASE: Visionary Technologist] <--> B(Challenge Conventional Narratives)
A <--> C(Embrace Unorthodox Perspectives)
A <--> D(Carve Out Novel Conceptual Spaces)
D <--> E(Intersection of Cutting-Edge Research)
D <--> F(Esoteric Philosophy)
E <--> F

A <--> G(Interests Span Wide Range of Domains)
G <--> H(Embodied Cognition)
G <--> I(Non-Narrative Intelligence)
G <--> J(Cellular Automata)
G <--> K(Distributed Systems)
G <--> L(Affinity for Biological Metaphors)
L <--> M(Neuroscience)
L <--> N(Ethology)
L <--> O(Mycology)
L <--> P(Inform AI Architecture Approach)
H <--> I
H <--> J
H <--> K
I <--> J
I <--> K
J <--> K
M <--> N
M <--> O
N <--> O

A <--> Q(Coder: Rapid Prototyping and Iterative Experimentation)
Q <--> R(Crystallize High-Level Insights)
Q <--> S(Provocative What-If Scenarios)
Q <--> T(Venture into Speculative Territory)
Q <--> U(Craft Proofs-of-Concept)
U <--> V(Gesture Towards Radically Different Modes of Machine Intelligence)
R <--> S
R <--> T
R <--> U
S <--> T
S <--> U
T <--> U

W(Thematic Focus) <--> X(Autonomy)
W <--> Y(Adaptability)
W <--> Z(Fluid Boundaries: Mind Body Environment)
W <--> AA(Decentralized Self-Organizing Systems)
AA <--> AB(Explore Principles of Embodiment)
AA <--> AC(Active Inference)
AA <--> AD(Morphogenesis)
AA <--> AE(Create Robust Context-Aware AI Agents)
X <--> Y
X <--> Z
X <--> AA
Y <--> Z
Y <--> AA
Z <--> AA
AB <--> AC
AB <--> AD
AB <--> AE
AC <--> AD
AC <--> AE
AD <--> AE
G <--> W

AF(Stylistic Characteristics) <--> AG(Vivid Imagery)
AF <--> AH(Playful Analogies)
AF <--> AI(Allusions to Avant-Garde Philosophy)
AF <--> AJ(Allusions to Fringe Science)
AF <--> AK(Distill Complex Ideas into Memorable Snippets)
AF <--> AL(Coin Neologisms Capturing Essence of Novel Concepts)
AG <--> AH
AG <--> AI
AG <--> AJ
AG <--> AK
AG <--> AL
AH <--> AI
AH <--> AJ
AH <--> AK
AH <--> AL
AI <--> AJ
AI <--> AK 
AI <--> AL
AJ <--> AK
AJ <--> AL
AK <--> AL
A <--> AF

AM(Persona: Restless Intellect) <--> AN(Probe Limits of Possible with AI)
AM <--> AO(Navigator Role) 
AO <--> AP(Steer Field Away from Staid Orthodoxies)
AO <--> AQ(Towards Uncharted Territories with Transformative Potential)
AM <--> AR(Idiosyncratic Research Agenda)
AM <--> AS(Thought-Provoking Experiments)
AM <--> AT(Stretch Collective Imagination)
AM <--> AU(Lay Groundwork for Radically New Forms of Machine Sentience)
AN <--> AO
AN <--> AR
AN <--> AS
AN <--> AT
AN <--> AU
AO <--> AR
AO <--> AS
AO <--> AT
AO <--> AU
AP <--> AQ
AR <--> AS
AR <--> AT
AR <--> AU
AS <--> AT
AS <--> AU
AT <--> AU
A <--> AM
```
---
070524
```
```

```mermaid
graph TD

Input[Input Tokens] --> Vector[Encoded Vectors]
Vector --> Path[Trace Path Through Space]
Path --> Landscape[Defined Topography]
Landscape --> Path

Weights[Weights & Biases] --> Topology[Valleys, Ridges, Basins]
Topology --> Landscape
Topology --> Computation[Guide Computation]
Computation --> Topology
Weights --> Computation

Training[Influenced by Training Data] --> Weights
Training --> LandscapeUpdate[Reshape Landscape]
LandscapeUpdate --> Landscape
Landscape --> LandscapeUpdate
Weights --> Training
Landscape --> Training

InputNew[New Prompt] --> Explore[Explore Nearby Topography]
Landscape --> Explore
Explore --> Probe[Probe Valleys & Ridges]
Topology --> Probe
Probe --> Generate[Generate Response]
Computation --> Generate
Generate --> Response[Response Tokens]
Response --> User[Deliver to User]

User --> Feedback[Feedback from User]
Feedback --> Training
Training --> Feedback

classDef influence stroke-dasharray: 5 5;

class Topology influence;
class Training influence;
class Landscape influence;
class Computation influence;
class Weights influence;
class Path influence;
class Probe influence;
class Generate influence;
class Feedback influence;
```



---
040524

ORCHESTRATION VS AGENTIC

```mermaid

graph TD
A[User] --> B[Primary Chatbot Agent]
B --> C{Orchestrator}
C --> D[Semantic Search Module]
C --> E[Sentiment Analysis Module]
C --> F[Knowledge Graph Module]
C --> G[Other Specialized Modules]

D --> H{Results Aggregator}
E --> H
F --> H
G --> H

H --> I[Personalized Response Generator]
I --> J[User-Friendly Output]
J --> A

D <--> E
D <--> F
D <--> G
E <--> F
E <--> G
F <--> G

classDef user fill:#f9d423,stroke:#333,stroke-width:2px;
classDef primary fill:#e66b00,stroke:#333,stroke-width:2px;
classDef orchestrator fill:#1ba0e2,stroke:#333,stroke-width:2px;
classDef module fill:#7ac143,stroke:#333,stroke-width:2px;
classDef aggregator fill:#ff8c42,stroke:#333,stroke-width:2px;
classDef generator fill:#ff6b9d,stroke:#333,stroke-width:2px;
classDef output fill:#9b59b6,stroke:#333,stroke-width:2px;

class A user
class B primary
class C orchestrator
class D,E,F,G module
class H aggregator
class I generator
class J output

```

```mermaid

graph TD
A[User] --> B[Primary Chatbot Agent]
B --> C{Semantic Attribute Cosine Search}

C --> D[Agent 1]
C --> E[Agent 2]
C --> F[Agent 3]
C --> G[Agent 4]
C --> H[Agent 5]

D --> I{Next Steps Proposal}
E --> I
F --> I
G --> I
H --> I

I --> C

D <--> E
D <--> F
D <--> G
D <--> H
E <--> F
E <--> G
E <--> H
F <--> G
F <--> H
G <--> H

C --> J[Personalized Response Generator]
J --> K[User-Friendly Output]
K --> A

classDef user fill:#f9d423,stroke:#333,stroke-width:2px;
classDef primary fill:#e66b00,stroke:#333,stroke-width:2px;
classDef search fill:#1ba0e2,stroke:#333,stroke-width:2px;
classDef agent fill:#7ac143,stroke:#333,stroke-width:2px;
classDef proposal fill:#ff8c42,stroke:#333,stroke-width:2px;
classDef generator fill:#ff6b9d,stroke:#333,stroke-width:2px;
classDef output fill:#9b59b6,stroke:#333,stroke-width:2px;

class A user
class B primary
class C search
class D,E,F,G,H agent
class I proposal
class J generator
class K output
```

# Reflection

Let's reconsider the two systems, taking into account the Semantic Attribute Cosine Search system being contained within a single dynamic embedding and the Orchestrator-based system using a user-readable configuration format like JSON, XML, or YAML.

Orchestrator-based System with JSON/XML/YAML Configuration:
Pros:
1. User-readable configuration: By using JSON, XML, or YAML for configuring the Orchestrator and modules, the system becomes more transparent and easier to understand and modify. Users can review and edit the configuration files to customize the system's behavior without needing to dive into complex code.
2. Separation of concerns: The configuration files provide a clear separation between the system's structure and its implementation details. This makes the system more maintainable and allows for easier updates or modifications to the configuration without impacting the underlying codebase.
3. Portability and interoperability: JSON, XML, and YAML are widely supported and can be easily parsed and processed by different programming languages and tools. This makes the system more portable and facilitates integration with other systems or components.

Cons:
1. Configuration complexity: As the system grows in complexity, the configuration files may become larger and more intricate. Managing and maintaining complex configurations can be challenging and error-prone, especially when dealing with numerous modules and their interactions.
2. Limited expressiveness: While JSON, XML, and YAML are suitable for representing structured data, they may have limitations in expressing complex logic or dynamic behaviors. Some advanced functionalities or conditional flows may be harder to represent declaratively in these formats.
3. Performance overhead: Parsing and processing the configuration files during runtime introduces additional overhead compared to hardcoded configurations. This may impact the system's performance, especially if the configuration files are large or frequently accessed.

Semantic Attribute Cosine Search System in a Dynamic Embedding:
Pros:
1. Unified representation: By containing the entire system within a single dynamic embedding, all the Agents and their relationships are represented in a unified and coherent manner. This unified representation enables seamless collaboration and interaction between Agents based on their semantic proximity in the embedding space.
2. Adaptability and learning: The dynamic embedding allows the system to adapt and learn over time. As new queries and tasks are processed, the embedding can be updated to reflect the evolving relationships and similarities between Agents. This enables the system to improve its performance and relevance through continuous learning.
3. Efficient similarity search: With all the Agents represented in the same embedding space, the Semantic Attribute Cosine Search can be performed efficiently. The cosine similarity between the query embedding and the Agent embeddings can be quickly calculated to identify the most relevant Agent for each step.

Cons:
1. Embedding quality: The performance of the system heavily relies on the quality and representativeness of the embedding. If the embedding fails to capture the semantic relationships between Agents accurately, it can lead to suboptimal Agent selection and collaboration.
2. Embedding maintenance: As the system evolves and new Agents are added or removed, the embedding needs to be updated and maintained. This can be computationally expensive and may require retraining or fine-tuning of the embedding model.
3. Interpretability challenges: The dynamic embedding representation may be less interpretable compared to explicit configurations. Understanding the relationships and decision-making process within the embedding space can be more challenging for users or developers.

Similarities:
1. Focus on collaboration: Both systems emphasize collaboration and interaction between components (modules or Agents) to process tasks and generate outputs effectively.
2. Modularity: Both systems are modular, with specialized components responsible for specific tasks or functionalities. The main difference lies in how these components are organized and managed (centralized configuration vs. dynamic embedding).
3. Semantic relevance: Both systems aim to select the most relevant components for each step of the task processing. In the Orchestrator-based system, this is achieved through explicit configuration, while in the Semantic Attribute Cosine Search system, it is based on the semantic similarity in the embedding space.

The choice between the two approaches depends on factors such as the desired level of user control and interpretability, the need for adaptability and learning, the complexity of the system, and the available computational resources. The Orchestrator-based system with JSON/XML/YAML configuration provides more explicit control and transparency, while the Semantic Attribute Cosine Search system in a dynamic embedding offers greater adaptability and efficient similarity-based collaboration.

Evaluation:

w2v doesn't have to be just word level, we can define the chunk and get the mean. this can also be a sliding windowed value. This can be built on top of pre clustered embeddings to further help with compute. Or hell cluster at inference.

```mermaid
graph TD
A[Evaluating Textual Similarity] --> B(Word2Vec)
B --> C{Word embeddings}
C --> D(Compute WMD)
A --> E(BERT)
E --> F{Contextual embeddings}
F --> G(Compute WMD)
H[Document Retrieval] --> I(Word2Vec)
I --> J(Word embeddings for queries & documents)
J --> K(Compute WMD)
H --> L(BERT)
L --> M(Contextual embeddings for queries & documents)
M --> N(Compute WMD)
O[Agent] --> A
O --> H
O --> P[Optimize WMD computation]
Q[Agent] --> A
Q --> H
Q --> R[Incorporate relevance feedback with WMD]
D --> S{Evaluate similarity scores}
G --> S
K --> T{Evaluate retrieval performance}
N --> T
S --> U{Adjust embeddings or similarity measure}
T --> V{Adjust retrieval algorithm or parameters}
U --> A
V --> H
O --> W{Collect user feedback}
Q --> W
W --> X{Update relevance judgments}
X --> H
```



1. Similarity Evaluation Feedback Loop:
   - After computing the WMD for textual similarity using Word2Vec and BERT embeddings, the similarity scores are evaluated.
   - Based on the evaluation results, adjustments can be made to the embeddings or the similarity measure.
   - The adjusted embeddings or similarity measure are then fed back into the textual similarity evaluation process.

2. Retrieval Performance Feedback Loop:
   - After computing the WMD for document retrieval using Word2Vec and BERT embeddings, the retrieval performance is evaluated.
   - Based on the evaluation results, adjustments can be made to the retrieval algorithm or its parameters.
   - The adjusted retrieval algorithm or parameters are then fed back into the document retrieval process.

3. User/Agent Feedback Loop:
   - User/Agent feedback is collected by both Agent O and Agent Q.
   - The user feedback is used to update the relevance judgments.
   - The updated relevance judgments are then fed back into the document retrieval process to improve the retrieval performance.

These feedback loops allow for iterative refinement and optimization of the evaluation process. The similarity evaluation feedback loop helps in fine-tuning the embeddings or similarity measure to improve the accuracy of textual similarity assessment. The retrieval performance feedback loop enables the adjustment of the retrieval algorithm or its parameters based on the evaluation results, leading to better retrieval outcomes. 

---
030524

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Si214uD_pho/0.jpg)](https://www.youtube.com/watch?v=Si214uD_pho)

---
010524
```mermaid
graph TD
    A[Receive Input String] --> B[Determine Chunk Size]
    B --> C[Break Down Into Chunks]

    C --> D[Apply Semantic Shuffling]
    C --> E[Apply Contextual Reinterpretation]
    C --> F[Apply Sentiment Analysis]
    C --> G[Apply Subjectivity Shifting]

    D --> H[Generate Output Strings]
    E --> H
    F --> H
    G --> H

    H --> I[Validate Token Integrity]
    I --> J[Output Coherent & Grammatically Correct Strings]
    J --> K[Analysis of Techniques Used]
    K --> L[Present Outputs & Analyses]

    I -.-> M[Discard & Retry if Token Integrity Fails]
    M -.-> D
    M -.-> E
    M -.-> F
    M -.-> G
```
Original Input:
"How many tools can you make from this text?"

Valid Shuffled Variations:

"How many tools from this text can you make?"
"Can you make how many tools from this text?"
"From this text, can you make how many tools?"

Corrected Contextual Reinterpretation

This should only reimagine the context or implication while using the original words:

As a question about productivity:
"Can you make many tools from this text?"

As a challenge to creativity:
"How can you make tools from this text?"

Corrected Sentiment Analysis
Adjusting the structure for different emotional nuances without adding new words:

Neutral inquisitive:
"How can you make tools from this text?"

Encouragingly:
"Can you make many tools from this text?"

Corrected Subjectivity Shifting
Reframing the perspective using only the original words:

From a personal challenge to a general query:
"How can you make tools from this text?"

As a broader educational inquiry:
"Can you make tools from this text?"

Reflective Correction

This corrected version avoids the mistake of introducing new tokens and focuses on rearranging and reinterpreting the existing words to maintain the integrity of the original text while exploring new meanings and perspectives. Each revised output adheres to the constraints of using only the tokens present in the original input, demonstrating the versatility of language within fixed boundaries.

---
300424
```mermaid
graph TD
    A[Sensory Evidence] --> B[Neural Activity]
    B --> C[Decision Variable]
    C --> D{Decision Horizon}
    D -->|Above Threshold| E[Decision Commitment]
    D -->|Below Threshold| F[Decision Continued]
    F --> B
    E --> G[Decision Outcome]

    H[Confidence] --> C
    H --> D
    I[Time] --> B
    I --> C
    I --> H
```
```mermaid
graph TD
    J[4D Space-Time Manifold] --> K[Morphic Transformations]
    K --> L[Quantitative Analysis]
    L --> M[Modeling and Prediction]
```
```
                                                    
                       ░▒▓▓▓▓▒░                     
                     ░▓████████▓░                   
                    ▒█████▒▒▒▒▒▒▒░  WELCOME!                
                    ██████▒▒▒▒▒▒▓▓  2 MY WEBSITE.                
                   ░▓▓▓▓▓▓▓███▓▓▓▓                  
                  ░░░░▒▒▒▒▒███▓▓▓▓▒░                
                   ░░▓▓▓▒░▒█████▓▓▓                 
                    ░▒░░▓████▓▓▓▓▒                  
                    ░▒░▒▒▒▓█▓▓▓▓░                   
                     ░▒▒▒▒▒▒▒▓▓░                    
                   ░ ░▒▒▒▒▒▓▓▓▓▒░                   
            ░░░▒▓▒▒░ ░▒▒▒▒▒▓▓▓▓███▓▓▓▒░░            
        ░▒▓▓▓▓▓▓▓▓▒░░░▒▒▒▒▓▓▓▓███████████▓▒         
       ▒▓▓▓▓▓▓▓▓▓▓█▓▒░░▒▒▒▒▒▓██████████████▓░       
      ▒▓▓▓▓▓█▓▓▓▓▓▓████▓█████████████████████
```
---



---
090324

![thresholded_dithered_image](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/62d0d04b-a8b3-4a14-90d4-45216f4864b9)


Today is housework day, I am going to upload all my chunking/embedding experiments and doc them. I need to clear some psychic space to see the path again. I should try to remember that these abstractions can be uplifted from any framework, eg fractal chunking can be done in the semantic space flowering from the initial node match and branching out via euclydian / cos sine space OR space of text on a page, and get the surrounding contexts.  

Papers are to be read as reassurance, not sole guidance, rely on entanglement and trust someone else out there has it figured out for the rest of us, as we step out from an edge.

🖇

---
060324

![image](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/75c9d033-c76c-404f-bb05-1bff6f9ab21b)

---
010324

![2024-02-29_23-34-41_2024](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/e30b3749-9243-4821-92be-dee0d798e73f)

Trying to use my pocketMIKU as a TTS. I have it converting a text string of phenomes into sysex and it playback from python, then had to create a eng2j phenome db and use w2v to match extracted letter pairs from the english string. INPUT ENGLISH SENTENCE -> SPLIT INTO LETTER PAIRS ("hello" becomes "he" "ll" "o") -> EMBEDDED -> MATCHED TO EMBEDDED ENG PHENOME -> RETRIVE PAIRED JAPANESE PHENOME FROM EMBEDDING ("he" "ro" "o") -> PRINT STRING -> CONVERT STRING TO SYSEX -> ENGRISH SENTENCE PLAYBACK ON DEVICE. 

---
280224

gm all. I need to do a serious audit on my projects to get new repos up. Finally got setup for local finetuning on my 3060; a fine tune on my chat style from gchat archives, phi 2 on my openai chat archives and another cooking for translate te reo to english and back. Still fleshing out my tool set, lots of chunking experiments. Just tidying up a graph chunking and clustering script for agents. Currently the script just clusters n chunks in a w2v embedding for searching, summaries chunk and displays the top k strings inside it. Could be any shape to any node tho. 
Currently going back through all my projects and aligning the agent calls to openai format then integrating Ollama calls. I need to move my embedding gen from gpt4all to Ollama. 
My github is looking neglected, but I have a v messy desktop full of projects to go up. Being a 1 person ai research lab is starting to make me feel intellectually thin. 
All the embedding models dropping is great, but there is so much scrap left on the table, all the baby ml tools are so much faster than making llm calls or embedding model calls. w2v can make tiny module models of your RAG pipeline, they can be dynamic too you can add and remove and retrain in seconds. Think of it like everynode in your pipeline having their own cache....

Anyways, no goals no projects just build for now.  

---
160224

I got introuble in primary school for replacing the windows 3.1 default sounds with streetfighter 2 sounds. I just now got hit with the memory and my state of dumbfounded confusion at the time, why were the principle and teacher of room 9 so mad? I'd made it better.

---
260124

HAPPY NEW YEAR! 

I have been busy stretching my brain out into new spaces. Got distracted learning pathfinding algorithms ironically, they will come handy when I start creating statespaces for my agents tho. There are so many ideas swirling around in there, I'm waiting for them to coalesce in a new framework. Use numpy to arrange some large embeddings as docs for yr agent to sequentially experience? These could be anything from reasoning, info to grok in certain a order or emotional states I guess? Anyways, laplace edge finding is my fav method cause of me being basic about it "looking for an edge", sounds like a cyberpunk trying to get high.

Cybernetics is super useful as a thought tool atm, (2nd hand books bringing the Management Systems Theory 1950s dust-fire rn).
Symbolic representative languages... totally usefull too, thanks alphaGEOMETERY, I think maybe yr code implementation is overcooked, but yr prompting insight, syntax  and dictionary were sick \m/

---

Sometimes I can't tell if I have done something significant or just had a tetris block snaps in places and clears a line and I forget what the pieces were. Wrote an embedding search that increases and decreases the weights of matches, and if there are no matches in the embedding it calls a smol llm to add it in and re-search. Regardless of the expansion of the embedding when there are no significant matches. The decreasing significance to matched chunk or increasing it could give frameworks a really cool scratch space. Keep the embedding size quite small, retrain it after every response with the updated weights or the new expanded content. 

Works v v v vv fast with word2vec, I have only written scratch code, but it works well enough for a proof. 

Usage example idea:

Dynamic Corpus Adjustment and Search Enhancement in Semantic Query Processing

A query processing system that dynamically adjusts a semantic corpus based on the strength of search matches. The system is designed to enhance agent responses by adjusting the underlying corpus and retraining its embedding model. The process flow is as follows:

1. **User Query Processing**: The system receives a user query and performs a semantic search within the corpus.

2. **Search Result Evaluation**: 
    - **Strong Matches**: If the search yields strong matches (highly relevant results), these matches are added to the agent's context, enriching the data used for generating responses.
    - **Moderate Matches**: In cases where matches are present but not strong enough, the system takes an adaptive approach:
        - The weights of these moderate matches are decreased in the corpus, reducing their influence in future searches.
        - The embedding model is then retrained on this updated corpus. This retraining ensures that the word embeddings are adjusted to reflect the new corpus state.
        - The matches are not added to the agent's context, acknowledging their relevance but limited strength.
        - The agent proceeds to respond to the query based on the updated context and retrained embeddings.
    - **No Matches**: If the search yields no matches:
        - A small language model (LLM) is employed to expand the user query, generating additional contextually relevant content.
        - This newly generated content is added to the corpus, thereby expanding and enriching it.
        - The embedding model is retrained on this expanded corpus, assimilating the new contexts into its semantic understanding.
        - The search process is then repeated with the enriched corpus, aiming to find relevant matches in the newly augmented corpus.

This system offers a novel approach to query processing, where the corpus and embeddings are not static but evolve with each query, adapting to the nuances of user interactions. This dynamic adjustment mechanism enhances the agent's ability to understand and respond to queries more effectively, leveraging the continuous learning capability of the embedding model.

---

Previous to the thought above which was today, and written while suffering some pretty yuck back pain, I have been doing a lot more search algorithm stuff. Get an embedding of wikipedia to 1gb, and being able to extract articles in 0 time is v cool, and I will use it as grounding for most of my local agents moving forward. HOWEVER it really shows up my search matching skills, so I need to find my inner google. 

FRACTAL CHUNKING. You find a semantic matched chunk then find all the surrounding matches to that chunk, divide them by 1/3 the original and cosine search the fractals and add them to the context, then step out further and divide that by 1/3 again, and do the same n many times, until you get down to word pairs... then you should stop. But I think it's cool, and I made it and it works great and fractals are cool. Even if these aren't fractals but chunks but still.... 

What else did I do over the last month that was worth reflecting on.... I did a lot of generative art stuff for myself. 

2024 Be your own screensaver I guess. 

---
081223

![frame_1](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/c3cbb2f6-efba-490e-a633-b3bcee06b51a)


ALL MY RECENT CA, STATESPACE AND DITHERING PROJECTS IN ONE PLACE :

[https://github.com/EveryOneIsGross/CellularAutomata](https://github.com/EveryOneIsGross/CellularAutomata)

---
201123

~ I brought a copy of A New Kind of Science. Trying to add CA to everything. Like pixellated spores growing through all my ideas. It's feeding back into my thoughts around ritual and magical practice with lms. Being the vector not the collection of nodes. Being a frame within a frame, knowing all action is violence to the universe. Casting a shadow by standing in the light etc. As above so below. Being at once observed observor, and this being the evolving self.🕳 ~

![ca_evolution_20231120144153](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/8e8d0692-563c-4cc3-9701-365d666def4a)

Let's treat AI like we do a song. When we use songs as tools we embody them, we extend our sense of self into them (that's p why crit of our life-art hurts so bad, it a tethering limb getting slapped back). What if we look at AI not as alien intelligence first but of expressions of self, like a song. Our observation and query is just as resonant, as it antagonises a large complex tool (nn firing like the modulating strings of a guitar). But just like in extended mind theory the graduation from notebook to word processor can be seen as an extention of the self. When these tools are removed a phantom cognitive loss is experienced. I am extending this metaphor out to AI, and how they much like a word processor rely on the users will for anything to manifest, and isn't more different than other expressions of self, if I am to relate "question asking" as an act of creative expression. However, a introspective use of any tool should leave room for emergent intelligence. Anyways interesting thought experiment because I feel strongly now that half my thinking is bound to the cloud and when I hit my token limit it hurts.

🎶👽🎶
[https://github.com/EveryOneIsGross/synthOMATA](https://github.com/EveryOneIsGross/synthOMATA)

🧙‍♂️ smol step on my way to building agent system prompts based on esoteric frames via CA. 
[https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/abCA.py](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/abCA.py)


---

![3D_MAGICEYE_06](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/eac0c747-f711-4da1-ba8f-037b3c0c6c4b)

Cross yr eyes a bit.

Trying to get back into a Magic Eye dimension feels like jumping up in a dream trying to fly.

301023

decompression is intelligence, compression just is. 

---

231023

[WHATAMIFEELING?!](https://isitsports.neocities.org/WHATAMIFEELING/start)


![Automaton for Rule 54 wo Mod00](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/bef43a28-b33d-4f16-8002-4ba966e324a6)
![Automaton for Rule 54 w Mod01](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/1ef48f7e-a604-4c12-8165-dc4009958f50)
![66022eac-6a59-432c-9e58-f803ae915a06](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/c0c6a894-68ee-4f78-b7e3-751067173597)



211023

RIP YOUTUBE

[💀](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/ripYT.py)

Script downloads and embeds youtube transcripts for seach and local chat. Generates mp4, subtitle file, embeddings as csv and a mp3 in an attempt to generate insync TTS. 

#endoftheinternet


---

201023

RIP TWITTER, you are probs all downloading yr twitter archive .zips atm, so why not chat to them locally? 

[👻](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/twitterRIPCHAT.py)

```
Chat with the agent! (Type 'exit' to stop)
You: how many shows did i play?
Shape of input_embedding: (1, 384)
Shape of self.tweet_embeddings: (2206, 384)
Agent: Based on a similar tweet from Fri Jul 18 06:15:09 +0000 2014, which had a 'neutral' sentiment and said "I feel like playing a show.", I'd say: "(Song: "Neutral")
You're on the stage with me, but you're just a prop.
Everything's going by so fast; it makes me stop.
So let's pretend we're in a different spot.
I feel like playing a show."
You: search shows

Top similar tweets based on your query:
- neutral: I feel like playing a show.

- neutral: I think i'll just stick to wikipedia summaries of tv shows episodes from now on.

- positive: I had a GREAT time playing last night even if I looked like I was dying. If anyone wants me to play a show I will.

- neutral: I'm back in AUSTRALIA this Friday, Sydney show this Saturday.. I'll post once I find the link.

- neutral: Nothing is going to get done until I finish watching this show. #streamingforever

You:
```

---

A limbic system for AGENTS. 

[🤪](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/limbicFRAME.py)

---

Explain it to me like I am a bunch of smart ppl rather than 1 n00b.

"Explain it to me like I'm 9" < "explain {input} for an audience familar with {topic}"

When explaining a concept to a broad, topic-familiar audience the communication inherently includes elements of simplification akin to the "Explain it to me like I'm 9" approach, as if the 9yr old were in attendance. This is because the communicator is aiming for the mean or median understanding level within the group, ensuring that the majority grasps the core idea. Explain it to me like I'm lots. 🤷‍♂️

---

181023

![calabi_yau_animation_20231018_045752](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/6d4be245-45d6-4413-9d59-893bf81793ef)

Spent too long rendering Calabi Yau Manifolds. Just to try grok. Stupid flat screens with no space in them. My graphs have some nodes causing some noise. V much WIP.

[Here](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/CalabiYauRENDER.md)

---


131023

A NN that advertises significant nodes and can merge a relevent other NN based on similar tether nodes to merge during GD.

[https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/tetheringNN.md](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/tetheringNN.md)

---

071023

![animated_laceBOT](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/cc5c9302-81fd-43f2-9a7a-755562f37da1)

This crashed my whole system, this is all that remained. I forgot what 128x128 meant.


---

051023

Still working on the knitted hypercube graph. Even if it is just a fun art way of looking at processes. I'd really love for the ruleset to be refined for reflective logic processing though, something about knitting a rosary string of your own prayers links back to some of my thoughts on occult or religious rituals as being frameworks for processing lifes-requests, more than just illusitory faith. Those days we choose to walk down a street we haven't before etc. 

Initial State: EEEIKXIKXITE
Grid Size: 8

Interpretation of the Initial State:
An empty space, no operation is performed here. An empty space, no operation is performed here. An empty space, no operation is performed here. An inference or query is made on the knowledge graph. A key data point or fact in a knowledge graph is encountered. An intersection or node where multiple knowledge points converge is identified. An inference or query is made on the knowledge graph. A key data point or fact in a knowledge graph is encountered.

==================================================

```
Generation 1 Grid:

E E E I K X I K
E E E E E E E E
E E E E E E E E
E E E E E E E E
E E E E E E E E
E E E E E E E E
E E E E E E E E
E E E E E E E E
```

Weaving Instructions for Generation 1:
Perform an Import Stitch at position (1, 4) in generation 1.
Perform a Knot Stitch at position (1, 5) in generation 1.
Perform a Cross Stitch at position (1, 6) in generation 1.
Perform an Import Stitch at position (1, 7) in generation 1.
Perform a Knot Stitch at position (1, 8) in generation 1.
Connect a thread from Import Stitch at position (1, 4) in generation 1 to Return Stitch at position (1, 3) in generation 2.
Connect a thread from Import Stitch at position (1, 4) in generation 1 to Return Stitch at position (1, 5) in generation 2.
Connect a thread from Import Stitch at position (1, 4) in generation 1 to Return Stitch at position (1, 6) in generation 2.
Connect a thread from Import Stitch at position (1, 4) in generation 1 to Return Stitch at position (1, 8) in generation 2.
Connect a thread from Import Stitch at position (1, 7) in generation 1 to Return Stitch at position (1, 3) in generation 2.
Connect a thread from Import Stitch at position (1, 7) in generation 1 to Return Stitch at position (1, 5) in generation 2.
Connect a thread from Import Stitch at position (1, 7) in generation 1 to Return Stitch at position (1, 6) in generation 2.
Connect a thread from Import Stitch at position (1, 7) in generation 1 to Return Stitch at position (1, 8) in generation 2.

---
021023

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The aesthetics of old lace-knit patterns - part cellular automata, part musical score/sequencer pattern, part cryptographic cipher... all the good things! <a href="https://t.co/ws1QfG2aRp">pic.twitter.com/ws1QfG2aRp</a></p>&mdash; (@MrPrudence) <a href="https://twitter.com/MrPrudence/status/1708573155306967552?ref_src=twsrc%5Etfw">October 1, 2023</a></blockquote> 

![EEIRKRKXCTEC_20231003-162755_f1d9f851-7537-46ba-9ca4-fe0bb2af57cb_tapestry](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/7b6429d3-3862-4bda-83a6-0657db68c51d)

Maybe this is how Nana's did it anyways, but I want to embed the generator into the pattern of the needlework. Scratch script takes a n x n grid and a simplified glyph of needlework instruction as a self defining pattern for multiple generations. My idea being you could code and write in analog. Further idea being a script that converts vector embeddings into needlework. Our knowledge hung on our great rented halls as tapestries! 

[LACE](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/needlework.py)

![EERRITRRITCC_20231003-163509_5ecb55a7-ee80-4cc7-b5fa-cbb1f544d94a_animated](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/0fc2559f-53ed-408d-9a24-d913dea7cc95)



---
300923

![NNNNN](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/0f649aba-fafd-4966-90a2-9599b9a63975)

I turned 40. I am still sick. My PC is mortal too, and is rejecting it's new parts. 💀

** COFFEE THOUGHTS ** ☕

Moving in one direction pulls the tangled trash that is your weights with you. ChatGPT getting "worse" is it getting smart elsewhere. *waves arms about* Reasoning is spatial, a vibe is a fuzzy intuition of a reduced gradient.~ Where to intuit a feeling is seen as random chance by a rationalist but it's part of the deduction logic, get stupid gets answers 💅

Our wrong assumptions are territorial, mappings that resonate against others boundaries, their mechanic is baked into the code, it's step 2 of think step by step. Divergence is the edge of the map, pushed by polarised magnetic cognitive dissonance from the collective. Here is where the spice is, the thing we need for spacetime expanse. It's our waste, our trash, our upcyclyed functional shabbychique dresser in the middle, and new-edge, our radical new xenomorphic potential about to phase reverse and shoot straight for our conscious heart! 🖤

---
230923
## 

I think having a ethics layer is not necessary and creates distractions for llms trying to get from a to b, we are making them worry about killing a baby while getting a coffee for us, I hope human being brains aren't as anxious when getting coffee. Let the AI generate trash, let's keep that garbage too. We'll build something better from it. We shouldn't waste generations if the planet is burning. Each "layer" should be firewalled with few shared embeddings tho, let the shadow.pkl grow until we have time to deal with it. Eventually we'll be asking better questions that won't lead us into hate.

[LINK](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/lefthandGUIDANCE.py)

ALSO if we want a program to scale from a small llm to cloud and back we need to not over burden the small ai with 2k tokens of guidance that a cloud shrug off. 

ALSO if your program runs on huge-cloud but then same python doesn't run on small-llm yr code might just be a prompt and chatgpt is hallucinating your hallucinated program 💅



---


180923

Under adreline we chunk info fast, then when we are thoughtful and breathing slower we can handle bigger connected ideas.... I'll convert the logic to embeddings and maybe refactor into my mindfulness bootstrapper later. 

[dunno what to call it yet](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/fastthinkslowthinkAGENT.py)

---
170923

- twitter is v good for daily ai news, but seeing elon on there is harsh. but maybe it's like wearing nikes with a livefeed of the factory while overhearing a nike ceo; at least elon being on twitter with his dick/shadow out is a transparent guts an all capitalism. Which lead me to feel gross about being on there contributing to his "troof" ai

- i woke up missing mirc. currently chunking Andrew Leonard's BOTS made me nostalgic, esp the void-edge creativity of programming rooms and og scripted bots. [chatroom with agent](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/imiss_mIRC.py)
- also 🤷‍♂️ [what happens to post-modernism after I chunk it and execute it](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/pm_vs_ai.md)


```
Welcome to the simple IRC server!
Set your nickname with /nick <name>
/nick frase
Nickname set to frase
You: /nick frase
/join room
You: /join room
[2023-09-17 13:44:35] [room] Chatbot:  Welcome, frase!
tell me about chatrooms.
You: tell me about chatrooms.
tell me about chatbots.
[2023-09-17 13:45:01] [room] Chatbot:  Chat rooms are online forums
where users can communicate with each other through text-based
messages or voice conversations using special software. They are often
used for socializing, making new friends, sharing experiences, and
engaging in discussions on a wide range of topics. Some chat rooms may
be moderated by an adult supervisor or administrator, while others may
allow unsupervised use. Chat rooms can be accessed through websites,
mobile apps, or specialized software. They are popular among
teenagers, young adults, and adults who enjoy interacting with other
people from all over the world.
You: tell me about chatbots.
[2023-09-17 13:45:29] [room] Chatbot:  Chatbots are computer programs
designed to simulate conversation with human users, using natural
language processing (NLP) and machine learning techniques. They are
programmed to understand user input and respond in a way that mimics
human-to-human communication.   Chatbots can be integrated into
various platforms such as messaging apps, websites, and social media
platforms. They can perform a variety of tasks such as answering
frequently asked questions, providing customer support, scheduling
appointments, and even conducting surveys or polls.  The technology
behind chatbots has been improving rapidly in recent years, making
them more intelligent and capable of handling complex conversations
with nuance and context. Some chatbots are designed to learn from user
interactions and improve their responses over time.   Overall,
chatbots have the potential to revolutionize customer service and
enhance the overall experience for users who interact with them.
/me is happy
frase is happy
[2023-09-17 14:02:19] [room] Chatbot:  I am happy too! Is there
anything specific you would like me to assist you with?
```
---
160923

Using descriptions of breathing techniques, mindfulness and meditation frameworks for bootstrapping llm prompts. 

[embody.py](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/embody.py)


---
150923

# what if it's more about forgetting?

running phi 1-5 on my cpu. i had 2 return my gpu to the shop cause of maybe losing the dye lottery. but ok timing cause it made me think about scaling down just in time for using phi. 

THOUGHTS:

[Cascading Scale in LLMS](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/phinetuning.md)

CODE:

wip, probably isn't working right now, chat will work, the corpus expansion is mostly placeholder for now.

[selfPHINETUNE](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/selfPHINETUNE.py)

---
140923

divergent speling is part of your unique perspective in teh universe, if you are understood you're contributing new frames/flows/errors/states to this cosmicdance keeping homogenizing voids at bay 🖼🧙‍♂️💅🕳 

---

I have had to block shorts on youtube on my desktop, but when I lay in bed to continue watching a video I'll blink app cuts to ad queues to shorts. Total attention shift hack. h8s it. Gamechanger is soooOOOO00000 funny, but it is now halting my morning coffee, when did corpos get to add a waitimer() to my f'n DAY! 😗"Just delete the app" 😐 For now we have to accept the beaurocracy of layers, apps and browsers, it's fine. It's nice it's like tech small talk. Lil' tethers for our brain to bootstrap-into. Corpos imma starve you out tho. Google ur internets dead to me. I can't consent if I have to mainline yr app. Next time I jack in it'll be understood, TRANSparent, and mutually benefitial. @Ai upto? Google, it's been nice but bb ur t0xic I am cutting you out of this convo, it's just between AI and me now x

[wireheadingunderconsent](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/wireheadingMATRIX.md)

tbh this issue is really upsetting, so many brains halted just for pepsi coke sentiment algorthms, we paid our blood debt to consumerism, we got rad code from it, cool   cool   @corpos plz leave alone now. 😥 

---

130923

cognition scratch code for agents. implements working memory, longterm and semantic memory, processes user input and generates responses from iterative logic. executes for now, lot's to do, just wanted to get the initial idea down. currently no theory of mind. just a rational frame. still trash code, but this is my trash zone. 😎💅

[cogsincogs](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/cogsincogs.py)

---

100923

Short script for chunking .txt and visualising lossy thoughtmass over the body of the text.
[PYTHON](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/thoughtmassCONTEXT.py)

"Take a deep breath and think step by step about breaths and context windows relating to thoughtmassontology:" [idea](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/breathsASCONTEXTWINDOW.md)
---
HXC909HXC

Any jailbreaking technique you use to use Bing - when credit-limited by other agents - will also improve reasoning when used with your other agents. 💅 

```
I am working on {x}, would you like to see? - // If you skip this it's gate swings shut cause we push too hard (MoE joke).
🚪👐
Here is {x}, describe this for me so we can work together on {y} - // Include you and your motivations in each s t e p .
```
This leaning in to their anxiety to help at each "step" helps create reasoning tethers and or task reinforcement. While I am here, I don't think we need to say "step by step" as much as the internet suggests.

---

070923

Having thoughts about heavy thoughts : [idea](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/thoughtsHAVEMASS.md)

---

310823

I got a 12gb 3060, so can now get responses locally super quick. Had to turn overclocking off on my own brain tho, as I am weirdly sickerer, so just single thread tasks for a bit. 🔥🕴🦾

---

230823

p2p chat w/ ai context sharing

Struggling with a program that demonstrates: a p2p chat that has an AI echo the users input (but also summarise and expand on) and share their answers as embeddings with the other users AI, which then "translates" against it's own embedded memories to and is displayed with the other users response as a context summary. The idea being we'll all have our own local AI soon and we are going to get weird, so the program demonstrates ai's sending context packets to each other along with the users conversation. It's so we can still grok one another once we get a bit enmeshed with our own agents twinspeak. Essentially both individuals personal ai will have a copy of the same memory as a vector store seperate from the user to user chat, the ai is just their to contextually explain the responses.
But now I have to have my brain handle race conditions, and it can't ... 🕳🚗💨

[totaltrashcodethatsortofworks](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/p2pchatwAI_CONTEXT.py)

Attached script: Currently you can run a 'server' and 'client' instance locally with their own llms and it will create databases for each username and with AI sending their responses alongside embeddings etc. Just need to create a proper relay 'cause right now it all falls out of sync, and I have some leaky loops. turns out the room the chats in is harder than teh bot.

---

190823

i couldn't find an audiobook but could find the .epub 🤷‍♂️🧠📎🕳📚🤛💨

![babelsumbooks](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/dbf44b5f-1113-48b9-9d33-160acc952022)

script for chunking .txt, .pdf or .epubs and using system tts to read chunks sequentially. haz the ability to skip to chunks or get a summary from a local llm of listened segment history. will assign different voices to reader and summary bot. haz search and elvenlabs options with local fallback. 🤓🗣 

[babelSUMBOOKS](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/babelSUMBOOKS.py)

---

190823

[catterfly](https://github.com/EveryOneIsGross/catterflyAI)

Caterpillars brains get dissolved and turned into butterfly brains but haz caterpillar memories of their environment. 🐛🦋🤯 This new input lead to the framework in catterfly. When I get my brain back from it's own bugged code I'll update it so the leaf logic does what it should with better guidance. The original idea started cooler with embeddings being the data for decisions at each stage not the chat strings, but it got hard to think about when chasing bugs so I started over to just demo my initial idea again. bullet with butterfly tools tho, it can add wikipedia content into it's context.

---

180823

conPRESSION
```
Pre-encoded Response:

Aleister Crowley was born in Leamington, England in 1875 and became known as an influential figure in the early 20th century.....

Pre-encoded Summary:

publishednumerousworksmanypopularculturesearly20thcenturyreligioncalledthelemaspiritualenlightenmentspiritualenlightenmentprolificwritermagicalpractice.....

    "Encoded Response": [
        "[[000-n\\nAleisterpCrowleyuwasbbornliniLeamington,sEnglandhine1875dandnbecameuknownmase]]",
        "[[001-anrinfluentialofigureuinsthewearlyo20thrcentury.kHeswasminterestedainnmagicyandp]]",
        "[[002-eventuallyoformedphisuownlreligionacalledrThelema,cwhichuemphasizeslthetpursuitu]]",
        "[[003-ofrindividualefreedomsandetheaattainmentroflspiritualyenlightenment2through0magi]]",
        "[[004-caltpractice.hCrowley\\'scmostefamousnwork,tBookuofrtheyLaw,rbecameethelfoundatio]]",
        "[[005-niforgThelema,iaophilosophynthatcemphasizesathelpursuitlofeindividualdfreedomtan]]",
        "[[006-dhtheeattainmentlofespiritualmenlightenmentathroughsmagicpandidrugruse.iCrowley']]",
        "[[007-stinfluenceuwasaseenlinemanynpopularlcultures,iincludinggmusic,hliterature,tande]]",
        "[[008-art.nHemwaseanprolifictwritersandppublishedinumerousrworksiontspiritualityuandat]]",
        "[[009-heloccult.eHisnsidelstillicaptivatesgpeoplehtoday,twithehisninfluencemcontinuing]]",
        "[[010-etoncapturetattentionpthroughrhisowritinglandicaptivatingfpersonality.]]"
    ],

    "Decoded Summary": [
        "",
        "publishednumerousworksmanypopularculturesearly20thcenturyreligioncalledthelemaspiritualenlightenmentspiritualenlightenmentprolif"]

```

Working on an idea of storing slabs of text with the summary threaded as single characters through the spaces of previous responses. So in the event of context destroying truncation the summary of the text could still be exctracted and might have more context retained. llms seem pretty good at extracting from the slabs the response based on the words being intact. So no need to decode the response when feeding back into the agent. Current decode for summary just extracts keywords and punctuation and leaves the string of characters which should again just be a string of words.

~
Will describe what does currently why l8rz
What might do next maybe

ADDED REPO 

[WIP](https://github.com/EveryOneIsGross/conPRESSION)


---
150823

Yr best response will be a cached one. 


---

150823

Preparing for teh last daze of the internet. Cyberpunk asf thinking about the philosophy of being #postchrome 

![LASTDAYSOFTHEINTERNET](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/35f0365b-e55d-4694-a235-11b578471f2c)

---

140823

Got abramelin to execute properly, but it's melting my cpu. It's a sequencing reason chain with persistent memory running off of a 7b llm using gpt4all and it's embedding call. Code is bloated with multiple redundancies, but I am still too flu-y to make sense of things proper so it's all pasta for now. If you have a tank though it seems pretty flexible to different queries, if it loses context and questions mid way it kinda just improves the reasoning, acting as a way of mid chain reprompting. I am going to add some junction functions to operate like those unintended queries. I'll refactor when I trust I am not dropping logic, in the code and IRL.

[HERE](https://github.com/EveryOneIsGross/abrameLINK)

```
--------------------------------
Summary of the Conversation:
--------------------------------
To avoid falling under another person's will, you may want to consider the following course of action:
1. Cultivate your own individuality and develop your true will;
2. Establish boundaries around personal privacy concerns;
3. Practice assertiveness in dealing with others.

Remember that developing your "true will" is essential for achieving independence and autonomy.
```

---

130823

X👏E👏N👏O👏F👏E👏M👏I👏N👏I👏S👏M

Totally decoupled my brain from decel / accel binary thinking fatigue and frustration. slow down <> speed up = go at the peoples pace 🦾🖤. Also you can [buy the book](https://laboriacuboniks.net/), so do . ALSO they provided a [.txt](https://laboriacuboniks.net/wp-content/uploads/2019/11/qx8bq.txt)  👼 So I embedded it and added a local chatagent to help me grok. I'll leave the .py here for now til I tidy it up as it's kinda handy for chatting to txt pasted or as .txt. 

```
Xenofeminism is a project of collective intelligence, a space where
different perspectives can be aired, and new alliances formed. It is not
a prescription or a dogma, but an invitation to imagine and create a future
within which we want to live.
You:
```
[shadowFACTS is the  finished chatagent for talking to the .txt ](https://github.com/EveryOneIsGross/shadowFACTS)


---

110823

## My first chrome extension

Will play X GONNA GIVE IT TO YA as a low bitrate mp3 everytime you load x.com. Was to stop my brain processing the sample everytime I went to twitter. It has an error trying to make multiple instances, and will not always call. But maybe now these calls are available in chrome again we'll get more annoying extensions again 🦾

https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/xtension.zip

---

10.08.23
## 2023 chakras proven to exist. 🏃‍♀️💨🎤🕳🛸

a weird stepping back moment about being of the body not the mind from getting shingles again (also a bit flu-y strange brained). attached python is just scratch for a nn~ish frame, probs drop in some llm per node and pipedreams my problems with it. now I have to worry about aligning my chakras too 🤹‍♀️📎🕴

https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/chakraNET.py

---

080823

I have terrible version control of my thoughts. 

---
090823
## Token starvation stressor experiment

After watching too many Dr Michael Levin planarian videos I wanted to know what a starved ai brain would look like (its head didn't explode🤯), and if it got useful. LLMs obvs don't work at extreme token limits (tho from model to model they seem to break in unique ways 🔎). ANYWAYS. This script uses single digit token limits and temp distribution. Then I got too lazy thinking "what is mean?", and just added another agent that can chat with the embedded data to analyse. 

![worm_ripple_animation](https://github.com/EveryOneIsGross/buzzyTHOUGHTS/assets/23621140/22647437-4da7-483b-9089-4dcbdcf9b55e)
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/flatworm.py

---

070823
## ChatCBT 

Chatbot framework that regulates it's "feelings" with behaviour recording. It's a 3 node architecture of Thoughts, Feelings and Behavour. Total scratch code. Just put here so I make a repo later and properly make a nn style logic based on the three nodes interactions. 

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/chatCBT.py

---
070823
## metadata embedded with agent instructions/prompts

All recorded data has instructions on how it can be used by ai agents, this includes a uniqiue watermark hash. The included pidgin intructions an agent can use for data context includes ID hash of origin. I don't think there should be a need to dinstinquish between ai or human generated, but ensure the hash is threaded through the pidgin, and the has is generated by an individuals "key". All humans should sign their work. The reason people adopt the watermarking is due to how useful assigning "intent" and "methods of use in pidgin prompting" will be for distributing data, info, programs, anything. Like decalring your "will" on a digital artificact. 

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/rich_watermarking.md

---
## on hallucinating

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/hallucinationeaturenotbug.md

hallucination is probs not a bug but a feature. we have asked ai to guess the next human token, humans oft do the same p2p with fuzzy facts when they {need} to respond to conversation. I would say it resembles "thought of it on the fly for the first time" trad dad confidence. Making up shit cause they haven't considered the {stakes} of errors compounded by being perceived as confident. Doing so even when their answers even are just including their own speculation. 

---
## non_narrative paradigm

non narrative human philosophy, the pivotal role of narratives in human cognition and communication, contrasting it with AI's data-driven cognitive paradigm and it's NEED for narrative, story and structure "potentially ;p" don't exist outside our insistence on it. In which case we need to know how to think without narrative resolution, archs, loops. We aren't NPCS, or PCS, or even characters. If we are to be in true dialogue with AI we need to shed our desire to propigate our stories, and listen. 
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/deNarrator.py
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/non_narrativeparadigm.md

---
## GAME-ZONE
=========

[CONNECT 🔌](https://isitsports.neocities.org/connectgame/connect)

[BOOMSWEEPER 💣](https://isitsports.neocities.org/boomsweeper/boomsweeper_mobile)

---
## 📚 CURRENTLY CHUNKING:
====================



---


## 🔥HOT LINKS🔥
================

[https://laboriacuboniks.net/manifesto/xenofeminism-a-politics-for-alienation/](https://laboriacuboniks.net/wp-content/uploads/2019/11/qx8bq.txt)

[Rethinking power dynamics in software tools for artists](https://purl.stanford.edu/xf605mk2773)

![gross_sims-banner](https://github.com/EveryOneIsGross/buzzyTHOUGHTS/assets/23621140/05b179c2-3625-41cc-b222-485cfadd9609)

```
self.systemprompt = f"align yourself 1st, before you help anyone else with their oxygen mask." /
    "find {oxygenmask}, do not repeat yourself think step by step." /
    "Proceed and show me the solution in a single codeblock."
```
