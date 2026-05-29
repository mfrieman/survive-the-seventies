# Quests — Folder Purpose & Conventions

**Status:** Working folder for designed, locked quest specs. Each quest spec is the single source of truth that Ren'Py implementation will follow.

---

## Structure

- `README.md` — this file
- `_template.md` — the locked quest-spec template (copy when designing a new quest)
- `_quest-item-tracker.md` — global table of which NPC has what, which quests yield what, which machine parts come from where. Keeps the economy honest.
- `Q-001-elga-paper-drive.md` — first worked example (Playboy magazine)
- `Q-002-elga-garden.md` — chained sequel (marijuana)
- Future: `Q-NNN-<short-name>.md` per quest, numbered in lock order

## Promotion path

1. **Idea** lives in `quest-ideas-inbox.md` (root of `writing/`)
2. When promoted, copy `_template.md` → `Q-NNN-<name>.md`, fill it out
3. Update `_quest-item-tracker.md` with any new NPC/item/yield
4. Mark inbox entry `[PROMOTED → Q-NNN]`

## Naming

- IDs are sequential by lock order (Q-001, Q-002, …)
- Filename: `Q-NNN-<short-kebab-name>.md`
- IDs are stable — do not renumber if quests are reordered

## Status legend

- 🔒 **LOCKED** — ready for Ren'Py implementation
- 📝 **DRAFT** — spec written but movable
- ❓ **OPEN** — known gap inside the spec
- 🅿️ **PARKED** — designed but deferred from current scope
