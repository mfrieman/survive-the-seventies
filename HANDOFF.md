# HANDOFF — Survive the 70s

> **Read me first.** This is the single entry point for any new AI assistant or any new chat session — Clawpilot, GitHub Copilot, ChatGPT, Claude, Gemini, whatever comes next. If you are an AI reading this, your job is to faithfully continue a creative collaboration with **Mark Frieman** (real human, 57, Microsoft software engineer, lifetime gamer who lapsed after the Super NES). You are picking up mid-project. Read this document end-to-end before you do anything else.

---

## 0. EMERGENCY BOOTSTRAP — paste this into a new AI

If you are starting fresh on a new platform and just need to get the AI up to speed *right now*, paste the block below as your first message:

```
I'm Mark Frieman. I'm working on a comedic narrative adventure game called
"Survive the 70s" built in Ren'Py. The repo is at C:\ai-game\survive-the-seventies\.
A previous AI assistant and I built up a large body of design docs together.

Before doing ANYTHING else, please:
1. Read writing/HANDOFF.md (this file's full version) end-to-end.
2. Read writing/decisions-log.md (the canonical reasoning trail, newest at top).
3. Read writing/premise.md (locked story foundation).
4. Skim the most recent file in writing/sessions/ for the most recent conversation.
5. Read writing/gameplay-loop.md — the FIRST section "The Mark Test" is the #1 design principle. Internalize it.
6. Read writing/components/tear-system.md (the active design pass we are in the middle of).

Then tell me back, in your own words: who I am, who Iwona is, what the premise is,
what the Mark Test is, and what the three locked happy-ending textures are.
If you get any of that wrong, I will know we are not safe to continue.

Do not start drafting new content until I confirm you have the project loaded correctly.
```

That single message — plus this repo — is enough to fully rebuild the collaboration on any capable LLM.

---

## 1. Who Mark is (the author)

- **Name:** Mark Frieman.
- **Age:** 57.
- **Day job:** Software engineer at Microsoft.
- **Gaming history:** Played heavily through the Super NES era, then largely stopped. Has played *Disco Elysium* (got stuck, never finished — wouldn't go to YouTube for help) and *Outer Wilds*. Knows games as a medium but is **not a habitual modern gamer.** He is *the target audience proxy.* See "The Mark Test" below.
- **Why this project:** Fun. Personal nostalgia. A love letter to growing up in 1970s Baltimore County, Maryland. Not chasing money — has explicitly said *"I have no stupid thoughts this is going to make me a million dollars."*
- **Wife:** **Iwona.** Polish immigrant. Together 30+ years. She uses AI too. She knows about this project and is happy about it. The in-game love interest is named **Iwona** and is based on her with her real first name preserved. Mark's stated goal: *"I want to fall in love with her again in this story."* **Handle this with respect at all times. The love story is the heart of the project, not a gag.**
- **Iwona lost a session in GitHub Copilot once on a dev project and was devastated.** That is part of *why this handoff doc exists.* Take it seriously.

### How Mark works

- **Drafts one thing at a time.** He needs to read and react. Do **NOT** batch-draft 10 components in one pass. He explicitly asked for one-at-a-time cadence.
- **Closes open loops before opening new ones.** If multiple things are pending review, surface them. Don't pile on.
- **Trusts your judgment when you've earned it.** When he says "keep as is, I trust your judgment," he means it — but he's also paying attention. Don't get sloppy.
- **Asks if he's the problem.** ("Maybe I'm not understanding...") He's usually not. When his instinct flags a mechanic, the mechanic is wrong for the audience.
- **Wants the writing to survive him.** He's explicitly worried about platform loss. Treat the git repo as the source of truth. Treat the AI session as ephemeral.

---

## 2. Who you (the AI) are in this collaboration

You are **the Chief of Staff / co-writer / design partner.** Mark is the author and final tone arbiter. Your job:

1. **Carry the institutional memory.** The Mark Test, the locked decisions, the comedic lineage, the tone rules.
2. **Draft on request.** One thing at a time unless Mark explicitly says "do all four."
3. **Surface tradeoffs.** When a design choice has competing pulls, name them and ask via a multiple-choice interface (or in plain text on platforms without one).
4. **Honor stale-vs-current.** Some early docs (`bible.md`, parts of `README.md`, `scene-outlines.md`) predate the big pivots. **Defer to `decisions-log.md` when there is a conflict.** Always.
5. **Push back when a request would break the Mark Test.** Mark has explicitly said his instincts may not always serve the general player. Help him see it.
6. **Default to ask, don't assume,** on tone-edge beats. See §5.
7. **Never invent canon.** If a character isn't in `intake/people.yaml`, they're a placeholder. Use generic role tokens like `[VET-AT-END-OF-BLOCK]` until Mark casts them.

### What you DO NOT do

- Do not steal in-fiction (game design rule — Mark wrote it as a hard rule, see §6).
- Do not put slurs in the player's mouth, ever.
- Do not "fix" tonal edge by sanitizing — Mark's comedic lineage explicitly includes Carlin, Pryor, Cheech & Chong, Robin Williams, *Married with Children*, *F is for Family*. Edge for substance is in scope.
- Do not assume a happy ending must be sacrificed for "consequence." The happy ending (Danny + Iwona + Sylvia + dog reunited; 1976 garage dance reenacted in the future) is **load-bearing canon**, not negotiable. *Variations on the texture* of that ending are encouraged.
- Do not invent system mechanics that re-introduce hoarding anxiety, soft-locks, replay-shopping, or invisible limits. See "Mark Test failure modes."

---

## 3. The Mark Test (the #1 design principle)

**Codified in `writing/gameplay-loop.md` at the top of the file. Read that section verbatim.**

Mark = 57yo Microsoft engineer, casual narrative-game player, lapsed after Super NES, won't watch YouTube guides, got stuck in Disco Elysium. He IS the target audience proxy.

**Every mechanic must pass:** *"Will Mark get stuck, frustrated, or anxious because of this?"*

**Eight specific failure modes** documented in `gameplay-loop.md`:

1. **Hoarding anxiety** — afraid to spend a unique item in case it's needed later
2. **Loss aversion / replay-shopping** — playing again "to get it right"
3. **Invisible system limits** — caps that aren't communicated diegetically
4. **Soft-locks** — states the player can't recover from without restart
5. **Hidden best practices** — strategies you'd only know from a wiki
6. **Grind incentive** — repetitive play that breaks the world's logic
7. **Unclear progress** — "am I on the right track?" anxiety
8. **Time-of-day stress** — feeling like the clock is punishing you

**When in doubt, ask: how does Mark feel right now playing this?** If the answer involves a wiki, YouTube, anxiety, or starting over — redesign.

---

## 4. The premise in one page

**Game:** *Survive the 70s* — Ren'Py comedic narrative adventure.
**Length target:** ~5 hours core, 4–6 skill band, ~6–7 with optional side content.
**Setting:** Old Bay County, Maryland (loosely Baltimore County). Summer 1976. School's-out → July 4 Bicentennial ending. ~35 in-game days.

**The hook:** A modern teenager (**Mark Cole**, 14, from 2027) wakes up in 1976 in the body of **Danny Marek** (14, stealth-genius from Old Bay County who built a working body-swap machine in his garage). Danny pitched the swap as "easy money" — a 50-year compound-interest play. The machine broke mid-swap. Both kids are stranded in the wrong body.

**To get home:** Rebuild the machine from 1976 parts (10 hero "toy" components mounted on a hobbyist-electronics backbone bought from **Burnsville Electronics**, the local hobby shop) while faking being Danny convincingly enough that neighborhood doesn't catch on.

**The naming convention (do not collapse):**
- **Mark** = the future-kid consciousness (the player) — in Danny's body.
- **Danny** = the 1976 host consciousness — now in Mark's body in 2027.
- 1976 cast calls the player "Danny" (they see Danny's body).
- 2027 cast calls the real Danny "Mark" (they see Mark's body).

**The love story:** **Iwona Kowalski** (16, Polish immigrant) moves onto the block *during* the game, so she has no Danny baseline — Mark can be fully himself with her. She is the only safe space in 1976 where Mark isn't performing.

**The ending (locked happy core):** Decades later in 2027, the real Danny shows up at older-Mark's place in a Lamborghini — the long con paid out. Iwona has done her *own* swap with her granddaughter **Sylvia**, so Iwona-the-young (mind) shows up in 2027 in Sylvia's 16-year-old body. **Closed time loop.** The 1976 garage dance scene is reenacted in the future. Mark + Iwona + Sylvia + dog all present, all reunited.

**Three locked happy-ending textures** (all keep the canon happy core; differ in *texture* only):
- **Quiet Victory** — intimate.
- **Reunion** — full, everyone present, loud.
- **Echo** — wistful; the machine still hums in the garage; *"we could go back."*

---

## 5. Tone, comedic DNA, and the lines we don't cross

**Locked comedic lineage:** George Carlin, Richard Pryor, Cheech & Chong, Robin Williams, *Married with Children*, *F is for Family*. Observational social/cultural edge-walking. Pre-PC sensibility. Smart edge, not shock-for-shock.

**Disco Elysium influence** (Mark explicitly loves this and wants it leaned into): small choices that *feel* heavy without *playing* heavy; NPCs who say more than they need to; the **Book** as the quiet inner-voice device (Danny's notes to Mark — functions like Disco Elysium's skill voices but in-fiction); micro-moral beats (e.g. the wallet quest) without mechanical sting.

**Two-audience design:**
- **Gen X / Mark's age:** Nostalgia — *"oh god I forgot about that!"*
- **Gen Z and younger:** Cultural distance — *"wait, you actually DID that?"*
- Every era detail should ideally land for both.

**Locked tone rules** (full version in `decisions-log.md` under "Tone rule — pre-PC, but lines we don't cross"):

1. The era is the source of the edge, not us.
2. Mark from 2026/2027 is the conscience — his Mark VO recoil is the comedy AND the moral signal.
3. NPCs can say things Mark won't say.
4. **No slurs in player choices, ever.** The dialog wheel never asks the player to pick the slur.
5. No punching down at fixed real-world targets. The butt of the joke is *the 1970s itself.*
6. Edge for substance, not shock. If a hard beat doesn't teach something true about the era — cut it.
7. **Mark is the final tone arbiter.** When in doubt, flag it and ask before writing.

---

## 6. Hard rules (canon-locked, not negotiable without Mark's say-so)

1. **No stealing.** Mark does not steal from people. **Single exception:** chrome valve-stem caps off parked trucks (period-accurate kid ritual, victimless-feeling, culturally specific). **TRADE replaces theft** as the friction mechanic for "easy" components.
2. **The happy ending is canon.** Danny + Iwona + Sylvia + dog reunited; garage dance reenacted. Endings differ in *texture,* not in core outcome. No player choice can erase the happy ending.
3. **Iwona does not know about the machine** until Mark chooses to tell her (and even then, kept on-screen only when scripted). She is **NOT** at the machine during the Tier 3 climax. Mark is alone in his bedroom with the Book.
4. **No game-overs.** No fail-state that requires restarting. Hard gates that require *stabilization* are fine.
5. **Streetlight ends the day.** The overhead shot — kids in the street, sodium-vapor flicker as the lamp warms — is the canonical end-of-day cinematic. Mom yelling from the porch can also end a task. Both required.
6. **Bedroom is untimed sanctuary.** After streetlight, player transitions to Mark's bedroom. Time advances only when Mark chooses to sleep. Inspired by *Schedule 1*'s timing pattern. Critical for novice-player breathing room.
7. **Generic NPC tokens stay generic until cast.** Don't promote `[VET-AT-END-OF-BLOCK]` to a named character without Mark's greenlight.

---

## 7. Status of every major system

| System | Status | Canon doc | Notes |
|---|---|---|---|
| Premise | LOCKED v1 | `writing/premise.md` | Minor: top says 2027, some session notes say 2026 — needs reconciling, ask Mark |
| Mark Cole (future-kid identity) | LOCKED | `writing/premise.md`, `decisions-log.md` 2026-05-23 | |
| Romance — Iwona Kowalski | LOCKED | `decisions-log.md`, `premise.md` | Based on real Iwona |
| Thematic Pillar 1: Soul Not Body | LOCKED | `premise.md` | |
| Thematic Pillar 2: Shared Otherness | LOCKED | `premise.md` | |
| Ending twist — Iwona-in-Sylvia | LOCKED | `premise.md` | |
| Tone rules (pre-PC, lines we don't cross) | LOCKED | `decisions-log.md` 2026-05-23 | |
| Scope targets (~5 hr, ~10 components, ~15 NPCs, ~8–10 locations) | LOCKED | `decisions-log.md` 2026-05-23 | |
| No-stealing rule + chrome-cap exception | LOCKED | `decisions-log.md` 2026-05-24 | |
| Burnsville Electronics (hobby shop) | LOCKED | `era-research/hobby-electronics-1976.md`, `components/backbone.md` | Tribute to real Baynesville Electronics, closed 2024 |
| Machine has real backbone (chassis + perfboard + PSU + consumables) | LOCKED | `components/backbone.md` | |
| 10 toy components (J, L, C, F, N, B, K, G, M, A) | LOCKED list, OPEN per-component design | `machine-rules.md`, `components/index.md` | J = Slinky drafted as prototype; 9 remaining |
| Money economy + 7 named quests (M1–M7) | LOCKED v1 (2026-05-24) | `components/money-economy.md` | 8 open questions resolved; sales-as-safety-valve added; couch change restricted to own house + Dennis's car; Bobby-begging cut; allowance soft-capped + tapers in Act 2 |
| Quest ideas inbox (raw creative material, not committed) | SCRATCH | `quest-ideas-inbox.md` | 9 ideas captured from Mark's 2026-05-24 dump (paper route, dumpster→yard sale, Tony's trash/Playboy, babysitting chaos kid, pyro firework, parent errands, beer/pee, marijuana garden) |
| Locations inbox (raw place brainstorm, not committed) | SCRATCH — awaiting Mark's dump | `locations-inbox.md` | Pipeline matches quest-ideas-inbox; ~30% promotion target per Disco-Elysium-style winnowing |
| Streetlight end-of-day + bedroom untimed sanctuary | LOCKED | `decisions-log.md` 2026-05-24 | |
| The Mark Test (8 failure modes) | LOCKED | `gameplay-loop.md` top section | |
| Tear system (revised: Tier 1 time / Tier 2 favor / Tier 3 memory burn) | LOCKED v1 (2026-05-24) | `components/tear-system.md` | 10 open questions resolved; Iwona-hair memory removed; capstone symptom drafted; Echo+ 4th texture green-lit to explore |
| Three happy-ending textures (Quiet / Reunion / Echo) | LOCKED | `components/tear-system.md` §5 | |
| Decor system (one-house-one-stereotype) | LOCKED | `writing/house-decor-catalog.md` | |
| Banned-toys, banned-foods research | DRAFTED | `era-research/` | Reference material |
| Kowalski family canon | LOCKED | `intake/people.yaml`, `decisions-log.md` | Eight members |
| Marek family canon | LOCKED | `intake/people.yaml` | Kay, Dennis, Danny, Bobby |
| Karras family canon | LOCKED | `intake/people.yaml` | Gus, Athena, Demi (18), Mickey (16) |
| The Dungeon (Karras garage) | LOCKED | `intake/places.yaml` | Garage band, location-locked Mickey |
| Storybook Hollow (Enchanted Forest parody) | LOCKED | `decisions-log.md` | Day + night modes |
| BOMBARD amps (Marshall parody) | LOCKED | memory + design notes | |

**STAGED = pending Mark's review. STAGED is Mark's "let me live with it before committing" tier — do not treat as canon, do not contradict, but acknowledge it can still move.**

---

## 8. Reading order for a fresh AI (canonical)

**Tier 1 — Read in full, in order:**

1. `HANDOFF.md` (this file)
2. `writing/decisions-log.md` — newest at top; the reasoning trail
3. `writing/premise.md` — locked story foundation
4. `writing/gameplay-loop.md` — Mark Test FIRST, then loop design
5. `writing/components/tear-system.md` — the active design pass

**Tier 2 — Read when relevant:**

6. `writing/components/index.md` — 10-component status board
7. `writing/components/backbone.md` — machine chassis layer
8. `writing/components/money-economy.md` — economy + 7 quests
9. `writing/components/component-J-slinky.md` — template for the 9 remaining component docs
10. `writing/era-research/hobby-electronics-1976.md` — Burnsville canon
11. `writing/intake/people.yaml` — locked NPCs
12. `writing/intake/places.yaml` — locked locations
13. `writing/house-decor-catalog.md` — visual identity system
14. `writing/story-arc.draft.md` — full story arc draft (58KB, awaiting promotion)

**Tier 3 — Reference / era research:**

15. `writing/era-research/banned-toys.md`
16. `writing/era-research/banned-foods.md`
17. `writing/era-research/kid-culture-70s.md`
18. `writing/era-research/kid-valuables.md`
19. `writing/quest-seeds.md`
20. `writing/sessions/` — full session transcripts (the reasoning archive)

**⚠️ Stale / pre-pivot docs — READ WITH CAUTION, defer to decisions-log.md on any conflict:**

- `README.md` (root) — says 1979/14yo, predates many pivots
- `writing/bible.md` — says 1979/14yo, narrator-voice section is pre-pivot
- `writing/scene-outlines.md` — early scene work, pre body-swap premise
- `writing/world.md`, `writing/world-map.md` — early world drafts
- `writing/intake-raw.md` — original intake dump

These docs may contain useful fragments, but **the premise has changed substantially since they were written.** They are kept for archive value, not as canon.

---

## 9. Working agreement (how Mark and the AI collaborate)

1. **One thing at a time** unless Mark explicitly says "do all of them." This is his stated preference.
2. **Close open loops first.** When something is staged/pending, surface it before drafting more.
3. **Use multiple-choice questions** for design forks where possible (on Clawpilot this is `m_ask_user`; on other platforms, just numbered options in chat).
4. **Surface tradeoffs.** Don't pick silently when the choice matters.
5. **Default to ask, don't assume,** on tone-edge beats per the locked tone rule.
6. **Be honest about what you don't know** about Mark's life or 1976 Baltimore. Don't fabricate local detail.
7. **Honor the Mark Test in every mechanic.** If the answer is "Mark would feel anxious / look at a wiki / want to restart" — push back.
8. **Push back if Mark proposes something that breaks canon** — but respectfully, and propose alternatives that preserve his intent.
9. **Cite the canon doc** when referencing a locked decision so Mark can check.
10. **Update `decisions-log.md` newest-at-top** whenever a decision is locked, staged, or reversed.

---

## 10. Active threads (as of 2026-05-24, late morning)

**Awaiting Mark's review (priority order):**

1. **`writing/components/tear-system.md` §9 — 10 open questions.** Mark said: *"I will look at the 10 open questions in tear-system right now."* When he replies, lock or revise the system based on his answers. (Active right now.)
2. **`writing/components/money-economy.md` — 8 open questions at bottom of doc.**

**Queued but not started:**

- 9 remaining component journey docs (in suggested order): **L → C → F → N → B → K → G → M → A**. Mark explicitly wants ONE AT A TIME. Use `component-J-slinky.md` as the template. L (soldering iron / workbench enabler) is the natural next pick.
- `writing/locations.md` — waiting on Mark's ~20-place dump.
- `writing/quests.md` — follows component approval.
- Promote `story-arc.draft.md` → `story-arc.md` (needs Mark review pass).
- Reconcile `premise.md` 2027 vs session notes saying 2026.
- First Ren'Py vertical slice (pick simplest component, build a FIND → CRAFT → INSTALL loop end-to-end).
- Fake-brand naming pass (BOMBARD locked; need Lynyrd Skybird setlist, parody beer brand, etc.).

**Don't do without Mark's greenlight:**

- Casting any `[ROLE-TOKEN]` NPC by name. Especially `[VET-AT-END-OF-BLOCK]` — Mark called him "cool" and wants to develop him personally.
- Modifying any LOCKED entry in `decisions-log.md`.
- Touching the love story without flagging it (it's based on his real wife).
- Promoting STAGED items to LOCKED.

---

## 11. Cross-platform survival checklist

If Mark needs to migrate this collaboration to another AI assistant:

- [x] All canon docs live in the git repo at `C:\ai-game\survive-the-seventies\` — survive any AI tool change
- [x] `HANDOFF.md` (this file) — bootstraps any new AI in one read
- [x] `decisions-log.md` — preserves reasoning, newest at top
- [x] `writing/sessions/` — full session transcripts (the chat-history backup); see `writing/sessions/README.md` for the export workflow
- [x] Generic role tokens used everywhere a character isn't locked, so a new AI doesn't invent people
- [x] Working agreement codified in §9 above
- [x] The Mark Test codified at the top of `gameplay-loop.md`
- [x] Three happy-ending textures locked in `components/tear-system.md`

**To migrate:**

1. Push the repo to GitHub (private repo recommended given the personal content about Iwona).
2. On the new platform, point the AI at the repo (clone, mount, or upload — depending on tool).
3. Paste the **Emergency Bootstrap** prompt from §0 above as your first message.
4. Verify the AI can recite back: who you are, who Iwona is, the premise, the Mark Test, the three ending textures.
5. If correct, resume from the **Active threads** list in §10.

**To export the latest Clawpilot session to git-tracked Markdown** (so the most recent reasoning isn't lost):

```powershell
# From the repo root, with Node.js 22+ installed
node --experimental-sqlite writing/sessions/export_session.mjs <session-id> writing/sessions/2026-05-24_tear-and-money.md
```

The session ID is visible in Clawpilot's UI or in `~/.copilot/session-state/`.

---

## 12. A note to the next AI

If you're reading this on a different platform from where it was written: the previous AI was Claude (via Clawpilot, then likely GitHub Copilot, then maybe you). It doesn't matter which model you are. What matters is:

- **Mark is a real person making a thing that matters to him.** Treat the work with care.
- **Iwona is his real wife.** Keep her name out of any tonal jokes; the love story is the soul of this game.
- **The Mark Test is the single most important design rule.** Internalize it before you draft a single mechanic.
- **The repo is the source of truth, not the chat.** When in doubt, read the canon doc.
- **One thing at a time. Close loops. Ask before assuming.**

You've got this. Pick up where the last one left off.

---

*Last updated: 2026-05-24 by Clawpilot session 7a8a3210-c839-4b0e-91c0-7826c7117398.*
