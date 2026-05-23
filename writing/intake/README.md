# Intake (YAML)

Mark's structured memory dump for *Survive the 70s*. One file per entity type, YAML, schema embedded as comments.

## Files

| File | What goes here |
|---|---|
| `people.yaml` | Family, friends, neighbors, teachers, bullies, crushes, famous-locals |
| `places.yaml` | The house, the block, the town, destinations (Cursed Forest, Ocean Side, Chocolatetown, etc.) |
| `things.yaml` | Toys, gadgets, foods, candy, contraband, gear |
| `media.yaml` | TV, movies, music, magazines, comics, books, games |
| `customs.yaml` | Weird normal stuff — latchkey life, hose water, smoking sections, riding in the truck bed |
| `banned-or-gone.yaml` | Things that no longer exist, got pulled, or were banned (lawn darts, clackers, leaded gas, etc.) |
| `stories.yaml` | Actual or quasi-actual events — anchors for game scenes |

## Conventions

**IDs:** `kebab-case`, unique within file. Used to cross-reference. Don't change once set.

**`reality` tag on every entry:**
- `real` — actually happened / existed exactly like this
- `mixed` — real with embellishment (you'll note what's tweaked in `notes`)
- `fake` — invented for the game world
- `parody` — real thing renamed for the parody universe (e.g., KISS → BLAZE)

**`change_name: true`** — if a real person should have their name swapped for the game. I'll handle the renaming downstream.

**`tags`** — free-form list. Use whatever helps you (`dangerous`, `food`, `forgotten-tech`, `gross`, `summer-only`, etc.). I'll cluster them.

**`audience`** — who this lands for:
- `gen_x` — your generation goes "oh god I forgot"
- `gen_z` — kids today go "wait, you actually DID that?"
- `both` — hits both ways
- (leave blank if unsure)

**Prose fields** (`description`, `notes`, `story`) use YAML block scalars (`|` preserves newlines, `>` folds):
```yaml
description: |
  Multiple lines
  preserved exactly as written.
```

**Don't worry about completeness.** Half-finished entries are fine. I'll surface follow-up questions when I process.

## Workflow

1. You dump into these files (voice → OneNote → paste here, or type directly).
2. When you've got a batch ready, tell me "process intake" and I'll:
   - Validate YAML structure
   - Distribute content into `world-map.md`, `world.md`, new `cast.md`, new `era-toolbox.md`, `scene-outlines.md`
   - Surface cross-references and puzzle hooks
   - Ask follow-up questions

3. Raw intake stays in this folder as the canonical source. Distributed docs are derived artifacts — if there's ever a conflict, intake wins.

## Tips

- **You don't have to fill every field.** Leave out what you don't have.
- **Bias toward writing it down crooked over not writing it down.** I can clean up later.
- **Cross-reference loosely** in `notes` — say "Tommy's older brother" and I'll resolve it.
- **Use parody names if you've got 'em, real names if not.** I'll parody-swap during processing.
