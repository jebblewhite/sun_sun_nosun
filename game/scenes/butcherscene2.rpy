label butcherscene2:

"""

You enter the butcher’s shop and are greeted immediately by the muffled sounds of someone … actually you’re not sure what the sound is.  All you can say is that it is wet and dull.  Maybe it is just your assumptions, but the sound makes you think of the word ‘flesh’.

A grunt from the back room lets you know that Mik is aware they have a customer, but it still takes several minutes before they appear, hands slick and dark with gore.

Mik seems genuinely surprised to see you for a moment, before they pull their face back into its normal sardonic scowl.
"""

butcher """

So the student has returned.  I’m a little surprised, but it appears you’re more stubborn than I had given you credit for.  

Or maybe more argumentative.  

Or maybe you just wanted to see little old me.  
""" #wink

"Mik holds the back of their hand to their chin as they say this, framing their face."

butcher """

Don’t tell me, I like the mystery.  Also knowing you I’ll be disappointed by the answer.  """#Wink here only if attraction is above a certain threshold.

butcher """

What I am more interested in hearing though, because very few people who aren’t already singing in my choir will listen to me long enough to debate me intelligently, is how wrong you think I am?
"""

menu:

    "You’re just wrong, about all of it.":
        $c=3

    "You’re right about the evils of the state, but liberal capitalism is how we will emancipate ourselves.  It isn’t the enemy.":
        $c=1
        butcher """

        So says the liberal propaganda.  But it isn’t true.  

        Yes, the rise of personal property did lead to emancipation from the state.

        But it only led to the emancipation of a very specific class: the bourgeoisie.  They were, and still are in the Kingdom, revolutionary, but their revolution would simply see one set of oppressors replaced with another.
        """

        #{Slight like loss with Mik} 
        #{Very slight respect gain with Mik}

        $c=5


    "You’re right about the evils of the bourgeoisie, but the state is how we protect ourselves from them.":
        $c=2

    "You’re right, the proletariat are all slaves to both the state and the bourgeoisie.":
        $c=4



butcher """

The point shouldn’t be revolution for the sake of revolution, although everyone does like a spot of excitement from time to time.

No, the aim is not to bring down #{i}the#{/i} state.  It is to bring down ‘state’ as a social construct.

The idea is not to destroy the oppressors.  It is to destroy #{i}oppression#{/i}.

The revolution I call for is total, final and destructive.
"""

return
