## Survive the 70s -- script.rpy
## Entry point. Renpy always starts at "label start:".
##
## Built 2026-05-24 ("first night" milestone).
## Scenes: Mark wakes up in 1976 -> reads Danny's Book -> walks to Burnsville
## -> first Tier 3 cover test with Stan Burns.
##
## stats.rpy holds the Kid class + dev HUD; we are not wiring stats to scenes yet.

## ---------- Characters ----------

define narrator = Character(None, what_italic=True, what_color="#dddddd")

define mark  = Character("Mark",        color="#9cd0ff")
define danny = Character("Danny",       color="#c89cff", what_italic=True)
define stan  = Character("Stan Burns",  color="#ffcf78")
define steve = Character("Steve Burns", color="#ffa040", what_prefix="(from the back) ")


## ---------- Placeholder backgrounds ----------
## Flat colors so the game runs with zero art. Replace with real images later
## by dropping files into game/images/bg/ and changing these lines to:
##   image bg bedroom    = "images/bg/bedroom.jpg"
##   image bg burnsville = "images/bg/burnsville.jpg"

image bg black      = "#000000"
image bg bedroom    = "#2a2418"
image bg burnsville = "#3a2e1f"


## ---------- Entry point ----------

label start:

    ## ============================================================
    ## SCENE 1 -- BEDROOM. Mark wakes up.
    ## ============================================================

    scene bg black with fade
    pause 0.5

    scene bg bedroom with fade

    narrator "Mark wakes up."

    narrator "Something is very wrong."

    mark "...okay. Okay okay okay."

    mark "This is not my bedroom."

    mark "This is not my century."

    pause 0.5

    mark "There's a notebook on the desk."

    mark "It wasn't here before. I mean -- it was. I think. But I didn't put it here."

    pause 0.3

    mark "(Open it.)"

    pause 0.5

    danny "If you're reading this, the machine worked."

    danny "If you're reading this and the room smells like burning, the machine also caught fire. Sorry."

    danny "I'm Danny. This is my body. You're me now. Sort of."

    danny "Don't panic. Don't tell anyone. Don't try to call your parents -- they don't exist yet. Don't try to use a phone -- you can't, anyway."

    danny "Read everything in this book before you do anything else."

    danny "There's a list of parts. I built the machine once. You're going to build it again."

    danny "Most of what you need is in the box under the desk. Some of it isn't."

    danny "When you have to ask someone about a part you don't recognize -- go to Burnsville Electronics on Loch Raven. Ask for Stan. He won't ask why."

    danny "Don't lie to Stan."

    danny "Trust me."

    pause 0.5

    mark "(Close the book.)"

    pause 0.3

    ## The receipts beat -- physical onboarding cue
    mark "(There's something else in the box. Underneath the parts.)"

    mark "(A handful of receipts. Yellow carbon copies. \"Burnsville Electronics / Loch Raven Rd. / Stan or Steve Burns, Prop.\")"

    mark "(Dates. Months of them. Resistors. Capacitors. A vacuum tube. A length of copper wire.)"

    mark "(Danny went there a lot.)"

    mark "(Danny KNEW these people.)"

    pause 0.3

    mark "Burnsville Electronics. Loch Raven."

    mark "...okay."


    ## ============================================================
    ## SCENE 2 -- BURNSVILLE ELECTRONICS. The first cover test.
    ## ============================================================

    pause 0.5

    scene bg black with fade

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

        "Bluff it. \"Hey Stan -- just need to double-check a few parts.\"":
            jump burnsville_bluff

        "Be honest-ish. \"Honestly? I got it all home and now I can't remember what half of these are. My handwriting is terrible.\"":
            jump burnsville_honest

        "Deflect. \"Just browsing. Mom sent me to get out of the house.\"":
            jump burnsville_deflect


label burnsville_bluff:

    mark "Hey Stan -- just need to double-check a few parts."

    stan "...okay."

    stan "Show me what you got."

    mark "(He's still smiling. But his eyes did a thing.)"

    stan "Spread 'em on the counter, kiddo. Let's see."

    jump burnsville_counter


label burnsville_honest:

    mark "Honestly? I got it all home and now I can't remember what half of these are. My handwriting is terrible."

    steve "Pop! You gonna retire today or tomorrow?"

    stan "I'll retire when I'm damn ready!"

    stan "You and every kid who ever built anything, Danny. Show me what you got."

    mark "(He bought it. He more than bought it -- he LIKED it.)"

    pause 0.3

    ## Era-teaching beat -- the Family Business reveal
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

    narrator "Stan goes back to whatever he was doing. The window for help just closed."

    mark "(I should have said something else.)"

    jump burnsville_exit_failed


label burnsville_counter:

    pause 0.5

    narrator "Mark spreads the mystery parts on the counter. Stan picks one up. Turns it over."

    stan "This one's a resistor. 4.7K. Color bands -- yellow, violet, red."

    stan "This one's a capacitor. Ceramic disc. Cheap, common, you've got six of these."

    stan "This one... huh."

    pause 0.5

    stan "I don't know this one."

    mark "(...oh.)"

    stan "It's old. Pre-war old, maybe. You said your old man gave you a box?"

    mark "Yeah. Said it was just junk."

    stan "It's not junk."

    stan "Take it to the library, kiddo. Ask for the technical reference shelf. There's a binder -- Allied Electronics catalog reprints, goes back to the forties. If it's in there, you'll find it."

    mark "(There's another quest now. The library. Allied Electronics catalogs. Got it.)"

    stan "Bring it back when you know what it is. I'll tell you what to do with it."

    mark "Thanks, Stan."

    stan "Don't thank me. Go figure it out."

    jump burnsville_exit_success


label burnsville_exit_failed:

    pause 0.3
    scene bg black with fade
    narrator "Mark walks home. The mystery part is still in his pocket. So is the question."
    narrator "First night ends here. Try again."
    return


label burnsville_exit_success:

    pause 0.3
    scene bg black with fade
    narrator "Mark walks home. The mystery part is still in his pocket. So is a name: Allied Electronics."
    narrator "First night ends here."
    narrator "Tomorrow: the library."
    return
