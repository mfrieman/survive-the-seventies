## How to run

From the project root (`C:\ai-game\survive-the-seventies`):

```powershell
# Run the game directly (fastest dev loop)
& "C:\ai-game\tools\renpy-8.5.3-sdk\renpy.exe" .

# Or open the Ren'Py launcher and pick the project from the sidebar
& "C:\ai-game\tools\renpy-8.5.3-sdk\renpy.exe"
```

## Dev controls

- `d` — toggle the dev HUD (stats overlay top-right)
- `Esc` — main menu / quit
- `Ctrl` — fast-forward already-seen dialogue (Ren'Py default)
- `Shift+R` — reload the script without restarting the game (HUGE for iteration)
- Mouse wheel up — rollback / re-read previous lines

## File map

```
game/
  script.rpy        entry point + character definitions + image aliases
  options.rpy       project config (name, version, build rules)
  stats.rpy         Kid class, skill_check, dev HUD
  scenes/
    01_kitchen.rpy  Scene 1 (TEMPLATE — copy structure for 2-5)
  images/bg/        scene backgrounds (PNGs go here)
  images/portraits/ character portraits
  audio/music/      .ogg music
  audio/sfx/        .ogg sound effects
writing/
  bible.md          tone, voice, edge rules
  scene-outlines.md beat-by-beat for all 5 scenes
  world.md          parody universe (brands, bands, cars, etc.)
art-prompts/
  style-guide.md    reusable AI image-generation template
```
