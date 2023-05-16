label butcherscene9:

$NewLeader = "" #JE: this is a placeholder, this line very, very much needs to be removed later.

if game.butcher.resp > 30:
    $textinsert = "Not that I think you'll manage, but it will be amusing to see you try, and I could do with a comical distraction."
else:
    $textinsert = ""

if game.butcher.romance == False:
    
    "You have barely swung the door open, answering a constant quick beat of knocking, before Mik pushes themselves into the room."
else:
    "Mik sits up suddenly, shattering the post sex calm."

butcher """

Fuck you.

I don't really mean that, but also, fuck you.

I'm not going to take that back. I know that, at the core, I'm still right. Power corrupts and systems of power will do everything they can to maintain themselves and the inequality they create.

Those systems, therefore, must be torn down, and they {i}must{/i} be replaced by systems created from the bottom up, systems that start with a foundation of equality and liberty and have the integrity to maintain that foundation.

I had it all neatly worked out. My conversations with you were never supposed to be a test. At the very least, they were meant to be practice.

But some of the things you've said [game.player_name], they've stuck to me. Look at me, clearly I've never been the kind of person who sleeps well, but it's been even worse recently.

I suppose I should thank you, the steam-powered mechanical monsters of my nightmares have been replaced by logical inconsistencies, but on the other hand personal emotional trauma is and always will be more sexy than flaws in reasoning.

I don't know where the fatal flaw is, [game.player_name]. I don't even know if it's in the logic, or if it's in me.

I haven't had doubts before [game.player_name], this is a new experience for me. Growing up there were just facts and we just dealt with them. And then when I discovered all of this … philosophy, I suppose, I either disagreed or I agreed.

I suppose I did find problems, little bits here and there, but I've always been able to work on them myself, put some flesh on the bones and fix it up. Maybe that was my problem, all of the training for my trade was about stripping flesh off.

Sorry, that was a poor joke. I'm tired and not up to standard.

I feel weak [game.player_name]. Not because I think I was wrong, but because I don't know where I'm going.

I feel vulnerable. How am I supposed to know how to move forward if I don't know where I'm moving to? How am I supposed to stand up for myself if I don't know what I stand for?

Well look at me, I'm finding a way to make it poetic after all. Is this a sexy kind of angst?

Don't answer that. Don't encourage my catastrophising. And don't point out how bourgeois it is either, I'm well aware of how lucky I am to be able to swoon in anguish because someone thinks my ideas aren't up to snuff.

Because, and I've been dancing around this so let me put it painfully bluntly, I want to see hundreds of people die. I stand by what I've always said, that if that sacrifice gave the people their utopia, then it's justified.

But it's that conditional I'm stuck on. 'If'. Because {i}if{/i} I'm wrong, like the communists are wrong, then I'm doing little more than advocating murder. And I know that I have bizarre politics, but even I think that's wrong.

Hence my dark cloud of woe.

I'm in a trough [game.player_name]. You got me into it, now help me out of it. [textinsert]
"""

if NewLeader = "No-one": #JE: placeholder variable name (as used in Alderman 9)

    """
    Although I don't know why I've come to you, after that stunt you pulled. Why? With what game have you sullied my philosophy? What long term political games are you playing, tearing down the Alderman and 'replacing' him with a system you have argued so ardently and adroitly is false?

    Fuck it, I don't want to know. Despite you, I refuse to be involved. I don't want to hear about it. You've used me and now I demand my right, under the laws of commerce you bourgeois like to pretend exist, that I get to use you back.

    I refuse to be your puppet. Now tell me what I should do with myself once you've put me aside.
    """

$SocialRevolution = False

menu:

    "You're right, you were advocating murder. I think you deserve to just stew with that for a while.":
        $c=1

    "The people \"will amaze you with the profound rationality of their ideas.\" You hated me when we first started talking and now we're here. That should be encouraging, not discouraging. You believe that utopia will come about from the people's ideas, so go speak to the people. They might give you the solution you're looking for.":
        $c=2

    "Write it all down Mik. At best, putting it on paper will make it easier to spot where it goes wrong. At worst, you will immortalised everything so that someday someone else can fix it for you.":
        $c=3

    "As I'm sure you've noticed, we're going through a difficult time, as a society. You say you care so much about the people, so why not get out there and help them? Go talk to the Alderman and volunteer your time, or speak to Stu and see whether he knows anyone who needs help with anything. Go and actually {i}make{/i} a difference, instead of just talking about it.":
        $c=4

    "No Mik, don't doubt yourself. You've won me round, I think you're right. The social revolution is the way to utopia, and now is the time to make it happen!":
        $c=5



if c==1:

    if game.butcher.romance == True:
        $textinsert = "And talking of 'fuck', that's about all you {i}are{/i} good for. So get ready for a second round, then I'm leaving."
    else:
        $textinsert = "A {i}useless{/i}, morally bankrupt fuck."

    "Mik just tuts and shakes their head good naturedly."

    butcher """

    I'll be the first to admit that I don't come off as particularly graceful, but that's a low blow [game.player_name]. And I don't mean that in a respectful, I'm-a-revolutionary-and-therefore-appreciate-sly-tricks way, it's just the kind of thing an arsehole would say.

    I wasn't going to make a point of saying this, but now, completely out of spite, I don't want you to think that you've won.

    I may not be completely {i}right{/i}, but that doesn't mean that you're not still completely {i}wrong{/i}. You haven't crushed my spirit, I'm not going to run into the paternal arms of the reactionaries sucking my thumb and choking out excuses about being young and seduced by the fancy men with their cheap cigars.

    No, you're still a morally bankrupt fuck.
    """

    if game.butcher.romance == True:
        butcher "And talking of 'fuck', that's about all you {i}are{/i} good for. So get ready for a second round, then I'm leaving."
    else:
        butcher """
        
        A {i}useless{/i}, morally bankrupt fuck.

        I've got what I expected I'd get out of this: nothing. Not that I needed anything, of course, don't try to trap me in that. But it would have been nice if you'd felt like sharing.

        But hey ho, can't blame you for consistency and loyalty to your dying cause. But I think we are done now, aren't we [game.player_name]? Oh no, don't cry. Just keep doing what you're doing, and I'll keep thinking of ways to try to stop you.

        Cheerio! And good luck with your oppression!

        You cunt!
        """

    if game.butcher.romance == True:
        $game.butcher.like -= 4
    else:
        $game.butcher.like -= 8

    $game.butcher.resp -= 2

    return



if c==2:

    if game.butcher.romance == True:
        $textinsert4 = " you are a very good fuck.  And"
    else:
        $textinsert4 = ""

    if game.butcher.romance == True:
        $textinsert3 = "Not to mention you're a very good fuck."
    else:
        $textinsert3 = ""
    
    if game.butcher.resp > 30:
        $textinsert2 = " I do respect you. {}".format(textinsert3)
    else:
        $textinsert2 = "{}, as the better person, I thought it only right that I should come and tell you what all our discussions have led to.".format(textinsert4)
    
    if game.butcher.like > 28:
        $textinsert = "Indeed. If I were gauche I might even call you a friend, but of course I am far too sophisticated for that. And too much of a cynical bastard."
    else:
        $textinsert = "Let's be clear, I still hate you. But{}".format(textinsert2)

    if game.butcher.resp > 30:
        $textinsert5 = "I hope the rest of the town lives up to your standard. I must say, for a statist, you did surprise me with your 'profound rationality'."
    else:
        $textinsert5 = "Although I must say it's not particularly encouraging. I would not say it was any kind of 'profound rationality' on your part that has led to my problems. I would put it down more to the principle of a broken clock being right twice a day."

    if game.butcher.like > 28:
        $textinsert6 = "Although I must admit, you made building this far easier than I expected, or rather, easier than I would expect anyone else to make it."
    else:
        $textinsert6 = "And if I could build this with you, I should be able to build it with anyone."

    butcher """

    [textinsert]

    But you are right. Our {i}long{/i} talks have given me pause. And as an enemy of absolutism and the blind following of an ideal, that is, ideologically if not personally or emotionally, a good thing.

    [textinsert5]

    Regardless, I am here and you are right. I've been a bit of a hypocrite, haven't I? For someone who believes that all the answers exist in the minds of the people, I have spent very little time actually speaking to the people.

    Well, that's not entirely true. I have tried, and the last time I did … well it didn't go to plan. On the other hand, I think that a single data point is the definition of 'not enough data'.

    Still, is now the time? When I'm already feeling like this, is now the time to step out?
    """

    if $RomanceMik == False:
        butcher "I suppose we shall see, won't we?"
    else:

        butcher """

        Listen, I know that we just fuck, and I know that's been at my suggestion, but you could introduce me, couldn't you?

        Actually … no. No, I'll do this on my own. Mother always said …

        Well, I should go. I think I've explored every corner of this bizarre little comfort zone we've made here. [textinsert6]

        I am not entirely sure who is dismissing whom? Which one of us has completed their lessons, which one has graduated and is going out into the world?

        I don't like to admit this, but I am genuinely afraid that it might be me.
        """

    $game.butcher.resp += 2
    #JE: {Slight cohesion increase} (if like is below a certain threshold)[#{Very slight cohesion increase}

    return



if c==3:

    if game.butcher.like > 28:
        $textinsert = " with friends"
    else:
        $textinsert = ", one with a disillusioned trouble-maker and the other with a die-hard statist"

    if game.butcher.romance == True:
        $textinsert2 = "I'll keep you in mind when I need to get my exercise, by which I mean when I want sex,"
    else:
        $textinert2 = "Our talks have been very useful,"


    "Mik nods, and you swear that you can see relief in their eyes."

    butcher """

    Oh how very sophisticated. I'm not sure it's the aesthetic I am going for, but I suppose it could work. I suppose there is a kind of chaste eroticism to academia, a kind of alluring mysticism.

    Yes, these are the first concerns I should be considering. What, you thought I became a revolutionary before I realised how sexy it all is?

    But in all seriousness, and yes I do realise that that immediately puts the lie to what I just said, writing it all down probably would be the best I could do, for now at least.

    I think I have always thought of myself as too active, too involved to take the time out to sit down and actually write. But I think we can both see how much of a delusion that is.

    The sum of my revolutionary activity in this town has been two private lecture series[textinsert], and one public rally that did not exactly go to plan.
    """

    "Mik lets out a long sigh."

    butcher """

    I'm a pretty poor excuse for a revolutionary, aren't I? A bag of second-hand ideas and not a drop of blood on my hands. Well, not the blood I wanted on my hands, anyway.

    Wrong kind of pig.

    I'm not going to hang up my … whatever it is that I would use to carry out the revolution in this metaphor. There'll be time to use it later.

    Hopefully.
    """

    "Mik looks out of your window, into the night. They bite their lip, shake their head and smile to themself."

    butcher """

    Who am I trying to fucking fool? Books never called me a 'dangerous fucking moron'.

    I'm off to find some paper, [game.player_name]. I'm sure I've got some lying around. I'll worry about binding and all that practical nonsense later.

    Oh, you've got my blood pumping [game.player_name].

    I wonder how the ink stains will pair with the blood stains?

    Take care [game.player_name]. [textinsert2] but I think I'll give writing a proper go. Which means, of course, disappearing into a room with no windows and smoking far more than is enjoyable.

    You'll read the first draft, after it's done though.

    I'll make sure of it.
    """

    "Mik winks, and then slides towards the front door."

    $game.butcher.like += 2

    return



if c==4:

    if $game.butcher.romance == True:
        $textinsert = "I mean you're good {}, but there".format(game.player_name)
    else:
        $textinsert = "There"

    if game.butcher.like > 28:
        $textinsert2 = "Although I must admit, you made building this far easier than I expected, or rather, easier than I would expect anyone else to make it."
    else:
        $textinsert2 = "And if I could build this with you, I should be able to build it with anyone."


    "Mik takes a deep breath and lets out a long sigh."

    butcher """

    This may surprise you to hear, [game.player_name], but I had actually noticed.

    Flippant? Really?

    It's not like I don't do my part. I'd like to see any of the rest of you deal with the meat that you lot bring back from the forest. I would be surprised to hear that some of it wasn't from the worlds beyond the stars.

    But again, fuck you [game.player_name].

    You've ruined it. My haven. My safe space I can crawl to.

    [textinsert] is nothing better to cuddle while I fall asleep than my theories. But now you've come along and pointed out their bad breath and the way they keep letting in cold air under the sheets.

    I am going to be honest [game.player_name], I have lost track of this metaphor.

    The point is, maybe you are right. Maybe I should take a step into the world of the practical. Actually do as I say.

    I very rarely think about the fact that we might all be about to die. I've had a lot of practice avoiding the 'here and now'. Perhaps helping to save people from a cold, miserable death is the way to change that.

    Still, is now the time? When I'm already feeling like this, is now the time to step out?
    """

    if game.butcher.romance == False:
        butcher "I suppose we shall see, won't we?"
    else:
        butcher """

        Listen, I know that we just fuck, and I know that's been at my suggestion, but you could introduce me, couldn't you?

        Actually … no. No, I'll do this on my own. Mother always said …
        """

    """

    Well, I should go. I think I've explored every corner of this bizarre little comfort zone we've made here. [textinsert2]

    I am not entirely sure who is dismissing whom? Which one of us has completed their lessons, which one has graduated and is going out into the world?

    I don't like to admit this, but I am genuinely afraid that it might be me.
    """

    #JE: {Cohesion increase} (if like is below a certain threshold)[#{Very slight cohesion increase} (if like is below a certain threshold)[#{Very slight cohesion increase}
    return



if c==5:

    "Mik smiles thinly."

    butcher """

    Fuck you [game.player_name]. I'm not going to play those games with you.

    You can't tear it up and then insist that {i}I'm{/i} the one who's abandoned it.

    Or were you being sarcastic? In which case: there's a time and place.

    After all this, all this talk, all these arguments, you can't come crawling back now. I don't want you thinking you can knock the crown off my head and scoop it up.

    Pardon the surprisingly statist metaphor…
    """

    if game.butcher.like > 28:
        butcher """

        I'm sorry, I should be giving you the benefit of the doubt. I know you were just trying to be encouraging.

        But a handful of cries of 'yippee, you can do it!' aren't going to fix fundamental logical issues.

        You're still completely unhelpful, in other words.
        """
    else:
        butcher """

        I know I should be giving you the benefit of the doubt.

        But that's the one silver lining, isn't it? I'm not defending anything any more. It's just about me now, and when it comes to feelings, 'fuck you and fuck off!' are perfectly legitimate arguments.

        You can't commit an ad hominem when the thing you're arguing about is someone's character.
        """

    if game.butcher.romance = True:
        butcher "No, I think it's best if we limit our relationship to what you're good at, going forward. So please, if you want another round, shut your mouth."
    else:
        butcher """

        So I think I should probably go now.

        It's been … useful? No, that's too subjective.

        I supposes that what's it's really been is just a lot of words.

        We should probably both go and try to work out whether any of them are worth anything.
        """

    $game.butcher.like -= 2
    $game.butcher.resp -= 2

return
