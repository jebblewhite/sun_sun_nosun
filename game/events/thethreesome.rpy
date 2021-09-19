# river event
label thethreesome:
image woodssky = im.Scale("woodssky.png", 3072, 1920)
image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)

show woodssky onlayer skyback
show woodsdeepest onlayer farfarback
show woodsdeeper onlayer farback
show woodsdeep onlayer back
"""

You are standing by the river growing more and more frustrated by your lack of success when you hear light footsteps approaching you from your right.

The man is lithe, short and handsome, walking with a casual yet self-assured swagger.  His hair is tousled with an elegance that can only be achieved with a large amount of work and care.  His sharp jawline is picked out by a beard just too long to be stubble and his eyes are dark beneath delicately shaped eyebrows.

His leather shoes are clean, but not shining like an overeager officer's.  He wears an open suit jacket over a brilliantly white, creaseless shirt, the top button undone to reveal a tanned, hairy chest.  

He winks at you as you notice him, inclining his head slightly and holding out his champagne flute in a kind of salute.

When he speaks, he does so with slipping hints of an accent that is both clearly 'put on' and unknown to you, something throaty and with rolling 'R's.
"""

"Stranger in the night"  "Ah, bonjoor my cherry, what brings such a beauty out to this spot on this night?"
menu:

    "Fishing.":
        $c=3
        "Stranger in the night"  """

        Fishing for compliments?  Wee wee, was a joke, no?  But I shall shower you with them nonetheless, you bootiful majestic creature, you sight grander than the finest art in all the world, you owner of a body that just makes certain parts of me all tingly and excited.

        Tell me, my moonlit darling, what must we do to win your heart?
        """
        menu:
            "'We'?":
                $c=7

            "Just leave me alone.":
                $c=4

            "You could get me some fish.":
                $c=6


    "Sorry, who are you?":
        $c=2
        "Stranger in the night"  "Oh, but what a simple question!  Do not ask who I am, ask what I am!  For I am a man, a man in love, a man in love tonight with the bootiful sight he sees before him.  Tell me, my moonlit darling, what must we do to win your heart?"
        menu:
            "'We'?":
                $c=7

            "Just leave me alone.":
                $c=4

            "You could get me some fish.":
                $c=6


    "None of your business.":
        $c=1
        "Stranger in the night"  "Hon hon hon!  I love them when they're feisty!  Tell me, my moonlit darling, what must we do to win your heart?"
        menu:
            "'We'?":    
                $c=7

            "Just leave me alone.": 
                $c=4

            "You could get me some fish.":  
                $c=6
                
if c==4:

    "Stranger in the night"  """

    Oh my cherry!  Oh you hurt me and my friend so!  All we want to do is give you a night you will never forget, no? a night of such passion that you will spend every moment of the rest of your life yearning for our touches!

    But alas, if I really must go, I will force myself to retreat into the night, but I will forever hold the sight of your body in my mind, to remember on the coldest of winter nights to keep my body and soul warm.
    """
    menu:
        "Wait, who is your friend?":
            $c=7

        "Yes, just go.":
            $c=5
            "Stranger in the night"  "Oh, you hurt me so!  Barbs, barbs to my mind and body!  What sagging disappointment I feel.  But I shall do as you wish, my cherry."

            """

            And with that, the man turns slowly and saunters out of view.

            A few minutes pass, and you make your first catch, and soon after you're lost in the fishing, as if the strange fish drought and the visit from the bizarre 'foreigner' had never happened.
            """

            #{Normal fish gain}

            jump threesomeend

if c==6:

    "Stranger in the night"  "If that is the way to your heart, then my heart sings, for we have the key.  Cath, bring this vision of perfection their fish!"

    """

    Nothing happens for several seconds.  And then you see a fish rise to the surface, belly first.  You scoop it up, and by the time you have, another has appeared.  And then another, and another, and another.

    Soon you've got a larger haul than you could possibly have hoped to catch yourself, lying in buckets beside you and all you had to do was pluck their already dead bodies out of the water.  You are about to turn to the man to ask him how he did that when one last thing rises out of the water.
    """

    #{1.5 times normal fish gain}

    $c=8

if c==7:

    "Stranger in the night"  "Ah yes, my perfectly proportioned darling, I have journeyed here with my good friend Cath.  Come and say bonjoor!"

    "Nothing happens for a moment, and then the sound of moving water makes you turn back towards the river."

    $c=8

if c==8:

    """

    Out of the water emerges something round, grey and slimy.  It looks soft, like a fat, scaleless fish, or a perfectly smooth, wet, human scrotum.

    Suddenly, two mounds, each about a foot in diameter, push themselves out of the semicircular mass, and skin smoothly slides aside to reveal two massive eyes, each one mostly a dark, slightly quivering pupil.

    The creature, which resembles a small hill with huge puppy's eyes, stares at you for a moment, and then winks.

    Something slithers through the water about a foot away from the mass, something long and thin and covered in suckers.

    A moment later and you notice more of these tentacles moving frantically through the water to propel 'Cath' surprisingly quickly towards the shore.

    The tentacles are elegant: strong and flexible, the bottom of each covered in hundreds of dextrous suckers, some as large as your open mouth, some smaller than the tip of your pinky finger.
    """

    "Stranger in the night"  """

    Cath is even more experienced in the arts of love than I am, and trust me my supple young lover, I am very experienced.

    So, my cherry, shall we follow the cliches of our medium?  Shall we dance naked beneath the moon with no thoughts but each other's bodies?  I promise you, Cath and I will show you pleasures you could never imagine.
    """
    menu:
        "Yes, I want this.":
            $c=10
            """

            As you lie naked and alone by the side of the river, you find it difficult to remember what happened when, or with whom, or where.  You expect your body to ache, but the slight coating of slime that Cath produced on...her?..tentacles made certain things surprisingly smooth and…

            Maybe it is best to leave certain things as memories.  As you gather up your scattered and discarded clothes, dress and begin the walk back to town, you muse that at least one of the things the stranger said was undeniably true.  You will never feel that kind of pleasure again.  It will take more thinking, however, to decide whether that is a bad thing…
            """

            #{No reward}

        "No.  Just no.":
            $c=9
            "You hear a little...whimper from the creature in the river."

            "Stranger in the night"  "Oh, you hurt me so!  Barbs, barbs to my mind and body!  What sagging disappointment I feel.  But I shall do as you wish, my cherry."

            """

            And with that, the man turns slowly and saunters out of view.  You hear a little 'harrumph' sound from the river, but by the time you turn to look, Cath has already gone.

            You turn your attention back to fishing, but no matter what you do, you can't catch a single fish, although you are almost sure that you do see a few under the water, before something long and flexible wraps around them and yanks them away from your lines and nets.
            """

            #{No reward}

            









label threesomeend:
$ game.riverevents['thethreesome'] = False # temporary
hide woodssky onlayer skyback
hide woodsdeepest onlayer farfarback
hide woodsdeeper onlayer farback
hide woodsdeep onlayer back
return
