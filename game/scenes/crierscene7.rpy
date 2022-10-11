label crierscene7: 

if game.crier.att > 0 or game.crier.like > 0:
    $textinsert = "surprised"
else:
    $textinsert = "disappointed"

"You find Nat sitting alone in his tower. When you push the heavy wooden door open he rises quickly from the old chair he had been sitting on, but looks [textinsert] when he sees that it is you."

crier "Oh, [game.player_name], I was not expecting you. I mean, maybe I should say that I was expecting [game.creature_name] rather than you, or anyone else for that matter."

menu:

    "Good, the monster has finally left then has it?":
        $c=1

    "Oh no, is she missing!":
        $c=2

    "Where did she go?":
        $c=3



if c==1:

    "Nat pulls a face as if he has just bitten into something tart, but otherwise ignores you."

    $game.crier.att -= 4
    $game.crier.like -= 4

    $c=3



if c==2:

    crier "Oh no [game.player_name], nothing like that, don't you worry!"

    $game.crier.att += 4
    $game.crier.like += 4

    $c=3



if c==3:

    crier """

    [game.creature_name]'s been acting a little oddly for the last few days.

    Or is it just that she was acting a little strange a few days ago, and what she's doing now is normal? It's been such a short time, all in all, that maybe saying something is ‘normal' is a bit, well maybe ‘forward' is the word, but I've always heard that about when you speak to someone you like, like like like, and that's not what I mean now.

    But anyway, she wasn't feeling too good. I could see it. Her tail was always wrapped around between her legs, and she'd be...saggy with her front legs, like usually she always used to keep them straight like a leg but then they were all bent and she'd lean forward you know, with her chest bit almost scraping on the ground. And she'd be moving really slowly and all.

    It took me a while to realise what was wrong, because I think she'd been looking at the door a lot but it's difficult to tell what she's looking at, given that I think she can see all around her.

    But eventually I understood. She wanted to go out. And not just for play either.

    I have to tell you [game.player_name], I didn't think I'd need bravery to just let her out of the door, but I did. I mean, we have so much fun together, but looking at her, slinking I think, around, I really didn't know if she would come back.

    I think she could tell that I was nervous. I think I must have looked like her, all cautious as I let her out.

    But she was back after just forty-seven minutes, and she brought me a, well...I think she thought it was a gift. She'd carried it with her hand all the way back here from the woods, which must have been uncomfortable, although maybe that's just me imagining holding something with my tongue, but I suppose that's very different.

    Anyway, it showed that she'd been thinking about me. But it was an odd gift [game.player_name]. It's the kind of thing that cats bring home I think. Surprised me, that she would bring me something so strange.

    Let me show you. I haven't wanted her to think that I would throw it away, although she hasn't seemed to think about it again since she brought it here.
    """

    """

    Nat scampers a little way up the tower, and returns with something held between two fingers.

    Even if it hadn't been so dark in the tower, you think it would have taken you a moment or two to figure out what it is.

    At first you think that the object is two dimensional, a patch of fabric, but as Nat moves you see parts near the bottom bulge and shift like something is being jostled inside it as Nat walks.

    That makes you think that it is some sort of thin bag, but as your eyes search for some kind of opening, you notice the ears. Long and pointed, they are the only part of the thing that retains their original shape.

    The rest is flattened and shapeless. Like a pocket filled with sticks. All dried up from the inside. Even its wet, scared eyes are gone.

    The husk of a rabbit, still given its only semblance of three dimensional shape by its bones, all of which must lie in a heap where gravity left them. Even the skull has slipped down the neck and pushes the thin skin of the animals stomach taut around its eye holes.
    """

    crier """

    I suppose that she must have realised that I eat the flesh of animals, but not quite understood. Maybe she thought we could share this?

    I don't know if she was disappointed when I just put it gently upstairs. But she hasn't brought another one of her finished meals back since.
    """

    menu:

        "What did she do to it?":
            $c=5

        "Why on earth have you kept it?":
            $c=6

        "I think it's lovely, that she was thinking of you even while she was hunting.":
            $c=7

        "I'm sorry, but that is disgusting.":
            $c=4



if c==4:

    "Nat looks at the rabbit, then looks at you and then, surprisingly, he smiles."

    crier "It is that, very much so. I'm going to put it back upstairs."

    $game.crier.like += 2

    $c=8



if c==5:

    "Nat pulls a face, sucking in his lower lip and raising his eyebrows."

    crier """

    I saw her do it once. It's not a nice thing to watch. She catches them with one of her front leg-things, sort of strangles them with it, and then once it's gone crack, she puts it in her, erm, hand and then sticks her nose into it.

    And then I suppose she, um, sucks.
    """

    "There is a moment of silence. Nat looks slowly down at the thing he is holding at arms length."

    crier "I think I'll go put this back upstairs."

    $game.crier.resp += 2

    $c=8



if c==6:

    crier """

    Because [game.creature_name] brought it to me, of course. It was a gift, I think. I mean I don't fully know, but I think it was. Either way, I would feel bad if I just threw it out. Well, I might have to when it starts to rot, but it's pretty dry so I'm not sure that'll happen too soon.

    Anyway, if you don't like it I'll go put it back.
    """

    $game.crier.like -= 1

    $c=8



if c==7:

    "Nat smiles at you, and then smiles at the...rabbit."

    crier "I hadn't thought of it that way [game.player_name]. You're awful clever. I was a little worried when she brought it to me, because it's not at all the kind of thing I would want and I had hoped she'd know that, but maybe you're right and she was just trying to tell me that she was thinking of me."

    "There's a short pause while Nat continues to admire his gift."

    crier "I'll go put it back upstairs now. Want it to last as long as possible now that I know how thoughtful it was."

    $game.crier.resp += 2
    $game.crier.like += 2

    $c=8



if c==8:

    "Nat goes back upstairs, but when he comes back he's looking sad."

    crier """
    
    She's been out a couple of times since she brought me that. But each time she's been out for longer than the last.

    Trust me, I know. Smile

    It's sad [game.player_name]. I haven't been with her that long, but already when she's gone I feel all empty. It's difficult, remembering how I was happy before, when I didn't have a friend.
    """

    "Nat looks up, bravely meeting your eyes and underlining the significance of what he just said."

    crier """

    I suppose I have my work. And the Alderman tries to keep me busy. I think he can tell, and he's always kind. But I suddenly find everything's more empty.

    Like, [game.player_name], I used to be able to walk by the river, and that was lovely and fun and always made me think happy thoughts. But now when I do it, I just think how much nicer it would be with her.

    I think I need to find something else [game.player_name]. For when she's gone. And maybe, you know, when she's gone.

    I don't know. I don't usually get worried about things. But having her, now I'm suddenly worried about things like that.

    But no, I don't want to talk about that. I don't want help with that because I don't want to think about it.

    But what about that other thing, you know, the something else I can do that isn't work or spending time with [game.creature_name]?

    Can you think of anything?
    """

    menu:

        "You could try and make some friends. Some human friends.":
            $c=9

        "You're the first person to be friends with something like [game.creature_name]. Why don't you write about it?":
            $c=10

        "You could join Elisabeta's group." if game.landowner.scene > 4:
            $c=11

        "I think the important thing is to try to learn to be happy within your own mind, rather than feeling you have to distract yourself. Maybe speak to Henryk?":
            $c=12

        "I'd like it, Nat, if you spent time with me. You know, like friends. But maybe, if you wanted, as more than friends?":
            $natattractionmatrix = (game.crier.resp + game.crier.like*2 + game.crier.att*4)/7
            if natattractionmatrix > 17:
                $c=14
            else:
                $c=15



if c==9:

    "Nat slowly shakes his head."

    crier """

    I've been trying that one my whole life. There isn't really anyone around here who is mean to me any more, but still, I never got the feeling that many people want to be my friend.

    I've always been okay with that, well, I tell a lie, but I've been okay with that for a long time and it would be sad if I suddenly went backwards and started feeling sad about it again now.

    It's a nice suggestion [game.player_name], but it's not for me. It's a skill, making friends. I've learnt that much. And I know you can work at skills, but I've never found myself being very good at learning things I can't do naturally.
    """

    $c=13



if c==10:

    "Nat seems to think for a long time."

    crier """

    It's a very noble suggestion [game.player_name]. I do like the idea that I'd be part of science. I suppose it's something I've thought about a bit before, what with my gift and all.

    But I don't think this is right. I don't think I'm good enough with words, especially written words. I'm not sure I'd be able to write the kind of thing that other people could learn from, or use.

    There are all sorts of rules for what you can write for science aren't there? Elisabeta's always talking about the ‘scientific method', and I don't think I'll be able to learn all that, as well as doing all of the writing stuff.

    It's a very clever suggestion though [game.player_name].
    """

    $game.crier.resp += 2

    $c=13



if c==11:

    "Nat shakes his head emphatically."

    crier """

    No [game.player_name], I shan't be doing that.

    Elisabeta is a very nice young woman, and I think she's very smart, but I don't think I want to get involved with a new god and all that.

    Like I heard that she said that we need to teach it things about who we are and our history and all and I'm barely able to teach myself all those things. I don't think I want the responsibility of teaching a god all of that. Smile
    """

    #JE{Very slight relationship gain between Nat and Elisabeta}
    $game.crier.resp += 2

    $c=13



if c==12:

    "Nat thinks for a long time, and as he does so he begins to nod, very slowly and subtly at first, but gradually picking up speed and momentum."

    crier """

    That sounds like one of those truly wise things [game.player_name]. \"Try to learn to be happy within your own mind, rather than feeling you have to distract yourself.\"

    I'm not too good at long term thinking. Ironic really, since I know more about time than anyone else here. But that does sound like a very good long term plan.

    I suppose that before [game.creature_name] came along I was happy with myself.

    Yes, that's it. I've just forgotten that. I've usually got a real good memory, but nothing is perfect.

    You say I should speak to Henryk? I might do just that. But I might do some private thinking first. I think I was there before, hopefully I can remember how to get back there again.

    But if not I'll be sure to give Henryk a visit. Try to think of some way to talk about all of this without mentioning [game.creature_name]…

    Thanks [game.player_name], I think you've been a real help.

    I know it's rude, after you've helped me so much, but I think I'd like to practice being alone now. [game.creature_name] might be back soon and I won't get any chance again after that.
    """

    #JE{Very slight relationship gain between Nat and Henryk}

    $game.crier.resp += 2
    $game.crier.like += 2
    $game.crier.romance = False

    return



if c==13:

    "Nat closes his eyes, and is clearly lost deep in thought for some time. It is some time before they eventually pop open and he shrugs."

    crier "No, I'll have to keep thinking. I'm sure that there must be something out in our wonderful world that I can do."

    "Suddenly he holds up a single finger, as if telling you to be quiet."

    crier """
    
    I'm terribly sorry [game.player_name], but I'm afraid I'm going to say what I feel like I'm always saying at the end of our conversations nowadays. I've got to ring the bell now, and I think I've said this before, but it's really not going to be good for you if you're in here when the bell goes.

    Very loud on the ears. I'm sure I'll be deaf by the time I'm forty.
    """

    "Nat smiles broadly, and then good naturedly shoos you out of the tower."

    $game.crier.romance = False

    return



if c==14:

    "Nat stares at you for a moment, his face completely blank."

    crier "Excuse me?"

    """

    You repeat yourself.

    There is another moment of silence.

    And then, slowly, a smile starts to form on Nat's face, a smile that quickly turns into a grin.
    """

    crier """

    Really? You want to be, you know, with me?

    Like, well, like you like me?
    """

    "His face has gone completely red, and you are surprised that he hasn't started giggling."

    crier """

    I'm not really sure what to do [game.player_name]. And I'm not sure that this is the most romantic of places.

    But [game.player_name], well, what I really want to do is…

    Well…

    [game.player_name]?

    Would you mind if I kissed you?
    """

    $game.crier.romance = True

    return



if c==15:

    if game.crier.like > 14:
        $textinsert = "I mean, I do like you [game.player_name], but "
    else:
        $textinsert = ""

    "Nat looks away from you to stare at his feet, which start shuffling."

    crier """

    That really is very kind of you [game.player_name].

    But I don't think so.

    I'm sorry [game.player_name].

    [textinsert]I don't think it would be a good idea.

    I don't know. I just, well I think I should be honest [game.player_name], but I don't think about you in that way. Well, there are parts of me that do, I suppose, but I think that that's just curiosity, because I've never been in a situation like this.

    But I don't think it would be fair on you to say yes because of curiosity. It think that you, and if I may say so I think that I also, deserve something more special than that. I think everyone does.

    So I'm sorry [game.player_name], but I don't think so. But thank you very much for asking.
    """
   
    if game.crier.like > 4:
        crier "Not that I'm saying no to just being friends. Just the other bit."

    """

    You are both plunged into an awkward silence, broken eventually when Nat looks up to mumble that it's almost the hour and you should probably leave so that he can ring the bell.

    He turns around and moves upstairs without looking at you.
    """

    $game.crier.romance = False


return
