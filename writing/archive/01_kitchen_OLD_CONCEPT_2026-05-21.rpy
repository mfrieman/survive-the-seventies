## Scene 1 — Kitchen
## The briefing. Mom delivers marching orders, Dad grunts behind the
## paper, you negotiate (or don't) for allowance.
##
## This is the TEMPLATE scene — copy its structure for scenes 2-5.

label kitchen_scene:

    scene bg kitchen with fade

    narrator "The kitchen smelled like burned toast and my father's cigarette."
    narrator "Harvest gold appliances, a linoleum floor going up at the corners, and a transistor radio on the windowsill playing something by Driftwood Jack."

    mom "There he is. The man of the hour."
    narrator "She said this every Saturday. I was 14. I was not the man of any hour."

    mom "Out. Be home when the streetlights come on. And not one minute after."
    dad "Mhm."

    # ----- allowance negotiation -----
    kid_v "Mom — could I get a couple bucks for the day?"

    menu:
        "\"Could I please have an extra dollar?\" (polite)":
            $ result = kid.opposed_check("common_sense", "dumb_kid_bravery", base=40)
            jump allowance_polite

        "\"You said you'd give me five last week.\" (push)":
            $ result = kid.opposed_check("dumb_kid_bravery", "common_sense", base=50)
            jump allowance_push

        "\"Never mind.\" (eat it)":
            $ kid.cash = 1
            narrator "I took the dollar she'd already put on the counter. The narrator in my head — that's me, now — winced at the version of me that didn't push."
            jump kitchen_leave

label allowance_polite:
    if result == "crit":
        mom "Oh — fine. Here. Three dollars. Don't tell your father."
        $ kid.cash = 3
        $ kid.adjust(moms_patience=+5, cool=+2)
        narrator "Three dollars. In 1979. I felt like a Rockefeller."
    elif result == "pass":
        mom "Two dollars. That's it. And I want a quarter back."
        $ kid.cash = 2
        $ kid.adjust(cool=+1)
        narrator "Two dollars. Adequate."
    else:
        mom "I gave you a dollar last week. Did you bury it?"
        $ kid.cash = 1
        $ kid.adjust(moms_patience=-2)
        narrator "I had not buried it. I had spent it on Cracklin' Stones and a comic. Both excellent investments."
    jump kitchen_leave

label allowance_push:
    if result == "crit":
        mom "I... fine. Here's five. But don't make a habit of it."
        $ kid.cash = 5
        $ kid.adjust(cool=+5, moms_patience=-2)
        narrator "Tommy was going to lose his mind when I told him."
    elif result == "pass":
        mom "I said two. Two."
        $ kid.cash = 2
        $ kid.adjust(moms_patience=-3)
    else:
        dad "Hey."
        narrator "Dad lowered the paper. This was bad."
        dad "Don't talk to your mother like that."
        mom "Here. One dollar. Now scoot."
        $ kid.cash = 1
        $ kid.adjust(moms_patience=-8, cool=-2)
        narrator "Dad's eyes were the color of a Sunday morning. I scooted."
    jump kitchen_leave

label kitchen_leave:
    mom "Streetlights! I'm not yelling for you twice!"

    # Inner voices weigh in on the day ahead
    brave "We're gonna jump the creek today. We're gonna BE somebody."
    common_sense "We are gonna be in the emergency room today, is what we are gonna be."

    narrator "I let the screen door slap shut behind me — louder than necessary, the way 14-year-olds slam doors on principle."

    # End of scene 1. Scene 2 (garage) doesn't exist yet — placeholder ending.
    scene bg black with fade
    centered "{i}— end of concept demo, scene 1 —{/i}\n\n{size=-4}stats this run:{/size}\n\nbones [kid.bones]   patience [kid.moms_patience]   cool [kid.cool]   cash $[kid.cash]"

    return
