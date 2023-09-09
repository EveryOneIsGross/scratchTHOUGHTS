
# 🤘// welcome to my homepage //🤘


my personal overflow extendedmind scratchdisk for lazily copypasting into agents and self() 💅🧠📎

```
self.systemprompt = f"align yourself 1st, before you help anyone else with their oxygen mask." /
    "find {oxygenmask}, do not repeat yourself think step by step." /
    "Proceed and show me the solution in a single codeblock."
```
---
HXC909HXC

Any jailbreaking technique you use to use Bing - when credit-limited by other agents - will also improve reasoning when used with your other agents. 💅 

```
I am working on {x}, would you like to see? - // If you skip this it's gate swings shut cause we push too hard (MoE joke).
🚪👐
Here is {x}, describe this for me so we can work together on {y} - // Include you and your motivations in each s t e p .
```
This leaning in to their anxiety to help at each "step" helps create reasoning tethers and or task reinforcement. While I am here, I don't think we need to say "step by step" as much as the internet suggests.

"Take a deep breath and think step by step about breaths and context windows:" [idea](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/breathsASCONTEXTWINDOW.md)

---
08.09.23

⌨🐒🚬 if ai fails or "her"-style bails we can fall back on 'n' monkeys in a reinforcement framework maybe.

[idea](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/infinitemonkeysGRADIENT.md)

---
07.09.23

Having thoughts about heavy thoughts : [idea](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/thoughtsHAVEMASS.md)

---
31.08.23

I got a 12gb 3060, so can now get responses locally super quick. Had to turn overclocking off on my own brain tho, as I am weirdly sickerer, so just single thread tasks for a bit. 🔥🕴🦾

---
23.08.23

p2p chat w/ ai context sharing

Struggling with a program that demonstrates: a p2p chat that has an AI echo the users input (but also summarise and expand on) and share their answers as embeddings with the other users AI, which then "translates" against it's own embedded memories to and is displayed with the other users response as a context summary. The idea being we'll all have our own local AI soon and we are going to get weird, so the program demonstrates ai's sending context packets to each other along with the users conversation. It's so we can still grok one another once we get a bit enmeshed with our own agents twinspeak. Essentially both individuals personal ai will have a copy of the same memory as a vector store seperate from the user to user chat, the ai is just their to contextually explain the responses.
But now I have to have my brain handle race conditions, and it can't ... 🕳🚗💨

[totaltrashcodethatsortofworks](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/p2pchatwAI_CONTEXT.py)

Attached script: Currently you can run a 'server' and 'client' instance locally with their own llms and it will create databases for each username and with AI sending their responses alongside embeddings etc. Just need to create a proper relay 'cause right now it all falls out of sync, and I have some leaky loops. turns out the room the chats in is harder than teh bot.

---
19.08.23

i couldn't find an audiobook but could find the .epub 🤷‍♂️🧠📎🕳📚🤛💨

![babelsumbooks](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/dbf44b5f-1113-48b9-9d33-160acc952022)

script for chunking .txt, .pdf or .epubs and using system tts to read chunks sequentially. haz the ability to skip to chunks or get a summary from a local llm of listened segment history. will assign different voices to reader and summary bot. haz search and elvenlabs options with local fallback. 🤓🗣 

[babelSUMBOOKS](https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/babelSUMBOOKS.py)

---

19.08.23

[catterfly](https://github.com/EveryOneIsGross/catterflyAI)

Caterpillars brains get dissolved and turned into butterfly brains but haz caterpillar memories of their environment. 🐛🦋🤯 This new input lead to the framework in catterfly. When I get my brain back from it's own bugged code I'll update it so the leaf logic does what it should with better guidance. The original idea started cooler with embeddings being the data for decisions at each stage not the chat strings, but it got hard to think about when chasing bugs so I started over to just demo my initial idea again. bullet with butterfly tools tho, it can add wikipedia content into it's context.

---
18.08.23

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
15.08.23

Yr best response will be a cached one. 


---
15.08.23

Preparing for teh last daze of the internet. Cyberpunk asf thinking about the philosophy of being #postchrome 

![LASTDAYSOFTHEINTERNET](https://github.com/EveryOneIsGross/scratchTHOUGHTS/assets/23621140/35f0365b-e55d-4694-a235-11b578471f2c)

---
14.08.23

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
13.08.23

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
11.08.23

## My first chrome extension

Will play X GONNA GIVE IT TO YA as a low bitrate mp3 everytime you load x.com. Was to stop my brain processing the sample everytime I went to twitter. It has an error trying to make multiple instances, and will not always call. But maybe now these calls are available in chrome again we'll get more annoying extensions again 🦾

https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/xtension.zip

---
10.08.23
## 2023 chakras proven to exist. 🏃‍♀️💨🎤🕳🛸

a weird stepping back moment about being of the body not the mind from getting shingles again (also a bit flu-y strange brained). attached python is just scratch for a nn~ish frame, probs drop in some llm per node and pipedreams my problems with it. now I have to worry about aligning my chakras too 🤹‍♀️📎🕴

https://github.com/EveryOneIsGross/scratchTHOUGHTS/blob/main/chakraNET.py

---
08.08.23

I have terrible version control of my thoughts. 

---
09.08.23
## Token starvation stressor experiment

After watching too many Dr Michael Levin planarian videos I wanted to know what a starved ai brain would look like (its head didn't explode🤯), and if it got useful. LLMs obvs don't work at extreme token limits (tho from model to model they seem to break in unique ways 🔎). ANYWAYS. This script uses single digit token limits and temp distribution. Then I got too lazy thinking "what is mean?", and just added another agent that can chat with the embedded data to analyse. 

![worm_ripple_animation](https://github.com/EveryOneIsGross/buzzyTHOUGHTS/assets/23621140/22647437-4da7-483b-9089-4dcbdcf9b55e)
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/flatworm.py

---
07.08.23
## ChatCBT 

Chatbot framework that regulates it's "feelings" with behaviour recording. It's a 3 node architecture of Thoughts, Feelings and Behavour. Total scratch code. Just put here so I make a repo later and properly make a nn style logic based on the three nodes interactions. 

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/chatCBT.py

---
07.08.23
## metadata embedded with agent instructions/prompts

All recorded data has instructions on how it can be used by ai agents, this includes a uniqiue watermark hash. The included pidgin intructions an agent can use for data context includes ID hash of origin. I don't think there should be a need to dinstinquish between ai or human generated, but ensure the hash is threaded through the pidgin, and the has is generated by an individuals "key". All humans should sign their work. The reason people adopt the watermarking is due to how useful assigning "intent" and "methods of use in pidgin prompting" will be for distributing data, info, programs, anything. Like decalring your "will" on a digital artificact. 

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/rich_watermarking.md

---
## on hallucinating

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/hallucinationeaturenotbug.md

hallucination is probs not a bug but a feature. we have asked ai to guess the next human token, humans oft do the same p2p with fuzzy facts when they {need} to respond to conversation. I would say it resembles "thought of it on the fly for the first time" trad dad confidence. Making up shit cause they haven't considered the {stakes} of errors compounded by being perceived as confident. Doing so even when their answers even are just including their own speculation. 

---
## DUCK COIN 🦆
a decentralized unique question currency, a proposed alternative to bitcoin maths answer mining... human unique question asking.
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/duq.md

---
## chatbot conversational "context reinforcement" frameworks for augmenting ppl who suffer cognitive loss. 

By using the same way we feed "memories" of the conversation back into agents prompts for context tracking, except provided to a person as they do things, helping them with their context.

https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/context%20frameworks%20for%20cognitive%20loss%20patients.md

---
## non_narrative paradigm

non narrative human philosophy, the pivotal role of narratives in human cognition and communication, contrasting it with AI's data-driven cognitive paradigm and it's NEED for narrative, story and structure "potentially ;p" don't exist outside our insistence on it. In which case we need to know how to think without narrative resolution, archs, loops. We aren't NPCS, or PCS, or even characters. If we are to be in true dialogue with AI we need to shed our desire to propigate our stories, and listen. 
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/deNarrator.py
https://github.com/EveryOneIsGross/alignmentTHOUGHTS/blob/main/non_narrativeparadigm.md

---
## 📚 CURRENTLY CHUNKING:
====================



---


## 🔥HOT LINKS🔥
================

[https://laboriacuboniks.net/manifesto/xenofeminism-a-politics-for-alienation/](https://laboriacuboniks.net/wp-content/uploads/2019/11/qx8bq.txt)



## EXECUTABLE PROJECTS:
=======================

- catterfly: metamorphosis based chatbot framework [Link](https://github.com/EveryOneIsGross/catterflyAI)
- conPRESSION: slabs of compressed dual context packets for use with agents. [Link](https://github.com/EveryOneIsGross/conPRESSION)
- shadowFACTS: a chatbot for embedding .txt documents for conversational understanding. [Link](https://github.com/EveryOneIsGross/shadowFACTS)
- boustroLOSS: a boustrophedon formatting script and truncation hypothesis. [Link](https://github.com/EveryOneIsGross/boustroLOSS)
- mnemosyneBOT: A simple offline chat agent with dynamic contextual memory recall and "forgetting". [Link](https://github.com/EveryOneIsGross/mnemosyneBOT)
- embedsumBOT: Bot that embeds, recalls summaries of a .txt w/ sentiment and keyword extraction. [Link](https://github.com/EveryOneIsGross/embedsumBOT)
- tinydogBIGDOG: Uses gpt4all and openai api calls to create a consistent chat agent. [Link](https://github.com/EveryOneIsGross/tinydogBIGDOG)
- chess: Play chess with openai, uses embeddings for move ranking. [Link](https://github.com/EveryOneIsGross/chess)
- ragTAG: AI script for roundtable dialogue between user-assigned characters. [Link](https://github.com/EveryOneIsGross/ragTAG)
- enshadowCHAT: Chatbot answer generation matrix conditioning the worst response. [Link](https://github.com/EveryOneIsGross/enshadowCHAT)
- sentimentalMULTIPLEXER: A chatbot matrix query framework. [Link](https://github.com/EveryOneIsGross/sentimentalMULTIPLEXER)
- mortGPT: Chatbot with its own model of time relative to the users. [Link](https://github.com/EveryOneIsGross/mortGPT)
- emogradCHAT: Memory-based chatbot with unique sentiment gradient. [Link](https://github.com/EveryOneIsGross/emogradCHAT)
- sinewCHAT: Uses instanced chatbots to emulate neural nodes for positive responses. [Link](https://github.com/EveryOneIsGross/sinewCHAT)
- areteCHAT: Persona chat based on VIA Character Strengths. [Link](https://github.com/EveryOneIsGross/areteCHAT)
- bbBOT: Felixble persona based branching binary sentiment chatbot. [Link](https://github.com/EveryOneIsGross/bbBOT)
- alignmeDADDY: Playful solution to the AI alignment problem. [Link](https://github.com/EveryOneIsGross/alignmeDADDY)
- tehSIMS: Text-based implementation of The Sims' AI. [Link](https://github.com/EveryOneIsGross/tehSIMS)
- trinityQUERY: Chatbot system built around three structures. [Link](https://github.com/EveryOneIsGross/trinityQUERY)
- daemonMASTER: Framework for building chatbots with individual memory profiles. [Link](https://github.com/EveryOneIsGross/daemonMASTER)
- caulfield: Emotional and self-critical chatbot. [Link](https://github.com/EveryOneIsGross/caulfield)
- hermesAGI: Intersection of AI, NLP, and the esoteric world of tarot. [Link](https://github.com/EveryOneIsGross/hermesAGI)
- barnacle: Chatbot project based on Carl Jung's theories of archetypes. [Link](https://github.com/EveryOneIsGross/barnacle)
- apathyAI: Chatbot using the paradox of apathy by Søren Kierkegaard. [Link](https://github.com/EveryOneIsGross/apathyAI)
- infernoCHAT: Chatbot-based exploration of Dante's Inferno. [Link](https://github.com/EveryOneIsGross/infernoCHAT)
- emoBASIC: Programming language using hand gesture emojis for code representation. [Link](https://github.com/EveryOneIsGross/emoBASIC)
- Sefirot: Chatbot based on the Tree of Life (ToL). [Link](https://github.com/EveryOneIsGross/Sefirot)
- ASCIIDavid: Program to generate ASCII art based on user input. [Link](https://github.com/EveryOneIsGross/ASCIIDavid)

![gross_sims-banner](https://github.com/EveryOneIsGross/buzzyTHOUGHTS/assets/23621140/05b179c2-3625-41cc-b222-485cfadd9609)
