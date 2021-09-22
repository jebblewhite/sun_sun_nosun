#river event
label theleviathan:
image woodssky = im.Scale("woodssky.png", 3072, 1920)
image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)

show woodssky onlayer skyback
show woodsdeepest onlayer farfarback
show woodsdeeper onlayer farback
show woodsdeep onlayer back

if game.playerbackground == "woodsman":
    $ textinsert = "From your experience with terrestrial animals, you would say that it is hunting.  Maybe that is why it has made its way up from the ocean?"
    $ textinsert2 = ""
elif game.playerbackground == "merchant":
    $ textinsert = ""
    $ textinsert2 = "You feel you have heard tell of these things, that in generations past the villagers would find a fish so large that they could eat for weeks.  So impressive was the kill that they would host a festival in honour of the hunters who brought it down."
elif game.playerbackground == "marked":
    $ textinsert = ""
    $ textinsert2 = "One thing you can say, however, is that the appearance of this thing is not like the other strange events that have occurred since the night began.  This is a thing of the world of the light.  You can feel it.  A beast this may be, but it is a mundane one."
else:
    $ textinsert = ""
    $ textinsert2 = ""

python:
    def textIn(insert, background):
        condition = False
        if game.playerbackground == background:
            condition = True
        
        return insert*condition

"""

You will never know how it got there.  It cannot have come from upstream, but why would it have come up from the ocean?

Well, regardless of its provenance, it is here now, a shape so large that it is simultaneously unmissable, as a huge black shadow in the water, and indescribable as, from any angle from which you can view it, you do not get a wide enough view to see all of its mass at once.

This moment it simply looks like a giant fish, oblong with blank dumb eyes, but now that little shiver of scales, caught by the light of the stars, looks like a neck, long and thin.  There, a talon, or is it the edge of a gill?  And how can it look like both of those things at once?

And why is it moving that way?  Quick movements back and forth, slowly turning in an eddy before shooting forward, twisting wildly. [textinsert]

[textinsert2]

Still, the question remains: what are you going to do about it?
"""
menu:
        
    "*Leave it be*":
        $c=1
        """

        The question then is, if you are deciding to let the creature do...whatever it is that it's doing, are you going to attempt to fish yourself, or accept this as a wasted trip?
        """
        menu:
            "Attempt to fish.":
                $c=3
                """

                You attempt to fish, although most of your attention is fixed on the giant just a matter of meters away from you.

                The distraction matters little, however, for while it does not seem at all bothered by your presence, it is having some effect on the other fish in the river, and your catch is significantly lower than you would normally have expected it to be.  You don't return to the village empty-handed, but you are not far off it.
                """

                #{Receive 1/6 expected fish catch}  
                $LeviathanAteFull = True


            "Just leave.  Best to keep as far away from this thing as possible.":
                $c=2
                "You leave the splashing, raging thing and return to town."

                $LeviathanAteFull = True
                #{All but one action refunded}
                jump leviathanend


    "*Find a spear and hunt it*":
        $c=8

    "*Run back to town to get help*":
        $c=4
        """

        You dash back to town, determined to find someone who can help you deal with the...thing.  You go straight to the inn, the most likely place to find people, but when you arrive you only find Joan's tea group and quickly learn that most of the younger citizens of the town are out hunting.

        You do, however, also learn that these fish are not unheard of.  In fact many of the people you hurriedly speak to remember some being caught when they were young.  There is a lot of good meat on them, they say, catching one would be a massive boon to the town right now.

        But how to catch it?
        """
        menu:
            "Go back and tackle it on your own.":
                $c=7
                """
                Deciding that there is no time to waste, and that you cannot risk the lives of the town's elders, you rush back to deal with the beast yourself and are pleased to see that it is still where you left it.
                """
                $c=8

            "Gather some of the older villagers and persuade them to help you.":
                $c=5
                if game.playerbackground == "marked" or game.playerbackground == "merchant":
                    $ textinsert = "You fear that if you had been on your own, it might have overpowered you."
                else:
                    $ textinsert = ""
                """

                You round up some of those attending Joan's tea meeting and hurry them back to the river, finding the creature more or less where you left it.

                You arrange your posse on the side of the bank, making sure that each of them is equipped with a spear or net.  You have already discussed a plan of action with them on the walk down here, and you are all soon ready.

                On your mark you dive, while the others clumsily wade, into the water.  The beast is huge and the water quickly turns dark red with blood and gore as you, and presumably the others, although the beast is so big it mostly obscures your view of your fellow hunters, thrust your spears into it.  

                It flails wildly, incredibly strong but also stupid, not coordinated enough to either attempt to flee or fight back.  [textinsert]

                You feel the beast make a particularly violent movement and you hear a scream from the other side of its bulk.  Pinned by the water and its mass, you have no option but to command the nets be thrown in the hope that the fish can be dragged aside in time for you to make it across and help with whatever has happened.

                But you are too late.  As the carcass, ripped and bloodied to the point where any guesses as to what it looked like when it was whole would be pointless, is pulled ashore, you see Danil, the retired miller, being propped up against a rock on the opposite shore by his brother in law.  

                You rush over, but it is clear long before you get there that the man is dead.  Drowned, although whether by the blood that filled his lungs when the beast crushed his ribs and sent splinters of bone spiralling through his upper torso, or just by river water, you do not know.

                The mood is dark as a cart is brought to take the carcass back to town.  These catches used to be causes of town-wide celebrations.  This one will not be.  But at least everyone still alive will eat.
                """

                #{Gain, as Angus says, a fuck load of food}  #{Lose 1 elderly citizen}

                jump leviathanend


            "Wait for the hunters to return.":
                $c=6
                if game.playerbackground == "marked" or game.playerbackground == "merchant":
                    $ textinsert = "You fear that if you had been on your own, it might have overpowered you."
                else:
                    $ textinsert = ""
                """

                You wait at the bar for the hunters to return, making idle chat with Henryk if you want, or simply tapping your foot against the leg of your bar stool if you don't.

                After what feels like an age the hunters return, ready to drink and relax after their hunt.  You have no intention of letting them fulfil that dream.  You jump up and immediately tell them, in a voice loud enough to cut across their post-hunt banter, about the beast.  

                Immediately they are excited, eager to kill this living myth, so you set off quickly down to the river, finding the beast almost exactly where you left it, although it seems to be moving more slowly now, more lethargically.

                You arrange your posse on the side of the bank, making sure that each of them is equipped with a spear or net.  You have already discussed a plan of action with them on the walk down here, and you are all soon ready.

                On your mark you all dive into the water.  The beast is huge, and the water quickly turns dark red with blood and gore as you and presumably the others, although the beast is so big it mostly obscures your view of your fellow hunters, thrust your spears into it.  

                It flails wildly, incredibly strong but also stupid, not coordinated enough to either attempt to flee or fight back.  [textinsert]

                Eventually you order for the nets to be thrown, and soon the carcass, ripped and bloodied to the point where any guesses as to what it looked like when it was whole would be pointless, is pulled ashore.

                You are tired, bruised and wet, but you cannot help but join in the jubilation of your equally battered fellows as a cart is called and the kill is paraded through town, people peering out of doors and windows to see what all the noise is about.

                Someone finds a guitar, and then someone else a fiddle, and soon half of Lotosk is gathered around the central fire while Mik prepares the meat, stripping out large, thick bones and throwing them, disgustedly, to a small pack of dogs.

                You will eat well for many days, but such thoughts are far from everyone's minds for the moment.  You are all too busy celebrating, feeling a communal love that you have not felt much, if at all, since the sun went down.
                """
                #{Morale boost}  #{A fuck ton of food}  #{Set $LeviathanAteSome = True}  #{Lose an additional action (if one is available)}

                jump leviathanend

if c==8:

    """
    You lay out a number of nets on the bank and then, taking a deep breath, pick up a strong spear and dive into the water.

    The beast seems to ignore your presence until you are right by it, its mass so huge that your world becomes nothing but the beast and the water, water which it splashes towards you in a blind, desperate attempt to keep you at bay.

    You stab your spear into it and almost get pulled off your feet as the creature writhes away from you.  You pull out and stab back in, again and again and again.  The fish flails wildly, incredibly strong but also stupid, not coordinated enough to either attempt to flee or fight back.

    """
    if game.playerbackground == "marked" or game.playerbackground == "merchant":
        """But that does not matter.  After who knows how long spent attacking the creature, in one of its moments of blind panic it rolls over, pushing you under the water and against the river bed.  You feel the air being knocked out of you and you instinctively breathe in.

        It is strange that water can feel so much like burning.  You push madly against the weight flexing against you, your eyes popping open but seeing nothing but black.  You feel yourself growing weak, the edges of your thoughts misty, distorted and lethargic, and you just begin to sense yourself letting go, letting go of everything, when the weight disappears and a wave pushes against you.

        You try to let out a scream, an expression of hope, but of course nothing comes out of your throbbing lungs.  You use the energy instead to go with the wave, pushing yourself across, slamming into the bank and then up until...

        ...you're coughing, blood, yours or the fishes you cannot tell, your vision mostly sharp points of light, all of your muscles concentrated on nothing but expelling all of the water from inside your body.

        You retch, fish scales and sediment from the river bed coming up with your breakfast.  Your vision starts to clarify and your spasms turns to shaking.

        And then the bulk of the fish slams into you, and you are dragged back into the water.

        Whether through rage or a panicked realisation that the only way to survive is to kill the beast, you grab the spear still impaled in the creature's side and, somehow, your mind is too flayed to remember how, kill it."""
        
    else:
        """That is what saves you.  If the creature had any understanding of what it should do to kill you, you would be dead.  You understand enough about this sort of thing to know that.

        But that is not to say the fight is not long, long and difficult.  By the time you have thrust your spear into the unmoving beast for the last time all of your limbs have turned to rubber, cold and weak, you feel light headed as soon as the adrenaline wears off and very little of your skin has not turned blue from bruises and extreme cold."""
        
    """

    You hear the town bell toll the hour as you trudge back up onto the bank to retrieve the nets.  Luckily just as you are attempting to haul the beast up the bank a group of youths, fresh from a hunt, stop their walk and wade in to help.

    You are exhausted, but you join them as a cart is called and the kill is paraded through town, people peering out of doors and windows to see what all the noise is about.

    Soon half of Lotosk is gathered around the central fire while Mik prepares the meat, stripping out large, thick bones and throwing them, disgustedly, to a small pack of dogs.

    The celebrations go on for some time, but you leave early.  Simply put, all you want right now is rest.
    """

    #{Slight morale boost}  #{A fuck ton of food}  #{Player takes injuries, some if deserter or woodsman, lots if marked or trader}

    








label leviathanend:
$ game.riverevents['theleviathan'] = False # temporary
hide woodssky onlayer skyback
hide woodsdeepest onlayer farfarback
hide woodsdeeper onlayer farback
hide woodsdeep onlayer back
return
