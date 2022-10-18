label crierscene9exile: 

if game.crier.romance == True:
    $textinsert = "I'm sorry {}, I know that you will want me to trust you with this, but would".format(game.player.name)
else:
    $textinsert = "Would"

"""

It has been decided, by who it is not quite clear, that it is your responsibility to make sure that Nat really does send [game.creature_name] back into the forest.

Enough people have been keeping an eye on the belltower's door that, your trust for Nat aside, you are confident that [game.creature_name] has not left her prison.

So, now that you hear a soft, slow knock on your door, you know that Nat has come to tell you that it is time for you to witness the exile.

When you open the door, he cannot meet your eyes.
"""

crier """

I'm not ready [game.player_name]. You know, I don't think I'll ever be ready. And I really don't think that this extra little time has made it any easier.

But [game.creature_name] wants to get out. I think she understands a bit, I think she understands enough.

But I had to let her out before, for her, and I have to do it again now.

Even if…
"""

"There is a long pause. Tears land in the dirt at Nat's feet."

crier "I think you need to come with me now."

"""

Without checking whether you are behind him, Nat turns and walks away from you, towards the belltower.

He moves fast, even with his head down and shoulders slumped, so there would be no chance to talk even if either of you wanted to.

People stop what they are doing to gawk as you go past, but despite, or perhaps because of, them all knowing what your short march means, they all have the respect to let you go without following.

When you reach the belltower, Nat indicates for you to wait outside.

He is gone for a long time.

You are just considering going in, perhaps worried there has been some accident, or breakdown, or possibly that there might be some kind of trickery, but just before you make up your mind Nat appears, [game.creature_name] hobbling awkwardly beside him, one of its front limbs curled through Nat's gentle grip.

The only sign, save maybe the swirling black and pink of her 'eye', of [game.creature_name]'s emotions is her tail, curled between her legs and flat against her stomach.

Nat's distress is much more obvious.

He nods at you, and the three of you make a slow, silent trek towards the forest.

It is only when you have gone as far as you can go before actually breaking through the tree line that Nat finally speaks again.
"""

crier "[textinsert] you mind standing over there a bit? I don't mind if you can still see us, but, well, I'd like to be able to feel like we're alone. Just one last time."

"""

You can think of no good reason to deny Nat's request, so you walk a little way into the tree line, keeping Nat and [game.creature_name] in your sights the whole time.

Nat, unsurprisingly, is crying. You see his mouth opening and closing, though you are too far away to know if he is actually saying anything. Not that it would matter either way. Nat has been aware of [game.creature_name]'s deafness for some time. He seems to find it strangely endearing, or perhaps even comforting.

Either way, the goodbye is surprisingly short. The two seem to embrace for some time, Nat kneeling on the ground, his arms thrown around [game.creature_name] while its front limbs wrap around him.

And then he's up, explaining with his hands: shooing motions towards the forest, palms held up between [game.creature_name] and Lotosk.

[game.creature_name] takes a few steps towards the forest, then turns back in a quick rush towards the town, but it doesn't make it more than a few steps before it plants its limbs firmly into the ground, creating a remarkably good illusion of what it would look like if it had just run face first into a barrier. Then she looks at Nat, who nods.

There is a pause, the only movement the flow of tears down Nat's face.

And then [game.creature_name] takes two steps forward and, delicately, uses her tongue-hand to grasp Nat around the wrist. He instinctively reaches down to stroke her glossy fur, but she pulls away, gently, suggestively, tugging him towards the forest.

Nat wails. He falls back to his knees, his arms flailing as he battles with the instinct to hold [game.creature_name] close while also reminding her that she has to go away.
"""

crier """

No! No no no [game.creature_name], I love you I love you I really do, but I can't, I just can't!

If I were anything else than what I am, I would, but I can't! We just can't live in each other's places. I thought maybe we could, but I've been shown that we can't. So you have to go.
"""

"""

Nat pushes himself to his feet and thrusts his hands out, his shaking fingers pointing towards the darkness of the forest.

[game.creature_name] stands still for a long time. Then one of her front limbs snakes up and gently wipes the tears from Nat's face.

He grabs the tentacle and kisses it.

Her tongue comes out and, the fingers slightly bent, she waves farewell.

And then she disappears into the forest, the night swallowing up her shadow black form.

Nat stands for a long time, staring at his feet. His hand idly cups the air, as if he can still feel her soft arm in his hand.

He only looks up when he has spent all his tears. He nods once to you and waits for you to approach.
"""

menu:

    "That was difficult to watch, I'm sorry.":
        $c=4

    "I know that things seem hard now, but I promise you, they will get better.":
        $c=3

    "It needed to be done Nat, for the sake of the town.":
        $c=2

    "Pull yourself together. This kind of stuff if why people think you're weird.":
        $c=1



if c==1:

    """

    Nat's eyes go wide with shock.

    His mouth opens and closes a number of times, like a fish that suddenly finds itself on dry land.

    Then he stops, looks down at the ground, and shakes his head.
    """

    crier """

    I've always been told, always be kind.

    And I don't like bad words. I don't like words that are meant to hurt people, I don't like that someone made them.
    """

    if $game.crier.romance == True:

        crier "But fuck you [game.player_name]."
    
    else:
        crier"""
        
        So I won't say anything.

        But I'm thinking things.
        """

    """
    And with that, Nat turns and walks back to town.

    You will hear his voice tomorrow morning, and the morning after that.

    But you know, as you watching his frail form disappear, that Nat will never speak to you again.
    """

    $game.crier.resp -= 4
    $game.crier.att -= 4
    $game.crier.like -= 4



if c==2:

    $natrelationshipmatrix = (game.crier.resp + game.crier.like + game.crier.att)/3

    "Nat shakes his head."

    crier """

    I understand that you, and miss Fyodora, think that. And I suppose I shouldn't be angry with you for being wrong. I know you're wanting to do the right thing.

    But you are wrong.

    [game.creature_name]'s a beautiful, wonderful, kind creature.

    I tried to show you [game.player_name].

    But I guess you couldn't see it.
    """

    if $game.crier.romance == True:
        
        crier """
        
        I don't think you're a bad person [game.player_name]. And I really am flattered that you say that you like me.

        I won't feel bad about the time we spent together.

        But I can't be around you any more [game.player_name].

        I know that's unfair, and maybe you were just trying to help, but I really think that it would be good if you could have tried more.

        I like to think I would have tried more for you. But maybe I wouldn't have.

        I guess we'll never know.

        So thank you [game.player_name].

        But I think I have to go now.
        """
    
    else:
        crier "I think I have to go now [game.player_name]."

        if natrelationshipmatrix > 14:

            crier """
            
            I don't think you're a bad person [game.player_name].

            But what you did...well, she's gone because of it. And that's what I'll think when I see you.

            So I'm going to say goodbye now.
            """

    "And with that, a little nod of the head and a turn of the heel, it is over."

    $game.crier.resp += 1
    $game.crier.like -= 2



if c==3:

    $natrelationshipmatrix = (game.crier.resp + game.crier.like + game.crier.att)/3

    "Nat shakes his head."

    crier """

    I know you're just trying to be kind. And I haven't done this before, so I don't know if you're right.

    But it doesn't matter. What matters is that it hurts now. And nothing about what's going to happen later can change that.

    But I know you were just trying to be kind, so thank you for that.
    """

    $game.crier.resp -= 2
    $game.crier.like += 2

    if $game.crier.romance == True:
        $c=5
    elif natrelationshipmatrix > 18:
        $c=6
    else:
        $c=7



if c==4:

    if game.crier.romance == True:
        $textinsert = "Maybe it's just because I like to feel like we had a connection."
    else:
        $textinsert = ""

    $natrelationshipmatrix = (game.crier.resp + game.crier.like + game.crier.att)/3

    crier """

    I don't know, but I would reckon it was more difficult to do.

    But, and I know this may sound cruel, I'm glad it was difficult to watch. I don't really know why, but I am glad. [textinsert]
    """

    $game.crier.like += 2

    if $game.crier.romance == True:
        $c=5
    elif natrelationshipmatrix > 18:
        $c=6
    else:
        $c=7



if c==5:

    """

    Nat stares down at the ground for a few moments, before looking up and meeting your gaze properly for the first time since you decided [game.creature_name]'s fate.

    Maybe, at one time, you would have described his expression as sad. But you've seen too much of his sadness, and seen too much of him, to confuse it now. No, what you see is closer to melancholy, or nostalgia.
    """

    crier """

    I don't think you're a bad person [game.player_name]. And I really am flattered that you say that you like me.

    I won't feel bad about the time we spent together.

    But I can't be around you any more [game.player_name].

    I know that's unfair, and maybe you were just trying to help, but I really thought that it would be good if you could have tried more.

    I like to think I would have tried more for you. But maybe I wouldn't have.

    I guess we'll never know.

    So thank you [game.player_name].

    But I think I have to go now.
    """

    "And with that, a little nod of the head and a turn of the heel, it is over."

    return



if c==6:

    "Nat cocks his head."

    crier """

    I don't know why you did what you did, and honestly I don't think I care to know.

    But I like to be an honest man [game.player_name]. I was always told it was a good thing, and while I don't know if it's done good things for me, I trust the people who told me it's good, so I'm going to keep doing it.

    So I'll tell you something, and I hope that you'll keep this a secret because I really don't want anyone knowing, definitely not miss Fyodora, but neither miss Elisabeta also, who is nice but I'm a little worried about why she seemed to like [game.creature_name] so much.

    No, I don't want you telling anyone.

    But I hope, and I must admit that I'll probably not sleep at all tonight because I'll be scared that I'm wrong, but I hope that this wasn't really goodbye.

    I know I'm a fool and a klutz when it comes to things like this, but I'm not just going to let her go. I'm going to follow [game.creature_name] into the forest. Not to live or anything like that, but to visit.

    I don't know that she'll be waiting for me. But I hope that she will. And if she is, I know that she'll protect me.
    """

    menu:

        "This is a terrible idea Nat. What if she isn't there to protect you? It's too dangerous.":
            $c=8

        "No Nat, you need to move on. Find some human friends that you can love that much.":
            $c=9

        "I understand Nat. If this is what you feel you have to do, then do it.":
            $c=10

        "Let me come with you.":
            $c=12



if c==7:

    "Nat stares at the ground for a few moments, and then lets out a little sigh."

    crier """

    I like to be an honest man [game.player_name]. I was always told it was a good thing, and while I don't know if it's done good things for me, I trust the people who told me it's good, so I'm going to keep doing it.

    So I'll tell you that I don't think we can be friends any more. To be honest, I'm not sure that we ever were friends, were we [game.player_name]?

    Well I don't know. And I don't think it matters either way.

    Because I think I just need to go now [game.player_name].
    """

    "And with that, a little nod of the head and a turn of the heel, it is over."

    return



if c==8:

    "Nat stares at you for a long time."

    crier "If she's not there to protect me then...well..."

    "Then he looks away, his eyes falling back to the ground."

    crier """

    She'll just have to be there to look after me, won't she?

    Because you're right, I don't know what I'll do if she isn't.
    """

    $game.crier.like -= 2
    $game.crier.resp += 1

    $c=11



if c==9:

    crier """

    You don't think I've tried that [game.player_name]? You don't think I've always wanted friends?

    I...I…

    I didn't pick [game.creature_name], [game.player_name]. I mean, she's wonderful and beautiful and kind, but I didn't pick her. She picked me.

    And no-one else ever has.
    """

    $game.crier.like -= 1
    $game.crier.resp -= 1

    $c=11



if c==10:

    "Nat smiles, and then, to the surprise of both of you, gives you a firm, bony hug."

    crier """

    I hate this. I hate all of this. Nothing this sad has ever happened to me before.

    But knowing that you're okay with me going to see [game.creature_name].

    Well, it makes it just a little bit easier.
    """

    $game.crier.like += 4
    $game.crier.att += 2

    $c=11



if c==12:

    "Nat smiles, a wide, genuine smile."

    crier """

    That's nice [game.player_name]. Really it is.

    I think I'd be happy. And I think [game.creature_name] would be too.

    But I don't think you'd be.

    You sent [game.creature_name] away [game.player_name]. If you didn't do it because you don't like her, you did it for the others. And if you did it for the others, you won't be happy leaving them.

    And they need you [game.player_name]. More than I need you, I think.

    So thanks. It's nice.

    But no.
    """

    $game.crier.like += 4 
    $game.crier.att += 4
    $game.crier.resp -= 1

    $c=11



if c==11:

    "Nat suddenly looks back towards town."

    crier """

    I missed the last bell [game.player_name]. I don't suppose you noticed, but I missed it.

    I knew I was missing it. But I don't want to miss the next one as well.

    People will get confused.

    So goodbye then [game.player_name], I suppose.

    It has been nice getting to know you. But now that [game.creature_name]'s gone, we're not going to talk much, are we? It just won't be the same.

    I think you're a good person [game.player_name]. But she was my world, and I tried to share her with you and you sent her away.

    So goodbye [game.player_name]. I am sure I will {i}see{/i} you plenty. And I'll just say now, while we are here, just the two of us, that I wish you well.

    But do try and stop sometimes. Because I think that love lives in those slow seconds, and you have to be moving slow to catch them.

    I know that doesn't make any sense. It's just something I feel.

    #{i}Watch#{/i} the river sometimes [game.player_name]. Don't think you always have to be swimming up it.

    Ah, that doesn't make any more sense than the last thing.
    """

    "Nat shrugs his bony shoulders."

    crier """

    I've said too much already.

    Goodbye [game.player_name].

    Be happy.
    """


return
