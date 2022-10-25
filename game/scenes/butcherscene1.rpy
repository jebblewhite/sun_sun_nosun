label butcherscene1: 

"Mik is exactly where you expect to find them: in their butcher's shop.  They're at the counter, a rare occurrence as they usually spend most of their time in the back, and they look up lazily from the knife they were polishing as the bell above the door announces your entry."

butcher "Well hello there [game.player_name].  What's made you stumble into my web today?"

menu:
    "Excuse me?":
        $c=1
        "Mik smiles."

        butcher """

        You heard me.  """#Wink here

        butcher """

        You're a person of influence now [game.player_name].  And that means I've got some things to say to you, whether you want to hear them or not.

        I'd say pull up a chair, but this is a butcher's shop so why would I have a chair?
        """

        $c=4


    "I just wanted to chat.":
        
        #JE: IMPORTANT NOTE, THIS SHOULD NOT BE LIKE, IT SHOULD BE WHETHER 7 DAYS HAVE PASSED IN GAME OR ELSE.
        if game.butcher.like > 4:
            $textinsert = "I'll just choose to think the best of you and get the preliminaries out of the way now:"
        else:
            $textinsert = "Given that the time to celebrate your new appointment would have been, ooh, at least a week ago, I think I can safely assume it's not the second one.  But I'll go along and pretend that it is:"


        $c=2

        butccher """
        Oh isn't that nice.  I think it's best not to ask whether this is a 'just wanted a chat to make sure you aren't going to cause any problems' chat or a 'you're a dear friend to me Mik and I value everything we have' chat.

        [textinsert]

        My health is satisfactory, the darkness is yet to drive me mad, my clothes are just as bloodstained as ever and the society I live in is still despotic and corrupt.

        All I could ask for really.

        But you, things have changed for you, haven't they?  You're a bona-fide part of the system now, a crank or a valve at least, no-more a mere cog.

        I don't want to know whether you're proud of yourself.  Again, I shall make my own assumptions, which will save us both the time we'll need to talk about something of import.

        I've got some things to say to you, whether you want to hear them or not.

        I'd say pull up a chair, but this is a butcher's shop so why would I have one?
        """

        #(if day < 7 then)[{Slight like and respect increase with Mik}](else)[{Slight like decrease with Mik}]


    "Wanted to make sure that the business is running fine.  We need you to deal with all the animals the hunters bring back.":
        
        $c=3

        butcher  """

        Ah good, the rumours are true.  You're assimilated.

        I would ask you to tell me how it is at the top, but I'm worried that you might not be able to put it in words that I could understand.  We proles don’t have the same intellectual capacity as you divinely appointed slave drivers.

        A little harsh?  I'd apologise, but you came here for business and such civilities will just slow you down.

        So I'll tell you that this meat is doing fine.  It's doing everything you want it to.

        The carcasses you bring in are satisfactory too.

        Does that answer your questions?  Good.

        Now I've given you something, you have to give me something.  That's how your trades work right?

        You're going to stand right there and listen to me.  I've got some things to say to you, whether you want to hear them or not.
        """
        
        $game.butcher.like -= 4

        $c=4



butcher """
You are now a member of an oppressor class, but I doubt anyone has sat you down and told you your new responsibilities.  The Alderman would never be so gauche and Henryk is too much in denial of his own position.
So the job must fall to me to tell you all about your new found power, and how you are expected to abuse it.
But first, I think, I'll start with a little quiz.  Tell me, are you a member of the bourgeoisie?
"""
menu:
    "You think I am.":
        $c=5
        butcher "No, I do not.  Because you are not."

        $game.butcher.resp -= 1

        $c=12


    "What is the bourgeoisie?":
        $c=6
        butcher """
        Oh my word that is depressing.
        You are serious, aren't you?
        Well I'll get on to that in a second, but to answer my own question, no, you are not a member of the bourgeoisie.
        """

        $game.butcher.resp -=1

        $c=12


    "No, I'm a proletarian, just like you.":
        $c=7
        butcher "Interesting.  And how do you figure that?"
        menu:
            "I still work everyday.":
                $c=8
                butcher """
                Work does not a proletarian make.  The bourgeois 'work', wasting their privilege spending hours upon hours playing their money moving games.
                Besides, you're not actually bourgeois.
                """

                $c=12


            "I don't own any factors of production.":
                $c=9
                butcher """
                That is quite true, and therefore you are not a member of the bourgeoisie.
                But that does not make you a proletarian.
                """

                $game.butcher.resp +=2

                $c=12


            "I don't own any factors of production and I have not been given any actual political power.":
                $c=10
                "Mik scratches their chin."

                butcher """
                Interesting that you see it that way.  It narrows down which of the two stories that I've heard is true.  The one I had been assuming, out of kindness to you of course, was that the Alderman, lost and confused by the world, had appointed you as regent.
                The other, which I suppose I must endorse now that I find that you endorse it, is that you are merely his puppet.  The mask of the friendly face for the community that he cannot be bothered to wear himself.
                Still, if it is true that he's got his hand up your, ahem, posterior, and you are nothing more than his play thing, I'll answer the question for him rather than you, and hope that you deliver it back to him.
                You are not a proletarian.  True, you are not bourgeois, but that does not make you a proletarian.
                """

                $c=12


    "No, I'm a different kind of oppressor.":
        $c=11
        "Mik cocks their head slightly to one side, an eyebrow arching with surprise."

        butcher "Correct.  Maybe you will be an effective tool of subjugation after all."

        $game.butcher.resp += 4

        $c=12

butcher """
You are a statist, a bureaucrat, a part of the hierarchy of despotic slavers that we call a body politic, a government.
Your power derives from laws, from force, from the powers of traditionalism and nationalism.
It's a messy, simplistic form of oppression, but no less effective for that.  And, somehow, you manage to make it just as insidious.
But perhaps, for the sake of academics, we should go over the difference.
As I said, you are not a member of the bourgeois class, the other great oppressors of the proletariat.  You are not even, by necessity, aligned with them, although if you were sensible you would be.  They are, or soon will be, just as reactionary as you.
But I am getting ahead of myself.  {i}Private property{/i}.  It is from private property that the bourgeois derive their power.
And, just so we can be as clear as day, I don't mean houses.  I don't even mean land, although feudal lords and their public relations savvy-successors - the land owners - are just as bad as the bourgeois.  What I mean is {i}productive capital{/i}.
You've never been to the city have you?
This might take some time…
It shouldn't be new to you that people, in our society, need money to survive, correct?  And don't start with that charity nonsense, it's not enough and it never will be.
Well, money, or rather wealth, is not a static entity.  It can be created and destroyed.
Take this now deceased pig.  The progress of its life, from birth to maturity, was a process of wealth creation for us humans, specifically for its owner.  Before it was born, there was no bacon.  As it grew, there was more and more bacon.  
Since bacon is useful to us, we can sell it for money, just by the act of growing {i}the pig was producing wealth{/i}.
Humans can do the same.  Again, take this pig, although this time we'll consider it as a carcass.  A dead pig is, on its own, useless, just like ore is useless.  It needs to be put through a process that will turn it from a lump of dead flesh, bone, and a disturbing amount of faeces into the delicious meat that we all know and love.
And that's where I come in.  I put in work: I slice and I dice and I pull the poo out.  I create wealth, I carve bacon out of pig flesh.
It's what we, the proletariat, do.  We create wealth.  But I'm a lucky one.  I can afford these knives, so I can do the work without becoming a slave.  But those in the city are not so lucky.
You see, it hasn't reached us here in the frigid north yet, but the whole rest of the world has changed more in the last thirty years than it ever has before.  You statists have fallen, not totally but not insignificantly, and the whip you dropped has been taken up by the bourgeoisie.
And it's all because of technology.
If I'm in the city and I want to feed myself, and I was born a proletarian, then I must create wealth.  And with the invention of large-scale manufacturing machines, I can do so with very little skill.  Indeed, many of the machines in Alexisgrad are worked by children, although that may just be because they've had fewer opportunities to lose fingers.
Anyway, this low demand for skill means that any individual can do any job.  Which means that if any one individual demands, say, a position that won't kill him after six months of work, his paymasters can simply fire him and find someone more desperate.  A desperation that the first person will feel after six weeks starving on the streets.
Of course, what this also means is that the factory owners can pay their workers whatever they like, which is usually not enough for the workers to feed themselves after a long day sawing their own fingers off and breathing in smoke.
But, I like to assume you are about to ask, if the proletariat are creating wealth, why are they so poor?
Because they have no choice.  If you wish to create wealth, you must, now, do so with the aid of machines.  But these machines cost more money than the entire factory of workers who work them could ever dream to see in a lifetime.
So they are forced to work other people's machines.  Which gives the power to the factory owners, or, to use a fancier word, the bourgeoisie.  
These individuals inherited wealth and used it to buy capital, the non-labour materials needed for wealth production, and then used the high price of capital to force the labour they need to operate the capital to work for effectively no pay.  Which they will do because they have no other choice.
So we have two classes out-with the state.  The bourgeoisie: who inherited wealth and used it to purchase capital, which they use to strong-arm the workers into giving up their share of the wealth they created.  And the proletariat: who are forced to work for so little money that they barely have enough to afford food, never mind save up enough to become capital owners themselves.
The proletariat creates the wealth; and the bourgeoisie steals it.
Do you understand?
"""
menu:
    "I do and it's horrible!":
        $c=29
        label mik29:
        butcher """
        Ah yes, 'that's horrible'.  The most cutting admonishment known to human kind.
        Still, I shouldn't jest.  Just because the furnaces of Alexisgrad blasted away all of my human emotions, it doesn't mean that I should mock those innocents still bright eyed and ready to be shocked into an appropriate revolutionary zeal.
        So I will warn you, things only get worse.
        """

        $game.butcher.like += 2

        $c=30


    "I think so.  The bourgeoisie owns capital, and the proletariat creates wealth.  So what does that make you?":
        $c=13
        label mik13:
        "Mik narrows their eyes."

        butcher "What do you mean?"
        menu:
            "Well, you own this shop.":
                $c=14
                butcher "Ah, I understand.  But you are mistaken.  I don't.  I rent the premises from Elisabetta.  I must earn enough to repay her, so I must work."

                $game.butcher.resp += 1
                menu:
                    "But still, you set your own wages.  You could charge as much as you want for your meat.":
                        $c=15
                        butcher "I cannot charge whatever I want.  I must take in a minimum to pay my rent, and if I charged too much people would not buy from me.  Alas, the townsfolk will continue living without sausages."

                        $game.town_stability -=1
                        menu:
                            "But that doesn't make you a proletarian.  True the market controls your prices, but you still work for yourself, and, aside from rent, you receive most of the wealth you create.":
                                $c=16
                                butcher "True, I am much more fortunate than those of the city, but paying any rent at all still leaves me at at the mercy of capital owners.  I am still creating wealth for the bourgeoisie."

                                $game.butcher.resp +=2
                                menu:
                                    "But without their capital, you wouldn't be able to create any wealth at all.  Isn't it fair that Elisabetta takes her cut?":
                                        $c=18
                                        butcher """
                                        No, it's not.  Because it's not fair that Elisabetta has the capital in the first place.  Saying that Elisabetta deserves a portion of the wealth because of her contribution of capital is ignoring the fact that she has actually done nothing herself to produce the wealth.
                                        Now if this building were a thinking feeling thing that needed things like food to survive, then it would absolutely deserve its cut.  It has to put up with me after all.
                                        But Elisabetta has done nothing, made no sacrifices.  It is merely luck that she was born with the wealth necessary to buy this building.  She herself has done nothing to deserve a cut.
                                        """

                                        $game.butcher.like -=1
                                        menu:
                                            "The building doesn't need to eat, but it does need repairs.":
                                                $c=19
                                                butcher """
                                                A good point, but hardly a world shaker.  If my rent was all going to maintenance, keeping the masons of this town in work, then I would be happy to pay.
                                                But we both know it's not.
                                                Now, enough of this.  All this talk of the bourgeoisie was nothing but an illustrative point anyway.
                                                """

                                                $game.butcher.resp +=2

                                                $c=30


                                            "So it all comes down to effort and sacrifice?":
                                                $c=20
                                                butcher """
                                                If you want to put it that way.  I suppose you should, sounds much more noble than 'those who create the wealth should reap the wealth'.
                                                Now, enough of this.  All this talk of the bourgeoisie was nothing but an illustrative point anyway.
                                                """

                                                $game.butcher.resp +=2

                                                $c=30


                                    "Elisabetta takes some of your money through rent, and the town takes some of hers through tax.  We all have to pay for things we don't want to.":
                                        $c=17
                                        
                                        butcher "And here is where I get truly radical.  For while I think that rent is a form of exploitation, I also believe that tax is a form of theft."

                                        $c=30

                                    "You're right, you shouldn't have to give any money to capital owners.":
                                        $c=26


                            "You are right, you are still a slave of the market.":
                                $c=26


                    "Still, you said yourself you own your knives.  Aren't they a form of capital?  They are the only equipment you seem to need.":
                        $c=21
                        
                        butcher "Well I do need the premises.  Whatever else, Elisabetta is still taking a portion of the wealth I work hard to create."

                        $game.butcher.resp +=2
                        menu:
                            "Say I convinced Elisabetta to stop charging you.  Then you'd own, or not have to pay for, all the capital you need.  You'd be a member of the bourgeoisie.":
                                $c=22
                                butcher """
                                Well, I wouldn't be what we traditionally call bourgeois.  I wouldn't exactly be a big capital owner.
                                But you are right.  I would, technically, be a member of the bourgeoisie.  A petty bourgeois, but a bourgeois none-the-less.
                                But I don't see what that has to do with the plight of the city proletariat?
                                """
                                menu:
                                    "Nothing, it just makes you a hypocrite.":
                                        $c=23
                                        butcher """
                                        It's cute that you're trying to be clever.  But my personal position has nothing to do with the cause.  To suggest otherwise is an ad hominem, a fallacy, a failure of reason.
                                        Besides, I recognise my position, and how it relates to the revolution.  But we are getting dangerously off track.
                                        """

                                        $game.butcher.resp -=2

                                        $c=30


                                    "Nothing, their suffering is still appalling.":
                                        $c=24
                                        butcher "Yes, it is.  But to return to the topic we started so long ago, the bourgeois whip is not the only one which beats them."

                                        $game.butcher.like +=4
                                        $game.butcher.resp +=4


                                        $c=30


                                    "Everything.  If you could break out of it and become a near bourgeois, or a petty bourgeois, then they can too.":
                                        $c=25
                                        butcher """
                                        I see where you're trying to go with your reactionary logic, but you're wrong for two reasons.
                                        Firstly, I was lucky.  I managed to con my way into an apprenticeship, working under the weaker, and therefore more forgiving, heel of a petty bourgeois master.
                                        Secondly, such opportunities, and places such as this, are disappearing.  Or at least, they were disappearing, before the sun vanished.  I had thought nothing would stop the march of progress, and I choose the word 'march' very carefully, but I live in hope that the total disappearance of the sun may have been the trump card.
                                        Anyway, now that you know you are wrong, perhaps we can move on to the actual matter at hand.
                                        """

                                        $game.butcher.like -=2
                                        $game.butcher.resp -=2

                                        $c=30



                            "So it all comes down to who makes effort and the sacrifices?":
                                $c=20


                    "Oh, that explains it.":
                        $c=26
                        butcher "Good.  Then we shall move on to the actual matter at hand.  After all, the bourgeois whip is not the only one which beats the proletariat."

                        $game.butcher.like +=2

                        $c=30



            "Nothing, I'm just confused.":
                $c=26
                $game.butcher.like +=2
                butcher "Good.  Then we shall move on to the actual matter at hand.  After all, the bourgeois whip is not the only one which beats the proletariat."

                $c=30

    "Surely the people are their own enemy.  If they were all unwilling to work for so little, then they would have the power.":
        label mik27:
        $c=27
        "Mik smiles {i}at{/i} you - the same way one laughs {i}at{/i} someone - eyes hooded and slyly mirthful."

        butcher """
        Oh [game.player_name], it's impressive that you can be right, but also horribly, horribly wrong.
        Would the lot of the workers be better if they organised?  Yes, on average.  
        Of course, some may appear to be worse off, as an easy strategy of the bourgeoisie would simply be to make sure that there are always fewer jobs than there are workers.  But systems such as wage sharing could be instigated, those in work sharing a portion of their wages with those who weren't lucky.
        But there are still two main problems with unions: the philosophical problem and the practical problem.
        The practical problem is simply that if you can't even feed yourself, you're probably not in a position to put in the work required to unite the vast majority of thousands of workers.
        I defy you to find a true proletarian in Alexisgrad who has the raw energy required to form a union.  Not out of laziness, don't even think that, and not out of a lack of ability or spirit, but because the industrial proletariat are kept in worse conditions than this pig was.  They have as little freedom, but they still have to spend their entire lives foraging for the scraps they need to survive.
        Which leads neatly into the philosophical problem.
        'Why Mik', I hear you asking good naturedly, 'surely there must be some people in Alexisgrad able to organise the workers, even if it isn't one of the workers.'
        And I reply, condescendingly: 'ah, it's good to meet you my sweet, naive, ignorant little bourgeois socialist, go run along and suck on your mother's teat before you do any real harm.'
        Because harm is exactly what you would do.  If you're not a worker, then any union you set up would be based on an ideology.  And it doesn't matter how well-intentioned that ideology is, no social organisation planned from the top down will ever, can ever, be just.
        You will have created a miniature state, albeit one which wipes dirt on its face so it can say that it's 'here to help the people, honest'.
        Which brings us on to the next part of our lesson, I think.
        """

        $game.butcher.like -=2
        $game.butcher.resp +=2

        $c=30


    "The government should do something to stop this.":
        $c=28
        label mik28:
        butcher "Oh dear.  Oh dear, oh dear, oh dear."

        $game.butcher.resp -=2

        $c=30


    "Sorry, what's going on?  I just came in for a chat.":
        $c=52
        "Mik's eyes twinkle."

        butcher """
        This is an education.  This is one of your subjects invoking their democratic right to be listened to.  In minute, dry, technical detail, but if I'm correct your position rests on your reputation and your reputation lies on your ability to humour the townsfolk.  So you won't be walking away.
        Besides all that, this is actually important.  I'm very good at attributing actions to malice, but malice can only get so far without a strong culture of ignorance.  Everyone should know what I am attempting to teach you, but you are in a position of power.  You should be able to recite it in your sleep.
        You want me to know the fundamentals of my trade, you wouldn't trust me with your meat if I didn't, so don't question me when I try to check that you understand the basics of yours.
        Besides, I'll keep it short.
        No sorry, couldn't keep a straight face.  Get comfortable.  But I will just teach you what you {i}have{/i} to know today.  Trust me, I have {i}so{/i} much more, but at some point you would be justified in calling me a kidnapper if I forced you to listen to it all today, so we'll keep it to lesson one.
        Now, tell me, do you understand?  About the bourgeoisie, not about the fact that you are my prisoner here.
        """
        menu:
            "I do and it's horrible!":
                $c=29
                jump mik29
            "I think so.  The bourgeoisie owns capital, and the proletariat creates wealth.  So what does that make you?":
                $c=13
                jump mik13
            "Surely the people are their own enemy.  If they were all unwilling to work for so little, then they would have the power.":
                $c=27
                jump mik27
            "The government should do something to stop this.":
                $c=28
                jump mik28
            "No, really, I don't want to hear this.  I'm leaving.":
                butcher """
                Really?  I hadn't expected you to be so petty.  But fine, have it you're way.
                Get out of {i}my{/i} shop.
                That's right, you can't leave, I'm throwing you out!
                Don't ever be let it said that I didn't have the last word!
                """
                "Mik dismisses you with an extravegant wave of their hand and, if you don't immediately scurry away, a pointed look at a meat cleaver."
                $game.MikResult = 'Mad'
                $game.butcher.like -=4
                $game.butcher.resp -=8
                jump end_scene


if c==30:

    butcher """
    The bourgeoisie are not the only oppressors of the people.  The state is just as much of a slave driver.  Yes, even our glorious free Republic.  Our despot is wearing the mask of democracy, but it's just as bad as the King of The Kingdom.  At least {i}he's{/i} honest.
    To quote a good friend of mine: \"No state is capable of giving the people what they need: the free organization of their own interest from below upward, without any interference, tutelage, or coercion from above.  That is because no state, not even the most republic and democratic-\" 
    which, let's be honest ours isn't really, 
    \"-not even the most republic and democratic represents anything but government of the masses from above downward, by an educated-\"
    or sometimes not so educated, my friend was making a point there but in this instance it isn't necessary.  Don't think he was just being kind to our reactionary masters.  Anyway:
    \"-by an educated and thereby privileged minority which supposedly understands the real interest of the people better than the people themselves.\"
    In other words, any state, whatever flag it may wave and whatever nice words it might be able to point to in its constitution, if it even has one, is nothing but a paternal, privileged minority of the population free to exert any influence it wants over the rest.
    When I said that at least the King was honest, I really do mean to do him credit.  When he refuses anyone but men positions of political office, or demands that his subjects starve for a week each year so that they can do nothing but dance in his honour, he is clearly being despotic.  We know it, and his people know it.
    But {i}our{/i} government?  They are much cleverer, and therefore much more insidious.  When they tell us what to do, they say that it is for our own good, and since they're all career politicians who have spent their lives training in sophistry, it is much harder to see that they're just as despotic as the king.
    You see, the problem is that our government tells us that it, or its constituent members, represent us.  But do you see the problem there?
    """
    menu:
        "They represent us but they aren't us.  They don't know what we actually want.":
            $c=36
            butcher "Exactly right [game.player_name].  Maybe I have underestimated you."

            $game.butcher.like += 4
            $game.butcher.resp += 8

            $c=37


        "They don't actually have to represent us, so they don't.  We may have a constitution, but if they break it, what is going to happen?":
            $c=35
            butcher """
            Interesting.  Anti-statist and considered.
            I may have underestimated you.
            What you're referring to is a specific instance of the problem of power, but in this instance I was referring to a different problem.
            """

            $game.butcher.resp += 4
            $game.butcher.like += 4

            $c=37


        "They're lying, they don't represent us.  All politicians are corrupt, so even if we vote, all our options are self-interested liars.":
            $c=31
            "Mik smiles at you."

            butcher """
            Maybe I've underestimated you.  Your zeal is admirable, but you have one or two things to learn about tactics.
            Never call your opponent a liar, unless you have solid, direct, relevant proof.  
            On the one hand there are libel laws, and there are so many more worthwhile things to get arrested for, and on the other hand people just don't like it when you call them liars, even if it's true, and when people aren't happy they don't listen properly.
            When you've got the truth on your side, and in politics {i}only{/i} when you have the truth on your side, you {i}have to{/i} make sure people listen.  So you have to be very, very careful about what you say and even more careful about how you say it.
            But back to the matter at hand.  You've successfully touched on the problem of power there, which I was going to move on to in just a moment.
            """

            $game.butcher.like += 4
            $game.butcher.resp -= 1

            $c=37


        "There is no problem.  We need a government to stop us sliding into anarchy.":
            $c=32
            "Mik stares at you for an uncomfortably long time."

            butcher """
            I think you might be missing the point.
            Let's start again.
            Hi there [game.player_name], I don't think we've met before, but I'm Mik, the town anarchist.
            Yes, [game.player_name], if we don't have a government we will slip into anarchy.
            That's rather the point.
            It's exactly the point.
            Maybe I should just continue my little sermon.  And yes, I'll call it a sermon, since you're going to think of it as one anyway.
            """

            $game.butcher.like -=2
            $game.butcher.resp -=2

            $c=37


        "The problem is that they can't satisfy all people all the time.  But that's life.  If we want the benefits of living in a society, then you have to grow up and accept compromise.":
            $c=34
            butcher """
            Ooh, getting catty are we?  I like to see someone get fired up.
            You are not wrong.  Not being able to satisfy all the people all the time is indeed a problem, but it is also one we cannot deal with.
            Like we all have to deal with the problem of our own faeces, we must all deal with the problem of compromise.
            However, in this case, that wasn't the problem I was referring to.
            """

            $game.game.resp += 1
            $game.game.att += 2

            $c=37
    butcher """
    The answer is that, while they may represent us, the politicians who fill our Senate are but a tiny minority of individuals.  There is a large divide between {i}us{/i} having the power and {i}our representatives{/i} having it.
    Even if we ignore the problem of power, which I will move on to in a moment, and yes I can see that you may want to leave and get on with your day but I want a free and equal society so it looks like we both have to put up with things we don't want, the ideal representative is still no substitute for the people they represent.
    A textiles worker, impassioned about the working conditions of his fellows, would still not know what would be best for his fellow iron refiners.  Or the women he works beside.  Or even his friends, who have different personal dreams from him.
    Can you argue with the suggestion that, while we may not all know what we want, we have a better idea than anyone else does?  And that in a truly free and just society, we could pursue our own goals, rather than being told what to do, where to go and what to think by a minority who will never know us as well as we know ourselves?
    """
    menu:
        "You're right, we need the freedom to make our own choices.":
            $c=41
            butcher """
            Good, I'm so glad you can see the obvious.
            But it gets worse.
            """

            $game.butcher.like += 2

            $c=42

        "You're wrong, many of us don't know what's best for us.  Like pacifists.":
            $c=38
            "Mik laughs, an ugly, honking, aggressive laugh.  You think they might be putting it on."

            butcher """
            Oh you are funny.  Who needs a draft when we have fine rabid nationalists like you to go and die on the front lines in the names of our country for us?
            If individuals care about the war, they'll fight.  If they don't, forcing them to fight is … well it's worse than either slavery or murder.  It's worse than both.
            It is so bad I don't feel I even have to justify myself to you.
            """

            $game.town_stability -=1

            $c=42


        "You're wrong, many of us don't know what's best for us.  Like alcoholics.":
            $c=39
            "Mik tilts their head to the side for a moment, clearly thinking."

            butcher """
            That is a … good point.  What you said is true, but I don't think that state action is the answer.  Abolition just drives things underground.  
            No, the answer there would be a caring, but free, society where alcohol was in no way restricted, but alcoholics are helped by the community and those who care about them to overcome their addiction.
            Anyway, alcoholism, and many similar conditions, are symptoms of greater psychological and social ills.  If we fix the society, we will have done much more good than a state ban on alcohol, or something similar but perhaps less extreme, like good old tax, would do.
            Any other thoughts, or shall we do the sensible thing, assume that I am right, and move on? 
            """
            #Wink here
            $game.butcher.resp += 2

            $c=42


        "You're wrong, many of us don't know what's best for us.  We should trust certain things to experts: sociologists, economists and statespeople.":
            $c=40
            
            "Mik raises an eyebrow and a finger, and smiles.  However, once they've opened their mouth they close it almost immediately again, clearly reconsidering something."

            butcher """
            You're wrong I'm afraid.  Relying on experts is playing with fire.  I could tell you why, but doing so would take longer than even {i}I'm{/i} willing to give to this … discussion.
            So I'll tell you what, we'll table this for now, I'll finish what I was going to say about your role as a statist pig today and you come back to see me some other time soon and we'll get into this in more detail.
            Okay?
            Good.
            """

            $game.butcher.resp += 1

            $c=42

    butcher """
    The problem is not simply that this minority does not understand the will of the people, but that any minority will never be able to understand the will of the people.
    It is that states are inherently reactionary.  Institutions can, and indeed do, develop their own consciousnesses.
    But anyway, institutions arise out of specific circumstance, and it is in {i}those{/i} circumstances that they flourish best.  Why else would they have grown then and there?  
    Institutions, once they have lasted at least a little time, develop a human-like desire for survival.  Why?  Because every institution exists for the benefit of someone.  The monarchy for the king, the republic for the senators, the businesses for their owners.
    Even charities, either for their board of directors if they are corrupt, or for their beneficiaries if they are not.
    An institution that does not benefit anyone would never have come into existence in the first place.  Can you imagine devoting time and effort into creating a business that nobody, including yourself, wants?
    So institutions, because there are members of them who benefit from their existence, even if those specific individuals change over time, develop a desire to survive.  But this desire is often at odds with an ever-changing world, which is always threatening to make those ideal circumstances, present when the institution was formed, a thing of yesterday.
    Small institutions can adapt.  This is why the position of the petty bourgeois has changed little in the shift from pre-industrial to industrial production.
    But large, old, bloated institutions are not so easily changed.  And what is larger, often older, and more bloated than any other institution?
    Yes, ring the bells, you've won the prize: it's states!
    So what can the state do if it cannot adapt?
    It can adopt reactionism and make sure that those ideal conditions never do go away.
    Like the rings of a tree, you can read the age of a state by its level of despotism.  As the strain of change pushes more and more against the state, it must become more and more ruthlessly conservative in order to maintain its relevance.
    It is why our Republic is not – yet - quite as ruthless as the Kingdom.  It has not had the time to ferment.
    But give it a chance and we'll all be scraping in the dirt when the Dictator rides by.
    """
    menu:
        "But states change all the time, there are constantly reforms and new laws.":
            $c=46

        "Wait, are there no good senators?  Has power corrupted all of them?":
            $c=44
            butcher """
            It is not so much about 'good' and 'bad', nor is it about individual senators.  It's about inevitabilities.  The state, as an entity, will protect itself.
            There is a small handful of 'good' senators.  Ex-workers mostly, or bourgeois socialists.
            Communists to a man.  All of them making the mistake of engaging with the social problem on a political level.  And all of them red-blooded statists.
            Socialists, yes, collectivists, usually.  But they see only the bourgeoisie as their enemy, and see the state, a state they would grow and nurture, as their liberator.
            They … No.  I've taken up enough of your time without ranting about communists.  I'll rip those idiots apart some other day.
            """

            $game.town_stability +=1
            menu:
                "If the communist senators want to empower the state, what about those liberal senators who want to weaken and reduce it?":
                    $c=45
                    butcher """
                    Ah, the liberals.
                    Cockroaches.
                    They're not statists at all.  They're spies.  Bourgeois spies.
                    They're just as reactionary, just for another cause.
                    A good question though, even if it does have a simple answer.
                    """
                    
                    $game.butcher.resp += 2
                    menu:
                        "Okay.  But states change all the time, there are constantly reforms and new laws.":
                            $c=46

                        "Okay.  That's why power corrupts.  Because people want to keep power, but unless they let it corrupt them, things will change and they'll lose it.":
                            $c=43




                "Okay.  But states change all the time, there are constantly reforms and new laws.":
                    $c=46
                    


                "Okay.  That's why power corrupts.  Because people want to keep power, but unless they let it corrupt them, things will change and they'll lose it.":
                    $c=43



        "That's why power corrupts.  Because people want to keep power, but unless they let it corrupt them, things will change and they'll lose it.":
            $c=43
    if c==43:
        butcher """
        I think you're getting somewhere [game.player_name]!  I hadn't thought about it in those words before, but it's good.  
        Much, much more concise than how I put it.  In the spirit of collectivism, which we'll cover another time, I think I will steal it.
        But I'll at least be gracious and say thank you.
        """

        $game.butcher.like += 4
        $game.butcher.resp += 4

        $c=47
    if c==46:
        butcher """
        Oh the details don't matter.  The individuals don't matter.  States create power where there should be none.  In a just society, we would not have oppressors, but the mere existence of a state means that there is a potential for some individuals to have power over others.
        So there will always be someone who either holds that power, and does not wish to let it go, therefore maintaining the state, or someone who is about to seize it, who would hardly put in all the work just to see all that power disappear.
        So the particular flavour of despotism may change from day to day as the politicians play their games, but the irresistible marrow, the oppressive nature inherent to all states, will never disappear.
        Well, not without a revolution anyway.
        """

        $game.butcher.resp -= 1

        $c=47
    if c==47:

        butcher """
        Moving on, however, we reach our last - and for the sake of novelty also least - point: taxation.  Private property is antithetical to justice, but I still feel confident in asserting that tax is theft.
        The workers create, or wish to create, wealth.  The bourgeoisie steals that wealth by using their exclusive access to capital to hold it hostage.
        The state is much more direct.  They just take it.
        """
        menu:
            "You're right, tax is theft, we deserve to keep everything that we make.":
                $c=49
                butcher """
                I think there might have been a slight misunderstanding, but I do not think now is the time to delve into it.  There is also some … disagreement about that sentiment.
                I argue with myself about it regularly.
                But now is not the time for that debate.
                """

                $game.butcher.like += 2

                $c=51


            "What about all the good that taxation does?  Couldn't tax be used to redistribute wealth?":
                $c=48
                butcher """
                I see my lessons are working, you're thinking like a good statist, and not only that, you're dressing it up with bourgeois socialism.  Very clever.
                But to answer your question, yes it could, but that is beside the point.
                Abolish private property, collectivise the capital and access is no longer an issue.  If the means of production belong to everyone equally, all can work, all can share in the fruits of labour and, given that basis of equality, redistribution, which actually rarely happens when the tax could instead go to lining the pockets of senators and generals, is no longer necessary.
                But as an obedient statist, you don't need to know any of this.  Your job is to conserve the status quo.  Thinking about alternatives is dangerous.  
                """
                #Wink here

                $game.butcher.resp -= 1
                $game.butcher.like += 1

                $c=51


            "No taxes, no army.  And then we'd be at the mercy of foreigners.":
                $c=50
                butcher """
                I see my lessons are working, you're thinking like a good statist.  There is only one way, and it is the way of the state.
                Pacifism is bad, but the only thing that's worse are those filthy foreigners, eh?
                Really, get a grip.
                """

                $game.butcher.like -= 4
                $game.butcher.resp -= 2

                $c=51
    butcher "I think we can conclude our lesson there.  Do you understand your role now?"
    menu:
        "I understand that you're completely mad.":
            $c=53
            "Mik holds up their hands and smiles."

            butcher """
            Nice comeback there.  Very intellectual, truly beautifully thought through.
            Why do I bother?
            I don't give a shit what you think.  I'll just take it as a compliment, that the only way to discredit my ideas is to pull out a completely arbitrary ad hominem.
            You're going to do what you want, you're going to think what you want.  
            Go on then.  Fuck off.  Don't waste any more of your time talking to a mad person.  People might start to talk!
            Idiot.
            """

            "Mik dismisses you with a wave of their hand and, if you don't immediately scurry away, a pointed look at a meat cleaver."

            $game.butcher.scene1result = 'Mad'
            $game.butcher.like -= 8
            $game.butcher.resp -= 2
            $game.butcher.att += 1



        "I understand what you are saying, but I don't believe that everything you've said is true.  Yes, there are problems with the system, but there are benefits that you are ignoring too.":
            $c=54
            "Mik sucks in the sides of their cheeks."

            butcher """
            Oh I hate it when they're reasonable.
            You're wrong.  But I concede, you've listened.  And you've thought.  Which, really, is more than I could have hoped for.
            We'll talk more, if you want?  I want you to go away and have a good think.  I've just fed you a banquet, you should digest a little.  
            And … and I will try to pry my mind a little open to what you may have to say.  You've done it to me - and even though I know I'm right - I'll try to return the favour.  
            Stop by my again whenever you feel like your ears are a little empty.
            I look forward to a proper round two.
            """

            $game.butcher.scene1result = 'Disagree'
            $game.butcher.like -= 2
            $game.butcher.resp += 4


        "You're dangerous, Mik.  There are things we need to protect ourselves from, but you'd just tear down all the things that make us safe and powerful.":
            $c=55
            "Mik shakes their head, and then stares you straight in the eye."

            butcher """
            Good.  I know where you stand.
            I learnt a long time ago that my dream will never be more than that.
            But if I'm wrong, if this night does lead to what I wish it might lead to…
            I'll know who my enemy is.
            I believe in the rationality and goodness of people.
            But some are beyond saving.
            I'll see you again, come the revolution.  Then I'll show you how dangerous I really can be.
            """

            $game.butcher.scene1result = 'War' 
            $game.butcher.like -= 8
            $game.butcher.resp -= 8


        "I think you're completely right Mik.  We need to do something about this!  We need a revolution!":
            $c=56
            "Mik tries to keep their smile sardonic, but fails."


            butcher """
            I'm slightly worried that you've come around so fast.  But maybe Alexisgrad just made me doubt the true power of truth.
            So welcome.  We have much more to talk about.  And then, maybe, with time, we can start to plan.  But there is much you don't yet know.  There is much we haven't yet talked about.
            So patience.  I've waited years, you can wait a little longer.  But keep it all in mind.  And look around you.  Internalise the truths.
            And we'll talk again.  Come again.  Later.  I need to breathe a bit first.
            """

            $game.butcher.scene1result = 'Revolution' 
            $game.butcher.like += 8
            $game.bucher.resp -= 1

return
