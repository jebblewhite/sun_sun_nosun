label aldermanscene9: 

if game.coup == "Alina":
    $textinsert = "enthusiastically "
elif game.coup == "Alderman":
    $textinsert = "tentatively "
else:
    $textinsert = ""


$ numberofweeks = game.ceil((30-game.day+3)/7)

"""

'In the event that the people believe their immediately appointed leader is acting against their interests,' the town's charter reads, 'they shall send a representative to address the Republic senate, who will judge the issue impartially and with the people of the town's interests as their chief concern.'

It does not take long before that single line starts circulating around the town and it takes even less time before everyone has an opinion on it.

Many lamely point out that 'impartially' contradicts 'and with the people of the town's interests as their chief concern', proving that they have a basic level of reading comprehension but little else.

Most point out the main problem: 'they shall send a representative to address the Republic senate'.  Some wield this line as a shield, others as a sword.  'There is no legal way', the former argue, 'to depose the Alderman, so we cannot depose the Alderman.'  The latter, meanwhile, say 'There is no legal way to depose the Alderman, so we must do it ourselves.'

Why 'there is no legal way' is self-evident.  Exactly who 'the Republic Senate' is is another matter of pointless debate, with some arguing it is a possibly non-existent social body hundreds of sunless and dangerous miles to the south, while others argue that, in all relevant ways, it is one woman regularly drifting in and out of confused consciousness in Fyodora's clinic.

Either way, both sides agree, it is out of Lotosk's reach.

You are [textinsert]involved in these discussions.  Your opinion on the logic of the charter and the exact nature on what you should take 'the Republic senate' to mean are, like everyone else's opinions on those matters, irrelevant.

But the main question remains.  What should be done about the Alderman?
"""

$ aldermanConvinced = False

menu:
    "He obviously sabotaged the step, we should force him out of office, or worse":
        $c=1

    "He obviously sabotaged the step, we should force him out of office":
        $c=2

    "We should definitely investigate, the timing is just too coincidental":
        $c=3

    "The Alderman would never intentionally do anything to harm someone":
        $c=4

    "The Alderman is too weak to do something like that":
        $c=23

    "*Try to keep your opinion, whatever it is, to yourself*":
        $c=5

label reevaluatealderman9:
if c==1:

    """

    Your view is shared by many of the kind of people who considered joining Cynthia and Edward, but couldn't face the danger, the kind of people who keep their old pitchforks, sharpened, under their beds.

    Still, the vague allusions to 'or worse' are never expounded upon, despite a loyal core strongly supporting them.  No-one seems quite ready to actually discuss exactly what horrible things your mob could do, never mind actually begin planning them.

    Maybe you're all just waiting for the right ignition.
    """

    #jE{Unrest increase}  
    #{Very slight morale loss}

    $c=6

if c==2:

    """

    Your view is shared by many, all of whom have have no proof but plenty of intuition.  

    On the other hand, it isn't as if the other side has better evidence.  True, all of yours is circumstantial, but the Alderman's supporters only have 'he isn't that kind of man' when trying to wave away the coincidence.
    """

    #{Slight unrest increase}

    $c=6


if c==3:

    """

    Your position is seen as infuriatingly sensible, and is therefore unpopular.

    Still, while it may not make you any friends, it does place you on the edge of both circles, and you become the mediator whenever both sides happen to meet.  

    The presence of logic tends to have a calming effect, and many an argument that started with barbed words and personal attacks is soothed by your presence into a more or less civil disagreement.

    Not to say that you completely shut down the debate.
    """

    #{Slight unrest loss}  #{Very slight morale gain}

    $c=6


if c==4:
    """
    Your view is shared by a variety of people: the older generation who have known Alexi all their lives, the young who just want peace and those of all ages who don't really care about the truth, but know Alina is bad news for the town.

    Whatever the reason, your critics are always quick to point out that it doesn't matter how nice the Alderman appears, there is no escaping the fact that the first time there ever appeared to be a problem with that staircase was the very moment that Alina was climbing it to deliver her senate writ.

    And, more than that, she only had to do that because he had strongly insisted that she had to do it in his Town Hall …
    """

    #{Very slight morale loss}

    $c=6


if c==5:

    """

    While you are sure that everyone has an opinion, you are not alone in not sharing yours.

    Whether it is your intention or not, staying out of it is the equivalent of not adding your log to the fire.  The fewer people who talk about the controversy, in other words, the faster it will all burn out.

    Although there is little evidence of that happening any time soon.
    """

    #{Very slight unrest decrease}

    $c=6

if c==6:
    if game.alderman.relationship_matrix(2,1,1) >= 8 or game.alderman.romance: #MM
        

        "The argument just keeps digging itself into the same ruts, the same points batted back and forth time and time again, neither side gaining any ground, until the Alderman knocks on your door."

        alderman  "Hello [game.player_name], I hope I am not interrupting anything?"

        "You shake your head."

        alderman  """

        Good.

        Well, I wanted to tell you what I am planning.

        I think it is the best thing to do.

        I am sure you're aware that there is a rumour going around that I intentionally sabotaged the stairs.  Some people, I hear, are calling for my resignation.  Or worse.

        But I can't let that happen, can I?

        This town needs strong leadership.  It needs someone who knows it, someone with a strong understanding of not only the surrounding countryside and its resources, but also the infrastructure and people of the town.

        But more than that, this town needs someone who will protect it, and protect its liberties and equalities.  The people of this town are free, and they are all treated with fairness and equality.

        The people want change.  That is clear.  But I am convinced that what we are doing now is best for the town.  There is no fairer distribution of our resources than strict equality, and everyone has access to Fyodora's services.

        Any actual change would lead to a worsening of the people of Lotosk's living conditions.  And, I also strongly believe, a decline in the likelihood that we will survive.

        I am the only one in this town who has both the knowledge and the motivation to maintain those methods.

        So it is clear.  I cannot resign.

        It is my moral duty to stay as this town's Alderman.
        """
        menu:
            "You're right, you need to stay.  No-one else could do what you do":
                $c=18

            "If the people want you to step down, you need to step down.  You talk about equality and liberty, but how can we have either if you become our dictator?":
                $c=12

            "You're wrong, your way isn't the best for this town.  You need to step down":
                $c=9


    else:
        """
        The argument just keeps digging itself into the same ruts, the same points batted back and forth time and time again, neither side gaining any ground.

        That is until the Alderman announces that he is going to make a public statement.

        It is quickly decided, through intimation and never out loud, that this will be the moment when everything will be decided.  When Alexi is either absolved or condemned.
        """

        $c=7


if c==7:

    """

    Almost the entire town waits in the dark, looking up to the steps of the Town Hall.

    When the Alderman appears, he is visibly thinner and more hunched.  Deep, dark teardrops of flesh hang beneath his eyes.

    His voice, when he speaks, cracks slightly, but still carries with an unusual clear volume.
    """

    alderman  """

    Hello.

    As I am sure you will all be pleased to hear, I am too tired not to just get straight to the point.

    I have heard that many people have proposed that I am guilty of sabotage.  That somehow I intentionally caused the stairs of the Town Hall to collapse under Alina when she came to deliver me the senate writ.

    I will start by saying that these allegations are untrue.  I will not try and prove that they are untrue.  I cannot, I don't even know how I could, and besides, here in the Republic, we assume innocence until guilt is proven.  I am sure Alina would agree with me on that point.

    But I know that is not enough.  I cannot prove my innocence and stating that I am innocent will not be enough to make those of you who think they have circumstantial evidence against me change their minds.

    In other words, I am saying I am innocent, not because I think it will change your minds, but for the record.

    You may think what you think.  I cannot stop you from doing that.  And without evidence, I would not wish to, although I must honestly say I do not know where I would find such evidence.
    """

    "The Alderman pauses for a moment, placing his hand on the side of his head, closing his eyes and taking a deep breath."

    alderman  """

    I know that many of you would, at the very least, like to see me resign.  I very much understand the desire to wipe the slate clean.  Because it is dirty.  This endless night had made it dirty before, and this new tragedy has only made it worse.

    But I wish to ask you a simple question.

    Who would take my place?  You may disagree with my decisions, you may even think I attempted to kill my political rival, but I hope that none of you will deny that I am the most qualified person to lead Lotosk.

    As we find the forest and river running low on all those things we need to survive, as the air becomes colder and the snow deeper, is now the time for a novice to take on the mantle?

    Believe me, I do wish that there was someone good who could take this burden from me.  If the sun was shining now I would gladly step down, even in the face of false allegations.

    But I don't have that luxury.  We don't have that luxury.

    Sorry.  I realise that I said I was asking you a question, but I am yet to give you the opportunity to answer.

    So.

    Who would replace me?
    """

    "Without a moment of hesitation, Mik's elegant, blood stained hand is in the air."

    butcher """

    No-one.

    Or are we all happy to let this opportunity to finally break the statist, bourgeois charade and take control of our own lives slip by?
    """

    "Man"  "Oh please gods, shut the fuck up!"

    if game.popCohesion<= 30:
        "Woman"  "I wish Cynthia or Edward was still here!"
    
    "Woman"  "What about [game.player_name]?"

    "Man"  "Oh yeah, [game.player_name] would be good, they've basically been running the town anyway."

    butcher "We're really going to just hand the key to our shackles to someone else?  Not even think about emancipating ourselves?"

    if aldermanConvinced:
        """

        Ignoring Mik, the crowd turns to you.

        There is a sudden stillness in the air.  Something presses down on you, the weight of responsibility pushing air out of your lungs and rushing blood through your heart.

        The Alderman gives you a small, resigned shrug, and a smile.

        Mik stares at you, their eyebrow raised.

        For the first time, the crowd stands completely still.  

        They have chosen their ambassador.

        But what will their ambassador say?
        """
        menu:
            "I will take on the Alderman's responsibilities":
                $c=8

            "Our Alderman is right, he is the best person to lead us":
                $c=19

            "The Alderman should continue to lead, but only till Alina recovers":
                $c=21

            "Mik is right.  We don't need any leaders":
                $c=24
    
    else:
        "Ignoring Mik, the crowd turns to you, but before you can open your mouth, the Alderman has stamped his foot with surprising force."
        #MM
        if game.alderman.relationship_matrix() < 8 and not(game.alderman.romance):
            alderman  "

            [game.player_name] is not qualified to make this decision.  [game.player_name] doesn't have the knowledge or skills required to run this town.
            "
            
        else:
            alderman "
            [game.player_name] and I have already discussed this and agree.
            "

        $c=20


if c==8:

    #{Set $NewLeader = "[game.player_name]"}  #{Unrest decrease}

    """

    Almost immediately, the crowd starts chanting your name.

    Yes, there are some who scowl.  Some who shake their heads.  Some who simply stand awkwardly with their hands by their sides.

    But it is clear that the majority has achieved what they wanted.

    The Alderman is out, and someone else is in.

    Or at least, in theory.

    It takes almost a full minute of holding his hands up for quiet before the crowd finally lets the Alderman speak.
    """

    alderman  """

    [game.player_name] is a good person, an intelligent person and a hard worker.

    If this truly is the will of Lotosk, I will accept it.
    """

    "The crowd begins cheering again, and again the Alderman requests quiet."

   

    alderman  """

    I will accept it, but on two conditions.

    Firstly, we must hold an election. I think the result is already clear, but I think we can all agree that the process will be easier and clearer for everyone, especially [game.player_name], if [game.player_name]'s elevation is official.

    Secondly, I will not relinquish my post for [numberofweeks] weeks.  

    Yes, yes I know that you all want to see change now.  But [game.player_name] still has much to learn, and I will need that time both to set up the election and to train [game.player_name].  Running a town, never mind a town dealing with what we are dealing with, is a complicated procedure.

    I trust that this is all acceptable to you?
    """

    "The extremists on both sides of the crowd cancel each other out, and the overall opinion is grudging acceptance."

    alderman  """

    I am sure I will make a concession speech after the election.  But for now, I just wish to say that I think that we have all made a difficult choice here today.

    I must admit, I am unsure if it is the right choice.

    But I have been reminded of the importance of democracy.  Liberty cannot survive under dictatorship.  So I will step down.

    Serving Lotosk has been the greatest gift that life has given me.

    Serving Lotosk has been my life …

    I don't …

    Well.

    None of you came here to hear an old man ramble about his life.

    I should let you all go back to work.

    Nat will keep you all informed about the progress of the organisation of the election.

    [game.player_name], may I have a word?
    """

    "The Alderman waits for the crowd to disperse before beginning to speak, the two of you standing alone on the steps of the Town Hall."

    alderman  """

    We should not waste too much time before we start your lessons.  An hour or so in the mornings, you might lose a little sleep but it shouldn't affect your ability to work.  

    It might take a little while that way, but I am sure you will agree that it is best for the town?
    """

    "You nod, and the Alderman smiles."

    alderman  """

    I must admit, it is true what I said before.  I don't think you are ready to run this town.  And I do not know if this was the right choice.

    But it is far from the worst choice, and it is the one we have made and I will not go back on that.  I am sure that the people are happy and I am just as sure that you will win that election.

    I will admit, I am looking forward to the rest.
    """
    if game.alderman.romance:
        alderman "Now, with the business out of the way, may I ask you a question?"
        $c=22
    else:
        alderman """
        I look forward to working together, [game.player_name].  A new chapter in our relationship.  A new chapter for Lotosk.

        Together, [game.player_name], I'm confident.

        I'm behind you [game.player_name].

        We'll get through this.

        Lotosk.  Together.
        """
    


if c==9:

    "The Alderman looks at you, obviously too worn down to be surprised."

    alderman  "What could be better?"
    menu:
        "Alina was right.  We should be prioritising those who work hardest":
            $c=17

        "Mik is right.  We don't need a leader at all":
            $c=15

        "I don't know what is best.  But I would start by actually listening to the people of this town":
            $c=10


if c==10:

    alderman  """

    But the people don't have the experience I have.  

    They don't know what would be best for themselves, they don't have the specific specialist knowledge required to know what it takes to run a town.
    """

    #{Slight like increase with the Alderman}
    menu:
        "'The people don't know what's good for them'?  That sounds like something a dictator would say":
            $c=12

        "You have to give the people some credit.  These are the people who chose to stay, rather than leave with Cynthia and Edward":
            $c=13

        "They don't need specialist knowledge, all that matters is the will of the people":
            $c=11


if c==11:

    "The Alderman shakes his head sadly."

    alderman  """

    I am afraid not.  You should know that knowing what you want and being able to do it are two different things.  

    That just isn't the way the world works.
    """

    #{Respect loss with the Alderman}

    $c=14


if c==12:

    """

    The Alderman stares at you for a moment, and then looks down at his feet for an uncomfortably long time.

    When he finally speaks, it is in a whisper.
    """

    alderman  """

    I can't become a dictator.

    I haven't come this far to become what Cynthia wanted me to be.

    I have already made that decision.  I have already let them go into the dark because of it.

    Even if it is just for her sake, I cannot go back now.

    Alina is right about that, isn't she?  We're not all equal as long as I refuse to share my power.  And the people can't be free until they have a say in what happens to the results of their labour.

    But … but who could do better [game.player_name]?  Because ideals and philosophy aside, this is still a practical matter.  A matter of life and death, for everyone in this town.

    I don't know [game.player_name].  I really don't know.
    """

    #{Respect gain with the Alderman}

    $c=16


if c==13:

    alderman  """

    True.  But many of them are also the people who supported Alina.

    The people want change for change's sake.  They see that the problems that were fresh when Cynthia and Edward left have not gone away, and they are desperate to find something they can do to change that.  Politicians are always a good place to start.
    """

    #{Slight like gain with the Alderman}

    $c=14



if c==14:

    alderman  """

    I have made my decision [game.player_name].  Well, I made it quite some time ago, but my mind has not been changed.

    What the people want is always important, and it is the lifeblood of a politician.

    But sometimes, a leader must do what is necessary, not what is popular.

    I am not stepping down as Alderman of this town.

    I will go now [game.player_name].
    
    """
    if game.alderman.romance:
        
        alderman " Believe me, I wish I could stay.  Maybe after all this politics is over, maybe then we can spend some time together."

    alderman "I will call a meeting, later today, to tell the people what I have decided.  I suppose I will see you there [game.player_name]."
    

    #MMJE Fade to black, then fade back in to the town square.

    $ aldermanConvinced = False

    $c=7
    jump reevaluatealderman9



if c==15:

    "The Alderman shakes his head, looking almost amused."

    alderman  """

    Mik is a very smart person and if I had more time I am sure I would enjoy listening to some of their ideas.  

    But the people will never agree to it.  It's not how Lotosk runs.

    Which might actually be a shame, in a way.  Maybe if we had the kind of equality that Mik argues for, I could continue to use my knowledge to guide the town, without the burden of being its only leader.

    But alas, the people will never agree.
    """

    #{Slight respect loss with the Alderman}

    $c=16


if c==16:

    alderman  """

    Maybe the answer is to persuade the people that I am their best choice.  Let them freely choose me?  Or maybe just convince them that they have chosen me.

    Oh [game.player_name], I am far too old for this.  And tired.  I don't want any of this.

    But what choice do I have?

    I will go now [game.player_name]. 

    """ 
    
    if game.alderman.romance:
        
        alderman "Believe me, I wish I could stay.  Maybe after all this politics is over, maybe then we can spend some time together."

    alderman "I will call a meeting, later today, to tell the people what I have decided.  I suppose I will see you there [game.player_name]."

    #MMJE Fade to black, then fade back in to the town square.

    $ aldermanConvinced = True

    $c=7
    jump reevaluatealderman9


if c==17:

    "The Alderman shakes his head with more force than you thought his tired body should be capable of."

    alderman  """

    No.

    No.

    We have talked about this, and I have thought all I can think about it.

    Alina was wrong.  Of that I am utterly convinced.
    """

    #{Like, respect and attraction loss with the Alderman}

    $c=14
    jump reevaluatealderman9


if c==18:

    "The Alderman nods, strangely sadly."

    alderman  "Thank you.  It is … surprisingly difficult to hear that you think there is no other way."

    #{Like gain with the Alderman}

    $c=14
    jump reevaluatealderman9


if c==19:

    "The crowd, which had only seconds ago pinned all of its hopes on you, deflates, the anger and hope sucked out as the Alderman takes advantage of the silence to resume speaking."

    #{Like increase with the Alderman}

    $c=20


if c==20:

    #JE{Set $NewLeader = "Alexi"}  #{Unrest increase}

    alderman  """

    I have considered everyone in this town, I know all of you, and while all of you have your own skills and talents, most of which I would never be able to match, none of you have the specific skills required to lead this town.

    You would not, I believe, expect me to treat your wounds in the way Fyodora does, or keep the time like Nat.  They have specialised skills that no-one else here has.

    It is the same for me.

    I wish I did not have to carry this burden.  I wish that there was someone we could all trust to whom I could pass the baton.

    But there is not.

    So I am not leaving.
    """

    """

    There is a moment of silence after this, broken as one brave, loyal person cheers.

    It is all the despondent crowd needs to break apart.

    'There'll be another chance', 'People will realise he's the problem' and 'Alina will be better soon'.

    The crowd has not given up on the possibility of a fight.
    """
    if game.popCohesion< 30:
        "It simply acknowledges that it is smarter to bide its time."
    else:
        """
        It simply does not have the appetite for it.

        Yet.

        """
    if game.alderman.romance == False:
        """
        The Alderman looks at you, standing amongst the thinning crowd, and nods.

        He is clearly tired and worn down.

        There is sadness in his eyes, and pain.

        But he is still standing.

        And he will continue standing.

        Alone.
        """
    else:
        """
        The Alderman looks at you, standing amongst the thinning crowd, and beckons for you to join him.
        """

        $c=22


if c==21:

    """

    The Alderman neither speaks nor moves for several seconds, staring at you with a mixture of sadness, confusion and betrayal.

    The crowd, or at least a not insignificant part of it, on the other hand, has started chanting 'Alina, Alina, Alina!'

    When the Alderman finally talks, it is in a voice so quiet the crowd is forced to hush in order to hear him.
    """

    alderman  """

    Alina's plans, as I have said, are vile and evil.  

    But I can see that I will not be able to convince many of you of that.

    It seems, therefore, that you have given me no choice.

    Once Alina has recovered enough to agree, we will hold an election, a fair, open election.

    Lotosk is a democracy, as is the Republic.  It is clear that many of you will not be satisfied with me retaining my position, but I urge you to consider that Alina taking it with nothing more than a piece of paper is equally, if not more, undemocratic.

    So we will have an election.  And, of course, I promise to abide by the results.

    Even if the vote does favour Alina and her evil policies.
    """

    """

    The crowd seems satisfied with this.  True, some seem disappointed by the lack of immediate satisfaction, but most accept the reasonableness of the Alderman's suggestion, and, with a nod from him telling them that he has said all he is going to say, they begin to disperse.

    The Alderman smiles through gritted teeth until the crowd has left, and then he looks to you.  His face drops.  He doesn't even put in the effort to scowl.  

    He simply stares for several seconds,

    shakes his head, 

    and walks away.
    """

    #{Set $NewLeader = "Alina"}  #{Slight unrest decrease}


if c==22:

    alderman  """

    This has been a...very difficult time.  For me.  Personally.

    I know there is probably a great deal more to talk about.

    But I feel I have done all the talking that I can, at least for a little while.

    So I wanted to ask you [game.player_name].

    Can I come back to your home?  Just for a little while.

    I … well, I want you to hold me.

    I want the only thing I have to think about, for a time, to be you.
    """


if c==23:

    """

    Your view is an uncommon one, but quickly picks up sympathisers.  There are many who oppose the Alderman, but do not believe him capable of what might very well be attempted murder.

    The debate tends to die quickly around you and those who argue the same as you.  You quickly find common ground on both sides of the argument, or rather both sides find common ground with you, and both tend to leave unhappy but at least a little more unified than they were before.  

    Still, your claim is not enough to sway the extremists on either side, those loyal to the Alderman refusing to agree to their leader's fallibility, while those accusing him of sabotage point out that you have failed to answer the question at the heart of the affair:

    Why did the staircase happen to fail at the very moment that the Alderman was to be deposed?
    """

    #je{Very slight morale loss}  #{Slight cohesion gain}

    $c=6
    jump reevaluatealderman9


if c==24:

    noah "Long live the social revolution!"

    """

    There is a moment of stillness.  You see Mik, standing as always near the edge of everything, suddenly frozen, not even their eyes moving within their mask of terror.

    They wait for the ideal of the people to make itself known.
    """
    if game.butcher.scene >= 7:
        "Man"  "If [game.player_name] is for it, then I'm for it."

        "Woman"  "It's about time we took our own lives into our own hands."

        "Woman 2"  "For equality and liberty!"

        noah "Yes!  Yes yes yes!  I'm so proud of all of you!  I knew that the people of Lotosk would-"

        butcher "It's highly unorthodox!"

        "The crowd takes their lead from Noah and quietens at the interruption, turning to Mik."

        butcher """

        The social revolution must take place through social, rather than political means.  

        It must be total and final.  Therefore anything that we achieve here will not be the social revolution, but merely a precursor.

        Finally, and crucially, it must be destructive.

        I feel a little bit like I have just been hit around the head, and maybe that is why I'm going to let these words flop out of my mouth:

        But you haven't done a bad job, for an Alderman.  You've been a good socialist, and not a terrible statist.

        But you have an important decision to make.  Will you let the people tear down everything: your power structures, your traditions and your laws?  Will you let it not just be collapsed, but torn apart and burnt?

        And if, as I suspect, you won't, then we, the people, have a decision to make.  Will we let that lie, or will we tear it down anyway, knowing that with it we must take the man who defends it?
        """

        "Mik turns to look across the crowd, but before anyone can respond to such a weighty question, the Alderman interjects."

        alderman  "I will."

        "Mik's eyebrows shoot up so far they almost spin around the back of their head and slam their gaping jaw shut."

        butcher "You will?"

        alderman  """

        I will, but on two conditions.

        Firstly, we must hold an election. I think the result is already clear, but I will not sacrifice democracy unless that is the democratic will.

        Secondly, I will not relieve my post for [numberofweeks] weeks.  

        Yes, yes I know that you all want to see change now.  But we should do this properly.  I don't like all this talk of 'tearing down' and 'destruction'.  We live in a small town, but this is a dangerous, complicated time.  Not to mention that Lotosk is still a part of the Republic.

        Lotosk is all that matters to me.  If it really is the will of the people, as an election will confirm, to leave the Republic and reject all government, then I will be happy to step aside.  But it must be done properly.  It must be done in such a way that no-one will starve, and the Republic will not have cause to … well I don't know.  But it must be done properly.

        There are conversations that must be had with Alina that only I can have.

        I trust that this is all acceptable to you?
        """

        butcher "An election to decide the social revolution?  No no, the social revolution cannot come about through political means.  And [numberofweeks] weeks before you abdicate?  More than enough time to bury the seeds of statism deep."

        "Man"  "Oh come off it, the Alderman's a good man."

        "Woman"  "You forgot why we're here?  He tried to kill Alina!  She's who should be running things!"

        "Woman 2"  "Oh anyone but Alina!  I still think [game.player_name] should be in charge!"

        "Multiple voices spring up at once, but one is strong enough to cut through all the rest."

        noah "We'll take it Alexi!  It's not ideal, but it's got to be better than what we've got now.  And Mik, if it isn't good enough, then we'll just do the revolution anyway, we won't be any worse off."

        "Perhaps Mik was planning to respond, but all but the most extreme political holdouts begin to cheer, so all they do is glare."

        alderman  """

        It seems to be decided.  Good.  I am sure I will make a concession speech after the election.  But for now, I just wish to say that I think that we have all made a difficult choice here today.

        I must admit, I am unsure if it is the right choice.

        Liberty cannot survive under dictatorship, and I understand that while I must give up democracy, I have heard enough of your way of thinking to know that it is not all bad.  So I will step down.

        Serving Lotosk has been the greatest gift that life has given me.

        Serving Lotosk has been my life …

        I don't …

        Well.

        None of you came here to hear an old man ramble about his life.

        I should let you all go back to work.

        Nat will keep you all informed about the progress of the organisation of the election.
        """

        """

        The crowd lets out a cheer, and surges away towards Henryk's inn, carrying Noah above their heads.  They had tried to do the same with Mik, but they had violently brushed them away and disappeared somewhere.
        """

        #{Set $NewLeader = "Alexi"} #{Slight like gain with Mik}

        if not game.alderman.romance:
            """
            The Alderman looks at you, standing amongst the thinning crowd, and nods.

            He is clearly tired and worn down.

            There is sadness in his eyes, and pain.

            But he is still standing.

            And he will continue standing.

            Alone.
            """

        else:
            "The Alderman looks at you, standing amongst the thinning crowd, and beckons for you to join him."
        

            $c=22
            jump reevaluatealderman9
    else:
        "Man"  "Didn't I tell you lot to shut the fuck up?"

        "Woman"  "We're barely surviving as it is, and you want to introduce anarchy and chaos?  We'll all die!"

        "Man"  "Now isn't the time to become animals!  We need to come together, not sink into lawlessness!"

        "Mik's gaze swivels lazily between you and Noah, clearly furious."

        alderman  "I see the good intentions of [game.player_name]'s words, but you are all right, now is not the time to take such risks."

        #{Slight respect loss with Mik}  
        #{Slight like gain with Mik}

        $c=20
        jump reevaluatealderman9





return
