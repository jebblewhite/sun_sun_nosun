label crierscene9alive: 

$Nat9Learn = False
$Nat9Furniture = False
$Nat9People = False

if game.crier.romance == True:
    $textinsert = "takes your hand"
else:
    $textinsert = "turns"

if game.crier.romance == True:
    $textinsert2 = "pressed against your side, his face half obscured as he pushes a kiss into your cheek, while {} lies at your feet.".format(game.creature_name)
else:
    $textinsert2 = "next to you, {} squeezed playfully between the two of you.".format(game.creature_name)
    
    """

    Nat's knock on your door is fast and light, approaching a playful rhythm but shying away from it at the last moment.

    When you open the door he stands in the night's darkness, beaming at you.
    """

    crier "We got you a present [game.player_name]! Want to come see?"

    """

    Without giving you the chance to say no, Nat [textinsert] and starts literally skipping away towards his belltower.

    The journey is short, especially going at the speed that Nat is, but you can't help but notice the way that people look at him as the two of you pass. Some look with anger, some fear, some disgust. But most just look away, maybe sad, but with the message clear: 'you are no longer one of us.'

    If Nat notices, he makes no sign of it. Instead he keeps smiling and skipping until he is bent double and giggling at the door to his belltower.
    """

    crier """

    Sorry, I run more now than I ever used to, but I always forget that I can't go as far as [game.creature_name]. It'd make me feel silly, knowing that she can run that fast and far, but then something silly and simple like opening doors comes along and I remember that there are plenty of things that I can still show her up at.

    Maybe that's mean, but it does make me feel a little better. And I don't think she minds.
    """

    "Nat smiles at you, and then straightens up."

    crier "You ready to see your gift?"

    """

    Not knowing what else to do, you nod, and Nat pushes open the door to the tower.

    The room is, as it always is, dark, and it takes you several seconds before your eyes adjust. Someone has brought a table and padded chairs in to the room: ornate, decorative pieces of furniture that are totally at odds with the feel of the rest of the space.

    You don't have long to examine them, however, because Nat is already ushering you to join him in climbing the rickety staircase that winds up along the walls of the tower. Some stretched, elongated shadows piercing down to your level tell you that [game.creature_name] is already up there.

    The steps groan and creek as you put your weight on them, but you don't feel worried as you follow a merrily chatting Nat up towards the bell.
    """

    crier "I say we got you a gift [game.player_name], but it was mostly [game.creature_name]. I'm not very good at this kind of thing, but she's got a real knack for it. She just had me help with some of the colouring, and oh, of course she didn't mind me doing the background."

    """

    Before you have a chance to wonder what Nat means by this, you are there, standing at the very top of the tower and looking into your own smiling face.

    One half of the outside of the bell, the side accessible from the small wooden shelf that you find yourself standing on, has been painted. A life sized rendition of Nat stands [textinsert2]

    The quality is stunning, the style naturalistic. True, you have seen better, but never painted on the side of a bell, from a small, possibly unstable wooden platform, in the dark. And certainly not painted by something who's only opposable thumb is in its mouth.
    """

    crier "Drawing that's pretty much all she's done for the last few days. I'm not sure, if I'm honest, whose idea it was, but she's the one who put most of the time into it. I could tell you exactly how long if you like."

    "Nat gives you a smile that lets you know that while he is joking, he actually could."

    crier "Oh, but I haven't done the polite thing and ask if you like it. That is the right thing to do, isn't it?"

    menu:

        "It is very well done, [game.creature_name] should be proud.":
            $c=3

        "Oh I love it, thank you both so much!":
            $c=2

        "I would have preferred if you'd asked my permission before doing this.":
            $c=1


label reevaluatecrier9alive:
if c==1:

    "Nat shakes his head."

    crier """

    If it makes you feel any better, at least no one will come up here to see it. I don't think anyone will ever care about this old thing except me ever again. But maybe that's just negative thinking, and I shouldn't do that, I don't like doing that any more.

    But it doesn't matter anyway. Because I like this, and [game.creature_name] likes it, and that's two out of three. I don't know all about democracy and that stuff, but I think that means that it's okay. But maybe I should have asked the Alderman about it.
    """

    "Nat shrugs."

    crier "Ah well, it's done now. And I think it's beautiful. So that's all that matters."

    $game.crier.like -= 2
    $game.crier.att -= 2

    $c=4



if c==2:

    "Nat smiles like a kid with candy."

    crier """

    That's why we did it, at first. Although I must say that I like it so much myself now that I'm not sure it would have mattered how much you like it.

    Not to say that we're not both very glad that you like it! It makes me happy and I'm sure it makes [game.creature_name] happy too.
    """

    """

    Nat turns towards [game.creature_name], pointing at you, then the bell and then giving a thumbs up.

    [game.creature_name]'s tail wags in response.
    """

    $game.crier.like += 2
    $game.crier.att += 1

    $c=4



if c==3:

    "Nat claps his hands."

    crier "Oh she'll be so pleased to know that! As I said, she worked very hard."

    "Nat turns to [game.creature_name] and, after pointing at the bell and then pointing at you, begins a weird kind of mime dance.

    It is clear early on, to you, what Nat is trying to do as he struts around with his chest out, clumsily miming careful drawing, throwing out thumbs up and bowing. He's trying to convey your short sentence, as you said it, to [game.creature_name].

    Judging by the way that [game.creature_name]'s head remains cocked to one side throughout the entire performance, you would guess that he's not doing a very good job. But then again, how would you convey the concept of pride using just mime?

    Nat eventually gives up, shaking his head and resorting to giving [game.creature_name] a thumbs up, which [game.creature_name] replies to by wagging enthusiastically.
    """

    crier "We'll figure it out someday."

    $game.crier.resp += 4
    $game.crier.like += 2
    $game.crier.att += 2

    $c=4



if c==4:

    "There is a brief pause in conversation as Nat looks admiringly at [game.creature_name]'s work, apparently lost in thought."

    menu:

        "How did you find out [game.creature_name] can paint?":
            $c=5

        "Where did that table and those chairs downstairs come from?":
            $c=6

        "Nat, I'm worried about you, and about how people are treating you since everyone found out about [game.creature_name].":
            $c=7

        "*Just let the moment pass in silence*.":
            $c=8



if c==5:

    crier """

    She saw me doing drawing. I had some paper and pencils and I was just doodling. I'm really not a very good drawer, but I enjoy it. It's nice to create something, even if I'm the only one who likes it.

    Well, sorry, you didn't ask about me, but [game.creature_name] saw me doing it and she seemed all curious, cocking her head to the side and the like, so I explained what I was doing. You know, I was trying to draw a leaf, so I took the leaf and pointed at it and the drawing and held up up against the drawing and that kind of thing.

    Well it seemed to take her a while to figure out what I meant, I think she didn't understand that I was trying to copy the world, which I suppose isn't what all artists try to do but I like to keep it simple like that. But anyway, once she got that, she wanted the pencil, and I gave it to her and she started drawing things perfectly!

    Well, maybe not perfectly. It was really hard for her to keep the paper still while she was drawing with her hand, and I'm pretty sure she can't see what she's doing, because her hand doesn't stick far enough out of her mouth for her eye to see it, if you understand what I mean.

    So I thought she could draw on the wall a bit, and then when that was better I thought she could do the bell.

    I don't know. It just seemed...oh what's the word...appropriate? After all, this bell was what I spent most of my time thinking and worrying about before [game.creature_name] came along.

    But there I go again, not answering the question. I'm sure there were things you wanted to know, weren't there?
    """

    $Nat9Learn = True
    $game.crier.resp += 1
    $game.crier.like += 1

    menu:

        "Where did that table and those chairs downstairs come from?" if Nat9Furniture == False:
            $c=6

        "Nat, I'm worried about you, and about how people are treating you since everyone found out about [game.creature_name]." if Nat9People == False:
            $c=7

        "*Shake your head and just enjoy the silence*.":
            $c=8



if c==6:

    if game.crier.romance == True:
        $textinsert = " and you"
    else:
        $textinsert = ""

    "Nat frowns slightly."

    crier """

    Ah yes, those were donated by that miss Elisabeta.

    I'm sure she means very well, and she always seems like a very nice person, but I'm not sure I like her coming over very much.

    She's been a couple of times, she's the only person who has, but I don't really feel like she's doing it as a visit. Do you understand? Like when you come it's so that we can spend some time together, but with her it feels like she's coming to work.
    """

    "Nat shrugs and then shakes his head, as if he is trying to dislodge something from his hair."

    crier """

    I'm being mean. She's very nice and has offered to help with things, if we need help with things. And she brought treats for [game.creature_name] the second time she came.

    I really don't mind it too much. And I suppose it's nice, to have someone else around here occasionally. And she's said that the only time she'll come without organising it first was that first time, when she organised the second time. Which is nice, because it's good to feel that this is our place, me and [game.creature_name][textinsert].
    """

    $game.crier.resp += 1
    $Nat9Furniture = True

    menu:

        "How did you find out [game.creature_name] can paint?" if Nat9Furniture == False:
            $c=5
            jump reevaluatecrier9alive

        "Nat, I'm worried about you, and about how people are treating you since everyone found out about [game.creature_name]." if Nat9People == False:
            
            $c=7

        "*Nod your head and just enjoy the silence*.":
            $c=8



if c==7:

    if game.crier.romance == True:
        $textinsert = " and you"
    else:
        $textinsert = ""

    if game.crier.romance == True:
        $textinsert2 = "And you.  "
    else:
        $textinsert2 = ""

    """

    Nat shrugs. He doesn't seem shocked, or upset, or worried.

    He just shrugs.
    """

    crier """

    I hadn't really noticed [game.player_name], but I don't mind. And I'm not upset either.

    There was a while, at the beginning of this, when people thought they liked me. What I mean is, they smiled when I walked past, and said nice encouraging things to me.

    That was quite different, to how it was before. There were plenty of people who were...cruel, to me then.

    But that change, I think it was just because I was doing something for them. I mean I've been crier for a while, and I know that helped some people before, but it's more important now, but not nearly as important as keeping the time is. I'm a part of the...inf...infastr...I'm a part of the town now.

    I'm not sure if that's what I want people being nice to me for. I'm very proud of my gift, and I wouldn't be who I am without it, but there is more to who I am than it.

    And now people see that, because they've seen [game.creature_name] and how much I care about her. And there would have been a time I would have worried about that, but now I have [game.creature_name][textinsert], so I don't need them.

    I'm happy [game.player_name]. And if they're not, then I'm sorry for them, but I don't think that I can do anything about it. I'm too busy looking after me. And [game.creature_name]. [textinsert]And that's enough for me.
    """

    $Nat9People = True
    $game.crier.att += 1

    menu:

        "Okay. How did you find out [game.creature_name] can paint?" if Nat9Paint == False:
            $c=5
            jump reevaluatecrier9alive

        "Okay. Where did that table and those chairs downstairs come from?" if Nat9Furniture == False:
            $c=6
            jump reevaluatecrier9alive

        "*Nod your head and just enjoy the silence*.":
            $c=8



if c==8:

    $natrelationshipmatrix = (game.crier.resp + game.crier.like + game.crier.att)/3

    "You, Nat and [game.creature_name] stand in silence, looking at your frozen reflections in the bell."

    if game.crier.romance = True:
        
        "Nat, slowly and uncertainly, takes your hand, and when he feels your fingers curl over his he suddenly turns and plants a big, full lipped kiss on your cheek."


        crier """

        I'm happy [game.player_name]. I'm sad, very sad about the darkness and the death, and the way so many beautiful things are going away. But really I'm happy. Because for the first time, I've got people. Well, person, and creature.

        I know it might not seem much. Especially to you, because you're always speaking to everyone and out saving the town and all that.

        But for me, it's all I want. I'm not scared of having more, or feel like I couldn't cope with it. I just don't want it. What I want is you, and [game.creature_name]. And what I have is you and [game.creature_name].
        """

        "Nat's eyes suddenly light up."

        crier """

        Oh, [game.player_name], can I ask you something? Tonight, after we've both finished all our work, do you want to come over to my house? [game.creature_name] sleeps with me there at nights now, and she and I could bring the spare paint over and we could paint the walls in there as well. The three of us.

        Does that sound fun?

        Or maybe, if you'd prefer, we can give the paints to [game.creature_name] and you and I, while she's busy, could go to the bedroom. If you wanted.

        Both sound fun to me.

        Or maybe something else?

        Whatever you want, do come and spend the night with me.

        Because just being with you is what I really want.
        """
    
    elif natrelationshipmatrix > 18:
        
        "It is a long time before Nat lets out a contented sigh."

        crier """

        I'm happy [game.player_name]. I'm sad, very sad about the darkness and the death, and the way so many beautiful things are going away. But really I'm happy. Because for the first time, I've got someone. I've got [game.creature_name].

        But there's more than that. Because for the first time, I've also got a friend.
        """

        "Nat turns to you, his blush clear even in the filtered starlight. Then, suddenly, his eyes light up."

        crier """

        Oh, [game.player_name], can I ask you something? Tonight, after we've both finished all our work, do you want to come over to my house for a sleep over? [game.creature_name] sleeps with me there at nights now, and she and I could bring the spare paint over and we could paint the walls in there as well.

        Does that sound fun?

        Or I don't know, we could just sit and talk. Or we could take [game.creature_name] out for a night time walk. I've got this instinct that night time walks are dangerous, but just because I've still got the count going in my head doesn't mean that anything in the rest of the world seems to be different between day and night.

        Oh, it would be so nice to do something friendship-y tonight. We could roast something over an open fire. Although I'm so bad with cooking I might ruin it. But maybe you could do it.

        Oh, I don't know. But we will do something, won't we?

        Because why shouldn't we spend our time with people who make us happy?
        """
        
    else:
        
        "It is a long time before Nat breaks the silence with a deep sigh."

        crier """

        We painted this because we know how much we owe you.

        I think we all know that if you hadn't had said anything to miss Fyodora, [game.creature_name] would…

        Well. You know…

        But we're not really friends, are we? The two of us, I mean.

        I'm not sure how much more we'll see each other, after this. So I want to say something now.

        Do try and stop sometimes. Because I think that love lives in those slow seconds, and you have to be moving slow to catch them.

        I know that doesn't make any sense. It's just something I feel.

        Watch the river sometimes [game.player_name]. Don't think you always have to be swimming up it.

        Ah, that doesn't make any more sense than the last thing.
        """

        "Nat shrugs his bony shoulders."

        crier """

        It's all very complicated.

        I guess I'm trying to say one thing, one nice simple thing.

        Because I think only really one thing matters.

        So go on, I'm sure you've got lots of very important things to do.

        Goodbye [game.player_name].

        Be happy.
        """

return
