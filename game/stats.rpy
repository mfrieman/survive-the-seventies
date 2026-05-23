## Survive the 70s — stats.rpy
## The Kid class: stats, inventory, and the one reusable skill_check.
##
## This is pure Python, wrapped in `init python:` so it runs once at game
## start before any scene executes.

init python:

    import random

    class Kid:
        """The 14-year-old protagonist. One instance for the whole save."""

        def __init__(self):
            # HP-style stats (0-100, clamped on change)
            self.bones = 100              # physical health
            self.moms_patience = 100      # social/parental health
            self.cool = 50                # what the older kids think
            self.cash = 0                 # set in Scene 1 by allowance check

            # Skills (0-100; opposed pairs roll against each other)
            self.common_sense = 40        # voice of caution
            self.dumb_kid_bravery = 80    # voice of "hold my Brain Freeze"

            # Inventory — populated by Scene 2 (Garage loadout)
            self.loadout = set()

            # Flags — set by scene choices, read by later scenes
            self.flags = {}

        # ---------- stat helpers ----------

        def adjust(self, **changes):
            """Bulk stat change with clamping. e.g. kid.adjust(bones=-10, cool=+5)."""
            for stat, delta in changes.items():
                current = getattr(self, stat)
                new_val = max(0, min(100, current + delta))
                setattr(self, stat, new_val)

        def has(self, item):
            return item in self.loadout

        def flag(self, name, value=True):
            self.flags[name] = value

        def get(self, name, default=False):
            return self.flags.get(name, default)

        # ---------- the one skill check ----------

        def skill_check(self, stat, difficulty=50):
            """
            Roll d100 + stat against difficulty.
              crit  : roll >= difficulty + 30   (spectacular win)
              pass  : roll >= difficulty         (barely worked)
              fail  : roll <  difficulty         (something went wrong — usually funny)
            Returns 'crit', 'pass', or 'fail'.
            """
            roll = random.randint(1, 100) + getattr(self, stat)
            if roll >= difficulty + 30:
                return "crit"
            if roll >= difficulty:
                return "pass"
            return "fail"

        def opposed_check(self, stat_a, stat_b, base=50):
            """
            Opposed check: roll stat_a vs stat_b. Use for
            Common Sense vs Dumb Kid Bravery moments.
            Returns 'crit', 'pass', or 'fail' from stat_a's perspective.
            """
            a = random.randint(1, 100) + getattr(self, stat_a)
            b = random.randint(1, 100) + getattr(self, stat_b)
            margin = a - b
            if margin >= 40:
                return "crit"
            if margin >= 0:
                return "pass"
            return "fail"


## Create the singleton Kid instance. `default` (not `define`) means it
## gets saved with the player's save file.
default kid = Kid()


## Optional: a tiny on-screen debug HUD so we can SEE stats during dev.
## Toggle with the 'd' key. Remove before shipping.

screen dev_hud():
    zorder 100
    if persistent.show_dev_hud:
        frame:
            xalign 1.0
            yalign 0.0
            xpadding 12
            ypadding 8
            background "#000000c0"
            vbox:
                spacing 2
                text "DEV HUD" size 14 color "#ffcc00"
                text "Bones:    [kid.bones]"          size 14 color "#ffffff"
                text "Patience: [kid.moms_patience]"  size 14 color "#ffffff"
                text "Cool:     [kid.cool]"            size 14 color "#ffffff"
                text "Cash:     $[kid.cash]"           size 14 color "#ffffff"
                text "Sense:    [kid.common_sense]"   size 14 color "#aaaaaa"
                text "Bravery:  [kid.dumb_kid_bravery]" size 14 color "#aaaaaa"
                if kid.loadout:
                    text "Has: [' '.join(sorted(kid.loadout))]" size 12 color "#88ccff"

init python:
    if persistent.show_dev_hud is None:
        persistent.show_dev_hud = True   # default ON during dev

## Bind 'd' to toggle the HUD.
init python:
    config.keymap.setdefault('toggle_dev_hud', []).append('d')

label toggle_dev_hud:
    $ persistent.show_dev_hud = not persistent.show_dev_hud
    return

## Show the HUD on every screen.
init python:
    config.overlay_screens.append("dev_hud")
