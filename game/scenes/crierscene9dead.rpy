label crierscene9dead: 

    """

    Nat has not stopped performing his duties. He makes his way to the town hall every morning, memorises what the Alderman tells him he has to say, and then he walks through the streets, shouting it out.

    In the times he is not crieing, he hides in the belltower.

    The bells, as far as you know, continue to ring every hour, on the hour.

    This is all he does.

    You see him in the town square now. He has stopped walking, his head twisted uncomfortably, looking down and behind him.

    You do not remember if it was the exact spot where [game.creature_name] died. But you know he does.

    He stares as if it had caught him by surprise mid stride.
    """

    menu:

        "Hi Nat!":
            $game.crier.like -= 2
            $game.crier.att -= 2
            $c=3

        "I'm so sorry Nat.":
            $c=3

        "*Approach, but say nothing*.":
            $c=2

        "*Leave him be*.":
            $c=1



if c==1:

    """

    Eventually Nat moves, his head swivelling around first, then the rest of his body uncoiling.

    His eyes meet yours.

    He stares at your face, his own unchanged as if he is still seeing the bloodstain in his mind.

    And then he's walking away.

    You will hear his voice tomorrow morning, and the morning after that.

    But you know, as you watch his frail form disappear round a corner, that Nat will never speak to you again.
    """

    $game.crier.resp += 1



if c==2:

    """

    As you approach Nat spins around, like a dear who just heard a twig snap.

    He holds his crouch for a moment, his eyes wide, before slowly straightening himself up.

    His face returns to what it was a moment ago, the exact same expression.

    Looking at you like he can still see the bloodstain.

    You see the muscles of his throat work, but he does not say anything.

    He simply gives a small shake of his head.

    You will hear his voice tomorrow morning, and the morning after that.

    But Nat will never speak to you again.
    """

    $game.crier.like += 1



if c==3:

    """

    Nat turns to you, slowly.

    You are afraid, for a moment, that he is about to hit you.

    But he doesn't. Slowly his hands unclench and his face becomes neutral, unreadable.

    The only part of him that seems to move is his throat, the muscles bulging as if a hundred words are trying to fight their way out of his mouth.

    Eventually, he simply manages:
    """

    crier "No."

    """

    True, you will hear his voice tomorrow morning, and the morning after that.

    But 'no' is the last word he ever gives just to you.
    """

    $game.crier.resp -= 2
    $game.crier.att -= 2
    $game.crier.like -= 2


return
