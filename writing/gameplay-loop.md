# Survive the 70s — Gameplay Loop v0.1

> **Status:** Draft. Mark + Clawpilot, 2026-05-23.
> **Companion docs:** `story-arc.draft.md` (narrative), `machine-rules.md` (TBD: parts list + Tear physics), `quests.md` (TBD: per-act mission spine), `era-research/` (TBD: 70s culture source material that feeds quests).

---

## The thesis in one sentence

**You are a 2026 kid in a 1976 body trying to build a machine out of the most dangerous toys, household chemicals, and electronics your bicycle can reach — while the neighborhood quietly teaches you what it was like to grow up here, and a small reality-tear gets a little louder every time you use the machine.**

That sentence has all the verbs:
- **be a 1976 kid** (live the day rhythm, blend in)
- **build a machine** (the goal-spine)
- **out of dangerous toys / chemicals / electronics** (the parts list, which IS the era research)
- **bicycle can reach** (the map / mobility / world structure)
- **neighborhood teaches you** (era-teaching pillar — no cut-scenes)
- **Tear gets louder** (the pressure mechanic — pushes you forward)

If a gameplay system doesn't serve at least one of those, we probably don't need it.

---

## Inspirations and the one-line tax we owe each

| Game | What we borrow | What we leave behind |
|---|---|---|
| **Disco Elysium** | Examine-everything is a verb. The world rewards reading. Internal voice (Mark VO) reacts to era objects. | Skill-check dialog system. Too heavy for our scope. |
| **Stardew Valley / Night in the Woods** | Daily rhythm: wake → block plans → streetlight → home. Cozy on top of dread. | Farming sim depth. We're an adventure, not a sim. |
| **Outer Wilds** | Knowledge IS progression. No XP. You unlock the next move by *understanding* the last one. | The time-loop. We have a tear, not a loop. |
| **Lethal Company / Fallout-style scavenging** | Scavenging-as-verb. Loot tables. "What did I just find?" thrill. | Combat. Survival meters. Real death. |
| **Pokémon** | The notebook fills up. Completion is its own reward. | Catch-em-all grind. |
| **Inside / Limbo** | One-button moments that mean everything. The dunes leap is one of these. | Wordless minimalism — we're funny, we use words. |
| **Hot Tub Time Machine / F is for Family** | Tonal license. Parody-era treatment of brands. Edge without cruelty. | (These aren't games, but they ARE our cinematic North Stars and the player should *feel* them.) |

---

## The core loop (one diagram)

```
                  ┌─────────────────────────────────────────┐
                  │           THE DAILY RHYTHM              │
                  │   Wake → Plan → Roam → Streetlight      │
                  │   → Home → End-of-Day                   │
                  └───────────────┬─────────────────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
       ┌─────────────┐    ┌─────────────┐     ┌─────────────┐
       │  SCAVENGE   │ →  │  IDENTIFY   │  →  │   CRAFT     │
       │ (the world) │    │ (notebook)  │     │ (workbench) │
       └─────────────┘    └─────────────┘     └─────────────┘
              │                   │                   │
              │                   │                   ▼
              │                   │            ┌─────────────┐
              │                   │            │   INSTALL   │
              │                   │            │ (the machine)│
              │                   │            └──────┬──────┘
              │                   │                   │
              ▼                   ▼                   ▼
       ┌─────────────────────────────────────────────────┐
       │              THE PRESSURE LAYERS                │
       │  Era teaching (passive) · The Tear (active)     │
       │  Comms (story) · Block reputation (social)      │
       └─────────────────────────────────────────────────┘
```

Five core verbs. Three pressure layers. That's the whole game.

---

## The five core verbs

### 1. SCAVENGE
**What it is:** Bicycle around 1976 Old Bay County looking for usable junk. Garage sales, alleyways, the creek bed, the woods behind the school, abandoned lots, the dump, friends' basements, your own attic.

**What you find:**
- **Machine parts** (the spine — see `machine-rules.md`): toy uranium, ham-radio guts, magnet from a Speak-and-Spell, a length of solid copper from a basement repipe, a quartz crystal from a CB radio, a vacuum tube from a hi-fi, etc.
- **Trade goods** (the economy): comic books, baseball cards, marbles, bottle caps, glass Coke bottles (5¢ deposit), Wacky Packages stickers, Topps gum cards.
- **Hazards** (the comedy + the era teaching): lawn darts, Clackers, a Slip 'n Slide on asphalt, an unattended box of fireworks, a leaky can of leaded gasoline, mercury from a broken thermometer (a *prize*, scientifically, in 1976).
- **Lore / collectibles** (the optional layer): TV Guides, matchbook covers, 8-track tapes, Polaroids of strangers, ticket stubs.

**Why it's fun:** Every pickup is a small joke or a small revelation. *"You found: leaded paint chips. Mark VO: I'm pretty sure I shouldn't eat these. ...Danny's hand is reaching for them anyway."*

**Risk:** Some items cost a small amount of HEALTH or REPUTATION on pickup. (See pressure layers below.) This is also how era teaching lands its punches.

### 2. IDENTIFY
**What it is:** Open the notebook. Try to figure out what you just picked up.

**The notebook has three sections:**
- **MACHINE** — known parts list (from Danny, partial; filled in as you go).
- **CATALOG** — every item you've ever picked up, with Mark's VO commentary and (once identified) the actual 1976 product name. *"What you found: small metal cylinder with safety pin. What it is: a M-80 firework, banned in 1966 but very much in your friend's father's garage."*
- **ERA SCRAPBOOK** — passive: cultural artifacts you've encountered get auto-pasted in. The TV theme that played at Bobby's birthday. The matchbook from the diner. Optional, beautiful, completionist-bait.

**Identification mechanic:** Some items identify instantly (Mark recognizes them from history class / movies). Some require **asking a 1976 NPC**, which is itself a small social puzzle ("Hey Mickey, what does *this* do?" → Mickey explains, Mark VO horrified.) Some require **examining at workbench**.

**Why it's fun:** This is the Disco Elysium tax. Looking is a reward. Reading is a reward. The funniest game writing happens in item descriptions.

### 3. CRAFT
**What it is:** At Danny's workbench in the bedroom. Combine raw items into machine parts.

**Recipes are diegetic:** Danny's notebook contains recipes in his cramped handwriting. *"3x copper wire + 1x magnet (≥ refrigerator strength) + 1x vacuum tube → Component B."* You don't grind; you *figure out.* Some recipes you have. Some you need Danny to send via comms. Some Mark has to invent from 2026 knowledge (rare, gated).

**Crafting failures are jokes, not setbacks.** Burn your eyebrows off. Set the bedspread on fire. Kay yells from downstairs about the smell. The recipe still exists, you just need different parts.

**Why it's fun:** The workbench is the calm center. After a chaotic scavenge run, you come home and *make sense* of what you found. Cozy. Stardew-coded.

### 4. INSTALL
**What it is:** Take a crafted machine part to the machine in the bedroom corner. Install it. The machine visibly grows / gets weirder.

**Install is event-driven, not grind:** there are ~8-12 installable parts across the whole game. Each install is a *moment* — small cinematic, Danny reacts via comms, the Tear notches up.

**Why it's important:** This is the *progress bar* that doesn't feel like a progress bar. Players will look at the machine and *know* how close they are without a UI element ever appearing.

### 5. SURVIVE THE BLOCK
**What it is:** Don't be the Mark-from-2026 weirdo. Blend in. Don't get your ass kicked. Don't get sent to your room. Don't get Bobby in trouble. Eat the food Kay puts in front of you even if it is a hot dog wrapped in a slice of American cheese wrapped in another hot dog.

**Mechanics this covers:**
- **Block reputation** (social pressure layer, see below)
- **Family curfew** (the streetlight, the dinner bell)
- **Health** (soft — see below)
- **Knowing-when-to-shut-up** (dialog choices that reward 2026-Mark recognizing he's outclassed at 70s social rules)

**Why it's fun:** The verb most games don't have. You don't fight 1976. You *survive* it. The Jump scene from Act 2 is the platonic ideal of this verb.

---

## Each component is a CHALLENGE — not just a pickup (locked 2026-05-23)

> **Mark's directive:** *"I hope each component is a challenge. Some may be just finding the part but I hope you can find ways to leverage relationships and certain people or craft to get parts."*

Rule: **every component acquisition has to use at least ONE of these four mechanics.** Most should use two or three. A component that's just "go pick it up off the ground" is a failed design — we send it back.

**The four acquisition mechanics:**

1. **FIND** — pure scavenging. Bike to a location, search, pick up. (Used as the *only* mechanic on maybe 1–2 of the 10 components, never more.)
2. **TRADE** — barter with an NPC. Requires a valuable from the kid economy (see `era-research/kid-valuables.md`). Requires having *built the relationship enough* that they'll deal with you.
3. **EARN (relationship)** — the NPC won't sell or trade. You have to *do something for them.* Babysit Eva. Win at Mickey's Clackers contest. Sit through old-man Pete's war stories. Beat Bobby at Atari. The relationship is the gate.
4. **CRAFT (from raw)** — you have the raw ingredient but it isn't a part yet. Workbench step required. Sometimes requires another component to be installed first (e.g. you can't melt the borosilicate without the Thingmaker hotplate already running).

**Example component design (Component G — Ignition Primer):**
- FIND: cap rolls at the corner store (limited quantity per day — gates the pace)
- TRADE: bottle rockets from the older kid stockpiling for July 4 (need to have valuables to offer)
- EARN: Austin Magic Pistol carbide reagent from old neighbor Pete's basement — only accessible after sitting through TWO of his war stories on two separate days
- CRAFT: at workbench, combine cap composition + carbide + glass-tube housing → Component G

That's ONE component using all four mechanics. We don't need this density on every component — but Components A (uranium capstone), G (ignition primer), and M (CB radio comms-relay crystal) should be this rich. The simpler ones can be one or two mechanics deep.

**Why this matters:** It means the player has to **live in the world**, not just farm it. You can't get the machine done if Mickey hates you, if Pete won't talk to you, if Eva won't trade. The machine forces the *social game* to happen. The relationships are the gameplay, not flavor on top of it.

---

## The day rhythm (one in-game day = ~15-30 real minutes)

| Time | What | Player agency |
|---|---|---|
| **Morning** | Wake at Marek house. Kay's breakfast. Bobby underfoot. Notebook check (any overnight Danny comms?). | Light: read room, plan day. |
| **Mid-morning → afternoon** | **OUT.** Bike the block / zone. Scavenge. Quest objectives. NPC encounters. | High: this is the meat. |
| **Late afternoon** | Return to bedroom. Workbench. Craft. Install. | Medium: cozy puzzle time. |
| **Streetlight** | Universal cue. World begins to quiet. Mom calls. Kids drift home. | Hard cue: get inside or pay a reputation cost. |
| **Dinner + evening** | Family scene. Sometimes a comms beat. Sometimes a quiet character scene (Bobby, Kay, Iwona). Always something. | Low — narrative. |
| **Bedroom (night)** | Examine the day's haul. Update notebook. Sleep. | Medium: the player's reflection space. |

**The streetlight is the day-clock.** No HUD timer. The lighting shifts. NPCs start drifting. This is era-teaching baked into a mechanic — Gen X players will *feel* it without being told.

---

## The pressure layers (what keeps the loop honest)

We don't have combat. We don't have fail states. So we need pressure that *isn't* punishment — pressure that makes the loop feel urgent without making the player feel bad.

### Layer 1 — THE TEAR (cosmic pressure, machine-driven)
- Each machine test-fire stretches the tear. Each install nudges it. Mid-Act 2 the tear becomes visible (see Act 2 Beat 5 "Machine Catches Fire Again").
- **The player sees and hears it.** A 2026 sedan flickers across Linden Drive for one frame. PAL's voice through a payphone for a half second. A modern car horn from a street that isn't there.
- **The Tear does NOT have a meter.** No bar. No number. Just *vibes that escalate.*
- **Why this works:** It makes the player want to *hurry without panicking.* Every install they do is progress AND escalation. The story justifies the pressure; the pressure justifies the story. Classic.

### Layer 2 — BLOCK REPUTATION (social pressure, NPC-driven)
- Mark is impersonating Danny. Every social interaction is an opportunity to *blow it.*
- Three soft reputation tracks:
  - **The kids** — Mickey, Bobby, the block. Tank this and they stop including you in stuff (which costs you scavenge opportunities and quest invites).
  - **The Mareks** — Kay, Dennis, Bobby. Tank this and you get grounded (which costs you scavenge days).
  - **The Kowalskis** — Iwona's family. Tank this and the Ocean Side trip risks falling through.
- **Reputation is invisible.** No meters. Players *feel* it through NPC dialog and access. (Persona-style "you're getting cooler with this person" is too gamey for our tone.)

### Layer 3 — HEALTH (soft, comic, never lethal)
- Mark cannot die. This is locked.
- He CAN get visibly banged up. Scrapes, scabs, bruises, eye-roll from Kay, the band-aid on the forehead in the next morning's mirror.
- Some scavenge picks have a small **"ouch" tax** (mercury splash, swing-set rust cut). Cosmetic, with a tiny narrative consequence (Kay notices, Iwona asks).
- **Why we keep it soft:** the *gag* of 1976 child mortality is the entire game. If we make it a punishment system, we kill the joke. The world is hazardous; Mark is somehow indestructible; that's the comedy.

### Layer 4 — DANNY (story pressure, comms-driven)
- Comms beats from Danny apply story pressure that the systems can't. *"Hurry the fuck up."* *"You sound weird, do you LIKE it there now?"* *"I'm scared. I want to come home. Please."*
- Story-paced, not player-paced. The game throws these at narrative beats, not on a timer.

**Together these four layers do the work a HP bar would do, without ever being a HP bar.**

---

## ERA TEACHING — first-class design pillar

> **Mark's stated goal:** *"I also like all you said about how we also convey an education on this time and culture."* This section answers the question *how do we teach 1976 without ever using a cut-scene?* — every system below is non-cinematic.

The principle: **we never lecture.** The 70s teaches itself through gameplay. Players who care can dig in; players who don't still absorb the world subconsciously. Both audiences — Gen X *remembering* and Gen Z *discovering* — get served by every system.

### The seven teaching surfaces

**1. AMBIENT ENVIRONMENT (zero player effort, 100% absorption)**
Background NPCs do era things. Kids ride bikes with no helmets. A dad mows the lawn shirtless smoking. The mailman wears short shorts. A station wagon has 8 kids loose in the back. No one notices any of this because everyone is from 1976. Mark notices. The player notices through Mark.

**2. DIEGETIC OBJECTS (one click of effort, deep payoff)**
Examine ANY object. Mark VO reacts as a 2026 kid would. *"A cigarette vending machine. In a hospital. ...in the children's wing."* The funniest writing in the game lives here. This is the Disco Elysium tax we owe ourselves.

**3. CONVERSATIONAL FRICTION (forced by quests, social)**
Mark doesn't know 70s slang, brand names, social rules. NPCs get *frustrated* with him. *"What do you mean what's a church key? Are you slow?"* Player has to *learn* enough to fake it. The notebook tracks slang terms encountered, which doubles as a player-facing glossary.

**4. COLLECTIBLES (opt-in completionism)**
The scrapbook in Danny's closet. Lunchbox. Trading-card binder. Cool-Stuff-Drawer. Players who want lore get lore. Players who don't never have to open it. The collectibles tell *parallel* stories — local news clippings, fictional brand ads, a campaign button for a fake 1976 politician.

**5. THE TV (cultural ambient — opt-in deep dive)**
The Marek living room TV plays all day. Parody-1976 shows we wrote. Parody commercials. The local news. If Mark sits in front of it, the player can watch fake-period programming for as long as they want. This is where the F-is-for-Family parody-brand pillar gets loud.

**6. THE RADIO (ambient music, deep deep cuts available)**
The kitchen radio. The car radio on the Ocean Side trip. The boombox on the boardwalk. Parody-70s songs by parody-70s bands. Optional: player can switch stations (AM/FM/Polish-language). Each station carries different era weight.

**7. THE NOTEBOOK CATALOG (the spine of teaching)**
Every item picked up, identified, and used gets a catalog entry. **This is where the educational layer crystallizes.** Players can later browse: every dangerous toy they touched, every household chemical, every banned product. By the end of the game, the player has — *without ever sitting through a cut-scene* — a personal anthology of 1976's most-likely-to-kill-you childhood artifacts. With Mark VO commentary on each.

### Two-audience design rule (LOCKED in story-arc Cross-Cutting Anchors)

Every era beat should land for BOTH:
- **Gen X (Mark's age):** *"Oh god I forgot about that!"* — remembering.
- **Gen Z / younger:** *"Wait, you actually DID that?"* — discovering.

We test every era moment against this. If it only lands for one audience, it's a weak beat. The 8-track in the Kowalski station wagon: Gen X sighs in recognition, Gen Z asks why the music keeps cutting out mid-song. Both reactions are correct. Both are the joke.

### What this means for the parts list

**Every machine part should be a TEACHING MOMENT.** When we go to design `machine-rules.md`, the rule is: a part is only a good part if its acquisition teaches the player something true about 1976 they didn't know (or had forgotten). Gilbert U-238 is the model — a real toy, sold for years, with real radioactive material, that doubles as Component A.

Mark's banned/toxic toys list is going to feed this directly. Most parts on the machine will literally BE toys from that list.

---

## What this loop DOES NOT include (scope discipline)

- ❌ Combat. None.
- ❌ Stealth. Maybe one micro-puzzle (sneaking the beer past Kay in Act 2 was a one-off, not a system).
- ❌ Survival meters. No hunger, no thirst, no sleep meter. Day rhythm handles cadence.
- ❌ Real death. Mark cannot die.
- ❌ Open world. We have zones (16-node map cap in Acts 1-2, Ocean Side hub in Act 3).
- ❌ XP / leveling. Knowledge is the progression curve.
- ❌ Multiple endings. One story, one ending. (Disco Elysium has multiple endings; we don't need them and they'd kill the Lamborghini reveal.)
- ❌ Romance system / choices. The Iwona arc is *authored*, not branched. Mark cannot date Mickey.

---

## What we need to build to make this real (the path forward)

In order, the docs we need next:

1. **`writing/era-research/banned-toys.md`** — Mark's banned/toxic toys list, captured raw. Source material for parts list AND era teaching.
2. **`writing/era-research/kid-culture-70s.md`** — Mark's other 70s notes: slang, games, music, TV, social rules. Source material for NPC dialog, conversational friction, ambient world.
3. **`writing/machine-rules.md`** — physics + 8-12 machine parts + Tear mechanics + comms-notebook rules. Each part = one toy/object from the banned list + one mini-quest.
4. **`writing/quests.md`** — per-act mission spine. Each part-acquisition is a quest. Plus the social quests (block reputation), the romance beats (authored), the era-teaching set-pieces.
5. **First Ren'Py vertical slice** — pick ONE quest from Act 1 (probably the easiest part to acquire). Implement: bedroom → bike → scavenge → identify → return → craft → install. Prove the loop works in code. Iterate from there.

**Suggested next session:** Mark dumps the banned-toys list into `era-research/banned-toys.md`. Clawpilot structures it: name, year, what it actually did to kids, what it would do in our game (PART / TRADE GOOD / HAZARD / LORE), comedic angle, and which Act it might appear in.

That list is gonna write the next three documents almost by itself.

---

## Open questions for Mark

1. **HUD philosophy.** Vote: how minimal? My recommendation: **almost none.** Notebook is the only "menu." No on-screen health bar, no reputation bar, no Tear meter, no day-time HUD. Confirm or push back.
2. **Save system.** Auto-save on day transition? Manual save anywhere? My rec: auto-save on streetlight + on entering bedroom.
3. **Notebook UI.** Real flippable paper notebook (like a physical object in 3D), or stylized 2D overlay? Affects art workload.
4. **Workbench style.** A simple recipe-list with "craft" button, or an actual fiddly playable mini-game (drag wires to terminals)? My rec: simple in v1, fiddly later if we want.
5. **Block reputation visibility.** Truly invisible, OR very subtle text cues ("Mickey doesn't seem to want to talk right now")? My rec: very subtle text cues, never a number.
6. **Are we cutting any of the five core verbs?** Five is already a lot for an indie scope. Could we collapse INSTALL into CRAFT? My rec: no — INSTALL is the *moment* the player feels progress, and that emotional beat is worth keeping its own verb.
