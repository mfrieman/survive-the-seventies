# Machine Rules — v0.2 PROPOSAL (FIRST DRAFT)

> **Status:** FIRST-PASS PROPOSAL — 2026-05-26.
> **Authority:** None yet. This document does NOT supersede `machine-rules.md` (v0.1) or `components/index.md` until Mark explicitly locks it.
> **Purpose:** A clean staging ground so Mark can propose swaps, push back on individual slots, and play "what if I replaced X with Y" without disturbing the v0.1 spine.
>
> **How to use this file:** Each component below has a `VERDICT:` line at the top. Mark edits it in place — `OK` / `REPLACE WITH ___` / `REWORK` / `CUT`. Once every line says `OK` we promote the table into `machine-rules.md` as v0.2 and update `components/index.md`.

---

## What changed vs v0.1

Three locked decisions from the 2026-05-26 review session:

1. **10 components → 12 components.** Two new slots added: `O` (Foot X-Ray fluoroscope) and `Amb` (amber-with-inclusion). Reasoning: the previous 10 was felt to be too thin for an adventure-game pacing target, and Mark explicitly wants both uranium AND amber as full mechanical members of the spine (uranium = power source, amber = soul-targeting — different functional slots, no conflict). Per the 2026-05-25 memory lock, amber is the ONE component Danny could not pre-stock, so it must be a quest.
2. **Quest-type taxonomy introduced.** Every component is now tagged as `IDENTIFY` / `RECOVER` / `ACQUIRE` (see definitions below). Target mix is **2 IDENTIFY + 3 RECOVER + 7 ACQUIRE**. This solves the box-vs-quest math: box-resident parts are still gameplay (Act 1 detective work), they just use lighter mechanics than full quest chains.
3. **Three v0.1 components changed:**
   - **F (Clackers pendulum)** → replaced with **Polaroid SX-70 battery pack** as a "stored charge cell." Clackers stay in the world as HAZARD/TRADE flavor but are no longer a machine part.
   - **B (vacuum chamber)** → ungated from Gilbert glass-blowing. Primary source is now a **mason jar + Gilbert bell jar** (no blowing required). The Gilbert kit stays as Act 2 atmosphere/optional flavor.
   - **L (soldering iron)** → reclassified from light-FIND to RECOVER (wood-burning kit is in basement but missing/broken tip — first Burnsville trip is the recovery quest).

Everything else in v0.1 carries forward unchanged.

---

## Quest type definitions

| Type | What the player does | Stat cost | Mini-game style |
|---|---|---|---|
| **IDENTIFY** | The part is **already in the Box of Leftovers, intact**. The mini-quest is figuring out *what it is*, *what it's for*, and *where it goes on the Blueprint*. | Mostly Knowledge gates + 1-2 NPC conversations. Low Energy/Money/Cover. | Detective work: cross-reference Danny's notes, ask Stan at Burnsville, read the era notebook. |
| **RECOVER** | The part **exists somewhere accessible** but is broken, missing a sub-component, or needs reactivation. The mini-quest is *repair or completion*. | Light real-world acquire — half a quest. One trip, one trade, one CRAFT step. | Hybrid detective + acquisition. |
| **ACQUIRE** | Full quest chain — **Identify → Locate → Acquire → Verify**. Multiple NPCs, multiple beats, sometimes multiple zones. | Full mini-game + cash/cover/energy stakes. | The "main course" puzzles. |

---

## The 12 — proposed roster

| # | Component | Source | Type | Act | Tear impact | Verdict |
|---|---|---|---|---|---|---|
| L | Soldering iron (workbench enabler) | Wood Burning Kit (basement, broken tip) | RECOVER | A1 | none | OK |
| J | Primary coil | Slinky (in box, kinked) | IDENTIFY | A1 | small | OK |
| F | Stored charge cell | Polaroid SX-70 battery pack (in box, leaky) | IDENTIFY | A1 | small | OK |
| C | Grounding spike | Lawn Dart tip (Dennis's garage) | ACQUIRE | A1→A2 | small | OK |
| N | Mercury switch | Broken thermometer (medicine cabinet) | RECOVER | A2 early | medium | OK |
| B | Vacuum vessel | Mason jar + Gilbert bell jar (no glass-blowing gate) | RECOVER | A2 | medium | OK |
| K | Rotational bearing | Swing Wing hub | ACQUIRE | A2 | large | OK |
| O | **Fluoroscope HV tube + viewport** (NEW) | Shoe-store back room (Zone 2) | ACQUIRE | A2 late | large | OK |
| G | Ignition primer (HERO) | Cap-gun caps + Austin Magic Pistol carbide | ACQUIRE | A2 | large | OK |
| M | Comms crystal (HERO) | CB Radio (Cobra 29 / Realistic TRC-447) | ACQUIRE | A2 late | **SEVERE** (mask-drop) | OK |
| A | Uranium core (CAPSTONE) | Gilbert U-238 Atomic Energy Lab (Ocean Side antique) | ACQUIRE | A3 | **CATASTROPHIC** | OK |
| **Amb** | **Amber-with-inclusion (SOUL CAPSTONE)** (NEW) | Iwona's necklace + Pirate's Cove UV blacklight authentication | ACQUIRE | A3 | (TBD — pair with A?) | OK |

**Type mix:** 2 IDENTIFY · 3 RECOVER · 7 ACQUIRE = 12.

**Act distribution:** A1 = 4 (L, J, F, C started) · A2 = 6 (C finished, N, B, K, O, G, M) · A3 = 2 (A, Amb).

---

## Per-component spec (one paragraph each)

Each entry below uses the same shape so swap-ins are mechanical:

> **VERDICT:** OK / REPLACE WITH ___ / REWORK / CUT
> **Source:** the 1976 object
> **In-machine function:** what it physically does
> **Type:** IDENTIFY / RECOVER / ACQUIRE
> **Act / position:** when it fires
> **Believability note:** how it passes the 4-question test (kid-knowable / sourceable in '76 Long Island / serves a clear function / signposting works)
> **Dependencies:** what must be installed first / what it enables
> **Tear impact:** none / small / medium / large / severe / catastrophic

---

### Component L — Soldering iron

> **VERDICT:** OK
> **Source:** Wood Burning Kit (basement, found but with broken/missing wood tip — first Burnsville trip is to replace it)
> **In-machine function:** Not a part. Unlocks the workbench / CRAFT mechanic.
> **Type:** RECOVER
> **Act / position:** A1 first install
> **Believability note:** Wood-burning kits were sold to children for $5; every basement had one. The "broken tip" recovery beat teaches the Burnsville pipeline early.
> **Dependencies:** None. Enables all subsequent CRAFT steps.
> **Tear impact:** none

---

### Component J — Primary coil

> **VERDICT:** OK
> **Source:** Slinky (in the Box of Leftovers, kinked from years in storage)
> **In-machine function:** Primary induction coil around the central housing.
> **Type:** IDENTIFY (part is already in the box; mini-quest is figuring out what Danny pre-stocked and that the kinked Slinky IS the coil)
> **Act / position:** A1 second install — first machine hum.
> **Believability note:** A Slinky IS a coil. Every kid knows what a Slinky is. Perfect "aha" moment.
> **Dependencies:** L installed (need CRAFT to un-kink and re-tension the helix).
> **Tear impact:** small (first tick)

---

### Component F — Stored charge cell *(REPLACES v0.1 Clackers pendulum)*

> **VERDICT:** OK
> **Source:** Polaroid SX-70 battery pack — included in every SX-70 film cartridge; Danny pre-stocked a partly-used cartridge in the Box. (Polaroid SX-70 was 1972, peak 1976.)
> **In-machine function:** Provides the initial stored charge that primes the ignition circuit. The cartridge's flat polymer battery is exactly the right form factor for what a teen genius would scavenge.
> **Type:** IDENTIFY (already in box; mini-quest is realizing the "film cartridge" is also a battery and the chemistry hasn't gone off)
> **Act / position:** A1 third install.
> **Believability note:** Real — every SX-70 cartridge contained a flat battery. Strong era-teaching beat (most modern players don't know this). Mark VO: *"Polaroid put the battery in the film. They put a literal battery in the film. So you'd buy more film."*
> **Dependencies:** L installed.
> **Tear impact:** small
> **Replaces:** v0.1 F (Clackers pendulum). Clackers remain in the world as HAZARD/TRADE flavor — Bobby has a pair, parents took them away, they show up in a corner-store memory beat — but are no longer a machine component. Reasoning: Clackers' "pendulum mass" function was mechanically vague and overlapped with K. The SX-70 battery has a clearer functional category and stronger comedy.

---

### Component C — Grounding spike

> **VERDICT:** OK
> **Source:** Lawn Dart (Jart) steel tip — Dennis next door has a set in the garage.
> **In-machine function:** Earth ground / discharge path. Without this the rig holds a static charge and cannot fire safely.
> **Type:** ACQUIRE (full quest — surveillance of Dennis's garage routine, low-Cover acquisition, then trade/EARN if confronted)
> **Act / position:** A1 starts the quest, A2 early completes it.
> **Believability note:** Jart tips are genuinely forged steel spikes. Banned in 1988 after killing kids. The "kids casually launching steel spears" beat IS the era teaching.
> **Dependencies:** L installed; preferably J installed (Mark needs to know what the machine sounds like with no ground).
> **Tear impact:** small

---

### Component N — Mercury switch

> **VERDICT:** OK
> **Source:** Broken bathroom thermometer — Bobby drops it in a comedy beat (Mark watches the silver bead roll under the sink with horror), Mark recovers the mercury.
> **In-machine function:** Tilt-activated switch — triggers the discharge moment when the central housing reaches true vertical.
> **Type:** RECOVER (the source exists in the medicine cabinet; recovery is the quest)
> **Act / position:** A2 early.
> **Believability note:** Mercury thermometers were universal in 1976. The horror of "Bobby thinks it's a prize" is the era teaching beat.
> **Dependencies:** L, B (mercury needs to be sealed in a glass capsule sourced from B's bell jar fragments).
> **Tear impact:** medium

---

### Component B — Vacuum vessel *(REWORKED from v0.1)*

> **VERDICT:** OK
> **Source:** Standard mason jar (kitchen) + Gilbert Glass-Blowing Set bell jar (basement). Hand-pump vacuum sealer from the kitchen drawer.
> **In-machine function:** Central chamber housing the U-238 core. Holds vacuum during the discharge event.
> **Type:** RECOVER (sourcing all three pieces, fitting them, sealing the rig)
> **Act / position:** A2.
> **Believability note:** Mason jars + bell jars are real, kid-accessible, no glass-blowing skill required. The Gilbert kit appears as a SET PIECE in Act 2 atmosphere — Mark VO can rant about it, Bobby can almost burn the house down using it — but it is NOT a gate on B. This unblocks the design.
> **Dependencies:** L, J. Enables N (need bell jar fragments to seal mercury) and A (the vessel must exist before the core can be installed).
> **Tear impact:** medium
> **Replaces:** v0.1 B (Gilbert glass-blowing as the gate). The Gilbert set stays as a candidate prop / Act 2 hazard but does not bottleneck core machine progress.

---

### Component K — Rotational bearing

> **VERDICT:** OK *(but: see open questions — this slot is the most-likely target for Mark's new idea)*
> **Source:** Swing Wing hub (1976 toy — twirl the wings to make them fly off).
> **In-machine function:** Allows the central housing to rotate freely during alignment.
> **Type:** ACQUIRE
> **Act / position:** A2.
> **Believability note:** Swing Wing was a real toy with a genuine ball-bearing hub. Slot is mechanically real but the *function* slightly overlaps with F (kinetic) — flagged as the weakest believability fit on the spine.
> **Dependencies:** L, J.
> **Tear impact:** large
> **Open question:** If a stronger candidate appears in Mark's research, this is the first slot to consider swapping.

---

### Component O — Fluoroscope HV tube + viewport *(NEW)*

> **VERDICT:** OK
> **Source:** Shoe-fitting fluoroscope — a real 1930s-1960s device, mostly banned by 1970 but still findable in old shoe-store back rooms in 1976. Contained a Coolidge X-ray tube, a fluorescent screen, and a wooden cabinet with 3 viewing ports.
> **In-machine function:** Two things — (1) the Coolidge tube provides the focused high-voltage rectifier needed for the targeting field; (2) the fluorescent screen becomes the machine's visualization output (Mark can finally SEE what the field is doing).
> **Type:** ACQUIRE (Zone 2 quest — Stan at Burnsville knows a shoe-store owner whose dad never threw it out)
> **Act / position:** A2 late.
> **Believability note:** Real device. Real X-ray tubes. Real shoe-store horror. Mark VO gold: *"This was in shoe stores. You could put your foot under it. As many times as you wanted."*
> **Dependencies:** L, J, C (need ground before HV).
> **Tear impact:** large
> **Why it slots in:** Solves a previously-unsolved UX problem (no current component lets Mark visualize the field). Strong period-horror beat. Sets up the Act 3 capstone visually — once O is installed, when A goes in, the player can see the reality-bridge field form.
> **NEW vs v0.1:** Did not exist as a component before.

---

### Component G — Ignition primer (HERO)

> **VERDICT:** OK
> **Source:** Two-source quest — cap-gun caps (corner store, easy) + Austin Magic Pistol calcium carbide (basement of a war-vet neighbor at the end of the block — long quest with NPC investment).
> **In-machine function:** "What strikes" — the ignition / discharge moment.
> **Type:** ACQUIRE (uses all four mechanics: FIND, TRADE, EARN, CRAFT)
> **Act / position:** A2.
> **Believability note:** Cap-gun caps and Austin Magic Pistol carbide are BOTH real. The Pistol fired calcium-carbide-and-spit fireballs and was sold to children in 1948.
> **Dependencies:** L, J, C, O.
> **Tear impact:** large

---

### Component M — Comms crystal (HERO)

> **VERDICT:** OK
> **Source:** CB radio (Cobra 29 / Realistic TRC-447). 1976 was the absolute peak of CB radio culture in America.
> **In-machine function:** LORE-CRITICAL. The quartz crystal + transmitter coil is the medium the Tear uses to talk to Danny across time. This is how the notebook receives Danny's messages.
> **Type:** ACQUIRE
> **Act / position:** A2 late close.
> **Believability note:** Real, ubiquitous in 1976 ("breaker 1-9, good buddy"). Strong CB-culture teaching beat.
> **Dependencies:** L, J, C, O, G.
> **Tear impact:** **SEVERE** — Comms 2 mask-drop. The machine catches fire after this install per the 2026-05-25 design lock.

---

### Component A — Uranium core (CAPSTONE)

> **VERDICT:** OK
> **Source:** Gilbert U-238 Atomic Energy Lab (1950) — sold to children with four real uranium ore samples, a polonium-210 alpha source, and a Geiger counter. Famously the most dangerous toy ever sold.
> **In-machine function:** Reality-bridge core. The "exit door."
> **Type:** ACQUIRE (Ocean Side antique store *Bayside Curiosities* — Act 3 destination quest)
> **Act / position:** A3 capstone.
> **Believability note:** Real. Even has the locked Mark/Danny exchange: *"How do we get uranium?" / "In a toy store."*
> **Dependencies:** L, J, C, B, N, K, O, G, M all installed.
> **Tear impact:** **CATASTROPHIC** — endgame.

---

### Component Amb — Amber-with-inclusion (SOUL CAPSTONE) *(NEW)*

> **VERDICT:** OK
> **Source:** Iwona's amber-with-insect necklace, bought by her in Poland before emigrating. (Per 2026-05-25 memory lock: this is the ONE component Danny could not pre-stock — amber must be GIVEN by Iwona, never purchased.)
> **In-machine function:** Soul-targeting / authentication. Pairs with the uranium core to lock the bridge onto a specific consciousness. Without amber, the machine fires blind.
> **Type:** ACQUIRE (long Act 2-3 arc — Polish-beaches banter seeds the recognition, Mark realizes amber is the missing component, Iwona offers to help find one rather than give hers up, Act 3 amber hunt in Ocean Side Polish-tourist shops fails, Iwona ultimately gives hers as the love-story climax). Pirate's Cove UV blacklight is the authentication minigame that proves the amber genuine before install.
> **Act / position:** A3 (paired with A; install order and ordering TBD).
> **Believability note:** Real Polish folklore — amber as soul-anchor across cultures. The "inclusion" (insect frozen inside) is the mystical anchor — the 10% mystical of the 70/20/10 believability split.
> **Dependencies:** Everything else installed. Amber install is the last act before A.
> **Tear impact:** TBD — pair with A.
> **NEW vs v0.1:** Did not exist as a component before. Was off-spine "Iwona's necklace" lore.

---

## Open questions to resolve next pass

1. **Install ordering for A and Amb.** Does amber install before uranium, after, or simultaneously? Design intuition: amber sets the target, THEN uranium opens the door. So Amb → A. But: does the player install Amb knowing what it's for, or is the "amber as soul-targeting" reveal saved for the moment of install?
2. **K (Swing Wing) is the weakest slot** on believability grounds. If Mark's new idea is a strong rotational/mechanical part, K is the first swap candidate.
3. **Backbone is still cash-gated separately** (Bud box, perfboard, power supply, consumables — see `components/backbone.md`). Not counted in the 12. Confirm this stays as-is.
4. **Identification mini-quests for J and F** need their own one-page design — what does the Blueprint UI show when an unidentified box-resident part is present? How does Mark "research" it (Stan / Burnsville pipeline / era notebook cross-ref / NPC conversation)?
5. **Tear cadence** with 12 parts instead of 10 — does the SEVERE/CATASTROPHIC pacing still land on M and A, or does the extra count let us spread severe-tier across M, O, and A? Currently O is "large" — could it be promoted to "severe" given the X-ray horror beat?

---

## Swap protocol — when Mark proposes a replacement

When Mark proposes a new candidate part:

1. **Name the new part and its real-world source** (toy, device, era-appropriate object).
2. **Identify which slot it would fill** by functional category (power / coil / vessel / switch / bearing / ignition / comms / output / ground / core / targeting / charge).
3. **Identify which current part it would replace** (if any) — usually the weakest believability fit in that category.
4. **Run the 4-question test** on the new candidate:
   - Could a 14-year-old plausibly know what this does?
   - Could Danny source it in 1976 Long Island?
   - Does it fit a clear functional category?
   - Does the player learn its purpose from one in-world clue?
5. **Update the VERDICT line** on the replaced part to `REPLACE WITH ___` and add the new entry below the table with its own paragraph.

Once 12 lines all read `OK`, this proposal graduates to `machine-rules.md` and `components/index.md` is updated to v0.2.
