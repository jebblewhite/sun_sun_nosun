label aldermanscene5: 

$alderman5morepeople = False
$alderman5emotions = False
$alderman5innovators = False
$alderman5unequal = False
$alderman5treaties = False

"""

The argument, which you could tell was heated from the muffled sound of their voices from the other side of the door, abruptly stops the moment you walk in.

You are here because the Alderman asked you to be here.  Or rather, the Alderman sent Nat to ask you to be here.  The Alderman's message had few details, but a quick questioning of Nat, who seemed more anxious than usual, revealed that the problem was probably related to Alina.

And now you're here in the Alderman's office, a still clearly ill Alina managing to convey a great deal with her expertly neutral expression, while the Alderman straightens from his cowed hunch as the door closes behind you.
"""

alderman  """

Ah, [game.player_name], I'm very glad you could join us.

I hope you don't mind Officer?
"""

alina  "Not at all Alexi.  You may have your second."

"The look that passes between the two lets you know that both accept that Alina just scored a point."

if game.aldermanplan == "Love":
    $ textinsert = "if we all care for each other, we'll all make it through this,"
elif game.aldermanplan == "Cunning":
    $ textinsert = "if we act sensibly and remind everyone that mutual aid is in their own best interest, we'll make it through this,"
elif game.aldermanplan == "Pride":
    $ textinsert = "if we all just remember our duty to the town, and our pride in it, we will all make it through this,"

alderman  "Very good.  Now, [game.player_name], Officer Alina and I were just discussing some practical matters.  While I am of the opinion that [textinsert] Officer Alina believes that the only way for Lotosk to survive is to, ahem, let the weak die."

"The Alderman turns confrontationally towards Alina, who does not even blink."

$textinsert2 = game.aldermanplan.lower()


alina  """

I said 'let the strong survive', but you aren't wrong {i}there{/i} Alexi.

Where you are wrong is thinking that [textinsert2] alone will result in total survival of this town.  Because it won't.  Your policies will kill everyone here.
"""
"The Alderman looks at you imploringly."
menu:

    "Let's hear Alina out":
        $c=4

    "Alina, that's a horrible thing to say!":
        $c=3

    "With all due respect Alina, the Alderman knows this town better than you do":
        $c=1

    "Having fewer mouths to feed sounds like a good idea to me":
        $c=2

label reevaluatealderman5:

if c==1:
    alina  "With all due respect, knowledge does not equal wisdom."

    #JE{Slight like, respect and attraction increase with the Alderman} #{Very slight respect loss with Alina}

    $c=5

if c==2:
    """

    Alina nods once, thankful for your support.  If she objects to your callous wording, she does not show it.

    The Alderman, on the other hand, does.
    """

    #JE{Like and respect loss with the Alderman}  #{Very slight respect increase with Alina}

    $c=5

if c==3:

    alina  "A mature, and well reasoned argument."

    #JE{Like gain with the Alderman}  #{Slight respect loss with the Alderman}  #{Respect loss with Alina}

    $c=5

if c==4:

    "Alina nods once, thanks for your support."

    #JE{Slight like loss with the Alderman}  
    #{Slight respect gain with the Alderman}  
    #{Respect gain with Alina}

    $c=5


if c==5:

    #check food against population
    if game.food >= 2*game.countAlive():
        $textinsert = "adequately"
    else:
        $textinsert = "barely"

    alina  """

    The fact of the matter is that resources are dwindling.  You may have enough to [textinsert] feed your populace now, but the situation will only get worse.

    It's a scientific fact.

    The same goes for fuel and pelts and medicine.  Your current distribution philosophy will, sooner or later - and if I were a gambler, which I am not, my money would be on sooner - lead to the death of everyone in this town.

    You are living through an unprecedented event and it will take strong, gifted, incentivised innovators to lift you out of it.  But even the greatest thinkers need time, especially for implementation, and you are not giving it to them.

    Most of the food you are gathering is meat.  I have checked your records and found that you have enough salt from when this town was considered as a fall-back point during the war to cure most of the meat that you gather.  Instead you cook it fresh and give it away to the ill, the old and the too young to work.

    It's dangerous, and if I may Alexi, you know it.  I know you know it because you feel the need to hide your Communism behind a veneer of Republicanism.

    [game.player_name], do you know that your Alderman is using you as a piece of propaganda?  I do not know if he is trying to fool his people or just himself, but as far as I can see it, your main role is to legitimise his socialism by pretending that it is all led by a single, free, hard-working, innovative individual.

    But it isn't.  What power has Alexi ever actually given you, save the power to represent his non-existent Republican loyalties?  You have, in material terms, and it is a Republican truth that those are the only terms that matter, no more power than any other individual.

    No, this town has adopted socialism at the very moment when it needed drastic, ruthless innovation.  If no-one in this town thinks of a way that this endless night can be survived, then every last one of you will die.  Do you disagree?
    """

    """

    A quick glance towards the Alderman shows a bent old man, staring at his feet and deeply lost in a mix of thought and sadness.

    He clearly isn't about to answer.
    """
    menu:
        "But surely the more of us who live, the more people there are to innovate?":
            $c=6

        "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died":
            $c=7

        "Not everyone in town has the same amount of power.  You're forgetting that Alexi has left plenty for himself...":
            $c=8

        "How do you know we aren't innovating?":
            $c=9

        "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treatise there, {i}'The Positive Impacts of Social Cohesion on Rural Economic Development'{/i}" if game.playerbackground == "merchant":
            $c=10

        "What you're saying is economically sound.  This treatise right here, {i}'Incentive, Necessity and Survival: The Ingredients of Innovation'{/i} would agree with you point for point" if game.playerbackground == "merchant":
            $c=11

        "The philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

if c==6:

    alina  """

    My apologies, I focussed too much on innovation.

    I know that it takes a village to raise a child.  The innovator will need skilled and hard-working hunters and craftspeople to keep them alive.  There must be workers as well as thinkers.

    But not everyone in this town is a worker.  Some are too old, some too sick, some too young**.

    It is giving {i}them{/i} the same materials as are given to the required workers to which I object.
    """

    #JE(if law)[, even with your new edicts]
    $alderman5morepeople = True
    #JE{Slight respect increase with the Alderman}  
    #{Slight respect loss with Alina}

    menu:
        "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died" if not(alderman5emotions):
            $c=7

        "Not everyone in town has the same amount of power.  You're forgetting that Alexi has left plenty for himself..." if not(alderman5unequal):
            $c=8

        "How do you know we aren't innovating?" if not(alderman5innovators):
            $c=9

        "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treatise there, 'The positive impacts of social cohesion on rural economic development'" if not(alderman5treaties) and game.playerbackground == "merchant": 
            $c=10

        "What you're saying is economically sound.  This treatise right here, 'Incentive, Necessity and Survival: the ingredients of innovation' would agree with you point for point" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=11

        "All this philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

        "I think you are right":
            $c=13

        "I think you're wrong":
            $c=18

if c==7:

    "Alina rolls her eyes."

    if game.aldermanplan == "Love":
        $textinsert3 = "love each other"
    elif game.aldermanplan == "Cunning":
        $textinsert3 = "take pride in their town"
    elif game.aldermanplan == "Pride":
        $textinsert3 = "just 'act smart'"

    alina  """

    Whatever my personal feelings towards emotions, which I acknowledge is an ironic turn of phrase, as someone who works closely with the senate I can never afford to forget emotions.  

    Remembering emotions is what separates the Senators who win votes from the ones who don't.

    In this case, {i}I{/i} have not forgotten that fear is the strongest emotion that a person can feel.  Nothing motivates more than that.

    To give you an extreme example, I believe that even a mother who rescues her infant from a burning building does so out of fear of loss, not love.  Well, maybe both, but it is fear that pushes her through the flames.

    In this case all your Alderman seems to be doing is coddling his people.  Telling them that if they [textinsert3] then they will survive.  He is doing everything he can to dull his people's natural fear instincts.

    Your Alderman is keeping the people of this town from feeling the fear of death until it comes to all of you.  At which point it will be too late.
    """

    "Alina stops for a second, and then sighs."

    alina  "I know that isn't pleasant.  But it is true.  And the truth is always worth more than feelings."

    $ alderman5emotions = True 
    #JE{Respect loss with Alina}
    menu:
        "But surely the more of us who live, the more people there are to innovate?  It's the same number of man hours either way" if not(alderman5morepeople):
            $c=6

        "Not everyone in town has the same amount of power.  You're forgetting that Alexi has left plenty for himself..." if not(alderman5unequal):
            $c=8

        "How do you know we aren't innovating?" if not(alderman5innovators):
            $c=9

        "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treatise there, 'The positive impacts of social cohesion on rural economic development'" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=10

        "What you're saying is economically sound.  This treatise right here, 'Incentive, Necessity and Survival: the ingredients of innovation' would agree with you point for point" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=11

        "All this philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

        "I think you are right":
            $c=13

        "I think you're wrong":
            $c=18

    jump reevaluatealderman5


if c==8:

    "Alina does not smile, but she does nod once."

    alina  """

    Political, rather than material inequality.  The first usually leads to the latter.

    I will say this for you, Alexi.  I think you will be an exception.  I think you are making massive mistakes with your policies, but I do not think you are corrupt.

    But [game.player_name] is right.  You are the only one in this town who is not an equal, at least in one way.
    """

    "The Alderman says nothing, but you think you see him nod, very slightly, as he continues to stare at his feet."

    $ alderman5unequal = True  
    #{Very slight respect increase with the Alderman}  
    #{Attraction loss with the Alderman}  
    #JE{Slight respect gain with Alina}
    menu:
        "But surely the more of us who live, the more people there are to innovate?  It's the same number of man hours either way" if not(alderman5morepeople):
            $c=6

        "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died" if not(alderman5emotions):
            $c=7

        "How do you know we aren't innovating?" if not(alderman5innovators):
            $c=9

        "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treaties there, 'The positive impacts of social cohesion on rural economic development'" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=10

        "What you're saying is econimically sound.  This treatise right here, 'Incentive, Necessity and Survival: the ingredients of innovation' would agree with you point for point" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=11

        "All this philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

        "I think you are right":
            $c=13

        "I think you're wrong":
            $c=18

    jump reevaluatealderman5

if c==9:

    alina  """

    Because I can see it.

    Your herbalist and doctor and innkeeper all seem to have made very small strides, but from what I hear they seem satisfied with what they have achieved and are not pushing their sciences further.

    Only the mad girl is doing anything 'unique', and that will be nothing but harmful.  Anyone whom she drags into her mad, dangerous, heretical cult will only become less productive as they become more certain that their false god will save them.
    """

    $ alderman5innovators = True 
    #{Very slight respect increase with the Alderman}  
    #je{Slight respect loss with Alina}
    menu:
        "But surely the more of us who live, the more people there are to innovate?  It's the same number of man hours either way" if not(alderman5morepeople):
            $c=6

        "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died" if not(alderman5emotions):
            $c=7

        "Not everyone in town has the same amount of power.  You're forgetting that Alexi has left plenty for himself..." if not(alderman5unequal):
            $c=8

        "I could give you a list of all the reasons your economic assumptions are incorrect if you want.  Alderman, if you could pass me that treatise there, 'The positive impacts of social cohesion on rural economic development'" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=10

        "What you're saying is economically sound.  This treatise right here, 'Incentive, Necessity and Survival: the ingredients of innovation' would agree with you point for point" if not(alderman5treaties) and game.playerbackground == "merchant":
            $c=11

        "All this philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

        "I think you are right":
            $c=13

        "I think you're wrong":
            $c=18

    jump reevaluatealderman5



if c==10:

    "Alina narrows her eyes at you."

    alina  """No need [game.player_name].  Pass me the book and I will read it in my own time.

    But I have studied political philosophy, and some economics, at the Holy University of Friedrich, Fourth of the Pantheon.  I do know what I am talking about.

    Still, I will take the treatise.
    """

    $ alderman5treaties = True 
    #{Respect increase with the Alderman}  
    #je{Slight respect increase with Alina}
    menu:
        "But surely the more of us who live, the more people there are to innovate?  It's the same number of man hours either way" if not(alderman5morepeople):
            $c=6

        "You're ignoring emotions.  People work better when they feel supported.  And when everyone they love hasn't just died" if not(alderman5emotions):
            $c=7

        "Not everyone in town has the same amount of power.  You're forgetting that the Alexi has left plenty for himself..." if not(alderman5unequal):
            $c=8

        "How do you know we aren't innovating?" if not(alderman5innovators):
            $c=9

        "All this philosophy is irrelevant, what you're suggesting is simply morally abhorrent":
            $c=12

        "I think you are right":
            $c=13

        "I think you're wrong":
            $c=18
    jump reevaluatealderman5



if c==12:

    alina  "I am a moral anti-realist, or more specifically a relativist.  So I won't argue with you, but I will say that, as far as I am concerned, {i}ethical discussions{/i} are irrelevant."

    #{Respect loss with Alina}  
    #{Slight like and attraction increase with the Alderman}

    $c=14



if c==13:

    "Alina smiles for the first time since you entered the room, the expression flat and rehearsed, but still pleased, if clinically so."

    #{Respect gain with Alina}  #{Slight like and attraction loss with the Alderman}

    $c=14



if c==14:

    alina """

    What I have said is economically and philosophically sound.  If your Alderman continues with his socialist distribution methods, then everyone in this town {i}will die{/i}.

    There are two things you need to do instead: firstly you have to offer a large, material reward in return for any actionable suggestions that could lead to an increase in habitability of the area, and secondly you have to-
    """

    alderman  "No."

    alina  "Excuse me?"

    alderman  """

    Sorry Officer, but no.  I will not do that.

    I've never studied in one of the Pantheon universities, but I think I am right that Alexis wouldn't have left their people behind.  I don't think Dominike would have left his people to freeze to death.  And I don't think Casimir fought for the freedom of only the able bodied and sharp of mind.

    I intend to follow their example.  I am the leader of all of my people.  

    And...and...and well...if that makes me a bad Republican…

    Then so be it.

    Now I'm afraid, Officer, that I have much work to do, so I am going to have to ask you to leave.
    """

    """

    The Alderman's words are strong, but you can see that he is shaking, although what exactly is causing it you cannot quite tell.

    Alina, her face totally dispassionate, glances towards you.  Waiting to see where you'll land.
    """
    menu:
        "You can't just kick her out, you have to listen to what she's got to say!":
            $c=15

        "It's best if you leave, Alina":
            $c=16

        "*Just stare back, don't make the first move*":
            $c=17

    

if c==15:

    alderman  """

    I have listened to what she has to say.  All morning.  Now I have work to do.

    I think it would be best if you left too, [game.player_name].  I want to work in peace.
    """

    "You open your mouth to speak back, but Alina beats you to it."

    alina  "Your unwillingness to co-operate is noted.  By both of us, I am sure.  But for now, [game.player_name], let us leave him.  I think when Alexi has had time to think it all over, he will see that I am right."

    """

    Alina turns and holds the door open for you.  Without any other choice, you leave.

    She does not speak to you as you walk out.  All she does is nod and smile once.
    """

    #{Slight respect gain with Alina}  
    #je{Slight like, respect and attraction loss with the Alderman}

if c==16:

    "Alina purses her lips, and then nods."

    alina  "Your unwillingness to co-operate is noted.  But I am sure that once you have had time to think it all over, you will see that I am right."

    "And with that, she leaves."

    
    #alderman  """

    #(if no events)[Thank you [game.player_name].  But I think it would be best if you left too, I am afraid.  I feel…I feel I need to be alone for some time.
    #"""]
    #MM
    #{Slight respect loss with Alina}  
    #JE{Slight like, respect and attraction gain with the Alderman}



if c==17:

    "Alina shakes her head slightly and lets out a tiny, calculated sigh."

    alina  "Your unwillingness to co-operate is noted, Alexi.  But I am sure that once you have had time to think it all over, you will see that I am right."

    "And with that, she leaves."

    #alderman  """

    #(if no events)[I think it would be best if you left too, I am afraid.  I feel…I feel I need to be alone for some time.
    #"""]
    #MM

    #{Very slight respect loss with Alina}  
    #JE{Very slight like, respect and attraction loss with the Alderman}

if c==18:

    "Alina shakes her head."

    alina  "I am afraid what you think doesn't matter."

    #{Slight respect loss with Alina}  
    #JE{Slight like increase with the Alderman}

    $c=14
    jump reevaluatealderman5




return
