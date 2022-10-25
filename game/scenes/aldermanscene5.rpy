label aldermanscene5: 

$alderman5morepeople = False
$alderman5emotions = False
$alderman5innovators = False
$alderman5unequal = False
$alderman5treaties = False

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

label reevaluatealderman5:

if c==1:
    alina  "With all due respect, knowledge does not equal wisdom."

    #JE{Slight like, respect and attraction increase with the Alderman} #{Very slight respect loss with Alina}

    $c=5

if c==2:
    """

    Alina nods once, thankful for your support.  If she objects to your callous wording, she does not show it.

    The Alderman, on the other hand, does.
    """

    #JE{Like and respect loss with the Alderman}  #{Very slight respect increase with Alina}

    $c=5

if c==3:

    alina  "A mature, and well reasoned argument."

    #JE{Like gain with the Alderman}  #{Slight respect loss with the Alderman}  #{Respect loss with Alina}

    $c=5

if c==4:

    "Alina nods once, thanks for your support."

    #JE{Slight like loss with the Alderman}  #{Slight respect gain with the Alderman}  #{Respect gain with Alina}

    $c=5


if c==5:

#check food against population
if game.food >= 2*game.countAlive():
    $textinsert = "adequately"
else:
    $textinsert = "barely"

alina  """

The fact of the matter is that resources are dwindling.  You may have enough to [textinsert] feed your populace now, but the situation will only get worse.

It's a scientific fact.

The same goes for fuel and pelts and medicine.  Your current distribution philosophy will, sooner or later - and if I were a gambler, which I am not, my money would be on sooner - lead to the death of everyone in this town.

You are living through an unprecedented event and it will take strong, gifted, incentivised innovators to lift you out of it.  But even the greatest thinkers need time, especially for implementation, and you are not giving it to them.

Most of the food you are gathering is meat.  I have checked your records and found that you have enough salt from when this town was considered as a fall-back point during the war to cure most of the meat that you gather.  Instead you cook it fresh and give it away to the ill, the old and the too young to work.

It's dangerous, and if I may Alexi, you know it.  I know you know it because you feel the need to hide your Communism behind a veneer of Republicanism.

[game.player_name], do you know that your Alderman is using you as a piece of propaganda?  I do not know if he is trying to fool his people or just himself, but as far as I can see it, your main role is to legitimise his socialism by pretending that it is all led by a single, free, hard-working, innovative individual.

But it isn't.  What power has Alexi ever actually given you, save the power to represent his non-existent Republican loyalties?  You have, in material terms, and it is a Republican truth that those are the only terms that matter, no more power than any other individual.

No, this town has adopted socialism at the very moment when it needed drastic, ruthless innovation.  If no-one in this town thinks of a way that this endless night can be survived, then every last one of you will die.  Do you disagree?
"""

"""

A quick glance towards the Alderman shows a bent old man, staring at his feet and deeply lost in a mix of thought and sadness.

He clearly isn't about to answer.
"""
menu:
    "But surely the more of us who live, the more people there are to innovate?":
        $c=6

    "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died":
        $c=7

    "Not everyone in town has the same amount of power.  You're forgetting that Alexi has left plenty for himself...":
        $c=8

    "How do you know we aren't innovating?":
        $c=9

    "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treatise there, {i}'The Positive Impacts of Social Cohesion on Rural Economic Development'{/i}" if game.playerbackground == "merchant":
        $c=10

    "What you're saying is economically sound.  This treatise right here, {i}'Incentive, Necessity and Survival: The Ingredients of Innovation'{/i} would agree with you point for point" if game.playerbackground == "merchant":
        $c=11

    "The philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
        $c=12

if c==6:

    alina  """

    My apologies, I focussed too much on innovation.

    I know that it takes a village to raise a child.  The innovator will need skilled and hard-working hunters and craftspeople to keep them alive.  There must be workers as well as thinkers.

    But not everyone in this town is a worker.  Some are too old, some too sick, some too young**.

    It is giving {i}them{/i} the same materials as are given to the required workers to which I object.
    """

    #JE(if law)[, even with your new edicts]
    $alderman5morepeople = True
    #JE{Slight respect increase with the Alderman}  #{Slight respect loss with Alina}

return
