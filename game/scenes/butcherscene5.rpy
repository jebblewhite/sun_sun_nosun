label butcherscene5: 

$Mik5MotherJob = False
$Mik5OtherParent = False
$Mik5Home = False
$Mik5Tutor = False
$Mik5Travel = False
$Mik5Anarchist = False

if game.butcher.att > 3:
    $textinsert = " and flirtatious wink,"
else:
    $textinsert = ","

if game.butcher.like > 17:
    $textinsert2 = "they simply give you an acknowledging smile"+textinsert+" but otherwise"
else:
    $textinsert2 = ""

"You find Mik, much to your shock, sitting at a table in the centre of Henryk's inn. Initially [testinsert]they ignore you, involved as they are in a heated discussion with their friend Noah, but after he is called away by the tolling of the hour bells, Mik gestures for you to join them."

butcher "Yes, that's good [game.player_name], make it look like you had arranged to meet me here. I don't want Henryk thinking for a single second that I came here, or would stay here, of my own free will."

"You follow Mik's gaze to see Henryk give you both a sad, sardonic smile."

butcher """

We had better animatedly talk about something, just to complete the illusion.

I realise that our relationship more or less begins and ends at my philosophy. Not exactly normal is it? Still, you cannot deny that it was probably a good ice breaker, so let's use it to dispense of the usual insufferable small talk and get straight to the 'big stuff'.

So then [game.player_name]. Tell me about your life. Who are you, and where did you come from?
"""

menu:

    "*Give the brief version of your life story*.":
        $c=1

    "*Give Mik the whole story of your life*.":
        $c=2

    "*Don't just tell Mik the facts, tell them your feelings, hopes, fears, dreams. Everything*.":
        $c=3


label reevaluatebutcher5:

if c==1:

    if game.playerbackground == "deserter":
        $textinsert = "your noble and daring escape from the brutality of the statist war machine?" 
    elif game.playerbackground == "woodsman":
        $textinsert = "all the interesting stories you must have from your years battling the dark and dangerous natural mysteries of the northern forests?"
    elif game.playerbackground == "marked":
        $textinsert = "your frankly disturbing but morbidly intriguing tendency to 'know things'?"
    else:
        $textinsert = "your life as a small town bourgeois trying to make it big as a big city oppressor?"
        

    "Mik raises an eyebrow as soon as it's clear that you are finished."

    butcher """

    That's it? That's all you can tell me about all your years on this planet? No more about your idyllic rural childhood, or [textinsert]

    But I won't push. I suppose it's fair that you wouldn't have more for me. Without even the promise of any return, I presume you don't reckon it a reasonable trade.

    Well I'll stand by my socialism just as you've stood by your capitalism, so I'll tell you all that you want to know about my story.
    """
    if game.playerbackground == "deserter":
        $game.butcher.like += 1 
    elif game.playerbackground == "woodsman":
        $game.butcher.like -= 1
    else:
        $game.butcher.like -= 2

    $c=4



if c==2:

    "Mik listens attentively throughout your story, interrupting only here and there to ask for clarifications. When you finish they nod slowly and smile."

    butcher """

    I suppose you don't need the approval of an outsider, but you've lived (if marked or trader)[an interesting](else)[a good] life. I must say, you've had more...ups and downs than I was expecting.

    I can see why (if respect is above a certain threshold, where the threshold is higher for marked and trader than it is for woodsman and deserter)[the people respect you](else)[you are useful to the Alderman].

    Regardless of all of that, I am sorry to hear about your parents. They sound like they were good people.

    I'm interested in giving you the third degree, but I think it's only fair that I share with you my tale. It's quite different. I won't presume to say whether it is better or worse, kinder or harsher.
    """

    $game.butcher.like += 2 
    if game.playerbackground == "deserter":
        $game.butcher.like += 2 
    elif game.playerbackground == "woodsman":
        $game.butcher.like += 1

    $c=4



if c==3:

    """

    Mik sits silently while you speak. Initially it is clear that they are feigning an air of aloofness, but by the time you finish it is clear that they are rapt, the emotions of your words mirrored earnestly on their face.

    When you finally stop talking, the whole of your life laid bare on the table between you, Mik sits back and thinks for a long time.
    """

    butcher """

    Thank you.

    I had not expected you to…

    Maybe I have slightly misjudged you [game.player_name].

    When you're in my position, the position of a fringe revolutionary who spends most of their day in the company of dead pigs, it's very easy to see everyone who isn't with you as against you. And it's very easy for any human, I believe, to see those who are against them as somehow less complex, less nuancedly human than themselves.

    You've shown me more kindness than I've perhaps earned by sharing all that with me.

    In other words, you've shown me up, haven't you? Emotionally, you're a better socialist than I. (if deserter)[And possibly practically. I doubt that I can help, but as far as I see it, what you did at the front was the best possible thing you could have done. Fuck those idiots who call you a coward, I think you're a hero.]

    (if deserter)[Too much emotion. Back to me. You know I can't let the idea that you might be a better socialist stand.](else)[You know I cannot let that stand.] I have a reputation as the town's sad, lonely, slightly mad #{i}revolutionary#{/i} to keep up. I refuse to just be the town's sad, lonely, slightly mad #{i}no-noun#{/i}.

    So I will redress the balance. I don't believe in debts, but still, I would like to share with you my equivalent of what you shared with me.
    """

    $game.butcher.like += 4
    $game.butcher.att += 1
    if game.playerbackground == "deserter":
        $game.butcher.like += 4
    elif game.playerbackground == "woodsman":
        $game.butcher.like += 2

    $c=4



if c==4:

    butcher """

    I don't remember much of my early years. I worry I would be a different person today if I could. And then I worry about that worry. It seems wrong to celebrate a lack of memory, doesn't it? Ah, who gives a fuck.

    What I mean is that, as far as I've been told, I grew up in good conditions. I was no bourgeois, don't get me wrong. What I mean is that I didn't have the damp, cold, hunger and bucket-shitting that so many in our 'great nation' have instead of a childhood.

    No, instead there is a warm void, a little black box protected on four sides by sound walls and glass filled windows, floored with wood and roofed with tile.

    I attended a school, of which I do have some memories. There were other children I'd play with, although my modern anti-social streak seems to have retroactively obliterated all of their names from my memory. Not that I'd be able to do anything with that information if I had it.

    Industry was yet to become the be all and end of of Alexisgrad life so back then it was still possible for 'us regular folk' to achieve a modest standard of living without abusing either our bodies or our souls.

    Then again, my mother worked very hard, even then.

    For as long as I can remember, from when I was old enough to walk the streets by myself, which wasn't long after I was old enough to walk full stop, she would always be gone out of our little apartment by the time I woke up, and then back only after dark. Then she'd cook something that she brought back from her work at the market and put me to bed, and that was life.
    """

    menu:

        "What did your mother do for work?":
            $c=5

        "What about your other parent?":
            $c=6

        "Carry on.":
            $c=9



if c==5:

    if game.playerbackground == "Trader":
        $textinsert = "Yes I know you know. But what you might not know is that those"
    else:
        $textinsert = "Those"

    butcher """

    Something that will make me sound, perhaps, like a hypocrite.

    She worked for the state.

    Many people did, well I suppose that almost as many still do, in Alexisgrad. In many ways the bourgeois revolution is still young, the last vestiges of feudalism still haven't died.

    Let me explain. Alexisgrad, being a bloated, pustulating mass of humanity even then, had multiple market squares, more or less one for each district of the city, which would fill up with traders from all over the country every morning, with many of the traders who came from further afield leaving again at night.

    [textinsert] squares used to be state-owned, used to be state land. Land that should have been open to all who needed it for the purposes of keeping themselves financially buoyant, and therefore alive, was regulated by our wonderful senate. And it was, along with many others, my mother's responsibility to keep it all ticking over.

    Somewhere between event organiser and bouncer. She was a lackey, of course, the lowest link in a chain that, through several hundred other links, many of them almost certainly completely pointless, reached all the way up to our fine elected representatives.

    The pay, I'm sure, wasn't good. My mother took an order of magnitude more money in tariffs for the use of 'public land' from the stall holders than she was ever paid herself. She handed that petty bourgeois cash up that pointlessly long chain, just so it could be embezzled long before it ever reached the senate treasury.

    Sorry, I'm getting sanctimonious again, aren't I? I {i}am{/i} a shit.

    My mother helped to run the local market, making sure dues were paid, merchants were happy and no one seriously hurt anyone else. That's the answer to your question.
    """

    $Mik5MotherJob = True 
    $game.butcher.like += 1

    menu:

        "Okay. I also wanted to ask about your other parent." if Mik5OtherParent == False:
            $c=6

        "Okay, carry on.":
            $c=9



if c==6:

    butcher """

    Ah yes, the other parent. Technically I had two mothers. But only one of them was ever a proper parent to me. The other was just that woman I only ever met two or three times, the one I only realised later my mother had never stopped loving.

    But love is a bitch, to put it delicately. Mother promised her love everything, most importantly - at least in my highly biased mind - a baby. But that other woman fell in love with someone else while I was still in my mother's womb.

    I'm not sure I should tell you who she fell in love with. Purely because you won't believe me.
    """

    "Mik looks you up and down before shrugging."

    butcher """

    Fine, I'll tell you the living cliché that is my life.

    The other woman, the woman who was technically my other mother, fell in love with a juggler and ran away to join the circus.

    It's true. And I can prove it. Because if it wasn't true, do you really think that I would have come up with it? I hope you can give me more credit than that. True, when I lie I always do so eccentrically, but I would never, never be caught dead parading a cliché.
    """

    $Mik5OtherParent = True

    menu:

        "I believe you. What did your other mother do for work?" if Mik5MotherJob == False:
            $c=5

        "I believe you. Please, carry on with your story.":
            $c=9

        "I believe you. You're right, you're much too avant-garde to come up with anything nearly as interesting as 'ran away to join the circus'.":
            $c=8

        "I don't believe you. If you had connections with the circus you would have run away yourself to join it long ago. I hear they're always looking for new clowns.":
            $c=7

    jump reevaluatebutcher5



if c==7:

    butcher """

    Ha.

    Believe me or not, I'm not changing the story. I cannot be arsed making up something suitably mundane and yet unique enough.
    """

    $game.butcher.like -= 2
    $game.butcher.att += 2

    menu:

        "Okay. What did your other mother do for work?" if Mik5MotherJob == False:
            $c=5

        "Okay. You can carry on.":
            $c=9

    jump reevaluatebutcher5



if c==8:

    "Mik smiles at you, a glint in their eye."

    butcher """

    I pour my heart out to you, and all you can do is insult me, is that it?

    Well I hope you're ashamed of yourself.

    And I hope that your shame blinds you to the fact that I cannot in good conscience deny your allegations.

    Ah, maybe one day I'll pull myself out of my arse enough to actually have fun. Maybe once the revolution comes, eh?

    Now let's change the subject before you say anything else true about me.
    """

    $game.butcher.att += 4

    menu:

        "Okay. What did your other mother do for work?" if Mik5MotherJob == False:
            $c=5

        "Okay. You can carry on with your life story.":
            $c=9

    jump reevaluatebutcher5
    


if c==9:

    butcher """

    Very well, I shall.

    By the time I was old enough to actually start noticing, the city had already changed. I am assured that when I was a young child I could play happily outdoors without worrying whether I should tie a cloth around my mouth because the wind was blowing the wrong way. But my awful human memory doesn't contain an imagine of Alexisgrad which does not contain a haze of smoke.

    I also do not remember a time when it would have been possible to play in those streets without the fear of being crushed by the crowds of hungry, homeless proletarians who now fill every square inch of them, but again I am assured that I did, briefly, live through such a time.

    As it happens, and again I wonder how much of who I am now is because of this fact, almost all my memories are from the time after my mother lost her job.

    I spent many pointless weeks, once, finding out exactly what had happened, but I don't need to bore you with the details.

    Let me just say that the market in which my mother worked, which had once at least masqueraded as public land, admitting farmers and traders from all over the region, was sold to an agricultural magnate, who barred entry to all traders outside her syndicate and sacked most of the previous staff.

    That was my mother's death warrant.

    I am not proud of what my mother did. Yes, she was working at the very bottom of the statist power structure, but she was, every day, in a small way, supporting the oppressive power of the state. Yet there is a part of me, a weak, fleshy part that I'm deeply ashamed of, of course, which feels nothing but rage at the people who cut her loose for no good reason.

    Because after she lost that job, she took the only other one she could find: working at a factory.

    She could have waited, using what little money she had left to keep us fed while she searched for something better, something that would not break her. But she was a practical woman, much more practical than I will ever be I fear, and she knew which way the wind was blowing.

    There were simply too many people coming to the city, and 'unemployment rate' was a phrase even I, a small child, was familiar with. The jobs in the city were few and more exploitative than any work in history has ever been, but if you were willing to work yourself to death for nothing, then at least there was work, which is more than could be said for the countryside.

    I will not bore you with all the details, again, but modern science did three things almost simultaneously: on the one hand it both killed almost all skilled work everywhere it touched and vastly reduced the need for agricultural labour and on the other it created thousands of industrial jobs in cities.

    The state threw her out and the bourgeoisie took her up, straight into their cage.

    I said I don't really remember that first apartment we lived in. And yet I remember the day we moved out of it.

    I remember what we arrived at.

    I'll spare you the details, unless you want them. But let me cryptically say that it just wouldn't be physically possible for something as desperate and decrepit to exist here.

    It is a miracle - by which of course I mean it was extremely lucky - that any of us survived as long as we did.

    It was also there, in those early days, that my mother made the biggest mistake of her life. I know that now, but I was a child at the time and had no idea what I was letting her do.

    We moved out of my first home before we had to. She had a little money left and she should have saved it for food, or kept it hidden away for when she fell ill. But she spent it on one of the only two things she believed in.

    She was always a devout follower of the pantheon, it was only when we became too desperate to afford the time off work that she stopped dragging me to church every week. But she realised that the church did not need her help.

    No, she spent the money on the only {i}other{/i} thing she believed in, the only other thing that gave her the hope she needed to push herself awake every morning.

    Me.

    She knew the money wouldn't go far and she knew that spending it on school would be a waste. So she found me a tutor.

    We could only afford her for about a year, once a week, even at a charitable discount, but it was enough. I was hooked on learning. There are still public libraries, a bourgeois-socialist initiative that no-one has thought of a legitimate reason to tear down yet, and most of my young life was spent waiting for a chance to go to one, and very occasionally getting to.

    My mother spent the only spare money she would ever have again on teaching me to think. She shouldn't have done it. She was a practical woman and she must have known there were a million better things to save the coin for.

    But instead she used it to buy me a gift.

    The best gift money could buy.
    """

    menu:

        "Who was your tutor?":
            $c=11

        "I do want to hear more about where you lived, actually.":
            $c=10

        "*Motion for Mik to carry on with their story.*":
            $c=12



if c==10:

    #JE: IMPORTANT this should not be woodsman background, it should be whether the Alderman stair collapsing scene has happened yet or not.
    if game.playerbackground == "woodsman":
        $textinsert = "I was traumatised by collapsed stairs long before you lot all were."
    else:
        $textinsert = ""

    butcher """

    Ah, a fan of horror stories are you? I've never seen the point in scaring oneself. I could say 'the world is scary enough as it is', or, 'I have lived through enough horror stories for one lifetime', but really I think it's because I'm a coward.

    But anyway, the building was ancient. I doubt it was ever grand, but at some point in the past I imagine it had been functional. It was built to be apartments and each one would probably, a couple of hundred years ago, have been quite similar to the one we had just left.

    That may not seem very long ago to you. Here in Lotosk it feels like change is just a thing that happens to other people.

    But it wasn't the last two hundred years that had reduced that building to what it was, it was the last twenty.

    The apartments had never been large, but by the time we got there each one was subdivided, walls of plaster or soft wood or paper thrown up as partitions, none thick or strong enough to keep out the smell of the families 'next door', let alone their sounds.

    Even with iron stairs bolted onto both sides, front and back, of the structure the choice was between a 'home' which you could only access by walking through other family's 'homes', or one that other families would have to walk through to get to theirs. We were lucky to have the former. And not on the side with the stairs that fell off.

    They never fixed the holes that those stairs left when they came down. But they did, eventually, clean up the bodies of the two who died crushed under them. But not, of course, before all the iron was salvaged. [textinsert]

    Those weren't the only holes in the building either, of course. I think the roof more or less held out for the first year or two that we were there, but by the time I left there was a complex system of gutters and floor holes for rain water, because whenever it rained the upstairs apartments would have flooded if they hadn't drained the water down to the neighbours below them.

    You've asked me before about why I moved up north, and I think I said something, witty and charming I'm sure but also flippant, about the fresh air. Which may seem odd coming from someone who spends most of their life locked inside with pig carcases.

    I tell you, and I hope for your sake you never have the opportunity to test this, that the smell of pig offal is like perfume after almost two decades in that building. On the good days the wind blew the smoke from the factories in through the broken windows and cracked masonry and you couldn't smell anything for choking.

    The rest of the time...there is a term, in biology. Biomass. I've always thought of it, more or less, as things that can rot. Well that building, from basement to bare, tile-less roof, was nothing but biomass. All of it was rotting.

    It was a rare day that you could pick out one smell: the damp, the remains of food, the urine, the shit, the cum, the sweat, the soot, the just general, miscellaneous 'dirt' that meant that nothing was allowed to remain 'not black' for long.

    And we were the lucky ones. The city was only built for so many people, and even after the slum landlords did what they did to my building to countless others all over the dock and worker's districts, there just weren't enough places for people to live.

    The state said that building was a private enterprise to be handled by private business, and private business, the bourgeoisie, didn't have any interest in building anything for workers who they weren't paying enough to afford the rent that would make building their houses worthwhile.

    So the poor, the really poor, those who couldn't even get the back-breaking, lung-shredding jobs, they lived in shanty towns, 'dwellings' made out of whatever scraps they could find.

    The lucky ones had roofs sturdy enough to crush them when the walls collapsed in the middle of the night.

    But now I'm going off topic. You wanted to know where I lived, and I've told you.

    I hope that was grisly enough to satisfy.
    """

    $game.butcher.like += 2
    $game.butcher.resp += 2
    $Mik5Home = True

    menu:

        "I also wanted to ask about your tutor." if Mik5Tutor == False:
            $c=11

        "*Motion that Mik should carry on with their story.*":
            $c=12



if c==11:

    butcher """

    My tutor?

    I don't think about her often. As I said, I only knew her for a year.

    I remember her name, I think. Lila Ayad. She wasn't particularly kind, she had a cold, reserved manner. When I do think of her I wonder what she went through in her life to give her that. Perhaps it was some profound betrayal that left her cut off from the world?

    Maybe she'd just always been a bitch.

    Either way, the one thing she did love was learning. I think most of the children she tutored were the kids of bourgeois factory owners or state officials, the kind of children whose class meant that they had to do well academically, regardless of whether they had any passion or aptitude for it.

    So I think she saw something she didn't expect to see in me. Gods no, she wasn't a revolutionary. I imagine she was the daughter of a rich merchant, or something similar that would allow her to live in a nice apartment half-way across the world from where she was born on the small wages of a part time tutor.

    But I think she could appreciate people who could see past the world in front of them. She talked a great deal about philosophy. You know, knowing what is or isn't real. I think that's all meaningless crap, a toy that the bourgeois use to distract themselves from seeing the world they have created, but I lapped it up as a child.

    Oh, I'm not calling myself some kind of child prodigy. I'm not trying to say that I was gifted. That 'seeing beyond what is there' is difficult for adults, but it's easy for children. Or at least, children who have not been drowned in their own parent's propaganda since the day they were born.

    No, I'm just trying to say that I cared. That I was interested. Again, easier for children. But maybe much easier for children who weren't handed the world as their plaything from year one.

    Anyway, I'm soliloquising again.

    If you wanted to know what she taught me, I'll tell you that she taught me all the basics: polishing up my reading and writing, mathematics, rudimentary science, bourgeois history and geography. But most importantly, she taught me the joy of arguing, and reasoning.

    All that metaphysics might be a waste of time, I mean who really cares what makes one object different from another? but it is a great way to practice rational debate. A completely meaningless toy-box to practise with, teaching you how to use all the tools of logic and reason and rhetoric.

    I used to love games when I was younger, and arguing was always my favourite of all.

    On the other hand, if you wanted to know who she was as a person, then I commend you for caring about a single, arbitrary stranger who may not even still be alive in a city hundreds of miles away.

    What I remember is that she was a short, older woman, or at least she appeared old to my young, proletariat eyes that rarely saw anyone who lived to see their 'golden years', with dark skin and darker hair.

    I remember that she had grown up in Il Fersaai and that she moved to Alexisgrad mostly because she fancied it. I remember finding that odd, that anyone would choose to move to Alexisgrad when they could have lived somewhere else. But I never really asked why. I regret that I didn't, but I suppose it would have been rude.

    So there, my tutor.

    I'm going to be honest [game.player_name], that was probably an utterly pointless question to ask. But then most are, aren't they? At least until we all start answering 'how are you?' honestly.
    """

    $Mik5Tutor = True

    menu:

        "Fair enough. Now tell me about where you lived?" if Mik5Home == False:
            $c=10

        "Fair enough. Please do carry on with your story then.":
            $c=12

    jump reevaluatebutcher5



if c==12:

    butcher """

    After the money was gone, nothing ever went right for my mother again.

    Rising tensions led to a reduction in trade with the Kingdom. I'm sure that throwing tariffs around feels like the 'safe' approach for our glorious leaders, but when they have also forced their people into a position where they must live or die on the whims of the market, a twenty percent increase in the tax on iron here or a cap on agricultural imports there can literally kill people.

    The Kingdom retaliated with a tariff on Republic textiles. Demand fell; prices fell. Someone had to take the hit, and it wasn't going to be the bourgeoisie. And by that time there were enough starving people on the streets of Alexisgrad that they could simply demand: 'you will take a pay cut or you will take nothing'.

    My mother took the cut, of course. It was a choice between a slow death and a quick death. I couldn't blame her for choosing either, but I would not be here today if she had chosen to walk out.

    No, sorry, I just misspoke. I shouldn't have said 'slow death'. It was the choice between starvation and starvation you could savour.

    Less than a year after my last lesson, I volunteered to take a shift at the factory. My mother cried when I told her, but she did not try to stop me. She quite literally couldn't afford to.

    Now I know you probably want all the details of those years. You expect me to tell you about all the injustices I and my fellow working child proletarians faced on that factory floor.

    But I can't talk about it.

    Let me let you into a little secret.

    This is what, the fifth time we've spoken one-on-one in the last several weeks?

    I'm sure you've done plenty of gallivanting with all the other locals, lots of opening of hearts and pouring out of souls.

    But before today, you've got nothing but theory, theory and theory out of me.

    Yes, surprisingly self aware I know, but it gets better.

    Maybe there is a reason I only ever talk theory? Maybe it is because practice, history, reality, is just too painful?

    I honestly don't know. But it's some pretty convincing-sounding psychoanalysis bullshit. Makes me sound very deep, doesn't it?

    Regardless, it is too painful. It was far, far too painful, and now even the scars of the memories of it are too harsh for me to look at.

    But I survived, unlike so many. And with all my fingers in tact, which I think is some kind of record.

    My mother did not survive. But not long before she passed, she did give me one final gift. She called in a favour: a butcher whom she knew from her days working the market had just lost his daughter, and needed a new apprentice.

    Yes, of course, all my principles despise nepotism. But show me a man who will choose death over mild hypocrisy and I will show you a dead idiot.

    I took the job, which kept me in the same district and same 'home' that I had lived in since the privatisation of that market. Not long after, as I said, I was living there by myself, but I was just about old enough for that and besides, no-one was going to hurt me. Despite what our oppressors would say, there is infinite fellowship and decency in the proletariat.

    Still, I saw a different side of life as a butcher's apprentice. It is disgusting that any human in our modern world should be reduced to the position of equating food with hope, but that is what I saw every day. People pushing their way through our door for the scraps that would keep them alive from one day to the next, the fuel for their hope that one day they will live to see better lives.

    I saw that life could be better, that it could be more. Well, to be fair, it wasn't all as pure and symbolic as that. I was out of the factory and eating enough that hunger was no longer one of the many things that kept me awake at night in that damp, rotting half room I called home.

    I wasn't happy during those years. I am sure I was happier as a child. But I felt … well it depends if you want to be charitable. I suppose I could say I felt at peace. I could also say, if I wanted to tell the truth, that I was numb.

    My mother's death had been a long time coming. Even if I had not watched her bend and shrivel, I would have known she did not have long. The reality of the industrial turn-over of human life was all around me, every moment of my life.

    There was no indication that my mother would be any different from anyone else's mother. She would work until she broke, or she would stop and starve. Having chosen the former, the only question was how long she would have to wait.

    Even {i}I'm{/i} not enough of an emotional wreck to say that it was a relief when she died. It wasn't. But I no longer felt like I was waiting. The worst had come, as I knew it would, and there was nothing more to dread.

    And nothing left to live for.

    It was unfair on my boss. He was hard-working and kind and gave me an opportunity that quite literally saved my life. And my spirit, if I believed in such things.

    I repaid him with hard work, but it was under him that I finally turned into the unthinking, unfeeling automaton that the bourgeoisie always wanted me, and everyone like me, to be.

    It wasn't my work. My work was good, clean, honest work, the kind that any person should be proud of.

    They didn't even have to have me in one of their factories to break me, although my years in one certainly wore me down to the point where I could snap.

    Like all good villains, they got to me through someone I loved.

    The only thing that saved me, eventually, was my discovery of the revolution. I had heard about the movements, the socialists, when I was in the factories, and I found out all I could about them without ever actually consciously meeting one. It wasn't until my mother had died and I found my life empty that I eventually had the courage to seek one out.

    And the rest, like everything else I've already said so I don't know why it's worth making a distinction, is history.

    I became a student of the revolution, became disenchanted with the Alexisgrad socialists and their favouring of statist communism and, when that butcher who had been kind enough to take me in died of one of those painful and slow city diseases, decided to run as far away as I could.

    I don't think I have to justify that. Philosophically it {i}is{/i} a bit muddy, you could call me a coward and a deserter if you want, but firstly I don't care and secondly I don't think I am. It is the communists who dismiss the rural proletariat and they are mistaken to do so. But personally my only regret is that I could not leave that city earlier.

    But regrets are near useless and dwelling on them is infinitely worse. So on with the future, I say. I'm more than happy to put that past behind me and look forward to the eternal night's revolution.

    I've always preferred dreaming to remembering anyway.
    """

    menu:

        "Thank you for opening up.":
            $c=16

        "Maybe remembering is a waste for you, but for me it's learning.":
            $c=17

        "You're right, that was all a waste of time.":
            $c=15

        "You glossed over your conversion to anarchism pretty quickly.":
            $c=14

        "Why didn't you leave earlier?":
            $c=13



if c==13:

    butcher """

    For the most practical, bourgeois reason imaginable.

    Money.

    Do you have any idea how difficult it is for a young person without even enough money to feed themselves to get all the way up here?

    No-one of means from the south ever wants to come all the way up here, so why would anyone have bothered to put in place any easy way to get here? Even when I did finally have enough coin to keep myself alive on the journey up, I was still mostly begging rides on the backs of old carts.

    As for where I got the money to both travel north and set up a life here, I was left most of what my boss had when he died. I don't think I was ever good at it, I was far too self-obsessed for that, but I was the closest thing to a child that he had.

    So I got the pocket change that was all he had to show for an entire life on earth and I used it to build something better for myself.

    It's not perfect, but I'm not regretting it at all so far.
    """

    $game.butcher.resp += 1
    $Mik5Travel = True

    menu:

        "Thank you for opening up, about everything.":
            $c=16

        "Maybe remembering all of this is a waste for you, but for me it's learning.":
            $c=17

        "You're right, that was all a waste of time.":
            $c=15

        "You glossed over your conversion to anarchism pretty quickly." if Mik5Anarchist == False:
            $c=14



if c==14:

    butcher """

    Well as I implied in my characteristically direct yet endearing way, there is not much to tell.

    If you're hoping for some kind of underground arcane induction ceremony, some moment of revelation, or months strapped into a chair while some mystic brainwashed me, then I am sorry to disappoint.

    I attended a meeting. Okay, fine, it was literally underground, but in reality it was a group of people in a smokey, smelly room talking. There weren't even many grand speeches.

    And I do not remember the moment that my eyes passed around the room and first alighted on the man who would be my guide, the man who reasoned out the truth and justice of the collectivist anarchist revolution.

    There must have been that moment, but it did not stand out. I just remember, over the course of several sessions in which I talked and smoked and drank with these thinkers, workers and leaders who called themselves 'socialists', I realised that one of the factions was right while all the others, while well meaning, were all, in their own unique and self-deceiving ways, wrong.

    I found my group and I made friends for the first time since I was a child. Some were better company than others, you learn quickly in revolutionary circles that just because people understand the same things you understand doesn't mean that they're not cunts, but we all shared the same dream.

    But, as I believe I've mentioned before, there weren't enough of us. My friend, brilliant and charismatic, the most intelligent person I've ever met, just couldn't subvert the vogue for communism. No matter how clearly he laid out the truth, even there, the corruption of the state was too strong.

    And so, when I was given the opportunity to leave, I left. To carry the message to what I hoped would be more fertile ground.

    I fucked that up. But I don't regret it.
    """

    $game.butcher.like += 1
    $Mik5Anarchist = True

    menu:

        "Thank you for opening up, about everything.":
            $c=16

        "Yeah, I can see why that was all a waste of time for you. But I don't care about that, because I found it interesting.":
            $c=17

        "You're right, that was all a waste of time.":
            $c=15

        "You say you were given the opportunity to leave, but why didn't you leave before?" if Mik5Travel == False:
            $c=13

    jump reevaluatebutcher5



if c==15:

    "Mik laughs, a genuine belly laugh."

    butcher """

    That's fucking rude [game.player_name].

    Genuinely, an awful thing to say to a person who has just slapped their naked, pained soul onto the table.

    You should have told me to shut up as soon as you could tell this was going to be another monologue. But then again maybe you were hoping that I'd just get to the point, eh?

    Well the joke's on you, my life's been a meaningless waste and there is no point.

    But if it was a waste of your time, then I won't waste any more.

    Goodbye [game.player_name]. Next time you see me I'll be sure to have something more constructive to say.
    """

    $game.butcher.like -= 4 
    $game.butcher.att += 2

    return



if c==16:

    $game.butcher.like += 1  
    $game.butcher.att -= 2

    if game.butcher.att > 5:
        $textinsert = "Especially someone as attractive as you."
    elif game.butcher.like > 19:
        $textinsert = "Especially someone that I'm beginning, despite myself, to actually quite like."
    else:
        $textinsert = ""

    butcher """

    Oh don't give me that sappy look. You're not a long-lost lamb and I'm not your overjoyed, reunited-at-last mother.

    The story of my life is just that, a story. It doesn't do me any good to keep it to myself, so I don't see why you should thank me for sharing it.

    But you are welcome, I suppose.

    Sorry, perhaps I'm being a little defensive. It is difficult to talk about. But I should get over that. Maybe if more people knew what it was like, if more people realised what life actually is for those most directly under the thumb of the bourgeoisie, they would be more ready to understand what must be done.

    Ah, there I go, covering up my feelings with theory again.

    Actually, I want to thank you. For listening. Both because of those self-righteous revolutionary reasons, but also, you know, personally.

    It's good to have someone to just listen. [textinsert]

    But I should go now. I've come close to thinking about things I don't want to think about and I want to do something therapeutic to put them out of my mind. Something like gutting a pig.

    I will see you again [game.player_name], I hope? Although I warn you, I feel another collectivism lecture coming on.
    """

    return



if c==17:

    $game.butcher.like += 2
    $game.butcher.resp += 2
    $game.butcher.att += 2

    if game.butcher.att > 5:
        $textinsert = "Especially someone as attractive as you."
    elif game.butcher.like > 19:
        $textinsert = "Especially someone that I'm beginning, despite myself, to actually quite like."
    else:
        $textinsert = ""

    "Mik smiles, the crooked angle of their lips and the hint of teeth not quite hiding the genuine warmth in their eyes."

    butcher """

    Well I'm just glad I could be of service. And since I've been of service, let me re-establish my credentials as the town socialist by conspicuously not asking for recompense.

    The story of my life is just that, a story. It doesn't do me any good to keep it to myself, so I don't see why you should thank me for sharing it.

    But thank you for your enjoyment, I suppose.

    And in all honesty, because why stop being honest now? it is difficult to talk about. But maybe if more people knew what it was like, if more people realised what life is actually like for those most directly under the thumb of the bourgeoisie, they would be more ready to understand what must be done.

    Ah, there I go, covering up my feelings with theory again.

    Actually, I want to thank you. For listening. Both because of those self righteous revolutionary reasons, but also, you know, personally.

    It's good to have someone to just listen. [textinsert]

    But I should go now. I've come close to thinking about things I don't want to think about and I want to do something therapeutic to put them out of my mind. Something like gutting a pig.

    I will see you again [game.player_name], I hope? Although I warn you, I feel another collectivism lecture coming on.
    """

return
