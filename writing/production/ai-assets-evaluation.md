# AI Asset Generation — Evaluation

**Status:** Advisory note. RE-EVALUATE AT UNITY PORT TIME — generative 3D is moving fast and will be better by then.
**Date captured:** May 29, 2026
**Question:** Can we use AI to generate all the game's assets? (Iwona's idea.)

---

## Verdict (one line)

**Synty POLYGON stays the consistent backbone. AI is a helper layer (textures, concept art, 2D), NOT the asset factory.** Going AI-first would dismantle the consistency that buying Synty already solved.

---

## The core mismatch

The AI tools we know — Firefly, Midjourney, Stable Diffusion — generate **2D images**. Unity + Adventure Creator needs **3D models**: meshes, clean topology, UV maps, textures, rigs. A great Midjourney house picture is **not importable as a Unity building**. So the real question isn't "can AI make images" (yes) — it's "can AI make *game-ready 3D*" — a younger, harder technology.

## What's true (the good news)

- AI-3D genuinely crossed the usable-for-games threshold in 2025–2026.
- Tools: **Meshy 5, Tripo P1, Rodin Gen-2, CSM Cube 2** — text/image → 3D with auto-UV + Unity export. Tripo explicitly markets "game-ready, export to Unity."
- So Iwona is **factually right** that AI can now make 3D assets. This isn't 2022.

## The trap (why not for THIS game)

- Our biggest art requirement is **consistency** (one coherent look across ~200 objects + carefully framed AC scenes).
- AI's biggest weakness is **consistency** — and it's **worse in 3D** than 2D, because you need consistency on TWO axes: art-style AND topology/scale. AI-3D still produces messy, non-uniform topology and varying styles object-to-object.
- The 2D-consistency pain Iwona already knows from Firefly/MJ does **not** go away in 3D — it compounds.
- **Synty POLYGON already solved consistency by construction** — that's the whole reason we chose it. Generating assets with AI re-introduces the exact problem the ~$30/mo Synty plan eliminated. Matching AI output TO Synty's style is even harder than internal consistency.

## On the specific technical ideas

- **"Microsoft pays for my AI / bring my own model":** those credits + the models powering Clawpilot are **text + 2D-image** (Azure OpenAI, DALL·E-class). They do **not** generate game-ready 3D. The "free models" angle doesn't transfer to the 3D problem.
- **5090 + local Stable Diffusion:** generates **2D images for free** — excellent for textures, concept art, skyboxes, UI, reference. **Not 3D models.** The 3D-gen tools are mostly cloud SaaS, not the local-SD pipeline. A 5090 IS justifiable for running Unity, local 2D-texture SD, and Iwona's Blender/modeling — just not as a "free 3D asset factory."
- **Unity's own AI:** Muse retired Oct 1, 2025 → folded into **Unity AI (Unity 6.2+)**. Does in-editor texture/sprite/assist generation, **not** full game-ready 3D meshes.

## The hybrid that actually works

| Use AI for ✅ | Keep Synty / hand-craft for ❌ |
|---|---|
| Textures & materials (retexture Synty props to read "1976," period wallpaper, signage) — local SD shines here | Bulk 3D environment (buildings, props, characters) — Synty, guaranteed consistency |
| 2D concept art & mood boards before modeling | Hero/period custom props (machine, Foto Hut, church) — hand-modeled in POLYGON style |
| Skyboxes, posters, in-world 2D art, UI elements | Anything that must match across many scenes |
| A single one-off prop via Meshy/Tripo, then manually cleaned in Blender | A whole consistent asset library from scratch |

## Re-evaluation trigger

This is months away. When we actually reach the Unity port, re-test Meshy/Tripo/Rodin/Unity AI — by then AI-3D consistency may be good enough to shift more work into it. **Tonight's decision: Synty backbone, AI as helper, not factory.**
