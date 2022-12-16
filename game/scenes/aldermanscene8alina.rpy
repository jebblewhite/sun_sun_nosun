label aldermanscene8alina:


"""

At first you think that it is Elena at your door, the knocking is demanding and imperious, but when you open it you find Alina standing on the other side.

She starts speaking before you even have the chance to open your mouth.
"""

alina  """

I have thought much, but I think that the best plan is a simple one.

Your Alderman clearly wants to make a show out of being removed from office.  He wants his people to see him being physically dragged out of the building.

I fear there is no way for us to deny him that.

But the man is old, and I can tell just by looking at him, not particularly strong.  One fit individual should be all it takes to strong-arm him out of the Town Hall.

You will be that individual, [game.player_name].  We will not give him the show of force that he wants from us, we shall simply walk in there and you will simply walk him out.

Now that it is decided, there is no reason to delay.

Follow me [game.player_name].
"""
menu:
    "*Follow Alina*":
        $c=1


label reevaluatealderman8alina:
if c==1:

    """

    Alina walks ahead of you for the short distance to the Town Hall, the tightly rolled senate writ held in her steady hand like a sword.

    Unlike her last coup attempt, she has not chosen the busiest time for her move.  Still, those few people who are milling around the town square instantly move to gather a little distance behind you, making no attempts to hide their curiosity and excitement.

    Little hushed arguments about who should run the town are instantly shushed out of existence as Alina leans in close to you, whispering:
    """

    alina  """

    I will call him out and present him the writ.  Then you will simply and calmly remove him from the building.

    If any of this crowd try to make any problems for you, ignore them if you can and deal with them in the same manner if you cannot.

    I am still weak from my journey, so do not count on me to help you if there is a physical confrontation.
    """

    """

    Then, nodding with an energy clearly manufactured for the crowd, Alina pushes open the doors of the Town Hall.

    The entrance hall was built, you notice for the first time in your life, with amusing proportions.  Clearly the architect had had grand ambitions, but did not have the budget to match.  Someone had been forced to make the decision between a large foyer or a grand staircase.

    Whoever it was, they had clearly chosen the staircase.

    The Alderman, clearly alerted to your coming by the gathering crowd, stands at the top, a stooped, small shadow in the darkness of the room.
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

    menu:
        "*Precede Alina up the stairs*":
            $c=2

        "*Follow Alina up the stairs*":
            $c=3



if c==2:
    if game.playerbackground == "merchant" or game.playerbackground == "deserter":
        $textinsert = "She is trying to avoid a show of strength, after all."
    else:
        $textinsert = ""
    "You begin to move in front of Alina, but a tactical tap on the shoulder shows you that she does not feel that that would be a good idea.  [textinsert]"
    menu:
        "*Nod and follow Alina up the stairs*":
            $c=3


if c==3:

    """

    Alina places one foot on the old wooden stairs, and then the next.  

    You follow a few steps behind.

    The crowd waits with hushed anticipation, any political allegiances they may hold momentarily forgotten in the spectacle of the show.
    """

    alina  "The senate writ, Alderman Alexi, just as you re-"

    """

    A creak.

    A snap.

    Alina does not scream on the way down.  You do not know if her face even looked shocked.

    Then another snap.

    Bone this time, rather than wood.

    Tiny fragments of splintered wood fall slowly through the moonlight.

    You feel the structure of the stairs wobble slightly under your weight.

    Then someone screams.  Not from below you, where Alina, or her body, must lie, but from behind you.
    """

    "Man"  "By the gods, what happened!"
    menu:
        "*Stand where you are, rooted to the spot by the shock of watching someone simply disappear through a broken step right in front of you.*":
            $c=4

        "Someone, find where she's fallen and help her!":
            $c=6

        "*Move carefully down the stairs, before anything happens to you*":
            $c=8



if c==4:

    alderman  """

    Someone please do something!

    The stairs, I think the old clerk's rooms are beneath them.  The door on the right, yes yes that one, open that and you should be able to find her.

    Someone else, quickly go and fetch Fyodora.  Tell her how urgent it is!
    """

    """

    The crowd, all political grievances forgotten, break from their trance and spring to action.

    A number of them surge forward, almost fighting to be the first to reach Alina.

    A moment later you hear a worried exclamation stab up from the hole in the stairs just in front of you.

    Again, there is a moment of stillness, half the crowd somewhere beneath you staring with shock at the Senate Outland Officer, the other half already rushing across the town square to Fyodora's clinic.

    Only you and the Alderman are left in the room.

    His nervous pacing, like a dog looking for some way down a steep incline, has stopped.  He's standing still, his hands balled painfully tight in front of him.

    His face is utterly expressionless.

    The door to the hall bursts open.

    The crowd almost pulls Fyodora to the little entrance of the clerk's office.

    The Alderman is pacing again, shouting out instructions and words of encouragement.

    A shout from below, an imperative slicing through everything else.
    """

    doctor  "I need people to help me move this debris.  Quickly now!"

    alderman  "[game.player_name], go help Fyodora."

    #je{Slight respect loss with the Alderman}
    menu:
        "*Go help Fyodora*":
            $c=5


if c==5:

    """

    You move carefully down the stairs and through into the old clerk's office.

    The small room is full, and most of the people in it seem to be very busily doing nothing.

    One person has lit a candle and is holding it up for Fyodora.  Another two are already shifting wood aside.  But all the rest are nervously moving, shifting their feet, rocking, sending their eyes on circuits round the room so they will at least appear as if they are looking for something to do.

    Only one person is completely still.

    Alina is lying face down.  One of her legs has smashed through the flimsy wooden desk.  The flesh below the knee is ripped and mangled, large shards of wood having scraped their way across her skin, some of them embedding themselves in her muscles.

    Her other leg lies twisted under her torso, the sole of her foot almost touching the side of her head.  Her arms may be bruised and some ribs may be broken, but from where you stand there is no clear sign of serious injury there.

    Her head rests in a pool of blood.

    Fyodora gives you a quick look and gestures with two fingers which parts of the debris you should be helping to move.  You get to it, hauling bloody pieces of wood away and clearing a space that Fyodora can use to safely examine, and then extract, Alina.
    """

    doctor  "She's alive, but unstable."

    alderman  "Thank the gods for that.  Can you save her?"

    """

    The Alderman's clearly relieved voice sounds soft through the new hole in the ceiling of the under-stairs room.

    Fyodora lets him, and the anxious crowd, know that she thinks she can.

    The work seems to go more easily from there, now that someone has taken responsibility.

    It does not take long before Fyodora states that it is safe to move Alina and you and a few others help take the mangled body across the square.

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




if c==6:

    alderman  "Indeed!  The room beneath the stairs, I think it is the old clerk's room.  The door is just there, to the right of the stairs."

    """

    The crowd, all political grievances forgotten, break from their trance and spring to action.

    A number of them surge forward, almost fighting to be the first to reach Alina.

    A moment later you hear a worried exclamation stab up from the hole in the stairs just in front of you.

    Again, there is a moment of stillness, half the crowd somewhere beneath you staring with shock at the Senate Outland Officer, the other half already rushing across the town square to Fyodora's clinic.

    Only you and the Alderman are left in the room.

    His nervous pacing, like a dog looking for some way down a steep incline, has stopped.  He's standing still, his hands balled painfully tight in front of him.

    His face is utterly expressionless.

    The door to the hall bursts open.

    The crowd almost pulls Fyodora to the little entrance of the clerk's office.

    The Alderman is pacing again, shouting out instructions and words of encouragement.

    A shout from below, an imperative slicing through everything else.
    """

    doctor  "I need people to help me move this debris.  Quickly now!"

    #{Respect gain with the Alderman}

    menu:
        "*Go help Fyodora*":
            $c=5




if c==5:

    """

    You move carefully down the stairs and through into the old clerk's office.

    The small room is full, and most of the people in it seem to be very busily doing nothing.

    One person has lit a candle and is holding it up for Fyodora.  Another two are already shifting wood aside.  But all the rest are nervously moving, shifting their feet, rocking, sending their eyes on circuits round the room so they will at least appear as if they are looking for something to do.

    Only one person is completely still.

    Alina is lying face down.  One of her legs has smashed through the flimsy wooden desk.  The flesh below the knee is ripped and mangled, large shards of wood having scraped their way across her skin, some of them embedding themselves in her muscles.

    Her other leg lies twisted under her torso, the sole of her foot almost touching the side of her head.  Her arms may be bruised and some ribs may be broken, but from where you stand there is no clear sign of serious injury there.

    Her head rests in a pool of blood.

    Fyodora gives you a quick look and gestures with two fingers which parts of the debris you should be helping to move.  You get to it, hauling bloody pieces of wood away and clearing a space that Fyodora can use to safely examine, and then extract, Alina.
    """

    doctor  "She's alive, but unstable."

    alderman  "Thank the gods for that.  Can you save her?"

    """

    The Alderman's clearly relieved voice sounds soft through the new hole in the ceiling of the under-stairs room.

    Fyodora lets him, and the anxious crowd, know that she thinks she can.

    The work seems to go more easily from there, now that someone has taken responsibility.

    It does not take long before Fyodora states that it is safe to move Alina and you and a few others help take the mangled body across the square.

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


if c==6:

    alderman  "Indeed!  The room beneath the stairs, I think it is the old clerk's room.  The door is just there, to the right of the stairs."

    """

    The crowd, all political grievances forgotten, break from their trance and spring to action.

    A number of them surge forward, almost fighting to be the first to reach Alina.

    A moment later you hear a worried exclamation stab up from the hole in the stairs just in front of you.

    Again, there is a moment of stillness, half the crowd somewhere beneath you staring with shock at the Senate Outland Officer, the other half already rushing across the town square to Fyodora's clinic.

    Only you and the Alderman are left in the room.

    His nervous pacing, like a dog looking for some way down a steep incline, has stopped.  He's standing still, his hands balled painfully tight in front of him.

    His face is utterly expressionless.

    The door to the hall bursts open.

    The crowd almost pulls Fyodora to the little entrance of the clerk's office.

    The Alderman is pacing again, shouting out instructions and words of encouragement.

    A shout from below, an imperative slicing through everything else.
    """

    doctor  "I need people to help me move this debris.  Quickly now!"

    #{Respect gain with the Alderman}
    menu:
        "*Go help Fyodora*":
            $c=5
            jump reevaluatealderman8alina
    


if c==7:

    "The Alderman has started anxiously pacing back and forth like a dog looking for some way down a steep incline, while you begin carefully picking your way down the stairs."

    alderman  """

    Someone please do something!

    The stairs, I think the old clerk's rooms are beneath them.  The door on the right, yes yes that one, open that and you should be able to find her.

    Someone else, quickly go and fetch Fyodora.  Of course tell her how urgent it is!
    """

    """

    The members of the crowd, all political grievances forgotten, break from their trance and spring into action.

    A number of them surge forward, almost fighting to be the first to reach Alina.

    A moment later you hear a worried exclamation stab up from the hole in the stairs just in front of you.

    The other half of the crowd drains quickly out of the front door, running as if they are fleeing.  Off to fetch Fyodora.

    By the time you have reached the bottom  of the stairs, the room is empty, save for you and the Alderman.

    His nervous pacing has stopped.  He's standing still, his hands balled painfully tight in front of him.

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

    It does not take long until Fyodora states that it is safe to move Alina, and you and a few others help take the mangled body across the square.

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
