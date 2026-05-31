# Quest-Item Tracker

> **Purpose:** Single source of truth for who gives what, what trades for what, and what machine part comes from which quest. Prevents over-coupling (every quest going through the same NPC) and orphan items (an item nobody wants).
>
> **Updated:** every time a quest is locked.

---

## NPC Hubs (GTA-style multi-yield characters)

Pattern: One NPC = multiple yields across multiple quests. Cap at 3 yields per NPC to avoid bottleneck.

| NPC | Yield 1 | Yield 2 | Yield 3 | Notes |
|---|---|---|---|---|
| **Elga** | Old papers stack (→ Playboy magazine) | Marijuana (→ VW-hippie-van quest) | — | Two quests, sequential |
| **Playboy Tony** | Lawn-chair gatekeeper (NOT a giver — barrier between player and Elga) | — | — | Time-gate NPC |
| **Tony Caruso** (14, band kid) | 12AX7 vacuum tubes (Signal Slot 7) | Marshall amp transformer (Signal Slot 4) | — | Both yield from Q-003 (band light-show favor). Band = recurring favor-faction; 2nd quest reserved (Q-IDEA-10) |
| **Pat the Vet** (Sonny's Surplus) | Surplus military battery (Good Power) | ❓ TBD ritual item? | — | Gas mask DROPPED 2026-05-30 (vapor pathway retired) |
| **Stan** (Burnsville Electronics) | Signal pathway teaching | SX-70 tip (via Danny comms) | — | Mentor, not item-source |
| **Denise** | Amber spiritual lore | Ritual-platform teaching + painted swap-altar board | — | Mentor; reactivates the platform |
| **Iwona** | Amber-with-inclusion necklace (Act 3) | Love-story arc | — | |
| ❓ **Boy Scout Friend** | Boy Scout uniform (lent for Paper Drive) | — | — | Needs character creation — see Q-001 |

---

## Tier Economy — What trades for what

| Tier | Item type | Example items |
|---|---|---|
| **Cash** | In-game money | Dollars from yardwork, paper route, errands |
| **Tier 1 — Common Trade** | Low-friction kid-economy currency | Baseball cards, marbles, soda bottles for deposit, matchbooks |
| **Tier 2 — Mid Trade** | Specific desirable items | Comic books, transistor radio, deck of cards, beer |
| **Tier 3 — Top Trade** | High-value taboo or scarce items | **Playboy magazine**, **Marijuana** (VW-hippie-van quest only), unopened fireworks |
| **Quest Currency** | Unique items only valid for specific trade | Boy Scout uniform (lent), specific ethnic grocery item, repaired TV |

**Rule:** A given machine part should NOT be obtainable by *more than one* trade currency. Each part has one canonical source. Player flexibility comes from *which parts they prioritize*, not from *which currency they spend*.

---

## Quest → Machine Part Mapping

| Quest ID | Quest | Primary Yield | Trades For (downstream) | Machine Slot |
|---|---|---|---|---|
| Q-001 | Elga Paper Drive | Playboy magazine + Old papers haul | → Q-004 (lawn-dart trade) | Enabler for Slot 10 |
| Q-002 | Elga Garden Cleanup | Marijuana | → VW-hippie-van quest (comedic payoff) | None — not a machine part |
| Q-003 | Showtime (Caruso Band Light Show) | Dead amp → 12AX7 tubes + Marshall transformer | Direct use (both) | Signal Slot 7 (Spirit Valve) + Signal Slot 4 |
| Q-IDEA-10 | 2nd Caruso Band quest (reserved) | ❓ TBD part or trade currency | ❓ TBD | ❓ TBD — add a part here if story needs more |
| ❓ | Pat the Vet — Power Cell | Surplus military battery | Direct use (Power Supply: Good tier) | Signal Slot 1 (controlled-option) |
| ❓ | Boy Scout Uniform Borrow | Uniform (lent, returned after Paper Drive) | Pre-req for Q-001 | None — enabler |

---

## 📋 CANDIDATE SLATE — drafted 2026-05-30 (to author next; binds open machine slots to inbox ideas)

> Demand side: of 16 blueprint slots, only Slots 4 + 7 are sourced (Q-003). This slate binds the
> remaining Act 1–2 Signal slots + the support economy to LIKELY inbox ideas. Act 3 slots (5 stones,
> U-238, amber) are already sourced in `machine-architecture.md` and get their own Act-3 quest pass.

| ID | Quest (working title) | Quest Tier | Archetype | Primary Yield | Fills Slot | Inbox src | Act |
|---|---|---|---|---|---|---|---|
| **Q-004** | Lawn-Dart Trade Chain | **T1 Part** (multi-item) | Part | Lawn-dart grounding rod | Signal 10 | Q-IDEA-04 (Playboy) | 1–2 |
| **Q-005** | Babysitting the Chaos Kid | **T1 Part** | Part/Favor | Slinky helical coil (the kid's toy = payment) | Signal 5 | Q-IDEA-05 | 1 |
| **Q-006** | Junkyard / Dumpster Run | **T1 Part** | Part | Ignition coil + found trade junk | Signal 3 | Q-IDEA-02 | 1–2 |
| **Q-007** | The Busted Walkie-Talkie | **T1 Part** (RECOVER) | Part | CB crystal + tuning knob | Signal 6 | (new) | 1–2 |
| **Q-008** | The Antique Shop | **T1 Part** (ACQUIRE, hero) | Part | Shoe-store X-ray tube | Signal 2 | (new NPC) | 2 |
| **Q-009** | Pat the Vet — Power Cell | **T1 Part** (RECOVER) | Part | Surplus military battery | Signal 1 (Good) | tracker | 2 |
| **Q-010** | Mom's Canning Shelf | **T1 Part** | Favor→Part | Mason jar vacuum chamber | Signal 8 | (Kay errand) | 1 |
| **Q-011** | Cap-Gun Carbide | **T1 Part** (RECOVER) | Part | Cap gun + carbide trigger | Signal 9 | Q-IDEA-06 spirit | 1–2 |
| **Q-012** | Paper-Route Help | **T3 Favor** | Favor | cash + free newspaper + friend warmth | — | Q-IDEA-01 | 1 |
| **Q-013** | Dumpster-to-Yard-Sale | **T2 Supply** (hub) | Favor | cash + trade stock (feeds Q-004/006) | — | Q-IDEA-02/03 | 1–2 |
| **Q-014** | Parent Errands (cigs/checks) | **T3 Favor** (recurring) | Favor | small cash + relationship currency | — | Q-IDEA-07 | 1–3 |

**Recommended authoring order:** Q-004 (proves multi-item trade chain + homes the Playboy) → Q-005
(clean single-slot comedy + a peer friend) → Q-013 (the supply hub that feeds the part quests).

---

## 🏷️ QUEST TIER TAXONOMY — proposed 2026-05-30 (parallels the 5-tier CHARACTER system)

> Mark wants quests tiered like characters. The tier is defined by **what completion does**, not by
> difficulty — so it's mechanical and unambiguous (mirrors how character tier = relationship/role weight).
> Keep it to **3 tiers** for now; expand only if real quests demand it.

| Quest Tier | Completion effect | Maps to archetype | Examples |
|---|---|---|---|
| **T1 — Part Quest** | Places a **component on the Blueprint** (Signal slot, stone, power, U-238, amber). The "main course." | Part / Muster | Q-003, Q-004–Q-011, the Act-3 set |
| **T2 — Supply Quest** | Yields **cash or a trade-currency item that a T1 quest consumes** (Playboy, found radio, beer). Exists to *feed* a T1. | trade-currency Favor | Q-001, Q-013; the Playboy sub-step inside Q-004 |
| **T3 — Favor Quest** | Yields **relationship warmth only** (read by the Note) → *unlocks* gated T1/T2 quests. No item, no part. | pure-warmth Favor | Q-012, Q-014 |

**Multi-item rule (Mark's question, answered):** a quest that needs several items to earn one part is
**still ONE T1 record** — it carries `requires_items: [...]` + a `§7 Trade Chain`. The sub-items it
consumes are typically **T2 Supply** quests/steps. One T1 quest, one part; many T2 inputs feed it.
This respects the anti-coupling rules (max 2 hops, one canonical source per part).

**Status:** PROPOSED — validate against Q-004/005/013 when authored, then lock into `quests/README.md`.

## Open Coupling Questions

- ~~**Who wants the Playboy magazine?**~~ ✅ RESOLVED 2026-05-30 — **Q-004 Lawn-Dart Trade Chain.** An older
  kid (neighbor's-shed archetype, NOT Pat/Tony Caruso) trades the **lawn-dart grounding rod (Signal Slot 10)**
  for the Playboy. This homes the Playboy *and* sources Slot 10 in one chain. Q-001 → Q-004.
- **What does the Boy Scout friend want?** ❓ Lower-tier trade. Candidates: baseball cards, comic books, matchbooks, a favor (covers his route one day).
- ~~**Secondary marijuana source?**~~ ✅ RESOLVED 2026-05-30 — exactly ONE marijuana quest, source = Elga only. Marijuana is no longer a machine ingredient (it feeds the standalone VW-hippie-van quest), so no safety-net is needed.

---

## Anti-Coupling Rules

1. **No NPC has > 3 yields.** Keeps the economy distributed.
2. **No item trades through more than 1 hop.** Player should never need: A → B → C → D → final part. Max 2 hops.
3. **Every Top Trade item (Tier 3) needs at least one NPC who wants it.** Otherwise it's clutter.
4. **Every machine part has exactly one canonical source quest.** Substitution comes from tiered controlled-options (Power Supply, Brew), not from multiple paths to the same part.
