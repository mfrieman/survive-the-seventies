# Canon Review Packet — *Survive the 70s*

> **Status:** REVIEW TOOL · assembled 2026-05-30 · companion to [`design-spine.md`](design-spine.md)
> **Purpose:** The single place to review the whole design and decide what to lock next.
> Up to now we've been *generating* ideas. This packet is the pivot to *organizing and finishing* them.
>
> **How to use it:**
> - **Part 1** = the doc map (what exists, its status, one-line summary). Use for *retrieval*.
> - **Part 2** = the Open Decisions Register — **every unresolved decision in the whole design, in one list, prioritized.** Use for *review & prioritization*. This is the heart of the packet.
> - **Part 3** = two structural calls that gate further cleanup (need your ruling).
> - **Part 4** = the recommended lock sequence to drive the "full design" phase.

---

## Part 1 — Canon Doc Map

Status legend: 🔒 LOCKED · 📝 DRAFT · 🟡 PROPOSAL (needs lock) · 📖 LIVING · 🗄️ STALE/ARCHIVE · 🧭 INDEX

### Index / spine
| Doc | Status | One-line |
|---|---|---|
| `design-spine.md` | 🧭 INDEX | Canon entry-point: 4 pillars, system map, quest archetypes, NPC tiers, doc map, open loops. Read first each session. |
| `canon-review-packet.md` (this) | REVIEW TOOL | The review/prioritization layer over the spine. |

### Story (narrative canon)
| Doc | Status | One-line | Open |
|---|---|---|---|
| `premise.md` | 🔒 LOCKED v1 | Logline, two leads, 3-act shape, romance arc, thematic pillars, ending twist. | 9 |
| `story/00-opening.md` | 🔒 CANON (structure) | Beat-by-beat opening: 2027 bedroom → smoke detector → "READ ME" → title card. | 3 |
| `story/01-act1.md` | 🔒 CANON (structure) | "The Detective Game" — knowledge-as-progression, house-as-hub, soft-gate Zone 2. | 6 |
| `story/02-act2.md` | 🔒 CANON (structure) | "Scavenge, Craft, Fall in Love" — comms open, Tear escalates, dance, all-hope-lost fire. | 5 |
| `story/03-act3.md` | 🔒 CANON (structure) | Oceanside — science kit, amber auth tests, Bicentennial concert kiss, swap fires. | 6 |
| `story/04-ending.md` | 🔒 CANON (structure) | 2027 wake, Lamborghini reveal, bootstrap paradox, sequel hook + stinger. | 5 |
| `story-arc.draft.md` | 📝 SCRIPT LAYER | **Reclassified, not archived.** Fleshed-out cut-scene dialogue (The Jump, dance, ending). Folds into act files. 3 conflicts flagged in its header. | fold + 3 conflicts |
| `scene-outlines.md` | 🗄️ ARCHIVED | Pre–body-swap 5-scene demo. Moved to `archive/` 2026-05-30. | — |

### Components (the machine)
| Doc | Status | One-line | Open |
|---|---|---|---|
| `components/machine-architecture.md` | 🔒 RECONCILED 2026-05-30 | **THE canon machine.** 16 slots = 10 Signal + 5 stones + 1 amber. Path 2 = ritual platform. | few |
| `components/second-pathway-ritual-platform.md` | 🟡 PROPOSAL | Path-2 design (body-on-painted-board altar). Machine spec folded to canon; story impacts pending. | 2 |
| `components/backbone.md` | 🔒 | Path-1 hobbyist chassis + money layer (perfboard/aluminum box under the toy parts). | — |
| `components/index.md` | ⚠️ REVIEW | Old 10-letter (L–J–C…) scheme. Superseded as *spine* by machine-architecture, but still referenced by component-J/L, money, tear, worldbuilding. **Reconcile refs before archiving.** | (reconcile) |
| `components/component-L-soldering-iron.md` | 📝 detail | Per-part detail doc (soldering iron) on the old letter scheme. Review vs new 16-slot model. | review |
| `components/component-J-slinky.md` | 📝 detail | Per-part detail doc (Slinky coil) on the old letter scheme. Review vs new 16-slot model. | review |

### Systems / mechanics
| Doc | Status | One-line | Open |
|---|---|---|---|
| `components/relationship-instrument.md` ("the Note") | 🟡 PROPOSAL | Tuning-fork relationship sense (sound, not a number). Never formally locked. | 9 |
| `components/tear-system.md` | 🔒 LOCKED v1 | 3-tier Tear pressure (time → favor → memory burn). | 2 |
| `gameplay-loop.md` | 📝 DRAFT v0.1 | Day-clock loop, HUD minimalism, notebook UI, workbench craft. | 6 |
| `components/money-economy.md` | 📝 DRAFT v0.1 | Kid-economy income vs machine-part spend (~$48–53 vs ~$77–92). | 1 |

### World
| Doc | Status | One-line | Open |
|---|---|---|---|
| `world.md` | 🔒 | Parody bible — F-is-for-Family naming rules + Standing Parody List (locked). | 5 |
| `world-map.md` | 🔒 | Old Bay County geography — 3 zones, ~30 places, Synty-pack-verified. | 5 |
| `worldbuilding-rules.md` | 📖 LIVING | Structural 1976 rules ("Every Store Has An Owner"). | ~3 |
| `house-decor-catalog.md` | 📚 REFERENCE | Period interior-decor catalog (set-dressing source material). | — |

### Characters
| Doc | Status | One-line | Open |
|---|---|---|---|
| `characters/README.md` | 🔒 CANON (system) | 3-tier model (Prime/Supporting/Ambient) + state-driven dialog authoring rules. | — |
| `characters/roster.md` | 📝 DRAFT living | Prime P1–P6 mostly cast; **P7 proposed, P8–P12 open.** Supporting/Ambient seeded. | 4 |

### Quests
| Doc | Status | One-line | Open |
|---|---|---|---|
| `quests/README.md` | 🔒 (process) | Idea→Q-NNN promotion path, naming, status legend. | — |
| `quests/_quest-item-tracker.md` | 📝 bridge | NPC hubs, quest→part map, tier economy, anti-coupling rules. Repointed for dropped vapor. | — |
| `quests/Q-001-elga-paper-drive.md` | 🔒 | Paper-drive favor (relationship/collectible). | — |
| `quests/Q-002-elga-garden.md` | 🔒 | Garden favor; marijuana repoints to VW-hippie-van quest (not a part). | — |
| `quests/Q-003-caruso-band-light-show.md` | 📝 DRAFT | Teaching quest (wish→scavenge→assemble→power-on); pays 2 Signal slots (amp). | 6 |

### Production
| Doc | Status | One-line | Open |
|---|---|---|---|
| `production/asset-plan.md` | 🔒 Art line LOCKED | Synty POLYGON only; 80 packs verified; SyntyPass; ~6 custom hero props (Iwona). | 1 |
| `production/learning-plan.md` | 📝 Reference | Unity + Adventure Creator ramp; Mark logic / Iwona scenes. | — |
| `production/ai-assets-evaluation.md` | Advisory | Synty = backbone, AI = helper (textures/2D), re-evaluate at port. | — |
| `build/renpy-first-night.md` | 📝 build | Ren'Py prototype scaffolding notes (first playable night). | — |
| `decisions-log.md` | 📖 RECORD | Chronological locked-decision ledger (~15+ entries). | — |

---

## Part 2 — Open Decisions Register

**Every unresolved decision across the design, in one place.** Grouped by area, tagged by priority:

- **P1 — Blocker / structural:** locks or rulings that block organizing or building the first slice.
- **P2 — Design-shaping:** shapes multiple downstream pieces; lock before mass-authoring.
- **P3 — Detail / deferrable:** nameable later, often "calibrate in prototype." Don't let these stall P1/P2.

### A. Machine (mostly settled)
| # | Decision | Pri | Source |
|---|---|---|---|
| A1 | Confirm `second-pathway-ritual-platform.md` story impacts (basement opening rework) | P2 | ritual §9 #1/#3 |
| A2 | Lock the ritual-platform proposal itself (machine spec already in canon; this is the prose home) | P2 | ritual |
| A3 | **Reconcile `components/index.md`** — repoint component-J/L, money, tear, worldbuilding refs off the old 10-letter scheme onto `machine-architecture.md`'s 16-slot model, *then* archive index.md. Load-bearing until then. | P2 | index.md |

### B. The Note / relationships (PROPOSAL — top P1 lock)
| # | Decision | Pri | Source |
|---|---|---|---|
| B1 | **Lock "the Note" as the relationship mechanic** (currently proposal) | P1 | rel-instrument |
| B2 | Denise gift-beat order vs Act 1 | P2 | rel #1 |
| B3 | Audible-tier granularity per channel (how many distinguishable states) | P2 | rel #2 |
| B4 | Does the Note read Iwona? (recommend "strange/overwhelmed" to protect romance) | P2 | rel #4 |
| B5 | Band-debut Muster threshold (~10 kids) | P2 | rel #5 |
| B6 | Down-state floor — cold vs dead/hostile | P3 | rel #6 |
| B7 | Denise's in-world term for the Note | P3 | rel #7 |
| B8 | Accessibility: Book-waveform visual + subtitle cues | P3 | rel #3 |
| B9 | Calibrate warmth thresholds in-engine | P3 | rel #8 |
| B10 | Update machine-architecture Denise section (knowingly built Path 2; senses Mark≠Danny from Act 1) | P2 | rel #9 |

### C. Story structure & narrative authority
| # | Decision | Pri | Source |
|---|---|---|---|
| C1 | **Narrative authority — RESOLVED 2026-05-30 as role-split:** `story/00–04` = canon **beat structure**; `story-arc.draft.md` = the **script layer** (cut-scene dialogue). Draft kept, not archived. | ✅ done | spine §10a #2 |
| C1a | **CONFLICT — Kay smoke-detector exchange:** `00-opening` has SHORT version; draft Beat 3 has LONGER version. Both marked "verbatim." Pick one. | P2 | draft header |
| C1b | **CONFLICT — Act-1 closing comms line:** `01`/`02` agree *"I'm scared/get me home" → "Same, I hate it here too"*; draft ends Act 1 on *"How hard can it be." / "You have no idea."* | P2 | draft header |
| C1c | **CONFLICT — Mark's home year:** draft says **2026**; act files say **2027**. | P1 | draft header |
| C1d | **Scene-by-scene fold:** migrate draft's unique full scenes (The Jump, dance, all-hope-lost mechanic, Lamborghini ending, Era Teaching System) into the lean act files. | P2 | draft fold |
| C2 | `scene-outlines.md` → archive (self-declared stale) — **DONE, moved to `archive/`** | ✅ done | spine §10a #3 |
| C3 | Basement opening rework (00-opening) per ritual-platform proposal | P2 | ritual §9 #1 |
| C4 | Act-1 home-base scene (01-act1) per ritual-platform proposal | P2 | ritual §9 #3 |
| C5 | Year-reveal method in opening (implicit vs calendar line vs hold) | P3 | 00-opening |
| C6 | When Mark realizes PAL is gone | P3 | 00-opening |
| C7 | Zone-2 soft-gate method (knowledge / mom / bike — recommend stack all 3) | P2 | 01-act1 |
| C8 | When Iwona & Denise first appear in Act 1 | P2 | 01-act1 |
| C9 | "Enough installed to open comms" threshold signal | P2 | 01-act1 |
| C10 | Starting money amount | P3 | 01-act1 |
| C11 | Act-2 Iwona-arc vs machine-arc beat braiding | P2 | 02-act2 |
| C12 | Swap-switch presented as player choice? "wait" option? | P2 | 02-act2 |
| C13 | Act-3 kiss framing + Iwona awareness at swap | P3 | 03-act3 |
| C14 | Where machine is assembled/tested in Oceanside | P3 | 03-act3 |
| C15 | Ending beat-4 hint level; closing line; player agency | P3 | 04-ending |
| C16 | Iwona knowledge-of-machine level (lean A2+A3 hybrid) | P2 | premise |
| C17 | Fake-band name + fake-Freebird song + 4-line lyric for kiss | P3 | story-arc.draft |
| C18 | Which friend accompanies Mark to Oceanside | P3 | story-arc.draft |

### D. Characters & roster
| # | Decision | Pri | Source |
|---|---|---|---|
| D1 | **Confirm Prime cap (~10–12) and fill P8–P12** from the Muster pool | P1 | roster |
| D2 | Caruso family — how many band kids Prime vs Supporting vs Ambient? Name them | P2 | roster, Q-003 |
| D3 | Family tier — special "Family" handling for Danny's parents/siblings? (recommend Supporting-with-depth) | P2 | roster |
| D4 | Mine `intake/people.yaml` (36KB) to pull real names/personalities into slots | P2 | roster |
| D5 | Name the open Ambient/Supporting locals (Camaro kid, beer-buyer, mean lady, 7-Eleven clerk) | P3 | world.md |
| D6 | Stan Burns immigrant background (Stanislaw→Stan); his wife at counter; Steve marital status | P3 | worldbuilding-rules |

### E. Quests
| # | Decision | Pri | Source |
|---|---|---|---|
| E1 | **Source the ~9 remaining machine-part quests** (now far easier via relationship-peak unlocks) | P1 | tracker |
| E2 | Finalize Q-003 (effect count, amp-blows-during vs dead-on-arrival, Act-1 order) | P2 | Q-003 |
| E3 | Clarify player-facing signal: which relationships yield *part* quests vs *Muster* favors | P2 | Mark's note |

### F. Systems / UX
| # | Decision | Pri | Source |
|---|---|---|---|
| F1 | Notebook/Book UI — how much to surface (people, quests) without overwhelming | P2 | gameplay-loop |
| F2 | HUD minimalism level; save system; workbench recipe-list vs mini-game | P2 | gameplay-loop |
| F3 | Collapse INSTALL into CRAFT? | P3 | gameplay-loop |
| F4 | Tier-1 Tear wait length; verify ≤3 waits fit 35-day summer | P3 | tear-system |
| F5 | Picky-lawn-client NPC casting | P3 | money-economy |
| F6 | The Tear's moment-to-moment *gameplay* expression (law locked, feel fuzzy) | P2 | spine |

### G. Production (low urgency)
| # | Decision | Pri | Source |
|---|---|---|---|
| G1 | Confirm Synty Town/City furniture covers house hub or add custom interior dressing | P3 | asset-plan |

---

## Part 3 — Two structural calls — ✅ EXECUTED 2026-05-30

Both calls were approved by Mark and executed. Recorded here for the audit trail.

### Call 1 — Narrative authority (C1) — RESOLVED as **role-split**, not winner-take-all
Two bodies of story canon existed:
- **`story/00–04`** — five per-act files = the lean **beat structure**.
- **`story-arc.draft.md`** — 800-line doc that, on reading, proved to be the **fleshed-out script layer** (full cut-scene dialogue: The Jump, the dance, the playable all-hope-lost mechanic, the Lamborghini ending, the Era Teaching System) — *not* a stale variant, and cross-linked from 7+ canon docs.

**Executed:** `story/00–04` declared canon **beat structure** (banner added to each); `story-arc.draft.md` **reclassified as the script layer** (header rewritten, pointer added) rather than archived. The draft's unique full scenes still need a scene-by-scene **fold** into the act files (C1d), and 3 conflicts surfaced during the read need Mark's ruling (**C1a/C1b/C1c**).

### Call 2 — Status-banner standard (C2 + housekeeping) — EXECUTED
- Status banners added to all five `story/` files.
- `scene-outlines.md` **archived** (moved to `archive/`).
- `components/index.md` **NOT archived** — it is **load-bearing** (its 10-letter scheme is still referenced by component-J/L, money-economy, tear-system, worldbuilding-rules). Flagged for a reference-reconcile pass first (**A3**).

---

## Part 4 — Recommended lock sequence (the "full design" phase)

Work the **P1s** first — they unblock everything and are mostly *rulings*, not big writing jobs:

1. **C1 + C2** — rule narrative authority + archive stale docs → *gives a clean story home to write into.*
2. **B1** — lock "the Note" (its 9 sub-Qs mostly become P2/P3 once the core is locked).
3. **D1** — confirm Prime cap + name P8–P12 → *the cast the whole game references.*
4. **E1** — source the remaining part-quests (now mostly relationship-peak unlocks).
5. *Then* the P2 design-shapers (act-gating, Iwona knowledge level, notebook UX, Caruso family).
6. *Then* mass-author against the proven schema; P3 details calibrate in the Ren'Py prototype.

> **Principle for this phase:** never let a P3 (a name, a song title, an exact day-count) block a P1.
> Park it in the relevant doc's open-questions list and keep moving.
