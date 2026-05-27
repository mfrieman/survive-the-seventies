# Components Index

> **Note (2026-05-26):** An active **v0.2 PROPOSAL** lives at [`../machine-rules-v0.2-proposal.md`](../machine-rules-v0.2-proposal.md). It proposes **12 components** (vs the 10 below), adds `O` (Foot X-Ray fluoroscope) and `Amb` (amber-with-inclusion) as full members, replaces `F` (Clackers) with a Polaroid SX-70 battery pack, and ungates `B` (vacuum) from glass-blowing. The 10-row table below is still **v0.1** and remains authoritative until the proposal is locked. Use the proposal file as the staging ground for swap ideas — including Mark's incoming new-part proposal.
>
> ---

> Per-component journey docs for the 10-part machine spine. Each component is its own file with the full quest journey, NPCs involved (kept generic for now — names filled in later), locations, dialog flavor, Tear impact, and era-teaching surface.
>
> **Status legend:** `DRAFT` = first pass written, `REVIEW` = Mark has reviewed, `LOCKED` = final.
>
> **NPC rule (current):** All NPCs in these docs are referenced by **role only** (e.g. "the vet at the end of the block", "older dealer kid", "antique store owner"). Specific names are deferred — we cast and name them later when we wire into `people.yaml`. The exception is locked existing NPCs (Marek family, Karras family, Kowalski family, Iwona's family).
>
> **No stealing rule:** Mark does not steal from people. The single exception is chrome valve-stem caps off parked trucks. Every quest's acquisition path must be FIND / TRADE / EARN / CRAFT — never theft.

---

## The 10

| # | Component | Source item | Mechanics | Act | Difficulty | Status | File |
|---|---|---|---|---|---|---|---|
| **L** | Soldering iron (workbench enabler) | Wood Burning Kit | FIND + cash | A1 (1st) | Easy | DRAFT v0.1 | [component-L-soldering-iron.md](component-L-soldering-iron.md) |
| **J** | Primary coil | Slinky | TRADE | A1 | Easy | DRAFT | [component-J-slinky.md](component-J-slinky.md) |
| **C** | Grounding spike | Lawn Dart tip | FIND + EARN | A1 | Easy-Med | DRAFT | [component-C-lawn-dart.md](component-C-lawn-dart.md) |
| **F** | Pendulum mass | Clackers | TRADE + CRAFT | A1 (close) | Easy | DRAFT | [component-F-clackers.md](component-F-clackers.md) |
| **N** | Mercury switch | Broken thermometers | FIND + CRAFT | A2 (1st) | Medium | DRAFT | [component-N-mercury.md](component-N-mercury.md) |
| **B** | Vacuum chamber | Gilbert Glass-Blowing Set | EARN-heavy + CRAFT | A2 | Hard | DRAFT | [component-B-glass-blowing.md](component-B-glass-blowing.md) |
| **K** | Rotational bearing | Swing Wing hub | FIND + CRAFT | A2 | Medium | DRAFT | [component-K-swing-wing.md](component-K-swing-wing.md) |
| **G** | Ignition primer **(HERO)** | Cap-gun caps + Austin Magic Pistol carbide | **ALL FOUR** | A2 | Hard | DRAFT | [component-G-ignition.md](component-G-ignition.md) |
| **M** | Comms relay crystal **(HERO)** | CB Radio | **ALL FOUR** | A2 (close) | Hard | DRAFT | [component-M-cb-radio.md](component-M-cb-radio.md) |
| **A** | Uranium core **(CAPSTONE)** | Gilbert U-238 Atomic Energy Lab | EARN + cash | A3 | Hardest | DRAFT | [component-A-uranium.md](component-A-uranium.md) |

---

## Combination rules (Mark's flag)

Mark flagged that some components — especially the "easy" ones — are not standalone challenges. They get used **in combination** with others. Document each component's combo hooks at the bottom of its file under **"Used by other components"**. Examples:

- **L (soldering iron)** is the *enabler* — every CRAFT step in components J, F, N, K, G, M, A requires the workbench L unlocked. Quest L is small; its *consequence* is massive.
- **N (mercury switch)** needs glass tubing from **B (glass-blowing set)** — so B must complete before N.
- **G (ignition)** needs **carbide** (Austin Magic Pistol) AND **caps** (cap gun) acquired separately, then combined.

Combos are tracked in each file's cross-reference section so we can untangle dependencies when we wire `quests.md`.

---

## Generic NPC roles in play (placeholders)

| Role token | Component(s) | When we cast/name | Notes |
|---|---|---|---|
| `[KID-WITH-SLINKY]` | J | When we draft kid-network | Probably one of the existing block kids |
| `[BACKYARD-LAWN-DART-OWNER-DAD]` | C | When we add a yard-owner NPC | Adult — guards garage |
| `[CLACKERS-OWNER-KID]` | F | When we draft kid-network | Probably an older sister type |
| `[THERMOMETER-SOURCE]` | N | When we draft adult-network | Pharmacist or school nurse |
| `[BURNSVILLE-MENTOR]` = **Stan Burns** | L, plus identification of mystery parts across A1-A2 | **LOCKED 2026-05-24.** Founder, ~65-70s, handed shop to son Steve, still works floor every day, lives to teach kids. Tier 3 / honest-humility-wins. See `worldbuilding-rules.md` Rule 10. | The third father. Warmest NPC in the game. |
| `[BURNSVILLE-OWNER]` = **Steve Burns** | background presence, comic interrupt | **LOCKED 2026-05-24.** Son, ~40s, current owner, excellent at it, proud of his dad, teases him warmly about retirement. Tier 2-3 floating. See Rule 10. | The success that frees Stan to teach. |
| `[SURPLUS-STORE-VET]` | B, G | **Mark developing now (2026-05-24): Vietnam vet, OWNS Military Surplus Store in Zone 2 of The Oaks.** Came back, built the business, turned the war's leftovers into a livelihood. Story-listening minigame TBD. Highest-stakes adult Mark Test in the game (the one adult who could actually understand the machine). Possible Tear-registers-here late-Act beat. | The "cool" character. Vietnam-era. Sovereign in his store. |
| `[OLDER-DEALER-KID]` | G, M | When we draft older-kid layer | The kid two grades up who has *everything* for a price |
| `[ANTIQUE-STORE-OWNER]` | A | When we draft Ocean Side trip | Ocean Side boardwalk antique shop |
| `[CB-DAD]` | M | When we decide Gus vs Dennis vs other | Adult with a CB rig |

When Mark is ready to flesh out a role, we promote the token → named NPC → entry in `people.yaml`.

---

## Tear cadence summary

| Component installed | Tear cost | Cumulative state |
|---|---|---|
| L | None (enabler only) | Stable |
| J | Tiny (first hum) | Stable |
| C | Small (lights flicker) | Mild |
| F | Small (clock skip) | Mild |
| N | Medium (smell of ozone, kitchen radio bleeds voices) | Noticeable |
| B | Medium (Bobby has nightmares he can't describe) | Noticeable |
| K | Large (Mark briefly speaks in Danny's voice, doesn't notice) | Visible |
| G | Large (Iwona "remembers" something that hasn't happened yet) | Visible |
| M | SEVERE (Comms 2 mask-drop — machine catches fire) | Crisis |
| A | CATASTROPHIC | Endgame |

---

## Open questions tracked at index level

1. Do "easy" components J, C, F need a friction beat each, or can two of them be a single "errand round" scene?
2. Mercury switch (N) currently uses broken thermometers — does it need a school-nurse subquest or is a single found-in-Halloween-junk-drawer beat enough?
3. Should component combos be visible to the player up-front (Book reveals dependency tree) or discovered (player builds and the machine rejects N until B is done)?
4. Capstone A (Ocean Side antique store) — is this a single trip, or does the family vacation thread weave through Act 2?
