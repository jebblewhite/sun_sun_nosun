label aldermanscene8notinvolved:


"""

This time, everyone knew there would be trouble, although no-one knew when.

And no-one knew how much.

It is purely luck, although you do not know whether it is good luck or bad, that you are in the square when Alina marches straight towards the Town Hall, Jacob behind her and her senate writ held in her steady hand like a sword.

The rest of the people who happen to be in the square instinctively move behind her, hungry for drama.
"""
menu:
    "*Go with them.  Whatever happens, you need to see it*":
        $c=1



if c==1:
    """
    The small crowd forms a knot behind the Senate Outlands Officer, the tension of the last confrontation between her and the Alderman bubbling until Alina leans in and whispers in Jacob's ear.

    There is something about that small act, publicly conspiratorial, that immediately grabs the crowd's attention.  You realise, as a group, that you are here to observe, not intervene.  This piece of history has already been choreographed, and you are just the lucky ones who get to watch it live.

    Jacob nods and Alina marches forward, pushing her way into the Town Hall.  You and the rest of the crowd follow behind, jostling through the doors into the surprisingly tight space beyond.

    The entrance hall was built, you notice for the first time in your life, with amusing proportions.  Clearly the architect had had grand ambitions, but did not have the budget to match.  Someone had been forced to make the decision between a large foyer or a grand staircase.

    Whoever it was, they had clearly chosen the staircase.

    The Alderman, clearly alerted to Alina's coming by your gathering crowd, stands at the top, a stooped, small shadow in the darkness of the room.
    """

    alina  """

    As I have said before, Alderman Alexi, by order of, and by the power of, the Senate, I hereby relieve you of your duty as governor of this town.

    You have had the chance to-
    """

    alderman  """

    Show me the writ.

    I wish to see the writ, again, if that is possible, Officer?
    """

    alina  "Of course."
    
    """
    Alina places one foot on the old wooden stairs, and then the next.  

    You and the rest of the crowd wait in hushed anticipation, any political allegiances they hold momentarily forgotten at the spectacle of the show.
    """

    alina  "The senate writ, Alderman Alexi, just as you re-"

    """

    A creak.

    A snap.

    Alina does not scream on the way down.  You do not know if her face even looked shocked.

    Then another snap.

    Bone this time, rather than wood.

    Tiny fragments of splintered wood fall slowly through the moonlight.

    Then someone screams.  Not from ahead of you, from the hole in the stairs beneath which Alina, or her body, must lie, but from beside you.
    """

    "Man"  "By the gods, what happened!"
    menu:
        "*Stand where you are, rooted to the spot by the shock of watching someone simply disappear through a broken step right in front of you.*":
            $c=2

        "Someone, find where she's fallen and help her!":
            $c=3


if c==2:

    "The Alderman has started anxiously pacing back and forth like a dog looking for some way down a steep incline."

    alderman  """

    Someone please do something!

    The stairs, I think the old clerk's rooms are beneath them.  The door on the right, yes yes that one, open that and you should be able to find her.

    Someone else, quickly go and fetch Fyodora.  Tell her how urgent it is!
    """

    """

    The members of the crowd break from their trance and spring into action.

    A number of them surge forward, almost fighting to be the first to reach Alina.

    A moment later you hear a worried exclamation stab up from the hole in the stairs.

    The other half of the crowd drains quickly out of the front door, running as if they are fleeing.  Off to fetch Fyodora.

    You raise your eyes to see that you are alone in the room with the Alderman.

    His nervous pacing has stopped.  He's standing still, his hands balled painfully tight in front of him.
    """

    #{Slight respect loss with the Alderman}

    $c=4


if c==3:

    alderman  "Indeed!  The room beneath the stairs, I think it is the old clerk's room.  The door is just there, to the right of the stairs."

    """

    The members of the crowd break from their trance and spring into action.

    You direct half of them to the Clerk's door, and then rush back to the others, instructing them on what exactly to tell Fyodora.

    It is only after they have left that you realise that you are alone in the room with the Alderman.

    His nervous pacing, like a dog looking for some way down a steep incline, has stopped.  He's standing still, his hands balled painfully tight in front of him.
    """

    #{Slight respect gain with the Alderman}

    $c=4



if c==4:
    """
    You cannot make out his face in the darkness.

    The door to the hall bursts open.

    The crowd sweeps you up as they almost pull Fyodora to the little door to the clerk's office.

    The small room is quickly full, and most of the people in it seem to be very busily doing nothing.

    The only thing that the advanced party seems to have achieved is the lighting of a candle, which one of them immediately holds up for Fyodora.  All the rest are nervously moving, shifting their feet, rocking, sending their eyes on circuits round the room so they will at least appear as if they are looking for something to do.

    Only one person is completely still.

    Alina is lying face down.  One of her legs has smashed through the flimsy wooden desk.  The flesh below the knee is ripped and mangled, large shards of wood having scraped their way across her skin, some of them embedding themselves in her muscles.

    Her other leg lies twisted under her torso, the sole of her foot almost touching the side of her head.  Her arms may be bruised and some ribs may be broken, but from where you stand there is no clear sign of serious injury there.

    Her head rests in a pool of blood.
    """

    doctor  "I need help moving some of this debris aside."
    """
    She gives you a quick look and gestures with two fingers which parts you should be helping to move.  You get to it, hauling bloody pieces of wood away and clearing a space that Fyodora can use to safely examine, and then extract, Alina.
    """

    doctor  "She's alive, but unstable."

    alderman  "Thank the gods for that.  Can you save her?"

    """

    The Alderman's clearly relieved voice sounds soft through the new hole in the ceiling of the under-stairs room.

    Fyodora lets him, and the anxious crowd, know that she thinks she can.

    The work seems to go more easily from there, now that someone has taken responsibility.

    It does not take long until Fyodora states that it is safe to move Alina and you and a few others help take the mangled body across the square.

    Her face is coated in blood, and almost unrecognisable.

    By that time some of the other townspeople have helped the Alderman past the hole and down the stairs.  He joins you in the hospital, says a few words at Alina's bedside and then helps Fyodora usher everyone out.
    """

    alderman  """

    What has happened today is tragic and shocking.  Officer Alina and I disagreed strongly, but I think I speak for all of us when I say that I want desperately for her to pull through.

    But those of us who heard her speak will know that she was passionate about the productivity of this town.  I think I can speak with confidence when I say that she would have hated to think that we would all stand around mourning her accident.

    The best thing we can do for her now is get back to work.  That is what she will want to see when she wakes up.

    So go, now.  I will sit with her and send Nat out with news if anything happens.
    """

    """
    And so the crowd disperses.  However you cannot help but notice that the feeling in the air is that the story has only jut begun.  

    After all, isn't it … odd … that the stairs just happened to collapse at the very moment that Alina was about to depose the Alderman?
    """

return
