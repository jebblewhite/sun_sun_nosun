label butcherscene2:

$Mik2Destructive = False
$Mik2Total = False
$Mik2Final = False
$Mik2Nationalism = False
$Mik2Globalism = False
$Mik2Militarism = False

"""

You enter the butcher's shop and are greeted immediately by the muffled sounds of someone … actually you're not sure what the sound is. All you can say is that it is wet and dull. Maybe it is just your assumptions, but the sound makes you think of the word 'flesh'.

A grunt from the back room lets you know that Mik is aware they have a customer, but it still takes several minutes before they appear, hands slick and dark with gore.

Mik seems genuinely surprised to see you for a moment, before they pull their face back into its normal sardonic scowl.
"""

if game.butcher.scene1result == 'Mad':

    butcher """

    Come to sneer?  Come to gawp?  Come to stretch your intellectual muscles in my face?

    Or come to admit that you're a bigot?

    Come to grovel and beg forgiveness for being both wrong and, dare I say it, rude?

    So go on, tell me.  How wrong do you think I am?  And try to use your grown up words this time.
    """

elif game.butcher.scene1result == 'Disagree':

    butcher """

    So the student has returned. I'm a little surprised, but it appears you're more stubborn than I had given you credit for.

    Or maybe more argumentative.

    Or maybe you just wanted to see little old me.
    """

    "Mik holds the back of their hand to their chin as they say this, framing their face."

    butcher """

    Don't tell me, I like the mystery. Also knowing you I'll be disappointed by the answer.

    What I am more interested in hearing though, because very few people who aren't already singing in my choir will listen to me long enough to debate me intelligently, is how wrong you think I am, now that you've had a little longer to think?
    """

elif game.butcher.scene1result == 'War':

    butcher """

    Ah, the class traitor is back.

    Come to sneer?  Come to gawp?  Bring your pitchfork?

    Or come to admit that you're an idiot?

    Come to grovel and beg forgiveness for being both wrong and, dare I say it, rude?

    So go on, tell me.  How wrong do you think I am?  Changed your mind?
    """

else:

    butcher """

    So the student has returned. Come to further the cause?  Or maybe you just wanted to see little old me?
    """

    "Mik holds the back of their hand to their chin as they say this, framing their face."

    butcher """

    Don't tell me, I like the mystery. Also knowing you I'll be disappointed by the answer.

    What I am more interested in is if you're changed your mind.  Are you still with me?  Totally?  Am I wrong?
    """

menu:

    "You're just wrong, about all of it.":
        $c=3

    "You're right about the evils of the state, but liberal capitalism is how we will emancipate ourselves. It isn't the enemy.":
        $c=1

    "You're right about the evils of the bourgeoisie, but the state is how we protect ourselves from them.":
        $c=2

    "You're right, the proletariat are all slaves to both the state and the bourgeoisie.":
        $c=4


label reevaluatebutcher2:
if c==1:

    butcher """

    So says the liberal propaganda. But it isn't true.

    Yes, the rise of personal property did lead to emancipation from the state.

    But it only led to the emancipation of a very specific class: the bourgeoisie. They were, and still are in the Kingdom, revolutionary, but their revolution would simply see one set of oppressors replaced with another.
    """

    $game.butcher.like -= 2
    $game.butcher.resp += 1

    $c=5



if c==2:

    butcher """

    Naive.

    Also apparently deaf. I covered this last time we spoke. You're thinking short term. But that isn't how states work. Power can only be good for the people for a limited time.

    Yes, a state that truly has the interests of the working person at heart may save, at best, a generation of proletarians, but people change while power structures don't.

    I said all this last time, about the state's need for conservatism and, therefore, eventually, despotism.

    No, political revolution is a mistake, it's just swapping out today's oppressor for tomorrow's, which, in the long term, is pointless, regardless of how shiny and new the new model is, or how appealing what it says on the box happens to be.
    """

    $game.butcher.like -= 2
    $game.butcher.resp -= 2

    $c=5



if c==3:

    butcher """

    You do realise that one of the best ways to convince someone of your way of thinking in a debate is to start by acknowledging common ground. Not only does it soften them up, always useful, but it also gives you both a common baseline.

    So let me try. You care about yourself, right? Don't worry, that's not the attack that it so obviously sounds like it is, we all do it.

    So we both care about ourselves. We don't want to die. So take it from a fellow self-interested human: the revolution is the answer.

    For me, and the rest of the proletariat, freedom and equality will mean we no longer die at the hands of uncaring factory owners or power-hungry generals.

    But for you ... well ... as long as there are inequalities of power, there will be people wanting to dethrone the powerful.

    Political revolutions happen all the time. Every day the Senate, at some level, sees coups and skirmishes. 'The state' doesn't care about you, it will continue to wallow no matter which individuals it is made up of. So nothing will protect you when someone comes along wanting your place.

    Either that, or a revolution, political or otherwise, with a little more teeth comes along and you're the first to be strung up, ruining the natural beauty of the village's biggest tree.

    Much better to join the inevitable, and final, social revolution than fall victim to it.

    You see, the revolution I endorse is not #{i}a#{/i} revolution, it is #{i}the#{/i} revolution.
    """

    $game.butcher.like -= 2

    $c=5



if c==4:

    butcher """

    I'm surprised. Mostly by the fact that you'll say that to me while still working for the Alderman. Still, better a self-deluded, hypocritical bourgeois socialist than no socialist at all.

    Don't bother explaining to me how what you're doing isn't statist, that you're just doing what's best for the survival of the village. We can deal with your own little lapses in logic another time. I want to take this opportunity to bang on about something more fundamental.

    Revolution.

    """

    $game.butcher.like += 2

    $c=5



if c==5:

    butcher """

    The point shouldn't be revolution for the sake of revolution, although everyone does like a spot of excitement from time to time.

    No, the aim is not to bring down #{i}the#{/i} state. It is to bring down 'state' as a social construct.

    The idea is not to destroy the oppressors. It is to destroy #{i}oppression#{/i}.

    The revolution I call for is total, final and destructive.
    """

    menu:

        "Why destructive?":
            $c=6

        "Why total?":
            $c=30

        "Why final?":
            $c=34



if c==6:

    butcher """

    Because the revolution I call for is social, not political. As I said, we aim to abolish private property and the state, not just instances of each, but the very concept of them as social institutions.

    And while I believe that both are chains holding the working people of this world back, I'm not blind to the fact that breaking chains is an act of destruction. However evil the state and the concept of bourgeois capital are, they are still 'things', things that have defenders and, at times, their own volition.

    When it comes to certain ideas, the difference between 'removal' and 'destruction' is simply semantic. Given the choice, I'll take the hard honest truth of 'destroy' over the deceptive 'remove'.

    So the revolution must be destructive because I refuse to talk about changing the state. I will speak only of destroying it. This is where I differ from most other revolutionaries, even most other socialists.

    The communists could achieve their goals through purely political means. It's why there is a communist party, and communist senators. They dream of an all-powerful proletariat state, and they could, theoretically, and I really do mean theoretically, achieve that dream by bending and twisting our republic until it is more or less the shape they want.

    They want a 'dictatorship of the proletariat'. But how can one dictate unless there is someone taking down your dictation?

    Sorry that sounded better in my head.

    For all the reasons that I explained last time we talked, the state must be destroyed. Not subverted, not 'changed from the inside'. Brought down, probably with violence, from the outside. Because trying to destroy politics with politics will never work. States are fundamentally self-preserving, they will never be persuaded to destroy themselves.

    Besides, fighting politics with politics? It even sounds like a fallacy.

    As for the bourgeoisie, it is already too late, in our Republic at least, to settle #{i}that#{/i} peacefully. They're too tied up with the state, its property and tax laws protect them and their money feeds it.

    You go after the state and the bourgeoisie might just let you pass, but attack the bourgeoisie and the state will crack down. Like an obedient dog, it knows where its food is coming from.
    """

    $Mik2Destructive = True

    menu:

        "So the only way to create your Utopia is through destruction and death?":
            $c=11

        "Wait, comparing the state to a dog? That's a bit cruel to dogs isn't it?":
            $c=7

        "I understand the need for sacrifices. Sometimes things need to be broken.":
            $c=16



if c==7:

    butcher """

    Have you seen dogs? No backbone. Any animal that will obey any master without hesitation, any creature that eager to please isn't something I want around me.

    It's just sad.

    And before you ask, because I'm sure you've already decided that I conform perfectly to the stereotype, I had a cat when I lived in Alexisgrad.

    Not all stereotypes are wrong, unfortunately.
    """

    $game.butcher.att += 2

    menu:

        "Oh I love cats. Why don't you have a cat now?":
            $c=8

        "Of course you'd have a cat. I suppose you had to have #{i}one#{/i} friend.":
            $c=9

        "Dogs are so much nicer though. Why have a pet if it's not going to like you?":
            $c=10

        "Back to the matter at hand: you're saying the only way to create your Utopia is through destruction and death?":
            $c=11

        "Back to the matter at hand: I understand the need for sacrifices. Sometimes things need to be broken.":
            $c=16



if c==8:

    butcher """

    Cats and butcher's shops are an excellent mix.

    Shall we return to the matter at hand?
    """

    $game.butcher.like += 2

    menu:

        "So the only way to create your Utopia is through destruction and death?":
            $c=11

        "I understand the need for sacrifices. Sometimes things need to be broken.":
            $c=16



if c==9:

    butcher """

    Ha. Witty.

    Shall we return to the matter at hand?
    """

    $game.butcher.att += 2

    menu:

        "So the only way to create your Utopia is through destruction and death?":
            $c=11

        "I understand the need for sacrifices. Sometimes things need to be broken.":
            $c=16



if c==10:

    butcher """

    Because I don't feel the need to have a little furry slave around to make me feel like I'm important.

    I don't want to buy love. I want to earn it.

    Anyway, shall we return to the matter at hand?
    """

    $game.butcher.like -= 1

    menu:

        "So the only way to create your Utopia is through destruction and death?":
            $c=11

        "I understand the need for sacrifices. Sometimes things need to be broken.":
            $c=16



if c==11:

    butcher """

    Theoretically? No. The bourgeoisie and the statists could recognise the injustice of their actions and step aside. Institutions don't bleed, it is only their defenders who do that.

    But practically, realistically? Yes. I wish it wasn't the case, but yes.
    """

    menu:

        "Ever worry that if you have to kill people who don't agree with you, you might be in the wrong?":
            $c=17

        "The power of the state is too strong for some people to resist. Sadly, you are right.":
            $c=16

        "You can't build a world of peace out of a furnace of war.":
            $c=12



if c==12:

    butcher """

    Why not? You wouldn't think that you could build a scarf out of a worm, or make cheese from a cow, and yet here we are.

    Besides, stating that I can't is a positive claim, so the burden of proof lies with you.
    """

    menu:

        "Wait, the burden of proof? How very intellectual of you.":
            $c=13

        "You'll have a population primed for violence. Many people can't stop fighting when they get a taste for it.":
            $c=15

        "It's philosophically hypocritical. People won't respect a militant pacifist.":
            $c=14



if c==13:

    butcher """

    I learnt it from a professor friend of mine. You have no idea how useful it is in arguments.

    But it's also true, so are you going to justify yourself, or just point out my pretentions?
    """

    $game.butcher.att += 1

    menu:

        "You'll have a population primed for violence. Many people can't stop fighting when they get a taste for it.":
            $c=15

        "It's philosophically hypocritical. People won't respect a militant pacifist.":
            $c=14



if c==14:

    $game.butcher.resp -= 2

    butcher """

    Who said anything about respect? You're thinking like a statist again.

    This isn't a game, after the revolution we won't have to use sophistry to con people into acting as they should. The ideal of the people will assert itself without help.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==15:

    butcher """

    You have a worse opinion of people than I do.

    I know, those words coming out of my mouth surprised even me.

    But I hope, I must hope, that the people's realisation of the ideal of the people will be stronger than barbaric blood-lust. If not, then it's all pointless anyway. But we can return to the ideal of the people some other time.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==16:

    butcher """

    I don't like the idea of some politician's wife's blood soaking into my shirt, but I'm aware of what the revolution will call for, and I'm willing to do it.

    For the ideal, yes. But also knowing that if I didn't the statists and the bourgeois would continue killing the proletariat in the names of profit and nationalism.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==17:

    butcher "I wish you wouldn't put it that way. You make it sound political."

    "Mik sighs, a long, genuinely sad sigh."

    butcher """

    It's all in the name of the ideal of the people, the wants and desires of every human. This revolution will be the last, and after it the bloodshed of oppression will end.

    Ah, but I haven't explained what the ideal of the people is yet have I? Some other time, perhaps.

    As I was saying though, the only people who will die are those so poisoned by state and capital that there is no saving them. We will only point our weapons towards those who have lost their connection with humanity so much that they they will lay down their lives for their institutions.

    It is not a political act of silencing dissenters. It is … it is removing, sorry, destroying, those who are so corrupted, so amoral that they are beyond saving.
    """

    $game.butcher.resp += 2

    menu:

        "Killing those who have lost their connection with humanity? Sounds like the language the last King used to justify driving out the 'heretics'. Sounds like ethnic cleansing.":
            $c=21

        "You'd kill me if I refused to stand aside?":
            $c=18

        "Of course. They are killing workers every day in the city. Violence is sometimes necessary.":
            $c=16

    jump reevaluatebutcher2



if c==18:

    "Mik stares at you for a long time before looking away."

    butcher """

    In the name of the ideal of the people … yes. I don't like that I would. Despite everything, I think I would be a better person if I said I wouldn't. But if it came to it, if you were standing between the revolution and the emancipation of all humankind, I would.

    Can we please talk about something else?

    Please?
    """

    menu:

        "You say that you'd kill me and then that you just want to continue talking about something else? No, I'm leaving.":
            $c=19

        "And I'd kill you if you tried to kill the Alderman, or anyone else just trying to do the best they can. So I guess we're even.":
            $c=20

        "Okay, I understand. You've told me why the revolution will be total, destructive and final. What next?" if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
            $c=36

        "Okay, I understand. Now tell me how the revolution will be total?" if Mik2Total == False:
            $c=30

        "Okay, I understand. Now tell me why the revolution will be final?"if Mik2Final == False:
            $c=34



if c==19:

    "Mik shakes their head, almost sadly."

    butcher """

    No. I'm sorry, but I didn't confess that to you so you could walk away.

    I understand why you want to. I would be worried about you if you didn't. But I won't let you until I've said all I'm going to say.

    You need to know why I would say such an awful thing.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==20:

    butcher "At least we both know where we stand."

    """

    Mik opens their mouth, as if they want to say more, but instead they just sadly shake their head. They haven't said what they wanted to say, but you can tell they know it's too late to change it now.

    Best to just move on.
    """

    menu:

        "Okay, I understand. You've told me why the revolution will be total, destructive and final. What next?" if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
            $c=36

        "Okay, I understand. Now tell me how the revolution will be total?" if Mik2Total == False:
            $c=30

        "Okay, I understand. Now tell me why the revolution will be final?"if Mik2Final == False:
            $c=34



if c==21:

    butcher "How dare you! I am talking of the liberation of the proletariat, not some fascist, evil, insane, religious mania inspired genocide!"

    menu:

        "I'm sure there were many of the King's men who thought that driving out the heretics would save the people of the Kingdom. They were misguided murderers and so are you.":
            $c=22

        "Not at all defensive then, eh Mik?":
            $c=24

        "You're right, of course, I'm sorry I even suggested it.":
            $game.butcher.resp -= 2
            $c=25



if c==22:

    "Mik shakes their head, obviously furious."

    butcher """

    I am not misguided [game.player_name]. I have facts, philosophy and history on my side.

    I have admitted that my revolution will be bloody. I haven't tried to hide that.

    But it is not genocide. And I'm disgusted that you would even suggest it.
    """

    $game.butcher.like -= 4

    menu:

        "You are suggesting killing people based on either their beliefs or their birth. That's genocide.":
            $c=26

        "I'm sorry I pushed.":
            $c=25



if c==24:

    butcher """

    Of course I'm defensive, you're accusing me of plotting genocide.

    But you are right. Open mind, reasonable thoughts. That's how you win. That's how you know you're right.

    Beating me at my own game here [game.player_name]. I like that.
    """

    $game.butcher.resp += 2
    $game.butcher.att += 2

    menu:

        "You are suggesting killing people based on either their beliefs or their birth. That's genocide.":
            $c=26

        "I'm sorry I pushed.":
            $c=25



if c==25:

    butcher "Well, I'm sorry I … I'm sorry I let myself go. We should move on."

    menu:

        
        "Okay, I understand. You've told me why the revolution will be total, destructive and final. What next?" if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
            $c=36

        "Okay, I understand. Now tell me how the revolution will be total?" if Mik2Total == False:
            $c=30

        "Okay, I understand. Now tell me why the revolution will be final?"if Mik2Final == False:
            $c=34



if c==26:

    "Mik takes a deep breath and places their hands on the shop counter to still them."

    butcher """

    By beliefs, I presume you mean the statists. Yes, you are not wrong, it would be killing people for their beliefs. But that does not make it genocide.

    People are killed for their beliefs all the time in the name of justice. Or if not killed, then as good as.

    A belief is anything that an individual thinks is true. And if an individual thinks that it is true that they can murder or rape then I, like most people, would say that it is fine to kill or imprison them for those beliefs.

    Why should the belief that it is okay to enslave the entirety of the working class of a nation be any different?

    As for people's birth, I presume you are talking about members of the bourgeoisie? The important note here is that the members of the bourgeoisie can choose at any time to stop being bourgeois. They can give their wealth away, to good causes, and join the proletariat. We will welcome them with open arms.

    And if not, well, then I think my points about their beliefs should cover me.
    """

    menu:

        "You are comparing our Alderman, trying to protect his village, to a rapist or murderer? That's just wrong.":
            $c=27

        "Many bourgeois do give away great deals of wealth to the poor. Many may only choose to not become proletariat because they know, or think, they can do more good by staying bourgeois and donating money that way.":
            $c=28

        "You've already said you don't endorse the political option. So you wouldn't give the bourgeois the chance to learn the error of their ways through discourse. You wouldn't give them the chance to be educated, you'd just kill them. And yet you claim that what you are doing is not genocide?":
            $c=29

        "I hadn't thought about it that way before. You make good points.":
            $c=16

    jump butcherscene2



if c==27:

    butcher """

    Just because the sickness is common, does not mean that it isn't still a cancer.

    Listen, I don't think that the Alderman is a bad man. But he, and his ilk, stand between the revolution and the emancipation of all of humanity. There is no part of me that wants to kill him. But it is necessary.

    I've come to terms with that: the necessity of the sacrifices that must be made. It isn't genocide. It isn't right, and it isn't 'good' whatever that means, but it is what needs to be done.

    Now, I'm sorry, but it's time we talk about something else before we just go round and round on this all day. Let's try and find some common ground.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==28:

    butcher """

    Just because someone is aware that they are sick, does not mean that they will then immediately be cured.

    These 'caring bourgeois' might not be bad people. But they nonetheless stand between the revolution and the emancipation of all of humanity. There is no part of me that wants to kill them. But it is necessary.

    I've come to terms with that: the necessity of the sacrifices that must be made. It isn't genocide. It isn't right, and it isn't 'good' whatever that means, but it is what needs to be done.

    Now, I'm sorry, but it's time we talk about something else before we just go round and round on this all day. Let's try and find some common ground.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==29:

    butcher """

    Yes, I have already said that I don't endorse political revolution, but I have also explained why that is. Because it simply won't work.

    As for the bourgeois, they've had their chance. If they were 'good people', they would be able to see what they are doing and they wouldn't be able to continue living the lives they live.

    But they do keep living those lives, or they chose not to look, which is as bad.

    And don't bring up their children. If they're too young to appreciate the evils of their wealth, they are too young to take up arms to defend it. Yes, we will sadly leave them orphaned, but we need not kill them.

    I've come to terms with the necessity of the sacrifices that must be made. It isn't genocide. It isn't right, and it isn't 'good' whatever that means, but it is what needs to be done.

    Now, I'm sorry, but it's time we talk about something else before we just go round and round on this all day. Let's try and find some common ground.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
        butcher "We should touch on practical matters now."

        $c=36
        
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be destructive, but don't you want to know why it must be total, and why it will be final?"
            
            menu:


                "Why total?":
                    
                    $c=30

                "Why final?":
                    
                    $c=34
                    
        elif Mik2Total == True:
            
            butcher "I should tell you about why the revolution will be final."

            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be total."

            $c=30



if c==30:

    butcher """

    By total, I suppose I should say global, although total has some nice implications. The revolution will only be complete when no square mile, no tiny island, no backwater peninsula suffers under the boot of statism, or the bourgeoisie.

    Ambitious? Really?

    Of course it's ambitious, but it is necessary, and necessary for a number of reasons, most of them disappointingly practical. I will #{i}try#{/i} to be quick.

    The first is the interconnectedness of the modern bourgeois world. I believe they refer to it as globalism, and it was a genius move on their part.

    We may still be licking our wounds after our war with the Kingdom, yet do you have any idea how many factories in Alexisgrad are owned by bourgeois from the Kingdom? And how many businesses in the Kingdom are owned by our Republican bourgeois?

    And it goes further, to Il Fersaai, our 'economic allies', and the Empire of Raplee, who supposedly prop up the Kingdom and yet have both political and unofficial-economic embassies in Alexisgrad (names in bold are very much subject to change).

    So you see, the Republic bourgeoisie have outsourced their oppression, while selling their own services to foreign markets in return, meaning that you cannot bring one system down without brining them all down.

    Secondly, and purely strategically, the post-revolutionary world will be one of peace and fraternities of small communities, communities will have no space for militarism and therefore communities which are highly susceptible to foreign invasion.

    And invaded we would be: no government in the world could look at a plot of mostly undefended land and not salivate over the thought of taking it. Add to that the example that it sets, that life liberated from the shackles of the state is better in every way, and every country in the world will be racing to subjugate us.

    Just by existing, we would be too dangerous to the statists to be allowed to live.

    And lastly, and this is where 'total' is more pertinent than 'global', I knew I'd used it for a reason, is that nationalism must be completely extinguished in the hearts and minds of every human on this planet.

    Partly this one is because nationalism is just purely bad. I would give you an analogy, but the only thing I can think of is faeces, and I've spent enough time around animal digestive systems to understand that even that has a purpose.

    Partly it is because nationalism is the fertiliser of statism.

    But mostly because, by design, nationalism acts as blinkers, or if I were to be more direct and say what I actually think, nationalism is a knife the state uses to gouge its own people's eyes out.

    Keeping the people worshipping at the altar of something which either doesn't exist, in this case national glory or 'national spirit', or is actively oppressing them is a brilliant way to make sure they don't notice their own chains.

    Or, more insidiously, the state knows that the people realise that they have an enemy, so they invented nationalism as a way to con them into thinking it is foreigners, rather than their own government.

    Either way, it's a cataract. Yes, I'll take that analogy out of the three that I've given you so far. It blinds people to their own actual desires and will. It distorts people's ideals.

    I apologise, I said I'd keep it brief…
    """

    $Mik2Total = True

    menu:

        "But globalism is a good thing. It means that we can be more connected with people we would otherwise never know, it allows us to learn and teach new ideas and without it we wouldn't have so many brilliant inventions, not to mention delicious foreign foods. It connects us with the world. In many ways it is the opposite of nationalism.":
            $c=33

        "But if the post-revolution world has no armies, then how could it defend itself if part of it reverted to the old ways and tried to conquer the rest?":
            $c=32

        "Nationalism isn't evil, it's noble. It's how we celebrate what is good about our Republic and how we protect ourselves from the bad aspects of other places. For example, even you must acknowledge that we should be aware of, and guard against, the tyranny of the Kingdom.":
            $c=31

        "It is ambitious, but every one of those points is reason enough to make the totality of the revolution necessary.":
            $c=35



if c==31:

    $game.butcher.like -= 4
    $game.butcher.resp -= 4
    $Mik2Nationalism = True

    butcher """

    Okay, for the sake of the argument, I will say, although not really believe, that there are some positive aspects of nationalism.

    It's nice that we can all come together and celebrate the warm, cosy, good things that we do as a community. It would be nice if we did that because we're good people with common sense, but let's pretend for a moment that nationalism is how we get there.

    What happens to these positive traits, the brotherhood that nationalism supposedly creates, when there are no nations? When all humans are equal and are acknowledged by all to be so?

    We will all be bound together in one global fraternity, for want of a suitable non-gendered word, and any celebration of that union will not be nationalism, for nationalism implies the existence of some excluded, 'other' group.

    So a nationalist in a post-revolution world would have naught to celebrate but exclusionary statist slavery.

    There. I think I've made that point rather well. And can we please celebrate the fact that I did it without using the word 'racist', or 'bigot', once. Despite that fact that I would have been justified in doing so.
    """

    if Mik2Globalism == False or Mik2Militarism == False:
        
        butcher "Now what else did you want to throw at me?"

        menu:

            "Okay, but globalism is a good thing. It means that we can be more connected with people we would otherwise never know, it allows us to learn and teach new ideas and without it we wouldn't have so many brilliant inventions, not to mention delicious foreign foods. It connects us with the world. In many ways it is the opposite of nationalism." if Mik2Globalism == False:
                $c=33

            "Okay, but if the post-revolution world has no armies, then how could it defend itself if part of it reverted to the old ways and tried to conquer the rest?" if Mik2Militarism == False:
                $c=32
            
            "Okay, I see why the totality of the revolution is necessary.":
                $c=35
                
    else:

        if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
            butcher "We should touch on practical matters now."

            $c=36
            
        else:
            
            butcher "But I'm getting ahead of myself."
            
            if Mik2Final == False and Mik2Final == False:
                
                butcher "I've told you why the revolution must be total, but don't you want to know why it must be destructive, and why it will be final?"
                
                menu:


                    "Why destructive?":
                        
                        $c=6

                    "Why final?":
                        
                        $c=34
                        
            elif Mik2Destructive == True:
                
                butcher "I should tell you about why the revolution will be final."

                $c=34
                
            else:
                
                butcher "I should tell you about why the revolution must be destructive."

                $c=6
    
    jump reevaluatebutcher2



if c==32:

    $Mik2Militarism = True

    if Mik2Final == True:
        "Mik shakes their head sadly."

        butcher """

        I shall repeat myself, shall I?

        As I have said - although I suppose if the butcher says it and there is no intelligence within the butcher's shop to hear it, was it really said? - this will be the final revolution. The social revolution will emancipate everyone, not just a select few, as all political revolutions do.

        Everyone will have liberty and equality within that liberty. If the ideal of the people is fully realised, which it must be for the revolution to be total, there will be no 'reverting'.

        And more practically, there will be no standing armies. Even if one mad person were to decide to reinstate the statist order, there would be no statist order maintaining the military engine that she would need in order to complete her mad, self-destructive scheme.

        So you are right, I suppose, the people would have no defence. But they would have no defence against something that would and could never happen, so the question is irrelevant.
        """

        $game.butcher.resp -= 4
        
    else:
        "Mik shakes their head."

        butcher """

        Ah, a practical question. Good. But one that I will defeat with more theory, I am afraid.

        The short answer is that, because the revolution will be final, there will never be, there never could be, a return to the 'old ways'. But I will cover that when we get there.

        I'm sorry to keep you in suspense.
        """

        $game.butcher.resp -= 4

    if Mik2Globalism == False or Mik2Nationalism == False:
            
            butcher "Now what else did you want to throw at me?"

            menu:

                "Okay, but globalism is a good thing. It means that we can be more connected with people we would otherwise never know, it allows us to learn and teach new ideas and without it we wouldn't have so many brilliant inventions, not to mention delicious foreign foods. It connects us with the world. In many ways it is the opposite of nationalism." if Mik2Globalism == False:
                    $c=33

                "Nationalism isn't evil, it's noble. It's how we celebrate what is good about our Republic and how we protect ourselves from the bad aspects of other places. For example, even you must acknowledge that we should be aware of, and guard against, the tyranny of the Kingdom." if Mik2Nationalism == False:
                    $c=31
                
                "Okay, I see why the totality of the revolution is necessary.":
                    $c=35
                    
    else:
        if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
            butcher "We should touch on practical matters now."
            $c=36
            
        else:
            
            butcher "But I'm getting ahead of myself."
            
            if Mik2Final == False and Mik2Final == False:
                
                butcher "I've told you why the revolution must be total, but don't you want to know why it must be destructive, and why it will be final?"
                
                menu:
                    "Why destructive?":
                        
                        $c=6
                    "Why final?":
                         
                        $c=34
                        
            elif Mik2Destructive == True:
                
                butcher "I should tell you about why the revolution will be final."
                $c=34
                
            else:
                
                butcher "I should tell you about why the revolution must be destructive."
                $c=6
    
    jump reevaluatebutcher2



if c==33:

    butcher """

    Ah, I think that the confusion here comes down to semantics: globalism is an inherently political and economic term.

    I by no means want to reduce the amount of contact that people from across the world have with each other. The society the revolution will create will be far more free to move and explore than the one that currently exists.

    Just because the standard social model will be small communities of individuals, brought together by their own voluntary desire to form a fellowship, does not mean that those communities shouldn't, or wouldn't, be diverse.

    If the advantages you have so eloquently pointed out are anything to go by, I would say that it is safe to assume that the communities would be diverse: there are so many advantages to it.

    After the revolution, people will be free to travel wherever they wish and settle with whomever they wish. Societies will be much more 'global' than any society that 'globalism' could produce would be.
    """

    $game.butcher.like += 2
    $game.butcher.resp += 2
    $Mik2Globalism = True

    if Mik2Militarism == False or Mik2Nationalism == False:
            
            butcher "Any other criticisms?"

            menu:

                "Okay, but if the post-revolution world has no armies, then how could it defend itself if part of it reverted to the old ways and tried to conquer the rest?" if Mik2Militarism == False:
                    $c=32

                "Nationalism isn't evil, it's noble. It's how we celebrate what is good about our Republic and how we protect ourselves from the bad aspects of other places. For example, even you must acknowledge that we should be aware of, and guard against, the tyranny of the Kingdom." if Mik2Nationalism == False:
                    $c=31
                
                "Okay, I see why the totality of the revolution is necessary.":
                    $c=35
                    
    else:
        if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
            butcher "We should touch on practical matters now."
            $c=36
            
        else:
            
            butcher "But I'm getting ahead of myself."
            
            if Mik2Final == False and Mik2Final == False:
                
                butcher "I've told you why the revolution must be total, but don't you want to know why it must be destructive, and why it will be final?"
                
                menu:
                    "Why destructive?":
                        
                        $c=6
                    "Why final?":
                         
                        $c=34
                        
            elif Mik2Destructive == True:
                
                butcher "I should tell you about why the revolution will be final."
                $c=34
                
            else:
                
                butcher "I should tell you about why the revolution must be destructive."
                $c=6
    
    jump reevaluatebutcher2



if c==34:

    $Mik2Final = True

    butcher """

    Why will the revolution be final? For the opposite reason to why no state will ever reign eternally: equality.

    You see, states are, by their very nature, rule of the few over the many. Well, to crawl even further up my arse, even #{i}that#{/i} is semantically redundant, since the position of the few over the many, or at least the position of some over another, is already implied by the word 'rule'.

    It is #{i}that#{/i} inequality that makes states conservative. The world must stay the same so that the ruling class can continue to have more than the ruled class.

    But if you take that inequality away, then the world, and the people in it, are free to change as much as they want.

    But I'm approaching the question arse first. The main reason the revolution will be final is because after the ideal of the people is realized, no one will have any reason to attempt another revolution.

    Likewise, no-one will ever desire any political movement, as to do so would risk the equality and liberty that they have learnt are the cornerstones of their emancipation.

    Lastly, and very much least...ly, because what I have already said makes it irrelevant, but I think it's worth mentioning that after the revolution, and the abolition of state institutions, there will be no standing armies, or military organisations. For purely practical reasons, no one would be #{i}able#{/i} to carry out another revolution even if they wanted to, which they won't.

    Some of that may sound slightly … airy, but that is because I am yet to explain the 'ideal of the people'.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
            butcher "We should touch on practical matters now."
            $c=36
            
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Total == False and Mik2Destructive == False:
            
            butcher "I've told you why the revolution must be final, but don't you want to know why it must be destructive and total?"
            
            menu:
                "Why destructive?":
                    
                    $c=6
                "Why total?":
                        
                    $c=30
                    
        elif Mik2Destructive == True:
            
            butcher "I should tell you about why the revolution will be total."
            $c=30
            
        else:
            
            butcher "I should tell you about why the revolution must be destructive."
            $c=6

    jump reevaluatebutcher2



if c==35:

    butcher """

    Ambitious, yes. Very. Very very very ambitious. Almost overwhelmingly so.

    But I have ideas. Radical ideas of course, what do you take me for? but ideas nonetheless.
    """

    if Mik2Total == True and Mik2Final == True and Mik2Destructive == True:
        
            butcher "We should touch on practical matters now."
            $c=36
            
    else:
        
        butcher "But I'm getting ahead of myself."
        
        if Mik2Destructive == False and Mik2Final == False:
            
            butcher "I've told you why the revolution must be total, but don't you want to know why it must be destructive, and why it will be final?"
            
            menu:
                "Why destructive?":
                    
                    $c=6
                "Why final?":
                        
                    $c=34
                    
        elif Mik2Destructive == True:
            
            butcher "I should tell you about why the revolution will be final."
            $c=34
            
        else:
            
            butcher "I should tell you about why the revolution must be destructive."
            $c=6

    jump reevaluatebutcher2



if c==36:

    if game.butcher.resp < 0:
        $textinsert = "Even you aren't stupid enough not to get that one. "
    else:
        $textinsert = ""

    if game.butcher.resp < 0:
        $textinsert2 = "I must say, regardless of anything else I might think "
    else:
        $textinsert2 = ""

    butcher """

    I've explained why the revolution will be total, final and destructive. That's all theory. It's true, but it's all been discussed ad nauseam in smoky underground bars in Alexisgrad. It's both dry and, sadly, not original. Very little of it is mine.

    But I'm not incapable of reaching conclusions on my own. And not just theoretical conclusions. Practical ones. Which you may think isn't as good, but please, really? Which ideas get food on the table, the actionable ones or the theoretical ones?

    No, I've come to my own, admittedly basic and obvious, conclusion. When do you strike against an enemy? When they're weakest. When is the state weakest? When things are in flux. What is the biggest change that has occurred, not just to our society but our entire world, in the last, well I don't even know, thousand years?

    It's a rhetorical question, we both know it's the sun disappearing. [textinsert]If our own dear Alderman is anything to go by, every government in the world is soiling itself right now.

    And what's more, the people might finally be waking up to the reality of their lives. Their state, their bourgeoisie, neither of them saved them from the night. Neither of them is #{i}going#{/i} to save them from the night. So why do they need them?

    The people will be scared, as they should be. Thoughtful, compassionate decision making has never been so important to their lives, but small, self-interested, conservative groups are the only ones who currently have the power to do it.

    You can taste the revolution in the air. Anyone who tells you that our republic is still alive is either an idiot or a desperate, lying statist. The same goes for the Kingdom, Il Fersaai, Raplee, every state on the planet.

    And anyone who thinks that the institution of private property will survive is equally evil or stupid. The settlements which, and the individuals who, don't collectivise will die.

    Just a few minutes ago I said that the idea of a total, global revolution was far-fetched. But look around you. Look at the world. It's not really far-fetched at all.

    It's inevitable.

    The only risk, the only obstacle standing between us and true social revolution, is political revolution. Because trust me, the communists, the fascists, possibly even the radical liberals, they're all having this exact same conversation right now. Any one of them could turn the inevitable revolution into their own political coup.

    And I really fear that they will. The power of 'state' is simply too strong. We are living through the best opportunity humanity has ever been given to organise itself in a just, equal and free way, and we're going to lose it because we couldn't get our message out fast enough.

    What I truly dream of doing … no. No, no we're getting off topic. This was supposed to be a lesson on oppression for our new member of the ruling elite. Not the birth of the anarchist revolution.

    Besides, I've taken up more than enough of your time. So I'll say that you're ready. Congratulations, you've graduated with honours, go and take your meaningless qualification and use it to be an oppressive bastard.

    Tell the Alderman you fully understand all the problems with the system you exist to uphold and are ready to ignore every single one of them.

    Now I've got to get back to my pigs. I'm slightly afraid that they may have gone rotten in the time that I've been out here talking to you.

    [textinsert2]I'm impressed you stayed to listen to the whole thing.

    Although you probably didn't feel like you had the choice …

    Anyway, cheery-bye!
    """


return
