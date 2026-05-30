# Q-003 — Showtime (The Caruso Garage Band Light Show)

## Header

- **Quest ID:** Q-003
- **Title:** Showtime
- **Status:** 📝 DRAFT (designed 2026-05-29, structurally locked — dialogue details TBD)
- **NPC Hub:** Tony Caruso (14, band kid) + his garage band
- **Act:** 1 (mid Act 1 — an early "learn the machine loop" teaching quest)
- **Gates:** Player must have met Tony Caruso and know the band exists; player must have access to the basic scavenge locations (home, Elga's shed, surplus store, neighbor's house)
- **Unlocks:** Hands over TWO Signal-pathway machine parts (amp-derived); deepens Caruso band as a recurring favor-faction

> **DESIGN NOTE — SAFETY (locked):** This quest deliberately contains NO pyrotechnics, explosives, or
> anything dangerous/replicable. Original concept was homemade fireworks; rejected. All effects are
> harmless duct-tape STAGECRAFT (fog from a fan + dry ice, a light show from Christmas lights + a slide
> projector, fake "sparks" from a fan + tinsel). Nothing in this quest teaches a real dangerous procedure.
> Crafting is shown as abstract icon-combines, not real instructions. Keep it that way.

---

## 1. NPC-as-Hub Yield

| Yield | Tier | Quest |
|---|---|---|
| 12AX7 vacuum tubes (→ Edison Spirit Valve, Signal Slot 7) | Direct-use machine part | Q-003 (this) |
| Marshall Amp Output Transformer (Signal Slot 4) | Direct-use machine part | Q-003 (this) |

Tony Caruso = 2-yield NPC (both yielded by THIS one quest, as the band's "payment"). Within the 3-yield cap.
*(Earlier tracker drafts split these across two trades; consolidating both into the single light-show favor
is cleaner — the band pays the pyro/tech kid with their busted amp's guts.)*

---

## 2. Reward Layer

- **Primary reward:** **Marshall Amp Output Transformer** (Signal Slot 4) + **12AX7 vacuum tubes** (Signal
  Slot 7, "Edison Spirit Valve"). The band's amp blew during the show (or was already half-dead); they give
  Mark the dead amp's salvageable guts as thanks / because "it's fried anyway, man."
- **Secondary reward:** Caruso band becomes a friendly recurring favor-faction; possible small cash.
- **Downstream use:** Both parts are DIRECT-USE (no further trade hop). They fill two of the ten Signal slots —
  a big, satisfying early haul that visibly advances the Machine Blueprint UI.
- **Teaching value:** This is the **tutorial for the whole machine loop** — wish-list → scavenge → assemble →
  power-on → reward — learned on something harmless and funny before the real stakes land.

---

## 3. What Player KNOWS (Initial Signposts)

| Signpost | Location / Trigger | Player-type targeted |
|---|---|---|
| Loud, bad garage-band practice audible down the block | Ambient, Caruso garage | All players |
| Tony Caruso brags the band is recording their "debut" and wants "a real rock show" | Dialogue with Tony | All players |
| The band has NO money and NO equipment for effects | Dialogue — they ask Mark, "the tech kid" | All players |
| Band's amp is buzzing/dying — visible sparks/smoke from it during practice | Ambient garage detail | Sharp player notes the amp early (foreshadows the reward) |
| Mark (future-self) recognizes amp guts = machine parts | Mark VO when examining the amp | Sharp player connects to blueprint |

**The "a-ha" trigger:** the band wants a *show* and can only pay in *junk* — and their junk (the dying amp)
is exactly what Mark's machine needs. The player should clock "I want that amp" early.

---

## 4. What Player FIGURES OUT (The Puzzle)

> *"Oh — if I rig the band a fog/light show out of household junk, they'll pay me with their busted amp —
> and that amp has the transformer and tubes my machine needs."*

Logical chain:

1. The band wants concert-style effects (fog, lights, sparks)
2. They have no money — they'll pay in equipment
3. Their amp is dying anyway (sparks/smoke during practice)
4. I can build the effects from safe household junk I can scavenge
5. Each effect needs specific scavenged parts from around the neighborhood
6. Assemble the effects → run the show → band is thrilled
7. They hand over the dead amp → I salvage the transformer + tubes → two Signal slots filled

---

## 5. Failure Feedback (Diegetic, Not Punishing)

Failures are CONTENT. No hard fail states — misfires give funnier show outcomes, never "game over."

| Wrong attempt | NPC / world response | Hint embedded |
|---|---|---|
| Offer the band money / ask them to just give you the amp | *"The amp? It still kinda works, man. Tell you what — make us a real show and it's yours."* | Sets the deal: do the show, get the amp |
| Try to run an effect missing a part | The build slot shows a gap; Mark VO: *"I need something to push the air."* (etc.) | Names the missing ingredient |
| Over-tune the fog (too much dry ice) | Garage fills completely — band coughs, can't be seen. *"DUDE. We're a band, not a weather system!"* | Comedy beat; effect still "counts" |
| Test the light show without dimming the garage | Washed out in daylight. *"...I can't see any of it, man."* | Teaches the time/place gate (do it dark) |
| Run the "spark fan" near the fog | Tinsel sticks to everyone, wet with fog. *"I've got tinsel in my MOUTH."* | Pure comedy; harmless |

---

## 6. Signpost Escalation Ladder

| Trigger | Source | Hint content | Subtlety |
|---|---|---|---|
| Day +0 | Tony Caruso | "We need it to look like KISS, man. Fog, lights, the works. You're the tech guy — figure it out." | Subtle (names the 3 effects) |
| Day +2 | Band drummer | "My uncle does the church Christmas display — boxes of lights in his garage. Just sayin'." | Medium — points at lights source |
| Day +3 | Ice-cream truck driver (ambient) | "Careful with that dry ice, kid — thing smokes like crazy in a bucket." | Medium — points at fog source |
| Day +5 | Mark VO at the garage workbench | "Fan, lights, projector, some tinsel... I've built scarier things out of less. Probably will again." | Obvious — lists the kit |
| Day +7 | Danny via comms (if unlocked) | *"Mark — the Caruso kids? Their amp was always one practice from death. If you ever get your hands on it, the transformer alone is worth the whole favor."* | Bail-out — names the reward + nudges the deal |

**Stop-condition:** hints stop once the player builds the first effect.

---

## 7. Trade Chain

| Step | Player has | Gives to | Receives | Notes |
|---|---|---|---|---|
| 1 | (agreement) | Caruso band | The "show wish-list" (3 effects) | The mini-blueprint that teaches the machine UI |
| 2 | Scavenged parts | (garage workbench) | 3 assembled effects (Fog Machine, Light Rig, Spark Fan) | Simple icon-combine, no stability fail |
| 3 | 3 working effects | Caruso band | Run "the show" → band thrilled | Set-piece cue sequence |
| 4 | (favor complete) | Caruso band | **Dead amp** → salvage **Marshall transformer** + **12AX7 tubes** | Two Signal slots filled, direct use |

### The 3 effects → scavenge map

| Effect | Safe household parts | Canonical source (reuses existing locations) |
|---|---|---|
| **Fog Machine** | Box fan + dry ice (+ optional humidifier) | Dry ice = ice-cream truck / fish counter (soft timer: melting); fan = home/shed |
| **Light Rig** | Christmas lights + slide projector + colored cellophane + foil "mirror ball" | Lights = drummer's uncle / own basement boxes; projector = rich-neighbor kid / attic |
| **Spark Fan (fake sparks)** | Box fan + tinsel/foil strips, lit by the projector | Tinsel/foil = home; reuses the fan if player has two, else a second fan from surplus store |

---

## 8. Time/Place Gates

| Pre-condition | Why |
|---|---|
| The garage is darkened (evening, or door down) for the show | Light/fog effects wash out in daylight (taught via failure) |
| Player has all 3 effects built before triggering "the show" | The set-piece needs all cues ready |
| Dry ice used reasonably fresh | Soft melting timer adds light urgency to that fetch (not a hard fail) |

---

## 9. Cutscenes & Memorable Beats

- **Quest opening beat:** Mark walks up to the garage mid-practice; the band's amp coughs a puff of smoke.
  Tony: *"See? She's got SOUL."* Mark VO (eyeing the amp): *"She's got a Marshall output transformer is
  what she's got."*
- **Mid-quest comedy beat (fog test):** Mark cranks the fan-and-dry-ice rig; garage vanishes into fog; a
  bandmate's disembodied voice: *"...are we still here?"* Mark VO: *"Define 'here.'"*
- **The Show (set-piece):** all three effects fire during the song in a little timed cue sequence. Fog rolls,
  Christmas lights strobe off the foil ball, tinsel "sparks" blow across the band. It is gloriously cheap and
  the band plays like it's Madison Square Garden.
- **Reward beat:** the amp finally dies for good with a sad *womp*. Tony, undaunted: *"Eh. It's yours, man —
  you EARNED it."* Mark cradles the dead amp like treasure. Mark VO: *"Two slots. In one night. Rock and roll."*
- **Warm beat (optional):** an adult (dad/Stan-type) peers into the fog-filled, glowing garage expecting
  catastrophe — and finds only kids putting on a goofy show. Small approving shake of the head. Possible
  minor respect bump.

---

## 10. Connections

- **Characters introduced/deepened:** Tony Caruso (deepened — now the band-favor hub, voice locked); the
  Caruso band (introduced — drummer + 1–2 bandmates need light character notes)
- **Locations introduced/deepened:** Caruso garage (band HQ — mirrors the basement-HQ motif); reuses
  ice-cream truck, shed, surplus store, neighbor's house
- **Era beats taught:** 1970s garage-band culture; concert-stagecraft envy (KISS/arena rock); dry-ice fog,
  slide projectors, Christmas-light rigs as the homemade special-effects of the era
- **Tear/money impact:** small cash possible; no Tear impact (helping friends, nothing taken from anyone)
- **MECHANICAL:** this is the **machine-loop tutorial** — first time the player runs wish-list → scavenge →
  assemble → power-on → collect-part, on a harmless, comedic target.

---

## 11. Open Questions

- ❓ **Band member names/characters.** Tony Caruso is canon; the band needs a drummer + 1–2 bandmates with
  light character notes (the drummer is already used as a hint-source — give him a name).
- ❓ **Exact number of effects — 3 (recommended) vs 2.** 3 feels full without bloating; could trim to 2 (fog +
  lights) if Act 1 pacing is tight.
- ❓ **Does the amp "blow during the show" or arrive already dead?** Blowing during the finale is funnier and
  motivates the handover; decide in dialogue pass.
- ❓ **Second fan sourcing** for the Spark Fan — reuse one fan across effects, or scavenge a second? Minor.
- ❓ **Where exactly does this sit in Act 1 order** relative to Q-001/Q-002? It's a strong EARLY teaching quest;
  consider placing it before or alongside the Elga chain.
- ❓ **Tracker reconciliation:** update `_quest-item-tracker.md` to show both Caruso amp parts yielding from
  Q-003 (currently listed as two separate unnumbered Caruso trades).
