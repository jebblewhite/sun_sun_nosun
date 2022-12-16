label aldermanscene7: 


"""

There was no sign that there would be trouble until it started.

The day had been normal, or as normal as days ever are since the sun disappeared.  The busiest time for the town square, when most of the town comes out to collect food and wood and fur, was just coming to an end.  

The Alderman, who had been helping to organise the proceedings, was just returning to the Town Hall, walking up to the front door, when Alina stepped directly into his path, a large piece of paper held in her hand.

Her voice had been firm, and loud enough for everyone in the square to hear.
"""

alina  """

Alderman Alexi, by order of, and by the power of, the Senate, I hereby relieve you of your duty as governor of this town.

I, as a representative of the Senate, have found your governorship wanting in many regards.  Most damningly, you have been unable to allocate resources appropriately during a time of crisis.

You have made no attempt to use your allocative powers to produce a solution to the current problem.

You have therefore put, and continue to put, the lives of the citizens, the Republican citizens, of Lotosk at risk.
"""

"""

There is a moment of shocked stillness.  The Alderman stands frozen in place, his body tilted as if time had simply stopped between steps.

Then he shifts, slowly, his legs coming together and his back straightening.  His arms quiver for a second as he fights the instinct to fold them across his chest, but he wins the battle and sends them down to rest by his sides.

His face is hard and neutral.
"""

alderman  "My job, as Alderman of this town, is to keep the people of Lotosk alive.  I have done that, as best as can be done, and I continue to do it."

"The Alderman suddenly turns his body slightly, no longer facing Alina but instead addressing the square."

alderman  """

What you suggest, Officer Alina, or what you have suggested to me in private discussions, is to deny equal rations to those who do not work.

This favouring of some over others does not sound like the action of a democratic republic.  You say you act in the name of the Republic, but I was elected and you were not.  What you are doing, Officer Alina, is un-Republican.

Not to mention, of course and more importantly, that it is vile and immoral.  The good people of Lotosk will not stand by and watch as their fellow townsfolk die for lack of what they have in plenty.
"""

#MM
if game.popMorale>= 60:
    "There is a short round of applause after the Alderman has finished speaking."
    if game.popCohesion<= 40:
        "However, a shrill voice cuts through clapping."

        "Man"  "If everything's so good and equal, why did I come home yesterday to find my window smashed and my new fur gone?"

        "The clapping stops as members of the crowd embarrassedly turn to each other to admit that yes, they have all at least heard the stories of rising crime."

else:
    "The Alderman's words are met with silence and an awkward shuffling of feet."

    "Woman"  "Those are awful nice words, but if she's bad, what makes you good?"
    if game.popCohesion<= 40:
        "Man"  "And if everything's so good and equal, why did I come home yesterday to find my window smashed and my new fur gone?"
    "The crowd bubbles slightly, a few more voices rising just above the general hum, cautiously voicing their own dissatisfaction."

"A man pushes himself through the crowd, and the Alderman visibly droops as the man plants his large legs firmly into the dirt, places his hands on his hips and begins to bellow."

"Jacob"  """

As someone who's actually travelled this Republic, both as a soldier in its fine army and then as a man of commerce, I can tell you, Mr Alderman, that you're wrong.

Now I've fought the Kingdom, I've seen what the life of a serf is, and it's a life without freedom, without the opportunity to forge your own path and make your own destiny.  The Kingdom, our greatest enemy I remind you, tells its people what to do and lets them only take what it gives them.

Does that sound familiar to you, Mr Alderman?  Isn't that exactly what you've created here, your own little Kingdom where you can tell us what to do and what to take?  Even our fine hunters, like my son, can only keep what you let them keep.

Now fine Miss Officer Alina, why she is only proposing that we let each person take their own life into their own hands!  Let us work for our own survival, rather than having to beg it from you!
"""

if game.playerbackground == 'merchant':
    $textinsert = ", and one of your biggest rivals,"
else:
    $textinsert = ""

"Jacob, a self made man and formerly one of the richest people in town[textinsert] finishes with a flourish, his bright orange silk shawl rippling as he raises his arms above his head.

However, from your position, on the other side of Jacob from the crowd, you notice that his theatrics neatly hide a wink he sends, almost flirtatiously, to Alina.
"""

menu:
    "Don't listen to Jacob, he's just in Alina's pocket, it's all just in his own self interest!":
        $c=1

    "I recognise that free enterprise is very important, but when we risk starvation we must consider its loss an acceptable opportunity cost.  We must pull together, not fracture apart" if game.playerbackground == 'merchant':
        $c=2
        #{Slight morale increase}
        #{Respect increase with the Alderman}
    "Now isn't the time for all that, we need to stick together to survive" if game.playerbackground != 'merchant':
        $c=3
        #{Like increase with the Alderman}
    
    "Jacob is right, but I will go even further.  If our survival is directly in our own hands, we will all find ourselves working harder and we will all be more likely to survive.  It's an economic fact" if game.playerbackground == 'merchant':
        #{Slight morale increase}
        #{Respect increase with Alina}
        $c=2
    
    "Jacob is right!  We need the freedom to save ourselves, we shouldn't rely on the Alderman for whether we get to eat!" if game.playerbackground != 'merchant':
        #{Respect increase with Alina}
        $c=3
        
    "*Say nothing, let this play out*":
        $c=4
label reevaluatealderman7:
if c ==1:

    "Jacob waves his hand towards you as if he is trying to swat a fly that he isn't actually too concerned about."

    "Jacob"  "I'm just saying what would be best for the town.  You're the one making it personal."

    "The crowd nods its general agreement, and you see a few people shoot dirty looks towards you."

    #{Slight like gain with the Alderman}  #{Very slight morale loss}

    $c=4

if c ==2:

    "The crowd begins to bob with nods, fuelled by the low hum of thoughtful agreement."

    $c=4

if c ==3:

    "A member of the crowd shouts out support, then another immediately shouts the first one down.  Within seconds the crowd has turned on itself, the arguments between neighbours civil for now but gaining heat by the moment."

    $c=4

if c ==4:

    "Alina takes half a step forward, the movement such a change from her controlled stillness that she immediately gains the crowd's attention."

    alina  "It is a fact, economic and sociological, that if you allow your Alderman to continue to control you like he has been doing, you will all die.  You must allow me to allow you to seize your own destiny."
    if game.AldermanPlan == 'Love':
        $textinsert2 = "Our care and love for each other is what will get us through this, not Alina's mathematics and economics!"
    else:
        $textinsert2 = "Alina gives you dry 'facts', but the answer to how we make it through this isn't in her Alexisgrad books, it's in our strong, northern, Lotosk souls!"

    alderman  "Nonsense!  I have led this town for years, you have all put your trust in me before and I promise you that I will be the best person to lead us through this crisis. [textinsert2]"

 
    "Woman"  "You're both just giving us words, what are you actually going to do for us, what are you actually going to change!"

    "Man"  "Yeah!  We can't feed ourselves on philosophy, we need action, we need change!"
    #MM
    if game.popMorale<= 30:
        "Woman"  "The only thing that's changed with Alexi in charge is that now we have less food on our plates!"
    if game.popCohesion<= 30:
        """

        A section of the crowd roars in agreement.

        There is a violence in that cry, a hungry aggression, and you instinctively find yourself dropping into a crouch ready for trouble, your eyes scanning the people in the square until…

        There.  A young man, standing up from a squat, his arm already returning to his sides.  Your eyes snap along the arc from his cupped hand just in time to see a rock fall less than a foot from the Alderman's head.
        """
    
    menu:
        "You don't need change, the Alderman is already doing the best that can be done!":
            #{Like increase with the Alderman}
            $c=6
        "Alina will act, she'll let you be the change you want to see!":
            $c=5
            #{Respect increase with Alina}

        "Tackle the man who threw the rock" if game.popCohesion<= 30:
            $c=8

        "*Say and do nothing*":
            $c=5

        "You're all acting like children!  Take your heads out of your arses and listen for a fucking moment!":
            $c=14
            #mm{unrest up}


if c ==5:

    "Woman"  "I'm too old to work and my granddaughter is too young.  You'd just let us die?"

    "A good section of the crowd hang their heads in shame at this, but some turn on the old woman."

    $c=7

if c ==6:

    "Woman"  "That's right.  I'm too old to work and my granddaughter is too young.  The Alderman is doing all he can to make sure we get the same opportunities as those lucky enough to be fit and strong."

    "Many in the crowd awkwardly look at their feet and nod, but some people turn on the old woman."

    $c=7

if c ==7:

    "Man"  "It's life or death out there!  You don't know what it's like, going into that forest every day, risking our necks just so that you can sit on your arse and eat the food that we bring you!  I'm sorry if it's not 'nice', but I'm not going to starve to death for you."

    "Another hunter spins on his heels and tells his younger colleague to go fuck himself.  An old trader, a man in his sixties, loudly says that he's had his chances in life and that it is wrong that the younger generation should lose their opportunities because of him."

    $c=9

if c ==8:

    """

    You sprint forward, planting your shoulder in the centre of the man's chest just a moment after he turned to see you, a look of shock on his face.

    He falls heavily to the ground, the air knocked out of him to such an extent that he does not even have the energy to attempt to fight back before the crowd pulls the two of you apart.  The hands that push him to his feet are rough, while the ones that pull you away turn into reassuring, supportive pats as the young man slinks away.

    You turn away from the surprised, respectful faces and as you do the silence is broken by an older woman.
    """

    "Woman"  "[game.player_name] understands the need to protect people.  I'm too old to work and my granddaughter is too young.  The Alderman is doing all he can to make sure we get the same opportunities as those lucky enough to be fit and strong."

    "Many in the crowd awkwardly look at their feet and nod, but some people turn on the old woman."

    #{Slight respect gain with the Alderman and Alina}  
    #je{Slight unrest decrease}

    $c=7


if c ==9:

    """

    A look passes between the Alderman and Alina, an acknowledgement that while they're on different sides, this is one thing that they can agree on.

    They both step forward, both holding up their hands.
    """

    alderman  "Please, please, this is not how we should behave.  This is not how the people of Lotosk deal with their problems."

    alina  "Quite.  This is not the forum for physical civil disobedience.  This is a political matter, and as such should be discussed in a calm, level-headed way.  That is the way of the Republic."

    """

    The crowd, seeing that the leaders of both factions are requesting it calm down, goes from a boil to a simmer, before the resentment causes it to split and disperse, neighbours staring daggers at each other as they take their food, wood and furs and return to their homes.

    Alina turns back to the Alderman.
    """

    alina  """

    Whatever else you may want to say, it is clear that I have local support.  Not that I need it, given my Senate support.

    Alexi, you are relieved of your position.
    """

    alderman  """

    No, Officer Alina.  I am not stepping down from my post.  I think it is quite clear that … things may become ugly if there is too much change to the social hierarchy of this town.

    If you want me out of my office, you shall have to come in and throw me out.
    """
    #MM change below - check game2.py line 43 for class based relationship matrix
    if game.alderman.relationship_matrix() > 8 and game.nazi.resp >= 4:

        "The Alderman turns and gestures for you to go with him.  Not seeing this, Alina shakes her head and indicates that you should follow her."
        menu:
            "*Go with the Alderman*":
                $c=11

            "*Go with Alina*":
                $c=10

            "*Shake your head and just walk away*":
                $game.coup = "Not Involved"
    
    elif game.alderman.relationship_matrix() > 8:

        "The Alderman turns and gestures for you to go with him and then starts walking into the Town Hall."
        menu:

            "*Go with the Alderman*":
                $c=11

            "*Shake your head and just walk away*":
                $game.coup = "Not Involved"
    
    elif game.nazi.resp >= 4:
        "As the Alderman walks back into the Town Hall, Alina gestures towards you, indicating that she wants to talk to you."
        menu:
            "*Go with Alina*":
                $c=10

            "*Shake your head and just walk away*":
                $game.coup = "Not Involved"
    else:
        "The Alderman walks back into the Town Hall.  Alina shakes her head, carefully rolls up her senate writ, and walks determinedly in the direction of Jacob's shop, leaving you alone in the town square."
        $game.coup = "Not Involved"

if c ==10:

    "Alina does not modulate her volume as she says:"

    alina  """

    [game.player_name], I've got some work to do, but soon enough I will be calling on you.  I will need help restoring order to this town and I can't think of anyone more qualified to help me.

    Be ready [game.player_name].  Justice will soon be restored, but until then, do keep working for Alexi.  The stockpiles will be useful for the creation of incentives.
    """

    "Alina nods and walks away."

    $game.coup = "Alina"#{Set $Coup = "Alina"}



if c ==11:

    "You follow the Alderman into the Town Hall, the large space cool and calm."

    alderman  """

    I'm not going to ask you if I'm doing the right thing [game.player_name].  I don't know if it's morally right, but I can't worry about that.  I know it is what is best for this town, so I'm going to do it.

    [game.player_name], I'm going to do something.  Something to stop Alina from taking over Lotosk.

    What I'm planning, what I have to do, it's not nice.  And I'm not at all proud that I even thought of it.

    It makes me sick that I'm actually going to do it.

    But I am going to do it.  Because I can't let any more people here die than have to.

    I can't tell you any more than that [game.player_name], not yet.  Only that if everything goes right, no-one should die.  That is the whole goal.  But still, it will be unpleasant.

    I am not expecting that you will help me.  But I am an old man, and I know that it will be difficult on my own, so I'm going to ask you to help me, knowing that you should probably say no.  But for the good of the town, I am asking you."""
    
    if game.alderman.attraction_matrix() > 8:
        alderman """
        Don't worry about what I feel, just think about the logic.  Because I desperately want you to do it, but I also desperately want you to stay safe.  But maybe you don't care about me as much as…

        Just think of the logic [game.player_name]."""

    alderman "Will you help me stop Alina?  Will you give me your solemn word that you will?"
    
    menu:
        "Yes":
            $c=12

        "No, I'm not going to get involved with this":
            $c=13


if c ==12:

    "The Alderman nods gravely."

    alderman  """

    Then I will contact you soon.

    For now go.  Put it out of your mind.  Sleep soundly tonight.  There is no need for you to dwell on this unpleasantness more than you have to.
    """

    $game.coup = "Alderman"


if c ==13:

    "The Alderman nods gravely."

    alderman  """

    That is probably for the best.

    Go now, then.  And put this unpleasantness out of your mind.  I think it is right that I should bear this burden alone.
    """
    $game.coup = "Not Involved"


if c ==14:

    "Man"  "Fuck you, you think you're better than us?  We work just as hard as you do, where do you get off telling us what to do?"

    "Woman"  "[game.player_name] is just trying to help!"

    "Man"  "Oh please, [game.player_name]'s just protecting their 'special relationship' with the Alderman."

    if game.alderman.attraction_matrix() > 8:
        "The Alderman glances at you, his eyes uncomfortable but his cheeks strangely flushed."

    "Woman"  "Listen, I'm too old to work and my granddaughter is too young.  The Alderman is doing all he can to make sure we get the same opportunities as those lucky enough to be fit and strong."

    #{Slight cohesion decrease}

    $c=7
    jump reevaluatealderman7


return
