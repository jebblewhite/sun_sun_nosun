label butcherscene1: 

"Mik is exactly where you expect to find them: in their butcher's shop.  They're at the counter, a rare occurrence as they usually spend most of their time in the back, and they look up lazily from the knife they were polishing as the bell above the door announces your entry."

butcher "Well hello there [game.player_name].  What's made you stumble into my web today?"

menu:
    "Excuse me?":
        $c=1
        "Mik smiles."

        butcher """

        You heard me.  """#Wink here

        butcher """

        You're a person of influence now [game.player_name].  And that means I've got some things to say to you, whether you want to hear them or not.

        I'd say pull up a chair, but this is a butcher's shop so why would I have a chair?
        """

        $c=4


    "I just wanted to chat.":
        $c=2

    "Wanted to make sure that the business is running fine.  We need you to deal with all the animals the hunters bring back.":
        $c=3

label butcherscene1end:
return
