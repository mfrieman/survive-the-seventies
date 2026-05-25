## Survive the 70s — script.rpy
## Entry point. Ren'Py always starts at `label start:`.
##
## Day-by-day structure: each scene lives in game/scenes/0X_<name>.rpy
## and we jump into it from here.

## ---------- Characters / narrator voices ----------

define narrator = Character(None, what_italic=True, what_color="#dddddd")
# narrator has no nameplate, italic dialogue, off-white — adult-you in 2026

define mom    = Character("Mom",    color="#e89b3a")
define dad    = Character("Dad",    color="#9a7b3a")
define tommy  = Character("Tommy",  color="#5fa3d6")
define kid_v  = Character("Me",     color="#ffffff")  # the 14yo's own voice

# Inner voices (Disco Elysium-style skill voices, scaled to 3)
define common_sense = Character("Common Sense", color="#7fb069", what_italic=True)
define brave        = Character("Dumb Kid Bravery", color="#d64550", what_italic=True)
define imag_mom     = Character("Mom (Imagined)", color="#e89b3a", what_italic=True)


## ---------- Placeholder backgrounds ----------
## Real painted art will replace these. For now, flat color so the game runs.

image bg kitchen   = "#3a2e1f"
image bg garage    = "#2a2a2a"
image bg quikmart  = "#503820"
image bg creek     = "#1f3320"
image bg dusk      = "#1a1a3a"
image bg black     = "#000000"


## ---------- Entry point ----------

label start:

    scene bg black with fade

    centered "{size=+12}SURVIVE THE 70s{/size}\n\n{size=+2}— a concept demo —{/size}\n\n{size=-4}press any key{/size}"

    scene bg black with fade
    centered "{i}Saturday, July 14, 1979{/i}\n\n{size=-4}somewhere in suburban Maryland{/size}"

    jump kitchen_scene


## The actual scenes live in game/scenes/.
## Ren'Py auto-discovers any .rpy file under game/, so we just include them
## by reference (the `label`s below are defined in those files).
