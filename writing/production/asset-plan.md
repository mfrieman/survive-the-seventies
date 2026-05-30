# Asset Plan — Survive the 70s (Unity / Adventure Creator)

**Status:** 🔒 Art line LOCKED 2026-05-29. Pack mapping = 📝 working manifest (refine as scenes are designed).
**Scope:** This is a PRODUCTION/tooling doc, not story canon. It informs the eventual Ren'Py → Unity decision.

---

## Locked Decisions

- **Core art line: Synty POLYGON.** Committed. Do NOT mix in SIMPLE or POLYGON MINI — crossing Synty lines reintroduces the exact multi-publisher "blend" mismatch we're avoiding. One line, library-wide coherence.
- **Verified scope: 80 POLYGON packs available for Unity** (filtered: https://syntystore.com/collections/polygon?filter.p.m.custom.engine=Unity — confirmed 80 via collection JSON, May 29 2026). More than enough coverage for every location in this game. POLYGON - Palm City (boardwalk/beach/pier for Oceanside/Act 3) confirmed present.
- **Acquisition: SyntyPass subscription** (~$30 USD/mo, unlocks the full 130+ pack library, ~$10/mo back in store credit toward permanent per-pack licenses, cancel when the project ships). Subscribe during development; buy permanent licenses only for the packs actually shipped.
- **Engine sequencing UNCHANGED:** fully prototype + design gameplay in **Ren'Py first**. Only port to **Unity + Adventure Creator** if Ren'Py proves it's a good game. This asset plan de-risks that port; it does not trigger it early.

## Why POLYGON + Adventure Creator shrinks the asset problem

- AC is **fixed/scripted-camera, scene-by-scene** — no seamless walkable city needed. We need ~25–40 framed *scene compositions*, not an open world. Far fewer assets; within-scene matching is all that matters.
- Low-poly is the **lowest-skill-floor, most-extensible** 3D style — Iwona can model custom period/hero props in POLYGON style far faster than matching any photoreal pack. Division of labor: **Synty = bulk environment; Iwona = hero/period custom.**

---

## Buy/Subscribe Manifest (all POLYGON line)

### Acts 1–2 — Burnsville suburb
| Need | Pack(s) |
|---|---|
| Neighborhood houses, streets, lawns, fences | **Town Pack** (core) + **City Pack** (building variety) |
| Elga's overgrown garden, sheds, rural yard | **Farm Pack** + **Nature Pack** |
| Burnsville Electronics, antique shop, deli, surplus store | **Shops Pack** + **Shopping Plaza Map** + **Office Pack** + **Coffee Shop (FREE)** |
| Home interiors + basement workshop | **Town Pack** modular house kit + 412 props (see Interiors section) + **Construction Pack** (workshop tools) |

### Interiors (RESOLVED — no gap)
Synty has no single "interiors" pack; interiors = each themed pack's **modular building kit + prop library**. Verified contents:
| Interior | Pack | What it gives |
|---|---|---|
| Inside houses | **Town Pack** | Modular house kit + preset houses + 412 props (kitchen/living/bedroom/bath) |
| Inside shops | **Shops Pack** ⭐ | 1,933 prefabs, fully modular shop buildings, shelves/counters/tables/food/items |
| Business/civic interiors | **Office Pack** | Modular pieces + desks/chairs/computers/break rooms |
| Aged/creepy interiors (e.g. Elga's old house) | **Horror Mansion** | 650+ prefabs, modular interior rooms — retexture away the horror |
| Bar/lounge interiors (optional) | **Nightclubs** | Modular bars, sofas, lounges |

Workflow note: interiors are **assembled** (modular walls/floors + placed props), not loaded pre-built — fits Adventure Creator's room-by-room scenes. This is set-dressing work, Iwona's lane.

### Custom period props (LOW DIFFICULTY — a strength, not a risk)
Items like a **1970s console TV, rotary phone, Foto Hut signage** that Synty's modern packs won't have are easy to model in POLYGON style:
- Low-poly = lowest-skill-floor 3D style. A 70s TV (box + screen plane + knobs + legs) ≈ 30–80 min for a first-timer in Blender, minutes once experienced.
- No sculpting/high-poly. The Synty look comes from **flat color via Synty's shared palette texture** — match palette + proportions and it drops in seamlessly. Iwona's graphic background makes this easier.
- **First** custom prop costs a few hours (learn Blender UI + Synty palette workflow + export-to-Unity round-trip); every prop after is fast (reusable pipeline).
- A TV with a **live on-screen picture** (machine "first contact" beat) = emissive screen-plane *shader* trick, not harder modeling.
- The **hero machine** is the only genuinely involved custom model. Everyday period props are afternoon warm-ups.

### Act 3 — Oceanside
| Location (locked L1–L5) | Pack |
|---|---|
| Boardwalk, pier, beach, main-street shops (general Oceanside) | **Palm City** (1,100+ assets — covers most of Act 3) |
| L1 Bank → Museum | **Heist Pack** (modular bank + vault) |
| L5 Boardwalk hotel | **Palm City** |
| L3 Hill + Denise's father's mystical rock gardens | **Nature Pack** + **Nature Biomes S1/S2** |

### Characters (Sidekick modular system — one rig for whole cast)
| Need | Pack |
|---|---|
| Kids: Danny/Mark, Bobby, Mickey, Boy Scout friend, Caruso kids, teenagers | **POLYGON Kids Pack** |
| Adults: Elga, Stan, Denise, Rosa, Pat the Vet, Playboy Tony | **Modern Civilians – Sidekick** (modular → retexture per NPC) |
| Mobility (Maggie, if needed) | **Wheelchair Pack** |
| Movement + comedy poses | **ANIMATION – Base Locomotion + Idles + Emotes and Taunts** |

### UI / Inventory
| Need | Pack |
|---|---|
| Menus + the four knowledge UIs (Map / People / 70s Notebook / Machine Blueprint) | **INTERFACE – Modern Menus** |
| Machine-part inventory icons + blueprint checklist | **POLYGON Icons Pack** |

---

## FREE pipeline-test packs (validate before paying)
Test the Synty → Unity → Adventure Creator pipeline at zero cost first:
**POLYGON Starter Pack (FREE)**, **Coffee Shop (FREE)**, **Sidekick FREE Starter Pack**, **Quad Bike (FREE)**, **SIMPLE Sky (FREE)**.
Goal: drop a character in a room, wire one AC hotspot, confirm the look/feel. THEN subscribe.

---

## Custom-model list (Iwona's bounded scope — what POLYGON does NOT cover)
1. **The soul-displacement machine** (hero prop — custom regardless)
2. **Foto Hut kiosk** (great first custom build — tiny)
3. **A church** (L4 fountain-behind-church — no POLYGON church pack)
4. **A waterslide attraction** (L3 — not in Palm City's beach set)
5. **Period cars** (Synty cars read modern — retexture/custom a 70s wagon/sedan)
6. **1976 home-interior dressing** (period appliances, the single TV)

~6 bounded items, all in the easiest 3D style to model. Everything else: subscribe + drop in.

---

## Open / to confirm
- ⚠️ **No dedicated POLYGON home-interiors pack.** Town/City packs include some furniture; Heist/Office cover commercial interiors. Confirm Town/City furniture is enough for the house hub (Acts 1–2) before relying on it — else add custom interior dressing.
- Publisher "ID 18116" (the "Toon packs" Mark linked) — evaluated as alternative core and rejected: a second publisher reintroduces the blend problem. POLYGON stays the single core.
- Period-character read: POLYGON modular clothing can be retextured toward 70s (bell-bottoms, wide collars) — Iwona's retexture scope.

---

## Verified sources (checked live 2026-05-29)
- SyntyPass terms: https://syntystore.com/products/syntypass
- POLYGON – Palm City: https://assetstore.unity.com/packages/3d/environments/urban/polygon-palm-city-art-by-synty-362342
- POLYGON – Town Pack: https://assetstore.unity.com/packages/3d/environments/urban/polygon-town-pack-art-by-synty-121115
- POLYGON – Heist Pack: https://assetstore.unity.com/packages/3d/environments/urban/polygon-heist-pack-art-by-synty-97949
- Full Unity catalog (180 packs): https://syntystore.com/collections/unity-asset-packs
