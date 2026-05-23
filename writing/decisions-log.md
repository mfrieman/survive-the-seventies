# Decisions Log

> Chronological record of major creative decisions for *Survive the 70s*. Each entry: what was decided, why, what it locks in, what it opens up. New AI assistants reading this should understand the whole creative trajectory of the project in one file.
>
> **Conventions:**
> - Newest at top.
> - Tag with `[LOCKED]` (committed to canon), `[STAGED]` (proposed, pending Mark's review), `[OPEN]` (under discussion), `[REVERSED]` (decided then changed).
> - Cross-reference the canon doc that holds the full version.

---

## 2026-05-22 (evening)

### `[LOCKED]` Romance Arc — Iwona Gorski

Mark introduced a love-story arc layered onto the body-swap premise. **Iwona is based on Mark's real wife of 30+ years (a Polish immigrant, also named Iwona).** Mark's explicit intent: *"I want to fall in love with her again in this story."* Iwona-the-real-person is aware of and happy about the project.

The Gorski family is a Polish family on the block (Zone 1). Members: Jack (father), Mary (mother), Michael (19, older son with a car), Jacob (14, same age as Mark/Danny — possible friend/rival), Maggie (Polish grandmother), Peter (Jack's brother, just arrived from Poland), Eva (Peter's wife), and **Iwona (15)** — the love interest.

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

Three zones: Zone 1 (the block / Linden Drive), Zone 2 (town / Old Bay), Zone 3 (destinations: Cursed Forest, Ocean Side, Chocolatetown, Glen Hollow).

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
