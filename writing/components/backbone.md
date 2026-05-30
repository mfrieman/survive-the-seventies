# Component Backbone — The Machine Chassis (Path 1)

> **Status:** Supporting canon — the **Path-1 chassis / cash-gated money layer.** Sibling to `machine-architecture.md` (the slot model); not in conflict with it.
> **Note:** the old "10 toy components (L, J, C, F, N, B, K, G, M, A)" letter model is **superseded** by the **Signal Pathway 10-slot** model in `machine-architecture.md`. Read the letter refs below as the Signal slots they became. **Path 2 (the ritual platform) has its own substrate — Denise's painted board — not this chassis.**
> **This is what the Signal-pathway parts mount onto.**

---

## At a glance

The machine has a real 1976 hobbyist chassis underneath the toy parts. The 10 components are mounted/soldered onto **this backbone.** The backbone is **cash-gated** (not quest-gated like the 10 toys) — Mark earns money via kid-economy loops and buys backbone parts at **Burnsville Electronics**.

| Field | Value |
|---|---|
| **Function** | The chassis, motherboard, power, and wiring everything else attaches to |
| **Source** | Burnsville Electronics (primary) + curbside TV salvage (alternative for power supply) |
| **Mechanics used** | **Cash + CRAFT** (assembly) — minimal quest friction, max economic friction |
| **Act / position** | Acts 1-2 — assembled in stages as money allows |
| **Difficulty band** | Easy-Medium (the *challenge* is affording it) |
| **Prerequisite for** | Everything. No backbone, nothing mounts. |

---

## The 4 backbone parts

### 1. Aluminum Chassis Project Box

- **Real-world part:** Bud Industries or Hammond aluminum project box, ~6"x8"x3". Bare aluminum with rubber feet, screw-on lid.
- **Function in machine:** The frame. Everything else lives inside or mounts to.
- **In-game cost:** ~5 days of average allowance ($3-5 real-world 1976).
- **Acquisition:** Buy at Burnsville. Owner shows two sizes — small (cheap, won't fit later parts) and standard (right size, more expensive). Choice teaches the player to think ahead.
- **Install step:** Mark drills holes in the lid for switches and the meter. CRAFT step at the workbench (component L must be unlocked).

### 2. Perfboard / Vectorboard

- **Real-world part:** Phenolic board with 0.1"-grid copper pads. Standard 4"x6" hobby size.
- **Function in machine:** The "motherboard." Toy components solder to this. Wires run on the underside.
- **In-game cost:** Cheap (~1 day of allowance).
- **Acquisition:** Buy at Burnsville. Owner sometimes throws in a free smaller piece if Mark buys other stuff. Small generosity beat.
- **Install step:** Mark mounts the perfboard inside the chassis on standoffs. Trivial CRAFT.

### 3. Power Supply Guts (TWO PATHS)

- **Real-world part:** Power transformer (120V → 12V or 24V) + bridge rectifier + filter capacitor + a fuse. Converts wall AC to the DC the machine needs.
- **Function in machine:** Without this, the machine has no juice. Component L's soldering iron plugs in the wall directly; *the machine itself* needs DC.

**Path A — Buy at Burnsville:** Cost is the **biggest single cash hit** in the game. Maybe 2-3 weeks of saving from kid-economy loops. Forces money pressure to its peak. Owner is reasonable; offers to teach Mark how to wire it safely (*"You short this and you're a 1976 statistic"*).

**Path B — TV Salvage:** Mark finds a broken console TV on the curb on a Tuesday (trash day). Strips it for the transformer, rectifier, and cap. FREE. But:
- Has to know which Tuesday (overheard at Burnsville, or from a friend).
- Has to drag the TV home in pieces (Bobby is suspicious; mom asks questions).
- Has to identify the right parts (Burnsville owner or the Book can teach this).
- Risk: pulling parts from a TV is electrically dangerous — picture tube vacuum implosion, the giant capacitor that holds a *lethal* charge for weeks after unplugging. Era-teaching beat.

**Player choice teaches the era:** Path A is safer and faster but eats your money. Path B is the *1976 way* — you fixed stuff, you scavenged, you knew how things worked. Recommended path narratively, but the player who hates salvage minigames can grind cash instead.

### 4. Consumables: Hookup Wire + Solder + Flux

- **Real-world part:** Spool of 22-gauge stranded hookup wire (multiple colors), spool of 60/40 rosin-core solder, can of flux paste.
- **Function in machine:** The connective tissue. Every CRAFT step on the 10 components consumes some.
- **In-game cost:** Low individual cost, but **runs out.** Each major component install consumes wire & solder. Player has to top up at Burnsville mid-game.
- **Acquisition:** Buy at Burnsville. Owner sometimes sells a kid a *small* clipping of solder for a quarter when the kid is broke. Generosity beat.
- **Subtle game systems implication:** Inventory has wire/solder as numeric stocks. If you run out mid-install, you walk to Burnsville. Friction = real but not punishing.

---

## The acquisition arc (across Acts 1-2)

| When | Backbone parts acquired | Driver |
|---|---|---|
| **Early Act 1** | Soldering iron (Component L, separate) + chassis box + perfboard | Mark's starting cash + first allowance + maybe first payphone scrounge |
| **Mid Act 1** | First spool of solder + wire | Cash drip from chores |
| **Act 1 → Act 2 transition** | **Power supply decision point.** Save up for purchase OR go salvage. Forces real choice. | Player choice |
| **Mid Act 2** | Consumables top-up (wire, solder runs low after Components N + B + K) | Forced visit |
| **Late Act 2** | Possibly a second chassis section if machine outgrows original box (optional — depends on final design) | TBD |

---

## Money economy — how Mark actually earns

(See `components/money-economy.md` — to be drafted. Quick summary here.)

The backbone's cash gates require Mark to engage with the **kid-economy loops:**

- **Allowance** — baseline trickle. Typical 14-year-old: $2-5/week.
- **Payphone coin return** — recurring small finds (quest seed already in `quest-seeds.md`).
- **Lawn mowing** — neighborhood EARN loop. One lawn = roughly a chassis box.
- **Returning bottles for deposit** — 2¢ a bottle, kids scoured roadsides for these.
- **Tube testing at Burnsville** — bring in tubes from salvage, test, sell good ones back to owner for small credit. Recurring mini-loop.
- **Selling specific kid-economy items** at the right rate (comics, etc.) — risky, since the no-stealing rule means Mark sells his *own* stuff, not others'.
- **Special one-shots** — finding a wallet (return it for reward — moral test), winning a bet, getting paid for a favor.

This makes backbone purchasing a **real game loop** rather than a menu transaction.

---

## Why this matters narratively

- **The machine looks real.** Aluminum box, perfboard, wires, plugged into the wall. The Slinky and the cap-gun caps and the mercury switch live inside this *almost-plausible* hobbyist chassis. The comedy is the *combination,* not the impossibility.
- **Burnsville is a recurring location.** Mark visits it 5-8 times across the game. The shop, the owner, the bell on the door, the smell of solder — these become *familiar* in a way the boardwalk-once trips never can.
- **Money pressure is REAL.** When you have to save 3 weeks for a transformer, every quarter from a payphone coin return *matters.*
- **Teaches the era's "fix it" ethic.** TV salvage path is the most period-accurate, and rewards the player who engages with the era's logic.
- **2026 Mark VO can land the "we don't build anything anymore" beat** organically as Mark walks the aisles of Burnsville.

---

## People involved

| Role token | Where they show up | Notes |
|---|---|---|
| `[BURNSVILLE-OWNER]` | Every backbone purchase, plus tube-testing loop | Generic for now. Mark will develop later. Patient with serious kids, brusque with time-wasters. Doesn't ask what kids build. |
| `[CURBSIDE-TV-NEIGHBOR]` | Optional — if salvage path triggers questions from a neighbor putting out the TV | Generic. Single line of dialog. "You want that piece of junk? Have at it." |
| **Bobby Marek** (existing) | Suspicious of the aluminum box growing in Mark's bedroom | "What is that?" recurring beat |
| **Kay Marek** (existing) | Asks where the money is going | "You're saving up? For what?" — pressure source |

---

## Locations involved

| Location | What happens | New or existing |
|---|---|---|
| **Burnsville Electronics** | All purchase scenes, tube testing, owner relationship | NEW — needs `locations.md` entry |
| **Mark's bedroom / workbench** | All assembly scenes | Existing |
| **A neighborhood curb (specific block)** | TV salvage on Trash Tuesday | NEW — light, transient |
| **Walking route to Burnsville** | Possible ambient scenes / encounters | Existing block exterior + extension |

---

## Dialog flavor

Sample lines:

- **`[BURNSVILLE-OWNER]` (first visit, Mark holding a chassis box and a perfboard):** *"You know what you're doing with that, son?"* / **Mark:** *"...yes."* / **Owner:** *"Mm. Don't electrocute yourself. The bigger one is for if you're building anything with a power supply. You building anything with a power supply?"* / **Mark:** *"Probably."* / **Owner:** *"Get the bigger one."*

- **`[BURNSVILLE-OWNER]` (later, Mark is now a regular):** *"Crystal for what channel?"* / **Mark:** *"Uh. Nineteen."* / **Owner:** *"Of course. Two-fifty. Don't talk to truckers, they'll lie to you."*

- **Mark VO (walking into Burnsville):** *"This place lasts almost fifty years. Almost. I won't tell him."*

- **Mark VO (TV salvage path, looking at a console TV on the curb):** *"That's a transformer, a rectifier, two electrolytics and probably half a CB worth of useful junk. In 2026 someone would haul this to a landfill and feel bad about it. Here it's just Tuesday."*

- **Kay (Mark counting change at the kitchen table):** *"What are you saving for?"* / **Mark:** *"...a radio."* / **Kay:** *"You have a radio."* / **Mark:** *"A different one."* / **Kay:** *"Mm-hm."*

- **Bobby (peering at the chassis box):** *"What's the box for?"* / **Mark:** *"Project."* / **Bobby:** *"What project?"* / **Mark:** *"Science fair."* / **Bobby:** *"That's not for like a year."*

---

## Tear impact

The backbone itself does **not** trigger Tear costs — only mounting toy components onto it does. The backbone is the canvas; the toys are the paint.

EXCEPTION: First time the **power supply** is wired up and energized, even with no toy components installed, the machine emits a single brief crackle and the bedroom light flickers. Mark VO: *"...okay. So it's real now."* Atmospheric beat, no real cost — just a marker that the project has crossed a line from "kid-with-tools" to "thing-that-could-actually-do-something."

---

## Mark-from-2026 VO beats unique to backbone

1. **First walk into Burnsville.** Bell on the door, smell of solder. Mark stops. *"Oh."* (Doesn't have to say more. Player who knows the real place will catch it.)
2. **The "lasts almost fifty years" line** at some point in Act 2.
3. **The TV salvage scene.** *"We threw this stuff out. We threw it in landfills. We threw away the parts AND the knowledge of how to use them."*
4. **The first cash counted at the kitchen table.** *"I have not counted change since 2008. I have not NEEDED to count change since 2008. This is the most attention I've paid to seventy-two cents in twenty years."*
5. **The power supply first-crackle.** *"Yeah. That's a real thing now."*

---

## Era-teaching surface

- **Hobby stores existed and were beloved third places.**
- **Things were fixable.** You bought parts, not replacements.
- **Curbside trash was a parts source** for anyone who could strip electronics.
- **Money was earned in coins** and kept in a jar on the dresser.
- **Mail-order kits** (Heathkit) let kids build their own everything.
- **You needed to know which transformer was which** — no Amazon search, no datasheet PDFs, just a wall of similar-looking parts and an owner who'd point.

---

## Open questions / risks

1. **TV salvage path — required or optional?** If optional, most players will skip it. Could lock the backbone power supply behind salvage (player MUST do the era-teaching scene) OR keep it optional (more freedom, less guaranteed lesson). Lean: **optional but heavily incentivized** (huge cost savings).
2. **Does the player see the chassis fill up visually?** Bedroom workbench should show the machine evolving — empty box → perfboard installed → first toy soldered → etc. Visual progression matters for the comedy.
3. **Does the owner know what Mark is building by the end?** A late-game "I always knew, kid" reveal? Lean: he suspects, never asks. The not-asking IS the relationship.
4. **Backbone failure states.** Does anything ever go wrong with the chassis itself? (Bad solder joint, blown fuse) Lean: yes, one mid-game beat where a solder joint cold-fails and Mark has to reseat it — teaches the "real" feel of hobby electronics. Small scene.

---

## Cross-references

- **decisions-log.md** — Burnsville Electronics locked (2026-05-24), Machine has a backbone locked (2026-05-24)
- **era-research/hobby-electronics-1976.md** — full research spine for the parts and the store
- **components/index.md** — sibling to the 10 toy components
- **components/money-economy.md** — to be drafted; the earning side of the equation
- **machine-architecture.md** — the canon slot model (Signal / Platform / Amber); backbone is the Path-1 substrate the Signal parts mount onto
- **quest-seeds.md** — payphone coin return, lawn mowing (the earning loops that fund backbone)
- **story-arc.draft.md** — Acts 1-2 (backbone is acquired across these)
