label butcherscene3: 

$FyodoraGood = False
$JoanGood = False

"You are passing by Mik's butcher shop when you notice something odd: Mik has brought one of their chairs outside, has placed it in the middle of the street, and is currently sitting on it, legs crossed and thinly smiling."

butcher "After … morni … eve … ah whatever. On your way somewhere important [game.player_name]? Am I getting in the way of the daily business of your oppression?"

menu:

    "What are you doing sitting out here?":
        $c=1

    "You shouldn't be blocking the street like this.":
        $c=2

    "Oh you know, just off to subjugate the masses, as you taught me *wink*.":
        $c=3

    "Nice to see you Mik, fancy a chat?":
        $c=4



if c==1:

    butcher """

    Well I could tell you that one of your hunters just brought in a … thing, something I was assured I could make into food on the one proviso that I could stop it from smelling worse than all of the village outhouses put together.

    But while that is of course true, I'm really out here because even I sometimes enjoy seeing what's going on in the lives of my fellows. Not to mention I can't bear to let all this clean country air go unbreathed.
    """
    $game.butcher.resp -= 1

    $c=5



if c==2:

    butcher """

    Why? This street was built for carts, yet I haven't seen a single one roll down here since quite a bit before the sun did its disappearing act. So there is enough room for carts, but no actual carts, and yet my one chair is 'blocking' the street?

    But I'll play your game. Bring me a law, a relevant one obviously, or a writ and I'll move. In the meantime I'll just stay here and enjoy watching the people of the town go by and breathe all this clean country air.
    """

    $game.butcher.resp -= 2

    $c=5



if c==3:

    butcher """

    I'm thrilled to hear it. If there's one thing I hate more than a statist, it's a bad statist. If you're going to oppress the majority, at least do it properly and at least enjoy it. Wink here

    I won't get in your way, not today at least. I've had a busy morning creating wealth for you, I don't have the energy to rise up today.

    No, I'm just going to sit here and enjoy watching the people of the town go by and breathe this clean country air.
    """

    $game.butcher.att += 4

    $c=5



if c==4:

    butcher """

    Isn't that adorable, you want a 'chat'. Haven't you learnt what it means when you try to 'chat' with me?

    But today I'll concede. I've spent the morning working on something one of your hunters brought in, something which she assured me I could make into food on the one proviso that I could stop it from smelling worse than all of the village outhouses put together.

    But I suppose I am willing to take a break from my people-watching, enjoying seeing what's going on in the lives of my fellows. Well, that and taking in the clean country air.
    """

    $game.butcher.like += 2

    $c=5



if c==5:

    butcher "You've never been to Alexisgrad, have you? Well, if you've got any fondness for your ability to breathe, I'd keep it that way.."

    menu:
    
        "Is that why you moved here? For the fresh air?":
            $c=6

        "Don't you find it depressing to be out here, seeing how well everyone is doing without your anarchism?":
            $c=7

        "I'm happy to know that you're interested in engaging with the community.":
            $c=8



if c==6:

    butcher """

    Not entirely, but for the sake of honesty I should say that it is part of the reason. The smoke was merely a part of the whole cocktail of toxins that were slowly killing me in Alexisgrad, many of them social but a disturbing number physical.

    Another reason was outreach. The communists have ignored everyone but the city proletariat, and while they are of course important to my movement, the workers of the countryside are just as vital for the social revolution.

    So I had both positive and negative reasons for coming here. And while one of them was indeed the breathable quality of the air, most of them were social.
    """

    $c=9



if c==7:

    butcher """

    You want my honest answer? Yes. One of the reasons I left Alexisgrad was because I thought I saw an opportunity here. The city proletariat were caught in an ideological conflict, us anarchists on the one side and statist communists on the other.

    But the country, the communists had forgotten about the country. So I thought that I should do some outreach, as well as get away from the city that was poisoning me, come here and sweep this town into revolutionary zeal.

    Yes, before you say it, I will. Naive. Our battle for the working people's soul back in Alexisgrad had distracted us from the real enemies: the statists and the bourgeoisie. Coming here, it was a kind of shock to realise that what this place lacks in communist influence, it makes up for with state-backed social ignorance.
    """

    $game.butcher.resp += 2

    $c=9



if c==8:

    butcher """

    I shall be honest with you [game.player_name], not necessarily because I want to be but because it sets a good precedent: I don't do it enough. I was thrown when I realised how mired in statist philosophy Lotosk is, and I withdrew into my profession.

    Yes, I'm out and about enough that people around here know that I'm an anarchist, but few know much more than that. It would be nice if people knew me better.

    And besides, it's hardly in the spirit of collectivism to keep myself away from the very people I believe I should form a collective.
    """

    $game.butcher.like += 1

    $c=9



if c==9:

    if game.butcher.resp > 13:
        $textinsert = "You've listened to me with respect, so I'd like to return the favour and ask you a question."
    else:
        $textinsert = "You're just the kind of person whose opinion I'd like to have so I can believe the opposite."

    butcher "That reminds me. I've been meaning to ask about someone. I hear - in those few moments when I go to the inn to enjoy my own company - mention of the town herbalist, Joan. [textinsert] What do you think of Joan?"

    menu:
    
        "She's just an old traditionalist, stuck in her ways.":
            $c=10

        "She means well, but doesn't really get anything done.":
            $c=11

        "You should give her a chance. She puts community and the people first in everything she does.":
            $c=12



if c==10:

    if game.butcher.resp > 13:
        $textinsert = "I suppose you wouldn't be saying that unless it was true."
    else:
        $textinsert = ""

    butcher "That's a shame. [textinsert]"

    #{Relationship loss between Mik and Joan}

    $c=13



if c==11:


    butcher "Ah, one of those. Won't stand in the way but won't man the guillotine. The model citizen after the revolution, but a waste of space before it."

    $c=13



if c==12:

    butcher "Interesting. Maybe I should go along and speak to her. Judging purely by the remoteness of her house, she can't be that bad."

    #{Relationship gain between Mik and Joan}
    $JoanGood = True

    $c=13



if c==13:

    butcher "What about the Doctor, Fyodora? I hear she's intense, but that might be just what we need."

    menu:

        "No, she's obsessed with conservatism, keeping things as they were. It's even the idea behind her medicine: she works to keep things the same.":
            $c=14

        "She's a good person, but she won't help you fight.":
            $c=15

        "She understands sacrifice and hard work. Speak to her.":
            $c=16



if c==14:

    butcher "That seems to be the trend around here. I don't think I'll ever understand why people care so much about tradition. Why can't people see that all the things they like were at some point new?"

    #{Relationship loss between Mik and Fyodora}

    $c=17



if c==15:

    butcher "I'm not sure how good a person you can be if you won't stand up to fight against evil, but sure. Thanks for telling me what you think."

    $c=17



if c==16:

    butcher "I do have respect for people in her position. Just in order to do her job, she has to give her life to helping other people. It's what we need more of, even if she's giving her life in the wrong way. In the social revolution, of course. You're right, I should talk to her. Thanks."

    #{Relationship gain between Mik and Fyodora}
    $FyodoraGood = True

    $c=17



if c==17:

    if game.butcher.att > 1:
        $textinsert = "Not that I mind a little bit of dirt."
    elif game.butcher.like > 15:
        $textinsert = "You take care {}, don't let all that oppression wear you down.".format(game.player_name)
    else:
        $textinsert = ""

    if FyodoraGood == True and JoanGood == True:
    
        butcher """

        (if relationship between Mik and both Joan and Fyodora above a certain threshold (in other words, if both good options were just chosen))[Maybe I have misjudged this place. Don't misunderstand me, I have always loved parts of it. Alexisgrad was killing me, and I actually do mean that, in some ways, literally.

        But I had this vision that I would find some kind of near Utopia here, a proletariat that only needed to realise the facts of its bondage to rise up, ready to emancipate itself. Maybe the blame is on me for giving up when I didn't immediately find that.

        People are people after all.

        I'll talk to Joan and Fyodora. Thank you [game.player_name]. Talking to you recently has made me realise that I've spent long enough stewing in my own privileged despondency. About time I reach out and bore some others with my revolutionary prattle.

        """
    
    elif FyodoraGood == False and JoanGood == False:
    
        butcher """
        
        Not a very encouraging prognosis [game.player_name], but better to know and not waste my clearly very important time.
        """

        "Mik looks around themself in the middle of the wide, empty street, and whistles half a verse of a tune you don't recognise."

        butcher """

        Still, I don't regret coming here. Alexisgrad was killing me, and I actually do mean that, in some ways, literally. And for all its faults, this place has given me everything I could personally, if not socially, want.

        People generally accept me, even if they don't understand me. And while they may all be politically brainwashed, they're mostly kind and actually seem to care about their fellow humans.

        I may be wasting my life here, doing little more than annoying the state's appointed model citizen, but it is undoubtedly better than dying in pain as a cog in some capitalist machine back in Alexisgrad.
        """

    else:
    
        butcher """
    
        Pretty much what I thought you'd say to be honest. Could be worse, could be better. The same sentiment that makes up the ruthlessly abridged version of human history.

        Still, I don't regret coming here. Alexisgrad was killing me, and I actually do mean that, in some ways, literally. And for all its faults, this place has given me everything I could personally, if not socially, want.

        People generally accept me, even if they don't understand me. And while they may all be politically brainwashed, they're mostly kind and actually seem to care about their fellow humans.

        I may be wasting my life here, doing little more than annoying the state's appointed model citizen, but it is undoubtedly better than dying in pain as a cog in some capitalist machine back in Alexisgrad.

    Anyway, thank you for stopping by [game.player_name]. I promise you, or threaten you depending on your preference, that the next time we talk I'll bore you with the details of the ideal of the people.

    But for now I should probably go back in there and clear up that … thing which I've been working on. Hopefully the smell has had time to dissipate … or to take hold. Either way, time I got back to it.

    [textinsert]
    """

    $game.butcher.like += 1


return
