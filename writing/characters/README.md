# Characters — System & How to Document Them

> **Status:** CANON (system doc) · 2026-05-30. Defines the **five character tiers** (top-down), how we write
> **personalities**, and the **state-driven dialog system** (the part that changes by act + quest).
> Templates live beside this file; the cast lives in [`roster.md`](roster.md).
> **Parent:** [`../design-spine.md`](../design-spine.md) §6–7 (the Note, quest archetypes, NPC tiers).

---

## 1. The five tiers (top-down)

We deliberately spend our writing effort where the player feels it. **Five descriptive tiers**, numbered
top-down (T1 = most significant), mapping onto **three authoring templates** (the real cost buckets):

| Tier | Name | Note rings / notebook? | Quest-giver? | Template | Count |
|---|---|---|---|---|---|
| **T1** | **Significant** — core cast: deep relationship **+** major game purpose (mentors, Iwona) | ✅ tracked | yes | **Prime** | see budget |
| **T2** | **Active relationship** — people you build relationships with, not pillar-significant | ✅ tracked | yes | **Prime** | see budget |
| **T3** | **Quest / scavenge** — real purpose in quests or item-gathering, **no** relationship grind | ❌ | yes | **Supporting** | see budget |
| **T4** | **Minor recurring** — exists because a **quest needs them**; small defined role, a few lines, no tree | ❌ | yes (their reason to exist) | **Ambient+** | ~40 |
| **T5** | **Background** — store bystanders, boardwalk walkers; 0–2 flavor lines, no quest role | ❌ | no | **Ambient** | ~12 archetypes |

> **Cast budget (authoritative):** see [`../design/README.md`](../design/README.md) §2a. In short — the
> **entire interactive cast (T1–T3) is ≤40, goal ~30** (fewer and more well-developed is the goal); T4 ~40
> named extras; T5 ~12 population archetypes. These are **ceilings, not quotas.**

**The three boundaries that matter:**
- **Relationship & the Note = T1 + T2 only.** These are the people the Note rings for and the only ones
  in the relationships notebook (the diegetic cap — *"It won't sing for everyone, child."*).
- **Quest-givers span T1–T3.** Giving a quest item is a **capability, not a tier** — a T3 can hand you
  beer cans or candy; a T1 can gate a hero machine part. Anyone tied to a quest sits in T1–T3.
- **T4/T5 exist to kill "wasted NPCs."** Even a store clerk gets a line or two, classified so no one
  ships as a faceless prop. T4 = minor-but-recurring (simple depth); T5 = true background flavor.

**Authoring reality — five labels, three templates:** T1≈T2 share the **Prime** sheet, T4≈T5 share the
**Ambient** sheet, T3 is **Supporting**. You get five tiers of granularity for the cost of three formats.

**Rules of thumb:**
- **The interactive cast (T1–T3) is capped at ~40, goal ~30** (see budget above). Of those, the
  Note-tracked Prime set (T1–T2) is the smallest, most-developed group — every Prime gets heart: a want,
  a wound, a voice, an arc. *Fewer and better always wins.*
- **Supporting (T3)** have personality (players barter with them, remember them) but **no fork, no
  relationship grind.** Store owners are mostly here ("**stores ARE the NPCs**").
- **Ambient (T4–T5)** are flavor. Don't over-invest — 3–6 good barks beat a flat paragraph. T4 gets a
  touch more (recurring, named, simple depth); T5 is 0–2 lines.
- A character can be **promoted** a tier if the design needs it (e.g., a T3 shopkeeper who becomes a
  relationship target). Note promotions in `roster.md`.

---

## 2. How we write PERSONALITY (so players feel the heart)

Every **Prime and Supporting** sheet answers these — short, specific, era-true, **never generic**:

1. **One-line essence** — who they are in a sentence.
2. **Want / Wound / Lie** — what they want, the hurt underneath, the lie they tell themselves. (This is
   the engine of a character players *care* about. **Prime mandatory; Supporting optional.**)
3. **Voice** — how they talk: vocabulary, rhythm, verbal tics, what they *never* say. Give 3–4 sample
   lines so any writer can match the voice.
4. **Look & staging** — silhouette, where you find them, what they're doing.
5. **Relationship to Mark/Danny** — do they know the *old* Danny? (Critical: Mark is an impostor, so
   anyone who knew Danny well reads "off" — mine that.)
6. **Function** — what they gate (parts, muster, info, barter, story).
7. **Arc** — how they change across Acts 1→3 (**Prime**).

> **Heart test:** if you deleted this character, would a player *miss* them? If not, they're either
> Ambient (fine) or under-written (fix).

---

## 3. The dialog system (the hard part) — state-driven layers

This is the standard game-design answer to "their lines change by act and by whether a quest is
active." You do **not** write one giant branching tree. You write **layers of guarded nodes**, and
the engine **picks the highest-priority node whose conditions are currently true.**

### 3.1 The state that gates dialog

Four kinds of state decide what a character says:

| State | Values | Example |
|---|---|---|
| **`act` / `day`** | Act 1 / 2 / 3 (or day N) | Stan is gruff in Act 1, fond by Act 3 |
| **`rel(npc)`** | the Note's bands: **Cold · Flat · Warming · Warm · Close** | Warm Mickey will cover for you; Cold won't |
| **`quest_state[Q]`** | Locked · Available · Active · Step-n · Done · Failed | Elga only mentions "the garden" once Q-001 is Done |
| **`flags`** | one-time booleans | `met_denise`, `knows_marijuana`, `cover_blown_once` |

### 3.2 The four dialog layers (priority: highest wins)

When the player talks to an NPC, the engine checks layers **top-down** and plays the first match:

1. **Quest-active branch** *(highest)* — a scripted exchange that fires while a quest involving this
   NPC is `Active`. This is the only place we author real **branching choice trees**.
2. **Story beat** — a one-time line gated by an `act`/`flag` (e.g., first meeting, a reveal). Sets a
   flag so it never repeats.
3. **Topic menu** — a *small* "ask about…" list; entries **unlock/change** by state. Keep it to 2–4
   live topics at a time (Mark Test: no wall of options).
4. **Greeting / bark** *(lowest, the fallback)* — short context lines that **swap by `act` + `rel`
   band**. Cheap to write, and they're what make a town feel *alive*. Always have one.

> **Why this beats a mega-tree:** you author **barks** in bulk (one matrix), reserve **branching
> trees** only for quest moments, and the "changes by act/quest" behavior falls out of the conditions
> automatically. This is how Ren'Py, Ink, and most narrative engines actually do it.

### 3.3 Anti-overwhelm rules (the Mark Test)

- **Most dialog is *heard*, not menu'd.** Greetings and barks just *play*. Menus appear only when
  there's a real choice.
- **Topic menus stay tiny** (2–4 items). Old/dead topics drop off.
- **The Book stores only the one-line takeaway**, in Mark's handwriting — never a transcript. (Diegetic
  UI law, `../components/tear-system.md`.)
- **A Prime character is not "more menus" — it's better *barks*.** Depth comes from lines that *know*
  the state (the act, your last screw-up, your warmth), not from option bloat.

---

## 4. How to document a dialog tree (the format)

Each Prime/Supporting sheet contains a **Dialog Map** with two parts:

### 4.1 Greeting matrix (the bark layer) — cheap life

A small grid: **rows = act, columns = rel band → the line that plays.** Example (Stan):

| | Cold/Flat | Warming | Warm | Close |
|---|---|---|---|---|
| **Act 1** | "Help you with something?" | "Back again, huh." | "There's the kid." | — |
| **Act 2** | "We're busy." | "Grab a stool." | "Saved you the good caps." | "Sit. Talk to me." |
| **Act 3** | — | — | "You're not gonna believe what came in." | "I always knew you were different, Danny." |

### 4.2 Node table (story / topic / quest layers)

| Node ID | Layer | Conditions (`act` / `rel` / `quest` / `flags`) | Line(s) | Choices → target | Effects (set flag · item · rel ±) |
|---|---|---|---|---|---|
| `STAN_meet` | Story | act≥1 ∧ ¬`met_stan` | "Burnsville's the name… you're one of Danny's…" | — | set `met_stan`; rel→Flat |
| `STAN_topic_parts` | Topic | `met_stan` | "What do you need off the board?" | → list | — |
| `STAN_qXX_active` | Quest | `quest[Q-XX]`=Active | (branching exchange) | A→… / B→… | give part; rel +1; set step |

**Node ID convention:** `NPC_purpose` (lowercase quest IDs as suffixes). Keep IDs stable — they map
1:1 to **Ren'Py labels** at build time.

### 4.3 Ren'Py translation (so this isn't theoretical)

The doc format above translates directly to Ren'Py:

```renpy
label stan_talk:
    if not met_stan:
        jump stan_meet                       # Story layer
    if quest_QXX == "active":
        jump stan_qXX_active                 # Quest layer (branching menu inside)
    menu:                                    # Topic layer (small)
        "Ask about parts" if met_stan:
            jump stan_topic_parts
        "Just looking":
            jump stan_greeting
label stan_greeting:                         # Bark layer (greeting matrix)
    $ say_greeting("stan", act, rel_stan)    # picks the line from the matrix
    return
```

You write the *content* in the table; the *plumbing* is a handful of reusable Ren'Py helpers
(`say_greeting`, a topic menu builder, flag/rel variables). **Author once, reuse everywhere.**

---

## 5. Files in this folder

- [`roster.md`](roster.md) — the full cast, tiered, with one-line essence + what each gates. Living.
- [`_template-prime.md`](_template-prime.md) — Tier 3 full sheet (personality + dialog map across acts).
- [`_template-supporting.md`](_template-supporting.md) — Tier 2 (personality + barter + light topics).
- [`_template-ambient.md`](_template-ambient.md) — Tier 1 (barks).
- One sheet per named character, filenamed `NN-name.md` (e.g., `01-stan-burns.md`).

**Source to mine for the cast:** `../intake/people.yaml` (36KB of real people Mark seeded) is the
quarry for personalities and names. The roster pulls from it; sheets flesh it out.
