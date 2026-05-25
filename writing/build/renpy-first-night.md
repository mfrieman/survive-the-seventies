# Ren'Py First Night — Hello Mark (Windows)

> **Goal:** In ~2 hours from a cold start, you will have a **playable scene** of *Survive the 70s* running on your Windows machine.
>
> **What "playable scene" means:** You will double-click an icon. A window will open. Black screen. The line *"Mark wakes up. Something is very wrong."* will appear. You'll click through Danny's first Book entry. You'll arrive at Burnsville Electronics, talk to Stan Burns, and choose one of three answers. Stan will respond. Fade to black. End.
>
> **It will NOT be:** a game, a save system, polished art, music, a menu, or anything you'd show anyone except yourself.
>
> **It WILL be:** running. With your dialog. On your screen. With Stan Burns in it.
>
> **That's the only thing that matters tonight.** Disco Elysium got built by getting *something* on screen first. Same playbook.

---

## Conventions in this doc

- **Code blocks** are copy-paste-ready. Don't retype them — copy them.
- **Bold lines** are actions you take.
- *Italic lines* are commentary / why we're doing this.
- **CHECKPOINT** blocks are optional pauses where you should confirm something works before moving on. Skip them if you're feeling brave; lean on them if you're feeling careful.

---

# STEP 1 — Install Ren'Py (~10 minutes)

## 1.1 Download

**Go to:** [https://www.renpy.org/latest.html](https://www.renpy.org/latest.html)

You want the **Windows SDK** — it's the larger download (~150 MB). Not the "ZIP for distribution." We need the SDK because it includes the launcher and the developer tools.

The file will be named something like `renpy-8.X.X-sdk.zip`.

## 1.2 Extract

**Extract the ZIP to a simple path with no spaces.**

Recommended location:
```
C:\renpy
```

After extraction you should have:
```
C:\renpy\renpy.exe         (the launcher — this is what you double-click to start Ren'Py)
C:\renpy\renpy.sh
C:\renpy\renpy\             (engine code — don't touch)
C:\renpy\launcher\          (the launcher app — don't touch)
C:\renpy\projects\          (where your games will live)
```

> *Why a path with no spaces? Ren'Py is generally fine with spaces but Python scripting around it sometimes isn't, and your project paths will be inside this folder. Saves headaches.*

## 1.3 Launch

**Double-click `C:\renpy\renpy.exe`.**

You'll see the Ren'Py launcher — a window with a project list on the left and big buttons on the right ("Launch Project," "Edit File," etc.). The list will include some demo projects: *The Question*, *Tutorial*, *The Worker's Way*, etc.

**CHECKPOINT 1:** The Ren'Py launcher window is open and you can see the demo projects.

---

# STEP 2 — Create the Project (~10 minutes)

## 2.1 Create new project

**In the Ren'Py launcher, click "+ Create New Project"** (left side, near the bottom of the project list).

Ren'Py will walk you through a wizard.

### Settings:

| Setting | Value |
|---|---|
| **Project Name** | `survive-the-seventies` |
| **Resolution** | `1920 x 1080` (full HD — what modern monitors expect) |
| **Color Scheme** | Pick anything — doesn't matter, we'll override |
| **Default Language** | English |

> *Why 1920x1080? It matches what you'll grab off Google Images for placeholder backgrounds. We can change later.*

**Click "Continue" through the wizard until it creates the project.**

When done, Ren'Py will return you to the launcher with `survive-the-seventies` selected in the project list.

## 2.2 Locate your project on disk

Your project now lives at:
```
C:\renpy\projects\survive-the-seventies\
```

**Open that folder in File Explorer in a separate window.** Keep it open — we'll come back to it constantly.

You should see this structure:
```
survive-the-seventies\
├── game\                   ← This is where your work lives
│   ├── script.rpy          ← The main script file (we'll edit this)
│   ├── options.rpy         ← Configuration
│   ├── gui.rpy             ← Visual styling
│   ├── screens.rpy         ← UI screens
│   └── images\             ← Backgrounds, character sprites, etc.
└── (other Ren'Py engine files)
```

**The only file you'll touch tonight is `game\script.rpy`.**

## 2.3 Test that it runs

**Back in the Ren'Py launcher, with `survive-the-seventies` selected, click "Launch Project."**

A game window will open showing the default Ren'Py template — a few lines of placeholder dialog about Eileen, Ren'Py's mascot. Click through it. It ends.

**Close the game window** (or hit Escape → Quit).

**CHECKPOINT 2:** You saw the default Ren'Py demo run inside your project. Now we wipe it and write our own.

---

# STEP 3 — Hello Mark (~20 minutes)

## 3.1 Open script.rpy in a text editor

**You need a real text editor. Three options, in order of preference:**

1. **VS Code** (free, best for this) — [https://code.visualstudio.com/](https://code.visualstudio.com/). Install if you don't have it. Then install the "Ren'Py Language" extension from the Extensions panel (search "renpy").
2. **Notepad++** (free, lightweight) — [https://notepad-plus-plus.org/](https://notepad-plus-plus.org/)
3. **Notepad** (built-in, last resort) — works but no syntax highlighting

> *Why not Ren'Py's built-in editor? It exists but VS Code is dramatically better. If you have VS Code, use it.*

**Open the file:**
```
C:\renpy\projects\survive-the-seventies\game\script.rpy
```

You'll see something like:
```renpy
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # ...
```

## 3.2 Replace everything with this

**Select ALL the text in `script.rpy` and delete it. Then paste this:**

```renpy
# survive-the-seventies / script.rpy
# First night build — Hello Mark

# ============================================================
# CHARACTERS
# ============================================================

define mark = Character("Mark", color="#9cd0ff")
define stan = Character("Stan Burns", color="#ffcf78")
define steve = Character("Steve Burns", color="#ffa040", what_prefix="(from the back) ")
define narrator = Character(None, what_italic=True)


# ============================================================
# GAME START
# ============================================================

label start:

    # Black screen, fade in
    scene black with fade

    # Narrator beat
    narrator "Mark wakes up."

    narrator "Something is very wrong."

    # First Mark voice-over
    mark "...okay. Okay okay okay."

    mark "This is not my bedroom."

    mark "This is not my century."

    # End of scene for now — we'll add more in Step 5
    return
```

**Save the file.** (Ctrl+S)

## 3.3 Run it

**Back in the Ren'Py launcher, click "Launch Project."**

You should see:
- Black screen
- *Mark wakes up.* (italic, no name shown)
- *Something is very wrong.*
- **Mark:** ...okay. Okay okay okay.
- **Mark:** This is not my bedroom.
- **Mark:** This is not my century.
- The window closes (or returns to the main menu — that's fine).

**CHECKPOINT 3:** YOU JUST RAN A SCENE OF *SURVIVE THE 70S*. That's the milestone. Everything from here is decoration.

> *If you got an error:* The Ren'Py launcher will show a traceback. Copy it and paste it to me — most likely an indentation issue (Ren'Py uses Python-style indentation; 4 spaces per level, no tabs).

---

# STEP 4 — Add a Placeholder Background (~10 minutes)

## 4.1 Grab a placeholder image

We need a "Mark's bedroom" background image. We're not picky — anything that *vaguely* looks like a 1976 kid's bedroom will do for tonight.

**Quick options:**
- Google Image Search: *"1970s kids bedroom"* — pick anything that looks lived-in
- Or: a photo of a generic messy bedroom
- Or: literally a brown/wood-paneled wall

**Save the image as:**
```
C:\renpy\projects\survive-the-seventies\game\images\bedroom.jpg
```

If `images\` doesn't exist yet, create it.

> *Tip: Aim for 1920×1080 or larger. Ren'Py will scale it down; if you give it a tiny image it'll look ugly when scaled up.*

## 4.2 Reference it in the script

**Edit `script.rpy`. Replace `scene black with fade` with this block:**

```renpy
    # Black screen, fade in
    scene black with fade
    pause 0.5

    # Cut to bedroom
    scene bg bedroom with fade
```

Then **add this block at the very top of the file**, above the `define mark = ...` line:

```renpy
# ============================================================
# IMAGE DECLARATIONS
# ============================================================

image bg bedroom = "images/bedroom.jpg"
image black = "#000000"
```

> *Why declare images? Ren'Py needs to know the names. `bg bedroom` becomes an alias for the file path. The `black` declaration creates a solid black background as a fallback.*

**Save. Run it again.** (Launcher → Launch Project)

You should now see:
- Brief black screen
- Fades to your bedroom image
- Narrator + Mark lines play over the bedroom

**CHECKPOINT 4:** Mark's bedroom is on screen. You're in 1976.

---

# STEP 5 — Danny's First Book Entry (~30 minutes)

## 5.1 The setup

Mark just woke up. He's in 1976. Across the room — or under his pillow, depending on later canon — is **the Book** that Danny left behind. Tonight we play just the first entry.

> *Why this scene first? It's the inciting beat. It's also dialogue-only, no choices yet — perfect for our second scene.*

## 5.2 Add the Book character and the scene

**In `script.rpy`, add this near the top of the CHARACTERS section:**

```renpy
define danny = Character("Danny", color="#c89cff", what_italic=True)
```

> *Why italic? Danny's voice is always "read from the page" — never present. Italics on his lines is the visual convention that he's never in the room.*

**Then replace the existing `label start:` block with this expanded version:**

```renpy
label start:

    # Cold open
    scene black with fade
    pause 0.5

    # Bedroom reveal
    scene bg bedroom with fade

    narrator "Mark wakes up."

    narrator "Something is very wrong."

    mark "...okay. Okay okay okay."

    mark "This is not my bedroom."

    mark "This is not my century."

    pause 0.5

    mark "There's a notebook on the desk."

    mark "It wasn't here before. I mean — it was. I think. But I didn't put it here."

    pause 0.3

    mark "(Open it.)"

    pause 0.5

    # Book entry begins
    danny "If you're reading this, the machine worked."

    danny "If you're reading this and the room smells like burning, the machine also caught fire. Sorry."

    danny "I'm Danny. This is my body. You're me now. Sort of."

    danny "Don't panic. Don't tell anyone. Don't try to call your parents — they don't exist yet. Don't try to use a phone — you can't, anyway."

    danny "Read everything in this book before you do anything else."

    danny "There's a list of parts. I built the machine once. You're going to build it again."

    danny "Most of what you need is in the box under the desk. Some of it isn't."

    danny "When you have to ask someone about a part you don't recognize — go to Burnsville Electronics on Loch Raven. Ask for Stan. He won't ask why."

    danny "Don't lie to Stan."

    danny "Trust me."

    pause 0.5

    mark "(Close the book.)"

    pause 0.3

    # The receipts beat — physical onboarding cue
    mark "(There's something else in the box. Underneath the parts.)"

    mark "(A handful of receipts. Yellow carbon copies. \"Burnsville Electronics / Loch Raven Rd. / Stan or Steve Burns, Prop.\")"

    mark "(Dates. Months of them. Resistors. Capacitors. A vacuum tube. A length of copper wire.)"

    mark "(Danny went there a lot.)"

    mark "(Danny KNEW these people.)"

    pause 0.3

    mark "Burnsville Electronics. Loch Raven."

    mark "...okay."

    # End of scene 1
    return
```

**Save. Run it.**

You should see Mark wake up, narrate, find the Book, and read Danny's first entry. Notice that Danny's lines render in italic and a different color — that's the "voice from the page" convention working.

**CHECKPOINT 5:** Mark has read Danny's first message. The mission is on the table.

> *This dialog is yours to rewrite. Don't fall in love with my draft. Adjust the voice to match what you hear in your head.*

---

# STEP 6 — The Burnsville Cover Test (3-choice menu) (~45 minutes)

This is the big one. The first real player choice in *Survive the 70s* — and it's the **Tier 3 social puzzle** we locked tonight. Mark walks into Burnsville, the Book in his pocket, a couple of mystery parts from Danny's leftover box in his hand. Stan looks up from the counter.

## 6.1 Add a second background

**Save another placeholder image as:**
```
C:\renpy\projects\survive-the-seventies\game\images\burnsville.jpg
```

Suggestion: Google *"vintage electronics shop interior"* — anything cluttered with hand-labeled bins and resistor reels.

**Add to the image declarations block at the top:**

```renpy
image bg burnsville = "images/burnsville.jpg"
```

## 6.2 Add the Burnsville scene

**At the bottom of `script.rpy`, REPLACE the final `return` with this expanded scene:**

```renpy
    # ============================================================
    # SCENE 2 — BURNSVILLE ELECTRONICS
    # The first Tier 3 cover test
    # ============================================================

    pause 0.5

    # Walk transition
    scene black with fade
    narrator "Mark walks. The neighborhood is louder than 2026. Lawnmowers. Kids on bikes. A radio in a window playing something with too much horn section."

    narrator "Burnsville Electronics. The bell over the door is real."

    scene bg burnsville with fade

    stan "Danny! Wasn't expecting you back so soon, kiddo. Thought you were all set after last week."

    mark "(Stan knows me. Of course Stan knows me. Stan probably knows everything Danny was working on.)"

    mark "(He doesn't, though. He can't. Danny said Stan won't ask why.)"

    mark "(He's looking at me. I need to say something.)"

    pause 0.5

    menu:
        mark "What do I say?"

        "Bluff it. \"Hey Stan — just need to double-check a few parts.\"":
            jump burnsville_bluff

        "Be honest-ish. \"Honestly? I got it all home and now I can't remember what half of these are. My handwriting is terrible.\"":
            jump burnsville_honest

        "Deflect. \"Just browsing. Mom sent me to get out of the house.\"":
            jump burnsville_deflect


label burnsville_bluff:

    mark "Hey Stan — just need to double-check a few parts."

    stan "...okay."

    stan "Show me what you got."

    mark "(He's still smiling. But his eyes did a thing.)"

    stan "Spread 'em on the counter, kiddo. Let's see."

    # Cover took a small ding but the scene continues
    jump burnsville_counter


label burnsville_honest:

    mark "Honestly? I got it all home and now I can't remember what half of these are. My handwriting is terrible."

    # Steve interrupts from the back of the shop
    steve "Pop! You gonna retire today or tomorrow?"

    stan "I'll retire when I'm damn ready!"

    # Stan turns back to Mark, laughing
    stan "You and every kid who ever built anything, Danny. Show me what you got."

    mark "(He bought it. He more than bought it — he LIKED it.)"

    mark "(Rule 7. Honest humility. Danny told me. Stan told me. The game told me.)"

    pause 0.3

    # Era-teaching beat — the Family Business reveal
    mark "(Wait. That guy in the back called him 'Pop.')"

    mark "(That's his son. The son OWNS this place. Stan used to own it and gave it to his son. They both work here. They tease each other about retirement.)"

    mark "(I'm in a shop owned by a family.)"

    mark "(In 2027 this would be a Best Buy with a guy in a blue shirt who'd never met the manager.)"

    mark "(...the future sucks.)"

    jump burnsville_counter


label burnsville_deflect:

    mark "Just browsing. Mom sent me to get out of the house."

    stan "...your mom sent you to an electronics shop to get out of the house."

    stan "Sure she did, Danny."

    stan "(Stan goes back to whatever he was doing. The window for help just closed.)"

    mark "(I should have said something else.)"

    # Bad outcome — cover is intact but the help didn't happen
    jump burnsville_exit_failed


label burnsville_counter:

    pause 0.5

    narrator "Mark spreads the mystery parts on the counter. Stan picks one up. Turns it over."

    stan "This one's a resistor. 4.7K. Color bands — yellow, violet, red."

    stan "This one's a capacitor. Ceramic disc. Cheap, common, you've got six of these."

    stan "This one... huh."

    pause 0.5

    stan "I don't know this one."

    mark "(...oh.)"

    stan "It's old. Pre-war old, maybe. You said your old man gave you a box?"

    mark "Yeah. Said it was just junk."

    stan "It's not junk."

    stan "Take it to the library, kiddo. Ask for the technical reference shelf. There's a binder — Allied Electronics catalog reprints, goes back to the forties. If it's in there, you'll find it."

    mark "(There's another quest now. The library. Allied Electronics catalogs. Got it.)"

    stan "Bring it back when you know what it is. I'll tell you what to do with it."

    mark "Thanks, Stan."

    stan "Don't thank me. Go figure it out."

    jump burnsville_exit_success


label burnsville_exit_failed:

    pause 0.3
    scene black with fade
    narrator "Mark walks home. The mystery part is still in his pocket. So is the question."
    narrator "First night ends here. Try again."
    return


label burnsville_exit_success:

    pause 0.3
    scene black with fade
    narrator "Mark walks home. The mystery part is still in his pocket. So is a name: Allied Electronics."
    narrator "First night ends here."
    narrator "Tomorrow: the library."
    return
```

**Save. Run it.**

**You should see:**
- The full intro scene (Mark wakes up, reads Danny's book)
- A walk transition to Burnsville
- Stan greets "Danny"
- A 3-choice menu appears
- Each choice routes to a different short scene
- The Honest-ish path triggers Steve's "Pop, you gonna retire today or tomorrow?" callback — the moment we locked tonight
- All three paths reach an ending screen

**CHECKPOINT 6:** Survive the 70s has a playable scene. With a real choice. With Stan Burns in it.

---

# What you just built

In one evening you went from zero to:

- ✅ Ren'Py installed and configured
- ✅ A real project with a real `script.rpy`
- ✅ Two scenes (bedroom + Burnsville)
- ✅ Five characters (Mark, Danny, Stan, Steve, narrator)
- ✅ A real player choice with branching consequences
- ✅ The Stan/Steve banter beat — the warmest recurring moment in the game — **already running on your screen**
- ✅ A teaching scene for **Rule 7** (Honest Humility) — the player who picks "Honest-ish" gets the good outcome, and the dialog explicitly tells them why

**This is not a vertical slice yet. It's not even a demo. But it's a thing that RUNS. And it's the only thing that mattered tonight.**

---

# What's next (NOT tonight)

The natural next builds, in rough order:

1. **Music + sound** — even just one ambient track + a UI click sound. Massive perceived-quality bump for ~30 min of work.
2. **A character sprite for Stan** — even a placeholder photo with the background removed. Adds a face to the voice.
3. **The "Book" as a visual element** — when Danny "speaks," show a notebook page overlay instead of his italic dialog box.
4. **Day system scaffolding** — the streetlight transition, the bedroom sanctuary loop.
5. **More scenes from `component-L-soldering-iron.md` v0.2** — but that doc needs a body rewrite first to match the v0.2 framing.

**But not tonight.** Tonight you have the milestone. Sleep on it.

---

# Common problems (Windows-specific)

| Problem | Fix |
|---|---|
| "Ren'Py couldn't find images/bedroom.jpg" | Check the path. Filename is case-sensitive. Make sure it's `.jpg` not `.jpeg`. |
| Indentation error / "expected an indented block" | Ren'Py uses 4 spaces, not tabs. VS Code → bottom-right → "Spaces: 4". |
| Window opens then immediately closes | There's probably an error — Ren'Py launcher shows the traceback. Paste it to me. |
| Can't find `script.rpy` | It's in `C:\renpy\projects\survive-the-seventies\game\` — note the `game\` subfolder. |
| Background image looks weird (stretched / tiny) | Ren'Py auto-scales — try a 1920x1080 source image. |
| Want to skip to a specific scene to test | Add `default config.developer = True` near the top — then Shift+D in the running game opens a developer menu that lets you jump labels. |

---

# When you hit something I didn't cover

**Paste the error to me.** Or describe what you're seeing on screen vs. what you expected. We'll fix it together.

Welcome to Ren'Py. 🎮
