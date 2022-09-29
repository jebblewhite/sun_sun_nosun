label crierscene4: 

"You're walking through the centre of town when you see Nat, ashen faced and breathing heavily, lurching towards you."

crier "Oh, [game.player_name], thank the gods I found you. I need you to come with me, please, if you would, now. We need to go to the forest, I'll explain on the way."

"Uncharacteristically, Nat turns on his heels and starts walking back towards the forest without waiting for a reply. Not wanting to disappoint him when he is clearly very anxious about something, you jog forward a few steps to walk next to him."

crier """

There's a thing, [game.player_name]. I was out by the river, you know how I like to do that, and I saw a something in the woods. It didn't look like anything I'd ever seen before, it was like a light but it wasn't glowing. And it was changing colour, all these colours that I've only ever seen in clothes or butterflies before, like purple and bright orange and this kind of sparkling blue.

It scared me [game.player_name]. It didn't look right. I'm sure you or another brave person would have just walked right up to it, but I didn't want anything to do with it so I walked a little further on, but when I turned around it was there again, it'd moved through the woods to follow me.

It was about this big,
"""

"Nat holds his hands about twenty centimeters apart,"

crier """

and it moved slightly, like it was attached to something that was, that was following me. But whatever it was, it was dark, I couldn't see it in the darkness of the forest.

Well, I say I couldn't see it. I couldn't see it until after I'd ran, ran straight back to town, but just as I was coming to that bend in the river, you know, where you can start moving away from the woods for the first time, I looked back and it was still there. But I saw something else just under it.

[game.player_name], it looked like a hand. Like a small, human hand, but dark and wet, like, well, like…

Like it was covered in blood.

I didn't see no more after that. I just ran straight back here to find you.
"""

menu:

    "I'm sure it's nothing to worry about Nat, after all, it didn't attack you.":
        $c=3

    "Whatever it is Nat, I'll kill it for you.":
        $c=2

    "Really, that's it?":
        $c=1


label reevaluatecrier4:
if c==1:

    crier """

    I'm sorry [game.player_name], it is.

    I know I'm a coward, and I'm sorry about that, but I really think that someone should, I think, investigate this, and I think it should be you and I think it should be now.

    There's no-one else in town who would do it…
    """

    $game.crier.like -= 2
    $game.crier.att -= 2

    $c=4



if c==2:

    crier """

    I don't necessarily want it dead [game.player_name], I, I…

    I don't know. I was just scared and I thought that someone should, I think, investigate this, and I think it should be you and I think it should be now.

    But...so, thank you. Thank you for being brave.
    """

    $game.crier.like -= 2 
    $game.crier.resp += 2

    $c=4



if c==3:

    crier """

    Thank you [game.player_name]. I suppose I was too scared to think about that.

    It's called 'putting it in perspective', isn't it?

    But still, I think you, or we, had still better, I think, investigate this and I think it should be now. Even if it does turn out to be nothing bad.
    """

    $game.crier.like += 4 

    $c=4



if c==4:

    crier """

    I'm really very sorry [game.player_name], but being this awful frightened and running and talking and keeping the count is all too much.

    I wish I could do something about the fear by myself, but I can't, I have to keep running because otherwise the fear might get too much more than it already is, and the last thing in the world I want is to lose my count. So do you mind if we just run [game.player_name]? Since I've told you the whole story and all?
    """

    """

    You don't really have any other choice but to nod, and the two of you jog towards the edge of the forest that borders the river.

    It doesn't take long. You haven't even reached the tree line when Nat grabs your arm with shaking fingers.
    """

    crier "There! Oh [game.player_name], you must see the colour, the bright pink!"

    """

    Yes. Yes, there it is, between two trees. A patch of unnatural pink, a fringe of orange on one side, a muddy yellow on the other.

    Then it's gone in a rippling of darkness.
    """

    crier "You saw it, yes [game.player_name]?"

    menu:

        "It was just a patch of colour Nat, nothing to be afraid of. I'll look after you.":
            $c=5

        "It's definitely some kind of unnatural beast. But I'm not afraid to hunt it.":
            $c=6

        "I saw something, yes. Let's go investigate. Together.":
            $c=7



if c==5:

    crier "Okay [game.player_name]. I'm not sure your words are helping much, but I appreciate them all the same."

    $game.crier.like += 2

    $c=8



if c==6:

    crier "Let's just look for it first, if that's all all-right [game.player_name]?"

    $game.crier.resp += 1

    $c=8



if c==7:

    "Nat opens his mouth as if to say something, and then closes it again, smiles and nods."

    $game.crier.att += 4

    $c=8



if c==8:

    """

    You move forward cautiously. Nat wraps his thin fingers around your arm as you step through the tree line and into the forest. You're quickly swallowed up within it, the world reduced to nothing but the darkness immediately in front of you.

    You walk for some minutes in near silence, the only thing that breaks your cover is the occasional whimper from Nat. You, however, are just beginning to calm: you cannot help but feel used to these dark woods by now.

    It is because of this calm that you barely even notice the sound of crashing somewhere close ahead of you. You know perfectly well that it is a wild pig, or young deer, creating the noise that you would usual celebrate as the sign of a good hunting session.

    But it occurs to you a moment too late that Nat does not share your familiarity of these woods. Before you can explain, Nat's grip on your arm has gone and you hear him thundering through the forest in just the wrong direction to head back to the river bank.

    You turn away from the suddenly fleeing animal to pursue a much more important quarry: Nat. It shouldn't be too hard.

    Or at least, that is what you think. You soon discover that your belief that all you had to do was catch up with Nat was misguided. At some point in his flight, he must have realised he was going the wrong way. At which point, presumably, his instincts told him to give up on the flight, and instead simply hide.

    And he's hiding better than you would have expected, although given that he had quite a significant head start on you, and was running faster than you would have advised in the dark forest, maybe anyone could have concealed themselves this well here.

    It is only at the point where you would have given up had this been a child's game of hide and seek that you find something.

    Swirling brown, orange and yellow, bright but not actually a light. Always just moving out of sight.

    Always close.

    And getting closer.

    There's darkness near it, a darkness that is part of it. Blacker than the sky, blacker than black. And large. It's difficult to tell whether it's the size of a dog or a horse.

    Once, you can hear it breathing. Rough gasping. A growling rasp.

    It's on you.

    Jumping out at you, a sudden noise that your mind doesn't have time to process as your arms bring up the bow you had not realised you were holding ready to fire.

    Part of you realises that the thing, right there in your path and moving quickly and erratically, has the wrong shape.

    It has a shape you recognise.

    But the fear is in your throat and your arms are pulling back the string of your bow no matter what you think.

    Until they aren't. Something blind-sides you.

    Something thick and strong, but boneless wraps around your arm.

    Pure muscle.

    It shoves downwards and your knees give way.

    You hear a scream.

    No, two.

    You and Nat.

    Then the colours are all you can see, an erratic flashing through of red, grey, pink and vibrant black.

    A...hand pulls your bow from your grip.

    It is the last thing that you feel before your control rushes back to you.
    """

    menu:

        "*Punch out at the beast in front of you*.":
            $c=12

        "*Try to pull yourself free so you can run*.":
            $c=11

        "*Grapple with the animal and shout for Nat to run*.":
            $c=10

        "*Scream for help*.":
            $c=9



if c==9:

    """

    You open your mouth and let your fear and panic out. The colours recede rapidly, and you can see the outline of the beast skitter away from you

    Towards Nat.
    """

    $game.crier.resp -= 2
    $game.crier.att += 2

    $c=13



if c==10:

    """

    You reach out towards the creature as you cry for Nat to run, but the fur of it's body is too smooth and your hands simply slip off as the creature skitters away from you.

    Towards Nat.
    """

    $game.crier.resp += 4
    $game.crier.like += 4

    $c=13



if c==11:

    """

    You pull yourself away from the creature easily.

    Too easily.

    You turn just in time to see it skittering away from you.

    Towards Nat.
    """

    $game.crier.resp -= 4
    $game.crier.like -= 4

    $c=13



if c==12:

    """

    You pull your fist back and let it fly straight into the furry body of the creature. There is a satisfying thump, but the lack of give indicates quickly that you have done no damage at all.

    Nonetheless, the creature reacts to your aggression and skitters away.

    Straight towards Nat.
    """

    $game.crier.resp += 1

    $c=13



if c==13:

    """

    It stops, the flashing colours facing you.

    A low growl.

    Having already tried running and hiding tonight, Nat freezes.

    Stillness.

    And then, slowly, you see Nat's hand reaching out, even as his eyes stare blankly forwards with horror.

    At Nat's touch, the creature arches its back up into Nat's fingers and begins rippling gently back and forward, again and again.

    Until it is clear that Nat is stroking it.
    """

    menu:

        "*Slowly attempt to stand up*.":
            $c=18

        "*Try to reach for your bow*.":
            $c=14

        "*Slowly hold your hand out to it*.":
            $c=21



if c==14:

    """

    While staring into the colours, positioned on the top of the creatures head where you would normally expect to find eyes, you move your hand across the forest floor, feeling for your bow.

    The moment that you feel its carved wood with the tips of your fingers, the creature's body twitches. You see movement at the bottom of its front...legs, movement like the uncoiling of a sleeping snake, and then a flick, and the thing is standing on its back legs, a full six feet tall at least, awkwardly shuffling between you and Nat.

    The colours at the top of the thing's head start flashing quickly: red, orange, briefly black and then red, orange, briefly black.

    It's growling, the same threat given by every dog you've ever crossed.
    """

    crier """

    I don't know what you're doing, but just stop [game.player_name].

    You're making it nervous.
    """

    menu:

        "*Let go of the bow*.":
            $c=16

        "*Try to shoot it*.":
            $c=15



if c==15:

    """

    Disregarding Nat's plea, you shoot your hand out for the bow, move skilfully into a crouched position, and see something almost fluid whip around from the side of the monster's body.

    You don't have time to react.

    Something strong and uniformly solid smashes into your head, partly moulding to the shape of your skull and driving you sideways until your head meets the side of a tree and then…
    """

    $game.crier.resp -= 2
    $game.crier.like -= 2
    $game.crier.att -= 2

    $c=22



if c==16:

    """

    You move your hand away from the bow. The creature waits a moment, swaying unsteadily on it's hind legs, before it falls back onto all fours.

    Then, leaving you lying on the ground, it turns and gently, with one of its long, seemingly infinitely flexible front limbs, reaches up to tug on Nat's shirt.
    """

    crier """

    I think, I think it wants me to follow it [game.player_name]. I think I should go with it. And I think it wants you to stay here.

    So, um, please stay here. I don't want you to get hurt.
    """

    "Nat is clearly scared, but there's something else there as well. You think it might be excitement."

    menu:

        "Nat, I'm not leaving you behind *grab your bow*.":
            $c=15

        "Only if you're sure Nat.":
            $c=17



if c==17:

    crier """

    You know, I know this sounds strange [game.player_name], but I am.

    And I don't mean any offence by this at all, so please don't take it the wrong way, but I do actually think that I will be safer on my own than with you.

    So I'm going to walk off now. You stay there for a minute or two, just rough, you don't have to keep that time exact, and then feel free to head back to town.

    Hopefully I'll see you soon.
    """

    "And, with a slight wave, Nat turns, following the creature as it slowly makes a path for him through the forest."

    $game.crier.like += 4

    return



if c==18:

    """

    You move your hands underneath you, but as you start to slowly push upwards, the creature twitches.

    You see movement at the bottom of its front...legs, movement like the uncoiling of a sleeping snake, and then a flick, and the thing is standing on its back legs, a full five feet tall at least, awkwardly shuffling between you and Nat.

    The colours at the top of the thing's head start flashing quickly: red, orange, briefly black and then red, orange, briefly black.

    It's growling, the same threat given by every dog you've ever crossed.
    """

    crier """

    I don't know what you're doing, but just stop [game.player_name].

    You're making it nervous.
    """

    menu:

        "*Stand up fully*.":
            $c=19

        "*Lie back down*.":
            $c=20



if c==19:

    """

    Disregarding Nat's plea, you move fluidly into a crouched position, ready to spring up, and see something almost fluid whip around from the side of the monster's body.

    You don't have time to react.

    Something strong and uniformly solid smashes into your head, partly moulding to the shape of your skull and driving you sideways until your head meets the side of a tree and then…
    """

    $game.crier.resp -= 1
    $game.crier.like -= 1
    $game.crier.att -= 1

    $c=22



if c==20:

    """

    You slowly lower yourself back down. The creature waits a moment, swaying unsteadily on its hind legs, before it falls back onto all fours.

    Then, leaving you lying on the ground, it turns and gently, with one of its long, seemingly infinitely flexible front limbs, reaches up to tug on Nat's shirt.
    """

    crier """

    I think, I think it wants me to follow it [game.player_name]. I think I should go with it.

    And I think it wants you to stay here.

    So, um, please stay here. I don't want you to get hurt.
    """

    "Nat is clearly scared, but there's something else there as well. You think it might be excitement."

    menu:

        "Nat, I'm not leaving you behind *grab your bow*.":
            $c=15

        "Only if you're sure Nat.":
            $c=17

    jump reevaluatecrier4



if c==21:

    "You slowly extend your hand towards the creature. The colours, an orb that makes up the upper portion of its head, change to swirling reds, yellows, pinks and blues.

    Then the bottom of one of its front...legs moves, like the uncoiling of a sleeping snake, and it extends what looks like a muscular, apparently infinitely flexible, tail. The hair here is rough and muddy, but still incredibly smooth as the creature gently runs the tip of its this front limb across each of the fingers of your hand in turn.

    And then, slowly, it pulls the limb back, curling it up like a coil of rope as it does so, placing it beneath itself so that it can bear weight.

    Then, leaving you lying on the ground, it turns and gently, with one of its long, seemingly infinitely flexible front limbs, reaches up to tug on Nat's shirt.
    """

    crier """

    I think, I think it wants me to follow it [game.player_name]. I think I should go with it. And I think it wants you to stay here.

    So, um, please stay here. I don't want you to get hurt.
    """

    "Nat is clearly scared, but there's something else there as well. You think it might be excitement."

    $game.crier.resp += 2
    $game.crier.like += 2
    $game.crier.att += 2

    menu:

        "Nat, I'm not leaving you behind *grab your bow*.":
            $c=15

        "Only if you're sure Nat.":
            $c=17

    jump reevaluatecrier4



if c==22:

    """

    You wake up.

    There are the sounds of other people around you: groaning, hushed conversation, the movement of bedsheets.

    You open your eyes to see Fyodora standing above you.
    """

    doctor "Oh good, you're awake. And within the time frame I was hoping for. That's a good sign, it probably means you've only got mind concussion."

    """

    Yes, that sounds about right. Your head hurts, but not so much that you believe anything is permanently damaged.

    Fyodora doesn't let you ask any questions until she's checked you, but even after she says that you're all clear, she doesn't have many satisfying answers.

    It seems that Nat, somehow, managed to drag you out of the woods. He'd run to Fyodora's, told her where he had left you, and then said that he had to leave because he had 'things he needs to do in the woods'.

    And then he'd said that he really hopes that you are okay, and run off.

    That was just a couple of hours ago. And, Fyodora adds as she dismisses you from her hospital, no-one has seen him since.
    """

return