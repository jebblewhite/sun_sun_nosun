label aldermanscene6: 

"""

You find yourself doing a double take when you see the Alderman sitting in the corner of Henryk's inn, a half empty glass in front of him.

Curious to discover what could have brought him here, you walk over, the Alderman indicating the free chair opposite him when you are close.
"""

alderman  "I don't know if she's wrong."

menu:
    "Alina?  She's definitely wrong!  If we are going to survive this, we have to work to keep as many of us alive for as long as possible.  Anyone could be the innovator, and we all rely on each other":
        $c=1

    "Alina?  She might be right, technically.  But what she says is evil, and evil is always, ultimately, wrong":
        $c=2

    "Alina?  Yes, she's right.  If we keep giving the same to those who work as we do to those who don't, we will all die":
        $c=3

    "Alina?  I don't know.  I just don't know":
        $c=4


if c==1:

    alderman  "But we don't all rely on each other.  Some citizens are simply more productive than others."

    #{Slight like, respect and attraction increase with the Alderman}

    $c=5

if c==2:

    alderman  """

    But if she's technically right, how is it evil?  How is it evil to want people to live?

    What if I am being evil and I don't even realise it?
    """

    #{Slight like and respect increase with the Alderman}

    $c=5

if c==3:

    "The Alderman nods as if he didn't hear you, although his eyes show that he did and just wished he hadn't."

    #{Like loss with the Alderman}

    $c=5

if c==4:

    "The Alderman shakes his head in solidarity."

    #{Very slight like and attraction increase with the Alderman}

    $c=5


if c==5:

    alderman  """

    Am I only objecting to Alina's logic because I know that she is right and it would be best if I was left to die?  Am I just being selfish, supporting a system of distribution that keeps me alive when really I do nothing for this town?

    No.  No, it can't be that.  I am not afraid of death.  I haven't been for a long time.  Maybe that makes me a bad Republican?  Didn't Alina say that it is fear that motivates us?  Maybe that is my problem.  I am not scared.  Does that mean I don't care enough?
    """

    "The Alderman takes a long, slow drink.  When he puts the glass down, it seems that he is only half aware that you are there."

    alderman  """

    I always thought that if I'd had more time to make the decision, then I would have done it right.  If I'd only had time to think, I would have done it right.  

    People call me slow, and maybe they are right, but at least part of it has always been caution.
    """

    "Another pause, and then the Alderman places his head in his hands and begins to sob."

    alderman  """

    Oh [game.player_name], I thought the gods were testing me!  I thought they were giving me a second chance, an opportunity to get it right this time.  I thought I was sure that I knew what to do.  I had to balance the loads, make sure that this time we all had enough.

    But what if I am wrong?  What if they aren't testing me, they're punishing me!  What if they don't want me to do better, what if they're showing me what he felt?  What if they want me to walk into the night?

    Oh [game.player_name], I don't know!  I feel that what I am doing is right, I know it is what I should have done before.  I was sure it's what I have to do now.  But what if she's right?  What if, what if I'm wrong?  What if I am him and I must do what he did?

    I never...I never understood how brave he was, until now.
    """
    "There is a pause, but it dies with the Alderman's sobs."
    menu:
        "Who was it, who was brave?":
            #{Slight like, attraction and respect increase with the Alderman}
            $c=6

        "What are you talking about?":
            #{Very slight like, attraction and respect loss with the Alderman}
            $c=6

        "Pull yourself together, you're our leader, you can't be seen crying in the back of the inn":
            $c=9



if c==6:

    alderman  """

    My brother.

    I was supposed to pack all the supplies but mum...mum was hurrying us and I...I…

    I have always known he was brave.  I can't count the times I wish, I wish I'd done it first.  He was older, he was leading us, but I should have thought...

    He was going to be a greater man then I have ever been.

    But even knowing how brave he was, I've always still wondered, even though I've done the sums a thousand times in my head, if we could #{i}both#{/i} have made it back.

    Now, now when I feel it's my turn, now I can't imagine that he made a mistake.  He looked at the numbers and he accepted what they told him.  I had not realised how brave that part of it was.  To accept that truth.
    """

    $ game.AldermanGrieved = True
    menu:
        "As far as I see it, it isn't about bravery.  It's about caring.  And I can tell how much you care.  So you'll do the right thing":
            #{Like and attraction increase with the Alderman}
            #(if $AldermanPlan = "Love")[{Slight respect increase with the Alderman}]
            $c=8

        "To me, it sounds like the best thing you can do to honour your brother is to live, like he wanted you to, and do the best you can for those others still here":
            $c=8
            #{Like, respect and attraction increase with the Alderman}

        "You failed your brother, now you're failing this town":
            #{Significant like and attraction loss with the Alderman}#{Respect loss with the Alderman}
            $c=7

        "You're right, your brother sounds very brave.  Perhaps it is time for you to follow his lead?":
            $c=7
            #{Like and attraction loss with the Alderman}


if c==7:

    #(if like or attraction is above a certain threshold)["The Alderman's teary eyes turn to you, hurt and confused.  But he shakes his head and looks away."](else)["The Alderman shakes his head, his teary eyes not surprised and not meeting yours."]

    alderman  "Hearing it said out loud, I realise, I realise..."

    """

    The Alderman finishes his drink and again rests his head in his hands, but this time it's different.

    He is no longer weeping.

    He is thinking.

    His eyes are cold when he finally turns them to meet yours.
    """

    alderman  """

    Hearing it said out-loud, I hear it how my brother would have heard it.

    He would have said that he did what he {i}had{/i} to do.  Just because for him, that was walking away, does not mean that it is the same for me.

    You're right.  I have been weak.  There are things that have to be done.  But leaving this town, when I know it and its workings better than anyone else, is not the answer.

    And neither is letting its people die.

    I must get back to my office.  And you should get back to work too, [game.player_name].  As Alina says, there is much to be done by people like you.
    """




if c==8:

    alderman  """

    I think you might be right.  

    I promised, on his memory, that I would always check the numbers.  Always check and check and check again.  

    No wonder I became a bureaucrat.

    I'm good at it.  The best in town.

    But I'm more than that.  I know this town.  I have all the records, all of them up here in my head.  And I know the people.  Alina has her economics degree, and I do respect that, but I know these people and I know this town.

    She doesn't know us.  She doesn't know how strong we are, but I do.  I've seen this town through good and bad.  I know that we come together and I know that when we do, we're far more productive than any of those city folk.

    We're made of different stuff and I have the records to prove it.

    Thank you [game.player_name].  I … I don't usually like becoming emotional.  I don't usually find that it helps me much.  But today I think it helped.  It and you.  And my brother."""
    
    if game.alderman.attract >4:
        #MM
        alderman "You have a way with it [game.player_name], something I haven't felt before.  It's … different."

        "The Alderman pauses, his cheeks flushing, his expression confused."

    alderman """
        
    I should get back to the office [game.player_name].  I've got a lot of thinking to do.  I fear Alina will not take no for an answer.  She has a strong Senate writ with her and I don't think she is at all afraid to use it.  

    It is funny, [game.player_name].  Knowing that I have the lives of everyone in Lotosk in my hands, the idea of treason doesn't sound too scary at all.
    """



if c==9:

    "At your words the Alderman snaps his head towards you as if he had forgotten that you were there.  His face is red and his eyes redder, but the tears stop flowing as soon as his vision clears and he fully processes your words."

    alderman  """

    You are right.  You are right.

    I am the leader of this town.  I shouldn't be here.
    """

    "As he says this, he surges to his feet."

    alderman  """

    I shouldn't be here weeping.  Tears never solved anyone's problems.  They don't get things done, and I have a lot I need to get done.  I have a town to run.

    I shouldn't be wasting my time second guessing myself.  I have made my decision.  I've seen it through this far, I will see it through to the end.
    """

    """

    The Alderman turns to you, as if surprised by your presence for the second time in as many minutes.

    His words are strong and bold.  His tear-stained face isn't.
    """

    alderman  "Thank you [game.player_name], for reminding me to pull myself together.  I...I have to move forward.  I can't sit here, wallowing in self indulgence.  

    I-I have to move forward.  Like he would have done."

    "His voice catches slightly on the last words, but he shakes himself and clears his throat."

    alderman  "I'm going back to my office now, [game.player_name].  To work.  Move on.  Put...put things in motion…"

    """

    His voice trails off, and he turns slowly, his shoulders hunched and tense.

    Holding the tears in as he walks away.
    """

    #{Like loss with the Alderman} #{Significant attraction loss with the Alderman} #{Very slight respect increase with the Alderman}  #{Set $AldermanGrieved = "False"}



return
