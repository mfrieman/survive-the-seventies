# Money Economy — How Mark Earns (and What Things Cost)

> **Status:** DRAFT v0.1
> **Purpose:** The substrate under the backbone. Mark needs cash to buy chassis parts at Burnsville Electronics, plus secondary cash sinks across the game. This doc defines the earning loops, the cost ledger, the pacing, and the **quests that live inside the money economy.**
>
> This isn't a spreadsheet. The numbers here are *design intent* — what FEELS right for a tight 5-hour game. We'll calibrate against playtest later.

---

## 1. Design philosophy

**Three rules:**

1. **Money pressure is real, but money grind is not.** The player should feel pinched 3-4 times across the game, never bored. Earning loops are interesting *as gameplay,* not as repetitive grinding.
2. **Every earning loop teaches something about 1976.** Bottle returns, payphone coin-return, lawn mowing, tube testing — each one is also an era-teaching surface. The economy *is* the time machine.
3. **No stealing.** Per locked rule. The chrome-valve-cap exception is **trade currency**, not cash. Mark never pockets money he didn't earn.

**The pressure curve we're aiming for:**

```
$ tight    ~~~~~~~~/\~~~~~~~~~~~~~/\~~~~~~~~~~~/\~~~~~
$ flush                /             /                /
            A1 start   L purchase    Power supply    A2 hero parts
```

Three big purchase moments where money is *tight* and the player feels it. Between them, slack — but never *too much* slack, or the loops become pointless.

---

## 2. The earning loops (in order of unlock)

### Loop 1 — Allowance (passive)

- **Rate:** $3/week. Comes from Dennis every Friday evening, kitchen table scene.
- **Unlock:** Day 1.
- **Era teaching:** Allowance was a *real conversation* in 1976. Dad pulled bills out of his wallet, counted them out, made a small comment. This wasn't an automated transfer.
- **Scene beat:** Recurring Friday-night allowance moment. Sometimes Dennis adds a quarter for a chore done well. Sometimes he docks for a screwup. **Variable allowance** = light gameplay layer. Quiet relationship development with Dennis (the otherwise-quiet sheetrocker dad — see decisions-log).
- **Quest hooks:** Mark's relationship with Dennis develops through this loop. Late-game beat: Dennis hands Mark a $5 bill, no explanation. *"Don't tell your mother."* Player learns Dennis has been quietly noticing.

### Loop 2 — Payphone coin-return scrounge

- **Rate:** $0.05–$0.50 per find. Random.
- **Frequency:** Pings appear at payphone locations on the map. Maybe 1-2 per in-game day if Mark passes them.
- **Unlock:** Day 1, but the *technique* is taught — Bobby or Mickey shows Mark the trick of slamming the coin return slot just so.
- **Era teaching:** Payphones existed everywhere. Kids checked them obsessively. Sometimes someone made a call, hung up, and the change rattled into the slot but stuck. Free money for the kid who walked by next.
- **Scene beat:** First time the player checks one and gets nothing. Second time, a dime. *"Hell yeah."*
- **Quest hooks:**
  - **"The Payphone Route"** (passive ambient — adds a payphone map layer, ~5-7 phones scattered around the playable world, each refreshes daily).
  - **Tie-in to existing quest seed "Payphone-as-receiver"** — one specific payphone is the one a contact calls Mark on for a mission. Same map, different use.

### Loop 3 — Bottle returns

- **Rate:** $0.02 per bottle. (Some states had $0.05 — we use $0.02 as more authentic to Maryland in 1976. Before bottle-deposit laws expanded.)
- **Frequency:** Bottles found roadside, in alleys, in friends' garages.
- **Unlock:** Day 2-3, after Mark notices Mickey carrying a sack.
- **Era teaching:** Glass bottles had real return value. Kids scoured roadsides, especially after weekends. Coca-Cola, RC, beer bottles — all returnable to grocery stores or corner stores. The aluminum-can-recycling era hadn't started yet — these were **glass deposit bottles.**
- **Scene beat:** Mark hauls a sack of clinking bottles to the corner store. Owner counts them out one by one. Hand cramps from gripping a heavy sack of glass. *"$1.40. Don't drop them on the way out, kid."*
- **Quest hooks:**
  - **"Saturday Morning Bottle Run"** — recurring opportunity. Saturday mornings, the roadside yields the previous night's empties. Best harvest day.
  - **Discoverable hot-spots:** Behind the bowling alley, the alley behind the bar, the high school football field bleachers Monday after a Friday game. Each location yields more per visit but requires the player to *find* it.
  - **Risk/cost variant:** Some bottles are by the highway — Mark VO recoils: *"In 2026 a kid would not be walking the shoulder of a state highway alone for forty-two cents."* Era-teaching beat.

### Loop 4 — Chores for Kay (or neighbors)

- **Rate:** $0.25–$1.00 per chore depending on size.
- **Frequency:** 1-2 per day max.
- **Unlock:** Day 1 (Kay asks Mark to do things; he gets paid for the bigger ones).
- **Era teaching:** Kid labor was *normal* and *cheap*. Adults asked kids to do things and paid them in coins, not gratitude. Mowing the neighbor's lawn for $3 was a real job for a 14-year-old.
- **Scene beat:** Kay hands Mark a list. *"Hardware store. Two D-cell batteries, a roll of duct tape. Here's three dollars. You can keep the change if you don't take all day."* Mark VO: *"In 2026 my mom would have ordered this from Amazon during the conversation."*
- **Quest hooks:**
  - **"The Hardware Store Run"** — repeating errand. Mark walks 3 blocks each way, has the chance to swing by Burnsville on the same trip (it's near the hardware store).
  - **Variant: Kay forgets to ask for change back** — small moral test. Player can keep the extra OR return it. Tone-flagged for the no-cruelty rule. Lean: returning gets a tiny relationship tick with Kay, keeping is fine but Mark VO notes it.

### Loop 5 — Lawn mowing (EARN — proper quest)

- **Rate:** $3-5 per lawn.
- **Frequency:** 1 per weekend max — physical exhaustion + neighbor availability.
- **Unlock:** Day 3-4, after Mark sees someone else mowing for cash.
- **Era teaching:** Kid lawn-mowing was an *enterprise*. You knocked on doors, you offered, you came back next week. The gas mower was loud, hot, and *yours to operate as a 14-year-old.* OSHA was 5 years old and no one cared.
- **Scene beat:** First time mowing a neighbor's yard. Mark grips the rope-pull starter, yanks three times, the engine catches with a roar of two-stroke smoke. *"Holy hell."* Pushes the heavy mower across the yard for 45 in-game minutes (compressed in real-time). Neighbor hands him $4 cash and a glass of Tang.
- **Quest hooks:**
  - **"The Mowing Route"** — Mark builds a recurring weekend client list across Act 1-2. Three regular neighbors = guaranteed $9-12/weekend. **Direct funding source for the power supply purchase.**
  - **The picky client** — one neighbor pays *more* but is impossible to please. Stripes, no missed edges. *"You missed a spot."* Tone: comedic but kindly. Could be Mr. Caruso (existing).
  - **The "you didn't ask for a deposit" client** — neighbor stiffs Mark on payment first time. Mark VO: *"I forgot people could just… not pay me. In 2026 Venmo wouldn't let this happen."*
  - **The lawn-mower-shared-with-Dennis subplot** — Mark borrows Dennis's mower; if Mark breaks it, that's a money sink AND a Dennis-relationship hit.

### Loop 6 — Tube testing at Burnsville (mini-loop tied to TV salvage)

- **Rate:** $0.10–$0.25 credit per good tube tested + sold back to owner.
- **Frequency:** Limited by tube supply (curbside TV salvage, asking dads for old tubes).
- **Unlock:** Act 1 mid, after Mark's first Burnsville visit.
- **Era teaching:** Tube tester at the counter is real; owners actually bought back good tubes for resale. Closed-loop economy.
- **Scene beat:** First time the owner teaches Mark to read the tube tester. Mark brings in a sack of tubes from a salvaged TV. Most are dead. Three test "GOOD." Owner gives him $0.45 credit and a nod. *"Not bad, kid."*
- **Quest hooks:**
  - **Tied directly to the TV salvage subquest** for the backbone power supply. The TV's tubes become both cash AND parts.
  - **The rare-tube find** — once across the game, Mark salvages a tube that the owner *really* wants (an obscure type that's hard to source). $2-3 credit + a small relationship beat (*"Where'd you get this?"*).

### Loop 7 — Found-money one-shots

- **Rate:** $0.10–$5.00.
- **Frequency:** Scripted events across Acts 1-2, maybe 4-6 total.
- **Unlock:** Throughout.
- **Era teaching:** Kids in 1976 *found* things. Loose change in the couch cushions, a dollar bill in the gutter, a wallet on the sidewalk.
- **Scene beat:** One specific big one is **the wallet** — Mark finds a wallet on the sidewalk near Burnsville. Inside: $12 and the ID of an older guy from a few blocks over.
- **Quest hooks:**
  - **"The Wallet" (moral test)** — Player can:
    - **Return it** — small reward ($2 + thank-you), relationship tick with a new minor NPC (could be developed into something), Mark VO line about decency.
    - **Keep the cash, ditch the wallet** — get $12 cash, no consequences mechanically, but Mark VO carries a small ugly note about it that doesn't go away. *"I told myself he probably had money. He probably did. Doesn't matter."* The line gets a callback in Act 3.
    - **Keep it all** — $12 + the wallet, additional Mark VO weight. *No mechanical Tear penalty* (would trigger hoarding/anxiety per Mark Test). Surfaces as ending-texture nudge only.
  - **The "couch change" mini-event** — Mark searching the Marek couch finds $0.85 in change and a dead AA battery. Small comedic beat.

### Loop 8 — Trade-currency conversions (indirect)

- **Rate:** Variable.
- **Mechanic:** Mark can sometimes convert *trade items* (baseball cards, candy cigs, comics) to cash by selling them to other kids. **He sells his own** — never others'.
- **Era teaching:** Kids ran little dealer economies. The kid with the rare card had cash flow.
- **Quest hooks:** Lean — don't over-build this. It's flavor, not a primary loop. Maybe one scripted "sell your stack of doubles" event.

---

## 3. The cost ledger (what Mark has to buy)

### Required purchases (machine-critical, must-do path)

| Item | Cost | Component | Notes |
|---|---|---|---|
| Soldering iron | $20 | L | Biggest single Act 1 purchase |
| Chassis box | $4 | Backbone | |
| Perfboard | $2 | Backbone | |
| Power supply parts | $12 | Backbone | Free if salvage path taken |
| Solder + wire (initial) | $3 | Backbone | |
| Solder + wire (top-up x2) | $4 total | Backbone | Across Act 2 |
| CB crystal | $4 | M | Burnsville |
| Misc small parts | $3-5 | Various | Resistors, capacitors as needed |
| **Gilbert U-238 lab** | **TBD ~$25-40** | A | **The big capstone purchase — Ocean Side antique store, Act 3** |

**Required total (buy path):** ~$77-92
**Required total (salvage path):** ~$65-80

### Optional/flavor purchases (cash sinks for ambiance)

| Item | Cost | Notes |
|---|---|---|
| Comic books | $0.25 each | Mark VO beats; ambient |
| Candy cigarettes | $0.10 / pack | Both ambient AND trade currency |
| Baseball card packs | $0.15 / pack | Both ambient AND trade currency |
| Movie ticket (theater scene) | $2.13 | Story scene if needed |
| Burgers / fries at the diner | $0.50-$1 | Diner scenes if needed |

### Trade-currency stockpile (cash → trade-leverage)

Optional but useful — Mark can pre-buy candy cigs, baseball cards to use as TRADE currency in component quests J and F. Buys flexibility.

---

## 4. Total earning vs. spending math (rough)

**5 hours of play, ~10 in-game days compressed:**

| Loop | Avg per day | Days active | Total |
|---|---|---|---|
| Allowance | $0.43 ($3/wk) | 10 | $4.30 |
| Payphone coin return | $0.30 | 10 | $3.00 |
| Bottle returns | $0.50 (mostly Sat) | 10 | $5.00 |
| Chores for Kay | $0.50 | 10 | $5.00 |
| Lawn mowing | $1.50 (weekends only) | 10 | $15.00 |
| Tube testing | $0.20 | 5 | $1.00 |
| Found-money (scripted) | — | — | $15-20 (across game) |
| **Total** | — | — | **~$48-53** |

**Spending need:** $77-92 (buy) or $65-80 (salvage).

**Gap:** ~$15-30. Closed by:
- The wallet event (player keeps it = $12)
- The Friday-night Dennis $5 bonus
- One or two scripted "neighbor pays extra" events
- Selling personal trade items if player engages

**This means salvage path + one moral compromise OR salvage path + diligent grinding both reach the budget.** Buy path + no moral compromises is *intentionally* slightly tight, requiring the player to engage with more loops. This is the design.

---

## 5. Quests inside the money economy (Mark — this is your "good place for quests" payoff)

The earning loops aren't just resource taps. Several have full quest arcs:

### Quest M1 — "Saturday Morning Bottle Run"

Recurring weekend opportunity. Three locations to discover. Each discovery is a small social interaction (Mickey tells you about behind-the-bowling-alley, an older kid mocks you about the bleachers, etc.). Discovering all three locks in a steady weekend income. **Difficulty:** Easy. **Reward:** ~$2-3/weekend.

### Quest M2 — "The Mowing Route"

Build a recurring client list. Knock on doors. Three regulars = guaranteed weekend cash. Includes the **picky client** (perfection beat), the **stiff client** (you didn't get paid beat), and the **shared-mower-with-Dennis** dependency. **Difficulty:** Medium. **Reward:** ~$9-12/weekend.

### Quest M3 — "The Wallet"

Sidewalk find near Burnsville. Three-branch moral choice. **Determines Tear cost on next component install.** Has a callback line in Act 3. **Difficulty:** N/A — pure choice. **Reward:** $2 (return) / $12 (keep cash) / $12+wallet (keep all + Tear penalty).

### Quest M4 — "The Hardware Store Run" (recurring)

Kay's errand. Repeating. The route happens to pass Burnsville, which means Mark can pop in. Small dialogue beats with Kay. Sometimes she sends Mark with a list that includes a part Burnsville sells cheaper — moral micro-test (tell her, or pocket the savings as a kid-tax). Lean: telling her earns a relationship tick, pocketing is fine but noted.

### Quest M5 — "Trash Tuesday TV Salvage" (one-shot, tied to backbone power supply)

The big era-teaching scene. Mark learns the schedule, finds a curbside console TV, drags pieces home, strips them at the workbench. Burnsville owner teaches tube extraction. Risk beat: the picture tube vacuum implosion and the **lethal capacitor charge** — real era danger. The Book or the owner warns Mark. Player who skips the warning gets a comedic-but-pointed Mark VO ZAP and a brief stun. **Difficulty:** Medium. **Reward:** Free power supply parts + ~$0.45 in tested-tube credit.

### Quest M6 — "The Tube-Tester Apprenticeship"

Optional small arc. Mark spends time at Burnsville with the owner learning the tube tester properly. Three short scenes. Final scene: owner teaches Mark to read schematic symbols. Unlocks a small ability — Mark can now identify oddball parts at curbside finds. Relationship beat with `[BURNSVILLE-OWNER]`. **Difficulty:** Light EARN (time investment). **Reward:** Identification skill + small relationship.

### Quest M7 — "Dennis at the Kitchen Table"

Recurring Friday-night allowance. Across the game, the conversation grows. Dennis goes from "$3, here you go" → noticing Mark seems different → asking quiet questions Mark can't answer → late-game handoff of $5 with no explanation. Background relationship arc keyed to the money loop. **Difficulty:** N/A — emergent. **Reward:** Variable allowance + Dennis bond.

---

## 6. UI / display

**The change jar.** Mark's money lives in a glass jar on his dresser. Bedroom scene shows it filling up. **Visible currency.** No abstract number — Mark counts it out before each major purchase. Counting scene at the kitchen table = small mini-game (drag coins into stacks of $1) OR auto-counted with a slow reveal.

**At Burnsville:** Owner counts the bills back. Period-correct register that *rings*.

**Quick view UI:** Bottom-corner persistent display showing current $$ — but stylized as a small icon of the jar, not a digital number. Period feel.

---

## 7. Pacing — the three pinch points

**Pinch 1 — Early Act 1, ~30 min in.**
Mark needs the soldering iron ($20). Has $4 from his pocket. Tutorial pinch — forces engagement with Loops 1-3 (allowance, payphone, bottle returns). Resolves in ~30-45 min real time. **First taste of money pressure.**

**Pinch 2 — Act 1→2 transition, ~2 hours in.**
Power supply decision point. Either save $12+ OR commit to the TV salvage subquest. **Player choice = pacing fork.** Resolves in ~30 min real time either way.

**Pinch 3 — Act 3 prep, ~4 hours in.**
The Gilbert U-238 capstone. Big chunk of cash needed. Forces final money push. **The wallet event** is positioned here so the player feels the temptation acutely. *Do I save more weekends, or do I just take the $12?* The game's moral spine is RIGHT at this moment.

---

## 8. Open questions

1. **Variable allowance — keep or simplify to flat $3?** (Lean: variable. Builds Dennis arc for free.)
2. **The wallet event — exact Tear cost calibration.** Has to be feelable but not punishing.
3. **Couch change as one-shot or repeatable random?** (Lean: one-shot. Repeatable feels grindy.)
4. **Burnsville prices on-screen visible** or hidden until counter? (Lean: visible — period-correct hand-written price tags on the shelves.)
5. **Are there any cash-IN events that violate the no-stealing rule we need to police?** (Currently: no. Confirm.)
6. **Bobby's "can I have a quarter" mechanic — keep or cut?** (Lean: keep as one comedic recurring beat, capped at 3 across game. Player can give or refuse.)
7. **Does the player ever run out of money in a way that blocks progress?** (Lean: no. Always at least one earning loop available. Pacing pressure, not actual blocker.)
8. **The picky-client lawn quest — assign to Mr. Caruso (existing) or a new NPC?** (Lean: Mr. Caruso. Reuses canon, gives Caruso household real screen time.)

---

## 9. Cross-references

- `components/backbone.md` — primary cash sinks
- `components/index.md` — sibling docs
- `quest-seeds.md` — original seeds for payphone coin return, lawn mowing, etc.
- `era-research/kid-valuables.md` — trade currency context
- `era-research/kid-culture-70s.md` — ambient money culture
- `era-research/hobby-electronics-1976.md` — Burnsville pricing
- `decisions-log.md` — No-stealing rule (2026-05-24)
- `story-arc.draft.md` — Acts 1-3 (pacing pinch points align with arc beats)
