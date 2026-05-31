# Design Data Architecture — the canonical store

> **Status:** 🔒 CANON (architecture) · v1 · 2026-05-30. This folder is the **single source of truth**
> for everything the game build consumes. Read this before adding or editing any entity record.
> **Parent:** [`../design-spine.md`](../design-spine.md). **Authoring guide for people:** [`../characters/README.md`](../characters/README.md).

---

## 1. The three content classes (why this folder exists)

Everything we write falls into one of three classes. They have different lifecycles and **must not be
mixed in the same store** — that was the old `intake/` smell.

| Class | What it is | Lives in | Lifecycle |
|---|---|---|---|
| **1. Reference (the Encyclopedia)** | 1970s world facts the game *cites* (customs, banned-or-gone, era media). | `../source/encyclopedia/` | Read-mostly lookup. Curated, rarely changes. |
| **2. Entities (the Game)** | Normalized records the **build consumes**: people, places, items, quests, dialog. | **`design/` (here)** | Production tables. Linked by `id`. |
| **3. Design canon (prose)** | Human-readable design intent: story acts, machine architecture, system rules. | `../story/`, `../components/`, root specs | Specs. Authored by hand. |

**`design/` is the warehouse. `source/` is the lake.** Content flows **one direction only:
`source/` → `design/`** via deliberate **promotion** (§4). Nothing in `design/` may depend on anything
in `source/`. The day the game ships, `source/` could be deleted and the build still works. That is the
single-source guarantee.

---

## 2. Folder = table

```
design/
  people/    characters.yaml  — T1–T3 (~35): full + medium schema, FK-linked. The heart.
             extras.yaml      — T4 (~40): named recurring, thin schema, a few lines.
             archetypes.yaml  — T5 (~12): anonymous POPULATION templates (bark-bank + spawn rule, no identity).
  places/    places.yaml      — locations + addresses
  items/     items.yaml       — gift items, machine parts-as-data, quest objects
  quests/    quests.yaml       (or one file per quest; see quests/README)
  dialog/    <id>.md          — node tables + greeting matrices, one per speaking character
```

Each record has a unique kebab-case **`id`**. Records reference each other by `id` — **foreign keys**,
never by copying data. One fact lives in exactly one place; everyone else points at it.

---

## 2a. Volumetrics & weight classes (the scale contract)

The cast is **radically bimodal** — a tiny heavy core and a large light tail. The schema **splits by
weight class** so the 200-person tail never carries the 20-person core's schema. This is what lets the
design reach ~90% final: every *class* of entity has a home, so the Nth record is **data entry, not
redesign.**

| Class | Tier | Target count | Schema | Authored how | Table |
|---|---|---|---|---|---|
| **Interactive cast** | **T1–T3** | **≤40, goal ~30** | Full (T1–T2) / medium (T3) — every one has personality + a real purpose | By hand | `characters.yaml` |
| **Named extra** | T4 | ~40 | Thin: identity + location + a **defined quest role** + 2–4 lines | Individually, fast | `extras.yaml` |
| **Population** | T5 | ~12 archetypes ⇒ ~150 bodies | Minimal: bark-bank + spawn rule, **no identity, no quest role** | As archetypes, NOT per-body | `archetypes.yaml` |

**Mark's authoring budget (locked 2026-05-30) — CEILINGS, not quotas:** the entire **interactive cast
(T1–T3) is ≤40, goal ~30.** *Fewer and more well-developed is the explicit goal.* Players should
**enjoy and want to interact with** T1–T2, and should **never meet a T3 without a purpose** in the game.
Below that: ~40 thin T4 (each justified by a quest role) + ~12 T5 archetypes for the anonymous crowd.
"The rest are just NPCs with some cute lines."

> **The T4/T5 line = does the quest graph need them?** A **T4 exists because a quest needs them** — a
> small, well-defined role (hands over an item, blocks a door, gives a tip). That job is the whole reason
> they get a named record. A **T5 has no quest job** — pure atmosphere, spawned from an archetype. If a
> T5 archetype ever acquires a real quest role, it **graduates to a named T4 record.**

**The population insight (critical):** "200 background characters" is the wrong unit. ~150 of them are
**anonymous populations** — "boardwalk-walker," "department-store-shopper," "kid-on-a-bike." You author
**~12 archetypes** (one bark-bank + a spawn rule each) and the engine populates scenes from the pool. One
`beach-goer` archetype = forty boardwalk bodies. Real authoring load ≈ **85 records**, not 300.

Other tables, same discipline: **places ~50, items ~100, quests ~30–40, dialog ≈ one per speaking
character (T1–T4).** None of these require restructuring as they grow — only rows.

> **Weight-class rule:** never push a heavier schema onto a lighter class. A T5 archetype has no `want`,
> no dialog tree, no quest FK. A T4 extra has no relationship arc. Forcing those fields is the
> gold-plating Rule A forbids.

---

## 3. The two governing rules

### Rule A — Field justification (anti-gold-plating)
> **Every table and every field must answer a question the Ren'Py build — or a real design decision —
> actually asks. If it doesn't feed the build or a decision, it is `notes`, not a field.**

This is the whole defense against turning a 2-year game into a CMS. It is why `change_name`, `reality`,
and `stories` were cut from the people schema (none feed the build).

### Rule B — Citations point *up*, coverage is *derived* (lineage)
A reference fact (Class 1) does **not** know whether it's in the game. The **consuming** entity declares
the citation via **`draws_on:`**. Example: the Kay dining-room scene cites `smoking-everywhere`; the
customs entry stays passive.

> "Is this encyclopedia entry in the game yet?" is **computed** (does anything `draws_on` it?), never a
> hand-maintained checkbox that drifts. A future one-line script produces the **coverage report**
> ("47 customs entries, 31 used, 16 orphaned"). Optional denormalized `status: in-game` flags are a
> *cache*, never the truth.

**Don't build tooling until hand-maintenance hurts.** The coverage script is the only early automation
worth wanting — and not yet.

---

## 4. Promotion: how content enters `design/`

Migration from `source/` is **selective, record by record** — not lift-and-shift. The act of promoting a
record *is* the curation pass. **Not every brainstorm person moves.** What never earns promotion stays in
the quarry or dies there.

A record is **promotable** when it has: a real role in the game, a `tier`, and at least its identity +
links roughed in. Prose can be refined after promotion; the *structure* must be sound on entry.

---

## 5. People schemas (v2) — three by weight class

Aligned with the 5-tier model and Want/Wound/Lie personality system in `../characters/README.md`.

### 5.1 `characters.yaml` — T1–T3 (heavy + medium), the full schema

```yaml
- id:            # kebab-case, unique (required)
  name:          # canonical in-game name — THIS is the source of truth (required)
  tier:          # 1–3 (see characters/README §1) (required)
  category:      # family | friends | neighborhood | school | famous_local | strangers
  role:          # one-line role tag — "mom; the loud one"
  age_1976:      # number or range
  relation:      # relation to Danny — "mother", "neighbor 5 houses down"

  # PERSONALITY (T1–T2 mandatory · T3 optional)
  essence:       # one line — who they are
  want:          #
  wound:         #
  lie:           #
  voice:    |    # how they talk (block scalar)
  physical: |    # silhouette, signature object
  vibe:     |    # the feel

  # LINKS (foreign keys — the structured spine)
  location:      { place: <places.id>, address: "1437 Linden Drive" }
  likes_items:   [<items.id>, ...]      # GIFTING these raises relationship (the relationship-builder hook)
  quests:        [{ id: <quests.id>, role: requester|giver|gatekeeper|target }]
  dialog:        <dialog ref / id>      # → design/dialog/<id>.md (node table + greeting matrix)
  draws_on:      [<encyclopedia.id>, ...]  # Class-1 reference facts this character embodies (lineage)

  # RELATIONSHIP (T1–T2 ONLY — the people the Note rings for; OMIT entirely for T3)
  relationship:
    starts_at:   cold        # warmth band when Mark first meets them (cold|wary|warm|tight)
    gates_at:    warm        # band required to unlock this person's quest/favor/cover
    warms_via:               # concrete levers that RAISE the band (FK-linked where possible)
      - { gift:  <items.id> }       # gifting a liked item  (→ likes_items)
      - { quest: <quests.id> }      # completing this quest warms them
      - { beat:  <event-id> }       # a scripted muster/event (e.g. bike-jump)
    cools_via:               # optional — what SOURS the fork
      - { betrayal: <event-id> }
    notes: |                 # why they start where they do; fastest path to the gate

  # META
  tags:          [free-form]
  audience:      gen_x | gen_z | both
  status:        stub | sketch | full     # how finished THIS record is (was the old `depth:`)
  notes:    |    # anything else — parody lineage, sensitivities, open questions
```

### 5.1a The warmth ladder (how `relationship:` works)

The Note (`components/relationship-instrument.md`) is **diegetic and never numbered to the player** — Mark
*hears* a bond on four axes (pitch / sustain / volume / bad-buzz), he never reads a bar. But the engine
tracks warmth **internally as a small integer band**, and the author writes gates against that band. Keep
the two strictly separate: **internal = a number; in-game = a sound.**

**The 4 internal bands** (matches `relationship-instrument.md` §11's "3–4 audible steps"):

| Band | Int | Fork *sounds* like (what the player gets) | What it means for gating |
|---|---|---|---|
| **cold**  | 0 | sour / flat / dies fast | Default for Danny's old friends — Mark is a stranger in his skin |
| **wary**  | 1 | truer, but short sustain | Will talk; won't hand over a real favor or quest |
| **warm**  | 2 | rings true, good sustain | **Trust threshold** — unlocks their Part quest / muster body / cover |
| **tight** | 3 | full bell, long sustain | Pillar bonds; deepest content, cover-for-me favors |

Authoring rules:
- **Only T1–T2 carry a `relationship:` block.** T3 has a quest link but **no Note tracking** — omit the block.
- `starts_at` is usually `cold` for Danny's existing circle (the cold-fork irony is the theme); a brand-new
  person Mark meets fresh may start `wary`.
- `gates_at` is the band the engine checks before unlocking their `quests:` / cover favor. Most land at `warm`.
- `warms_via` lists the **concrete levers** — gifting a `likes_items` entry, completing a quest, or a scripted
  `beat` (the bike-jump warms many at once). These are the "how to build it" instructions per character.
- Never surface the band name or number in dialogue or UI — it exists only for the author and the engine.



A T4 exists **because a quest needs them.** The `quests` link is their reason for being a record — not
optional. Thin everything else.

```yaml
- id:
  name:
  tier:          # 4
  category:
  role:          # one-line — usually their quest function ("gives the tip about the junkyard")
  location:      { place: <places.id> }   # optional
  quests:        [{ id: <quests.id>, role: requester|giver|gatekeeper|target }]  # the REASON they exist
  lines:         [ "2–4 flat barks", ... ] # heard, not menu'd
  tags: []
  notes: |
```
No `want/wound/lie`, no relationship arc, no dialog tree. If a T4 ever needs those, **promote it to T3**.

### 5.3 `archetypes.yaml` — T5 anonymous populations (minimal)

```yaml
- id:            # archetype id, e.g. "beach-goer" — NOT a person
  label:         # "Boardwalk walker"
  tier:          # 5
  spawn:         [ <places.id>, ... ]      # where the engine populates them
  barks:         [ "short ambient line", ... ]  # the bark-bank; engine picks at random
  variants:      # optional visual flavor for the spawner — "old couple", "surfer", "tourist"
  notes: |
```
**No identity, no names, no FKs to quests/items.** One archetype = many on-screen bodies.

**Changes from v1 intake schema:** cut `change_name`, `reality`, `stories`; renamed `depth:` → `status:`
and removed the `sketch:` field-name collision (its prose folds into `voice/physical/vibe`); **added**
`tier`, `category`, `location`, `likes_items`, `quests`, `dialog`, `draws_on`, and the
`essence/want/wound/lie` personality fields so the people store and the character authoring guide agree.
**Split the one people table into three by weight class** (§2a) so the ~200-record T4–T5 tail never
carries the heavy schema.

### The beer-can pattern (relationship fetch quests, in data)
A "collects beer cans, fetch him cans" quest is **not** special schema. The character lists
`likes_items: [beer-can]` (gift hook → +relationship) and `quests: [{id: q-XXX, role: requester}]`. The
**item** is defined once in `items.yaml`, the **quest** once in `quests.yaml`; the person carries only
pointers. A low-tier fetch quest is just a quest whose reward is **+relationship** instead of a part.

---

## 6. Pilot status (2026-05-30)

`people/characters.yaml` seeded with **3 migrated entities** to stress-test the schema against real
content + live foreign keys: **Kay Marek** (T1, family), **Mickey Karras** (T2, neighborhood), **Athena
Karras** (T3, quest-giver). Sibling tables (`places`, `items`, `quests`, `dialog`, `extras`,
`archetypes`) are stubs until the schema is confirmed. **Do not mass-migrate the quarry until Mark signs
off on the pilot.**
