# needs to be tied to the map
label aldermanscene2:
"""

You have to look twice before you realise that what you’re looking at is the Alderman.  Sitting perfectly still and wrapped in a large brown blanket, the Alderman looks more like a rock than a person as he sits by the river, looking towards the forest.

Still, as you approach he turns to you and smiles, although the light of the moon is strong enough for you to see that there is sadness in his eyes.
"""

alderman  "Ah, [game.player_name].  It’s good to see you.  I just came out here to get away from work for a time.  Please, come and sit with me."

"He waits for you to sit before he continues."

alderman  "Would you like to borrow my blanket?  It’s cold out."
menu:
    "I’m dressed warmly enough already, thank you":
        $c=2
        alderman  "Ah, of course you are.  You probably get out a lot more than I do, you’re much more used to it."

        $ game.character.statchange("resp", 1) #{Very slight respect increase with the Alderman}

        $c=3

    "That’s very kind of you, thank you":
        $c=1
        alderman  "Of course.  I wouldn’t want you to be cold."

        $ game.character.statchange("like", 2) #{Slight like increase with the Alderman}

        $c=3
alderman  "Before this awful cold I never thought such happiness could be found in a simple blanket."

"He mentions happiness, but there is no joy in his voice.  He sits silently, his eyes fixed on the forest, but it is clear that he isn’t really looking."
menu:
    "*Stay silent*":
        $c=6
        pass

    "I sense there’s something wrong":
        $c=5
        pass

    "How’s work going?":
        $c=4
        if game.aldermanplan == "Love":
            $ textinsert = "I’ve been speaking to people, going around town, helping with the little things that I can.  Calling on the old and weak.  I haven’t run the numbers on it yet, but it feels like people are listening.  Like it matters to them, and it is helping.  With some things, at least."
        elif game.aldermanplan == "Cunning":
            $ textinsert = "I’ve been talking to the business owners around town, and those more involved with organising the work.  They seem convinced of my ideas.  But I haven’t actually run the numbers yet."
        elif game.aldermanplan == "Pride":
            $ textinsert = "I talked to some veterans in town as well as the priest and Samuel the sculptor.  We’re going to put up a small statue of Krasov, you know, the town’s founder, in the town square, with a plaque of some kind."
        else:
            $ textinsert = ""
        alderman  "It...it goes. [textinsert]"

        "It feels like he should say more, but he doesn’t, he just returns to staring, motionless, into the trees."

        $ game.character.statchange("resp", 2) #{Slight respect increase with the Alderman}  
        $ game.character.statchange("like", -1) #{Very slight like decrease with the Alderman}
        menu:
            "*Stay silent*":
                $c=6
                pass

            "I sense there’s something wrong":
                $c=5
                pass

if c==5:

    "The Alderman sighs heavily."

    alderman  "Yes, I suppose there is."

    $ game.character.statchange("like", 2) #{Slight like increase with the Alderman}  
    $ game.character.statchange("att", 2) #{Slight attraction increase with the Alderman}

    $c=6

if c==6:
    if game.playerbackground == "woodsman":
        $ textinsert = "But I don’t need to tell you all that of course, you must have worked with him."
    else:
        $ textinsert = ""
    alderman  """

    I’ve been thinking about Cynthia, and Edward.

    She was very bright.  She was born here but her mother sent her to the city to study.  She has a degree in history, I believe.  She spoke to me about it on occasion.  It and other things.

    I think she knows more about the Senate than I do, and I am, or was, in some ways, a member of it.  

    She was always very bold in our conversations.  She was never afraid to tell me when she thought I was wrong.  Which was often.

    And it wasn’t all just talk either.  She worked her way up from being a shop keeper in her mother’s little shop to having powerful trading partners across the Republic.  (if trader then)[But I don’t need to tell you all that, you were one of her competitors.]  She was one of the best organisers, one of the best educated people, that this town had.

    And he, he was brave.  I heard that in the war he, nothing but a private remember, led a group of soldiers lost behind enemy lines and successfully got every single one of them back to base safely.

    And here at home he was one of our best hunters. [textinsert] This blanket, this pelt, was one of his.

    So much talent.  So much potential.  She could have been a great organiser here now, and he could have led great hunting parties.  

    But they’re gone.

    I let them go.

    Or did I drive them away?
    """

    "He turns to you suddenly and you can tell the only reason he’s not crying is because he’s simply too tired to."
    menu:

        "They were bad apples, troublemakers.  We’re better off without them, they would only have caused problems":
            $c=13
            

        "They made a mistake, thinking they should leave.  As well as all those good things you say, they were stubborn.  No-one could have persuaded them to stay, not even you":
            $c=7
            alderman  "Thank you, it’s kind of you to say that.  I suppose you’re right, no-one is perfect, they had their vices like we all do.  But still, if only they had turned that stubbornness to a good cause, to helping this town."

            $ game.character.statchange("like", 2) #{Slight like increase with the Alderman}

            $c=12


        "You should have been harder on them.  Made them stay":
            $c=8
            alderman  "No, no that wouldn’t have been right.  Even if it had worked, I would just have become what Cynthia was wanting me to become, and while she was right about many things, turning Lotosk into a dictatorship was not one of them.  I would prefer to see them go than to have seen them stay under duress."

            $ game.character.statchange("like", -4)#{Like decrease with the Alderman}  
            $ game.character.statchange("resp", -2)#{Slight respect and attraction decreases with the Alderman}
            $ game.character.statchange("att", -2)
            $c=12


        "They were good, but remember all that you still have.  I’m still here, and I’ll work just as hard as they could":
            $c=9

        "They were good, but remember all that you still have.  I’m still here for you":
            $c=10

        "It wasn’t your responsibility to make them stay.  It was their choice to leave, and you did the right thing in letting them choose that":
            $c=11
            alderman  "I suppose you are right.  I spoke to them, asked them to stay, and they still chose to leave.  If I had done more then I would have become what Cynthia wanted me to become.  You are right, I prefer to see them go rather than stay under duress."

            $ game.character.statchange("resp", 4) #{Respect gain with the Alderman}

            $c=12


if c==9 and game.alderman.resp >= placeholder:

    alderman  "I suppose."

    "He smiles suddenly, the sadness still in his eyes, but briefly softer."

    alderman  "I should think of you like this blanket then.  Be thankful for the things I still have, not the things I’ve lost."

    $ game.character.statchange("like", 2) #{Very slight respect increase with the Alderman}  #{Slight like increase with the Alderman}
    $ game.character.statchange("resp", 1)
    $c=12



if c==10 and game.alderman.resp >= placeholder:

    alderman  "I suppose."

    "He smiles suddenly, the sadness till in his eyes, but briefly softer."

    alderman  "I should think of you like this blanket then.  Be thankful for the things I still have, not the things I’ve lost."

    $ game.character.statchange("like", 4) #{Like increase with the Alderman}  #{Slight attraction increase with the Alderman}
    $ game.character.statchange("att", 2)
    $c=12



if (c==9 or c==10) and game.alderman.resp < placeholder:

    alderman  "I’m afraid that having you here is not much comfort.  But the sentiment is good, all the same."

    $ game.character.statchange("like", 1) #{Very slight like increase with the Alderman}

    $c=12


if $c==12:
    if game.alderman.life >= placeholder2:
        $ textinsert = "But thank you.  You’ve helped an old man grieve."
    else:
        $ textinsert = ""
    alderman  """

    But it’s not just about them leaving Lotosk, taking their skills and their knowledge with them.  It’s more than that of course.  

    It’s also not just that I’m the one supposed to be keeping this town together, and they left at the first possible opportunity.

    It’s that I’ve failed them.  They’re out there, in the cold.  They’re clever and brave, and they have all that food they stole and all of Elena’s guns, but they can’t know where they’re going.  They’re lost.

    And it was my job to guide them.  Guide all of us.  And whatever happens to us here, I’ve already failed them.

    I know I shouldn’t be thinking about them, I should be thinking about all of those who are still here, all the ones I am yet to fail.  Because I am just as lost here as Cynthia and Edward are out there in the wilderness.

    But I can’t stop thinking about them.  Strong, brave, clever people, and they’re wandering lost and I can’t help them.

    I can only hope that they find what they are looking for…

    I’m sorry [game.player_name].  I think it would be best, for me, if you left.  I don’t want you seeing me like this.

    (if like is above a certain threshold then)[textinsert]
    """

    $c=0






 
return
