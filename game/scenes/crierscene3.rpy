label crierscene3: 

if game.playerbackground == "woodsman":
    $textinsert = ", the sound a trainee hunter makes when they are trying, and failing, to be subtle,"
else:
    $textinsert = ""

"""

It takes you some time to find Nat. You began searching not long after the bells last rung, and had therefore assumed that he would be somewhere near the bell tower, on his usual rounds. It was only after you assumed you had missed him, and checked by the river, that you thought to check the bell tower itself.

The moment you push the old door aside, you know he is there. His voice echoes through the large, cold, damp, and, surprisingly, clean space. He's talking in a little whisper, his words a constant stream, pushed through both the exhales and inhales of his breath.

The door shuts behind you with a loud click and the muttering instantly stops. There is silence for a moment, your eyes adjusting to the darkness tarnished only by a small square of starlight high, high above you.

Then there's a shuffling sound[textinsert] and you hear:
"""

crier """

Ah, it's you. Thought someone might be sneaking up on me, although now that I think, I can't see any reason why any of the folks round here might do that.

Old habits, you know how it goes.

What brings you here anyway [game.player_name]? People don't usually like coming here, except maybe back in the old days when you could see some of the view from up top.
"""

menu:

    "What do you mean by old habits?":
        $c=1

    "Here to check on you. Disappointed to see that you aren't on your rounds.":
        $c=3

    "Just here to see you Nat, see how you are.":
        $c=2











return
