label crierscene5: 

$Nat5Hold = False
$Nat5Tell = False

"""

Being honest with yourself, you were unsure whether Nat would ever make it out of the forest. But, while some hours did go by without any sign of him, it did not take too long before the bells were ringing again.

At the very least, Nat has survived. But that is all you know as you mount the few steps up to the tower and push at the old wooden door.

Which doesn't move.

It's not locked. You can feel that much. Instead you guess that there must be something heavy blocking it on the other side.
"""

menu:

    "*Push harder*.":
        $c=1

    "*Knock*.":
        $c=2



if c==1:

    """

    You lean your weight against the decaying door, planting your feet firmly and giving it all your strength.

    You hear a little shriek from inside, and just as you feel yourself begin to win the battle something strong slams into the other side, knocking you stumbling back.

    You are just about to try again when you hear Nat's voice, echoing down from somewhere well within the tower, calling out to you.
    """

    $game.crier.like -= 2

    $c=3



if c==2:

    "You knock, the sound echoing up through the empty tower. Just as the echo of your knock dies, it is usurped by the echo of Nat's voice, coming down from somewhere above you."

    $game.crier.like += 1

    $c=3



if c==3:

    crier "Who is it? I don't really want to be disturbed."

    "You reply, but before you can get any further than your name, Nat responds."

    crier "Oh, okay [game.player_name], if it's only you, I'll be down in just a moment."

    """

    It feels like Nat takes quite a bit more than a moment to reach you, although if anyone in town was to be an authority on that it would be Nat himself, and the process seems to involve the sounds of slowly moving heavy furniture.

    But, eventually, the door creaks open to reveal Nat, seemingly perfectly healthy, smiling awkwardly as he ushers you inside.
    """

    crier "Sorry I left you the way I did [game.player_name]. But it seems to have all turned out all-right in the end, hasn't it?"

    menu:

        "I've been worried sick about you Nat. What happened?":
            $game.crier.like += 2
            $c=6

        "Of course it hasn't turned out all-right, you left me on my own while you did gods knows what with a nightmare beast in the forest.":
            $c=4

        "I'm so happy to see that you're okay Nat.":
            $c=5



if c==4:

    crier """

    Well, I figured that you were okay, or as close to it as I could make sure you could be, and I thought that if I did it on my own that at least the only person who could get hurt was me.

    I'm...I'm sorry if that was wrong.
    """

    $game.crier.like -= 2

    $c=6



if c==5:

    crier """

    That's, that's very nice of you to say.

    I'm happy to see that you're all-right too. I suppose there was a moment there when it looked a bit, well I suppose 'tense' would be the word, for us both there.
    """

    $game.crier.like += 2
    $game.crier.att += 2

    $c=6



if c==6:

    crier """

    I'm okay now. I think it would be wrong if I tried to pretend to you that I wasn't scared right up until w...I got back here.

    You see, after I left you, the...thing took me through the forest, the colours on its head were flashing and swirling the whole way. I couldn't get a good look at it, it was too dark, but I got an, a general idea of what it must be like. Never seen anything like it before.

    Anyways, it took me to this little, well I suppose it was a lair but it was much nicer than that makes it sound. I'm sure there's a better word but I've never really had to deal with this kind of thing before so I'll just go with the one I heard used about the homes that dragons and the things like that are supposed to have in those fairy tales I was told as a kid.

    Anyway, sorry I keep getting off track don't I? And I suppose that's off track again, even just saying that.

    So anyway, it showed me its lair. It had found all sorts of stuff, weird shiny rocks and these hard, pitch-y sticks but also things that weren't natural, you know, like it had found a little tin soldier and a broken hoe and a couple of empty bottles.

    And it had this big old blanket that I think maybe one of the farmers used to use to keep the sickly cows warm in the winter, but I suppose that there aren't many cows left any more so I don't suppose they'd mind that they don't have the blanket any more.

    Anyway, the thing picked these all up one by one and showed them to me. Some of them were oh-so-pretty. Then, after it had shown me everything, it showed me a bunch of mushrooms. I think it wanted me to eat them, but I recognised them as some of the ones that Joan says might be bad for us, so I, well I guess I told it I couldn't eat them.

    It was quite late by then, around my normal bed time, and I think it knew I was tired so it pulled that old cow smelling blanket over me and we slept for a little bit.

    When we woke up, well, we, well, I suppose we tidied a few things up. And...came back here.
    """

    "Nat finishes suddenly and looks down at his feet."

    menu:

        "Wait, how did you tell it you couldn't eat the mushrooms?":
            $c=7

        "Wait, how did it pick these things up?":
            $c=8

        "There's something you're not telling me Nat....":
            $c=9

        "So what happened to the creature?":
            $game.crier.att += 2
            $c=9



if c==7:

    crier "Well, I tried just telling it, but I don't know if it can even hear, you know, anything, so I did this:"

    "Nat begins extravagantly miming the act of eating something and then being immediately, violently, ill. Once he finishes, which takes longer than you would have expected, he looks up at you and smiles."

    $Nat5Tell = True

    menu:

        "Wait, how did it pick these things up?" if Nat5Hold == False:
            $c=8

        "There's something you're not telling me Nat....":
            $c=9

        "So what happened to the creature?":
            $game.crier.att += 2
            $c=9



if c==8:

    crier "Well, with its ha-...Umm..."

    $Nat5Hold = True

    menu:

        "Wait, how did you tell it you couldn't eat the mushrooms?" if Nat5Tell == False:
            $c=7

        "There's something you're not telling me Nat....":
            $c=9

        "Never mind that, what happened to the creature?":
            $game.crier.att += 2
            $c=9



if c==9:

    """

    Nat opens his mouth, ready to say something, when there is a sudden *thump* behind you, which you feel more than you hear.

    You turn and there, maybe just a few feet away from you, is the creature, fully visible in the moonlight streaming through the windows.

    Despite it being the only thing you've already seen clearly before, you notice the colours first: a swirling mixture of sky blue, grey and pink.

    The difference is, now you can see the colours in context.

    The creature's head, and indeed most of it's body, is roughly the shape of a dog's. However, it is the differences that are most noticeable.

    The colours exist in a semicircle, which looks to be somewhat like the consistency of an eye, but which takes up the entire top of the creature's head, starting from just below where a dog's eyes would normally be and moving all the way up and around, covering the entire area that would usually house a hound's brain.

    Weirdly, you are caught for a moment by the lack of ears, as the coloured portion of the head covers where they would usually be, but this is thrown from your mind when your eyes move down to the nose, or at least, where you had naively expected a nose to be.

    Instead you see something tapering, quivering from side to side, about four inches long, ending in a sharp point, the tip of which keeps opening and closing to reveal a minute, wet orifice.

    The creature moves slightly, and despite your macabre fascination, your eyes are drawn to the front legs. They're covered in the same silky smooth, pitch black fur as the rest of the animal, but that is where the similarities to normal dog legs end.

    You can tell just by looking at them, the way they twist around as the creature slowly repositions itself, that there are no bones in there. It's pure, incredibly strong, absurdly flexible muscle.

    Each limb is about five feet long, much longer than is needed for the creature, so they are coiled at the bottom. In other words, instead of front legs, it looks as if the creature is held up by boneless tails that it keeps curled into wide, flat disks.

    Possibly more shocking than all of this is that, as your gaze lifts up from these pads and scans back along the rest of the beast, you see nothing else unusual. The hindquarters are exactly what you would expect from an unusually uniformly black dog.
    """

    crier """

    She came back with me. After I'd spent the night with her, I helped her wrap up all her things in the blanket and I took her back here. It was clear she didn't want to be out there all by herself.

    I didn't do the wrong thing, did I?
    """

    menu:

        "Of course you did, you've brought a monster into our town!":
            $game.crier.like -= 1
            $game.crier.resp += 2
            $c=10

        "I suppose that it might be okay....":
            $c=10

        "If you like her, and trust her, then you did the right thing.":
            $c=11



if c==10:

    crier """

    I know you're worried about the rest of town, and I think that's probably the right thing for you to do, but I don't really know what's the right thing to do, but please trust me with her. I'll look after her, I promise. And I don't think she's dangerous.

    What I mean is, I don't think her … personality, I think that's the word, is bad, I think she'll be fine, but even if she isn't, I don't think she'd be very dangerous. She doesn't even have any teeth.
    """

    "Nat turns to the creature and waves excitedly at it."

    crier "Go on, show [game.player_name] you don't have teeth."

    $c=12



if c==11:

    crier "Oh thank you [game.player_name]! It really means a lot that you say that. (if respect and attraction are above a certain threshold)[I hope you won't mind me saying this, but I really respect your opinion [game.player_name]. And I, I just really wanted you to like her...](else if respect is above a certain threshold)[I hope you won't mind me saying this, but I really respect your opinion [game.player_name].](else if attraction is above a certain threshold)[I, I just really wanted you to like her…]"

    "Nat turns to the creature and waves excitedly at it."

    "[game.player_name] thinks that I did the right thing bringing you here. Why don't you give [game.player_name] a wave to say thank you!"

    $game.crier.like += 4
    $game.crier.att += 4

    $c=12



if c==12:

    """

    Maybe you should be inoculated to surprises by now. But you were not expecting what happens when the creature opens its mouth.

    The lack of teeth isn't a surprise. You trusted Nat's word on that.

    But what comes sliding out of the mouth is.

    It's pink and fleshy, slightly bumpy and wet. All like a tongue. But unlike a tongue, this thing has four fingers and a thumb.

    It waves at you.

    The hand that comes out of the dog-thing's mouth waves at you.
    """

    menu:

        "*Wave back*.":
            $c=13

        "That is disgusting.":
            $c=14

        "Scream.":
            $c=15

        "Just stare.":
            $c=16



if c==13:

    crier "It makes me very happy to see you two getting on so well."

    "Nat says this as the hand disappears back into the creature's mouth. It pads over to you, pushing it's soft fur against your hand."

    crier """

    She's really warmed to you. I think sh-.

    She should really have a name, don't you think?

    I don't think I'll be introducing her to anyone else for a while, but I still think she should have a name.

    Why don't you think of one? I wouldn't have met her if it wasn't for you.
    """

    #[game.player_name] gets the chance to input a name, unless we think that's too abusable in which case we can just come up with a list.

    crier """

    Okay, that's your name now, you hear?

    Oh, well I don't think she can hear, but I'm sure she'd like it if she could.

    Thanks for waving back [game.player_name]. I know that that can be quite, un...unsettling, is it? Well it can be quite shocking, to see that. But I don't think it's her fault that it's a little shocking.

    Thank you for coming round [game.player_name]. It means a lot. But I hope you don't mind if I tell you that I should probably get back to work. It's been difficult splitting my time between work and her.

    I really do hope you come back and visit me and [game.creature_name] some time soon. I think we'd both like it.
    """

    $game.crier.like += 8
    $game.crier.resp += 2

    return



if c==14:

    crier """

    I don't think she can help it. I think that's just the way that she is and I'm not sure it's nice to say that something that someone can't help is disgusting.

    Although I suppose poo and stuff like that is disgusting, and none of us can help that.
    """

    "Nat shrugs to himself."

    crier """

    Either way, I'm not surprise that you think that. I think it's what most people would think. That's why I'm not going to show her to anyone for a while. I want to spend some more time with her first, here, so that I can better tell people all the good things about her.

    Because I don't find her disgusting.
    """

    "Nat looks past you for a moment, clearly lost in his own thoughts, before he shakes his head and looks straight into your eyes."

    crier """

    I appreciate you coming over [game.player_name]. I know how odd these kind of things can be, so I hope you'll trust me when I say that if you give it a bit of time, it should all calm down.

    Once you feel better about her, do come back. I'm sure if you got to know her better, you'd get on more.
    """

    $game.crier.like -= 4
    $game.crier.att -= 4

    return



if c==15:

    "Nat grabs you lightly by the shoulders."

    crier """

    Hush now, hush now [game.player_name], it's all-right, it's all okay.

    She don't mean to scare you. That's just the way that she is.

    I can see why it's scary, but it's just part of her body, just like your hand is part of yours.

    And if you think about it, tongues are scarier than hands, if you really think about it. Although that might be just my opinion, because I can't rightly tell you why tongues are scarier than hands.

    I'm sorry, that probably isn't helping.

    Maybe it would be best if you just go. I need to get on with my work anyway.

    And don't worry, I'm not planning on showing her to anyone else any time soon. I want to spend some more time with her first, here, so that I can better tell people all the good things about her, so that they can be less scared by her odd things.
    """

    "As he's saying this, Nat is gently guiding you towards the door. The creature is nowhere to be seen, as it scampered up the stairs the moment you started screaming, the colours on its head rapidly flashing between yellow, grey and pink."

    crier """

    I appreciate you coming over [game.player_name]. Please do come back once the shock has died down a bit.

    I know how scary these kind of things can be, so I hope you'll trust me when I say that if you give it a bit of time, it should all calm down.

    Once you feel better, do come back. I'm sure if you got to know her better, you'd get on more.
    """

    $game.crier.resp -= 4

    return



if c==16:

    "Nat nods knowingly."

    crier """

    That's just about what I thought people would do.

    Actually I think they might want to do worse, some of them.

    I hope you're not too scared. Or disgusted. Because she's not scary or disgusting really, she's actually just lovely and kind.

    But I'm worried that people won't see that. People don't like giving things lots of time.

    That's why I'm not going to show her to anyone for a while. I want to spend some more time with her first, here, so that I can better tell people all the good things about her.
    """

    "Nat looks past you for a moment, clearly lost in his own thoughts, before he shakes his head and looks straight into your eyes."

    crier """

    I appreciate you coming over [game.player_name]. I know how odd these kind of things can be, so I hope you'll trust me when I say that if you give it a bit of time, it should all calm down.

    Once you've gotten over the shock, I suppose, when you feel better about her, do come back. I'm sure if you got to know her better, you'd get on more.
    """

    $game.crier.like -= 4
    $game.crier.att -= 4

return
