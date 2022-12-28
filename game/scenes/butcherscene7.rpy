label butcherscene7: 

$game.butcher.zeal = 0
$game.crier.romance = False

"""

You are slightly surprised to see the small crowd gathered in the town square, but your curiosity is only truly piqued when you see that the Alderman, hands clasped modestly behind his back, is standing at the edge of the group, rather than leading the discussion from the centre.

That there is a leader, or at least a focal point of the group, is obvious. True, people mill and talk in little flowing clusters, but all bodies are tilted inwards, as if everyone is only half paying attention to their neighbours while they all wait for something else to happen.
"""

menu:

    "*Approach one of the townspeople and ask what is going on*.":
        $c=3

    "*Approach the Alderman and ask what is going on*.":
        $c=2

    "*Shrug and carry on with your day*.":
        $c=1



if c==1:

    "You start to move around the crowd, but you do not make it far before a loud, strong voice stops you in your tracks."

    Noah "Oy, [game.player_name]! We're fermenting the revolution, won't you come stop us?"

    """

    You turn, instinctively, as the crowd slightly parts, giving you a view of its centre: Noah and Mik. They stand slightly apart, but the way that those folk between them swivel on their feet slightly, like a compass needle sitting at the edge of two different magnetic fields, shows you that it is these two individuals whom everyone else is here to listen to.

    Noah, standing straight with his chest out and eyes sparkling, gestures you over with a well muscled arm, while Mik, slouched and slightly cowed-looking, simply nods.

    The crowd, too, gestures for you to join them, although the body language they display is just as varied. Some, with sharp movements and sweeping elbows, are clearly extending Noah's challenge, while others, some with rolling eyes, some others with a clear look of desperation, merely flick their wrists and fingers, covertly entreating you to save them.

    The group is clearly no mob, but you still sense it would be unwise to ignore whatever is happening here. So you nod and approach, the crowd reforming behind you as you join Mik and Noah in the centre.
    """

    $game.butcher.resp -= 2

    $c=4



if c==2:

    "The Alderman nods as you approach, his drawn and tired face only showing his concern through a slight knitting of his forehead."

    Alderman "Did you know that they were planning this?"

    "You shake your head and the old man gives a little shrug."

    Alderman """

    Well to be fair on them, I am not sure that they did either. I think they might be as surprised as I am. Possibly more.

    Sorry, I should explain. When Mik came to deliver their meat and pick up their supplies today, they wore a little sign around their neck. I think it said 'ask me about the social revolution.' I think they were quite surprised when people actually did. Although I do not believe that the crowd could be said to have properly formed until Noah joined them.

    There has been quite a bit of shouting since then, but I believe it is harmless enough. They're young people who are unhappy and they just want to change things, but I think that they are decent enough, both of them. I think people are excited, but I don't think they will turn violent.

    Still, if you wouldn't mind, could you go in there and make sure that everything stays civil? I would do it myself but I have heard enough of their rhetoric to know that I'm not really welcome here.
    """

    "Knowing that you do not really have a choice, and perhaps feeling curious besides, you nod and push your way through the crowd until you find yourself standing at the nexus, a point between Noah, standing straight with chest out, arms gesticulating wildly, and Mik, slouched with hands in pockets and eyes uncomfortably sliding from side to side."

    $game.alderman.like += 2

    $c=4



if c==3:

    define Woman = Character("Woman")

    "As you approach a young woman turns to you, smiling."

    Woman "Come to learn about the social revolution [game.player_name]?"

    "You clearly do a bad job of hiding your confusion and surprise, because she lets out a light laugh."

    Woman """

    It's okay, I don't really understand it all either. But it is very interesting, if a little … academic.

    Still, I think we're all pretty excited about it. It sounds like real change [game.player_name], and a chance for us to do better than we have ever done before.

    I've never really thought much about being proud of Lotosk, but if we can do what Noah, and Mik, say we can do … well, wouldn't that be something?

    Certainly something better than this.

    I'm sorry, I'm rambling. There's a lot to take in, and this is the first I'm hearing about it all, so you should probably go speak to Noah and Mik.
    """

    """

    The young woman inclines her head gently towards the centre of the mass. As you follow the line she indicates, your eyes catch on the faces of the other people in the crowd. Not all of them appear as enthralled as the woman, but most do.

    Nevertheless, there is tension in the air. You do not sense that there will be violence, but your arrival has changed the dynamic. The people around you are looking at you now, some with a challenge, some with a plea.

    It would be a mistake, you think, to leave this be.

    So you smile to the woman and push your way gently through the press of people until you find yourself standing at the nexus, a point between Noah, standing straight with chest out, arms gesticulating wildly, and Mik, slouched with hands in pockets and eyes uncomfortably sliding from side to side.

    """

    #JE {Very slight morale increase}

    $c=4



if c==4:

    Noah "Ah [game.player_name], how good of you to join us! We were just discussing the social revolution. You've talked with Mik about it a lot haven't you? What's your opinion on the state then? You agree that we should tear it down?"

    menu:

        "The state has its dangers and disadvantages, but I'm yet to be convinced that anarchy would be better.":
            $c=5

        "Without a state there is no order or protection. If we want to stay safe, we need a state to keep us safe.":
            $c=6

        "States cannot help but breed reactionism and corruption. Any state that appears sound today will not remain so for long. Anarchy is the only solution.":
            $c=7



if c==5:

    if game.butcher.resp < 26:
        $textinsert = "their eyes rolling and a look of exaggerated exhaustion on their features"
    else:
        $textinsert = "a look of concern on their features"

    "Noah purses his lips, while the crowd around you mumbles, no consensus being strong enough to generate outrage at your mild sentiment."

    Noah """

    A perfectly understandable response, especially from someone who works for the state. A lot of people, good intelligent people, will be scared. But we've all got to be strong and confident! Even [game.player_name] sees that the state is wrong, and {i}that's{/i} the important thing!

    If we're good people and we're the ones who set up the world after the revolution, then there shouldn't be anything to worry about if we go beat the snot out of those fat cats in Alexisgrad!
    """

    "While Noah speaks Mik stares at you, [textinsert], but as soon as Noah is finished their face takes on a neutral cast as they address the crowd."

    butcher """

    I can't tell you what the world will look like after the states fall. No-one can. But if we all build the new world, if we follow the ideal of the people as it drives equally through all of us, we will create a world that is just, free and equal for all.
    """

    "There is a pause, Mik clearly looking like they have more they want to say, but it eventually becomes clear, to them and everyone else, that they will say no more, and the attention slides back to you and Noah."

    Noah "You'll grow some nerve with time, [game.player_name]. You'd better. But if you're going to be limp when it comes to your opinion on the state, what's your take on the bourgeoisie?"

    if game.butcher.resp > 25:
        $game.butcher.zeal -= 1
    else:
        $game.butcher.zeal += 1

    $game.butcher.resp -= 2

    menu:

        "As they are, the bourgeoisie are definitely a problem, but I think there are better ways of dealing with that problem than abolishing private property.":
            $c=10

        "The bourgeoisie? You mean the hard-working people pushing humanity towards a golden age of advancement and liberalism?":
            $c=8

        "The bourgeoisie are unrepentant, undisguised slave drivers. They are a true evil.":
            $c=9



if c==6:

    if game.butcher.resp < 26:
        $textinsert = "bored contempt"
    else:
        $textinsert = "sadness"

    "Before anyone else can respond, Noah lets out a hearty 'boo!'."

    Noah """

    Oh come the fuck on [game.player_name]! That's bullshit and you know it! You really so keen on your job and your own importance that you'd happily lie to all of us?

    If I went over and punched Mik here in the face, what would you actually do about it? You can't do shit, or at least no more than anyone else here could do. The Alderman could do even less.

    No, the sooner we stop listening to stuck up twats who think that they're important just because someone else who was told that they're important told them that they're important the better off we'll be.

    Still, prefer to be listening to your bullshit. At least you're useless. It's the cunts in Alexisgrad who back up their meaningless 'power' with guns who are the real fucking problem.

    A problem that no-one else is going to fix, right everyone‽
    """

    "A small but energetic cheer goes up from certain elements of the crowd, while Mik looks away from you, a look of [textinsert] giving way to a neutral expression as they address the crowd."

    butcher "The 'safety' that the state promises is a sham. A society united by the ideal of the people won't need 'security'. There won't be any reason to fight or steal or murder when all know, truly and rationally, that they have as much freedom, justice and equality as they can ever get."

    Noah """

    Hear hear! Greed doesn't look good on you [game.player_name], especially when it's stupid greed. We'll all be better off once we've kicked those aristocrats and senators down.

    Talking of the bastards who are ruining everything, I presume you'll be defending the bourgeoisie too [game.player_name]?
    """

    if game.butcher.resp > 25:
        $game.butcher.zeal += 1
    else:
        $game.butcher.zeal -= 1

    $game.butcher.like -= 4

    menu:

        "As they are, the bourgeoisie are definitely a problem, but I think there are better ways of dealing with that problem than abolishing private property.":
            $c=10

        "The bourgeoisie? You mean the hard-working people pushing humanity towards a golden age of advancement and liberalism?":
            $c=8

        "The bourgeoisie are unrepentant, undisguised slave drivers. They are a true evil.":
            $c=9



if c==7:

    Noah "Aye, there's a good revolutionary! Everyone, a big clap for [game.player_name]!"

    "A small but energetic cheer goes up from certain elements of the crowd. You catch Mik out of the corner of your eye looking sidelong at Noah, but when they notice you they turn to you and smile thinly, badly disguising the look of worry in their eyes."

    Noah """

    [game.player_name] works for the Alderman but is still out here championing the cause! Could you want a better endorsement than that?

    We're really not too bad here in Lotosk, are we? Even your boss, [game.player_name], has laid some pretty good socialist groundwork. I mean it needs to be in the hands of the people, but still, we are one step ahead of the rest of the Republic. We'll do great things, won't we?
    """

    "Another cheer, after which Mik, clearly unable to contain themself any longer, interjects."

    butcher """

    Don't get too proud. There is a great deal of work that still needs to be done here. You can admire the Alderman's socialist methods all you want, but they're still statist. We have to throw off the chains of the state, not just put them aside so that they can be snapped on again later.

    Social, not political, revolution. Remember that.
    """

    "Noah nods vigorously, and seeing this, the crowd follows suit."

    Noah "Aye, and remember, it's not just the state. It's the bourgeoisie as well. You just as revolutionary when it comes to them, right [game.player_name]?"

    if game.butcher.resp > 25:
        $game.butcher.zeal += 2
    else:
        $game.butcher.zeal += 1

    $game.butcher.like += 4

    menu:

        "As they are, the bourgeoisie are definitely a problem, but I think there are better ways of dealing with that problem than abolishing private property.":
            $c=10

        "The bourgeoisie? You mean the hard-working people pushing humanity towards a golden age of advancement and liberalism?":
            $c=8

        "The bourgeoisie are unrepentant, undisguised slave drivers. They are a true evil.":
            $c=9



if c==8:

    if game.butcher.resp < 26:
        $textinsert = "while Mik shakes their head at you."
    else:
        $textinsert = "but Mik is looking at you, sadness clear in their eyes."

    "Noah makes a big show of reeling back, widening his eyes and clutching the side of his head."

    Noah """

    I'm sorry [game.player_name], I'd pretend I'd misheard but I worry that if you say it again I might catch stupid..

    The {i}bourgeoisie{/i} are the ones saving us? The people who did nothing but be born into wealth, the ones who do nothing but sit on their arses all day while we make money for them? They're the ones pushing us towards a golden age?

    What have you been smoking [game.player_name]? The state may be a repressive evil, but at least they do stuff. The bourgeoisie just lie on their fat stomachs and suck the life out of everything around them. There is no, and I mean no, argument to defend them.

    They're selfish, lazy pricks, is what I'm saying. Now if that doesn't sound familiar to you all, that's because we're lucky. I mean we've got our fair share of landowners and fat cat merchants up here, but Lotosk doesn't have it nearly as bad as those down in Alexisgrad.

    There's a lot Lotosk could teach them.
    """

    butcher """

    The bourgeoisie are indeed indefensible, but it would be a mistake to forget that they are an inevitable outcome of any system based on private property. If you allow wealth to flow freely, it will accumulate in the hands of the few.

    The bourgeoisie must fall, but so must the system that created it.
    """

    "Noah leads a small cheer, [textinsert]"

    if game.butcher.resp > 25:
        $game.butcher.zeal -= 2
    else:
        $game.butcher.zeal -= 1

    $game.butcher.like -= 4

    $c=11



if c==9:

    Noah """

    Now that's what I'm talking about!

    The state may be a repressive evil, but at least they do stuff. The bourgeoisie just lie on their fat stomachs and suck the life out of everything and everyone around them.

    They're selfish, lazy pricks, is what I'm saying. Now if that doesn't sound familiar to you all, that's because we're lucky. I mean we've got our fair share of landowners and fat cat merchants up here, but Lotosk doesn't have it nearly as bad as those down in Alexisgrad.

    There's a lot Lotosk could teach them.
    """

    butcher """

    Let's not forget that the work is far from done here. It would be a mistake to forget that the bourgeois are an inevitable outcome of any system based on private property. If you allow wealth to flow freely, it will accumulate in the hands of the few.

    The bourgeoisie must fall, but so must the system that created it.
    """

    Noah "Yeah, of course. But it's important to stop and acknowledge when things are going well, isn't it Mik?"

    "Mik looks as if 'going well' is a concept entirely foreign to them, but after a short hesitation they nod."

    if game.butcher.resp > 25:
        $game.butcher.zeal += 2
    else:
        $game.butcher.zeal += 1

    $game.butcher.like += 4

    $c=11



if c==10:

    Noah """

    Well that's an understatement, isn't it? I mean I'm glad you're getting there, but the bourgeoisie is more than a 'problem'.

    They're like, I don't know, one of those things, leeches, they're like leeches!

    The state may be a repressive evil, but at least they do stuff. The bourgeoisie just lie on their fat stomachs and suck the life out of everything around them. There is no, and I mean no, argument to defend them.

    They're selfish, lazy pricks, is what I'm saying. Now if that doesn't sound familiar to you all, that's because we're lucky. I mean we've got our fair share of landowners and fat cat merchants up here, but Lotosk doesn't have it nearly as bad as those down in Alexisgrad.

    There's a lot Lotosk could teach them.
    """

    butcher """

    Noah, unlike [game.player_name], you're not wrong. But you need to deal with the whole point. [game.player_name]'s mistake is to forget that the bourgeoisie is an inevitable outcome of any system based on private property. If you allow wealth to flow freely, it will accumulate in the hands of the few.

    The bourgeoisie must fall, but so must the system that created it.
    """

    "Noah nods vigorously, not very subtly hiding the bruising his ego just took."

    if game.butcher.resp > 25:
        $game.butcher.zeal += 1
    else:
        $game.butcher.zeal -= 1

    $game.butcher.resp -= 2

    $c=11



if c==11:

    """

    Noah opens his mouth, ready to say more, when the town bell cuts him off.

    There is a moment of silence while the revolutionaries plan their next move. However, they never get the chance to execute it, because a small, purposeful cough makes everyone turn.

    The Alderman stands hunched at the edge of the crowd. He does not say anything, but as the final ring echoes through the streets, everyone remembers that it's time for the next distribution. Soon the square will be filled with cold, hungry Lotoskns, each one just trying to get their next meal.
    """

    Noah """

    We've had a good talk today. But there's much more to talk about, I'm sure much more for Mik to teach us. We will gather again soon, yes?
    """

    """

    A general murmur of assent goes through the crowd as it breaks apart, but not without a few shouts of  'down with the state, down with private capital!' and 'liberty and equality!'.

    Noah retreats to the inn and the Alderman shuffles off to assist with the handing out of furs, leaving you and Mik alone.
    """

    menu:

        "I think that went well.":
            $c=12

        "What the hell are you doing trying to start your revolution at a time like this!":
            $c=13

        "What was that all about?":
            $c=14



if c==12:

    $game.butcher.like += 2

    butcher """

    Did it?

    It didn't go quite how I had envisioned, but then what does? I had intended something a little more edifying, a little less … patriotic.

    Noah seems to have some interesting ideas when it comes to Lotosk's role in the coming revolution.

    Oh, I don't know. I'm not used to feeling conflicted.

    It's probably a good sign that I can feel conflicted though.
    """

    if game.butcher.like > 22:

        "Mik gives you a large, honest smile."

    butcher """

    Well, as you say, it probably did go well. I'm not as good at seeing the progress as I am at picking out the faults.

    Still, I think I'll have to have a think about what happened here today.
    """

    $mikattractionmatrix = (game.crier.resp + game.crier.like*2 + game.crier.att*4)/7
    if mikattractionmatrix > 15:
        
        butcher """
        
        I'll bid you farewell then [game.player_name]. It was good of you to join us.

        See you at the next one, I suppose.
        """

        return

    else:

        butcher "But I can do that later. What are you doing now [game.player_name]?"

        menu:

            "Just getting on with my day.":
                $c=15

            "Nothing more important than getting a drink with you.":
                $c=16



if c==13:

    "Mik, apparently completely unfazed raises an eyebrow."

    butcher """

    I presume you'd prefer for me to wait until we are all dead? No, as I have said before, what better time to start a revolution than now, when the people can truly see how little they have to lose?

    True, I had expected today to be more educational and less … actionable. Certainly less patriotic. But if you're waiting me to apologise for what happened, then I'll tell you that there are better ways to spend the rest of your life.

    But thank you for your paternalistic concern. It is always nice to know that the instruments of the state are ready and waiting to stand and yell after the point of concern has already been and gone.

    Take care of yourself [game.player_name]. I really don't know what we'd all do without you.
    """

    $game.butcher.like -= 2
    $game.butcher.resp -= 2

    return



if c==14:

    $game.butcher.att += 4

    "Mik smiles."

    butcher """

    I will be honest [game.player_name], I'm not entirely sure. I had intended something a little more edifying a little less … patriotic.

    Noah seems to have some interesting ideas when it comes to Lotosk's role in the coming revolution.

    Oh, I don't know. I'm not used to feeling conflicted.

    It's probably a good sign that I can feel conflicted though.
    """

    if game.butcher.like > 22:

        "Mik gives you a large, honest smile."

    butcher """

    I think I'll have to do a lot of thinking about what happened here today. It didn't taste quite right. I don't think that it was as delicate as it needed to be.

    """

    $mikattractionmatrix = (game.crier.resp + game.crier.like*2 + game.crier.att*4)/7
    if mikattractionmatrix > 15:
        
        butcher """
        
        I'll bid you farewell then [game.player_name]. It was good of you to join us.

        See you at the next one, I suppose.
        """

        return

    else:

        butcher "But I can do that later. What are you doing now [game.player_name]?"

        menu:

            "Just getting on with my day.":
                $c=15

            "Nothing more important than getting a drink with you.":
                $c=16



if c==15:

    butcher "Got a long day of statist oppression planned, have you? Well, don't let me stand in your way."

    if game.butcher.like > 22:
        
        "Mik smiles at you."

        butcher """

        In all seriousness though [game.player_name], I probably should thank you for what you're doing. I think that the office that you hold is a sham produced and supported by a repugnant system, but you, personally?

        I suppose you're doing alright.
        """

        "Mik winks, looks you up and down, sighs, shrugs, smiles again, and then walks off."
        
    else:
        "Mik nods once, thrusts their hands into their pockets, and walks away."

    return



if c==16:

    butcher "As friends?"

    menu:

        "Or more…?":
            $c=17

        "As friends.":
            $c=18

        "As friendly rivals.":
            $c=19



if c==17:

    "Mik nods slowly."

    butcher """

    Sure, why not? I could go for a pint and a fuck. If you're as good in bed as you are in debate, I imagine we could have a good time.

    Sorry I'm being flippant. I like you. You're a fun person to be around.

    And I like that you like me.

    I'm not seeing anyone else at the moment, but I can't promise that won't change. Hope that won't be a problem. Don't know if you were looking for something serious enough for that to matter either way.

    But yeah. I'll not turn this into a debate. Let's go get a drink. Might be nice having a chat, now that we know we actually like each other.

    And then, well, we'll see where the night leads, won't we?
    """

    $game.crier.romance = True
    
    $game.butcher.like += 4

    return



if c==18:

    "Mik nods slowly, as if they are trying to work past an emotional hiccup."

    butcher """

    Alright. It might be nice having a chat, now that we know we actually like each other.

    Lead the way then. I think I've earned the right to take the back seat for the rest of the day.
    """

    $game.butcher.like += 4

    return




if c==19:

    "Mik smiles slyly."

    butcher """

    Oh how exhausting. I've just finished all that and you want to go have a sniping contest at the inn?

    But I'd be a flaming hypocrite if I denied you now. So go on, lead the way to the bar! But if you win this argument, we'll put it down to my tiredness, okay?
    """

    $game.butcher.like += 2
    $game.butcher.resp += 2
    $game.butcher.att += 2


return
