label crierscene6: 

$nat6Animal = False
$nat6Monster = False

"""

Not long after the last time you saw Nat, a note appeared under your door.

'[game.creature_name] and I usually spend the time between Three and Four playing at the place on the map that I've drawn on the back of this paper. If you ever want to join us, I think it would be a good chance for you two to get to know each other better.

Best wishes and all that,

Nat.'

Today, you have decided to take him up on his offer. You know just by looking at it that the map is terribly drawn, so you leave early enough that you can afford to get lost a couple of times.

Nevertheless, by the time you arrive at the small strip of grass, surrounded on three sides by the forest and the other by river, Nat and [game.creature_name] are already there.

You see them before you hear them, and your heart starts beating double time when you see [game.creature_name], the hand that is its tongue lolling out of the side of its mouth, chasing Nat, who's face is frozen in a silent scream.

You dash forward a few steps, but you couldn't make it in time before one of [game.creature_name]'s front limbs flashes out and curls effortlessly around Nat's waist. Nat stops as if caught by a lasso, his head and legs continuing to move forward even as his torso is dragged backwards.

He lands on his arse with a heavy thump, and then the creature is on him with its mouth opening wide...

...it's hand reaching out…

...to ruffle Nat's hair.

The wind changes direction slightly, and the sound of Nat's laughter is blown towards you.

You slow your pace, and as you do [game.creature_name] stops mock wrestling with Nat and turns to you, the index finger of its tongue-hand pointed straight at you.
"""

crier """

Oh, hi there [game.player_name]! I'm glad you found us, I don't think the map was very good: I'm not very good at knowing where things are and such like. And I didn't have anything green or blue that I could use to make the forest or the river.

Sorry, I meant it's very nice to see you [game.player_name]. [game.creature_name] thinks it's nice to see you too, don't you?
"""

"""

Nat gestures at the side of [game.creature_name]'s head, smiles and then points to you.
"""

if game.crier.like < 17:
    "[game.creature_name] makes no move to acknowledge you, but does lean slightly forward, both on its hind dog legs and front tail-legs, placing itself slightly between you and Nat, the orb that makes up the top portion of its head a swirling dirty yellow."

    crier "Uh-sorry."

else:
    "[game.creature_name]'s hand transfers from pointing at you to waving energetically from side to side, while her tail-like front limbs push her body up and down, creating an energetic rocking-horse effect. The orb that makes up the top portion of her head is a swirling reddy purple."
    
    crier "That means she's happy."

crier """

You want to play something [game.player_name]? [game.creature_name] and I were just playing 'chase'. Well, it's something I've been calling chase, I don't know if it has a proper name. We just try and catch each other, although it's very hard to beat [game.creature_name], she's very good.
"""

menu:

    "Sure, I'll play!":
        $c=1

    "That hardly seems fair, playing a game that [game.creature_name] is always going to win.":
        $c=4

    "No, I don't want to play with that thing.":
        $c=5


label reevaluatecrier6:
if c==1:

    crier "Okay, I'll go first!"

    """

    Nat springs up onto his legs and sprints off with surprising speed towards the river. Before you can even start to dash towards him, [game.creature_name] has uncurled her long front limbs and shot off ahead of you. She has successfully downed him before you have even fully moved through the tree line and properly joined them on the thin patch of grass between forest and river.

    Laughing, Nat pushes [game.creature_name] off him and indicates that it is now her turn to run. She lopes away from him, much slower than she was when chasing him, and Nat windmills his arms as he follows after her.

    Nat is fast, but you think that you might just be faster. The question is, do you let him win?
    """

    menu:

        "*Let Nat get to [game.creature_name] first.*":
            $c=2

        "*Try to beat Nat to [game.creature_name].*":
            $c=3



if c==2:

    if game.crier.att > 17:
        $textinsert = "His eyes linger on yours for a second too long after he speaks, then he quickly and conspicuously glances away to an empty patch of grass by his side."
    else:
        $textinsert = ""

    """

    You slow down your run slightly, but quickly realised that you had misjudged anyway: even if you had pushed yourself Nat may very well have beaten you anyway.

    You play for some time, circumstances occasionally pushing [game.creature_name] into your path before Nat's, but mostly you are the third wheel in a game between Nat and [game.creature_name].

    For her part, this is because [game.creature_name] seems hesitant to tackle you in the same way that she joyously slams Nat into the ground.

    True, she does grab you, but while she again and again snatches Nat from behind, always prompting a squeal of joy and a stream of laughter, she prefers to ‘catch' you by jumping in your path and gently curling one of her front limbs around your waist, never actually pulling you enough to bring you down.

    Maybe, while Nat seems totally unaware of your restraint, [game.creature_name] does realise that, for some reason, you are holding yourself back.

    Eventually Nat collapses, clearly exhausted, and [game.creature_name] slinks over to curl up next to him.
    """

    crier "That...was...fun, [game.player_name]!"

    "Nat beams at you as he pants, his face flushed and glowing. [textinsert]"

    $game.crier.like += 4

    menu:

        "*Curl up with Nat and [game.creature_name].*":
            $c=11

        "*Sit on the grass near Nat and [game.creature_name].*":
            $c=12

        "*Stand near to Nat, but not too close to [game.creature_name].*":
            $c=13

        "Nat, how do you know you can trust [game.creature_name]? Remember that when we found it in the woods it attacked me.":
            $c=14



if c==3:

    if game.crier.att > 17:
        $textinsert = "His eyes linger on yours for a second too long after he speaks, then he quickly and conspicuously glances away to an empty patch of grass by his side."
    else:
        $textinsert = ""

    """

    You push yourself as far as you can, and as you do so you realise that you might have been wrong about Nat. As you bend forward into a more effective stance, Nat appears at your side and both of you hurtle towards [game.creature_name].

    But, despite his valiant attempts, you slam into the impossibly soft coat of [game.creature_name] just a moment before Nat can. And then the game truly begins.

    You must admit to yourself, you are in pain. As the game wears on, [game.creature_name] starts to treat you the same way that it treats Nat: stalking you from behind and then grabbing you by your waist and slamming you to the ground. [game.creature_name] is careful, but there is no possible way to avoid bruises.

    Not to mention that keeping up with the other two means that you push yourself slightly more than perhaps you should.

    Eventually Nat collapses, clearly exhausted, and [game.creature_name] slinks over to curl up next to him.
    """

    crier "That...was...fun, [game.player_name]!"

    "Nat beams at you as he pants, his face flushed and glowing. [textinsert]"

    $game.crier.like += 4
    $game.crier.resp += 4
    #{Minimum injury gained}

    menu:

        "Curl up with Nat and [game.creature_name].":
            $c=11

        "Sit on the grass near Nat and [game.creature_name].":
            $c=12

        "Stand near to Nat, but not too close to [game.creature_name].":
            $c=13

        "Nat, how do you know you can trust [game.creature_name]? Remember that when we found it in the woods it attacked me.":
            $c=14



if c==4:

    crier """

    It's not about fair or not [game.player_name], not the way I see it at least. We're just having fun.

    And anyway, I don't think that things are fair for [game.creature_name] anyway. She has to stay inside all the time when I'm out working, and I still think she can't hear, so she can't have the fun of conversations. Although I suppose that conversations can be very stressful, so maybe that is fair.

    But still, she does stay in the tower all the time. So I actually think it is fair, if when we play we play a game that she's good at.

    So, are you going to play?
    """

    $game.crier.resp -= 2

    menu:

        "Sure, I'll play!":
            $c=1
            jump reevaluatecrier6

        "No, I don't want to play with that thing.":
            $c=5



if c==5:

    "Nat bites his lower lip and looks at the ground."

    crier "Oh. What's wrong with her?"

    menu:

        "It's a wild...creature, it can't be trusted.":
            $c=6

        "It's a monster: it has a human hand instead of a tongue, that can't be good!":
            $c=7

        "She's gross.":
            $c=8

        "I just don't like animals, it's nothing personal.":
            $c=9



if c==6:

    crier "But she can be trusted! Look, I taught her some tricks!"

    """

    Nat then proceeds to gesticulate wildly, his actions followed lazily by 'tricks' from [game.creature_name].

    First, pointing at the ground is followed by sitting. Then a turning motion is followed by a roll over. A mimed hug prompts [game.creature_name] to walk right up to Nat and curl one of her long front limbs fully around his body. And then an extended hand is met with [game.creature_name]'s dripping wet hand-tongue, which shakes it.
    """

    crier "See! And she knows when I'm happy, or sad, or frustrated. She's not a wild animal and she's more intelligent than any dog."
    

    $game.crier.resp -= 2 
    $nat6Animal = True

    menu:

        "If it's that intelligent, then it's a monster: it has a human hand instead of a tongue, that can't be good!" if Nat6Monster == False:
            $c=7

        "Well, I still think she's gross.":
            $c=8

        "Well I just don't like animals, it's nothing personal.":
            $c=9

        "Fine, but I still don't want to play.":
            $c=10

        "Okay, if you say so, then we can play.":
            $c=1
            jump reevaluatecrier6



if c==7:

    crier """

    Maybe she is a monster, maybe she isn't. I don't know all that much about words. But if you mean that she's evil, then you're wrong.

    Yes, she's very unusual, and very different, and yes she has a human hand instead of a tongue. But that doesn't mean she's evil.

    It's like Elisabetta said, things are very weird right now, but that doesn't mean that it's all bad. Just different, and special.

    That's what [game.creature_name] is, different and special. And nice and kind. I know her much better than you do, so I can tell you that's what she is.
    """

    $game.crier.like -= 4  
    $nat6Monster = True

    menu:

        "If it's not a monster, then it's a wild...creature, it can't be trusted." if Nat6Animal == False:
            $c=6
            jump reevaluatecrier6

        "Well, I still think she's gross.":
            $c=8

        "Well I just don't like animals, it's nothing personal.":
            $c=9

        "Fine, but I still don't want to play.":
            $c=10

        "Okay, if you say so, then we can play.":
            $c=1
            jump reevaluatecrier6



if c==8:

    crier """

    Well that's very unkind [game.player_name]. I'm sure that if someone found you gross, you wouldn't want them to not play with you because of it.

    But still, if you find her gross, there's not much I can do about it. I don't think it's fair, and I don't think it's nice, but if it's how you feel, then there's nothing I can do to make you feel anything else.
    """

    $game.crier.resp -= 2
    $game.crier.like -= 2

    $c=10



if c==9:

    "Nat looks at you, clearly confused."

    crier """

    I don't understand how you could [game.player_name]. Firstly, as far as I know, there are hundreds of different kinds of animal, and they all really are very different from each other. I figure there must be some animal that you like?

    And secondly, I don't understand how anyone could not like animals. I don't even know how I could say how wonderful they are. But they are wonderful, all of them.

    I'm confused that you can't see that.

    But I'm not sure I can say why any way that I try. So I'll just say it's okay. I suppose you don't have to like animals...
    """

    $game.crier.att -= 4

    $c=10



if c==10:

    "Nat shrugs, and lies fully down on the grass. [game.creature_name] slinks over to curl up next to him."

    menu:

        "Sit on the grass near Nat and [game.creature_name].":
            $c=12

        "Stand near to Nat, but not too close to [game.creature_name].":
            $c=13

        "Nat, how do you know you can trust [game.creature_name]? Remember when we found it in the woods it attacked me.":
            $c=14



if c==11:

    $game.crier.att += 4 
    $game.crier.like += 2 

    if game.crier.att > 17:
        $textinsert = "happily"
    else:
        $textinsert = "kindly"

    if game.crier.resp > 12:
        $textinsert2 = "You're an important person with very good work to do after all!"
    else:
        $textinsert2 = ""

    """

    You tuck yourself into a small gap between Nat and [game.creature_name]'s warm soft body.

    Nat smiles [textinsert] at you. He begins to tell you, excitedly, about all of the things that he's learnt around town recently, all the pieces of small happy gossip that he's collected: Kendra's new baby, Stefan and Kyle's engagement, another successful operation by Fyodora.

    It's difficult to not share in his happiness. And then suddenly he's pushing himself up onto his feet, telling you that he has to get back to the tower to ring in the hour.
    """

    crier """

    I really enjoyed seeing you [game.player_name]. And I love playing games with [game.creature_name], but I had no idea how much more fun it could be with all three of us! Oh please can we do this again some time [game.player_name]!

    I know you're busy, so I won't pressure you to arrange a time now. But as my note said, I'm here most days at this time. We would both love it, I'm sure, if you came along again.

    I've got to take a long way round [game.player_name], so that no one will see [game.creature_name]. You just go straight to wherever you need to go, I don't want to keep you. [textinsert2]
    """

    return



if c==12:

    $game.crier.like += 2 

    if game.crier.resp > 12:
        $textinsert2 = "You're an important person with very good work to do after all!"
    else:
        $textinsert2 = ""


    """

    As you sit down on the grass Nat begins to tell you, excitedly, about all of the things that he's learnt around town recently, all the pieces of small happy gossip that he's collected: Kendra's new baby, Stefan and Kyle's engagement, another successful operation by Fyodora.

    It's difficult to not share in his happiness. And then suddenly he's pushing himself up onto his feet, telling you that he has to get back to the tower to ring in the hour.
    """

    crier """

    I really enjoyed seeing you [game.player_name], you should join me out here again at some point, if you feel like it.

    I know you're busy, so I won't pressure you to arrange a time now. But as my note said, I'm here most days at this time.

    I've got to take a long way round [game.player_name], so that no one will see [game.creature_name]. You just go straight to wherever you need to go, I don't want to keep you. [textinsert2]
    """

    return



if c==13:

    $game.crier.like -= 2 

    if game.crier.resp > 12:
        $textinsert2 = "You're an important person with very good work to do after all!"
    else:
        $textinsert2 = ""

    """

    Nat gives you an odd look when you don't join him on the grass, then gives a light shrug and begins to tell you, not very enthusiastically, about the things that he's learnt around town recently, all the pieces of small happy gossip that he's collected: Kendra's new baby, Stefan and Kyle's engagement, another successful operation by Fyodora.

    When there is a lull in the conversation he stands up to tell you that he has to get back to the tower to ring in the hour.
    """

    if game.crier.like > 16 or game.crier.att > 17: 
        crier """
        
        I really enjoyed seeing you [game.player_name], you should join me out here again at some point, if you feel like it.

        I know you're busy, so I won't pressure you to arrange a time now. But as my note said, I'm here most days at this time.
        """

    crier "I've got to take a long way round [game.player_name], so that no one will see [game.creature_name]. You just go straight to wherever you need to go, I don't want to keep you. [textinsert2]"

    return



if c==14:

    "Nat looks at you, clearly confused."

    crier """

    Well of course I can trust her [game.player_name]. She's been nice and kind and gentle. I know she attacked you, but she was scared. Couldn't you tell? I think she'd seen hunters before and she was scared of your weapons. But she didn't attack me, because I didn't have a bow or an axe or anything, and she was nice to me right away.

    She's nice to you now though [game.player_name], isn't she? Because you showed her that you don't want to kill her. I mean, you did that just by being in the same space as her and not doing it, you know? And now she trusts that you're safe.

    Can't you do the same thing with her? She's not attacking you, she hasn't attacked me and we've been together a lot, doesn't that mean we can trust her? And more, because she's been really nice to me, so why can't I be really nice to her back?
    """

    $game.crier.att += 2

    menu: 

        "That's a very simplistic way of looking at it Nat. We don't know anything about this creature, she might just be pretending to be nice.":
            $c=16

        "She's an animal Nat, and one we know very little about. Animals are unpredictable, maybe she's nice now but that could change at any time.":
            $c=17

        "Okay Nat, if you're sure.":
            $c=15



if c==15:

    crier """

    More sure than I am about people.

    Now come sit down [game.player_name]!
    """

    menu:

        "*Curl up with Nat and [game.creature_name].*":
            $c=11

        "*Sit on the grass near Nat and [game.creature_name].*":
            $c=12

        "*Stand near to Nat, but not too close to [game.creature_name].*":
            $c=13

    jump reevaluatecrier6



if c==16:

    "Nat laughs."

    crier """

    Why would she be pretending to be nice [game.player_name]? She's always been nice to me. What could she want except friendship? She still gets her own food and toys and things.

    Do you think she's got some great evil plan? That's funny.

    I know it's rude to laugh. I know you didn't mean it as a joke.

    But [game.creature_name] would never be like that. She's a good person … or creature. I don't care what she is. She's nice and she's kind. She doesn't hide things like people do.

    That's that. Now come sit down.
    """

    $game.crier.resp -= 2

    menu:

        "*Curl up with Nat and [game.creature_name]*.":
            $c=11

        "*Sit on the grass near Nat and [game.creature_name]*.":
            $c=12

        "*Stand near to Nat, but not too close to [game.creature_name]*.":
            $c=13

    jump reevaluatecrier6



if c==17:

    if game.crier.att > 17:
        $textinsert = "It's a little private, but maybe one day I'll show you."
    else:
        $textinsert = "It's right up there on my thigh so a little too private for me to show you."

    crier """

    Dogs are animals, aren't they? I've seen some really big strong dogs. I've been scared of dogs before, but I can always tell if they want to bite me. One of them did once, Fyodora had to clean out the wound and there's still a bit of a scar. [textinsert]

    The mean ones bark and growl and show their teeth, but the nice ones just wag. [game.creature_name] wags, so I know she's nice.

    And the people who own these dogs, even some of the growly mean ones, they sometimes have them in their house and let their children play with them and everything is fine.

    So everything is fine.

    Now come sit down.
    """

    "Nat gives you a smile, so pure and confident that you know that any further arguments will get you nowhere."

    menu:

        "*Curl up with Nat and [game.creature_name]*.":
            $c=11

        "*Sit on the grass near Nat and [game.creature_name]*.":
            $c=12

        "*Stand near to Nat, but not too close to [game.creature_name]*.":
            $c=13

    jump reevaluatecrier6

 
return
