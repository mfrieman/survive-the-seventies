# Decisions Log

> Chronological record of major creative decisions for *Survive the 70s*. Each entry: what was decided, why, what it locks in, what it opens up. New AI assistants reading this should understand the whole creative trajectory of the project in one file.
>
> **Conventions:**
> - Newest at top.
> - Tag with `[LOCKED]` (committed to canon), `[STAGED]` (proposed, pending Mark's review), `[OPEN]` (under discussion), `[REVERSED]` (decided then changed).
> - Cross-reference the canon doc that holds the full version.

---

## 2026-05-24 (late morning)

### `[LOCKED]` Day system — streetlight ends the world, bedroom is untimed sanctuary

Mark's design instinct from `schedule 1`'s timing mechanic: separate the **timed daytime world** from the **untimed bedroom phase** so novice players have a sanctuary to think and act without time pressure.

**The structure:**

1. **Daytime (timed).** Streets, errands, Burnsville Electronics, Halloran's porch, the corner store, lawn-mowing routes, payphone scrounging, friend visits. **Each action consumes a block of time.** The world advances. Possible end-of-day triggers:
   - **Mom yells from the porch** ("MAAAARK! DINNER!") — diegetic, period-perfect, breaks any task immediately. Required mechanic.
   - **Streetlight comes on** — the universal 1970s "be home" rule. Overhead shot, kids in the street, sodium-vapor orange flicker as the lamp warms up, neighborhood quiets. **This is the canonical end-of-day cinematic.** Locked.
2. **Bedroom phase (untimed).** After the streetlight beat, the player transitions to Mark's bedroom. **Time does not advance until Mark chooses to go to sleep.** In the bedroom Mark can:
   - Work on the machine (CRAFT, install components)
   - Read the Book / new entries from Danny
   - Count the change jar (UI counts cash)
   - Make Tear stabilization decisions (Tier 1 wait, Tier 2/3 if scripted)
   - Reflective beats (the chair, the beer, journaling, Mark VO)
   - Review inventory, plan next day
3. **Sleep = next day.** Player chooses when to advance.

**Why this works:**
- **Novice players have breathing room.** No clock ticking in the sanctuary. Take all the time you need.
- **The streetlight beat is golden** — period-accurate, recognizable, no UI text needed.
- **Mom's porch yell handles interruption** comedically and accurately.
- **Mark VO has a natural home.** Bedroom is where reflection lives. Where the beer-in-the-chair cutscene goes. Where the 2026-Mark interiority lands without disrupting daytime pacing.
- **Tear stabilization happens at home.** Story-natural — the Book is here, the machine is here.

**Time budget reality:**
The story spans **summer 1976 → July 4 ending.** Roughly **35 in-game days** from school's-out to the Bicentennial. The day system has to fit inside this budget. Bedroom phase being untimed means we don't burn days on player indecision. Tier 1 Tear waits will be calibrated in **streetlight transitions, not 24-hour days** (see Tear system doc for detail).

### `[STAGED]` Tear system (revised) — see `components/tear-system.md`

Per long discussion with Mark this morning: pulled back from the original "burn an item to stabilize" Tier 1 mechanic because it would trigger hoarding anxiety in the casual / older-novice player (the Mark Test). Replaced with **time-based stabilization** for the recurring tier. Kept the **memory burn** but moved it to a SINGLE scripted moment near the climax (Mark alone in his bedroom, not at the machine with Iwona — she still does not know about the machine per locked premise).

Full system in `components/tear-system.md`. Marked STAGED, not LOCKED — Mark wants to live with it before committing.

### `[LOCKED]` Burnsville Electronics — the hobby shop (tribute to real-world Baynesville)

Mark's hometown had **Baynesville Electronics**, a regional hobby-electronics store with real local fame that closed in 2024. The in-game equivalent is **Burnsville Electronics** — one syllable off, preserves the rhythm, and "Burn" works on three levels (solder smell, the always-too-hot iron, the rite-of-passage burned-finger). Locals from Mark's area will recognize the homage immediately; everyone else just gets a credible 1976 hobby shop name.

**Canon role:**
- Recurring location where Mark buys the **machine backbone parts** (chassis, perfboard, transformer, hookup wire, solder).
- Has a **tube tester** at the counter (real era detail).
- Has **salvage / surplus bins** in the back (cheap parts, sometimes the only source for an oddball component).
- Owner is a **future named NPC** — kept generic for now (`[BURNSVILLE-OWNER]`). When we cast him, he becomes the "doesn't ask what kids are building" type with a soft spot for kids who actually solder.

**Hidden VO opportunity (Act 2 or 3):** Mark leans in the doorway and thinks *"This place lasts almost fifty years. Almost. I won't tell him."* The whole game in one line.

**Tone rule:** Burnsville is treated with affection, not parody-cruelty. The store is one of the *good things* about 1976 that doesn't survive. It earns the small ache when the player thinks about it later.

### `[LOCKED]` Machine has a real backbone — hobby-shop chassis + 10 toy components

The machine is not just 10 toys taped together. It has a real-world plausible 1970s hobbyist chassis underneath, sourced from **Burnsville Electronics**. The 10 toy components are mounted/soldered onto that backbone.

**Backbone parts (cash-gated, hobby-shop sourced — NOT quest-gated like the 10 toys):**

1. **Aluminum chassis project box** — the frame
2. **Perfboard / vectorboard** — the "motherboard," toy components solder to this
3. **Power supply guts** (transformer + rectifier + filter cap) — converts 120V wall AC to DC. Player can buy new OR salvage from a curbside broken TV (free, optional subquest)
4. **Hookup wire + rosin-core solder** — consumables, recurring cash drip

**Why this matters:**
- Machine looks *almost-plausible* — aluminum box, perfboard, soldered toy parts, wall plug. Comedy lives in the *combination,* not the impossibility.
- 2026-player recognizes the hobbyist form factor — feels real.
- Burnsville becomes a recurring location with a real reason to revisit.
- Money pressure layer is REAL now — kid-economy quests (payphone coin return, lawn mowing, can returns) funnel into Burnsville cash.
- Teaches the era's **repair-don't-replace** ethic via the TV-salvage option.

Full detail: `era-research/hobby-electronics-1976.md` + `components/backbone.md`.

### `[LOCKED]` No stealing — except chrome caps off trucks

Mark: *"No stealing except for Chrome caps from trucks. This needs to be a rule. If a friend has a slinky I don't just want to steal it and fulfill the quest."*

**The rule:**

- **Mark does not steal from people.** Not friends, not neighbors, not store owners, not strangers. No pocketing a Slinky off the Karras coffee table, no lifting candy from McCrory's, no "borrowing" a wallet.
- **The single exception is the chrome valve-stem caps off parked trucks** — a real, near-universal 1970s kid ritual. Period-accurate, victimless-feeling at kid-scale, and culturally specific. This stays in.
- **TRADE replaces theft as the friction mechanic.** If a friend has the Slinky, Mark *trades* for it (kid-economy: baseball cards, candy cigs, comics, favors, info). If no one will trade, Mark earns one (chores, find one buried in the alley, win one in a bet).
- **The "easy" components are still real challenges** — they're acquired through *social negotiation*, not violence or theft. That IS the gameplay.
- **Story consequence:** Mark from 2026 is a decent person and a future PO. The protagonist who runs the machine that saves both timelines doesn't get there by being a sneak thief. The moral throughline matters because the Tear costs are about *what kind of person* survives the swap.

This locks **TRADE as the dominant Act 1 mechanic** and removes a whole category of cheap-feeling quest solutions. machine-rules.md and quests.md must reflect this: no acquisition path may be "steal it."

## 2026-05-23 (late evening)

### `[LOCKED]` Scope targets — tight and fun, people will complete

Mark: *"I like a tight and fun game people will complete."* Agreed and locked.

- **Target core playtime:** ~5 hours. Skill band ~4-6 hours. Completionists with optional side content: ~6-7.
- **~10 machine components.** Each one a real challenge using ≥1 of FIND/TRADE/EARN/CRAFT.
- **~15 NPCs total.** Add only when a quest needs one. No speculative casting.
- **~8-10 locations.** Same rule. Mark has a list of ~20 candidates; we pick on-demand.
- **No filler.** Every scene must (a) advance the machine, (b) advance the romance, or (c) teach the era. If none — cut.
- **Comedy first.** Pacing > length. A Carlin-energy adventure has to move.

This protects a first-game-ever side project from development hell and protects the comedy from dilution.

### `[LOCKED]` Tone rule — pre-PC, but lines we don't cross

Mark's direct words: *"I want pre-PC but there are still lines we don't want to cross."*

This refines the earlier locked comedic lineage (Carlin / Pryor / Cheech / Robin Williams / *Married with Children* / *F is for Family*). We push at lines. We occasionally cross them. **We do not put hateful slurs in the player's mouth, and we do not use the protagonist's narration as a vehicle for cruelty.**

**Working principles:**

1. **The era is the source of the edge, not us.** Period-accurate adult/teen cruelty — racial, ableist, homophobic, misogynist — *existed.* The game can witness it. It doesn't celebrate it.
2. **Mark from 2026 is our conscience.** He's the audience proxy. He hears 1976 talk, and his Mark VO reaction is the comedy *and* the moral signal. The joke is usually his recoil.
3. **NPCs can say things Mark won't say.** Hard-edge NPCs (Mickey-type, older kids, certain adults) carry the period-accurate language. Mark notes it. Mark doesn't join in.
4. **No slurs in player choices.** The dialog wheel never asks the player to *pick* the slur. We never give the player that line.
5. **No punching down at fixed targets.** Casual cruelty in 1976 was directed at specific real groups. We can show it happened; we don't make any of those groups the *recurring* butt of the joke. The butt of the joke is almost always *the 1970s itself.*
6. **Edge for substance, not shock.** Every hard moment should *teach something true* about the era. If it doesn't, cut it.
7. **Mark (the author) is the final tone arbiter.** When in doubt, Clawpilot flags the beat and asks before writing it. Default = ask, don't assume.

**What this means in practice:**
- The "short bus" beat (quest-seeds.md SEED 8) follows this rule: Mickey says it casually, Mark recoils, scene moves on. No slurs in Mark's narration. One scene, not a recurring bit.
- Smoking, drinking, pot, sex jokes, body-comedy, religious humor, casual property crime, parental neglect, adult incompetence — all in bounds. These are *the era,* not punching down.
- Any slur that ends in "-ist" today gets flagged before drafting. Clawpilot asks before writing.

**Cross-references:**
- `quest-seeds.md` SEED 8 (short-bus tone call)
- `decisions-log.md` earlier entry on comedic lineage (Carlin/Pryor/Williams etc.)
- All future scene drafting

---

## 2026-05-23 (afternoon)

### `[LOCKED]` Future-kid name — Mark Cole

Mark wants his real first name used for the protagonist (the future-kid consciousness who wakes up in Danny's body). Surname is **Cole** — explicitly NOT Mark's real surname (Frieman), to keep the character one degree removed from the author. Options pitched: Walsh, Doyle, Reilly, Sutton, Halloran, Pemberton, Vance, Day, Cole, or leave TBD. Mark picked Cole.

**Naming convention going forward (do not collapse):**
- **Mark** = the future-kid consciousness (the player).
- **Danny** = the 1976 host consciousness.
- 1976 cast says "Danny" to the player (they see Danny's body).
- 2027 cast says "Mark" to the real Danny (they see Mark's body).
- Narrative voice, UI, and design docs should always distinguish them.

The duality is load-bearing for the body-swap premise and the Soul-Not-Body thematic pillar.

**Canon:** `writing/premise.md` → "The Future-Kid" section; `writing/intake/people.yaml > mark-cole`.

---

## 2026-05-22 (evening)

### `[LOCKED]` Romance Arc — Iwona Kowalski

Mark introduced a love-story arc layered onto the body-swap premise. **Iwona is based on Mark's real wife of 30+ years (a Polish immigrant, also named Iwona).** Mark's explicit intent: *"I want to fall in love with her again in this story."* Iwona-the-real-person is aware of and happy about the project.

The Kowalski family is a Polish family on the block (Zone 1). Members: Jack (father, electrician, hidden alcoholic), Mary (mother, stylish "European" homemaker), Natan (19, charismatic, into clothing design — sexuality canonically ambiguous), Jacob (15, intelligent introvert with dark humor, troublemaker, looks up to Natan), Maggie (Mary's senile-but-nice mother), Peter (Jack's brother, just arrived from Poland — musician/painter/engineer renaissance man), Eva (Peter's wife), and **Iwona (16)** — the love interest. (Renamed Gorski → Kowalski 2026-05-23 to avoid using a real friend's name.)

**Why this works structurally:**
1. Iwona arrives DURING the game (moving van, Option B). She has no prior relationship with Danny → Mark can be fully himself with her because she has no Danny baseline. Solves the cover-blowing problem.
2. She's the only safe space in 1976 where Mark doesn't have to perform.
3. Sets up the parallel Danny-in-2027 romance with Sylvia, which enables the ending twist.

**Open (pending Mark):** Iwona's specifics (mannerisms, phrases, signature objects), her knowledge of the machine (5 levels staged, leaning A2+A3 hybrid), first kiss location (5 options staged, leaning B2 basement dance lesson).

**Canon:** `writing/premise.md` → "The Romance Arc" section.

### `[LOCKED]` Thematic Pillar 1 — Soul Not Body

Both lovers reunite in different bodies than they started. Mark fell for Iwona-in-Iwona's-body. Iwona fell for Mark-in-Danny's-body. At the ending, Iwona returns in Sylvia's body. Neither lover is in their original body. The game's body-swap mechanic earns this thematic resolution — love is the soul, not the meat. Never preached; just present.

**Canon:** `writing/premise.md` → "Thematic Pillars" section.

### `[LOCKED]` Thematic Pillar 2 — Shared Otherness (Fish-Out-of-Water Squared)

Both lovers are fish-out-of-water. Mark from 2027. Iwona from Poland. Shared otherness is the foundation of their intimacy. They recognize each other's loneliness before they have words for it. The language thing becomes intimacy currency.

**Endgame inversion:** When Iwona shows up in Sylvia's body in 2027, she's the fish now and Mark is home. The whole game has been Mark learning her world; the ending is Iwona learning his. **Love symmetric across time.**

**Canon:** `writing/premise.md` → "Thematic Pillars" section.

### `[LOCKED]` Ending Twist — Iwona-in-Sylvia

Original ending: 65-year-old billionaire Danny shows up in a Lambo, pays out the long con.

**Extended:** Mark asks if Danny destroyed the machine for good. Danny: *"I did. But it happened again."* It turns out Danny fell in love in 2027 with Sylvia (Iwona's granddaughter). Decades later, Iwona and Sylvia swap. Iwona-the-young (mind) arrives in 2027 in Sylvia's 16-year-old body.

Closed time-loop / bootstrap paradox — Sylvia grows up to BE the grandmother she descended from. Mark's head explodes. Danny: *"Don't blow up your brain. You have a Lamborghini and your Iwona is here now and has a driver's license. How about you two go for a drive."*

Cut to black.

**Canon:** `writing/premise.md` → "Ending Twist" subsection of Romance Arc.

---

## 2026-05-22 (afternoon)

### `[LOCKED]` Intake Schema — YAML files

Mark (Director of Engineering, schema-fluent) requested structured intake instead of unstructured prose for the world-building dump. We built `writing/intake/*.yaml`:

- `people.yaml`, `places.yaml`, `things.yaml`, `media.yaml`, `customs.yaml`, `banned-or-gone.yaml`, `stories.yaml`
- Schema embedded as YAML comments at top of each file
- Universal conventions: `id`, `reality` (real/mixed/fake/parody), `change_name`, `audience` (gen_x/gen_z/both), `tags`, `notes`

**Workflow:** Mark dumps prose or speech → I structure into YAML → Mark fine-tunes → batch-process distributes into canon docs (`world-map.md`, new `cast.md`, new `era-toolbox.md`, etc.).

**Canon:** `writing/intake/README.md`.

### `[LOCKED]` Comedic Lineage

Pre-PC observational comedy. Mark's stated touchstones: George Carlin, Cheech & Chong, Robin Williams, Richard Pryor, Married with Children. Push hard at lines, occasionally cross them, no cancel-culture fear. Smart edge, not shock for shock's sake.

**Canon:** `writing/bible.md` (existing tone rules align — this elevates the lineage explicitly).

### `[LOCKED]` Two-Audience Design

Every era detail should ideally serve two audiences:
- **Gen X (Mark's age):** *"Oh god I forgot about that."* Nostalgia.
- **Gen Z (kids today):** *"Wait, you actually DID that?"* Cultural-distance comedy.

Examples: 8-tracks, needle wear on records, newspaper vending machines, checking phone booth coin returns, tin foil on TV antennas.

**Canon:** All intake YAML files have `audience` field. `writing/era-toolbox.md` (when created) will categorize by audience.

### `[LOCKED]` Initial Premise — Body Swap

The core story:
- Modern teenager wakes up in 1976 in the body of Danny Marek.
- Danny is a **stealth genius** (load-bearing trait) who hides his intelligence so adults leave him alone. This is why future-kid can fumble Danny's life and friends/family attribute it to "Danny being Danny."
- Danny built a body-swap machine, planned a quick "get rich off the future" trip. Machine broke. Both stuck.
- Future-kid is from **somewhere vague** — no specifics. Allows player projection. Solves the "future-kid knows the town" problem.
- The Book (Danny's notebook) is the central artifact: tutorial, save menu, hint system, eventually mid-Act 2 quantum-paired comms with Danny in 2027.
- Both kids want the **Lou Dorchen** ending (not Doc Brown reluctance). They become co-conspirators.
- 4-5 long-con favors, optional but for full ending.
- Hint system: diegetic, 4 tiers per puzzle (Nudge → Direction → Method → Solution), snarky Danny commentary per tier, no mechanical penalty.
- 4-5 hour playtime, 7 machine parts, 3 acts.
- Ending: billionaire Danny in a Lambo, payout, emotional friendship beat. *"You were the best friend I ever had, kid. I told my wife about you. She thinks I made you up."*

**Canon:** `writing/premise.md`.

---

## 2026-05-21 (evening)

### `[LOCKED]` Game Engine — Ren'Py

Chosen for: easiest concept-game tooling for Mark's first game project, Python-friendly, supports hotspot-based exploration in addition to pure VN style. Mark wants Beavis & Butt-Head Virtual Stupidity-style interaction; Ren'Py can deliver this via `imagebutton` / `imagemap`.

**Canon:** `HOW-TO-RUN.md`, `game/options.rpy`.

### `[LOCKED]` Setting — Old Bay County, MD (fictional)

Fictional Maryland county, Baltimore-shaped. Lets Mark mine real Baltimore County childhood material without legal/literal constraints. Name is the joke (Old Bay seasoning = Baltimore).

Three zones: Zone 1 (the block / Linden Drive), Zone 2 (town / Old Bay), Zone 3 (destinations: Storybook Hollow, Ocean Side, Chocolatetown, Glen Hollow).

**Canon:** `writing/world-map.md`.

### `[LOCKED]` Parody Universe (F-is-for-Family-style)

Every real-world brand, band, movie, product, franchise gets a fake in-game equivalent. KISS → BLAZE, Star Wars → Super Star Adventures, Mongoose → ?, 7-Eleven → Quik-9, Trimper's → Stomper's, etc. Sidesteps copyright AND sharpens the comedy.

**Canon:** `writing/world.md`.

### `[LOCKED]` Protagonist Age — 14

Originally seeded at 9. Mark moved it to 14 to enable: joyriding, mild drinking, weed, dating, dating risks, the cool-older-kid dynamic, dangerous self-led adventures. Protagonist is old enough to make stupid choices and live with them; young enough that adults still control the world.

**Canon:** `writing/premise.md` (Danny age 14), `writing/bible.md`.

### `[LOCKED]` Tone — Not Politically Correct, Pre-PC

Period-accurate peer-to-peer slurs allowed (retard, spaz, queer, fag as 1970s schoolyard insults). N-word NEVER. No sexual content with the 14yo. Drugs/booze always have consequences (the fun is in *getting* them, not consuming). Narrator never says slurs — narrator is adult-Mark in 2026 wincing at the memory. Kids say slurs peer-to-peer in period-realistic dialogue.

**Canon:** `writing/bible.md` "Tone Bright Lines" section.

### `[LOCKED]` Repo Location and Remote

Repo: `C:\ai-game\survive-the-seventies\`
GitHub: `https://github.com/mfrieman/survive-the-seventies` (Mark's personal account `mfrieman`, NOT the Microsoft enterprise account `mafriema_microsoft`).

---

*This log is the chronological source of truth for "why is this the way it is?" Future AI assistants: read this BEFORE making creative changes. If a decision seems wrong, ask Mark — don't override.*
