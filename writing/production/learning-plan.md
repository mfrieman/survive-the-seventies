# Learning Plan — Unity + Adventure Creator (Survive the 70s)

**Status:** 📝 Reference plan (not date-bound). Captured 2026-05-29.
**Scope:** PRODUCTION/tooling doc, not story canon. For the eventual Ren'Py → Unity port.
**Context:** Mark + Iwona are both **C# experts**, **new to Unity**. Months of game design/writing come FIRST — this is a plan to bank, not start now.

---

## Guiding principle

You are NOT trying to "learn Unity completely." You are learning:
1. **Just enough Unity editor literacy** to place objects and build scenes, and
2. **Deep Adventure Creator (AC) fluency** — because **AC is your gameplay engine.**

Since you already know C#, skip "learn to code in Unity" courses entirely. AC builds hotspots, dialogue, inventory, and objectives in a **visual editor, largely without code** — which maps almost 1:1 onto this game (Q-001 = hotspots + dialogue + inventory).

---

## The 4-tier ramp (priority order, not a calendar)

### Tier 1 — Unity editor literacy (FREE, do first)
- **Unity Learn → Essentials Pathway** only: GameObjects, scenes, prefabs, Inspector, importing assets.
- Skip Creative Core for now (Iwona revisits it in Tier 3).
- Outcome: you understand how Unity "thinks" and can build a simple scene.

### Tier 2 — Adventure Creator fluency (the multiplier)
- **AC official tutorials** (`adventurecreator.org/tutorials`) — the definitive AC resource.
- Order: **"Making a 3D Game" primer → Interactions → Conversations → Inventory → Objectives.**
- **Hands-on milestone:** build one clickable room with one talking NPC and one inventory pickup. That's this whole game in microcosm.
- Outcome: you can build interactive objects, NPC dialogue, and quest logic with little/no code.

### Tier 3 — Scene craft (mostly Iwona's lane)
- Unity **lighting, materials, NavMesh**, and the **Synty POLYGON import workflow** — pulled as needed.
- Unity Learn **Creative Core** helps here.
- Outcome: a real playable world, not just test scenes.

### Tier 4 — General Unity course (OPTIONAL, skim)
- **GameDev.tv "Complete C# 3D Game Developer"** (Unity 6 version) — only if one of you wants deeper Unity-API comfort for custom AC actions later.
- **Cherry-pick** scene-flow + architecture lessons. **Skip** player-controller / physics / enemy-AI projects (irrelevant to point-and-click).
- **Do NOT gate starting the game on finishing this.**

---

## Spend rules

| ✅ Worth paying for | ❌ Skip |
|---|---|
| Adventure Creator (the asset itself — your engine) | Any "build a point-and-click game in Unity" Udemy course — it hand-codes from scratch the exact system AC already gives you |
| GameDev.tv Complete C# 3D — ONLY on sale (~$15), and only as optional Tier 4 | Full-price Udemy (always wait for the recurring ~$15 sale) |

**Key finding:** There is **no high-quality Udemy course built around Adventure Creator** — AC's own free tutorials are the best resource. The Monkey-Island-style Udemy courses teach you to *reinvent* AC, which wastes your time. Mark's instinct (free items > Udemy here) is correct.

---

## Division of labor
- **Mark:** hotspots, interactions, quests, dialogue, game logic (AC layer).
- **Iwona:** environments, scene composition, lighting, asset import/placement (Unity scene layer) + the custom POLYGON props (see asset-plan.md).

---

## Confirmed technical targets (verified live 2026-05-29)
- **Engine version: Unity 6.** Both Adventure Creator and the GameDev.tv course support it — start there, not an older LTS.
- Adventure Creator: Unity Asset Store pkg 11896; confirmed Unity 6 compatible.

## Verified links
- Unity Learn (free pathways): https://learn.unity.com/
- Adventure Creator tutorials: https://adventurecreator.org/tutorials
- Adventure Creator (asset): https://assetstore.unity.com/packages/tools/game-toolkits/adventure-creator-11896
- GameDev.tv Complete C# 3D (Unity 6): https://gamedev.tv/courses/unity6-complete-3d (Udemy mirror: udemy.com/course/unitycourse2)

---

## One-line summary
**Free Unity Essentials + free Adventure Creator tutorials are your core path. Buy AC the asset; optionally grab GameDev.tv on a $15 sale. Skip every point-and-click Udemy course — AC already is the point-and-click engine.**
