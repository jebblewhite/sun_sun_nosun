label butcherscene4: 

$Mik4Everyone = False
$Mik4Hobbes = False
$Mik4Labour = False
$Mik4Hobbes = False

"Mik barely lets the door close behind you before, smiling like a shark, they begin."

butcher """

I hope that, by now, I've gotten across the basic notion that states are a bad idea. Don't tell me whether I have, if you said that I haven't I'd be too depressed about, either your intelligence or my ability to speak, to continue.

Well, to put all my anarchist waffling simply: no social structure organised from the top down will ever work. This is because, and I quote my friend again:

\"Revolutionary Socialists believe that there is much more of practical reason and intelligence in the instinctive aspirations and real needs of the masses of people than in the profound minds of all the learned doctors and self appointed tutors of humanity…

\"… who, having before them the sorry examples of so many abortive attempts to make humanity happy, still intend to keep on working in the same direction.\"

You can see from whom I learnt to argue, can't you? I aspire to great heights. But that is irrelevant. The point is that not once has a model that started from theory, or constitution or the ideas of one man - and yes I am aware I said 'man' - led to a just, equal and free society.

However well intentioned, plans will inevitably turn into tools of the oppressor for all the reasons I have given for why states always become oppressive. They are, quite literally, the will of the few imposed on the lives of the many.

All that lofty, intellectual ideas do is determine {i}negative{/i} conditions. That is how I can sit here and tell you why we need to bring down the state and the institution of private property. But what of the {i}positive{/i} side of the argument, what a post-revolutionary society would actually look like?

That is where the ideal of the people comes in. Again, I'll let my friend's considered words - and trust me that they are considered, I was with him when he went over them again and again to get them right, so much so that I didn't even plan on learning them off by heart but hearing it so often gave me no other choice - anyway, I'll let them do the talking:

\"This ideal of course appears to the people as signifying first of all the end of want, the end of poverty, and the full satisfaction of all material needs by means of collective labour, equal and obligatory for all…

\"… then the end of domination and the free organization of the people's lives in accordance with their needs - not from the top down, as we have it in the state, but from the bottom up, an organisation formed by the people themselves, apart from all governments and parliaments, a free union of associations of agricultural and factory workers.\"

I'll give you that one; for the amount that he worked on it, it's dry as sandpaper. Maybe I should have given you:

\"such an ideal arises from the very depths of popular life. It is the product of the people's historical experiences, of their strivings, sufferings, protests, and struggle, and at the same time it is a graphic expression, as it were, always simple and comprehensible to all, of their real demands and hopes.\"

Yes, the second one is better, even if it is less concrete. The ideal of the people is the instinctual expression of the demands, hopes and aspirations of all the working people of the world.

What will this look like? I can't tell you, because the only way it can be expressed is through a society constructed from the bottom up, an ideal that arises from the natural, voluntary grouping of people, which is only possible in a world where the scourge of statists and bourgeois has been eradicated.

Again, and I promise I'll stop quoting him after this, but to round this off with one last little bit from my friend:

\"Give the people a broad human existence, and they will amaze you with the profound rationality of their ideas.\"
"""

$Mik4First = True

$c=2


label reevaluatebutcher4:
if c==2:

    menu:

        "Wait, if this is really the ideal of the people, the one that will, once recognised, lead to a society that is so perfect it will never again rise up in revolution, why is it not already in place? Why are there people who would fight against it if it is perfect?" if Mik4Everyone == False:
            $c=3

        "Wait, you said that you, or your friend, can't say anything concrete about what the ideal of the people will look like, and yet also say that labour will be obligatory for all. Isn't that a concrete claim?"  if Mik4Labour == False:
            $c=4

        "Wait, do you have any actual evidence that it will work, or that every worker really does share the same ideal?"  if Mik4Hobbes == False:
            $c=10

        "Wait, you expect the people to rule themselves intelligently? That won't work." if Mik4Ratinoal == False:
            $c=11

        "I understand perfectly. The only just society is one that the people, free and equal, make themselves." if Mik4First == True:
            $c=15
            
        "Okay, I understand enough, let's move on." if Mik4First == False:
            $c=15

        "I'm not convinced Mik, but let's just move on." if Mik4First == False:
            $c=16

    $Mik4First = False



if c==3:

    butcher """

    I see the confusion. You are wondering - if the ideal of the people is truly so great and so universal - why do the bourgeois and the statists fight against it? Why do they exist at all?

    They exist because historically they have always existed. Well, maybe not statists and bourgeois, definitely not the bourgeoisie, but there have always been oppressors and there have always been the oppressed. I'm not a historian, so I can't claim to know who were the first, but if I were to guess, I would say that it probably all started with patriarchy.

    The system of oppression has, through political revolutions, changed, but the people are still indoctrinated into accepting the concept of oppression.

    And the economic argument is simple: oppressors have more material goods than they would if they were not oppressors. Simple as.

    Now the obvious next step is for you to bounce up and down on the balls of your feet and shout: 'Ah-ha! You are wrong Mik, because there have not always been people, so at some point some person must have chosen to be an oppressors, instead of taking the option of equitable, liberal anarchy. There must have been a first oppressor!'

    """

    if Mik4Hobbes == True:

        butcher """

        Firstly, I've said that already in this conversation, so don't let that theoretical strawman that I set up for you get too big headed.

        But it would be right to point that out. But consider the time in which that happened. I am not saying that instigating the will of the people would have been impossible when we were still fighting tigers with blunt stones, but that poor sod who first decided to subjugate his woman didn't have a number of the advantages that we have today.
    
        """

    else:

        butcher """

        And you would be right to point that out. But consider the time in which that happened. I am not saying that instigating the will of the people would have been impossible when we were still fighting tigers with blunt stones, but that poor sod who first decided to subjugate his woman didn't have a number of the advantages that we have today.

        """

    butcher """

    For starters he didn't have science or technology. If you don't know that putting those little hard bits in the middle of your apple into the ground could get you more apples and no one else on earth knew it either, the struggle just to survive as a species would have been much greater.

    Those few extra mouthfuls you could steal out of someone else's mouth may have actually made the difference between life and death. Not so any more, of course. Our oppressors take the skin off our bones and use it to fund their seventh golden chandelier.

    But most importantly, the first oppressors wouldn't have known the social facts we know today. I can confidently tell you that collectivisation is better than oppression because I have experienced oppression and studied its systems. Early man, yes almost certainly 'man', wouldn't have had those advantages.

    Not to mention the thousands of years of philosophical, political and economic thought and writings.

    Or even the leisure time to think about any of these things himself.

    I am not simply arguing for anarchy, [game.player_name]. I am arguing for socialist anarchy, an anarchy of liberty and equality. I am arguing for the expression of the will of the people. And that is something that has to be created and nurtured.

    Our species has only had one chance to create that before the scourge of oppression took hold and that was before we had the benefits of agriculture, tools or possibly even language.

    I don't think it was a surprise that humanity missed that opportunity.

    And after that first seed was planted the systems of oppression were off to the races. And they weren't going to let themselves die without a fight. But I have said all that already.

    No doubt you have other questions?
    """

    $game.butcher.resp += 2
    $Mik4Everyone = True

    $c=2
    jump reevaluatebutcher4



if c==4:

    "Mik smiles at you, their face held at an angle to yours."

    butcher """

    I'll concede that one [game.player_name]. Maybe there are certain things that I could say about it.

    No, that's unfair. There are plenty of things I could say about it.

    But they are inferences, not commandments.

    When my friend says 'obligatory' with regard to collective labour, he is not prescribing. He is merely following the facts.

    Work must be done in order to keep humans alive. At the very least, we all must eat.

    So how can an individual survive if they do not work? By taking the fruits of someone else's labour. By creating a system of inequality.

    But the ideal of the people calls for equality. So we work backwards and find that it must be impossible to have an equal society where people are not obliged to work.

    My friend and I are not prescribing. We are merely reasoning. And that is the difference.
    """

    $game.butcher.resp += 4
    $Mik4Labour = True

    menu:

        "Okay, that makes sense.":
            $c=5

        "But what about those who can't work? Like the elderly or the disabled?":
            $c=6



if c==5:

    butcher """

    Good. And very good observation.

    Got any others?
    """

    $game.butcher.like += 1

    $c=2
    jump reevaluatebutcher4



if c==6:

    "Mik raises one eyebrow, almost as if they are surprised."

    butcher """

    Well those who can work will do what they can, I imagine. But that is just dodging the question, isn't it?

    I must admit, this isn't something anyone has mentioned before…
    """

    "Mik takes a moment to ponder, before eventually shrugging their shoulders."

    butcher """

    Well done, you have found a loophole. But you don't disprove the logic. Well you do, but you show that the argument was too simple.

    We are human beings. I cannot imagine that the ideal of the people would allow the elderly and the disabled to die because they cannot work. So we would assist them.

    True, it's not technically equal. But I think it is still just. After all, it would be the people who are choosing to help them. It's a very far cry from oppression.
    """

    $game.butcher.resp += 4

    menu:

        "So you'd place the wellbeing of those who can't work in the hands of charity?":
            $c=7

        "I understand, I agree that it will work in practice, even if it is a little logical loophole.":
            $c=5

    jump reevaluatebutcher4



if c==7:

    "Mik snorts, but there is a glint of respect in their eyes, beside the panic."

    butcher """

    It's not charity [game.player_name]. It's basic human decency.

    Bring me an anarchist, no, bring me any socialist who doesn't care about the welfare of those who cannot help themselves and I will show you a fake socialist.
    """

    $game.butcher.resp += 1

    menu:

        "But you aren't just talking about socialists, or anarchists. You can't rely on the character of anarchists and socialists, or cite any examples of their historical actions, because you'd just be talking about those who already believe. But you're talking about total revolution. You have to consider everyone. And I don't think that you can prove that everyone is as kind and caring as those who have already chosen to be socialists or anarchists. Maybe you can persuade them to your philosophy, but you can't expect them to be as devoted as you and the other early adopters. You can't rely on everyone being as good as you are.":
            $c=9

        "If it's human nature to help the disabled and elderly, then why isn't charity enough to keep them all safe and healthy now?":
            $c=8

        "I understand. After the revolution and the institution of the ideal of the people, we will all be decent.":
            $c=5
    
    jump reevaluatebutcher4



if c==8:

    butcher """

    Because they've been corrupted by the system.

    Those who have enough won't give it because the systems of oppression that they maintain have trained them to hoard as much stolen wealth as they can. While those proletarians who do care don't have anything to give.

    'Charity' is voluntary. But there shouldn't be anything voluntary about helping another human being. It is an instinct.

    But the systems of oppression have destroyed that instinct. Only social revolution can bring it back.
    """

    $game.butcher.resp -= 1

    menu:

        "This all relies on the existence of a universal charitable instinct, but can you prove that such an instinct exists? Do you have any facts? Because without facts, isn't it simpler to say that the instinct just doesn't exist and there are many people who are just inherently less caring than you? Where is your proof that it's not that many people just naturally don't care?":
            $c=9

        "You're right. Humans are fundamentally good and once we have destroyed the systems subverting that we will be free again to express our nature.":
            $c=5

    jump reevaluatebutcher4



if c==9:

    "There is a long pause while Mik looks down at the counter top."

    butcher """

    I don't have facts for why you're wrong [game.player_name].

    I know I should.

    I don't believe in faith [game.player_name]. I don't think that relying on faith is ever healthy.

    But…
    """

    "There is another long pause, Mik still not meeting your gaze."

    butcher """

    It has to be true [game.player_name], that once we have liberated the world from the chains of oppression, that the ideal of the people will be good and will be universal.

    It has to be. Because if it's not, then what hope do any of us have, under any system?

    And I hate to fall back on this. I really do. But even if I'm wrong, then that doesn't mean that what I'm suggesting would be worse than what we have right now.

    Even if it wouldn't be perfect.

    Which I believe it will be. It has to be.

    I will think of some way to prove it. I will make it my next mission. But for now, do you have anything else you wanted to challenge me with?
    """

    $game.butcher.like -= 2
    $game.butcher.resp += 4

    $c=2

    jump reevaluatebutcher4



if c==10:

    butcher """

    The existence of a universal people's ideal shouldn't be controversial. And I'll prove it using bourgeois arguments.

    You see, I only actually need to start with one thing. 'Humans want to live.' Now yes, we could tie ourselves up in pointless knots about the brave souls who sacrifice themselves for their country or their loves, but one must still live long enough to sacrifice oneself in the desired way.

    Fine. I'll change what I said. Can we agree that 'no human wants to die pointlessly', or maybe 'Humans either want to live or die for reasons of their choosing'. It's a horrible fucking mouthful, but I don't think you could reasonably disagree.

    And yes, it does cover suicide. You can't commit suicide without choosing to do so. It's in the literal definition of the word.

    So we already have a baseline, something that I think every human who has ever lived can agree on.

    Now, picture the kind of anarchy you statists like to imagine when someone brings up the word. Everyone running around with sharp sticks, nothing to stop them sticking them in each other. Life as 'nasty, brutish and short', eh?

    Pack all that hay in, I want you imagining the plump and juicy straw man all good oppressors like to concoct when forced to consider what life might be like without their chains.

    And now let me tell you why that would never happen.

    That kind of 'nasty, brutish and short' is the last thing any human would want, because as we've already agreed, no-one wants the kind of life where it's very possible to wake up one morning to find a pointed stick jammed through their jugular.

    So it follows from people's natural distaste for random death that they would join together in societies and agree that, within those groups, none of them are allowed to kill each other randomly.

    But that's not all, is it? Because if that agreement is to stand, it has to be understood that agreements stand. So the binding nature of promises follows from a desire for society, since without it the benefits of society could not be relied upon.

    There's a bushel of other facts that follow logically from the desire for peaceful society too: gratitude, generosity, forgiveness and kindness all follow from wanting to live in harmony. Because if everyone values their lives, they will value their peaceful society, and if they value their peaceful society, they will work to keep it whole, harmonious and peaceful.

    Gods I sound like a fucking cleric.

    Anyhow, from these premises follows another thing, a very important thing. Equality. It should be clear that such a society is formed from agreement and civility. Agreement because every member of the society is there by their own contract, and civility because each member stays for as long as the society is to their advantage.

    In other words, the society only exists because each member chooses for it to exist. Now, again, let us accept the statist and bourgeois ideal of selfishness.

    I have already shown that the power to form such a society rests equally in the hands of all of its members. Now if we accept selfishness, we will see that no member would be willing to start from this base of equality and then allow another individual to take more power in the society than they take themselves.

    So a group of selfish people could only agree to form a society under equal terms. And unselfish people would do the same, because they would know that equality is the most fair.

    So we must accept equality. Which then entails at least some form of collectivism, because not everything can be equally divided, and must then instead be shared.

    Those, in very, very brief, are what I have heard called the 'laws of nature'. Which is a fucking awful name. But then the man who conceived them was an idiot.

    Yes, I am forced to admit, I didn't think of all that myself. It's from an old, long dead pet philosopher of one of the Kingdom's kings, I forget which one.

    But while I didn't think of it, I also didn't make the mistake that he made and add on the pointless addendum that no contract is enforceable without the threat of violence against anyone who breaks the contract. Despite the fact that his own logical progression gives a perfectly sound reason on its own for why contracts must be binding.

    Another reason that they're not 'laws of nature' is because they've never been enforced. Everything I said is true, but another possibility follows from a desire to get away from that 'nasty, brutish and short' existence.

    Slavery.

    And that's the path that {i}was{/i} taken. Thomas, that was the man's name by the way, figured out that whole system and then tried to cram oppression, awkwardly and erroneously, into it as a way of justifying his king's rule.

    But he's wrong because his king didn't inherit the world that was built by the 'laws of nature'. He inherited the world that was built from taking the other path, the path of slavery and oppression. Societies built up by individuals for protection from others, not by mutual agreement and civility, but by enslaving those others before they could enslave them.

    But I've gone off track. You asked for evidence. True, I haven't given you empirical facts. But I've done you one better. I've given you air tight logic. Air tight logic lifted straight from the mouth of a rabid monarchist, so you can't even accuse it of bias.

    Ah, I've been waiting to give that rant for a long time.

    So, what else dare you throw at me?
    """

    $game.butcher.resp += 2
    $Mik4Hobbes = True

    $c=2

    jump reevaluatebutcher4



if c==11:

    butcher "Ah yes. 'No it won't.' A sterling argument. Specifics, [game.player_name]. Why won't it work?"

    $Mik4Rational = True
    
    menu:

        "Because the people aren't 'profoundly rational'. That's why states exist, to make the decisions that most people aren't intelligent enough to make on their own.":
            $c=12

        "Because there is no one simple collection of knowledge that is required to run a country. You need experts in a wide variety of fields. You shouldn't expect everyone to understand the nuances of economics or geography or sociology, never mind all of them. We need experts to guide us.":
            $c=13

        "Because not everyone wants to spend their lives figuring out the problems of politics. Self-organised society may be good for people like you, who really care about this sort of thing, but many, many people just want that to be all managed for them so they can live their lives in peace.":
            $c=14



if c==12:

    "Mik sighs deeply."

    butcher "I'll deal with the second sentence first like this."

    "Mik cocks their head at you and sardonically drawls:"

    butcher """

    Really?

    How much of my life have I wasted telling you why the state exists? And you come out with that. That's why you think the state exists?

    Wow.
    """

    "Mik straightens up, tucking their blood-stained apron into their belt as if it were a crisp, snow-white silk shirt."

    butcher """

    As for the first sentence:

    I don't have any proof that all people are not idiots. Just as you don't have any proof that they're not.

    But I will say two things: I've lived in Alexisgrad. I've met senators, and plenty of want-to-be senators. And I can tell you that one thing does indeed unite them, but it's not intelligence, oh no. It's nothing more sophisticated than greed. Greed for power that is. Money is just power by its newer, trendier bourgeois name.

    And secondly, although you might be the kind of statist who doesn't give a shit about this, if the people are so thick, then why are we so proud of the fact that our Republic is a democracy? If the people are so stupid, then surely the King of kingdom has the right idea.

    But then again, there are people like you who make arguments like that. So maybe you are right, maybe people are just stupid.

    In which case all is lost and why should we bother with any of it.

    Rhetorical. Don't answer. Just move on, give me your next demeaning, pointless argument.
    """

    $game.butcher.resp += 4
    $game.butcher.like += 4

    $c=2

    jump reevaluatebutcher4



if c==13:

    if Mik4Everyone == True or Mik4Labour == True or Mik4Hobbes == True:
        $textinsert = "we've already gone off subject enough"
    else:
        $textinsert = "I sense you have more questions about that"

    "Mik nods in a way that, bizarrely, looks like they are agreeing."

    butcher """

    I agree with everything you just said.

    It is just the sentiment that we disagree on, I wager.

    I agree that we need experts. And I agree that we will need their guidance. But I doubt that's what you meant when you said 'guide us'. What I believe you meant to say was 'lead us', in the sense of 'rule us'. And that is where is disagree.

    Either way…
    """

    "Mik taps the blunt edge of a bloody knife against their chin."

    butcher """

    No, this is worth getting into in full, but some other time. We were going to talk about the people's ideal today, and [textinsert] so we'll table this for now.

    So just know that I don't disagree. But I don't agree either.
    """

    $game.butcher.resp += 2

    $c=2

    jump reevaluatebutcher4



if c==14:

    "Mik taps the blunt edge of a bloody knife against their chin, their face troubled."

    butcher """

    Well people are interested in themselves and their own well-being. Lives in a small commune should be simple enough that no individual would have to put in much time and effort to be fully engaged.

    I do take your point though. In an ideal world of liberty, everyone would be free to care as little about the logistics of governance as possible.

    Still, I don't believe it is too steep a price to pay. An inconvenience for the less politically inclined shouldn't get in the way of a vastly increased standard of living for all.

    And besides, it is not like our Republic is much better. We live in a democracy in which we are told it is our duty to vote. And if it is our duty to vote, it is our duty to stay informed about not just the logistics of governing a much, much, much larger and more complex system than any local anarchist commune would be, but also the tangled web of senate politics as well.

    Of course, most voters don't do that. But I think that's actually in support of my point, don't you think?

    But it is a good point. I'll have more of a think, maybe there is a solution, although as I said, I don't think that the problem is too large.

    Any other observations?
    """

    $game.butcher.resp += 4

    $c=2

    jump reevaluatebutcher4



if c==15:

    "Mik smiles and spreads their hands."

    $game.butcher.like += 2

    $c=17



if c==16:

    "Mik shakes their head."

    butcher "As boringly predictable as I had predicted you'd be. Still, I admire your commitment to conservatism."

    $game.butcher.like -= 4

    $c=17



if c==17:

    butcher """

    Luckily for you, that's all I had to say today. There's more to say, of course, about the exact nature of the collectivist anarchist utopia, but the ideal of the people is its true positive core, the other side of the coin from the negative premise of breaking the chains of oppression.

    The power will be given to the people by the shocking, revolutionary and unprecedented method of actually giving the power to the people. Not giving it to their representatives like in a democracy, or their heavenly appointed leader, like a Kingdom, or their party, like the communists would.

    All the power, equally shared by the people, who will, from the bottom up, create their own structures derived from their own ideals.

    We, as a race, have time and time and time again, throughout history, attempted to organise ideal societies from the top down, imposing rules and laws and guidelines, and it has not worked once. Because the ideal of the people, the only ideal that should ever matter, can only be expressed by the people, from the bottom up.

    That is how our utopia will be organised. By everyone and for all.

    It really doesn't sound like it should be revolutionary. It sounds like it should be common sense.

    So there. That's my 'propaganda'. I've shown you before what you're working for as the Alderman's little statist, and that's what you're working against.

    (if respect is above a certain threshold)[Although I must say, it looks like you're doing a bad job of it. Are you sure you're cut out to be an oppressor? wink](else)[And you seem to be doing a good job of that. Keep that boot on our throats, that's a good oppressor.]

    Now run along. Again I've wasted far too much of both of our time.

    Maybe next time we meet we can actually just chat.

    Won't that be novel?
    """

return
