label butcherscene8: 

$Mik8Capitalism = False
$Mik8CapNotWar = False
$Mik8Utopia = False
$Mik8AnarchoCapitalism = False

#JE: this event will either trigger at Mik's shop or at the player's home, depending on which side the first conditional lands on.

if game.butcher.like > 24 or game.butcher.romance == True:
    $textinsert = "I"
else:
    $textinsert = "I don't like you, but I do"

#JE: This shouldn't be like, it should only be something if the Alderman story has finished and 'no-one' was elected as the new leader.
if game.butcher.like > 24:
    $textinsert2 = "Well, after that little stunt you pulled, things have already moved, but it's so far from the correct way to carry out the social revolution that given its chance of success, zero, it's not even worth discussing. So thank you, I suppose, but ultimately it will only make the revolution easier. It is {i}not{/i} the revolution itself."
else:
    $textinsert2 = ""

#JE: same as above
if game.butcher.like > 24:
    $textinsert3 = "But regardless of your kind-hearted but naive attempts to cut 'destructive' out of the list of necessary conditions of the revolution, things are moving, and "
else:
    $textinsert3 = ""

if game.butcher.resp > 25 or game.butcher.romance == True:
    #Starts at player's home.
    
    "There is a knock at your door, rhythmic and firm. Mik gives you a dry smile when you answer, a challenge and an apology."

    butcher """

    I thought I would find you slacking [game.player_name].

    No, don't challenge me on that. We both know it isn't fair as much as we both know that I'm not going to apologise for it.

    Instead let me cut straight to the chase.

    [textinsert] respect your opinion [game.player_name]. You have a way of cutting to the bone.

    Trust me, I know that talent when I see it.

    Things are moving. [textinsert2]

    [textinsert3]I'm not used to that. I know that I'm very good at talking about the game, but it's coming remarkably close, I feel, to the point where I might actually have to play it.

    I believe in reason, [game.player_name]. I believe in freedom of information and thought. I believe in the scientific method, of challenging ideas, ideals and traditions.

    I am confident that I am right.

    But if this is really going to happen, I realise that I owe it to my own beliefs and my own convictions to check it all, one last time.

    And I can't think of anyone else more suited to helping me than you.

    So, [game.player_name], what do you say? What have you got, what fatal flaws have I missed, what chinks in the armour of my convictions will send me falling to the ground?

    Why is collectivist anarchism wrong?
    """
    
else:
    #Starts at butcher's shop.

    """
    Mik's shop smells different. It has been a gradual change, from the familiar, hot, rich smells of meat and rot to something foreign, cold and stinging, like a breath of cool night air through clear, raw sinuses.

    One thing that hasn't changed is Mik, who greets you with a weary smile as the bell above their door chimes your arrival.
    """

    butcher """

    Come slithering back have you? I must say, I'm surprised. I would have thought you'd stop coming much earlier than this.

    Still, you're here, I might as well make use of you.

    No, don't get your hopes up. Work is slow today, as it has been for a while. You hunters aren't doing the work you should be doing.

    But things are moving quite fast all of a sudden on the revolutionary front. I know that I'm very good at talking about the game, but it's coming remarkably close, I feel, to the point where I might actually have to play it.

    I believe in reason, [game.player_name]. I believe in freedom of information and thought. I believe in the scientific method, of challenging ideas, ideals and traditions.

    I am confident that I am right.

    But if this is really going to happen, I realise that I owe it to my own beliefs and my own convictions to check it all, one last time.

    I can think of several people who could probably help me with this better, but none of them are currently standing in front of me, so I guess it's going to be you.

    So, [game.player_name], what do you say? What have you got, what fatal flaws have I missed, what chinks in the armour of my convictions will send me falling to the ground?

    Why is collectivist anarchism wrong?
    """

menu:

    "Why question your beliefs Mik, you know you're right.":
        $c=1

    "If you're looking for arguments, it could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works.":
        $c=2

    "You've never actually explained exactly how anarchist collectivism works.":
        $c=20


label reevaluatebutcher8:

if c==1:

    "Mik gives you a long look."

    butcher """

    I can't tell if you're being sarcastic or short-sighted.

    And while I appreciate the venom of the first and the commitment of the second, neither is useful right now.

    Not questioning our beliefs is how we ended up in this mess in the first place. Well, partly. Nodding along and accepting is the ultimate expression of the oppressed. It's why I can't stand dogs…

    As for my own position, intellectually I understand why you may want me to apologise for being dogmatic. But that would be stating that you were correct when you confused passion and drive for obedience.

    For future reference, it's all about the sparkle of the eyes. Never trust a revolutionary without it, never trust a statist with it.

    But can we actually get on with it? I have a revolution to foment.
    """

    $game.butcher.resp -= 2

    menu:

        "If you're looking for arguments, it could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works.":
            $c=2

        "You've never actually explained exactly how anarchist collectivism works.":
            $c=20



if c==2:

    "Mik opens their mouth, closes it, sighs, then smiles."

    butcher """

    It's not particularly useful pointing this out, but I can't help myself. I just can't miss an opportunity to be a pedant.

    Even according to that narrative, it's not competition that propels progress. It's adversity.

    As I said, that's not a particularly helpful thing to point out, since I would propose to get rid of both, but I'm going to say anyway that it is worth remembering.

    I think we can both agree it would be abhorrent if I proposed that we wage war with another country solely because war is good for making scientific advances?

    And yet that is the same argument that the capitalists make when defending their position. They justify their creed because it drives progress, but I think I have just, very succinctly, proved that increased progress is by no means a universal shield to any criticism.

    War is not justified by progress, so why should oppression?

    But that's an aside. There is a more fundamental point that must be made.

    I can see the logic behind the idea that adversity drives progress. Desperate people try desperate things.

    But is desperate what you really want? We're not living in caves rubbing sticks together any more. We're building coal-powered machines, thousand-mile roads, we're breaking down the barriers of biological sex. Do we want desperate, or do we want reasoned?

    Do we want intelligent, educated people devoting time and energy, or do we want desperate, starving people who do not even have any time or energy to give?

    Science is a big boy now. A few scraps of wood and a rumbling belly can only get you so far, and science has already made it further than that. Bring me a famous scientist and I will show you a fat bourgeois.

    I don't hold that against them, well, no more than I hold their position against every member of that class. But I think it's horsecrap to say that the adversity they create is helping those they oppress to strive. Because it's not.
    """

    $Mik8Capitalism = True

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?":
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it.":
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?":
            $c=13

        "I can see why a collectivised populace with a socialist education would innovate more, not less, than the society we have now. We can move on.":
            $c=19



if c==2:

    "Mik opens their mouth, closes it, sighs, then smiles."

    butcher """

    It's not particularly useful pointing this out, but I can't help myself. I just can't miss an opportunity to be a pedant.

    Even according to that narrative, it's not competition that propels progress. It's adversity.

    As I said, that's not a particularly helpful thing to point out, since I would propose to get rid of both, but I'm going to say anyway that it is worth remembering.

    I think we can both agree it would be abhorrent if I proposed that we wage war with another country solely because war is good for making scientific advances?

    And yet that is the same argument that the capitalists make when defending their position. They justify their creed because it drives progress, but I think I have just, very succinctly, proved that increased progress is by no means a universal shield to any criticism.

    War is not justified by progress, so why should oppression?

    But that's an aside. There is a more fundamental point that must be made.

    I can see the logic behind the idea that adversity drives progress. Desperate people try desperate things.

    But is desperate what you really want? We're not living in caves rubbing sticks together any more. We're building coal-powered machines, thousand-mile roads, we're breaking down the barriers of biological sex. Do we want desperate, or do we want reasoned?

    Do we want intelligent, educated people devoting time and energy, or do we want desperate, starving people who do not even have any time or energy to give?

    Science is a big boy now. A few scraps of wood and a rumbling belly can only get you so far, and science has already made it further than that. Bring me a famous scientist and I will show you a fat bourgeois.

    I don't hold that against them, well, no more than I hold their position against every member of that class. But I think it's horsecrap to say that the adversity they create is helping those they oppress to strive. Because it's not.
    """

    $Mik8Capitalism = True

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?":
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it.":
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?":
            $c=13

        "I can see why a collectivised populace with a socialist education would innovate more, not less, than the society we have now. We can move on.":
            $c=19



if c==4:

    butcher """

    Let me see if I understand this. Your genius idea for ending oppression and bringing in a new golden age of the bourgeoisie is: don't change anything, it's all good?

    Also, the basis of your plan was 'what if everyone were bourgeois' and I give, what, two sentences of criticism and your fix is to reintroduce the proletariat?

    I think the kindest thing to do would be to move on, no?
    """

    $game.butcher.like -= 4
    $game.butcher.resp -= 4

    menu:

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47



if c==5:

    butcher """

    Fine, your logic doesn't fall apart at the first hurdle. I did not want to do this, but that regrettably leaves me with more practical concerns.

    Namely, you talk about everyone owning the factors of production. But if everyone owns the factors of production, who will work them? The progress of which you speak so highly has already changed the facts of production too much for it to be possible for individuals to fully operate their own resources.

    It takes hundreds of people to work a factory, but if everyone is too occupied using their own resources, then that factory will sit unused for want of labour.

    No, in the age of industry, collectivisation or oppression, be that bourgeois-capitalist, statist-socialist or some other horror, are the only choices.
    """

    $game.butcher.resp += 2

    menu:

        "You're wrong. Some kind of collectivist-capitalist model could work too. Certain property, like factories, could be jointly owned by the workers of those factories. This kind of co-operative model would still have the competition of capitalism, different individuals and co-operatives working against each other, while maintaining the social justice of collectivisation.":
            $c=9

        "Under the current model, you probably are right. But that is why we need to push for innovation. It seems inevitable that, with time, competition will drive the means of production to become cheaper and that drive is in everyone's interest. Capitalism will push towards a future where everyone has access to productive technology, at which point the class war will be over because the distinction between 'the bourgeoisie' and 'the proletariat' will become completely meaningless.":
            $c=6

        "So it all comes down to 'no-one owns the property' versus 'someone owns the property'? I suppose putting it that way, it is clear that things are always going to be better when it's 'no-one'.":
            $c=10



if c==6:

    "Mik raises an eyebrow."

    butcher """

    I think I've heard this before. It's a literary term and not something I am particularly au fait with, but I believe it was 'science fiction'.

    We live in a world where the sun really didn't rise tomorrow, so I will not say anything is impossible. But you would be hard-pressed to convince me that there will come a time when productive technology is so easily accessible that it will be available to more or less everyone.

    I am afraid that I cannot even picture what that technology would look like. Certainly it could not be something that produces material goods. But what else would that leave?

    You cannot be proposing a society so advanced that what people are willing to spend money on are just services.

    We live in a society where the poor are not able to feed themselves, and you invoke a future where that problem is so thoroughly solved that the common man is capable of owning his own machines?

    Maybe if such a far fetched utopian vision were possible in, say, the next five hundred years, I would consider it an interesting proposal, but…

    But fine. Let us say that you aren't some kind of techno-fantasist and such a future were possible. I will concede that the class struggle, as it now exists, would no longer exist. 'Bourgeoisie' and 'proletariat' would, in their current form, cease to be relevant terms.

    But it would be highly naive to imagine that the world's problems would be solved. When I talk, I talk of the social revolution, the ideal of the people and the final, permanent Utopia. But your suggestion would merely produce a world where the chains of slavery were loosened.

    The problem we face is one of legacy. The bourgeois are feudal lords by a different name because money breeds money. Any kind of capitalist system will reward capital with capital, so the wealth will always flow to the top and just keep on flowing.

    Your 'progress' may end the {i}necessity of slavery{/i}, but if technology has progressed to the point that the former {i}proletariat{/i} can afford machines, then just imagine how far it will have progressed for the {i}bourgeoisie{/i}.

    Everyone being better off will not mean that there won't still be those who are significantly better off than all the others. Just because the old classes no longer make sense on a technicality would not mean that there would no longer {i}be{/i} classes. You could call it wealth disparity instead of class oppression if you really wanted, but that wouldn't stop it being immoral.
    """

    $game.butcher.resp += 2

    menu:

        "But don't you see, progress is the answer there too! Because if everyone has the ability to innovate, an ability that suitably advanced technology and access to essentials could theoretically allow, then in a truly free capitalist society, an anarchist-capitalist society if you will, then those old dynasties can always be peacefully challenged and toppled by the hard-working and innovative. As long as technology and society keeps progressing, those who strive will always be rewarded while those who stagnate will always fail, no matter their starting positions.":
            $c=8

        "You are worried about the risk of creating capitalist dynasties? A way to promote individual striving and competition while removing that risk would surely be the abolition of inheritance, correct?":
            $c=7

        "Okay fine, you win.":
            $c=11



if c==7:

    if game.butcher.resp > 25:
        $textinsert = "I shall have more of a think, [game.player_name], try to put myself in your philosophical shoes. You've said one or two things that are worryingly appealing …"
    else:
        $textinsert = ""

    butcher """

    Woah, where did that bit of hard-line statist-socialist policy come from?

    There are two points against abolishing inheritance, one of which I care about and one of which I don't.

    The one I don't care about, because I always start with the pointless one so the important one hits home, is that people aren't as selfish as capitalists would like you to think.

    You want people to work hard for themselves, but do you know how you really make people work hard? You make them think that what they are doing matters. The best way to do that is let people actually work for the ideal of the people. But the easiest way to do that is get them to work for their children and their families.

    Plus, isn't abolishing inheritance anti-liberal? I mean I don't care about that, but surely you should. People should be able to spend their money on whatever they want: drugs, sex, that extra carriage that they don't really need but will match their new mare that much better.

    But abolishing inheritance would mean the one thing they're not allowed to spend their money on is their own children. It comes across as cruel and arbitrary, even if it isn't.

    The kind of people who would drive an anarchist-capitalist world are not the kind of people who would accept inheritance laws. And good luck enforcing it with that kind of opposition.

    Which brings me to the actually important point: who is going to enforce it? And where will that capital go? There can, really, be only one answer: a state. 'Abolishing inheritance' is in all practical ways really instituting a one-hundred percent inheritance tax. No state, no tax.

    And you know my opinions on states.

    Still, you've led me on a merry chase, stretched my muscles, made me think. You've opened up avenues that are … worth considering, at the very least.
    """

    if game.butcher.resp > 25:

        "I shall have more of a think, [game.player_name], try to put myself in your philosophical shoes. You've said one or two things that are worryingly appealing …"

    butcher "But on to other topics for now, shall we?"

    if game.butcher.resp > 25:
        $game.butcher.zeal -= 2
    else:
        $game.butcher.zeal -= 1

    menu:

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47



if c==8:

    if game.butcher.resp > 25:
        $textinsert = ", their face openly both troubled and excited,"
    else:
        $textinsert = ""

    "Mik thinks[textinsert] for a long time before replying."

    butcher """

    We are talking about such far-fetched possibilities that it is difficult to think through all of the implications.

    What I see, first and foremost, is the essential nastiness of capitalism. I want a Utopia, a world filled with co-operation and neighbourly love, however sickening those words sound coming out of my mouth. But capitalism is, essentially, war. Aggressive antagonism, everyone an island, each island only able to remain free as long as it fights against all others.

    A bad metaphor. Maybe something about bricks, each one rising only by crushing all those beneath? No, that's crap too.

    Ah well, you understand me, or at least I hope you do. It's all so cruel. It's not what good people want.

    But maybe I'm being naive? I don't know. I'd have to think. But I know I don't like it.

    More troubling, but oh we're dealing with so many theoreticals that I'm really not sure what I'm saying any more, doesn't progress imply growth? Doesn't capitalism? Is that a necessary component?

    And surely growth must have a limit? Social, intellectual or geographical? Or at least might growth reach a point of diminishing returns, a point when it slows down?

    If that is true, then surely what you propose would just be a stop gap, a nice but inevitably short period of relative social freedom and prosperity before the seeds of dynastic feudalism sprout?

    I do not know. I would, and will, have to think a great deal more on this. I suppose I would have to find statistics …
    """

    "Mik makes a show of shuddering."

    butcher "You've led me on a merry chase, stretched my muscles, made me think. You've opened up avenues that are … worth considering, at the very least."

    if game.butcher.resp > 25:

        butcher "I shall have more of a think, [game.player_name], try to put myself in your philosophical shoes. You've said one or two things that are worryingly appealing and a few more that are just worrying..."

    butcher "But on to other topics for now, shall we, before your science fiction makes my brain melt out of the side of my head?"

    if game.butcher.resp > 25:
        $game.butcher.zeal -= 3
    else:
        $game.butcher.zeal -= 2

    $game.butcher.resp += 4

    menu:

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47



if c==9:

    "Mik nods their head slowly, a smile creeping along from their lips to their eyes."

    butcher """

    Clever, [game.player_name]. And not just in a cunning way, but in a thoughtful, possibly ethical way as well.

    I see the appeal, [game.player_name]. And I see the logic. It's more than just beating the bourgeoisie at its own game by taking its arguments and running with them. It's also about {i}actually{/i} empowering the workers while keeping the gate open for industry and urbanization.

    It could be glorious [game.player_name].

    For a while, that is.

    Because capitalism isn't stable. Now I'm going to try really hard to keep my tone neutral here, because I think you might very well have made your suggestion from a good place, but it still won't work.

    As you yourself have so ably, no that's getting sarcastic again, I should just say as you have pointed out, the bourgeoisie is the competing class. And while I'm sure that there are inefficiencies that can be fixed and there is progress to be made, there will still be winners and losers.

    And in a system where capital has value, which it still would under your system, capital will produce capital and therefore inequality will grow.

    Because the balance can't last forever. At some point, someone will lose and be forced to sell their shares. And then {i}bam{/i}, the proletariat is back.

    No, however noble the idea, wealth redistribution, even wealth redistribution as nuanced as co-operative ownership of the factors of production, is never going to work in the long term. It's a nice dream, as long as you're not saying it because the only fix you care about is one that will work for you, but it doesn't actually {i}fix{/i} most of the fundamental problems with our class system.
    """

    if game.butcher.resp > 25:
        $game.butcher.zeal -= 2
    else:
        $game.butcher.zeal -= 1

    menu:

        "You are worried about the risk of creating capitalist dynasties? A way to promote individual striving and competition while removing that risk would surely be the abolition of inheritance, correct?":
            $c=7

        "Okay fine, you win.":
            $c=11
    jump reevaluatebutcher8



if c==10:

    butcher """

    A pithy and eloquent way to put it, at least since the communists ruined the term 'public ownership' by making it mean 'state ownership', which is in reality just another kind of private ownership.

    Now, hit me with the next one.
    """

    if game.butcher.resp > 25:
        $game.butcher.zeal += 2
    else:
        $game.butcher.zeal += 1

    menu:  

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47



if c==11:

    butcher """

    Ah, some of my favourite words. Still, you gave me a good run on that one.

    I expect you to do just as well with the next point.
    """

    if game.butcher.resp > 25:
        $game.butcher.zeal += 3
    else:
        $game.butcher.zeal += 2

    menu:

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47



if c==12:

    "Mik nods, courteously."

    butcher """

    You're getting good at this [game.player_name]. A little too good. My argument wasn't intentionally wrong, but I'll give you that now that I look at it I did frame it … ungenerously.

    I hate that. I'm arguing against a social structure that murders hundreds of people every day, but I can't 'win' unless my arguments are 'generous'. Why is it that my points cannot have merit unless they are as kind as I can possibly bend them to be?

    No, don't answer that, it's rhetorical. And it does make sense. But I think it should be fair that I can get a little frustrated from time to time. That I have to go through all of this justification before anyone would even begin to take me seriously rankles when the system that I am arguing against is so obviously corrupt.

    I am not angry that my arguments must be perfect. I am merely incensed by the fact that bourgeois-statism doesn't have to go through the same review merely because it has cheated its way into being the status quo.

    But you made a point, and it was a good one. I graciously, shut up yes I'm gracious, rescind my previous argument and replace it with this:

    You say that capitalism is justified by the progress it creates, but war is not because the former has less of a death toll than the latter. I do not have the statistics to prove you wrong, although I am not confident they don't exist. But what I will say is: just because something is better, does not mean it is good. It also does not mean it is the best.

    But well done though. I'll say it more gently next time.
    """

    $game.butcher.resp += 4
    $game.butcher.like -= 1
    $Mik8CapNotWar = True

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?" if £Mik8AnarchoCapitalism == False:
            $c=3

        "But if everyone is living in the perfect utopia about which no-one would have any complaints, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8



if c==13:

    "Mik smiles like a shark."

    butcher """

    The heart of the issue, isn't it? If things are perfect, then why would they innovate? It sounds almost like a paradox, a logical trap, but it isn't. Because I can just say that they wouldn't.

    Because you're right, why would they?

    Yes, I know, appalling right? A society that didn't progress. What a monstrosity, what a backwards step.

    Why? Why would you balk at the idea of a heaven without a science budget? The bourgeoisie and the militaristic statists justify everything they do with the shield of progress. But why should we care?

    What has science brought us? Poverty, inequality, the destruction of the rural working class, the enslavement of the urban working class. Oh, and don't forget guns and cannons and shells.

    I realise how this sounds. I sound mad, like that one crazy person who lives in a barrel in the town market. But I believe it is at least worth considering that 'progress' is a smokescreen that the bourgeoisie and the statists have thrown up to obscure their own practices.

    Or, more cynically, a shiny object they distract us with every time we get too uppity. They say 'ah yes, but look at the {i}progress{/i}!' as if that is something inherently good in itself. But I don't see why it is.

    This belief that pushing the boundaries is an inherently good thing is as new as the inventions themselves are. Yes, I know I sound like a dying conservative, but it really is only in the last few hundred years that it has been universally 'accepted' that we need to push forward. It's by no means a historic, self-evident truth.
    """

    $game.butcher.resp += 2
    $Mik8Utopia = True

    menu:

        "But it's human nature to want to discover more about the world that we live in. It would be wrong to try to repress that.":
            $c=14

        "That's an overwhelmingly cynical way to look at this. Yes, science has given us all those things, but it has also given us medicine, sanitation and the technology necessary to give us the free time we need to come up with things like collectivist-anarchism.":
            $c=15

        "You do sound a bit like a conspiracy theorist. But I must admit, you may not be wrong.":
            $c=17



if c==14:

    "You did not think Mik's smile could become any more broad, but now it does. Before they even begin to speak, you can see that you have fallen into the trap"

    butcher """

    Oh, so people enjoy progressing? And the reason that people progress is because they want to?

    Then why would they need competition to drive them there? If curiosity is such a strong force, then the bourgeois justification of capitalism - that it leads to progress - falls away.

    And don't go putting words in my mouth. 'Repress'? Really? When did I ever say I stood for the repression of progress. Please. In fact, I have said the opposite: with their daily bread lining their stomachs and safe leisure time, I'm giving more people more time to pursue their curiosity than any capitalist system would.

    No, I believe I have you in check.

    Oh it's nice to win easily and neatly every so often.

    This is probably gambler's fallacy, but I'm feeling good. Hit me with the next thing.
    """

    $game.butcher.resp -= 4
    $game.butcher.zeal += 1

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?" if £Mik8AnarchoCapitalism == False:
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8



if c==15:

    if Mik8CapNotWar == True:
        "Mik shakes their head."

        butcher "I'm being unkind again, aren't I? And this time I probably have even less justification."
    else:
        "Mik nods approvingly."

        butcher "I am, of course, being a little melodramatic."

    butcher """

    Of course science has done, and continues to do, wonderful things. And that is why I do not think it will disappear. There will always be people who are good, clever and curious, and in my utopia all such people will have the chance to pursue progress.

    But that they will is a guess. I cannot know, I can merely predict. The people will do what the people want to do, and they will organise their own structures, from the ground up. I think I have argued why that is the best way for humanity to organise, and I do not think that bourgeois arguments for enforced progress will sway me.
    """

    $game.butcher.resp += 1

    menu:

        "But won't that lead to a great deal of waste, since people will probably be living in smaller communities so may end up researching the same things?":
            $c=16

        "I agree, progress is not a justification for slavery.":
            $c=18



if c==16:

    "Mik scratches their chin and shrugs."

    butcher """

    There will still be travel, but fundamentally I do take your point. There may be inefficiencies. But I think that is a small price to pay for utopia.

    And if I may swing things jarringly from the bourgeoisie to the state, the situation will still be better than what we have now, each state guarding their advances like dragons guard princesses. Actually, heck, you could say the same thing about corporations. So your camp doesn't fare much better than mine, eh?

    But you've made a good point and given me some pause. Not a stop, just a bit of pause. That's good, it's what I'm after. Give me something else.
    """

    $game.butcher.resp += 2
    $game.butcher.zeal -= 1

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?" if £Mik8AnarchoCapitalism == False:
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8



if c==17:

    butcher "How very kind of you. I wanted you to give me things to worry about, but I mean about my philosophy, not about my sanity, so shall we move on?"

    $game.butcher.att += 1

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?" if £Mik8AnarchoCapitalism == False:
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8



if c==18:

    butcher """

    Good, join me! There are lots more conspiracies where 'progress as a good is a myth created by the bourgeoisie to keep us in line' came from!

    But another time. Quick, get us back on track before I start talking about beings from beyond the stars. Although now that I mention it, that might explain a few things…
    """

    menu:

        "I {i}did{/i} mean competition, not adversity. In today's society the bourgeoisie is the competing class, so you stating that all of today's scientists are bourgeois proves my point. Collectivisation creates a society where everyone is, in effect, a proletarian. Why are we not aiming for a society where everyone is a member of the bourgeoisie?" if £Mik8AnarchoCapitalism == False:
            $c=3

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8



if c==19:

    "Mik pouts."

    butcher """

    It's always less fun when I don't have to put up a fight. But I suppose sometimes the opening arguments can be so convincing I don't need anything else.

    Very well, let us put those debates behind us. I'm sure there are plenty of other things you want to get your teeth into. Either philosophically or literally. I've never quite figured out if you only speak to me in the hope of getting your hands on some pork.
    """

    $game.butcher.resp -= 2
    $game.butcher.like += 2

    menu:

        "You've never actually explained exactly how anarchist collectivism works." if Mik8AnarchoCapitalism == False:
            $c=20

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45



if c==20:

    butcher """

    You know how I have to start answering that question, don't you?

    I cannot say exactly how the systems will work after the revolution, because they must be built from the bottom up by the people as a whole.

    But that is not going to stop either of us from speculating, is it?

    No, it seems clear to me that any kind of private ownership, of which the so called 'public ownership' of the communists is a type, leads to inequality, which leads to oppression, which is the death of liberty. So property cannot be owned, as such. It must, therefore, be freely accessible to all who need or want it.

    Now obviously there will be different ways of doing that, and that is what I can't really speak to. Some resources are more easily collectivised than others. It is very difficult to collectivise a single turnip, say, but it is possible to equally divide a #{i}harvest#{/i} of turnips.

    I imagine that some resources will be divided equally between all while others will simply be accessible to all. But this is where we get to the end of the line. This is the point where speculation can take us no further, only putting the ideal of the people into practice can show us more.
    """

    $Mik8AnarchoColect = True

    menu:

        "No, we can still think this through further. You say that some resources will be divided equally, but surely there should be a distinction between need and want? Some people, like the elderly and disabled, need more help than others. Surely what you should want to achieve is equity, rather than equality.":
            $game.butcher.like += 2
            $c=22

        "No, we can still think this through further. You say that some resources will be divided equally, but surely there should be a distinction between need and want? Because some people may want resources, resources that other people need, for trivial or wasteful reasons.":
            $c=21

        "Okay, thanks for clearing that up.":
            $c=39



if c==21:

    "Mik frowns at you."

    butcher "I think you are underestimating the basic goodness of free people, [game.player_name]."

    $game.butcher.like -= 1

    $c=22



if c==22:

    butcher """

    But of course there will be some level of distinction between 'need' and 'want'. Well, I say of course, rather I predict with a high level of certainty that there will be.

    Given that the post-revolution communities will be small, it should not be difficult to distinguish between who needs resources and those who simply want them. And if that can be established, then it should not be too difficult to establish how much all those who need do practically need, at which point the rest can be distributed equally between the 'wants'.

    Fair?
    """

    menu:

        "Maybe fair, but who would organise this? Who would be the one to make the decision?":
            $c=26

        "No, not fair. Because people will always want different resources to different degrees. It isn't as simple as splitting people into 'want' and 'need', especially if you are just going to divide equally. Such a system would encourage people to 'want' everything that is going, so that they could trade the resources they want less for those they want more. Those who are best at trading will soon accrue more productive materials than the others, and at that point equality will be dead and collectivism will have been replaced by anarcho-capitalism.":
            $c=23

        "Okay, that answers all of my questions.":
            $c=39



if c==23:

    """

    You see something you are not used to seeing in Mik's face.

    Panic.
    """

    butcher """

    A good point. Cynical, but I suppose I can't leave it at that.

    I'm talking to myself here, but this really is a problem, isn't it? I would like to counter by positing that, in the post-revolution utopia, everyone would be able to acquire as many resources of each type as they wanted, but I don't think I could get away with that, could I?
    """

    "Mik looks at you hopefully, then shakes their head."

    butcher """

    No, I couldn't. The social revolution will do many things, but it won't create infinite resources.

    Well the obvious practical step would be to ban inter-person trading. And really that does follow. To trade something one must have a claim on it, one must own it. But in a collectivised system, just because something is distributed to someone, it does not mean they own it.

    They do not own the object, they have equal access to the common source. Which, ah, yes, suggests another fix.

    This problem is most stark with clearly divisible objects, yes? In other words, products, the things that cannot be easily collectivised individually. But those aren't the factors of production, are they?

    Me trading my turnip for your sprouts isn't going to give me a capital advantage. Trading my turnip for a piece of your farm would, but that can't happen, because you don't have the same claim over land as you could be argued to have over your sprouts.

    In other words, it won't be possible to trade productive capital, because productive capital is non-divisible, and therefore cannot ever be distributed. All people within the society will have indivisible, equal and non-reliquishable access to all productive capital.

    So even if trading was allowed, which I'm not sure it would be, an anarcho-capitalist state would not follow, because capitalism requires the ownership of productive capital, and that will not exist under any circumstances after the revolution.
    """

    $game.butcher.resp += 2
    if game.butcher.resp > 25:
        $game.butcher.zeal -= 1

    menu:

        "You casually mention banning trade, but isn't that a violation of people's liberties? And further, wouldn't that give all of the power to the people who distribute the goods? Who would be making those decisions anyway?":
            $c=25

        "Okay, so let's take a step back. No-one owns the productive capital, and everyone is expected to work it communally. At the same time, the community will also give all the required essentials to any individual who needs them, which in greater or lesser amounts will be everyone. Why, then, should any individual put in more than the minimum amount of effort?":
            $c=24

        "Okay, that all makes sense, but it still doesn't explain who would organise all this.":
            $c=26

        "Okay, that answers all of my questions about anarchist-collectivism, we can move on.":
            $c=40



if c==24:

    butcher """

    As a whole, if the people don't want to put in the effort, then they don't have to put in the effort. They'll go hungry, but that will be their choice, and I am sure it won't be their choice for long.

    That sounds like I'm dodging the question, but I'm not. I will now though:

    I don't know what will happen.

    I don't think I can stress that enough. I grant you, what I have presented thus far is a bit idealistic, but that grants it robustness. Yeah, I know, sounds like it must be false, but that's because you're used to systems that work from the top down. If they're from the bottom up, they're much more malleable.

    I don't know what individual communities will do with slackers. But I don't need to, because each community will find its own solutions. Some groups may not care, in which case that's fine, and some may decide to be more … forceful, which is fine as well, if that is their choice.
    """

    $game.butcher.resp += 1

    $c=26



if c==25:

    "Mik nods, as if they are in a rush."

    butcher """

    Yes yes, I suppose it is.

    To your first question, that is. Thank you for asking three questions at once. The first is a good point, but something I'll have to think about more, although I think my point about the indivisibility of productive capital mostly solves the issue of trade anyway.

    As for the third question, let me elaborate, since the second was clearly just a way to introduce the third.
    """

    $game.butcher.resp += 2

    $c=26



if c==26:

    butcher """

    Who will organise the communities? A statist question. The communities will organise themselves. How? Another statist question. They will organise themselves in whatever way the people think will be best in order to build better lives for themselves, with the joint ideals of 'liberty' and 'equality' as their common bonds and causes.

    I believe I have already explained to you why those ideals will hold, why they are the only logical foundation of any utopian society. Don't make me do that again. So we may take them as read, which means nothing 'political' will be left to organise, which, let's be honest, is the vast majority of what our Senators and the like do nowadays.

    Which leaves only the unglamorous and dull administrative tasks. Which is all the better really. Managing the communities of equals will be an exercise in hard work, not a means to wield power. Who will do that work will be decided in the same way that everything else will be decided: by the people.

    Just so we're clear, when I say 'by the people' I do actually mean 'by the people'. Not by representatives, not by someone interpreting their will. No, each decision will be made by all the people, for all the people.

    There are other reasons, but that is the main reason why I can say that the world will be split into smaller communities after the revolution. Because for everyone to have a say, not only does everyone need to be aware, or to be able to be aware, of everything that is going on, they also have to have time to listen to everyone else's thoughts on it.

    Efficient? Of course not. Equal and free? Of course yes. And when you have those two, efficiency doesn't just mean less, it means nothing. When you have perfection, the speed at which that perfection is moving is a meaningless question.
    """

    menu:

        "I think it's fair to say that not everyone will be able to agree on everything all the time. So, since you say that everyone has an equal say, then surely won't that just mean that the majority on any issue can force through anything that they want? Surely that's just a form of oppression, oppression of the minority by the majority, but oppression nonetheless.":
            $c=28

        "But what if they're bad at it? Sometimes people do not know what is best for them, which is why we need experts to manage matters of state for us.":
            $c=27

        "When you put it like that, I can see how a free and equal people united by the ideal of the people would be able to satisfyingly resolve their disputes. I'm sure there would still be disagreements, but I can think of no better model for solving them. You have convinced me Mik.":
            $c=41



if c==27:

    "Mik lets out a frustrated growl and rolls their whole head, not just their eyes."

    butcher """

    No, I refuse to go through this all again.

    The people aren't idiots. That's statist propaganda. When given the reins of their own future, the people #{i}will#{/i} surprise you with their reason and ingenuity. Because, and this the liberals did get right, every person is an expert in one thing: themselves, and their own desires and needs.

    The ideal of the people is what happens when everyone's sets of expertise, their expert knowledge of themselves, come together.

    To give you an iota of credit, the management of today's societies does require expertise in society management. But to take the iota back again, #{i}that is why the communities must be small!#{/i}

    Pretending that it takes university degrees to organise anything is just one way the bourgeoisie and the statists make it appear like we need them, but we don't.

    But we've already talked about this, so can we move on please? Tell me, collectivist anarchism, yay or nay?
    """

    $game.butcher.resp -= 8
    $game.butcher.like -= 4
    $game.butcher.zeal += 1

    menu:

        "Honestly Mik, I'm not convinced and I don't think anything you're going to say is going to convince me, so let's just move on.":
            $c=42

        "I apologise, yes, you're right, you have made that point before. So yes, I am convinced, collectivist-anarchism is the only way forward.":
            $c=41

        "No, sorry, we're not done here yet Mik. If you reject that the people need guidance, then let me ask about the role of the majority. I think it's fair to say that not everyone will be able to agree on everything all the time. So, since you say that everyone has an equal say, then surely won't that just mean that the majority on any issue can force through anything that they want? Surely that's just a form of oppression, oppression of the minority by the majority, but oppression nonetheless.":
            $game.butcher.resp += 2
            $c=28



if c==28:

    butcher """

    Ah, then I have not explained myself well enough. You think I am talking about pure, as opposed to representative, democracy, but I am not. What you said is right, right up until the word 'force'. Because in an anarchist world, no-one will be able to 'force' something on anyone.

    Everything will be optional. The community may only make binding decisions so far as those decisions bind the community, not the individuals who make it up.

    So, for example, the community may make decisions about resource allocation, because that does not involve any kind of compelling action. But they could not, say, lock you up if they don't like what you do.

    Make sense?
    """

    menu:

        "So no-one can compel anyone to do anything, but you have said that a core part of collectivist-anarchism is mandatory labour. How can something be mandatory if it cannot be enforced?":
            $c=29

        "So what could the people do if there was someone troublesome? At the very least, you must admit the existence of psychopaths, or possibly more relevantly sociopaths, who can't or won't grasp the logic of your system. How would your system deal with them?":
            $c=32

        "Okay, I can see why that's not oppression. You've answered all my questions Mik, consider me convinced when it comes to collectivist anarchism.":
            $c=41



if c==29:

    "Mik blinks, slowly."

    butcher "It will not be {i}the people{/i} who enforce mandatory work. It will be the ideal of the people. Mandatory work is a logical precondition of equality, which is a logical precondition of liberty. All the people will work because they know it is logical to do so. We've talked about this all before when we discussed the ideal of the people."

    $game.butcher.resp += 2

    menu:

        "But what about people who reject the logic? At the very least, you must admit the existence of psychopaths, or possibly more relevantly sociopaths, who can't or won't grasp the logic of your system. How would your system deal with them?":
            $c=32

        "I'm sorry but that's ridiculous. Working for the bourgeoisie is a logical precondition of being able to eat within a capitalist system, but you won't accept that as a justification of the proletariat's oppression, will you? Just because your coercion is built into the logic of a system doesn't make it just.":
            $c=30

        "That does actually make sense. An even simpler way to put it would be to say that nothing will enforce mandatory labour, but everyone will simply realise themselves that it is required. Okay Mik, when it comes to anarchist collectivism, you've convinced me.":
            $game.butcher.zeal += 1
            $game.butcher.resp += 2
            $c=40



if c==30:

    butcher """

    Nice try, but no. Firstly my 'coercion' {i}is{/i} just, because it {i}is{/i} the only way to establish equality and liberty, which must be the end goals of all social endeavours. Sometimes the ends justify the means, and this is one of those cases.

    And secondly, your example does not hold water, because working for the bourgeoisie isn't a logical precondition of being able to eat. There are other, more effective ways for the proletariat to gain what they desire. Well, one way.

    The social revolution.

    No, nice try [game.player_name], but I'm afraid you haven't scored a goal this time.
    """

    menu:

        "Okay, fine, but your solution still leaves the problem of what to do about those who reject the logic? At the very least, you must admit the existence of psychopaths, or possibly more relevantly sociopaths, who can't or won't grasp the logic of your system. How would your system deal with them?":
            $c=32

        "So you are saying that your system is justified because there is no other option, but the capitalist system isn't because the people at least have the opportunity to rise up and almost definitely die in a violent class war?":
            $c=31

        "You're right, my logic was messy. I'm convinced, anarchist collectivism is the future.":
            $game.butcher.zeal += 1
            $c=41



if c==31:

    "Mik's face snaps around, the slight worry instantly disappearing in a toothy grin."

    butcher """

    I think you have made my point rather well, don't you? One system demands some labour as the cost of utopia, while the other leaves only the option of bloody, tragic conflict as a means to attain emancipation.

    Work must happen for people to survive. There is no getting around that. That the only 'oppression' enforced on the people after the revolution will be enforced by the laws of biology and physics is, I think, a strong point in my favour.

    Now, did you have any good points to make?
    """

    $game.butcher.resp -= 4

    menu:

        "Okay, fine, but your solution still leaves the problem of what to do about those who reject the logic? At the very least, you must admit the existence of psychopaths, or possibly more relevantly sociopaths, who can't or won't grasp the logic of your system. How would your system deal with them?":
            $c=32

        "Well done Mik, you've ably out manoeuvred me there and I must concede. When it comes to anarchist collectivism, consider me convinced.":
            $game.butcher.zeal += 2
            $c=41



if c==32:

    butcher """

    A problem, but a fringe problem I believe, [game.player_name]. I think you probably have a remarkably regressive view when it comes to mental illness.

    As I have already said, no people can oppress any other people, but there are still certain things that can be done. Since all resources are collectivised, I suppose it wouldn't be unreasonable for the society to restrict access to certain resources until the individual can begin acting with the interests of the community in mind.

    After all, since it is the community that produces the goods, if an individual refuses to engage productively, or actively seeks to damage the community, then it follows that the community can refuse them the benefits of membership, if they decide they wish to.

    Or, to put the same thing in better words, every action within the community is voluntary. If someone voluntarily does not engage with the community, then the community cannot be forced to maintain a relationship with that individual. They may not force the person out of the area, but they can withhold all of the benefits of membership.
    """

    menu:

        "In other words: they can't be imprisoned but they can be starved to death. I'm sorry but I find that much more morally repugnant.":
            $c=37

        "So in effect if anyone refuses to conform, their only real choice is to leave. In other words, if someone is a troublemaker, the way your society deals with them is just to send them off to be someone else's problem." :
            $c=38

        "But what about dangerous individuals? Surely a social system without any kind of policing would be vulnerable to the first person to pick up a gun and declare themselves leader.":
            $c=33

        "I think that's perfectly fair. If someone refuses to engage with the community, I completely agree that the community can refuse to engage with them. Mik, I'm ready to declare that you've convinced me on the matter of anarchist collectivism.":
            $game.butcher.zeal += 2
            $game.butcher.like += 2
            $c=41



if c==33:

    butcher """

    Now that is a very fringe case. But I suppose I should at least attempt to answer it.

    Well my gut response is to say that, since there will be no need for militaries after the revolution, it would be prudent to simply destroy all weapons of war.

    But that wouldn't work, would it? The kind of person you are talking about, and I'm sceptical that they would exist after the revolution but I'll play along, would likely hide a little horde for themselves. And even if they didn't, the statist world that we live in is so militarised that I'm sure there would always be another hidden firearm somewhere for someone to find.

    No, a better solution would be to simply fight fire with fire. I doubt they would ever be used, but I do not see why each community couldn't have free access to collectivised firearms, to defend themselves if this unlikely eventuality ever did actually occur.

    And, just to be clear, I do not think that, in this situation, there would be any good argument against self-defence. If someone is running around waving a gun and telling everyone that they are now slaves, then I think in the spirit of the revolution that the people should have no compunction in killing them.

    After all, your hypothetical agitator is a statist, and it is the cause of the revolution to clean the world of their taint, if you'll forgive me the aggressively grandiose language.
    """

    menu:

        "Okay, so you give everyone rifles. But what happens when the 'trouble maker' gets their hands on one of those new gatling guns?":
            $c=34

        "What if the 'trouble maker' were to form a posse? True, the rest of the population could still just shoot them, but the risk of death would be much higher.":
            $c=43

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But your method of dealing with less violent 'trouble makers' is still to deny them 'resources', by which you mean food, don't you? So they can't be imprisoned but they can be starved to death. I'm sorry but I find that much more morally repugnant.":
            $game.butcher.zeal += 1
            $c=37

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But that still leaves the less violent ones, who, in effect, only have the choice between conforming or leaving. In other words, if someone is a troublemaker, the way your society deals with them is to just send them off to be someone else's problem.":
            $game.butcher.zeal += 1
            $c=38

        "Giving everyone a gun doesn't sit quite right with me, but I do agree, it would solve the problem. Fine Mik, consider me convinced, about collectivist anarchism at least.":
            $game.butcher.zeal += 2
            $game.butcher.like += 4
            $c=41



if c==34:

    "Mik shrugs."

    butcher "Everyone has to sleep eventually."

    $game.butcher.resp -= 2

    menu:

        "What if they have accomplices?":
            $c=43

        "So that would leave a society where every individual has to live in constant fear that their neighbours may try to kill them and their only defence would be if they kill their neighbour first? That doesn't sound like Utopia to me.":
            $c=35

        "Okay, fair point. Fine Mik, consider me convinced, about collectivist anarchism at least.":
            $game.butcher.zeal += 2
            $game.butcher.like += 2
            $c=41



if c==35:

    "Mik rolls their eyes and lets out a long, deep sigh."

    butcher """

    What part of 'fringe' do you not understand? The people will not live in 'constant fear' because they will know that they will be safe. Only very specific people would still think the way you are suggesting after the revolution. In small communities, how many of them would be able to remain hidden for long?

    I am not saying that there will be no instances of what you describe. I am merely saying that they will be so incredibly rare that 'constant fear' is such an overstatement as to be actually laughable.

    You do not see us all cowering under tables for fear that an earthquake will strike at any moment, and yet that would be more reasonable than the people of the post-revolution utopia crying themselves to sleep at night over the thought that the little old woman down the road might try to instigate a violent martial state.
    """

    $game.butcher.resp -= 1

    menu:

        "I think you're being naive Mik. Everything that you've said would make logical sense, but you've missed two important factors. Firstly, people aren't fully rational. If we were, we never would have got taken in by statist propaganda in the first place. And secondly, it is part of human nature to want to have more and be better than others. Evolution tell us that competition is part of who we are. What you say is logical if all people want is basic necessities and security, but that's not all people want. They want glory, power and many just want to dominate. You can't wave these problems away, because for many more people than you'd like to admit, power is something that they want in and of itself.":
            $game.butcher.zeal -= 2
            $c=36

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But your method of dealing with less violent 'trouble makers' is still to deny them 'resources', by which you mean food, don't you? So they can't be imprisoned but they can be starved to death. I'm sorry but I find that much more morally repugnant.":
            $game.butcher.zeal += 1
            $c=37

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But that still leaves the less violent ones, who, in effect, only have the choice between conforming or leaving. In other words, if someone is a troublemaker, the way your society deals with them is to just send them off to be someone else's problem.":
            $game.butcher.zeal += 1
            $c=38

        "You're right, my logic was messy. I'm convinced, anarchist collectivism is the future.":
            $game.butcher.zeal += 3
            $c=41



if c==36:

    if game.butcher.att > 12:
        $textinsert = "You're irresistibly sexy, but I'm afraid I'm the sociologist here."
    elif game.butcher.like > 24:
        $textinsert = "You're a nice person, {}, but nice doesn't mean bright.".format(game.player_name)
    else:
        $textinsert = ""

    "Mik holds your gaze for a long time."

    butcher "I presume you don't have any actual empirical evidence to back that up? I didn't think so. But before you say it, I don't have anything to prove you wrong, either."

    if game.butcher.resp > 25:
        
        "Mik lets out a long sigh, the air pushing itself out through a tired, constricted throat. Exhaustion and sadness, but no anger."

        butcher """

        I can't say that you're wrong, [game.player_name]. Everything I believe is based upon the knowledge that people do terrible things to each other, and they do it all out of nothing more than a desire for power. I believe, I really do believe, that the true culprit is the social system that we all, in one way or another, find ourselves trapped in.

        But I can't know I am right. Maybe some, you will never make me believe most, but enough, people really are born evil. Maybe, for some people, power really is valuable in and of itself.

        I don't know. But I have to believe it's not true. There are some things like that, aren't there? I knew someone once, well, knew of someone, I didn't move in those bourgeois academic circles, but I heard about a person who 'figured out' that free will is an illusion. Ended up killing himself.

        I think this is more important than that. Because if I'm wrong, and you're right, then we're doomed, as a species we're doomed. We're just going to keep finding better and better ways to kill and enslave each other until we finally just end it all.

        If I'm right, then the revolution is the answer. But if you're right, then there simply is no answer.

        I don't know. But humanity at least deserves to be given that chance.

        Right?

        To be honest with you [game.player_name], and however coy I like to play it I always do try to be honest, I don't know. I will think and reflect.

        I won't sleep tonight [game.player_name]. So knowing that I'll be up all night going over this, distract me with something else instead for now.
        """

        $game.butcher.like -= 4
        $game.butcher.zeal -= 5

    
    else:
        
        "Mik lets out a long sigh."

        butcher """

        No, no I have to believe you're wrong. I've seen deeper into the hearts of the people than you have, and I've certainly spent more time thinking about what I've seen there.

        I'm sorry to say this, but I know what I'm talking about more than you do. [textinsert]

        Of course it's a gamble. But I think it's a gamble I'm just going to have to take. If I'm wrong, and you're right, then we're doomed, as a species we're doomed. We're just going to keep finding better and better ways to kill and enslave each other until we finally just end it all.

        If I'm right, then the revolution is the answer. If I'm wrong, then everything is meaningless anyway and we might as well give the revolution a crack.

        Right?

        I'll think about it, [game.player_name]. But I don't think you're right. I think it is naive of you to think I am naive, [game.player_name]. At least about this.

        So that's that [game.player_name]. What else do you have to throw at me.
        """

        $game.butcher.like -= 8
        if game.playerbackground = "trader":
            $game.butcher.zeal -= 3
        else:
            $game.butcher.zeal -= 2

    menu:

        "It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream that no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==37:

    "Mik blinks, and in the brief moment after they open their eyes, you see a softness you have rarely seen. A pain, a flash of regret, an acknowledgement of both your and their humanity. But a moment later, it has gone, disappeared behind a hard mask of idealism."

    butcher """

    Morally repugnant? I won't try to convince you to not see it that way.

    But if the ideal of the people is not protected, and protected in a way that is compatible with it, then all of humanity will fall back into slavery. It does not matter in what way or for what reason, anyone who acts against the will of the people is attacking the equality and liberty of all in their community.

    We have talked before about both the universality of the ideal of the people, and the necessity of destruction within the revolution. The only reason I can think of for someone standing against the will of the people would be residual reactionary thinking.

    Under which circumstances, given the necessary nature of the revolution, I think reduced access to resources, yes, including food, would be a remarkably kind way to treat the reactionary.

    And I'm not leaving behind those who couldn't 'understand' the logic. I'm not denying that everything we have talked about is complicated. But people learn from what is around them. And if all that is around them is good, then they should only learn good. And for any individual who wishes to strive further, their logic will bring them to the same conclusion.

    In other words, words I should have said upfront, the people you are talking about won't exist. Those who can't grasp the logic will simply learn from example, and those who won't must be reactionaries, because who else would reject utopia?
    """

    $game.butcher.like += 4
    $game.butcher.zeal -= 1

    menu:

        "I think you're being naive Mik. Everything that you've said would make logical sense, but you've missed two important factors. Firstly, people aren't fully rational. If we were, we never would have got taken in by statist propaganda in the first place. And secondly, it is part of human nature to want to have more and be better than others. Evolution tell us that competition is part of who we are. What you say is logical if all people want is basic necessities and security, but that's not all people want. They want glory, power, and many just want to dominate. You can't wave these problems away because for many more people than you'd like to admit, control over other people is something that they want in and of itself.":
            $c=36

        "Let's move on. It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $game.butcher.zeal += 5
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream that no amount of violent revolution could make real.":
            $c=45

        "It's an unpleasant thing to do, but I do think your logic is sound: the only people who would cause problems would be those sadly still under the effects of statism and capitalism. In other words Mik, when it comes to collectivist anarchism, you've convinced me.":
            $game.butcher.zeal += 3
            $c=41
    jump reevaluatebutcher8



if c==38:

    "Mik nods thoughtfully."

    butcher """

    A fair point, if a practical one.

    Yes, it's not a brutally efficient solution. But it does have some elegant features. The first is the difficulty of the transit. I do not imagine that most communities will be too far from each other, although of course that is a wild guess, but even so, travelling from one to the other would give the 'trouble-maker' plenty of time to, as my mother always said, \"think about what they've done.\"

    It sounds trite, and maybe it is, but I would imagine that travelling alone and in exile would make anyone reflect on their behaviour.

    You may be unconvinced, and I don't blame you. Maybe the other advantage will convince you. Different communities will be made up of different people, people with different needs if their environments are different enough.

    If someone does not fit in with one group of people, they may very well fit in better with another. Just because it's a lesson most children learn, often the hard way, on the first occasions they are allowed to 'go out and play with the other children', doesn't mean it's not a valuable piece of sociology.

    Liberty means the expression of self. And utopia or no utopia, some people are simply not going to get along with each other. It's an unfortunate truth, but change the setting and the people, and someone who may have been a troublemaker once may become a fully productive member of the community.

    You may still be unconvinced, but I think the issue is more pressing for the traveller, not the communities they would travel through. No community would have an obligation to provide anything to someone who refuses to engage productively with the community, so there would be nothing wasted when the communities refuse to help the traveller.

    Either they would settle down, or they would keep drifting, receiving nothing from anybody who did not give away freely, until they died. Either way, they will have made their free choice, and I can't see that that choice would have harmed anyone else, one way or another.

    An interesting point to consider, but not a knockdown argument I'm afraid.
    """

    $game.butcher.resp += 2
    if game.butcher.resp > 25:
        $game.butcher.zeal -= 1
    
    menu:

        "I still think it is morally repugnant. Yes, these people would have the freedom to travel, but on a larger scale, your solution is still just to deny them 'resources', by which you mean food, don't you? Which means that, even if they travel, their options are really between conforming with some group before starving to death, or just simply starving to death.":
            $c=37

        "Your logic is sound Mik, the only people wanderers would harm are themselves, and they will do so as part of their own free choice. When it comes to collectivist anarchism, then, you've convinced me.":
            $game.butcher.zeal += 3
            $c=41

        "Let's move on. It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $game.butcher.zeal += 5
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream that no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==39:

    "Mik raises an eyebrow."

    butcher """

    I am surprised that satisfied you, I'm almost disappointed that it did, but I suppose efficiency has it's place.

    Is there anything else you have more questions about?
    """

    $game.butcher.resp -= 2
    $game.butcher.zeal += 1

    menu:

        "It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==40:

    if game.butcher.romance == True:
        $textinsert = "Maybe I should save my boasting for all the other things I'm exceptionally good at, eh?"
    else:
        $textinsert = "Oh well, I have more important things to work on."


    butcher """

    Ah wonderful. For a brief moment I thought you might have me there [game.player_name], but I think I recovered admirably.

    Too immodest? Perhaps. [textinsert]

    Besides, we were engaged in a quasi-academic exercise. Do you have any other points you wish to raise?
    """

    $game.butcher.zeal += 2

    menu:

        "It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==41:

    if game.butcher.romance == True:
        $textinsert = "Maybe if you took all my clothes off and ravished me it might knock something loose."
    else:
        $textinsert = ""

    butcher """

    Another minor victory for the revolution. How splendid.

    I am actually pleased [game.player_name], it's just that years of soot and dust clogged up my emotion glands and now it's difficult to give off anything but cynicism.

    A coping strategy, you understand. [textinsert]

    But we should return to our quasi-academic exercise. Do you have any other points you wish to raise?
    """

    $game.butcher.zeal += 2

    menu:

        "It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream that no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==42:

    "Mik aggressively rolls their eyes and lets out something on the border between a sigh and a growl."

    butcher "Ah yes, \"you're wrong, '{i}because{/i}'\". The height of all intellectual arguments. Thank you so much my dear [game.player_name], I've learnt so much from you."

    "Mik shakes their head."

    butcher "Fine, I don't have the energy to push you. Let's just move on. What else did you want to chicken out of pressing me on?"

    $game.butcher.resp -= 8
    if game.butcher.resp > 25:
        $game.butcher.zeal -= 1
    else:
        $game.butcher.zeal += 1

    menu:

        "It could be argued that competition drives progress. It could be argued that it's how evolution works, and it's how human ingenuity works." if Mik8Capitalism == False:
            $c=2

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==43:

    "Mik rolls their eyes and lets out a long, deep sigh."

    butcher """

    What part of 'fringe' do you not understand? Only very specific people would still think the way you are suggesting after the revolution, because it's just not logical. They would have to be illogically power-hungry, willing to take enormous personal, physical risks and be completely morally bankrupt, and you are expecting to find posses of these people within small communities?

    No [game.player_name], that's not something that anyone would have to worry about, because it's simply something that couldn't happen.
    """

    $game.butcher.resp -= 3

    menu:

        "I think you're being naive Mik. Everything that you've said would make logical sense, but you've missed two important factors. Firstly, people aren't fully rational. If we were, we never would have got taken in by statist propaganda in the first place. And secondly, it is part of human nature to want to have more and be better than others. Evolution tell us that competition is part of who we are. What you say is logical if all people want is basic necessities and security, but that's not all people want. They want glory, power, and many just want to dominate. You can't wave these problems away because for many more people than you'd like to admit, control over other people is something that they want in and of itself.":
            $game.butcher.zeal -= 2
            $c=36

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But your method of dealing with less violent 'trouble makers' is still to deny them 'resources', by which you mean food, don't you? So they can't be imprisoned but they can be starved to death. I'm sorry but I find that much more morally repugnant.":
            $game.butcher.zeal += 1
            $c=37

        "You're right, easy access to the tools of self-defence probably would deal with the most violent 'trouble makers'. But that still leaves the less violent ones, who, in effect, only have the choice between conforming or leaving. In other words, if someone is a troublemaker, the way your society deals with them is to just send them off to be someone else's problem.":
            $game.butcher.zeal += 1
            $c=38

        "You're right, my logic was messy. I'm convinced, anarchist collectivism is the future.":
            $game.butcher.zeal += 3
            $c=41
    jump reevaluatebutcher8



if c==44:

    if game.butcher.resp > 25:
        $textinsert = "You'll make a very good ambassador for the cause."
    elif game.butcher.like > 28:
        $textinsert = "You've got a good heart {}. You'll fit in perfectly, when all is said and done.".format(game.player_name)
    else:
        $textinsert = ""
    
    if game.butcher.romance = True:
        $textinsert2 = "But really, I couldn't manage that right now. I'm far too horny for it. Fancy doing something to help fix that problem?"
    elif game.butcher.like > 28:
        $textinsert2 = "But right now I'm parched. Fancy grabbing a drink?"
    else:
        $textinsert2 = "I don't see any reason to delay, so I'll get to that now.  This was a good conversation {}. I look forward to marching by your side.".format(game.player_name)

    "Mik nods slowly, and as they do, a smile of pure joy breaks through their stoic, cynical defences."

    butcher """

    You didn't half make me work for that.

    Well, I guess that's it then. Your education is complete. You've been very patient with me [game.player_name], but it's paid off.

    Welcome to the revolution. [textinsert]

    There's not really anything else to say. I have some more things to consider, both theoretical and practical, before any of us take the next step.

    [textinsert2]
    """
    $game.butcher.like += 4

    if game.butcher.resp > 25 or game.butcher.like > 28:
        $game.butcher.zeal += 3
    else:
        $game.butcher.zeal += 2
    
    return



if c==45:
    
    if game.butcher.like > 28:
        $textinsert = "I must say, I am a little surprised. Somewhere deep in there, I think I've seen glimmers of a good person. It's a shame to see you give up on that."
    elif game.butcher.resp > 25:
        $textinsert = "You'll be a formidable adversary {}.".format(game.player_name)
    else:
        $textinsert = "Not that I'm particularly surprised."

    """

    Mik slumps to the floor.

    Literally.

    Their voice, muffled by the floorboards, is slurred with tired cynicism.
    """

    butcher """

    Well, if I remember correctly, wasn't the whole point of this exercise to teach you to be a good little statist?

    In which case congratulations, you pass. Not with honours though, people who can't grasp simple logic don't get honours.
    """

    "Mik props themself up on their elbows and looks up at you."

    butcher """

    [textinsert]

    I suppose this is it then. No more lectures.
    """ 

    if game.butcher.romance == True:
    
        butcher """
        
        Oh, but I could really use a hate fuck right now.  

        Any chance?
        """
        
    else:

        butcher """
        
        The end of an era really, eh? A long and completely fucking pointless era.

        I am sure I will see you around.

        But for now, bye.
        """

    $game.butcher.like -= 2

    if game.butcher.resp > 25 or game.butcher.like > 28:
        $game.butcher.zeal -= 3
    else:
        $game.butcher.zeal -= 2

    return



if c==46:

    butcher """

    Ah, good to hear it. I didn't want to spend too much longer on that topic anyway, it was always one of my least favourite bourgeois talking points.

    I do hope the next thing you have to throw at me is better.
    """

    $game.butcher.zeal += 2

    menu:

        "You've never actually explained exactly how anarchist collectivism works." if Mik8AnarchoColect == False:
            $c=20

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==47:

    "Mik snarls, but nods."

    butcher """

    You should know I don't like letting things go without a fight. But in this case I think you're probably right, I've always hated this bourgeois talking point anyway. We'll probably both be dead soon, let's not waste our time on this drivel.

    Give me something else to get my teeth into.
    """

    $game.butcher.zeal -= 1

    menu:

        "You've never actually explained exactly how anarchist collectivism works." if Mik8AnarchoCapitalism == False:
            $c=20

        "That's all I wanted to say. I'm glad to see that you're really thinking everything through, but I do believe that revolution is the answer.":
            $c=44

        "I've said everything I wanted to say, and I hope that you have too. And after all this, I'm not convinced. There are problems with your theories Mik, your 'utopia' is a dream no amount of violent revolution could make real.":
            $c=45
    jump reevaluatebutcher8



if c==48:

    "Mik nods and shrugs."

    butcher "Alright, if you want to make it that easy I'm not going to stop you. But you must have something else?"

    $game.butcher.zeal += 1

    menu:

        "Your comparison between war and competition is wrong. Capitalism is good, in part, precisely because it produces progress at a much lower cost than war would. The argument is not that progress justifies all, but that if we want progress, capitalism is the least harmful of the most effective ways of getting it." if Mik8CapNotWar == False:
            $c=12

        "But if everyone is living in the perfect utopia which no-one would have any complaints about, then why would anyone feel the need to innovate at all? Wouldn't life already be perfect?" if Mik8Utopia == False:
            $c=13

        "Okay, you've answered my concerns about innovation. We can move on.":
            $c=46

        "You haven't convinced me Mik, but I can't see the point of either of us wasting any more of our time going around in circles on this. You're clearly not going to listen to my reason and your arguments aren't going to change my mind. Let's move on.":
            $c=47
    jump reevaluatebutcher8








return
