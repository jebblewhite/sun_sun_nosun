label thestag: 
    image woodssky = im.Scale("woodssky.png", 3072, 1920)
    image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
    image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
    image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)
    
    show woodssky onlayer skyback
    show woodsdeepest onlayer farfarback
    show woodsdeeper onlayer farback
    show woodsdeep onlayer back
    
    """
    There is something strange about the cold tonight. It feels piercing, like a draft through a tear in fabric, but covering your whole body, so that it does not matter how you adjust your furs, the feeling on your skin is constant.

    And yet, you are warm. How, you do not know. But it seems to be coming from inside you. Your skin is
    freezing, you are aware of that, and yet somehow warmth flows down from your eyes, making you feel
    strong and comfortable.

    That is the first thing you notice.
    
    The second is the glow.

    At first you think it’s the moon. But it’s too white, it seems hazy through the trees despite the lack of fog
    in the forest tonight, so you look up to the sky and see that the moon is riding high, not sitting low and
    casting long, swaying shadows.

    It is those shadows that allow you to work out where the light is coming from. You take a few tentative
    steps towards it and feel that warmth in you growing.

    The question is, do you continue? Or do you move away from the light and find a different, darker part of
    the woods to continue your search?
    """
    menu:
        "Go away from the light, focus on what you came here for":
            $ c = 1
            if game.playerbackground != "marked":
                """
                You move away from the light, across the woods, and as you do you feel the warmth flowing into your
                eyes dull, and the necessity for your furs return. You feel as if you have lost something beautiful. But
                now is not the time for beauty, you reason, now is the time for survival, and you finish your job in peace.
                """
                $ game.playerHarvest("gather",1)
                "Wood gathered heheh" # temporary
                hide woodssky onlayer skyback
                hide woodsdeepest onlayer farfarback
                hide woodsdeeper onlayer farback
                hide woodsdeep onlayer back
                return
            else:
                """
                You try and move through the forest, away from the light, but it follows you, long shadows moving and
                twisting behind you. Eventually you decide to ignore it and continue on with your task.

                You become so engrossed, however, that you lose track of the direction of the shadows, and as you
                continue moving forward, satisfied that you already have a good haul, you stumble across a large
                clearing. And there standing in the centre, lit with light whiter than you have ever seen before:
                A stag.

                The only thing whiter than the light, whiter than even the snow that covers the clearing, is its fur. Its
                hooves are pearl, its antlers silver. It turns to look at you, spotting you instantly no matter how stealthily
                you approach, and its eyes are swirling vortexes of stars. It stands taller than a man, pure white and
                glowing.

                And staring, its eyes deeper than the sky, at you.
                """
                $ game.playerHarvest("gather",1)
                "Wood gathered heheh" # temporary

        "Move towards the white light":
            $ c = 2
            """
            You move cautiously towards the light, and as you do waves of vitality and warmth flow throw you,
            unnaturally, down from your eyes. The stiffness in your limbs disappears, you no longer feel the weight
            of your equipment and while your skin feels like ice, beneath it you feel your heart beat strong and proud.

            And then up ahead, you see it, standing in the centre of a large clearing, lit with light whiter than you have
            ever seen before:

            A stag.

            The only thing whiter than the light, whiter than even the snow that covers the clearing, is its fur. Its
            hooves are pearl, its antlers silver. It turns to look at you, spotting you instantly no matter how stealthily
            you approach, and its eyes are swirling vortexes of stars. It stands taller than a man, pure white and
            glowing.

            And staring, its eyes deeper than the sky, at you.
            """
    menu:
        "Approach, slowly, with your hand out to pet it":
            $ c = 3
            """
            You place your tools gently down on the snow and stand up straight. The stag adjusts its head so it may
            still look you in the eyes, but apart from that it makes no movement as you slowly walk across the
            clearing, your palm flat and outstretched. Only when you are within a step of it does it finally change
            position, stretching out its head and nuzzling your hand with its nose.

            The feeling of warmth, strength, purity and power reaches its zenith as the light grows, overwhelming you
            as the stag, its eyes infinitely deep whirlpools of stars, stares deep into you, and its tongue, so bright it
            appears as nothing more than a blur to you, licks your hand and...

            ...you wake up in the centre of the clearing, your whole body feeling warm and strong. You do not know
            how much time has passed, but the forest is dark again and you no longer feel that your skin is ice or your
            eyes are sending vitality through your body.

            But you do not feel the quite same as you did before. You feel...pure. Healthy. Well. Your limbs no
            longer ache, your bruises and cuts have vanished and you feel calm. You head back to town feeling
            young again, fit and ready for life as you were in your adolescence, long before the sun set for that last
            time.

            {All player health restored}
            """
            $ game.eventstag = True # temporary
            hide woodssky onlayer skyback
            hide woodsdeepest onlayer farfarback
            hide woodsdeeper onlayer farback
            hide woodsdeep onlayer back
            return
        "Turn and leave":
            if game.playerbackground != "marked":
                $ c = 4
                """
                You begin to move away, but the moment you do you hear the stamping of a hoof on the ground. You
                turn instinctively, perhaps worrying that it is about to charge, but when you look back it fixes you with its
                infinitely deep eyes, and bows.

                Whether you bow back or not, the beast turns and runs with otherworldly grace and speed off between the
                trees, leaving you alone, the cold of the real world slowly returning to you.

                You’ve wasted quite some time chasing down the buck, and you do not manage to gather quite as much
                as you had hoped on this journey. Still, the stag was one of the most beautiful things, if not the single
                most beautiful thing, that you have ever seen, and that feeling of health, warmth and strength is something
                that your body will never let you forget.

                {gain a quarter of normal action reward} 
                """
                $ game.eventstag = True # temporary
                hide woodssky onlayer skyback
                hide woodsdeepest onlayer farfarback
                hide woodsdeeper onlayer farback
                hide woodsdeep onlayer back
                return
            else:
                $ c = 6
                """
                You begin to move away, but the moment you do you hear the stamping of a hoof on the ground. You
                turn instinctively, perhaps worrying that it is about to charge, but when you look back it fixes you with its
                infinitely deep eyes, and bows.

                Whether you bow back or not, the beast turns and runs with otherworldly grace and speed off between the
                trees, leaving you alone, the cold of the real world slowly returning to you.

                It is time to return home.
                """
                $ game.eventstag = True # temporary
                hide woodssky onlayer skyback
                hide woodsdeepest onlayer farfarback
                hide woodsdeeper onlayer farback
                hide woodsdeep onlayer back
                return
        "Shoot it":
            $ c = 5
            """
            It continues to stare at you, unmoving, as you pull out your bow, knock an arrow and fire.

            You hit it square in the chest. The stag blinks once. The arrow has lodged deep, it should have struck its
            heart, and yet there is no blood to mar the whiter-than-white coat.

            The Stag continues to stare at you. You look into its eyes. The constellations there seem to be receding,
            the infinite depth somehow pulling away, flying infinitely quickly backwards, away from the world and
            into the animal’s skull. The light in the clearing starts to fade, the warmth coming in through your own
            eyes drops, you feel the cold, the normal, everyday cold, returning to you.

            And then, just as the light dims so much that you can no longer see down the beast’s enchanted eyes, it
            collapses.

            Darkness.

            You drag the corpse back to town, where it is prepared as meat and pelts. Mik tells you that they have
            never seen an animal with so much meat on it, and the pelts are thick and ethereally beautiful.

            Still, you never see that light again, and never feel that warmth and strength. Something magical has been
            lost from the world. You cannot help but wonder, was it worth it?
            """
            "gain meat n pelts !!!" #temporary
            hide woodssky onlayer skyback
            hide woodsdeepest onlayer farfarback
            hide woodsdeeper onlayer farback
            hide woodsdeep onlayer back
            return

    hide woodssky onlayer skyback
    hide woodsdeepest onlayer farfarback
    hide woodsdeeper onlayer farback
    hide woodsdeep onlayer back
    return

label thestagnight:
    image woodssky = im.Scale("woodssky.png", 3072, 1920)
    image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
    image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
    image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)
    
    show woodssky onlayer skyback
    show woodsdeepest onlayer farfarback
    show woodsdeeper onlayer farback
    show woodsdeep onlayer back

    """
    You have a dream of purity, warmth, strength, vitality. A dream in which you are strong and young, a
    dream filled with light, bright white light and the sound of galloping hooves. You awake feeling strong
    and happy, better than sleep has ever made you feel.

    But as you leave your house and journey into town, you notice something strange. There are hoof tracks
    in the snow all around town. And you hear people talking about dreams of bright, pure white light. Of
    feeling strong, or warm, or healthy. Younger. Full of life.

    You hear mention of a pure white stag.

    It is only later that you hear of the miracle, that all of the patients at the hospital have been dismissed, that
    no new cases of illness have been reported today.

    No one in the town ever feels anything quite like it again. But you know where it came from. You felt it
    when you were awake. And you will never forget that feeling.
    """
    "Reduce the illness to 0!!" #temp
    hide woodssky onlayer skyback
    hide woodsdeepest onlayer farfarback
    hide woodsdeeper onlayer farback
    hide woodsdeep onlayer back
    return