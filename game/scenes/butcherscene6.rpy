label butcherscene6: 

$Mik6Tactics = False
$Mik6Friend = False
$Mik6Science = False
$Mik6Religion = False

"You almost trip over Mik, concealed as they are within a large clump of dying grass, as you make your way towards the forest. The only thing that stops you is a 'hey' from just below where you are about to place your foot."

butcher """

I am not sure if I should fault you for taking 'step on the downtrodden masses' too literally or praise you for taking the whole thing to new heights.

Either way, on a purely personal level I hope that you will find it in your heart to walk around me.

Oh, and just in case you think me strange, because there is no way that ship hasn't already sailed, I'm out here 'exercising'.

Yes, this is part of it. It's important to take regular breaks. It's not important that those breaks be significantly longer than each period of exercise, but better safe than sorry, don't you think?
"""

menu:

    "Why are you exercising?":
        $c=1

    "Mind if I join you down there?":
        $c=2

    "*Shake your head and go to move round them*.":
        $c=3

label reevaluatebutcher6:

if c==1:

    butcher "I presume it wouldn't surprise you if I told you it's for ideological reasons. When the revolution comes, if the revolution comes, I will bear arms just like everyone else."

    menu:

        "I thought you'd be leading from the back.":
            $c=4

        "Aren't you more of a 'stay at home and complain' type of revolutionary?":
            $c=5

        "So you'd actually take up arms, if it came to it?":
            $c=6



if c==2:

    butcher """

    Well of course that will get in the way of my strenuous regime, but I suppose I could spare a few minutes.

    After all, the psychological war must be won before the physical war. No point preparing for battle if that battle's not going to happen.

    And the gods know I wouldn't be exercising for any other reason.
    """

    $game.butcher.like += 2

    menu:

        "You're going to fight? I thought you'd be leading from the back.":
            $c=4

        "You're going to fight? Aren't you more of a 'stay at home and complain' type of revolutionary?":
            $c=5

        "So you'd actually take up arms, if it came to it?":
            $c=6



if c==3:

    "You move around Mik and head towards the forest, but you don't make it far before you are stopped by their voice."

    butcher "Of course, it would be much easier for me if the likes of you just didn't exercise either. That way when the bullets start flying we'll both be equally out of breath."

    $game.butcher.like -= 2

    menu:

        "You're exercising so you can fight? I thought you'd be leading from the back.":
            $c=4

        "You're exercising so you can fight? Aren't you more of a 'stay at home and complain' type of revolutionary?":
            $c=5

        "You're exercising so you can fight? So you'd actually take up arms, if it came to it?":
            $c=6



if c==4:

    "Mik pushes themself up into a sitting position."

    butcher """

    Ha.

    I can see why you'd think that. But revolutionary combat service will be just as obligatory and universal during the revolution as labour will be after it.
    """

    $game.butcher.resp += 1
    $game.butcher.att += 1

    $c=7



if c==5:

    "Mik pushes themself up into a sitting position and rolls their eyes."

    butcher """

    I can't decide whether you're exacerbating because you are right or whether you being exacerbating is just a constant trait.

    Either way, however much I'd like to 'stay at home and complain', however much that is my natural environment, my ideology won't allow it.

    Revolutionary combat service will be just as obligatory and universal during the revolution as labour will be after it.
    """

    $game.butcher.att += 2

    $c=7



if c==6:

    "Mik pushes themself up into a sitting position and shakes their head."

    butcher """

    Do you have so little faith in me that you believe I wouldn't actually stand up for what I believe in?

    Or do you just have so little faith in your own system that you cannot imagine anyone willingly killing and dying for theirs?

    Either way, yes, I would actually take up arms.

    Revolutionary combat service will be just as obligatory and universal during the revolution as labour will be after it.
    """

    $game.butcher.resp -= 2
    $game.butcher.att -= 2

    $c=7



if c==7:

    butcher """

    There won't be any generals or lieutenants or admirals or what-have-you in our war. Well, not on the people's side anyway.

    No, we shall all fight, all classes, races and genders, or lack thereof, united as one equal force. Anarchy cannot be born from state, and a regimented army stuffed and stilted with rank is about as 'state-y' as you can get.

    Yes, I know. Abhorrent, isn't it? It's one thing for people to lead themselves, but an army? Surely not! Such a thing is unlikely to lead to a military dictatorship and how is a state to reassert itself without one?

    You see my point? I will take no orders and I will give no orders. No one will. In war as it is in state, we shall refuse to be slaves.

    Now, shush, before you say anything, that does not mean I will reject all authority. I think my friend, the one I admit I am slightly obsessed with, put it best. And be ready because this is a long one.
    """

    "Mik takes a deep breath, fixes you with a teacherly stare, and then begins:"

    butcher """

    \"Does it follow that I reject all authority? Far from me such a thought. In the matter of boots, I refer to the authority of the bootmaker; concerning houses, canals, or railroads, I consult that of the architect or engineer. For such or such special knowledge I apply to such or such a savant.\"

    \"But I allow neither the bootmaker nor the architect nor the savant to impose his authority upon me. I listen to them freely and with all the respect merited by their intelligence, their character, their knowledge, reserving always my incontestable right of criticism censure.\"

    \"I do not content myself with consulting authority in any special branch; I consult several; I compare their opinions, and choose that which seems to me the soundest. But I recognize no infallible authority, even in special questions; consequently, whatever respect I may have for the honesty and the sincerity of such or such an individual, I have no absolute faith in any person.\"

    \"Such a faith would be fatal to my reason, to my liberty, and even to the success of my undertakings; it would immediately transform me into a stupid slave, an instrument of the will and interests of others.\"

    In other words, I will acknowledge and listen to others without ever allowing any other to control my own will. I will always be free to choose to follow their advice or not.

    What goes for bootmakers and architects is even more true for military tacticians. It will be my choice if I throw myself into a suicide mission, not the choice of some high command I have never even seen.
    """

    menu:

        "But that's not how war works, is it? You need people who can make fast decisions without having to explain all of their reasons to absolutely everyone involved. Philosophy aside, your plan could never win a war.":
            $c=8

        "I have seen my fair share of incompetent commanders. The troops on the ground having more say can only be a good thing." if game.playerbackground = "deserter":
            $c=14

        "You say your friend said: 'I have no absolute faith in any person' and yet I get the impression that if that friend said jump you'd ask 'up who's arse?'.":
            $c=13

        "Sensible and principled. I approve.":
            $c=15



if c== 8:

    if game.playerbackground == "deserter":
        $textinsert = ""
    else:
        $textinsert = ", like you,"

    butcher """

    You think that a group of aristocrats gorged on their own importance would do a better job coordinating the ground forces than the ground forces themselves?

    But I[textinsert] am not a military tactician, so let us pretend you are right. Military efficiency will be lost. But there is one thing that will be gained.

    Justice.

    Okay, even I thought that sounded preachy and melodramatic. Can we pretend I said that in a less pretentious way?

    But my point stands. The social revolution will be just, equal and fair. More, it will be a people's revolution. The number of times I have heard that 'numbers win wars', there must be some truth to it. And we will have the numbers, many times the numbers than our enemies will have.

    And more, because we have truth on our side. Okay now I'm making myself gag. But listen, every statist, bourgeois soldier will be able to see what is coming. They will see their choice is between dying defending men and women who have never and will never care for them, or turning around and joining with the masses for their own liberation.

    If we make our message heard then there won't be a war, because there won't be an opposing army. Just a few scared statists and bourgeois, those few so lost in their own delusions that only death can free them.
    """

    $Mik6Tactics = True
    if game.playerbackground == "deserter":
        $game.butcher.resp += 1

    menu:

        "You make it sound like the country's soldiers would have nothing to lose, but you forget: one side is offering to pay them, while the undisciplined mob is not.":
            $c=12

        "Okay, I'll now presume that you are right, whether you are or not. Still, there will be some people with guns trying to stop you. Who would choose to be the ones running into their bullets?":
            $c=9

        "I hadn't thought of that, and you're probably right.":
            $c=11



if c==9:

    butcher """

    Oh that won't be a problem. We are talking of the social revolution. Who wouldn't fight for their emancipation? True, there may be some who, for their own reasons, would not wish to risk their lives in particular operations.

    Just look at the fervour that many soldiers fight with now, when they are not even fighting for their own rights. No, I don't think the problem will be gaining volunteers. If anything the problem would be deciding on who actually carries out the task … something to ponder for another time I think.
    """

    $game.butcher.resp += 1

    menu:

        "So the gullible then? The people who will go in to the dangerous missions will not be those who are most qualified, or strategically best placed, but those who are most susceptible to social pressure?":
            $c=10

        "You are probably right. People do take dangerous risks for what they believe in.":
            $game.butcher.resp += 1
            $c=11

        "Of course. I would be one of them.":
            $game.butcher.like += 2
            $c=11



if c==10:

    "Mik bites their lower lip."

    butcher """

    A very uncharitable way of putting it. And not one that would hold water after the revolution, I hope. A good scientific, socialist education should put things like peer pressure behind us.

    But it really is too much to expect those influences to be purged from the people before the revolution. To which I suppose I can do nothing but shrug.

    In this one regard, you might be right. But I still maintain that, if anyone has to die, which I agree they will, I would prefer it to be those who chose to take the risk over those who didn't. Even if they did choose to for the wrong reasons.
    """

    $game.butcher.resp += 2

    menu:

        "Good. Now can we talk about when you quoted your friend saying: 'I have no absolute faith in any person.' And yet I get the impression that if that friend said jump you'd ask 'up who's arse?'." if Mik6Friend == False:
            $c=13

        "I agree. Shall we move on?":
            $c=15

        "I don't agree that it's fair or right and I don't think you do either. But let's move on.":
            $game.butcher.resp += 2
            $c=15



if c==11:

    butcher """

    Indeed. I'm not a military tactician, I mean look at me, I couldn't grow one of those handlebar moustaches if I wanted to, but I do know people. And I'm not trying to sound revelatory, but what is war but an interaction between people?

    But enough about my genius, do you have other complaints?
    """

    menu:

        "Earlier you quoted your friend saying: 'I have no absolute faith in any person' and yet I get the impression that if that friend said jump you'd ask 'up who's arse?'." if Mik6Friend == False:
            $c=13

        "No, I am ready to move on.":
            $c=15



if c==12:

    "Mik shakes their head and rolls their eyes."

    butcher """

    Even after all this, you've still got no ability to see outside your paradigm, do you? You'd be one of those last idiot hold-outs, the poor sods so far gone into their master's pocket that there is no hope of ever fishing them out again.

    Money is fake. It's a construct. It's just paper. But freedom? Fraternity, equality? They are real. And everyone, even and especially those bourgeois and statists who fight against reality with all of their might, know it, deep down.

    Now can we move on? Or do you have more inane, narrow minded complaints?
    """

    $game.butcher.resp -= 4

    menu:

        "Earlier you quoted your friend saying: 'I have no absolute faith in any person' and yet I get the impression that if that friend said jump you'd ask 'up who's arse?'." if Mik6Friend == False:
            $c=13

        "I understand. Let's to move on.":
            $c=15

        "You're still wrong Mik, but {i}you're{/i} too closed-minded to see, so let's just move on.":
            $game.butcher.resp -= 1
            $game.butcher.att += 1
            $c=15
            


if c==13:

    "Mik opens their mouth, closes it, and then smiles."

    butcher """

    Firstly, I don't believe everything my friend says. He had a lot to say about the racial rights of the people of the Republic in their relation to the racial rights of the Kingdom, most of which was pretty much nonsense. No, I just believe all of the things that he said that I think are worth repeating.

    Secondly, I believe what you just did, in pretentious language, is called an 'ad hominem'. Basically attacking the person rather than their argument. Even if it was true that I didn't practice what I preach, that wouldn't make what I preach any less true. It would just make me a hypocrite, something I could probably live with.

    But thirdly … fine. Maybe I am a little bit too devoted. (if attraction is above a certain threshold)[Philosophically, of course. Romantically I'm perfectly emotionally available.]

    Next time I'm alone, which will be in a few minutes and last probably until we next speak, I'll have a think about it. Do some real soul searching and inevitably come back reaffirmed that I was right all along about everything.

    Don't you love the human condition?

    Anyway, any other fallacies you want to throw at me?
    """

    $game.butcher.att += 4
    $Mik6Friend = True

    menu:

        "But that's not how war works, is it? You need people who can make fast decisions without having to explain all of their reasons to absolutely everyone involved. Philosophy aside, your plan could never win a war." if Mik6Tactics == False:
            $c=8

        "I have seen my fair share of incompetent commanders. The troops on the ground having more say can only be a good thing." if Mik6Tactics == False and game.playerbackground == "deserter":
            $c=14

        "No, let's just move on.":
            $c=15

    jump reevaluatebutcher6



if c==14:

    if game.butcher.resp < 24:
        $textinsert = "Whatever else,"
    else:
        $textinsert = ""

    if game.butcher.resp > 23:
        $textinsert2 = "And respect for you besides that as well, however painful it is to say that."
    else:
        $textinsert2 = ""

    "Mik nods, slowly and sombrely."

    butcher """

    It's good to hear you say that, [game.player_name]. [textinsert] I have respect for your actions in the war. [textinsert2]

    You have the double experience of having actually been to war and having seen through the lies and manipulations of your commanders. I can think of few better endorsements.

    Well, with that boost of confidence, shall we move on? Or do you want to go back to tearing me down again?
    """

    $game.butcher.resp += 4
    $Mik6Tactics = True

    menu:

        "Actually I do. Earlier you quoted your friend saying: 'I have no absolute faith in any person' and yet I get the impression that if that friend said jump you'd ask 'up who's arse?'." if Mik6Friend == False:
            $c=13

        "No, I am ready to move on.":
            $c=15
    
    jump reevaluatebutcher6



if c==15:

    "Mik claps their hands together."

    butcher """

    Right, with that out of the way, two points occur to me. Just a little ideological clearing up, a little putting ourselves on the same page.

    We will not accept military authority during the war. I hope you can see how it also follows that we will accept neither religious nor scientific authority after it either.

    I would be surprised if you were surprised to hear that I'm an atheist. In fact I see it as a precondition of my philosophy.

    It isn't just the way that statists use religion. I mean that's such old hat that they don't even bother doing it too much any more. It's just too obvious. Sure, the priests still spend their lives giving their statist master's words a veneer of the holy, but everyone knows that.

    I mean for their sake, our 'gods' are just a list of this country's greatest statists! And while that is an extreme position, a ballsy move that most statists wouldn't dare make, other religions aren't better. Bring me a religion that doesn't preach its nation's ruler's creed and I'll show you a heresy.

    No, we all know that, but I go further. Religion implies some sort of metaphysical hierarchy; there is something greater than man which must be worshipped, or at least respected. Some cosmic authority that we {i}must{/i} obey, for some value of 'must'.

    Fuck that. In our case, you're asking me to enslave myself to people who can't even enjoy my servitude because they're not alive any more.

    In the case of the Kingdom's god, we are expected to believe that there's some all powerful being that created and controls all, or at least could. But even if it didn't, just knowing that it could play with us like puppets removes human freedom.

    It doesn't matter whether you don't have free will or you only have it because some deity allows it. Well, at least the first is honest. The second would tease you with it, but control you all the same with the threat of its removal if you dare act out of line.

    No, I believe in human freedom. And humans can only be free if there is no cosmic master, or set of masters, lording over them.

    So there must be no gods.

    A bit twisted, that logic, I grant you. But if humans aren't, or can't, be truly free, then what's the fucking point? There's no such thing as an argument without at least some assumptions, and that's one of mine.

    Anyway, I probably spent more time on that than I needed to. If you're actually religious then it would take far, far, far more time than I care to give to convince you that you're wrong, and if you're not then you didn't need to hear any of that.

    No, my second point is probably the controversial one. There is a common trend among Alexisgrad socialists that if it is wrong to worship religion, it must be right to worship science.

    I think you can probably see where I'm going with this.

    Perhaps I should go back a step. I'm not saying I 'don't believe in science'. I'm not an idiot. The sciences, especially those burdened with the prefix 'social', as if they were in some way inferior to the 'hard' sciences, are what will allow our utopia to flourish.

    The studies of psychology, economics and especially sociology will allow us to move forward as a more enlightened people. Equal education for all will give everyone the tools they need to reason for themselves, as free, informed individuals.

    But here's the rub. No amount of education could ever teach anyone everything. Science is young, relatively speaking, but there is more in each field than it would be possible for any individual to learn in a lifetime.

    There will, I concede, be a disparity of knowledge. There will be many things that some people will know that others won't. That is a fact of life, and no social revolution could change that. What it can change is who can access that specialist information, and while that will shift from just the privileged classes to everyone, that doesn't change my point.

    There will be some who have more knowledge of the social sciences, again foremost sociology, than others, either out of inclination or out of ability. What I stand against is not science, but these individuals being given any elevated status within society.

    An expert of the social sciences should be treated with no more respect than a shoemaker. Which isn't to demean them, because I could just as easily say that we should treat shoemakers with the same respect we show expert social scientists.

    This is because there is just as much slavery in science as there is in religion. Just as much that can strangle a person's freedom in scientific planning as theological doctrine.

    It all comes down to what I keep on saying and will keep on saying till the day I die: we will not be free until our society is organised by the people from the bottom up, rather than from a minority from the top down.

    Whether it is a statist, a bourgeois, a priest or a scientist who sits at the top, what they impose on those below them is slavery. It may be a different shade of slavery, but I don't care what colour you paint it, slavery is slavery.
    """

    menu:

        "But science is different from statism or capitalism or religion. It's rational and reasoned. It uses objective facts.":
            $c=16

        "Not all religion is like that though. Belief in the spirits is belief in other entities that are equal to us.": #JE if JoanScene >= 4
            $c=17

        "Those are all good points. We can't accept any masters, regardless of what they call themselves. Shall we move on?":
            $game.butcher.like += 2
            $c=18



if c==16:

    butcher """

    Maybe my language was a bit harsh. Or maybe you just weren't listening. Either way, let me say that yes, of course science is different. Of those four, it is the only one that is true.

    But it is not that simple. I am not a scientist. I would be bold to even call myself a philosopher. But I have read and listened to much about both. Science is great, but it can only prove a negative.

    I have friends who very passionately believe that mathematics and logic are branches of philosophy rather than science. Personally I think there are better - 'actually important' - things to get militant about, but I do think they are right. You can prove things in maths and logic. You can't prove anything in science.

    Philosophically, the problem is with induction. It's a type of argument. You take what exists in the world and you extrapolate information from that. \"I have met one hundred thousand statists, all the statists I have met were evil idiots, you are a statist, therefore you are an evil idiot\". That kind of thing.

    That is a perfectly valid inductive argument. And the premises would be true as well, but I was exaggerating with the number. Not exaggerating the thing about them all being evil idiots, that's true.

    But my provocative argument illustrates my point: there would be nothing to stop you saying 'well that doesn't {i}prove{/i} that there isn't a single clever and nice statist, just that it's unlikely'. You would be absolutely right.

    There is always a chance that there is a nice statist, there is always a chance that a chemical will burn at a different temperature next time, and there is always a chance that the sun will not rise tomorrow.

    See?

    No, science can never prove a positive statement, only disprove it. Or prove negative statements, 'it is not the case that all swans are white', but that comes to the same thing. And it can do this disproving very easily. One clever statist, one day when the sun doesn't rise, and the whole theory is out. Or, one failed nation, one starving child, one industrial slave, and the whole societal model is out.

    When we talked those first two times, when I was showing you why the capitalist and statist models don't work, that was science. Science can prove things to not work or not exist just fine, and that is what taught us the negative conditions of the future, how we must tear down individual property and any kind of controlling authority within human lives.

    But more than that? I can't say. Science can't say. Because you would be asking for a {i}positive{/i}, a constructive, proposal. And no science can guarantee truth.

    Science can never prove that it is not itself dogma.

    And besides all those technical details, science is still carried out by humans. And humans, whether they are scientists, statists, bourgeois or theologians, are corrupted by power in the same way.

    It is the elevation of scien{i}tists{/i} I argue against. Not {i}science{/i} itself.
    """

    $Mik6Science = True
    $game.butcher.like += 1
    $game.butcher.resp -= 1

    menu:

        "Sure. But on religion, not all religion is like that though. Belief in the spirits is belief in other entities that are equal to us." if Mik6Religion == False: #JE and if JoanScene >= 4
            $c=17

        "Okay. Shall we move on?":
            $c=18

        "What about other positive claims you've made, like 'work will be obligatory' and 'property will be collectivised'. Aren't they positive statements?":
            $c=19



if c==17:

    butcher "Spirit worship? I can't say I'm familiar … Is that a local custom?"

    "You nod and Mik pulls a long, quizzical face."

    butcher """

    Interesting. Well if it is what you say it is, then I {i}probably{/i} couldn't object.

    But, and this might be insensitive, this really isn't my area, I would be hesitant to call it a religion. Maybe a superstition, or some kind of folk tradition. Which could be harmful in its own way, standing in the way of communal socialist scientific understanding, but it probably wouldn't be as fundamentally inconsistent with anarchist collectivism as other religions.

    But now we're playing semantics and that's not helping us get anywhere. I think we both know what I meant when I said 'religion', and I stand by what I said about it.

    I should look more into this spirit worship though. Always good to know about everything that challenges your own beliefs.
    """

    $game.butcher.resp += 4
    $Mik6Religion = True

    menu:

        "Okay. But what about science? That is different from statism or capitalism or religion. It's rational and reasoned. It uses objective facts." if Mik6Science == False:
            $c=16

        "Okay, let's move on.":
            $c=18
    
    jump reevaluatebutcher6



if c==18:

    butcher """

    There's not much to move on to, I'm afraid. I seem to have lost myself along the long road of the role of the individual within the world of the social revolution, but I think I've reached the end.

    Sorry, I'm being a prick again. Blah blah blah finished now. I've said all I wanted to say.

    About this.

    I will not be leading the social revolution, and neither will anyone else.

    I should have just said that in the first place, eh?

    Well fine, you've got places to be and I've got sweat I've should think about sweating. I don't want to waste even more of your time by lying here and telling you about all of your time that I've wasted.

    Seriously, go on. I should do some push ups and I don't like anyone knowing that I can't even do one.
    """

    return



if c==19:

    "Mik nods, off guard but in no way annoyed."

    butcher """

    A fair blow, now let us analyse the wound together.

    So 'work must be obligatory and property collectivised' is a positive statement. It should probably have 'within a free and equal society.' at the end, but I think we both knew that was implied. Regardless, I can't prove it.

    With science.

    Luckily for me, I'm not doing science. My argument is deductive, not inductive.

    The gods really did curse us when they invented jargon, didn't they?

    Deductive: working from the large to the small. Inductive: working from the small to the large.

    'I have seen five swans and all were white', small, 'therefore all swans are white', large. Inductive.

    'All swans are white', large, 'therefore these five swans must be white', small. Deductive.

    Both wrong. But wrong for different reasons. Inductive is all about guesses and extrapolations. Deductive is just about applying definitions. If the definitions are right, then the statement is right.

    Which sounds just as tricky, 'how can you know the definition is right?' but actually isn't so bad, because definitions are just things that people made up, and a good deal of the time, like with 'labour', 'property', 'liberty' and 'equality', the things we are defining are also things we made up.

    So 'all things that split resources or responsibility equally between all parties are examples of equality', large, 'obligatory work splits responsibilities equally between all parties, therefore obligatory work is an example of equality', small, is a deductive argument. It's got nothing to do with science.

    I prefer the deductive. It's cleaner, it guarantees truth and, most importantly, I don't have to leave the house to go count things.

    So that's that. All very tangential, taking me back to my childhood lessons in philosophy, but I hope that answers the question. And if it doesn't then keep it to yourself, I'm worried about catching frostbite from being away from my cosy warm comfort zone for too long.
    """

    menu:

        "Sure, we can return to religion then. Not all religion is like what you described. Belief in the spirits is belief in other entities that are equal to us." if Mik6Religion == False: #JE and if JoanScene >= 4 
            $c=17

        "Okay. Shall we move on?":
            $c=18

    jump reevaluatebutcher6

return
