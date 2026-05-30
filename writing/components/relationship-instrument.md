# The Note — Relationship Resonance Instrument

> **Status:** PROPOSAL (2026-05-30) — NOT locked. Staging ground for the relationship-measurement
> mechanic. Lock only after Mark reviews and we calibrate against the prototype.
> **Author intent (Mark, 2026-05-30):** A relationship mechanic that gates content (band debut
> needs ~10 people willing to come; NPCs only trust Mark with quests above a threshold; the bike
> jump warms many friends at once). Must be **diegetic and mystical — NOT a numeric meter the
> player checks**. Sourced from Denise (the Path 2 / spiritual mentor).
> **Sibling docs:** `components/tear-system.md` (diegetic-UI law), `components/machine-architecture.md`
> (Denise + Stan mentors), `quest-ideas-inbox.md` (VW Bus hippies, character pass).

---

## 1. The one-line pitch

Denise gives Mark a worn **brass tuning fork** on a cord — **"the Note."** Struck near a person,
it doesn't ring the same for everyone. Mark *hears* the state of a bond instead of reading a bar.

> *"Everybody's got a note, child. The only question is whether yours and theirs ring together —
> or fight."* — Denise

**Why a tuning fork (and explicitly NOT amber):** Amber is load-bearing elsewhere in the plot
(Denise's original amber → destroyed in the fire → the Oceanside amber store → the saltwater +
blacklight authentication that *fails* → Iwona's kiss-and-gift of her own amber-with-inclusion at
the concert). Amber must stay the single most precious object in the game. The Note uses a
**different sense entirely (sound)** and a different material (brass), so it never competes with
amber — while still speaking the machine's native language of **resonance and frequency**
(Edison Spirit Valve, the CB-crystal "tuning," soul-frequency). Soul-resonance for relationships
is the same physics as the machine, minus the amber.

---

## 2. How Denise derives it (in-fiction)

Per Mark (2026-05-30): Denise helped Danny the *first* time with the **second / spiritual (Vapor)
pathway**, and — being spiritually attuned — **she can feel that Mark is not Danny.** She is the
one person who knows the truth.

Her worry isn't the machine. It's that **Mark is living a life whose map he doesn't have.** He
doesn't know who Danny could trust, who'd take a punch for him, who's a narc. So she attunes an
old tuning fork to him — *"so you can hear what I hear"* — and hands him a way to navigate Danny's
relationships without a map. This is **her Act 1 gift**, and getting it is *why the player meets
Denise early.*

> Cover line (period camouflage): to everyone else it's just the weird mystic neighbor's trinket —
> a 1976 kid wearing hippie jewelry is unremarkable. Denise can even tell Mark, *"If anyone asks,
> it's one of those mood-ring things."* The magic hides behind a real 70s fad.

---

## 3. The four-axis read (this is what makes it NOT a number)

You don't open a menu and read a level. You strike the fork and *listen.* It reports **four
independent things at once** — far richer than a single scalar:

| Channel | Range | What it means |
|---|---|---|
| **Pitch** | rings *true* ↔ sounds *sour / flat* | Alignment. In-tune = trust; sour = wary stranger |
| **Sustain** | rings *long* ↔ *dies fast* | Stability. A solid earned bond sustains; a shaky new one fades quick |
| **Volume** | *full bell* ↔ *faint hum* | Intensity of the bond |
| **Bad buzz / rattle** | clean ↔ *ugly buzz* | **Deceit or threat** — someone lying to Mark or meaning him harm |

That last channel makes the Note a **danger sense**, not just an affection gauge — useful with
older burnouts, the mean lady who calls the cops, and Act 3 Oceanside strangers. One object,
layered output = it feels like *perceiving a person*, not checking a stat.

---

## 4. The thematic engine: it reads MARK, not Danny

The most important design move. Danny's friends treat Mark like Danny — but **the Note reads
Mark's *actual* bond, which starts near zero.** Mickey throws an arm around "Danny" and the fork
rings **flat and dead.** Danny's Book notes nag from the other side:

> *"You and Mickey were in tune since we were six. Why's your fork sour?"*

This turns the relationship system into a statement of the whole game's spine —
**displacement, and the love that bridges it.** You inherited a life; you did *not* inherit the
love in it. Every degree of warmth must be earned by Mark, personally. And it pays off the ending:
the bonds Mark builds are *his* — which is exactly why leaving 1976 hurts.

---

## 5. How the player experiences it (anti-min-max)

- **Ambient, not a menu.** During a scene, the Note reacts *in Mark's peripheral hearing* — a soft
  hum or a sour twang under the dialogue. Players aren't compelled to "scan" everyone.
- **Deliberate consult only when unsure.** Mark can choose to strike it to read someone he's
  uncertain about (a stranger, a possible liar).
- **Denise's warning doubles as design guidance:** *"Don't stare at it. Live — and let it tell you
  when you're not looking."* This is literally the anti-grind rule, in character.
- **Feedback without popups.** Screw up — lie and get caught, miss the creek jump, narc on someone
  — and you *hear the fork go sour next time you're near them.* The world tells you; no UI scold.

---

## 6. The "UI" — obeys the Book-only law (tear-system.md §6/§8)

Your locked rule: the Book is the only persistent diegetic UI; no numeric stats (the Tear is an
ink stain, not a bar). The Note obeys it:

- Denise teaches Mark to **press the humming fork to the Book.** It vibrates a **little waveform
  line** beside that person's name.
- **Long smooth line** = strong, settled bond. **Short jagged scratch** = cold or volatile.
  **A broken/buzzing line** = someone not to be trusted.
- So your "relationship screen" is a **hand-drawn ledger of names with waveform marks** —
  annotated by Danny from the other side (reinforcing the reads-Mark-not-Danny irony).
- **Hear it live in the moment; see the recorded ledger in the Book later.** Same visual family as
  the Tear ink-stain — your wife's graphic-design hand unifies both.

No bars. No percentages. No number to check.

---

## 7. Gating logic (under the hood vs. what the player sees)

The engine can still track relationship state numerically **internally** — the player just never
sees the number. They see/hear the fork. Mapping examples:

| Gate | Internal check | What the player perceives |
|---|---|---|
| **Band debut needs ~10 bodies** | N neighbors at "warm" threshold | The room "isn't ready" — too many sour/faint forks across the block |
| **NPC trusts Mark with a real quest** | that person's bond ≥ trust threshold | Their fork must ring *true and sustain* before they'll hand over the favor |
| **The bike jump** | group event: +warmth to many at once | Pull it off and a *crowd* of forks warm together — a "level up the neighborhood" beat |
| **Relationship DOWN** | caught lying, narcing, failing a peer | The fork audibly cools next time you're near them |

**Cross-tie to the Tear system's Tier-2 favor** (`tear-system.md` §4): "who covers for me"
(Mickey / Bobby / Iwona) is literally a *warmth-bond being spent.* The Note is how the player
feels which of the three is warm enough to ask — and what it costs the fork afterward.

---

## 8. Act 1 / Zone 1 onboarding — solving the "meet both mentors early + stay contained" problem

Mark's linked problem (2026-05-30): force the player to meet **Denise** (spiritual mentor) and
**Stan Burns** (Burnsville Electronics, technical mentor) early, and keep them inside **Zone 1**
in Act 1. The **Box of Leftovers** is the forcing function — it hands Mark *both* mentors:

- **Stan (Signal path):** the **Burnsville Electronics receipts** already in the box (canon) + a
  half-finished schematic marked *"ask Stan for the rest."* Mark must find Stan to advance the
  Signal pathway. Burnsville is in Zone 1.
- **Denise (Soul/relationship path):** the **organic painting hook** (see
  `second-pathway-ritual-platform.md` §6): Mark examines the intact-but-inert **ritual platform with stone-sockets** in
  the bedroom, steps outside, and sees **Denise painting the same images on her lawn** → he
  recognizes the match and goes to investigate her. Danny's sealed *"see Denise first"* note is kept
  only as backup/confirmation. Meeting her **is how Mark gets the Note.** Denise **immediately** knows
  he's a stranger in Danny's skin (*"You're not Danny. Sit down, child."*).
- **Containment to Zone 1:** both Denise (across the street) and Stan (in-neighborhood) sit *inside*
  Zone 1. Mom's streetlight rule + Mark not knowing the town yet + no bike-range trust yet = a
  natural soft fence. The machine won't power on until both mentor intros happen, so neither is
  skippable.

**Net Act 1 shape:** two mentors, two systems — **Stan = Signal (technical)**, **Denise = Soul
(relationships + Vapor)** — both taught as Zone 1 tutorials. The Note goes live immediately, so the
cold-fork-with-Danny's-friends irony teaches *"you must earn your own warmth"* from minute one.
That is *why* the instrument is forced early.

> Note alignment with existing Act 1 doc: `story/01-act1.md` currently recommends Denise is
> "glimpsed across the street, first conversation Act 1 mid-late." This proposal pulls the **first
> Denise conversation earlier** (it's now the relationship-system tutorial) OR keeps the glimpse →
> a clear early hook → the gift. Exact beat order = open question §11.

---

## 9. Canon reconciliation (FLAG — needs Mark's lock)

Today's statement evolves Denise's locked canon. Capturing the delta honestly:

- **Existing canon** (`machine-architecture.md`, Denise section): "Danny's original folklore
  consultant… Knows things about the Vapor pathway the kids can't figure out alone." An earlier
  working note had Denise *not* knowing the machine's true soul-transfer purpose.
- **New (Mark, 2026-05-30):** Denise **knowingly helped Danny build the second/spiritual (Vapor)
  pathway**, and **she can sense Mark is not Danny — from the start of Act 1.**
- **Also answers an open question:** `story/02-act2.md` asks *"Does Denise sense something's off
  about 'Danny' in Act 2? When?"* → New answer: **she knows in Act 1, on first contact.** She is
  Mark's secret-keeper, not a late-game suspicion beat.

**Action when locked:** update the Denise section in `machine-architecture.md` and resolve the
Act 2 open question. Not edited yet — `machine-architecture.md` is LOCKED canon; await Mark's go.

---

## 10. Why this passes the Mark Test

- Casual/older players never face a spreadsheet — they hear a friendly bell or a sour twang.
- No hoarding/sacrifice anxiety; the Note is a *sense*, not a resource you can lose by spending.
- It teaches itself diegetically (Denise's tutorial + the cold-fork irony).
- It gates content without ever exposing a number, honoring the Book-only UI law.

---

## 11. Open questions (for review / prototype calibration)

1. **Beat order:** does the first Denise conversation (and the gift) happen on first trip out, or
   after a glimpse + a small hook? Reconcile with `story/01-act1.md`.
2. **Read granularity:** how many *audible* tiers per channel before it's too fiddly to hear?
   (Likely 3–4 steps of pitch; calibrate by ear in the prototype.)
3. **Accessibility:** sound-primary read needs the Book-waveform as the full visual equivalent for
   hard-of-hearing players + subtitle-style cues (*[the fork rings true]* / *[a sour buzz]*).
4. **Does the Note ever read Iwona?** Risk: making the love story feel "measured." Recommend the
   Note goes *strange/overwhelmed* near Iwona rather than giving a clean reading — protects the
   romance from feeling gamified. TBD.
5. **Band-debut threshold:** exact count (~10) and whether the bike jump alone can carry most of it.
6. **Down-state floor:** can a bond go fully "dead/hostile," or does it bottom out at "cold"?
7. **Naming:** player/design term "the Note"; Denise's in-world term ("your tuning"? "the fork"?).
8. **Calibration:** like the Tear waits, lock exact thresholds only once we feel it in-engine.

---

## 12. Cross-references

- `components/tear-system.md` — diegetic-UI law (no numeric stats; Book-as-UI); Tier-2 favor tie-in.
- `components/machine-architecture.md` — Denise (Path 2) + Stan (Path 1) mentors; Vapor pathway.
- `components/index.md` — machine spine (the Note is NOT a machine component; it's a separate gift).
- `story/01-act1.md` — Act 1 chunk pacing, Burnsville scene, Denise first-appearance question.
- `story/02-act2.md` — "Does Denise sense something's off?" question (answered here: Act 1).
- `quest-ideas-inbox.md` — VW Bus hippies (Vapor supply), character pass (Denise/Caruso/hippies).
- `quests/_quest-item-tracker.md` — Denise/Stan listed as mentors, not item-sources (consistent).


