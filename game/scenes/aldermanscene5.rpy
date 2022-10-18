label aldermanscene5: 


"""

The argument, which you could tell was heated from the muffled sound of their voices from the other side of the door, abruptly stops the moment you walk in.

You are here because the Alderman asked you to be here.  Or rather, the Alderman sent Nat to ask you to be here.  The Alderman's message had few details, but a quick questioning of Nat, who seemed more anxious than usual, revealed that the problem was probably related to Alina.

And now you're here in the Alderman's office, a still clearly ill Alina managing to convey a great deal with her expertly neutral expression, while the Alderman straightens from his cowed hunch as the door closes behind you.
"""

alderman  """

Ah, [game.player_name], I'm very glad you could join us.

I hope you don't mind Officer?
"""

alina  "Not at all Alexi.  You may have your second."

"The look that passes between the two lets you know that both accept that Alina just scored a point."

if game.aldermanplan == "Love":
    $ textinsert = "if we all care for each other, we'll all make it through this,"
elif game.aldermanplan == "Cunning":
    $ textinsert = "if we act sensibly and remind everyone that mutual aid is in their own best interest, we'll make it through this,"
elif game.aldermanplan == "Pride":
    $ textinsert = "if we all just remember our duty to the town, and our pride in it, we will all make it through this,"

alderman  "Very good.  Now, [game.player_name], Officer Alina and I were just discussing some practical matters.  While I am of the opinion that [textinsert] Officer Alina believes that the only way for Lotosk to survive is to, ahem, let the weak die."

"The Alderman turns confrontationally towards Alina, who does not even blink."

$textinsert2 = game.aldermanplan.lower()


alina  """

I said 'let the strong survive', but you aren't wrong {i}there{/i} Alexi.

Where you are wrong is thinking that [textinsert2] alone will result in total survival of this town.  Because it won't.  Your policies will kill everyone here.
"""
"The Alderman looks at you imploringly."
menu:

    "Let's hear Alina out":
        $c=4

    "Alina, that's a horrible thing to say!":
        $c=3

    "With all due respect Alina, the Alderman knows this town better than you do":
        $c=1

    "Having fewer mouths to feed sounds like a good idea to me":
        $c=2





return
