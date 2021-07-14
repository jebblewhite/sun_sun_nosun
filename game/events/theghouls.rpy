# requires 20 people dead at least -make this conditional

label theghouls:
    image woodssky = im.Scale("woodssky.png", 3072, 1920)
    image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
    image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
    image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)
    
    show woodssky onlayer skyback
    show woodsdeepest onlayer farfarback
    show woodsdeeper onlayer farback
    show woodsdeep onlayer back

    "???"  "Fucking ‘ell, will you look at that one!"

    """

    It’s not a voice you recognise, of that you are instantly certain.  Not only is it unfamiliar, but it is also too high pitched, too strained to be entirely comfortable, entirely healthy.  

    The second voice you hear, also coming to you from the direction of the graveyard, is also unknown and unnatural, but this one is deep, phlegmy and slow.
    """

    "???"  "I’m tryn’ to look Inky but there’s so little of it there’s nothing to see!"

    "The voice laughs at its own comment and is joined by another sound, an inorganic dry rasping.  The fist voice, the high pitched one, joins in with a light chuckle, and then continues:"

    "???"  "In all fucking seriousness, eh, it’s better than the nothin’ we’ll be having soon, so we better enjoy the poor cunt."

    $ deadcitizen = game.returnRandomDeadName()
    """

    By this point your curiosity has, stealthily, brought you in view of the scene.  Three figures are standing around [deadcitizen]’s fresh grave, the loose earth that the townsfolk had so recently packed over their coffin lying in a neat pile just off to the side.

    The three figures are standing in a line, all with their backs to you.  The naked one with fatty hooves, crooked shoulders and a rat’s tail curled neatly around like a pig’s tail answers, in its whining phlegmy voice.  The tall one, the one with a scraggy raven’s wing instead of a left arm and long skin covered claws at the end of its feet, listens.
    """

    "???"  "Why you gotta be such a sour puss cunt Inky?  I though’ we were gunna get a feast?"

    "The third figure, also naked and with pussing snake arms, feet that look like whole dead animals, one a rat and one a rabbit, and what looks to be a rotting doll’s head perched atop its twisted neck, bobs up and down and rasps in agreement."

    "Inky"  "You wanna run this operation on your own, do ya Fuckface?  Sorry if I’m tryn’ to keep things realistic.  And sorry if it’s always funny to watch you two squirm."

    "Inky laughs, the jet black feathers of its arm quivering up and down while it leans its weight on the spade it holds with its normal hand.  ‘Fuckface’ loudly complains of bullying, emphatically swinging the pickaxe it’s carrying around, while the third figure continues to rasp, a rotten scale falling from the arm it has wrapped around what looks a bit like a broken hoe."

    "Inky"  "Right, that’s enough fuckin’ around.  Time to dig in, me-thinks.  Pull it up Slimey."

    "The one with the doll’s face stops its creaking laughter and drops its hoe, kneeling down on legs that let out a dangerous popping sound and snaking its long limbs into the open grave.  A moment later, and with very little strain on ‘Slimey’s’ part, the figure straightens again, holding [deadcitizen] in its long flexible arms."

    "Fuckface"  "It’s even more skinny than it looked in the ‘ole!"

    "Inky"  "Lookin’ for something your size fatso?  Now shut up, my stomach’s rumbling."

    menu:
        "*Attack.  These creatures cannot be allowed to eat [deadcitizen]’s body!*":
            $ c=3
            """

            You launch yourself from the undergrowth, weapon in hand, quickly closing with the figures.  You are impressed by your own stealthiness, moving quickly but silently over the frozen earth, but your joy is short lived.

            In one fluid motion, and without looking round, the figure called Inky swings its arm behind its back, the head of the space it is holding impacting your face with enough force that you find yourself suddenly on the ground, your ears ringing.
            """

            "Mild injury" # temp

            $ c=4


        "'Hello there'":
            $ c=2
            "All three creatures turn towards you as you step out of the undergrowth, Fuckface with surprise, Inky with an air of cool nonchalance that shows that he knew you were there all along, and Slimey simply by rotation its rotten doll’s head one hundred and eighty degrees."

            $ c=4


        "*Leave these creatures to their dark feast*":
            $ c=1
            "Feeling disgusted, whether with yourself or with the scene acting itself out behind you, you leave the creatures to their food and return to your own work."

            $ game.eventyieldmod = 0.8
    if c == 4:
        "Fuckface"  "Where the fuck did that come from!"

        "Inky"  "It’s been watchin’ us from the bushes over there, hasn’t it?  Seen it plain as day from that eyeball I stuck up your areshole."

        "From the lack of laughter at this remark, and the fact that ‘Fuckface’ self consciously pats his behind, you are sickeningly conscious that this is probably not a joke."

        "Inky"  "Anyway, that’s no way to treat our honored guest!  This is [game.player_name] isn’t it!"

        "Fuckface"  "Aw shit Inky I think you’re righ’!"

        "Inky"  "Of course I’m right you fuckin’ moron!  Now what do you say to it?"

        "Fuckface"  "Oh righ’ yeah, sorry [game.player_name].  We’re very grateful and all."

        "Inky"  "That’s right.  We were worried there for a second, after old man Alexi got all ‘igh and migh’y, but you’ve gone and kept the food rollin’ in."

        "Inky inclines its long, beaked face towards [deadcitizen]’s body."

        "Inky"  "You want a bite?"

        menu:
            "'No!'":
                $ c = 5
                "Inky"  """

                Then what the fuck are you doing here?

                Wait, don’t tell me.

                You wanted to have a little chat right?

                Seems to be your main skill up there in town, eh?

                Chattin’.

                Keep it up.  More time you spend natterin’, less time you spend gettin’ your people food.
                """

                "Fuckface"  "But don’t we wan’ it getting ‘em food?  I mean this one real skinny..."

                "Inky lets a long, irritated sigh out of the human looking nose that sits at the end of its beak."

                "Inky"  """

                Clearly your brain’s as fucked up as your face, Fuckface.  If they were eatin’, they wouldn’t be dyin’.

                Sorry my colleagues such a fuckin’ idiot.  His tummy’s rumbly so he’s even more slower than usual.

                You should probably get goin’.  We got eatin’ to do and knowin’ how much you like chattin’ with ‘em, you probably won’t be so keen on watchin’ us skin ‘em.

                Keep up the good work though.  You’ve got a nice fat arse from all that sitting around you do, wouldn’t want it to spoil before I get the chance to eat it.
                """

                """

                The three creatures laugh, but Inky doesn’t take its eyes off you while it does, casually hefting the space in its hand while it does so.  Slimey picks up on this first, taking a step forward and fixing you with the dull, unpainted pits that used to contain the doll's marble eyes.  

                Only after the laughter has died down, and the brandishing of makeshift weapons has gone beyond obvious, does Fuckface realise what is happening.  

                The muscles underneath the skin of its face, deformed almost beyond description with three eyes each randomly placed, a snout on the forehead and the mouth constantly drooling at a seventy degree angle over the cheek bone, tighten.
                """

                "Fuckface"  "Oh yeah, fuck off!  I’m hungry!"

                "Inky’s pitch black bird eyes bore into you, and you realise that there really is no choice but to follow Fuckface’s command and leave these creatures to their feast and return to town empty handed."

            "'Yes'":
                $ c = 6
                "Fuckface"  "It wants to ea’?  But Inky, I don’t wanna share my food with tha’!"

                "It is difficult to read any emotions in Inky’s avian face.  It stares at you, in that motionless way only birds can, for several seconds, before it twists and brings the edge of its spade down on [deadcitizen]'s hand, severing it in a single shockingly strong blow, scooping it up and tossing it adroitly to you."

                "Inky"  "Our guest can have an ‘and, how’s that Fuckface?  You don’t like ‘ands anyway."

                "Fuckface"  "Oh that’s true.  Find ‘em difficult to ea’."

                """

                This isn’t surprising.  As his name suggests, Fuckface’s face is deformed almost beyond description, with three eyes each randomly placed, a snout on the forehead and the mouth constantly drooling at a seventy degree angle over the cheek bone.  All three of those eyes, mismatched not just in colour but in size and shape, are focussed on the item in you are holding.

                A raw human hand.
                """
                menu:
                    "*Take a bite*":
                        $ c=7
                        """

                        The meat is cold, loose and tough.  The body is not sufficiently old to have turned rancid, but the flavour could not be described as ‘good’.

                        You look up as you chew to see Inky and Slimey watching you, their faces unreadable, while Fuckface looks between you and them, confusion visible even on its alien features.
                        """

                        "Fuckface"  "I didn’t think it would actually..."

                        "Inky"  "Well it did, didn’t it?"

                        "Slimey makes some rasping sound, the meaning of which is beyond you but which seems clear to the other two.  Fuckface begins to look scared, but Inky merely shrugs."

                        "Inky"  """

                        Maybe so, maybe not so.  I don’t fuckin’ know.  And right now I’m too fuckin’ hungry to care.

                        You should probably scram [game.player_name].  We gotta lotta eatin’ to do, and it ain’t fuckin’ pretty.  Fuckface here eats like a fuckin’ monster, and you don’t even want to know about Slimey.  Nightmares for weeks.  And you’ve got a lot of work to not do, can’t be missing that sleep.

                        It’s been lovely chattin’, even if you’ve hardly said a word.  I like to see you chattin’.  Keeps you from doing anything else, and that keeps the crop comin’ in for us.

                        So bugger off and keep up the good work.  Keep the good stuff coming, alright?  Then maybe we’ll see you again.
                        """

                        "You get the impression from the way that Inky brandishes its spade that this point is not up for debate, so you return to town, the flesh of your former comrade already digesting in your stomach."

                        $ game.GhoulFriend = "True"


                    "*Change your mind and refuse*":
                        $ c=8

                        "Inky"  "Yeah, that’s what I fuckin’ thought."

                        "Inky uses the spade to knock the hand out of your grasp."


                        $ c = 5
                        "Inky"  """

                        Then what the fuck are you doing here?

                        Wait, don’t tell me.

                        You wanted to have a little chat right?

                        Seems to be your main skill up there in town, eh?

                        Chattin’.

                        Keep it up.  More time you spend natterin’, less time you spend gettin’ your people food.
                        """

                        "Fuckface"  "But don’t we wan’ it getting ‘em food?  I mean this one real skinny..."

                        "Inky lets a long, irritated sigh out of the human looking nose that sits at the end of its beak."

                        "Inky"  """

                        Clearly your brain’s as fucked up as your face, Fuckface.  If they were eatin’, they wouldn’t be dyin’.

                        Sorry my colleagues such a fuckin’ idiot.  His tummy’s rumbly so he’s even more slower than usual.

                        You should probably get goin’.  We got eatin’ to do and knowin’ how much you like chattin’ with ‘em, you probably won’t be so keen on watchin’ us skin ‘em.

                        Keep up the good work though.  You’ve got a nice fat arse from all that sitting around you do, wouldn’t want it to spoil before I get the chance to eat it.
                        """

                        """

                        The three creatures laugh, but Inky doesn’t take its eyes off you while it does, casually hefting the space in its hand while it does so.  Slimey picks up on this first, taking a step forward and fixing you with the dull, unpainted pits that used to contain the doll's marble eyes.  

                        Only after the laughter has died down, and the brandishing of makeshift weapons has gone beyond obvious, does Fuckface realise what is happening.  

                        The muscles underneath the skin of its face, deformed almost beyond description with three eyes each randomly placed, a snout on the forehead and the mouth constantly drooling at a seventy degree angle over the cheek bone, tighten.
                        """

                        "Fuckface"  "Oh yeah, fuck off!  I’m hungry!"

                        "Inky’s pitch black bird eyes bore into you, and you realise that there really is no choice but to follow Fuckface’s command and leave these creatures to their feast and return to town empty handed."




    $ game.eventghouls = True # temporary
    hide woodssky onlayer skyback
    hide woodsdeepest onlayer farfarback
    hide woodsdeeper onlayer farback
    hide woodsdeep onlayer back
    return
