# Quest-Item Tracker

> **Purpose:** Single source of truth for who gives what, what trades for what, and what machine part comes from which quest. Prevents over-coupling (every quest going through the same NPC) and orphan items (an item nobody wants).
>
> **Updated:** every time a quest is locked.

---

## NPC Hubs (GTA-style multi-yield characters)

Pattern: One NPC = multiple yields across multiple quests. Cap at 3 yields per NPC to avoid bottleneck.

| NPC | Yield 1 | Yield 2 | Yield 3 | Notes |
|---|---|---|---|---|
| **Elga** | Old papers stack (→ Playboy magazine) | Marijuana (Vapor brew) | — | Two quests, sequential |
| **Playboy Tony** | Lawn-chair gatekeeper (NOT a giver — barrier between player and Elga) | — | — | Time-gate NPC |
| **Tony Caruso** (14, band kid) | 12AX7 vacuum tubes (Signal Slot 7) | Marshall amp transformer (Signal Slot 4) | — | Both yield from Q-003 (band light-show favor). Band = recurring favor-faction; 2nd quest reserved (Q-IDEA-10) |
| **Pat the Vet** (Sonny's Surplus) | Gas Mask + Hose | Surplus military battery (Good Power) | ❓ TBD secondary brew? | |
| **Stan** (Burnsville Electronics) | Signal pathway teaching | SX-70 tip (via Danny comms) | — | Mentor, not item-source |
| **Denise** | Amber spiritual lore | Vapor pathway teaching | — | Mentor, not item-source |
| **Iwona** | Amber-with-inclusion necklace (Act 3) | Love-story arc | — | |
| ❓ **Boy Scout Friend** | Boy Scout uniform (lent for Paper Drive) | — | — | Needs character creation — see Q-001 |

---

## Tier Economy — What trades for what

| Tier | Item type | Example items |
|---|---|---|
| **Cash** | In-game money | Dollars from yardwork, paper route, errands |
| **Tier 1 — Common Trade** | Low-friction kid-economy currency | Baseball cards, marbles, soda bottles for deposit, matchbooks |
| **Tier 2 — Mid Trade** | Specific desirable items | Comic books, transistor radio, deck of cards, beer |
| **Tier 3 — Top Trade** | High-value taboo or scarce items | **Playboy magazine**, **Marijuana** (ingredient only), unopened fireworks |
| **Quest Currency** | Unique items only valid for specific trade | Boy Scout uniform (lent), specific ethnic grocery item, repaired TV |

**Rule:** A given machine part should NOT be obtainable by *more than one* trade currency. Each part has one canonical source. Player flexibility comes from *which parts they prioritize*, not from *which currency they spend*.

---

## Quest → Machine Part Mapping

| Quest ID | Quest | Primary Yield | Trades For (downstream) | Machine Slot |
|---|---|---|---|---|
| Q-001 | Elga Paper Drive | Playboy magazine + Old papers haul | ❓ TBD top-tier machine part | TBD Signal slot |
| Q-002 | Elga Garden Cleanup | Marijuana | Direct use (Vapor brew tier) | Vapor Slot 13 |
| Q-003 | Showtime (Caruso Band Light Show) | Dead amp → 12AX7 tubes + Marshall transformer | Direct use (both) | Signal Slot 7 (Spirit Valve) + Signal Slot 4 |
| Q-IDEA-10 | 2nd Caruso Band quest (reserved) | ❓ TBD part or trade currency | ❓ TBD | ❓ TBD — add a part here if story needs more |
| ❓ | Pat the Vet — Gas Mask | Gas Mask + Hose | Direct use | Vapor Slot 11 |
| ❓ | Boy Scout Uniform Borrow | Uniform (lent, returned after Paper Drive) | Pre-req for Q-001 | None — enabler |

---

## Open Coupling Questions

- **Who wants the Playboy magazine?** ❓ Must NOT be Pat the Vet (already hub) or Tony Caruso (already hub). New NPC needed — probably a teenager Mark trades with for a Signal-pathway part. Candidates: junkyard older kid, antique-shop kid, the pyromaniac kid (Q-IDEA-06), Tony Caruso's older brother (paper-route money kid).
- **What does the Boy Scout friend want?** ❓ Lower-tier trade. Candidates: baseball cards, comic books, matchbooks, a favor (covers his route one day).
- **Secondary marijuana source?** ❓ For safety-net (player who skips Elga). Don't gate Vapor brew hard.

---

## Anti-Coupling Rules

1. **No NPC has > 3 yields.** Keeps the economy distributed.
2. **No item trades through more than 1 hop.** Player should never need: A → B → C → D → final part. Max 2 hops.
3. **Every Top Trade item (Tier 3) needs at least one NPC who wants it.** Otherwise it's clutter.
4. **Every machine part has exactly one canonical source quest.** Substitution comes from tiered controlled-options (Power Supply, Brew), not from multiple paths to the same part.
