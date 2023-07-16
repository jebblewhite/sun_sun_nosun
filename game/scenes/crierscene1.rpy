label crierscene1:

"""

You approach Nat, who is perched on the edge of the fountain in the town square, smiling at a couple of moths playing with each other in a small patch of grass and weeds that lies mostly hidden and forgotten in the corner between two cracked stones.

He looks up as you approach, hearing your footsteps from quite some way away, and smiles.
"""

crier  "Afternoon [game.player_name], heard the Alderman gave you some responsibilities.  I've been doing responsibilities for him for years now, so if you need any help, just ask me, although I will say I've not got much of a mind for all that technical numbers stuff."

menu:

    "I don't believe you, you must be good with numbers to keep the time":
        $c=-1

    "Don't worry, I've had practice at the number stuff.  But thanks" if game.playerbackground == "merchant":
        $game.crier.resp += 1
        $c=-2

    "Thanks, that's kind of you, but I'll be okay" if game.playerbackground != "merchant":
        $c=-2

    "I don't need your help":
        $game.crier.like -= 4
        $c=-2


if c==-1:

    crier  """

    Ah that's very kind of you [game.player_name], but it's really not the same.  I remember when I was young, they always used to call it learning your numbers and learning your letters, but it wasn't ever really like that.

    Did you get that?  As far as I see, learning your letters isn't really about learning letters at all.  I mean maybe a bit, so early on none of us can remember it, but you learn pretty fast your 'a's from your 'b's and such.

    No, it's about what you do with the letters, see?  Words and sentences and grammar and all that.  And it's the same with numbers.  Only I never really understood it.

    If it had just been learning the numbers, then I could have been the best in the village, and I don't like to speak immodest but it's true and I swear it.

    But I never really learnt what to do with them beyond which one comes after which other one.  And that other stuff's what they really mean when they say learn your numbers, or when I say I can't do the number stuff.

    Anyway, you didn't want to hear me ramble.  What was it you wanted?
    """

    $game.crier.like += 4
    menu:
        "No, I'm interested in you and your counting.":
            $c=4

        "I just came over to talk, about whatever you want to talk about.":
            $c=7


if c==-2:

    crier "Oh, well that's all all right then.  Say, I saw you walking over here but I didn't let you say what you wanted."

    menu:
        
        "I just thought I'd come over for a chat":
            $c=-3



if c==-3:

    crier "Well then, what is it you wanted to chat about?"

    menu:

        "I don't know, what do you want to chat about?":
            $c=7

        "I wanted to ask you how you're so good at keeping the time":
            $c=4



if c==7:

    crier """

    Oh you did?  Oh that's very sweet of you.  Most people want to just ask for the news, or ask about my time-keeping.  I'm not accustomed to people asking me what I want to talk about.
    """

    "Nat sits in silence for a moment, staring across the square."

    crier  "You see, the thing is, all I can think about right at this moment is the count.  Those people leaving recently has kind of thrown me.  So actually I think that's what I want to talk about, nice and familiar.  Have I told you about it?"

    $game.crier.att += 4
    $game.crier.like += 4

    $c=4



if c==4:
    crier """

    I've got a gift, see?  Got it a few years back when I went over to Gritilz.

    They've got one of them mechanical clocks there. Watched it for hours, got the rhythm stuck in my head, which I reckon isn't too hard, but I didn't have to think about the count of them. 

    But more than that, more than just keeping the rhythm, I count them.  Easy when you put sixty into sixty and sixty into sixty into twenty-four.  Keeps it all neat and the tick's always just about right.  And more, I can do it when I dream as well, so I don't lose the time when I sleep.

    Was staying there for a week, down in Gritilz, and at the end of that time I went back to that clock and what do you know?  Only seven seconds out!  Now I think that's quite impressive, if I do say so myself, but maybe you haven't seen these clocks and can't say how precise they are.
    
    """
    menu:
        "That all sounds very impressive Nat. I don't think I could even keep the right rhythm.":
            $c=5
                        
            crier """

            Well that's very kind of you to say.  The Alderman says that I'm a fine crier and most of the people are nice to me, hopefully even more so now that that Edward is gone, but I think that my only real talent is the time thing.

            It's not necessarily what I would have chosen, but I'm lucky to have it.  Some folk have nothing you know.  Always got to remember them.

            Anyway, I'm terribly sorry [game.player_name], but I've got to go.  Coming up for the next ring now and I always take forever to climb the steps in the bell-tower.  Not that there's something hard about them, mind, I just don't like the height so I keep having to close my eyes.

            It was very nice of you to come and chat.

            """
            $game.crier.att += 4
            $game.crier.like += 4

        "I could keep the rhythm, but I have better things to do than count up all those seconds.":
            $c=6
            crier """

            Is that right?  Well I won't challenge you on it.  Would be rude.  Also there's no clock to measure us by here, and I don't want to leave and go back to Gritilz.  

            Still, probably best that I keep keeping the time.  You do have your other important things to do, don't you, like you said.

            Anyway, I'm terribly sorry [game.player_name], but I've got to go.  Coming up for the next ring now and I always take forever to climb the steps in the church.  Not that there's something hard about them, mind, I just don't like the height so I keep having to close my eyes.

            It was very nice of you to chat with me though.

            """

            $game.crier.like -= 2
            $game.crier.resp += 1

return
