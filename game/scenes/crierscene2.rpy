label crierscene2:

"You find Nat standing by the edge of the river, near where the fishermen usually set up, staring into the dark water."

crier "Ah [game.player_name], it's good to see you, although I find myself curious as to why you're all the way out here?"

menu:
    "I was looking for you.":
        $c=16

    "Just out for a walk.":
        $c=1

    "Thought I'd do some fishing.":
        $c=18



label reevaluatecrier2:
if c==1:

    crier "Out for a walk you say? Why, I was doing a very similar thing. I've always liked going for walks all about, but now I'm usually going to this river."

    $game.crier.att += 2

    menu:

        "Why do you think that is?":
            $c=6

        "I like the river too.":
            $c=2



if c==2:

    crier "Oh aye, what do you like so much about it?"

    menu:

        "The beautiful water.":
            $c=4

        "It's safer than the forest.":
            $c=3

        "It's a useful place to fish.":
            $c=5



if c==3:

    crier """

    Oh yes, that it is. That's why I don't go in the forest. Not one for excitement and adventure and all that myself.

    But I would have thought someone like you might go, for hunting and such.
    """

    "The two of you stand in silence for a moment, watching the water."

    crier "Still, that's not the whole reason for why I come here. I used to go all around the safe parts, the fields and crags and such, and I've been doing some thinking about why that isn't so much true any more, you see?"

    $game.crier.resp -= 1#
    $game.crier.att += 1

    $c=7



if c==4:

    crier "Ah yes, there is that, isn't there. I suppose that's part of the reason why I come out here. But I've been thinking, much of it when I've been looking at this here river, that that's not really why I've been walking here more."

    $game.crier.att += 1

    $c=7



if c==5:

    crier """

    Ah, I suppose you're right. Still, that makes me sad. The fishing, that is.

    It's odd that it makes me sad, isn't it?

    But I think it does. I've been thinking, much of it when I've been looking at this here river, and I think that I've figured out something.
    """

    $game.crier.att -= 1
    $game.crier.resp += 2

    $c=7



if c==6:

    crier "Oh, well isn't that a difficult question? But you've asked, so I won't feel guilty about giving you the answer, but I will warn you that it's not particularly clear, even to me. I've been thinking, much of it when I've been looking at this here river, and I think that I've figured out something."

    $game.crier.like += 4
    $game.crier.att += 2

    $c=7



if c==7:

    crier """

    The river's both moving and it's not going to change. You see, all the other things are either boring, and I hate saying that about anything in this beautiful world but it's true, or it makes me sad.

    I used to go for walks along the crags, and those rocks and things are beautiful, but they're always the same, see? What do you think of when you think of the most beautiful mountain walk you can imagine? I'd wager you're thinking of a sunrise? Or sunset?

    Maybe a beautiful evening storm?

    But those don't happen any more. I mean storms happen, but without the light you can't hardly see their majesty.

    So it's horrible to say, but it's boring now.

    And then on the other hand, even though I don't go to the woods because they're dangerous, you have the forest and such. Or maybe a walk through the fields. But that's just sad instead, you know?

    Because with no sun, and this cold just getting worse, its dying.

    But this river, that's okay, because that's moving, flowing, changing. It still rains so the waterline still goes up and down, and I heard once that some man from one of those cities, where they pay people just to think, said \"You can't step in the same river twice.\"

    I think that was supposed to make a clever point about something, but I can still see truth in it. But on the other hand, it is the same river and that's perfectly clear. It's always in the same place, water always flowing in the same direction.

    And I know that you could tell me that that can't be so, that it can't be different all the time and also the same, but I'm told I've got my eccentricities and what's the point in having them if you can't let yourself believe in some things that other folk say can't be?

    Also I figure that the most important thing is that it makes me happy to look at the river that way. Shows that it's possible for things to change without disappearing.
    """

    menu:

        "So you like it just because it looks different sometimes?":
            $c=9

        "But it is a different river: different water, different river.":
            $c=8

        "That's a very beautiful way of looking at it.":
            $c=10

        "But what about the fish? Alderman says they're dying, and they're part of the river.":
            $c=14

        "If it makes you happy, then that's what matters.":
            $c=15



if c==8:
    if game.crier.resp > 1:
        $textinsert = ", especially someone I respect as much as you"
    else:
        $textinsert = ""
    crier """

    You see, I've thought about this, and I hate to contradict anyone[textinsert], but I'm afraid that isn't true.

    I thought about it with a field, you see? Like after you've ploughed it and seeded and fertilised it, and then reaped it, it's still the same field, but it's all different stuff, right?

    Or, or take my shirt, now I know I don't dress very nice under my crier's coat, but I take care of what I've got and I've patched this shirt a good few times, but it's still the same shirt.

    Or just take me, I mean I was knee high once, but I'm still the same man now as the boy I was then, right?

    No, I'm sorry but the river is the river. That's how we can name it.
    """

    "Nat ponders the water in silence for a moment, and then his head snaps up."

    $game.crier.resp -= 1

    $c=20



if c==9:

    crier """

    I don't think that's a very kind way to put it, I'm afraid.

    And I don't think it's true.

    I mean, take a drop of that water, we could tell an adventure about that drop.

    It'd start somewhere up in the mountains, maybe as a piece of ice or snow, melting in that thin white sun they have up there.

    Then it'd follow a little rut or something, run into other drops, and more and more until it found itself a stream.

    It'd run along beautiful mountain stones, and then past fish and between water reeds when it came downhill enough for that stuff to grow.

    It might have an insect land on it, one of those boater bugs, or it could just get out of the way before someone puts a cup in for a drink.

    And then there'll be other drops from the rain, or shaken off a wet dog, or I heard that some of it comes from underground.

    I guess my point is that all the water drops have their own story and each one is different.

    And the river is like one of those books with lots of different stories in it, except that each second all the stories are being changed.

    And if you had one of those books, and another one with all different stories in it, you'd say they were different books, wouldn't you?

    Well, that's the river. It's always different, and that's why it's always exciting.
    """

    "Nat ponders the water in silence for a moment, and then his head snaps up."

    $game.crier.resp -= 1
    $game.crier.like -= 1
    
    $c=20



if c==10:

    crier "You think?"

    "Nat glances shyly at you, but quickly looks away after your eyes meet. It's difficult to tell in the dark, but it looks like he might be blushing."

    crier "No need to condescend to me [game.player_name], I know I've got my ways and I'm happy with them being just mine."

    menu:

        "No really, it's beautiful, the way that you find the fun and the happiness in something simple.":
            $c=11

        "No really, it's beautiful, the way that you can find something that's still changing like a living thing in this time of death.":
            $c=12

        "I can respect that. We've all got our own thing.":
            $c=13



if c==11:

    crier "That's nice of you to say, but..."

    "Nat stares into the water for a long time, before turning to you slowly, a glint of sadness in his eyes."

    crier "That's nice of you to say."

    "He looks at you for a moment, then suddenly his eyes widen with surprise."

    $game.crier.like += 2
    $game.crier.resp -= 1
    $game.crier.att -= 1

    $c=20



if c==12:

    "Nat stares into the water for a long time and when he finally turns to you, there are tears in his eyes."

    crier "Yes. Yes, that's it."

    "He stares at you for a minute, a small, sad, almost embarrassed smile on his lips. It looks like he is about to say more when suddenly his eyes widen with surprise."

    $game.crier.resp += 4
    $game.crier.like += 4
    $game.crier.att += 4

    $c=20



if c==13:

    crier """

    Aye, that we do. Alderman's got his job, Stu's got his inn and I s'pose Izzy's got her project or whatever it is she's doing.

    I'm happy with my river.
    """

    "Nat nods thoughtfully to himself, then suddenly turns to you, eyes wide with surprise."

    $game.crier.resp += 4
    $game.crier.like += 4

    $c=20



if c==14:

    crier """

    Alderman's right there. I've looked here long enough in the dark that I can see the shine of the scales when the fish go by. There are fewer each day already.

    I suppose they're part of the river. But just because they die doesn't mean the river will die. If I took a cup out and drank it, that won't kill the river. Just change it.

    That being said though, it makes me sad. And there's enough to be sad about already.
    """

    "Nat turns to you, his face blank."

    crier "I've got to get back to the bell, it's almost the hour. Thank you for coming to talk, it was nice."

    "And with that he lopes off, back down the trail and towards town."

    $game.crier.like -= 1



if c==15:

    crier """

    Yeah, that's exactly the way I think about it. We've all got our things, don't we?

    Alderman's got his job, Henryk's got his inn and I s'pose Elisabeta's got her project or whatever it is she's doing.

    I'm happy with my river.
    """

    "Nat nods thoughtfully to himself, then suddenly turns to you, eyes wide with surprise."

    $game.crier.resp += 4
    $game.crier.like += 4

    $c=20



if c==16:

    crier "Oh, looking for me? Did the Alderman send you, did I forget to do something?"

    menu:

        "No no, just came for a chat.":
            $c=17



if c==17:

    "Nat smiles broadly."

    crier "Oh that's lovely. I was just looking at the river, thinking about the river. I'm spending a lot of time down here since the sun went away."

    $game.crier.like += 2

    menu:

        "Why do you think that is?":
            $c=6

        "I like the river too.":
            $c=2
    jump reevaluatecrier2



if c==18:

    crier "Fishing?"

    "Nat pulls an uncomfortable looking face."

    crier "It's good work I suppose, but not for me. I don't like the thought of the fish dying. To be fair I think it might be easier to think that way when you don't like the taste anyway. I'll let you get on with it then, don't want to disturb you."

    "Nat turns, taking a last look at the river, before beginning to move off down the path."

    $game.crier.like -= 4
    $game.crier.resp += 2

    menu:

        "Bye!":
            return

        "Wait, I wanted to talk to yo first.":
            $c=16
    jump reevaluatecrier2



if c==20:

    crier "Oh, I'd quite forgotten the time!"

    "He turns to you, an uncomplicated smile beginning to cross his face."

    crier """

    That's the first time I've forgotten the time since the sun went. I mean, not forgot, it's still there, but not just been thinking of.

    Thank you.

    But I must run, got to get to the belltower to ring the bells!
    """

    "And with that he lopes off, back down the trail and towards town."

    $game.crier.like += 2

return