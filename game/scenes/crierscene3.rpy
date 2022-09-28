label crierscene3: 

if game.playerbackground == "woodsman":
    $textinsert = ", the sound a trainee hunter makes when they are trying, and failing, to be subtle,"
else:
    $textinsert = ""

"""

It takes you some time to find Nat. You began searching not long after the bells last rung, and had therefore assumed that he would be somewhere near the bell tower, on his usual rounds. It was only after you assumed you had missed him, and checked by the river, that you thought to check the bell tower itself.

The moment you push the old door aside, you know he is there. His voice echoes through the large, cold, damp, and, surprisingly, clean space. He's talking in a little whisper, his words a constant stream, pushed through both the exhales and inhales of his breath.

The door shuts behind you with a loud click and the muttering instantly stops. There is silence for a moment, your eyes adjusting to the darkness tarnished only by a small square of starlight high, high above you.

Then there's a shuffling sound[textinsert] and you hear:
"""

crier """

Ah, it's you. Thought someone might be sneaking up on me, although now that I think, I can't see any reason why any of the folks round here might do that.

Old habits, you know how it goes.

What brings you here anyway [game.player_name]? People don't usually like coming here, except maybe back in the old days when you could see some of the view from up top.
"""

menu:

    "What do you mean by old habits?":
        $c=1

    "Here to check on you. Disappointed to see that you aren't on your rounds.":
        $c=3

    "Just here to see you Nat, see how you are.":
        $c=2



if c==1:

    crier """

    Oh, you know. People haven't always been kind. I'm sure there's a reason, but I've never really been able to figure it out. Been told it's because I'm different, but as far as I can tell everyone is different, so it can't be that.

    But things have been better since the others left with Cynthia and Edward. Most of those who seemed to dislike me went with them.

    It's not been perfect though. Just better.
    """

    $game.crier.like += 2

    $c=4



if c==2:

    if game.crier.like > 4:
        $textinsert = "Actually that's one of those lies I'm afraid [game.player_name]. One of the white ones."
    else:
        $textinsert = "Actually [game.player_name], you're an important person, so I should tell you the truth."

    crier "Oh I'm alright [game.player_name], I'm alright."

    "There is a brief pause, Nat clearly on the precipice of saying something."

    crier "[textinsert]"

    $c=4



if c==3:

    crier """

    Oh, I'm sorry [game.player_name]. But I have already delivered all of the Alderman's messages today, and I'm keeping the bells going. But I suppose it would be good if I were out there just making sure people don't forget things.

    It's just that I…
    """

    $c=4



if c==4:
    #VERY IMPORTANT!!!!  THIS SHOULDN'T BE LIKE, IT SHOULD BE ABOVE A THRESHOLD OF FOOD SUPPLIES!!!!!!!!!!!!!!!!!  ALSO WHEN FIX DELETE POOPOO...
    if game.crier.like > 4:
        $textinsert = "up, and they'll ask if it wouldn't be wiser to stockpile it for the hard times PooPoo"
    else:
        $textinsert = "down, and they'll ask what they are supposed to do to feed themselves PooPoo"

    crier """

    I've not been feeling too good recently. In my head, that is.

    Oh don't worry, I'm still sure of the count. But I've been confused about other things. Or maybe I'm less confused.
    """

    "Nat smiles to himself."

    crier """

    See? Confusion all around.

    I don't know what it is. Maybe it's the dark, maybe it's the way everyone seems to be doing more thinking now, they're always talking about it down at the inn.

    But I've been wondering about our Alderman, and why he has me doing what I'm doing.

    I mean, I know why I do the time. I've got the count. I don't feel bad about saying I'm better at that than anyone else.

    But the crier...ing, I don't know, I always get all these questions from folk about the things that I'm telling them and I don't ever know the answers, I just know what the Alderman told me to say.

    Like, I'll say that the food ration is [textinsert] and I always just have to say 'ask the Alderman', and they'll shout that they were asking me and I should use my common sense. But I try and I just don't know.

    I just wonder why he doesn't get someone with more of this common sense to do it. Someone who can answer all these questions.
    """

    menu:

        "You're right, that would be better, but the Alderman doesn't want to waste anyone else's time with your job.":
            $c=5

        "I agree, but the Alderman seems to value you, for some reason.":
            $c=6

        "The Alderman values you because of your special skills. You can memorise exactly what he wants you to memories. The Alderman doesn't want you to answer those questions, he can do that himself if he wants to.":
            $c=7

        "I don't think it matters if you can't answer those questions. You're kind, loyal and hard working. That's what I think matters.":
            $c=8



if c==5:

    crier "Oh, okay. I suppose that makes sense. Everyone else can do more important work than me anyway. Our Alderman is very wise, isn't he?"

    "Nat turns away from you suddenly, and you hear a single, loud sniff. When he speaks again, his voice sounds slightly choked."

    crier """

    Why doesn't he have Elena do my job then? Everyone says she's a very intelligent lady, and she's not doing anything else for the town at the moment.

    I'm sorry, I don't want to speak ill of her, but it is true. Unless she's working on something I don't know about of course.
    """

    $game.crier.like -= 1
    #{Relationship loss between Nat and the Alderman}

    menu:

        "Elena might be the one exception. She's cruel and unlikable, she'd be worse at your job than you.":
            $c=9

        "Elena couldn't do it, her main priority is to her daughters. As a single mother, I think that is as it should be.":
            $c=10



if c==6:

    crier """

    Oh. I understand. Our Alderman is a very kind man, or he's always been kind to me at least.

    I don't think I thank him enough for his kindness. I don't think that I'm too proud to be grateful for charity.
    """

    "Nat turns away from you suddenly, and you hear a single, loud sniff. When he speaks again, his voice sounds slightly choked."

    crier """

    But you're probably right, someone better would be better. Do you think Elisabeta? She's intelligent, and she's always liked talking to people more than me. Do you think you'd pick her?
    """

    $game.crier.like -= 4 
    #{Relationship gain between Nat and the Alderman}

    menu:

        "No, I wouldn't. She's too self interested, or at least only interested in her own things.":
            $c=11

        "Yes, she cares about the fate of this town a great deal, and she's very good at communicating complex ideas to people.":
            $c=12



if c==7:

    crier """

    I suppose you're right. I always forget that I've got skills other than the count. I suppose it's all part of the same memory thing, isn't it?

    Sorry, I don't know why you should know, no one seems to know. Not even Fyodora, and she's a doctor.

    You were a child with her, weren't you? I mean, you are about the same age. I don't know her too well, she's always very kind to me but she's always a bit...I don't know. I've heard the word ‘intense', that might be what I'm looking for.
    """

    $game.crier.like += 2  
    #{Relationship gain between Nat and the Alderman}

    menu:

        "Fyodora is unrelentingly caring. If she comes across as intense, it is only because of how dedicated she is to always doing the right thing.":
            $c=13

        "Fyodora has all the weaknesses of a sentimentalist and all the weaknesses of an intellectual. She's intense because she's always trying to analyse you, while at the same time being completely caught up in her own unexamined emotions.":
            $c=14



if c==8:

    crier "You're very nice."

    "You did not know that you could hear a blush, but standing here in the dark, you find out that you can."

    crier """

    But I don't know how much I am any of those things. Those are always the words I hear people say about Henryk. He does seem like a very nice man, of course. Always smiles and says that if I ever want to talk than I can talk to him, but I never really have. Don't rightly know why.
    """

    $game.crier.like += 4
    $game.crier.att += 4

    menu:

        "You should talk to him. Not only does he really listen, and not only does he really care, he also thinks about what you tell him, and he replies from the heart.":
            $c=15

        "Henryk says he cares, but all he really wants is a chance to preach at you. Don't waste your time with him.":
            $c=16



if c==9:

    crier """

    Oh, is that right? I don't like thinking badly of people, but that is what I hear around the town.

    I hate thinking that it might be true that some people don't have goodness in them.
    """

    #{Slight relationship loss between Elena and Nat}

    $c=17



if c==10:

    crier """

    Is that so? I suppose those girls have had a hard enough life already. A good thing for them to have a mother like that then.

    I suppose it's just that people don't like it when other people have the courage to do things that they wish they'd have the courage to do themselves.
    """

    #{Slight relationship gain between Elena and Nat}

    $c=17



if c==11:

    crier """

    Oh, is that right? I've always thought that being a good person mostly came from caring about other people.

    But, sorry, I suppose you were more talking about the job, and how you have to be able to really concentrate on it.
    """

    #{Slight relationship loss between Elisabeta and Nat}

    $c=17



if c==12:

    crier """

    Yes, that's what I thought too. I don't quite understand all she's been saying since the sun disappeared, but she's certainly putting a lot of effort into making people feel like this is a beginning instead of an ending.
    """

    #{Slight relationship gain between Elisabeta and Nat}

    $c=17



if c==13:

    crier """

    It must be a difficult life, always caring about people so much. I can see why she's like what she is.

    It makes me glad she's our doctor though. I think that's one of those jobs where the feelings are just as important as the doings, if you know what I mean.
    """

    #{Slight relationship gain between Fyodora and Nat}

    $c=17



if c==14:

    crier "Sounds like she's trying to be a good person, but doesn't quite know how. I sometimes feel like that's all of us, except maybe a few here and there, and I'm sorry to say it but I think they were just lucky enough to be born good. Or born knowing how to be good or something."

    #{Slight relationship loss between Fyodora and Nat}

    $c=17



if c==15:

    crier "Aye then [game.player_name], I might just do that. I'm never too sure about talking things through with people, always worried that I'll be wasting their time, but if Henryk's offered and if he's as good as you say he is, which I don't doubt for a second of course [game.player_name], then I should take him up on his word."

    #{Slight relationship gain between Henryk and Nat}

    $c=17



if c==16:

    crier """

    Oh that is a shame to hear.

    I really do hate it when that happens. It took me a long time to realise that some good acts can actually be bad. And now that I know it I hate it. I'm not sure that you can lie about anything more than pretending that something is good when it's not.
    """

    #{Slight relationship loss between Henryk and Nat}

    $c=17



if c==17:

    if game.crier.like > 4:
        $textinsert = "It's been very nice talking to you though [game.player_name]. I do hope you come and find me again some time."
    else:
        $textinsert = "Look forward to seeing you again next time though [game.player_name]."

    "Suddenly the shadowy outline of Nat, which is all that your eyes can give you in the gloom, springs up from its slouch."

    crier """

    Ah, sorry [game.player_name], but you better get out of here. It takes me a minute or two to get up to the bells and then a little longer to get them ready for ringing, but you don't want to be in here when they go. The ringing always stays longer than the bells keep moving, if you know what I mean by that.

    After that I should get back to my rounds. Better safe than sorry with that.

    [textinsert]
    """

return
