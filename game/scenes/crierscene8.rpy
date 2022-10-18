label crierscene8: 

"""

Screams.

Some of terror, some of shock.

Instinctively, you race towards the sound.

Shouting.

Yelling.

The screams change, become an aftershock, shape shift into fearful weeping.

Another scream, anguish, desperation.

You turn into the town square.

Nat is on his knees, tears streaming down his face, his hands covered in dirt as he snottily begs at Fyodora's feet.

A child, about ten or eleven, bleeding from a badly scraped knee, wiping dust out of his crying eyes.

A group of workers, strong and muscled, holding a net.

A cleaver.

And [game.creature_name], caught in the middle of it all, pinned to the ground but still struggling to get to Nat, who begs for her life.
"""

crier "Please miss doctor! Please! She didn't want to harm no-one, she barely even did, please, please!"

"Nat's words are a scream, his pain and fear slicing through the quiet town."

crier "She's my only friend Fyodora, she's good and kind! Please don't kill her, you can't kill her!"

"Fyodora shakes her head."

doctor "It's a monster Nat, and it attacked a child. We can't-oh, [game.player_name]. You'll help me with this, won't you. It seems-"

crier "They're going to kill her [game.player_name]! Don't let them kill [game.creature_name]! Please, please!"

menu:

    "What's going on here?":
        $c=2

    "I don't know what you're talking about. Fyodora, why don't you tell me what's going on?":
        $c=1

    "Good, it's about time someone finally did something about that monster.":
        $c=3

    "You can't kill [game.creature_name]! I'm sure that this is all a misunderstanding.":
        $c=4



if c==1:

    """

    Nat pauses in his wailing for just a moment, looking up at you with a face twisted by confusion.

    But once he has realised your betrayal, he pushes his hands hard into his eye sockets and curls up into a wailing, shivering ball.
    """

    $game.crier.like -= 8
    $game.crier.resp -= 8

    $c=2



if c==3:

    crier "No no no no!"

    "Nat wails, beating his fists against the ground. Fyodora smiles sadly at you, resolve overcoming the deep concern in her eyes, before shaking her head."

    doctor "You're probably right."

    $game.crier.like -= 8

    $c=2



if c==4:

    crier "Exactly, yes, tell her [game.player_name], it's all a mistake!"

    "Fyodora shakes her head sadly."

    doctor "I don't think so."

    $game.crier.like += 4
    $game.crier.resp += 4
    $game.crier.att += 4

    $c=2



if c==2:

    doctor """

    I saw the whole thing [game.player_name].

    Nat was doing his rounds when Bretik approached to say something to him.
    """

    "Fyodora indicates the child, still lying on the ground and nursing his bloody knee."

    crier "You didn't see everything! He was, he was calling me mean things! And he threw a rock at me! That's the only reason [game.creature_name] did anything. She was just trying to protect me!"

    "Fyodora frowns slightly."

    doctor """

    Well I didn't see that, but I suppose I could have missed it. But regardless of the provocation, this monster suddenly appeared out of one of the side streets, picked up Bretik with one of its...legs and threw him to the ground.

    Who knows what it would have done next, but luckily there were enough people in the square to contain it.

    Then Nat started crying. He says that the monster is his friend, that-
    """

    landowner "What's all this?"

    "Fyodora turns towards the interruption to see Elisabeta walking confidently towards you, her head cocked quizzically to one side. She frowns at Nat and lifts her gaze up towards Fyodora, but does not give the doctor time to react before she lets out a little shriek of excitement."

    landowner "My, what is this wonderful thing!"

    "Without waiting for an answer, Elisabeta skips towards [game.creature_name] and her captors."

    landowner "Why, aren't you a magnificent creature?"

    """

    Elisabeta, probably instinctively, waves at [game.creature_name].

    There is a scream of terror and a shriek of delight.

    Fyodora is recoiling in horror while Elisabeta jumps up and down.

    [game.creature_name] opened its mouth and waved back.
    """

    landowner "It's intelligent! Or at least it can mimic behaviours! What a marvel!"

    doctor "Its tongue is a hand!"

    landowner "Yes, curious isn't it? Oh it is amazing what biological marvels this night is producing!"

    crier "Don't let them kill her miss Elisabeta! Please, please stop them!"

    "Elisabeta turns towards Nat, clearly surprised to see him still grovelling in the dirt. Slowly she lifts her head, taking in the whole scene around her, for the first time consciously noticing more than just [game.creature_name]."

    landowner "You aren't seriously considering killing this specimen, are you?"

    menu:

        "Wait, this is all happening too fast, we should all calm down and think before doing anything we might regret!":
            $c=5

        "I know [game.creature_name]. She really is good and kind, and less aggressive than many dogs.":
            $c=7

        "I don't care about anything else: that thing is an unnatural monster and we would be fools if we kept it alive.":
            $c=9

        "You can't kill it! You can't do that to Nat.":
            $c=7

        "We don't have to kill her. I don't like having her in our town, but I trust her enough that if we made her leave, she would stay away.":
            $c=8



if c==5:

    #MM: the resp value here should be appropriate to Doctor scene 4 or thereabouts.
    if game.doctor.resp > 10:
        $textinsert = "I trust you {}.".format(game.player.name)
    else:
        $textinsert = "I will accept {}'s decision.".format(game.player.name)

    """

    There is a moment of tension, everyone unsure of how to proceed. When finally someone does move, it is [game.creature_name].

    Very slowly, she lowers herself down, her front limbs first and then her back, until she is lying on the ground, no longer struggling against the grip of the villagers.

    Fyodora's frame relaxes slightly, and seeing this, the fisherman holding the cleaver gently pulls his arm back down to his side.

    Elisabeta smiles encouragingly, first at Nat, then at you, then at [game.creature_name].

    Nat reacts last, his fists slowly unclenching from the balls of panic he had bunched them into. Tears still run down his face, and his eyes still dart from side to side, but his breathing evens out slightly and you can see tension slowly releasing from his shoulders.
    """

    doctor "Fine, perhaps we should talk it out. Nat, why don't you start by telling us your...relationship with this creature?"

    """

    Nat, through sobs and fearful twitches, recounts the story of how he, and you, met [game.creature_name], how she has been living in the belltower and how the two of them now play and generally keep each other company.

    Fyodora listens to the entire tale with her hands on her hips, while Elisabeta unashamedly copies everything Nat says into a small notebook, occasionally interrupting to ask questions.
    """

    crier "So she's not dangerous, she's lovely and kind and thoughtful! Just because she's different doesn't mean that she can't be my friend!"

    landowner """

    This all really is fascinating. She does sound like a very clever girl! She could tell us so much about the night. I've found no records of any creature as intelligent, we could find out so much from the way that she thinks.

    And that hand, or tongue, or whatever it is! I would love to get a proper look at that. It appeared so human! Think of the implications of that!

    Oh there are so many questions, we can't possibly throw away the opportunity to answer them!
    """

    "Nat clearly does not quite know what to make of Elisabeta's words and before he can make up his mind Fyodora speaks."

    doctor """

    I have heard all you have both said, but I know what I saw.

    This creature attacked a child.

    Yes, the boy seems relatively unhurt, and maybe he was teasing you Nat, but fundamentally that thing is some kind of monster.

    Elisabeta, you said \"think of the implications\" of its tongue. Indeed, where did it come from? Because there is no way it occurred naturally. So it must have come from a human. Did this creature copy it from us, or did its creator use a human hand in its creation? If there is a hand, where is the rest of the body?

    This is a being of the night, a night that has done nothing but weaken and kill us.

    I am sorry Nat. But it is my opinion, as the doctor of this town, that this creature cannot be allowed to stay here.

    It is too alien. There is just no saying what it will do.
    """

    "Nat had started weeping and screaming before Fyodora had even finished talking."

    crier "[game.player_name], [game.player_name] please! It's not up to miss doctor, is it? Please please tell her she can't kill [game.creature_name]. She has to listen to you, you're an important person!"

    "Fyodora turns to you and, after a moment's hesitation, nods."

    doctor "[textinsert]"

    $game.doctor.resp += 1
    $game.landowner.resp += 1
    $game.crier.resp += 2

    menu:

        "Just let [game.creature_name] go!":
            $c=6

        "Fyodora is right, [game.creature_name] cannot live here. But she doesn't have to die either. I trust her enough that if we make it clear she isn't welcome here, she will leave and not return.":
            $c=8

        "Fyodora is right. [game.creature_name] needs to die.":
            $c=9



if c==7:

    doctor "That may be true, but-"

    crier """

    Oh please miss doctor, you have to listen to [game.player_name]! [game.player_name]'s an important person, the Alderman said so! Oh please please, you have to you have to!

    Please don't be evil, please be kind!
    """

    $c=6



if c==6:

    $game.doctor.resp -= 2
    $game.crier.like += 8
    $game.crier.att += 8
    $ame.crier.creaturefate = "Alive"

    "Fyodora stares at you for several seconds, and then bows her head."

    doctor "This is a mistake [game.player_name]. This monster should not be allowed free reign of our town."

    "She shakes her head, and then turns to the townspeople holding [game.creature_name] down."

    doctor """

    I am sorry.

    But let it go.
    """

    """

    Some slowly, some quickly, they all step away from [game.creature_name].

    [game.creature_name] waits till they are all several steps away before pushing herself up and bounding across to Nat, who, crying and laughing, welcomes her with open arms.

    Both man and beast fall to the dirt, neither willing to be the first to let go. Nat's body vibrates with relief and you are worried that he might pass out, but you know that if he did, [game.creature_name] would be there to care for him.

    By the time that Nat eventually sits up Fyodora has already left, and Elisabeta has, finally, moved a respectful distance away, although she is still furiously taking notes.
    """

    crier "Oh thank you [game.player_name], thank you thank you thank you!"

    "Nat is weeping again now, his breaths long and deep."

    crier """

    I really, I really don't think I have the words for how I would have felt...what I would have done. (maybe some way to make the text box transition last a beat longer?)

    Oh [game.player_name], thank you!

    I owe you everything.
    """

    if game.crier.romance == True:

        crier"""
        
        You are far too kind to me [game.player_name]. I really must be the luckiest person in the world, to have someone like you. I don't know what I did to deserve all of this, but it all makes me very happy.

        I'd like to come back to yours, if that's okay? Now that people have seen [game.creature_name], I can go through town with her, and your place is so nice and warm and cosy.

        I…I think I just want to lie down. Can [game.creature_name] and I come back to yours [game.player_name], and all just lie on your bed for a while? I think that's what I would like to do most in the world.
        """

        return
        
    else:
        
        crrier "But for now, if you don't mind [game.player_name], I think that we should leave. Me and [game.creature_name], that is. All these people are staring at her, and that man...that man with the…"

        "You follow Nat's gaze to see that the man who had held the cleaver above [game.creature_name]'s neck is still in the square, watching you throw narrowed eyes."

        crier """

        Well, I think it would be best if we left. People have seen [game.creature_name] now, and that's good, but I think they might need a bit more time, you know?

        But thank you, again that is.

        For saving us.
        """

        return



if c==8:

    "Nat buries his head in the dirt and weeps. But he no longer screams."

    crier """

    I'll do it. Oh you evil people, you are destroying my life, but I will do it! I will do it for her.

    But let me say goodbye! Please [game.player_name], let me say goodbye!

    I promise I'll keep her locked in the belltower until it's time. But I'm not ready yet.

    I promise, when I'm ready, I'll do it [game.player_name]. And she won't get out until that time. But not now, not just yet.

    Please [game.player_name]. Please miss doctor.

    Please, give me time to say goodbye.
    """

    "Fyodora looks uncomfortably at the ground, but eventually lets out an angry sigh and gives a little nod."

    doctor "I think this is a mistake Nat. But it is your decision to make. And I promise that I will treat you, if it does anything. But only, only if you promise that you will keep it locked up until you send it away."

    """

    Tears streaming down his face, Nat promises. He stands up and slowly approaches [game.creature_name], looking nervously not at the beast, but at the people holding her.

    [game.creature_name] simply watches him come. It is impossible to know if she understands what has been decided.
    """

    doctor "You'll take that thing back to the belltower?"

    "The villagers nod to Fyodora's question, and she indicates that they should go."

    landowner "Ahem, what about my study of the creature? It's just that if we are-"

    """

    Nat does not say anything, but the look that he gives Elisabeta silences her. She shakes her head, clearly disappointed, but does not press the matter.

    The villagers begin to carry an unresisting [game.creature_name] away.
    """

    $natrelationshipmatrix = (game.crier.resp + game.crier.like + game.crier.att)/3

    if game.crier.romance == True:
        
        "Nat looks at you, his head gently shaking from side to side."

        crier """

        I hoped...I hoped that you would have helped me.

        After what you've said, I hoped you would understand.
        """

        "And with that he turns and hurries after his friend."

        $game.crier.like -= 4
        $game.crier.resp -= 4
        $game.crier.att -= 4
        
    else:
        
        "Nat turns to you, his eyes shining with tears."

        if natrelationshipmatrix > 14:
            
            crier "I thought you loved her too [game.player_name]?"

            "And, without waiting for your reply, Nat hurries after his friend."
            
        else:
            crier "I suppose thank you, for doing what you could."

            "And with that he turns and hurries after his friend."

        $game.crier.like -= 4
        $game.crier.att -= 4
        $game.crier.resp -= 2

    $game.crier.creaturefate = "Exiled"

    return



if c==9:

    """

    Nat stares at you for several seconds, uncomprehending.

    And then he screams.

    Unintelligible sounds, primal sounds, fear and loss beyond language.

    Fyodora nods while Elisabeta attempts to make her polite objections heard over the sound of Nat's world being torn apart.

    The doctor mumbles something, an unheard apology to Nat, before turning to the man who holds the cleaver.

    Suddenly Nat is on his feet, running faster than any of you thought possible.

    He slides in the mud, crashing undignified into [game.creature_name] just as the cleaver comes down.

    His fingers bury into her eye, his screaming, twisted, red face pointed up at the executioner, begging for his friend's life.

    But the cleaver is already coming down. It is too late to stop it.

    One of Nat's hands comes up instinctively to block the blow, but you see in that moment he has accepted what is about to happen to him.

    For just an instant, he is at peace.

    Someone, you are never sure who, screams.

    And then Nat flies. One of [game.creature_name]'s limbs pushing him across the ground.

    Away and to safety as the cleaver comes down.

    It is an odd thing to note, but even in the starlight you can see that [game.creature_name]s's blood is red.

    The same scarlet as your own, sinking into the dirt of Lotosk's town square, splashes staining the fabric of Nat's clothes.
    """

    $game.crier.like -= 16
    $game.crier.resp -= 16
    $game.crier.att -= 16
    $game.doctor.resp += 2
    $game.landowner.resp -= 1
    $game.crier.creaturefate = "Dead"

return
