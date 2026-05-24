# Machine Rules — The 10-Component Spine

> **Status:** v0.1 first-pass draft, 2026-05-24. Clawpilot drafted; Mark to react. Pared from the 14-candidate roster in `era-research/banned-toys.md`. This document is the **mission spine** for the entire game — every component below is a quest.
>
> **Authority:** Locks the machine. When this doc and another doc disagree about machine specs, this wins. Story arc + gameplay loop take precedence over THIS doc for tone/loop choices; THIS doc takes precedence for parts/missions.

---

## Design rules (locked from prior sessions)

- **10 components** total. Each MUST be a real challenge.
- **Every component uses ≥1 of FIND / TRADE / EARN / CRAFT.** Most use 2-3. Hero components use all 4. A pure-FIND component is a design failure.
- **Cadence target:** Act 1 = 4 components (the workbench + 3 easy parts that teach the loop). Act 2 = 5 components (escalation, mid-act mask-drop, first severe Tear). Act 3 = 1 capstone (the uranium core, retrieved at Ocean Side).
- **Tear cost.** Every install ticks the Tear up. Bigger / more central components tick it more. The final install (capstone) cracks reality open.
- **No filler.** Each component teaches something true about 1976. If it doesn't, swap it.

---

## How to read each entry

```
COMPONENT [letter] — [name]
Function: what this part does in the machine
Sourced from: which 1976 object becomes the part
Acquisition: which of FIND / TRADE / EARN / CRAFT (and combo notes)
Act / position: when this fires in the story
Mission sketch: one paragraph — obstacle, era teaching, comedy beat
Tear impact: small / medium / large / catastrophic
NPCs surfaced: who this component requires
Open questions: things needing Mark's call
```

---

## The 10 (in install order, roughly chronological)

### COMPONENT L — The Soldering Iron (the Workbench Enabler)

- **Function:** Not a part of the machine itself. **Unlocks the workbench.** Without this, no CRAFT mechanic exists in the game.
- **Sourced from:** **Wood Burning Kit** (1970s craft staple — basically a soldering iron with a "wood-burning" cover story). Real, sold to children, ~$5 at any toy store.
- **Acquisition:** FIND + a token amount of cash.
- **Act / position:** Act 1, **first component** — the on-ramp. Player has bike but no workbench. Tutorial-adjacent.
- **Mission sketch:** Mark wakes up in Danny's room (Act 1 Beat 3 territory). He has the notebook. He has a bike. He stares at the half-built rig under the workbench. He needs to start *building.* Danny's marginal note says: *"wood burning kit — top shelf at McCrory's, $4.99, take a quarter from the dresser."* Mark walks to the local five-and-dime. Buys the kit. The clerk, a bored teenager smoking a cigarette behind a candy display, does not card him. Mark walks home. Workbench unlocks. **The era teaching here is the casual "kids can buy a soldering iron" beat. Mark VO: *"He just sold a fire device to a 14-year-old. He didn't even look up."***
- **Tear impact:** **NONE.** This is the workbench-enabler, not a machine install. Player learns the install ritual on the *next* component.
- **NPCs surfaced:** The five-and-dime clerk (unnamed, ambient).
- **Open questions:**
  - Should it cost cash or be a FIND from Danny's room? Pitch: cash. The shopping trip teaches the corner-store world.

---

### COMPONENT J — The Primary Coil (Slinky)

- **Function:** Primary inductor. Wraps around the central housing.
- **Sourced from:** **Slinky** (James Industries, 1945, peaked through the 70s). The metal helix is *literally* a coil — perfect-pitch period gag.
- **Acquisition:** FIND + CRAFT.
- **Act / position:** Act 1 early, **2nd component** — first real install, first Tear tick.
- **Mission sketch:** Bobby's bedroom has a Slinky. It's been kinked and tangled and partly straightened — useless as a toy, perfect as a coil. Mark needs to trade or persuade Bobby to give it up. Bobby's a soft trade (per `kid-valuables.md`) — a couple Wacky Packages stickers and the deal is done. Mark takes the kinked Slinky to the workbench. The CRAFT step is *un-kinking and re-tensioning* the helix — a minor mini-puzzle. Install. The machine HUMS for the first time. Mark VO: *"I am building a quantum reality bridge. Out of a Slinky. Out of a Bobby's broken Slinky."*
- **Tear impact:** **SMALL.** First install. The notebook shows one extra line of marginal text after the install, but it's still warm-and-fuzzy Danny tone.
- **NPCs surfaced:** Bobby (already in `people.yaml`).
- **Open questions:**
  - Bobby's trade asking-price — Wacky Packages stickers? Confirm. Could also be "let him watch you build for an hour" = EARN flavor.

---

### COMPONENT C — The Grounding Spike (Lawn Dart Tip)

- **Function:** Grounds the rig to the earth. Without it, the whole apparatus floats electrically and can't discharge.
- **Sourced from:** **Lawn Darts (Jarts).** The forged-steel tip is the spike. Whole set comes with 4; we only need 1, but Mark has to *get a whole Jart* because nobody breaks up the set.
- **Acquisition:** FIND + EARN.
- **Act / position:** Act 1 mid, **3rd component.**
- **Mission sketch:** Dad (Dennis Marek) has a Jart set in the garage. Hasn't been played with since '74 — the previous summer ended with a near-miss on the neighbor's kid and Mom (Kay) declared *"those goddamn things stay in the goddamn garage."* So they're THERE, gathering dust. But the garage is *Dad's domain* — Mark can't just take one. He has to either (a) help Dad on a weekend project (drywall, per Dennis-the-sheetrocker character) and earn the right to "borrow" one, or (b) wait until Dad is at work and risk getting caught. **The era teaching is the dad-domain boundary** — kids didn't just go into the garage. Garage = Dad's. Bedroom = yours. Kitchen = Mom's. Real spatial-authority pattern. Mark VO: *"My dad in 2026 doesn't even have a garage. He has a parking spot in our condo building. This is a different planet."*
- **Tear impact:** **SMALL.**
- **NPCs surfaced:** Dennis Marek (already in `people.yaml`).
- **Open questions:**
  - Earn or steal? Pitch: **earn.** Stealing in Dad's garage is a fail-state (caught, grounded, lose a day). Earning teaches more about Dennis.

---

### COMPONENT F — The Pendulum Mass (Clackers)

- **Function:** Kinetic counterweight. Stabilizes the resonance.
- **Sourced from:** **Clackers** (two heavy acrylic balls on a string — the legendarily injurious 1970s playground toy). Crack one open at the workbench, harvest the inner weight.
- **Acquisition:** TRADE + CRAFT (and one HAZARD beat).
- **Act / position:** Act 1 late, **4th component** — closes Act 1. Mark feels competent. The machine has a satisfying shape.
- **Mission sketch:** Mickey carries Clackers around the Dungeon (per `banned-toys.md`). He uses them while talking to make a *crack-crack-crack* punctuation. Mark wants one. Mickey trades hard — he wants cigarettes or fireworks (per NPC currency table). Mark probably has to do a corner-store run (use cash, possibly first cigarette purchase scene — vending machine, no ID). Hand cigs to Mickey. Take the Clackers. **Then comes the hazard beat:** Mark tries to use them at the workbench to "rev them up" before harvesting, and they SHATTER. Plastic shrapnel. Soft-health hit. Mark VO: *"In 2026 this product would have triggered a Class Action by 9 AM on the launch day. In 1976 it's been outselling Hot Wheels for two years."* Then he carefully cracks the surviving ball at the bench. Install.
- **Tear impact:** **SMALL** to **MEDIUM.** Notebook starts to have *two* margin notes per install now. Danny's tone is slightly more clipped.
- **NPCs surfaced:** Mickey (already in `people.yaml`).
- **Open questions:**
  - Cigarette purchase scene — Act 1 or wait for Act 2? Pitch: **Act 1.** It's a perfect "oh god, this world" beat early. Vending machine in the Dungeon corner.

---

### COMPONENT N — The Mercury Switch (Thermometer Mercury)

- **Function:** Tilt-activated switch. Triggers the discharge cycle when the rig is aligned to true vertical.
- **Sourced from:** **Mercury thermometers** (every medicine cabinet in 1976). Player needs to break ~3 thermometers, collect the silver beads, and CRAFT them into a sealed glass tube.
- **Acquisition:** FIND + CRAFT (with a HAZARD comedy beat).
- **Act / position:** Act 2 early, **5th component overall, 1st of Act 2.**
- **Mission sketch:** Marek house bathroom has a thermometer. Bobby has one too — kids' thermometer, smaller. The Kowalskis have one (Iwona-house scene opportunity). Mark needs three. **The comedy:** the FIRST one he breaks at the workbench. The mercury beads roll across the wood. They are *mesmerizingly silver*. Mark stares. Mark VO: *"This is liquid metal. This is a class-1 neurotoxin. This is currently rolling around in my workbench. In 2026 a single broken thermometer triggers a hazmat response. In 1976 this is Tuesday."* Bobby walks in. *"Cool — can I touch it?"* Mark physically blocks him. The era teaching writes itself. The CRAFT step is using the Gilbert glass-blowing set (Component B prerequisite — see below) to seal the mercury into a tilt-switch. **HOLD: this implies B must come before N, OR we use a regular medicine vial and re-do later.** See open Q.
- **Tear impact:** **MEDIUM.** First Act 2 install. Notebook gets longer. First time the marginal note ends mid-sentence.
- **NPCs surfaced:** Bobby (already there). Possibly Iwona / Mary Kowalski if we use the bathroom-of-the-Kowalski-house trip.
- **Open questions:**
  - **Sequencing problem:** N needs glass tubing from B. Either we put B before N (then Act 2 opens with a heavy quest), or N uses a temp vial and gets a "v2 upgrade" later (Tear-cost surcharge). Pitch: **put B before N.** Glass-blowing set is the right "we're escalating now" Act 2 opener.

---

### COMPONENT B — The Vacuum Chamber (Glass-Blowing Set)

- **Function:** Central vacuum chamber. Houses the core. Without it the U-238 capstone has nowhere to go.
- **Sourced from:** **Gilbert Glass-Blowing Set** (1950s-60s, *predates* 1976 — the kit was discontinued by then). Has to come from an older neighbor's basement / antique find / yard sale.
- **Acquisition:** EARN-heavy (single source) + CRAFT.
- **Act / position:** Act 2 early-to-mid, **6th component overall, 2nd of Act 2.** ESCALATION marker.
- **Mission sketch:** Danny's marginal note (one of the earliest cryptic ones Mark decoded) said: *"Old Man at end of block — basement — Gilbert set — listen first."* Mark walks to the end of the block. Knocks. **The old vet** (placeholder NPC — un-named per the on-demand rule until this quest greenlights) opens the door. He's wiry, deeply tanned, smells like Old Spice and pipe tobacco. He invites Mark in. He starts telling a war story. **The mechanic is the story-listening minigame.** Player must STAY (no clicking through). Don't interrupt. Ask one (1) follow-up question when prompted. After ~5 minutes of in-game listening, the vet sighs, stands up, says *"come down to the basement, son, I want to show you something."* The basement is a museum of dangerous toys. He hands Mark the glass-blowing set. *"Don't tell your mother."* The CRAFT step: Mark spends real time at the workbench drawing tubing into the vacuum-chamber shape. The alcohol torch is the secondary heat source for this. **Era teaching: the entire mechanic of "old men want to be listened to" is a load-bearing 1976 truth.** Mark VO: *"In 2026 I would have asked him three questions and left in 4 minutes. He'd have died alone six weeks later. He told me about North Africa and I gave him 12 minutes and he was so happy. Christ. Christ."*
- **Tear impact:** **MEDIUM-LARGE.** First time Danny's marginal note finishes a sentence with *"…not sure how much longer I can—"*
- **NPCs surfaced:** **THE WAR-VET BASEMENT NPC** — needs a name and a war (WWII, Korea, or Pacific Theater). Pitch: name him **Mr. Halloran** or **Mr. Brennan** — let Mark pick. WWII, Pacific Theater. 16 in 1942 = 50 in 1976.
- **Open questions:**
  - Name the vet. Decide war.
  - **One visit or multiple?** Pitch: he becomes a recurring stop. Mark can visit any time. Each visit = one new story = small Mark-recoil VO beat. He becomes a quiet favorite NPC. He's also the source for **Component G's Austin Magic Pistol** later.
  - Listening-minigame design: pure click-to-stay? Or a dialog wheel where wrong choices end the visit?

---

### COMPONENT K — The Rotational Bearing (Swing Wing Hub)

- **Function:** Allows the central housing to rotate freely on its axis during alignment.
- **Sourced from:** **Swing Wing** (helicopter-propeller hat from 1975 — wear it, swing your head, propeller spins, you get a concussion). The hub is a beautiful small smooth bearing.
- **Acquisition:** FIND + CRAFT.
- **Act / position:** Act 2 mid, **7th component.**
- **Mission sketch:** Eva (Iwona's little sister) has one — won at a Bicentennial-themed playground giveaway last summer. She doesn't use it anymore. **Per `kid-valuables.md` NPC table, Eva wants Shrinky Dinks or jewelry trinkets.** Mark needs to source a Shrinky Dinks set, which means corner-store run. Trade. Get Swing Wing. **The hazard comedy beat:** Mark, at the workbench, *tries it on* once before harvesting. Spins his head. Vision blurs. Slight Tear-meter tick because the player just *did* something physically disorienting in-fiction. Mark VO: *"I want everyone in 2026 to understand: this was MARKETED as a TOY. The instruction sheet said 'swing your head in a circle.' It MEANT it."* Then he disassembles. Install. **Bonus payoff:** small Iwona-adjacent beat — Eva talks about her sister. *"Iwona thinks you're weird. But like, weird-good."* Mark dies inside. Player smiles.
- **Tear impact:** **SMALL.** (Compensating for the heavy B install just before.)
- **NPCs surfaced:** Eva (already in `people.yaml`).
- **Open questions:**
  - Eva's Iwona-aside — confirm landing this here. It's a small romance beat without spending a romance scene. My take: yes.

---

### COMPONENT G — The Ignition Primer (Hero Component — All Four Mechanics)

- **Function:** The firing primer. When the machine cycles, this is what *strikes.* The discharge moment.
- **Sourced from:** **TWO sources required:**
  1. **Cap-gun caps** — pyrotechnic compound (potassium chlorate + sulfur + antimony sulfide). Corner-store source. ~20 rolls.
  2. **Austin Magic Pistol calcium carbide** — the *capstone reagent*. Lives in old Mr. Halloran's basement (Component B's vet). Cannot be bought; cannot be substituted.
- **Acquisition:** **ALL FOUR — FIND + TRADE + EARN + CRAFT.** This is the hero component.
- **Act / position:** Act 2 mid-late, **8th component.** Heavy lift. Mark feels the work.
- **Mission sketch:** Multi-stage quest.
  - **(FIND)** Corner store — buy cap-gun cap rolls. Cash. Easy. *But you need ~20 rolls and the store only stocks 5 at a time.* So this is a multi-day FIND beat, watching the shelf restock, possibly hitting two different corner stores in different zones.
  - **(TRADE)** Bottle rockets for the kid who has a stash. Per the "older dealer kid" placeholder NPC (now NEEDS naming if we greenlight this — Mark can name on the fly). Trade currency: Playboys (S-tier) OR a small stack of cash.
  - **(EARN)** Return to Mr. Halloran. This time he's slower to invite Mark in. Mark has to ask after his health, listen to TWO war stories (not one), and *bring something* — pitch: a fresh tin of Sir Walter Raleigh pipe tobacco from the drugstore (real 1976 brand). Halloran softens. *"Son, what's a boy your age want with calcium carbide?"* Mark lies smoothly: a chem-set experiment for the science fair. Halloran half-believes but hands it over. *"Don't blow your face off. I've seen what this does to faces."* The mood shifts. The Tear ticks UP just from the conversation — Danny is closer to the surface here than usual.
  - **(CRAFT)** Workbench. Combine cap powder + carbide + glass vial (recycled from Component N's CRAFT byproduct? or new). Multi-step CRAFT mini-puzzle, with a HAZARD beat — Mark almost mixes wrong proportions. If the player gets it wrong, fail-state is funny (eyebrows singed, lose a day, repeat).
  - **Install.** The machine now has a discharge mechanism. It is *almost* a machine.
- **Tear impact:** **LARGE.** Comms 1.5 lands right after this. Danny's note: *"Mark — be careful with the next two. Once those go in I don't know what happens."*
- **NPCs surfaced:** Mr. Halloran (lock from B), **the older dealer kid (needs name).** Suggested name: **Wade** or **Tony Doolin** — Mark, your call.
- **Open questions:**
  - Name the dealer kid.
  - Multi-step CRAFT mini-puzzle vs single craft action — design call. Pitch: small puzzle, three steps, low difficulty, high comedy.
  - HAZARD eyebrow-singe — single-use joke or repeatable fail-state? Pitch: single-use, then never again (the player learns).

---

### COMPONENT M — The Comms Relay Crystal (CB Radio — Hero Component — All Four Mechanics)

- **Function:** **THE LORE-CRITICAL COMPONENT.** The crystal from a working CB radio is what lets the notebook receive Danny's messages across time. *This is how the Tear talks.* Without it, no comms. With it, the bridge to 2026 is open enough for Comms 2 (the mask-drop).
- **Sourced from:** A working CB radio (Cobra 29, Realistic TRC-447 — 1976 peak gear). Crystal is a small quartz oscillator inside the unit.
- **Acquisition:** **ALL FOUR.**
- **Act / position:** Act 2 late, **9th component.** Last install before Act 3. Triggers Comms 2 and the "Machine Catches Fire (Again)" beat already locked in story arc.
- **Mission sketch:**
  - **(FIND)** Mark spots a CB radio in the back of a parked truck on Main Street. (CB radios were EVERYWHERE in 1976 — *Convoy* was #1 — every dad had one.) But the truck is locked and Mark isn't ready to break into a vehicle. Mental note. *"Wait — there's another one. Mickey's dad has one in his pickup. And the guy at the gas station. And —"* The era teaching is just **how saturated CB was in 1976.**
  - **(TRADE)** Older dealer kid (Wade/Tony, locked above) knows somebody who'll *sell* a CB. Trade currency: S-tier or a big cash sum. Player can pursue this path but it's expensive.
  - **(EARN)** **Alternate path: Mickey's dad.** Mickey's dad is the cooler dad on the block (per Karras family / Marek family contrast — actually wait, let me check who's who).
  - **[Clawpilot pause — need to verify which dad has the CB. Pitch: not Dennis Marek. Possibly Gus Karras, the Greek-Orthodox dad. He drives a delivery truck. Gus has the CB.] Mark has to befriend Gus directly** — which means showing up at the Karras household for dinner, eating Athena's intimidating Greek food without flinching (mini-game: do not pull a face), surviving Sunday-school discussion at the table. Earn Gus's respect. Gus shows him the CB. *"You want to TALK on it?"* Mark says yes. They have a 4-AM-bored-trucker conversation on the CB together. Gus, drunk on Metaxa, says: *"Kid, you ever need parts for a thing — I got connections."* Hands Mark a *spare CB* he picked up at a swap meet.
  - **(CRAFT)** Workbench. Disassemble the CB. Harvest the crystal. The CRAFT step is delicate — solder iron on tiny pins. Wood Burning Kit (Component L) gets its capstone use here.
  - **Install. The notebook BURNS WARM.** Comms 2 fires within minutes (the locked story-arc mask-drop scene). The machine catches fire (already locked in story arc Act 2 Beat 5). Tear severe.
- **Tear impact:** **LARGE → SEVERE.** Direct trigger for Comms 2 + Tear opening.
- **NPCs surfaced:** **Gus Karras** (already in `people.yaml`!). Athena Karras (already in). Mickey (already in). The dealer kid (Wade/Tony, from G).
- **Open questions:**
  - Confirm Gus Karras as CB dad. Pitch: yes. He drives delivery. Greek immigrant trucker = perfect 1976 archetype.
  - Confirm Mark's CB conversation with Gus is playable (dialog-wheel) or cinematic. Pitch: **playable.** Player gets to *be* a 1976 trucker for 90 seconds. *"Breaker breaker, this is Little Greek, you got a copy on me?"* Comedy gold and educational.
  - Athena's intimidating-food mini-game — design later. One-line note for now.

---

### COMPONENT A — The Uranium Core (THE CAPSTONE — Gilbert U-238)

- **Function:** The reality-bridge core. The thing that makes the whole machine *work* as a quantum-trans-temporal-whatever. Without it, the machine is decoration. With it, the machine is the *exit door.*
- **Sourced from:** **Gilbert U-238 Atomic Energy Lab (1950).** Real product. Real uranium ore sample inside. $49.50 in 1950 dollars. By 1976 these are *antiques* — they exist in old men's basements, antique stores, the back of toy-store stockrooms. **Locked: Ocean Side antique store** per story-arc Act 3 Beat 5.
- **Acquisition:** EARN + CASH + a small heist beat. (Not all-four — by Act 3 the player's competence is high, this is the *destination,* not the puzzle. The journey to Ocean Side and back IS the quest.)
- **Act / position:** **Act 3, Beat 5** — the locked Ocean Side trip moment. The Gilbert U-238 hunt is the spine of the entire Ocean Side trip.
- **Mission sketch:** Already mostly locked in `story-arc.draft.md` Act 3 Beat 5. Quick recap of the part-acquisition layer: Mark, on the boardwalk, ducks into a dusty antique store ("**Sea Glass Antiques**" — placeholder name). The owner is an old guy who reminds Mark of Mr. Halloran. He has a Gilbert U-238 on a high shelf. Sticker price: $35 — a *fortune* for Mark in 1976 dollars. Mark either:
  - **(CASH)** Has saved $35 from Act 2 grind (corner-store odd jobs, bottle returns, payphone coin-returns per `quest-seeds.md` SEED 2). Pays it. Owner asks no questions. *"You know what's in this thing, kid?" "Yes sir." "OK then."*
  - **(EARN)** Doesn't have $35. Owner offers a deal: clean out his back storeroom for the rest of the afternoon. Mark spends a real in-game hour sorting boxes. Iwona finds him there. *Scene.* Owner gives him the Gilbert + a discount.
  - **(HEIST)** Optional darker path: Mark could try to steal it. Fail-state available. Pitch: leave the option *visible* but punishing — caught, kicked out, can't come back, has to find a second source (which DOES NOT EXIST — soft-locks the player and forces a reload). **Probably cut.** Too punishing for first-time players.
- **Tear impact:** **CATASTROPHIC.** This install opens the Tear all the way. Cuts to story-arc Act 3 Beat 7+ (the build, the kiss, the leap).
- **NPCs surfaced:** **Antique store owner** (placeholder — needs naming if we greenlight). Pitch: **Mr. Doroshenko** — Ukrainian immigrant, ex-merchant marine. Adds another immigrant texture without duplicating Halloran.
- **Open questions:**
  - Cash + EARN dual path, or just one? Pitch: **both available.** Player choice. EARN path gets a free Iwona scene which is *very* tempting design-wise.
  - Confirm "no heist option." Pitch: confirmed cut. Adds a bad fail-state with no recovery.
  - Name the antique store owner.

---

## Cadence summary

| Act | Components | Tear progression | Story beats triggered |
|---|---|---|---|
| **Act 1** | L (workbench), J (Slinky), C (Lawn Dart), F (Clackers) | None → Small | Player learns the loop. Notebook is warm. Danny is chatty. |
| **Act 2** | N (Mercury), B (Glass-Blowing), K (Swing Wing), G (Ignition Primer — HERO), M (CB Radio — HERO) | Small → Medium → Large → SEVERE | **Comms 1.5 after G. Comms 2 after M (already locked mask-drop). Machine catches fire after M.** |
| **Act 3** | A (Uranium Core — CAPSTONE) | CATASTROPHIC | **Tear opens all the way. Ocean Side trip is the entire Act 3 spine. Locked story-arc beats fire.** |

Total: **10 components.** Act distribution: **4-5-1.** Tear cadence: gentle slope through Act 1, steepening Act 2, cliff at Act 3.

---

## NPCs this spine REQUIRES (locked the moment Mark greenlights this doc)

Already in `people.yaml`:
- **Bobby Marek** (Component J — Slinky)
- **Dennis Marek** (Component C — Lawn Darts in his garage)
- **Mickey Karras** (Component F — Clackers / Cigarette trade)
- **Eva** (Component K — Swing Wing trade)
- **Gus Karras** (Component M — CB Radio + trucker scene)
- **Athena Karras** (Component M — Greek dinner mini-game)
- **Iwona** (multiple — including the EARN-path Ocean Side antique store scene)

To be ADDED to `people.yaml` (these missions cannot ship without them):
- **Mr. Halloran** (Components B + G) — WWII Pacific vet, end of block, war-stories-listening mechanic
- **Wade or Tony Doolin** (Components G + M) — older "dealer" kid for S-tier trade
- **Mr. Doroshenko** (Component A) — Ocean Side antique store owner, Ukrainian ex-merchant-marine

Three NPCs to add. Each tied to a specific quest — follows Mark's "on demand only" rule.

---

## Items NOT on the 10-list (what got cut from the 14-draft)

For transparency. These remain available as **trade goods, ambient props, comedy beats** — they're just not installable components.

- **Slime (Mattel)** — kept as ambient + trade. Bobby owns. Eva owns. Comedy prop.
- **Disc-shooter** — kept as HAZARD + ambient. Mickey has one. Showed up in playground beats.
- **Lemon Twist** — kept as ambient + comedy beat. Eva owns. Cut from pendulum role (Clackers won).
- **Slingshot** — kept as ambient. Mickey has one. Possible Eric-equivalent trade later.
- **Dip-a-Flower** — kept as ambient (the *smell* of Dip-a-Flower in the basement is era texture). Cut from the resin role (didn't need a separate resin component).
- **LEGO** — kept as small-trade with younger kids. Cut from housing role.

If any of these survivors get a quest hook later, they can be promoted back. The 10 above are the spine.

---

## Open questions for Mark

1. **Approve the 10-list as-is, or swap any?** This is the central decision.
2. **NPC name calls (three new NPCs):** Halloran or Brennan for the vet? Wade or Tony Doolin for the dealer kid? Doroshenko OK for the antique-store owner?
3. **Cigarette purchase scene in Act 1 (Component F detour)** — pitch yes, vending machine, no ID. Confirm.
4. **Gus Karras as CB-dad** — confirm. (Or do you want Dennis Marek instead? Pitch: Gus, because the Karras household visit is otherwise underused.)
5. **Old Mr. Halloran's story-listening mechanic** — single-visit-with-multiple-conversation-points, or recurring-stop-with-stories-per-visit? Pitch: recurring stop, becomes a quiet game favorite.
6. **Athena's Greek-food mini-game** — keep as design seed or cut? Pitch: keep, design later.
7. **Ocean Side antique store — heist option cut?** Pitch: cut. Don't soft-lock the player.
8. **Tear cost calibration.** The current cadence (Small → Medium → Large → Severe → Catastrophic) is *vibes-based* right now. We'll calibrate when we prototype.

---

## What this doc unlocks

Once Mark signs off on this 10-list, we can:

1. **Draft `quests.md`** — each component becomes a multi-step quest with branching dialog and item requirements
2. **Update `people.yaml`** with the three new NPCs (Halloran, Doolin/Wade, Doroshenko)
3. **Start `locations.md`** by pulling the locations these missions IMPLY (corner store, McCrory's five-and-dime, Halloran's house, Karras household, Ocean Side boardwalk + Sea Glass Antiques, the gas station, the local park, etc.)
4. **Begin the first Ren'Py vertical slice** — pick the simplest component (probably L or J) and build the complete loop in code

This is the spine. Everything from here flows from these 10 quests.
