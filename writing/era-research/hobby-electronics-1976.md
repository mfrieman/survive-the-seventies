# Era Research — Hobby Electronics in 1976

> Source-of-truth research doc for what a 1976 kid would have encountered walking into a real hobbyist electronics store. The in-game store is **Burnsville Electronics** (tribute to real-world Baynesville Electronics, which closed 2024). This doc feeds `components/backbone.md` and any quests/dialog that touch the hobby-shop world.
>
> **Why this doc exists:** Mark's machine is not 10 toys taped together. It needs a real-world plausible 1976 chassis. To get that right and to write the hobby-shop scenes credibly, we need a grounded picture of the actual era.

---

## 1. The hobby electronics ecosystem in 1976

This was the **golden age** of consumer electronics tinkering. Three reasons:

1. **Things were repairable.** TVs, radios, appliances were modular. Tubes blew, capacitors leaked, transistors failed — you replaced the part, you didn't throw out the device. Every neighborhood had a TV repair guy.
2. **Kits were huge.** Heathkit, Knight-Kit, Allied dominated. You could build your own ham radio, oscilloscope, color TV, even a personal computer (the Heathkit H8 launched 1977 — Altair 8800 was already out in 1975).
3. **CB radio mania.** The CB craze peaked 1975-77. *Convoy* hit #1 in 1976. Every truck driver, every dad, every kid wanted a CB. This drove huge hobby-shop traffic.

**The store types:**

| Type | Examples | What they stocked |
|---|---|---|
| **Chain stores** | Radio Shack (Tandy), Lafayette Radio | Mass-market parts, kits, CB, stereos. Catalog-driven. |
| **Regional hobby shops** | Baynesville (Baltimore), countless local | Same as chains + deeper parts inventory + tube tester + surplus bins. Owner usually was the buyer. |
| **TV/appliance parts counters** | Independent — often in the back of a repair shop | Replacement chassis sections, TV tuners, picture tubes, refrigerator compressors |
| **Surplus / military surplus** | Mail-order (Edmund Scientific, Fair Radio) + occasional storefronts | Government/industrial pulls. Cheap, weird, often unlabeled. |

Burnsville Electronics is the **regional hobby shop** type. Has the kit selection, the tube tester, the surplus bins, *and* a TV-parts counter in the back.

---

## 2. What Burnsville Electronics stocks (canon inventory)

### Active components (the "smart" parts)

- **Vacuum tubes** — still ubiquitous. Every TV had 8-20 tubes. The store has a **self-service tube tester** at the counter (this is canon — a real era detail). Kids brought bags of tubes from their parents' TVs to test for free.
- **Transistors** — 2N3055 (power), 2N2222 (signal), MPS-A06, plastic bins of NPN/PNP signal types
- **Integrated circuits** — the **555 timer** (most famous chip ever), **741 op-amp**, early TTL (7400-series), CMOS (CD4000-series)
- **Diodes** — 1N4148 signal, 1N4001-4007 rectifiers
- **LEDs** — still NOVEL. Red was standard. Green and yellow existed. Blue was years away. A blinking LED was exotic.
- **SCRs / triacs** — for power switching

### Passive components

- **Resistors** — carbon-composition, color-banded, sold in bags of 100 or as part of "experimenter's packs"
- **Capacitors** — ceramic disc, mylar film, electrolytic (the big ones with polarity)
- **Variable capacitors** ("tuning caps") — for radio projects
- **Potentiometers** — volume pots, trim pots
- **Inductors / RF chokes**
- **Transformers** — filament transformers, audio output transformers, power transformers

### Mechanical / structural — **THE BACKBONE PARTS**

These are what Mark actually mounts the toy components onto. See `components/backbone.md` for full quest treatment.

- **Aluminum project boxes** — bare aluminum chassis with rubber feet, screw-on lid. Comes in standard sizes (4x6x2, 6x8x3, etc.).
- **Perfboard / vectorboard** — phenolic board with a grid of copper pads on 0.1" spacing. The amateur's PCB substitute. You solder components in, run jumper wires on the back.
- **Terminal strips, barrier strips, lug strips** — multi-point soldering anchors for wires
- **Chassis punches** — knockout tools for cutting holes for switches, meters, jacks
- **Standoffs and screws** — mount perfboard inside the chassis

### Tools & consumables

- **Soldering irons** — Weller pencil (15-25W for ICs), Weller gun (100W trigger-grip for chassis work)
- **Rosin-core solder** — 60/40 tin-lead, on a spool, sold by weight. Lead solder was standard — leaded everything in 1976.
- **Desoldering braid / solder sucker** — for fixing mistakes
- **Hookup wire** — 22-gauge stranded, color-coded, spools or pre-cut packs
- **Electrical tape** (no heat shrink yet — barely)
- **Flux paste**

### Test gear (in the display case, expensive)

- **VOM (volt-ohm meter)** — Simpson 260 analog. *The* meter. Triplett was the competitor.
- **DMM (digital multimeter)** — JUST starting to appear in '76, still expensive
- **Oscilloscope** — Heathkit IO-105, Tektronix for serious money. Rare in a kid's bedroom.
- **Signal generator**

### Salvage / surplus bins (the back of the store)

- **"Grab bag" parts** — sold by weight. Mixed everything. Sometimes treasure.
- **Pulled boards** from defunct TVs, radios, calculators. Strip 'em for parts.
- **Military surplus** — knobs, switches, meters with mil-spec stamps. Cheap, weird, often the *only* source for an oddball part.
- **One-off oddities** — left-behind kit parts, miscounted inventory, returns

### TV & appliance parts (the back counter)

- **TV tuners** (VHF, UHF), **picture tubes** (special-order)
- **Filament strings**, **deflection yokes**
- **Refrigerator compressors** (special-order)
- Less for kids, more for repair-guys, but kids absolutely poked through this stuff

### CB radio gear (front display — biggest seller in 1976)

- **CB transceivers** — Cobra, Midland, Realistic
- **Antennas** — base station verticals, mobile whips
- **Crystals** for non-synthesized rigs (component **M** comes from here)
- **SWR meters, power supplies, microphones**

### Kits (whole shelf)

- **Heathkit** — high-end, real instrument-grade kits (oscilloscopes, ham gear)
- **Knight-Kit / Allied** — mid-range
- **Radio Shack "Science Fair"** kits — entry-level, often the kid's first build
- **Build-your-own crystal radio**, **AM transmitter** (legal under low-power FCC rules), **strobe light**, **theremin**

---

## 3. What the store FEELS like (sensory anchor for writing scenes)

- **The bell on the door.** Aluminum-and-spring jingle. Every shop had one.
- **The smell.** Hot solder + flux + old carpet + dust + the slightly-burning smell of tube filaments warming up on the test rig.
- **The lighting.** Fluorescent overheads, slightly buzzing.
- **The floor.** Cracked linoleum tile, scuffed. Often a worn path from the door to the counter to the surplus bins.
- **The counter.** Glass display case full of meters and the more expensive ICs. Cash register that rings. Tube tester bolted to the end of the counter.
- **The walls.** Pegboard wall behind the counter with hundreds of small parts in clear plastic envelopes. Posters for Heathkit, RCA tubes, CB rigs.
- **The owner.** Behind the counter, often eating a sandwich, reads while business is slow, knows every regular by name, *will help a kid* if the kid is serious.
- **The back.** Open bins, slightly chaotic, where the kids and the cheapskate adults go.
- **The radio.** Always on. Tuned to AM news or a local talk station. Sometimes a ham rig is on in the corner — staticky voices fading in and out.

---

## 4. The owner archetype (Burnsville's `[BURNSVILLE-OWNER]`)

> Kept generic for now. Cast and name later.

**Role:** Mid-50s to early 60s. Wears a short-sleeve button-up over a t-shirt. Glasses. Pocket protector is real, not ironic. Probably ex-Navy electronics tech or ex-radio repairman. Built the store himself in the late '50s or early '60s.

**Disposition toward kids:** Patient with the serious ones, brusque with the time-wasters. Will let a kid hang out and learn if the kid actually wants to learn. Has a quiet way of pushing the right part into a kid's hand: *"You don't want that one. You want this one. Three cents cheaper and it'll actually work."*

**Doesn't ask what you're building.** This is canon. He's seen kids build everything from one-tube radios to spark-gap transmitters to (allegedly) one kid who built a small flamethrower. He's not interested in the *project*, he's interested in the *technique.* Mark can buy weird combinations of parts without explanation.

**Has a soft spot for a kid who actually solders.** First time Mark shows up with a real circuit question instead of "where are the batteries," the owner shifts. Becomes an info source — knows where to get a vacuum tube Mark can't find, knows which kid in the neighborhood is selling off his older brother's CB rig.

**Eventual story role:** A late-game scene where Mark needs an obscure part with no time to find it, and the owner reaches under the counter without asking and pulls it out. *"Figured you'd need this eventually."*

---

## 5. The tube tester scene (canon set-piece)

Every hobby shop had a tube tester. Free to use, mounted at the end of the counter. Big metal cabinet, dial with hundreds of tube types, sockets for every base style. You'd plug in a tube, look up its number in the chart, set the dials, push the button. Needle swings into GOOD / WEAK / BAD zones.

**Why it matters for the game:**
- Visual gag for a 2026 player: *"…they had a special machine just for ONE kind of part?"*
- Mini-puzzle potential: Mark brings in a bag of tubes from a curbside TV salvage, tests them, sorts good from bad, sells the good ones back to the owner for a small credit. Money-making loop.
- Tonal beat: First time Mark uses it, the owner walks over: *"You know how to read this?"* / Mark (cautious): *"Sort of?"* / Owner: *"Here. Forty seconds, you'll know forever."* Teaches the era's craft-passing-down ethic.

---

## 6. CB radio in 1976 (set context for Component M)

CB was a **mass phenomenon** in 1976. Not a hobbyist niche — a *cultural movement*.

- *Convoy* by C.W. McCall hit #1 in January 1976.
- *Smokey and the Bandit* (1977) and *Convoy* the movie (1978) capitalized on it.
- "Breaker breaker 1-9" was in every household. **Handles** (CB nicknames) were a thing — dads picked them, kids picked them, truckers wore them like names.
- CB was technically licensed but **the FCC stopped enforcing** by 1976. Anyone with $40 could buy a base station.
- **Channel 19** was the trucker channel. **Channel 9** was emergency-only.
- Range: 4-10 miles typical. Atmospheric "skip" sometimes carried signals across continents — the magic of accidentally talking to a guy in Texas from Maryland.

**For Component M:** When Mark needs the CB crystal, he's not pulling from an obscure hobby. He's pulling from the most ubiquitous consumer electronics craze of the year. Half the dads on the block have a CB. The challenge is which one will give up a *crystal* (a specific frequency-controlling component, since some rigs needed multiple crystals to access different channels).

---

## 7. Heathkit and the build-it-yourself culture

Heathkit was a brand of mail-order electronics kits. From 1947 to 1992 they sold everything from radios to TVs to oscilloscopes to *aircraft instruments* in kit form. The 1976 catalog was an event — kids and dads read it like a wishlist.

**Why this matters:**
- A 2026 player doesn't grok kit culture. The idea that you could *build your own color TV* over a weekend is alien. This is a teaching surface.
- Mark Cole, future PO, can have a brief VO line about Heathkit when he sees the wall of kits at Burnsville. Something like *"In 2026 we don't build anything. We subscribe to it."*

---

## 8. The repair-don't-replace ethic (Mark's flagged point)

Mark called this out specifically. It's *the* defining difference between 1976 and 2026 consumer electronics culture.

- **TVs got fixed.** A TV repair guy made a house call, pulled the back off the console, swapped a bad tube or capacitor, billed you $15. The TV ran another 5 years.
- **Toasters got fixed.** Heating elements were user-replaceable.
- **Vacuums got fixed.** Belt swap, brush swap. You owned a vacuum for 20 years.
- **Stereos got fixed.** Channel sounds weak? Owner cleans the contact, replaces the resistor, you're back.
- **Radios got fixed.** Cars too.

**Curbside finds were treasure.** Trash day in 1976 = free parts day for a hobbyist kid. A broken TV on the curb was a transformer, a flyback, a half-dozen tubes, capacitors, knobs, the speaker — easily $30 worth of parts for free if you had the patience to strip it.

**For the game:** This unlocks the **TV salvage subquest** as an alternative to buying the backbone power supply. Player can:
- Pay full price for transformer + rectifier + cap at Burnsville (~the cost of 3-4 days of allowance)
- OR find a broken TV on the curb on a specific weekly trash day, strip it, salvage the parts for free (but takes time and the player learns *how* to strip a TV — era-teaching)

---

## 9. Pricing reference (rough 1976 dollars)

Useful for calibrating the money economy.

| Item | 1976 price | 2026 equivalent (rough) |
|---|---|---|
| Vacuum tube (common) | $1-$3 | $5-$15 |
| 555 timer IC | $0.50-$1 | $3-$5 |
| Aluminum project box (small) | $3-$5 | $15-$25 |
| Perfboard (4x6") | $1-$2 | $5-$10 |
| Power transformer (small) | $4-$8 | $20-$40 |
| Solder spool (1lb 60/40) | $5 | $25 |
| Hookup wire (spool 22ga) | $1-$2 | $5-$10 |
| Soldering iron (Weller pencil) | $15-$25 | $75-$125 |
| VOM (Simpson 260) | $90-$120 | $450-$600 — out of reach for a kid |
| CB base station (entry-level) | $80-$150 | $400-$700 |
| CB crystal (single channel) | $2-$5 | $10-$25 |
| Heathkit basic radio kit | $20-$40 | $100-$200 |
| Comic book | $0.25 | $1.25 |
| Candy bar | $0.15 | $0.75 |
| Movie ticket | $2.13 (US avg) | $11 |
| Allowance (typical 14-yo) | $2-$5/week | $10-$25 |

**Implication for the game:** A kid with a $3/week allowance saves for *weeks* to afford a basic chassis box. This is the *real* money pressure. The payphone-coin-return + lawn-mowing + can-returning + tube-testing loops aren't padding — they're how the machine gets built.

---

## 10. Where this feeds into the game

| Game system | What this doc supplies |
|---|---|
| `components/backbone.md` | The 4 backbone parts, sourcing, prices |
| `components/money-economy.md` (TBD) | Price calibration, kid earning rates |
| Burnsville Electronics location entry (TBD in `locations.md`) | Sensory detail, layout, NPC seed |
| Component G (cap gun + carbide) | Likely also touches Burnsville (caps) |
| Component M (CB crystal) | Heavy use — CB context, crystal mechanics |
| Component N (mercury switch) | Burnsville stocks glass tubing + the switch base hardware |
| Component L (soldering iron) | Direct buy at Burnsville |
| TV salvage subquest | Alternative path to backbone power supply |
| Era-teaching surface "Things were fixable" | Direct teaching surface |
| Era-teaching surface "Things were built from kits" | Heathkit wall reference |

---

## Open questions

1. **Burnsville layout.** Single room with counter + bins + back parts counter? Or two rooms (front sales + back salvage)? Affects how scenes block.
2. **Owner backstory depth.** Do we cast him now or keep `[BURNSVILLE-OWNER]` and develop later? (Lean: develop later when Mark is ready, per current NPC rule.)
3. **Tube tester as recurring mini-game.** Yes/no? (Lean: yes, light — it's a money loop AND a charming era beat.)
4. **TV salvage subquest weight.** One-shot, or recurring (Trash Tuesdays as a weekly opportunity)? (Lean: one-shot for the backbone, but if it lands well, recurring for spare cash.)
5. **Does Mark Cole (2026) recognize the store name?** Player-set hometown could trigger an extra VO line if they pick Baltimore — Easter egg. Probably too niche, but flag it.
6. **Other 1976 hobby brands to name-drop.** Heathkit is locked. Lafayette? Allied? Edmund Scientific? Probably 1-2 max so we don't overload.
