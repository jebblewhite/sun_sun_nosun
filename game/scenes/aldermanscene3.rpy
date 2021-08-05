# needs to be tied to the map
label aldermanscene3:
"The Alderman usually lets you continue with your work without oversight, after all that was his original plan for your job, but today he has called you in so that you can ‘act in an advisory role’."

alderman  "It’s good to see you [game.player_name].  You don’t mind that I asked you here, do you?"
menu:
    "I’d prefer to just get on with my own life....":
        $c= 1
        alderman  "Quite, well, I’m sorry.  I just don’t really have anyone else to talk to about this kind of thing, no-one unbiased that is.  I am sorry.  But hopefully that will change after today.

        Anyway, if you want to get on with it, we should just get on with it, shouldn’t we?
        """

        $ game.alderman.statchange("resp", -2) #{Slight respect, like and attraction loss with the Alderman}
        $ game.alderman.statchange("like", -2)
        $ game.alderman.statchange("att", -2)
        $c= 3

    "Not at all, I’m happy to help.":
        $c= 2

        alderman  "Marvellous.  Shall we get straight to it then?"

        $ game.alderman.statchange("like", 1) #{Very slight like and respect gain with the Alderman}
        $ game.alderman.statchange("resp", 1)
        $c= 3

alderman  """

I hope that you, and the town, will forgive me for this, but there have been certain things I have had the opportunity to do, but have until now put off in favour of other matters.

Most of them I can, and will, get to {i}myself{/i} soon, but there is one I wanted to ask your opinion on, since you have more opportunity to talk with people than I do.

The old tower, it’s an awkward space but it is right here in the centre of town and I think that we must be able to find a good use for it.  Currently it is used by Nat, who only uses the top floor for ringing his bells, as far as I can tell.

True, the space is very strange, and I would be surprised if anything above the ground level was stable enough for anyone to feel comfortable using it for any sustained period of time.  But I still think it would be a good symbolic gesture, to hand it over to someone who might be able to put it to use.

It is too small, and the walls too rounded, to make a good storeroom anyway.

Don’t you think giving it to someone in town is a good idea?

The question is then, of course, to whom should we give it?
"""
menu:
    "Fyodora could use the space for extra beds.":
        $c= 4
        if game.aldermanplan == "Love":
            $ textinsert = "Fyodora’s compassion to others deserves compassion in return, after all."
        else if game.aldermanplan == "Cunning":
            $ textinsert = "Not only will this be good for Fyodora, but her patients will also be aware that they, in part, also owe their lives to us."
        else if game.aldermanplan == "Pride":
            $ textinsert = "After all, is there any greater Lotoskan than our doctor, who fights for our lives every single day?"
        else:
            $ textinsert = ""
        alderman  """

        Yes, a fine idea.  I believe someone has mentioned to me already that Fyodora could use more space.

        I’m sure it will look … I’m sure it will do the town good, to see our wonderful doctor being given more space for her work.  Shows how much we really do care about the health of the people.

        Grand, thank you.  I shall offer it to Fyodora later today. [textinsert]

        """

        $ game.relchange(alderman, doctor, 1) #{Relationship gain between the Alderman and Fyodora}  
        $ game.aldermantower = "Fyodora" #{Set $TowerPlan = "Fyodora"}

        $c= 7


    "Joan’s tea club is currently taking up space in the inn, but I don’t think that they and the regulars get on too well.  You could give it to her?":
        $c= 5
        if game.aldermanplan == "Love":
            $ textinsert = "Joan has shown great care to those who need it most.  It is only fitting that we help her."
        else if game.aldermanplan == "Cunning":
            $ textinsert = "Giving the space over to the tea club, it’s actually ingenious, now that I think about it, because of how many people it benefits.  We’ll have the thanks of not just Joan’s group, but Henryk’s rowdier regulars as well."
        else if game.aldermanplan == "Pride":
            $ textinsert = "Giving the space over as a social landmark, it is the kind of thing that can bring all Lotoskans together."
        else:
            $ textinsert = ""
        alderman  """

        Joan’s tea group?  Yes, I’ve heard of it, I believe she’s tried to get me to join…

        It wouldn’t be my choice [game.player_name].

        But I asked you because you know more about these circumstances than I do and I will respect that.  I’ll talk to Joan as soon as I get the chance. [textinsert]

        """

        $ game.relchange(alderman, herbalist, 1) #{Slight relationship gain between the Alderman and Joan and Henryk}  
        $ game.relchange(alderman, innkeeper, 1)
        $ game.aldermantower = "Joan" #{Set $TowerPlan = "Joan"}

        $c= 7

    "Nat loves that space.  It’s too small for anyone else to use much anyway, let Nat keep it.":
        $c= 6
        if game.aldermanplan == "Love":
            $ textinsert = "Nat has given so much to this town, and to me.  This really is the least we can do."
        else if game.aldermanplan == "Cunning":
            $ textinsert = "Nat is a model citizen, in many ways.  Yes, this will set a good example."
        else if game.aldermanplan == "Pride":
            $ textinsert = "Nat is the mouthpiece of Lotosk.  He deserves his own offices."
        else:
            $ textinsert = ""
        alderman  """

        You think so [game.player_name]?

        I suppose it is a very small space, it couldn’t be used for much by anyone else anyway.  And I did bring you in here because you have more expertise in this area than I do.

        But mostly, it would be nice to do something good for Nat, wouldn’t it? [textinsert]
        
        """

        $ game.relchange(alderman, crier, 1) #{Relationship gain between the Alderman and Nat}  
        $ game.aldermantower = "Nat" #{Set $TowerPlan = "Nat"}

        $c= 7

if game.aldermanplan == "Love":
            $ textinsert = "I worry that I, as a leader, do not reflect all of these beliefs.  I think that it would be good if I appointed an advisor, of sorts, who could help put me in the shoes, as it were, of those in town I do not know so well."
        else if game.aldermanplan == "Cunning":
            $ textinsert = "I think it would look good if I were to choose an advisor, of sorts, but someone who could otherwise be ideologically problematic.  A way to throw any dissenters a bone, as it were."
        else if game.aldermanplan == "Pride":
            $ textinsert = "I think it would be a good show of town unity if I were to choose an advisor, of sorts, but choose someone who represents a different way of thinking."
        else:
            $ textinsert = ""
alderman  """

Well, that was the main question I wanted to ask you, but while you are here I should get your opinion on another matter I have been considering.

Lotosk is a diverse town with many different beliefs.  [textinsert]

I’ve narrowed my choice down to three individuals.  To keep things pure, I think it would be best if I chose just one.

Elisabetta may be the most obvious choice.  True, her father and I worked together on many projects, it was necessary that we did, but since the sun has gone Elisabetta has been acting more strangely.  And people have been listening to what she’s been saying.  I think they are finding comfort in it.

Then again, there’s Elena.  Very intelligent and straight-talking.  She doesn’t represent an agenda, as far as I can tell, but will also say exactly what she means, what she thinks will be best for us all.

And then, of course, there is Mik.  I don’t think many people around town agree with much of what Mik says, but there is no denying that they and I think very differently.

So, [game.player_name], I’ve narrowed it down to just three, but I want you to make the final decision.
"""
menu:
    "Choose Elisabeta.  No-one understands the night as well as she does.":
        $c= 8
        alderman  """

        Yes, that makes sense.  She has embraced our new world like no-one else has.  It would be good to have someone who is thinking about this as more than just a disaster.

        Some positivity could very well be a good thing.
        """

        $ game.relchange(alderman, landowner, 1)#{Relationship gain between the Alderman and Elisabetta}  
        $ game.aldermanadvisor = "Elisabeta"#{Set $Advisor = "Elisabetta"}

        $c= 11

    "Choose Elena.  You’re right, she’d be the best advisor.":
        $c= 9
        alderman  """

        Yes, that is what I thought.  I think her reputation is well known enough that people will know that she is giving me honest council.

        It will be good having another critical mind thinking through the problems I face.
        """

        $ game.relchange(alderman, widow, 1) #{Relationship gain between the Alderman and Elena}  
        $ game.aldermanadvisor = "Elena" #{Set $Advisor = "Elena"}

        $c= 11


    "Choose Mik.  Everyone would be better off if more people listened to their ideas.":
        $c= 10
        if :$c= 10:

        alderman  """

        Indeed…  Well, I suppose there’s no one better to reach out to than the person who disagrees with you the most.  I’ve heard Mik is an intelligent person, if a little fanatical.

        Besides, they’re city name through and through.  It will be good to have someone around to remind me of the little time I spent in the Senate.
        """

        $ game.relchange(alderman, butcher, 1) #{Relationship gain between the Alderman and Mik}  
        $ game.aldermanadvisor = "Mik" #{Set $Advisor = "Mik"}

        $c= 11

if game.alderman.resp >= placeholder3:
    textinsert = "And I’m so glad I can speak openly around you."
else:
    textinsert = ""
alderman  """

Well [game.player_name], that’s all I wanted to discuss with you.  Thank you so much for coming.  I know that you’re very busy, and I know that much of that is my fault.

So thank you.  Your advice is invaluable.

[textinsert]

Anyway, we had both best get back to work.  But thank you again.
"""

$c=0





return
