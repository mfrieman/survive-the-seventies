## Survive the 70s — options.rpy
## Project-level configuration. Game name, version, save dir, etc.

define config.name = _("Survive the 70s")
define gui.show_name = True
define config.version = "0.1.0"

define gui.about = _p("""
A comedic point-and-click adventure exaggerating the everyday dangers
of being a kid in 1979.

Concept demo — not for distribution.
""")

## Default save directory name. Tucked under user's Documents/RenPy.
define build.name = "survive-the-seventies"

## Window icon (we'll replace with custom art later).
# define config.window_icon = "gui/window_icon.png"

## Skip splashes and reduce ceremony during dev.
define config.has_autosave = True
define config.autosave_slots = 3
default preferences.skip_unseen = True

## Sound channels (tweak when we add audio).
define config.has_music = True
define config.has_sound = True
define config.has_voice = False  # voice acting deferred

## Default text speed — slightly slower than Ren'Py default, more readable.
default preferences.text_cps = 35

## Build distribution settings (for later — `renpy.exe . distribute`).
init python:
    build.classify("game/**.rpy", None)         # don't ship source
    build.classify("game/**.rpyc", "all")       # ship bytecode
    build.classify("game/scenes/**.rpy", None)
    build.classify("game/scenes/**.rpyc", "all")
    build.classify("**~", None)                  # no backup files
    build.classify("**.bak", None)
    build.classify("**/.git/**", None)           # never ship .git
