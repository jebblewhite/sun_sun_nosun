label aldermanscene1:
    """

    The Alderman’s maid, who is also his secretary, lets you into the town hall and tells you that the Alderman is in the meeting room upstairs.  

    You take the stairs and push open the double doors to see the Alderman slumped in a chair at the head of the table, looking mournfully at the spread of books, charts, and other assorted pieces of paper that cover every inch of the table.

    He smiles thinly as you enter the room, lazily motioning for you to take a seat.
    """

    alderman  """

    I’ve been working on these for a few days now.  I wanted to make absolutely sure, so I pulled out every record I could get my hands on.  There’s so much that I couldn’t fit it all on my desk, so I had to come in here for the larger table.

    But I needn’t have bothered.  It tells me what I knew all along.

    Productivity is down.  It’s not just that the farms have stopped producing, or that Cynthia and Edward’s group left.  I’ve run the numbers, and {i}individual{/i} productivity is down.  The people simply aren’t working as hard.

    And I don’t understand.  Now is the time we need to pull together and work harder than we’ve ever worked before.  

    We need more wood now, to keep the cold at bay, than we have at any other time on record. The same goes for pelts.  Without operating farms we also have more call for hunters, foragers and fishers.  And I am sure that Fyodora is looking for medicine, which likely will require getting herbs to Joan.

    Yet the people are just simply working less hard than they ever have before.

    Why?
    """
    menu:
        
        "Likely people are stockpiling for themselves, rather than sharing with the community, so it just looks like they’re less productive":
            $ c=1
            alderman  "Really?  You think so?  Well what do I do about it?"
            menu:
                "Show them that you’re a capable and fair leader and that you have a plan which they can trust to do the right thing with their resources":
                    $ game.alderman.statchange("resp",2) #{Slight respect gain with the Alderman}
                    $ c=22

                "Show them that you’re a strong leader and that if they don’t do the right thing there will be consequences":
                    $ game.alderman.statchange("resp",-2) #{Respect and like loss with the Alderman}
                    $ game.alderman.statchange("like",-2)
                    $ c=16

                "Show them that you’re a compassionate and caring leader, and appeal to the people’s natural kindness":
                    $ game.alderman.statchange("resp",-2) #{Slight respect loss with the Alderman}
                    $ c=4


        "People are scared":
            $ c=2
            alderman  "I suppose that scared people are less reliable.  But what do I do about it?"

            $ game.alderman.statchange("resp",-1) #{Very slight respect loss with the Alderman}
            menu:
                "Give them direction.  Show them that you have a plan, that you can guide them through":
                    $ game.alderman.statchange("resp", 1) #{Very slight respect gain with the Alderman}
                    $ c=22

                "Make them turn their fear into productivity.  Show them that you’re strong, and let them know the consequences of being weak":
                    $ game.alderman.statchange("resp",-2) #{Respect and like loss with the Alderman}
                    $ game.alderman.statchange("like",-2)
                    $ c=16

                "Be compassionate and caring.  Reach out to them as a person, show them that you’re going through the same thing":
                    $ game.alderman.statchange("resp", -1) #{Very slight respect loss with the Alderman}
                    $ c=4



        "Have you considered that people are doing different jobs, so are using different skills?  We’ve lost the benefits of specialisation" if game.playerbackground == "merchant":
            $ c=26


        "The people don’t know what they should be doing.  So they do nothing":
            $ c=3
    if c==3:

        alderman  "So I need to give them direction?  But what direction?"

        $ game.alderman.statchange("resp", 1) #{Very slight respect increase with the Alderman}
        menu:
            "Logical direction.  Show them that you have a plan, and make them understand that that plan shows that the clever thing to do is to work hard":
                $ game.alderman.statchange("resp",4) #{Respect gain with the Alderman}
                $ c=22
                jump label22
            "Be strong.  Don’t just give them direction.  Tell them to work.  Force them to work":
                $ game.alderman.statchange("resp",-4) #{Respect and like loss with the Alderman}
                $ game.alderman.statchange("like",-4)
                $ c=16
                jump label16
            "Show them love.  People are thinking of this as about resources and organisation.  But if they think of it as being about helping each other and fraternity, they’ll know what to do":
                $ game.alderman.statchange("resp",-4) #{Respect loss with the Alderman}
                $ c=4
                jump label4
    label label4:
        if c==4:

            alderman  """

            You think that it can all be solved with care and love?  Perhaps in part you are right.  But I’ve seen a great deal in my days, and a great deal more of politics than I ever wanted to, and I can tell you that love will only ever get you so far.  

            The Republic wasn’t built on love, it was built on self-interest.  It was built on the backs of smart people doing what they wanted to do.  That’s what you discover when you spend time on the Senate floor.  Love dies quickly in that building.

            But it was that Senate that won us the war.
            """
            menu:
                "Surely it was the soldiers who won the war, not the Senate":
                    $c=5

                "But doing things for those you love is in your self-interest.  You can value people just as you value material things":
                    $c=11
                    alderman  "Yes, of course that is true.  But surely you recognise that not everyone cares about everyone else.  They care about {i}their family{/i}, so they will prioritise them, surely?"

                    $ game.alderman.statchange("resp", 2) #{Slight respect gain with the Alderman}
                    menu:
                        "They don’t have to care about everyone in the world.  Just those in town name":
                            $c=13
                            alderman  "Oh, I see.  You're saying that it's always going to be 'us versus them', but that the smart thing to do would be to change who the 'us' and 'them' are?"

                            $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}

                            $c=25


                        "But in a practical sense everyone can be useful to everyone else.  A clever person would choose to protect everyone":
                            $c=14
                            alderman  "Yes, yes that is certainly true.  I am sure that some folk would have thrown out Joan, just as an example, but we'll all be begging for her medicine soon enough.  You never know who is going to be useful."

                            $ game.alderman.statchange("resp", 2) #{Slight respect gain with the Alderman}

                            $c=28


                        "They need to be reminded that when someone dies, we all lose something: a potential friend, or lover":
                            $c=12
                            alderman  "Ah, still on love are you?  But I suppose, when you put it like that, it makes more sense.  It {i}is{/i} practical, in a way."

                            $ game.alderman.statchange("resp", -1) #{Very slight respect loss with the Alderman}  #{Like gain with the Alderman}
                            $ game.alderman.statchange("like", 2)
                            $ c=29


                "We can do better than the Senate.  We can show that we can be stronger with love":
                    $c=15
                    alderman  "I like your faith in me."

                    "The Alderman sits, clearly deep in thought for a moment."

                    $ game.alderman.statchange("resp", -2)#{Slight respect loss with the Alderman} #{Very slight like gain with the Alderman}
                    $ game.alderman.statchange("like", 1)
                    $c=29


    if c==5:

        alderman  """

        That is true, yes.  But it was the Senate who guided the army, the Senate who kept it better equipped than the Kingdom’s forces.

        But to follow your reasoning, I suppose it was the soldiers on the front line who won us the war.  And I suppose what made them fight was duty…
        """

        $ game.alderman.statchange("resp", 1) #{Very slight respect gain with the Alderman}
        menu:
            "Isn’t duty a kind of love?  Love for one’s country and the people who live in it?":
                $ c=6
                alderman  "I suppose it is."
                $ c=29

            "They didn’t fight for duty, they fought because they had to.  Or because they were being paid":
                $ c=7
                alderman  "So not for love either then?  They were chasing the carrot?  I suppose something like that could work."

                $ game.alderman.statchange("resp", 1)#{Very slight respect gain with the Alderman}  #{Slight like loss with the Alderman}
                $ game.alderman.statchange("like", -2)
                $ c=28


            "Forget love then, show the people that it is their duty to help others":
                $c=8

                alderman  "You mean force them?"
                menu:
                    "No, just appeal to their sense of civic pride":
                        $c=10
                        alderman  "So somewhere between love and self-interest, I suppose."
                        $c=25


                    "Yes.  They’ll only act if you make them act":
                        $c=9
                        alderman  "So show them the stick?"
                        $c=27



    label label16:
    if c==16:

        alderman  """

        I don't like this talk of forcing, and consequences.  Firstly, Player, I'm not strong.  We both know that.  If I was, do you…

        No, I'm not strong.  But secondly, I refuse to force anyone.  If I was willing to, I would already have become the despot that Cynthia wanted me to become.  The people of Lotosk are free.  

        I am the Alderman of this town, and I am here to protect the people, not enslave them.  And I am also, in a way, a member of this Republic's Senate, a Republic which has fought hard for the freedom of its people.

        I will not become a dictator.  I...I cannot become a dictator.
        """
        menu:
            "Then the people of this town will die":
                $c=27

            "Then don't be a dictator.  Just act as if you could be one.  Pretend that their freedom is on the line, so that you can protect it":
                $c=17
                alderman  "But how would I even do it?"
                menu:
                    "You talk about the freedom of Lotosk as something that is under threat.  Say it is people's duty to work for that freedom":
                        $c=19
                        alderman  """

                        I suppose.  I suppose that that could work.  It's not manipulation either.  It really is people's duty to work for their freedom.  Just like it was the duty of our soldiers to fight for our freedom in the war.

                        Yes, the people will do their duty.  They were proud of our soldiers during the war.  They will still be proud of the people of Lotosk now, even if the fight we're fighting is very different.
                        """
                        $ game.alderman.statchange("resp", 2) #{Slight respect gain with the Alderman}
                        $c=25

                    "By being the dictator, just once.  Use what power you do have to force people to do what is needed":
                        $c=18
                        "The Alderman sits stroking his beard for a few moments, then lets his hand drop and his body fall back into his chair."
                        alderman  "I appreciate that you think that this is for the best, and I appreciate that you listened to me.  But I can't do it.  Even once.  I'm sorry.  But I have to do what I think is right.  And what I think is right is freedom."
                        $ game.alderman.statchange("resp", 1) #{Very slight respect gain with Alderman}
                        $c=28


            "If you can't lead with strength, then do what you can and set a good example":
                $c=20

                alderman  "But how do I do that?"
                menu:
                    "By showing them love":
                        $ game.alderman.statchange("resp", -4) #{Respect loss with the Alderman}
                        $c=4
                        jump label4

                    "By showing them what a person can achieve when they do all the right things.  Maybe use my position as an example":
                        $c=21

    label label21:

    if c==21:

        alderman  "Yes, yes I like that.  Show people the carrot."

        $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}

        $c=28

    label label22:
    if c==22:

        alderman  """

        Yes, I like that.  It's what I want to do.  Show them that I have this grand plan for how to fix what's going on.

        But I don't have a grand plan.  I know that free people working hard is what will get us out of this, but I don't know any more than that.  I don't have anything I can show them to prove it.
        """

        $ game.alderman.statchange("att", 1) #{Very slight attraction increase with the Alderman}
        menu:
            "You don't have to have a full plan.  If the people see you relying on the community for help, they'll know they can and should do the same":
                $c=23               
                alderman  "I'm sorry, but how will that work?"
                menu:
                    "You'll show that you care about them, you'll show them love and they'll return that love to each other":
                        $ game.alderman.statchange("resp", -4) #{Respect loss with the Alderman}
                        $c=4
                        jump label4
                    "Make it a Lotosk matter.  Show that we all have to work together for the good of historic Lotosk.  We're not working for ourselves, we're working for the home of our parents and our children.   We're working for Lotosk":
                        $c=24
                        alderman  "Ah I see.  Turn to the community to show that this is bigger than any one of us.  It is a matter of heritage."
                        $ game.alderman.statchange("resp", 2) #{Slight respect gain with the Alderman}
                        $c=25
                        "The Alderman's brow furrows and he sits motionless, staring at a point just past you, until he suddenly jumps to his feet and starts shuffling through pages, muttering calculations under his breath.  Suddenly he stops."

                        alderman  "No.  No, I hadn't.  That might be it.  At least a large part of it.  It definitely explains discrepancies here, and there.  I'm not sure about this though…"

                        "He goes back to moving his finger along a line of figures, before he suddenly stands up straight again, as if he's just had an epiphany.  Instead of jumping up and down and shouting 'Eureka', though, he simply slumps back down in his chair."

                        alderman  """

                        I think you may be right Player.  I'm disappointed in myself that I had not thought about it before.  But it does not actually solve my problem.  

                        I thought that knowing why people were working less hard would help know how to work more, but if it is this, which in part I think it must be, it does not actually help.  People have to do different jobs now.  The farmers cannot farm, to take an obvious example.

                        Whatever the reason, we need to increase productivity.  And knowing why it has fallen, in this case, does not help us make it rise again.

                        I have to actually do something to make the people work.
                        """

                        $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}
                        menu:
                            "Show them that you're a capable and fair leader who has a plan":
                                $c=22
                                jump label22

                            "Show them that you're a strong leader and that if they don't increase their productivity there will be consequences":
                                $c=16
                                jump label16

                            "Show them that you're a compassionate and caring leader, and appeal to the people's natural kindness so they work harder for each other":
                                $c=4
                                jump label4


            "You did have a plan.  You empowered me.  Show them what a free, hard working individual can achieve":
                $c=21
                jump label21
    if c==25:

        alderman  """

        Civic pride.  Yes, I can see that working.  

        I've never known why people will work, and fight and die for that matter, for an ideal or a nation, when they wouldn't do it for a person.  Although I suppose they do, in the Kingdom.  Perhaps it is something that comes with our enlightenment as a republic?

        Never mind.  Pride.  Yes, people are proud of Lotosk.  And why shouldn't they be?  Asking them to work for the town, rather than themselves or their neighbours, that might just work.  

        I'm not comfortable about it.  Just between you and me I don't think it's a good reason.  People should work for things, not ideas.  But I've seen enough in city name to know that it will probably work.

        Thank you Player.  You've really helped me here.  I would offer you a drink, but I feel the need to start planning now.  I've spent too long staring at these pages without adding anything to them and I feel the need to get started.

        But again, thank you.
        """

        $ game.aldermanplan = "Pride" #{Set $AldermanPlan = "Pride"}

        $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}

        $c=0

    if c==27:

        alderman  """

        No, sorry, I'm not doing it.

        Actually I'm not sorry.  I should not apologise for refusing to motivate the people of this town to do the right thing by threatening them with force.  Force I do not even have.

        The people of Lotosk, the people of this Republic, are free.  We didn't sacrifice our freedom when threatened by the Kingdom, we're not going to sacrifice it now.  

        It's the smart thing to do.  The people will come around.  They need food and warmth.  They'll work hard for it, and they'll share because trade is beneficial.

        I just need to think of some way to persuade them of that, sooner rather than later.  That's what I have to do.  I need to find some proof in these numbers, something that I can use…
        """

        "The Alderman stands up and starts shuffling through the pages.  You are not sure if he is deliberately ignoring you.  If you try to speak to him, it becomes clear that he is.  You really have no choice but to leave."

        $ game.aldermanplan = "Cunning" #{Set $AldermanPlan = "Cunning"}

        $ game.alderman.statchange("resp", -4)
        $ game.alderman.statchange("like", -4) #{Significant respect and like loss with the Alderman}

    if c==28:

        Alderman  """

        Cleverness.  That's how we're going to get ourselves out of this.  Showing people the value to themselves of their own hard work.

        The people understand what they need to survive.  Some of them may just be confused as to how to get it.  We show them that the best way to gain materials is through hard work and co-operation.

        We get the people what they need by showing them how to get exactly what they want.  They want freedom and we'll show them how to use that freedom.

        We'll have to be careful to make sure that people realise that the best way to serve themselves is to serve each other, but it's the truth, so I do not imagine that it will be too hard.

        Thank you Player.  You've really helped me here.  I would offer you a drink, but I feel the need to start planning now.  I've spent too long staring at these pages without adding anything to them and I feel the need to get started.

        But again, thank you.
        """

        $ game.aldermanplan = "Cunning"  #{Set $AldermanPlan = "Cunning"}

        $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}

        $c=0
    if c==29:

        alderman  """

        Love.

        Love?

        You really think that the way through this crisis is love?  When people are starving and freezing to death, you think that love is what we need to survive this?

        It's not what I would think.

        But maybe you're right.  I've been sitting here for days trying to find the missing piece.  I would be a fool to simply disregard this.
        """

        "The Alderman stares at you for several moments."

        alderman  """

        I'm really not sure.  But I certainly have no better ideas.  So I'm going to trust you.  I want you to be right.

        I hope that you are right.

        Love.

        Thank you Player.  You've really helped me here.  I would offer you a drink, but I feel the need to start planning now.  I've spent too long staring at these pages without adding anything to them and I feel the need to get started.

        But again, thank you.
        """

        $ game.aldermanplan = "Love" #{Set $AldermanPlan = "Love"}
        $ game.alderman.statchange("resp", 4) #{Respect gain with the Alderman}

        $c=0



return
