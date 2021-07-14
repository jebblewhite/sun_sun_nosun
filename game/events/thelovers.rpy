label thelovers:
    image woodssky = im.Scale("woodssky.png", 3072, 1920)
    image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
    image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
    image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)
    
    show woodssky onlayer skyback
    show woodsdeepest onlayer farfarback
    show woodsdeeper onlayer farback
    show woodsdeep onlayer back

    if game.playerbackground == "woodsman":
        $ textinsert = "You remember making structures like it when you were a child."
    else:
        $ textinsert = "True, you could do little better, but you’ve spent long enough around these woods to know rough work when you see it."

    if game.playerbackground == "deserter":
        $ textinsert2 = "You believe their names were Dagmar and Kristopher, although you know little more about them than that."
    else:
        $ textinsert2 = "They are Dagmar and Kristopher.  The last couple to be married under the light of the sun. One slightly older than you, the other slightly younger, she was a lumberjack and he the baker’s apprentice.  Neither had many friends before they found each other, and both had none afterwards.  They weren’t anti-social, it just seemed that all either wanted was the other."
    """

    The shelter is crude, clearly the work of an amateur.  [textinsert]
    The whole thing is made of sticks.  Once a blanket had draped over the structure, giving it some semblance of insulation, but now it lies where it must have been blown, slumped on the ground, only attached by a few strands that probably got caught by sticks more out of luck than judgement.

    Not that it would have mattered much if the fabric had stayed in place.  It would only have delayed the rain from reaching anything inside, and if the snow had landed on top it would have been liable to grow so heavy the entire structure collapsed.

    Not that the shelter was wholly spared that fate.  A section, almost in the dead centre, has collapsed, leaving the inside of the shelter more or less completely open to the elements.

    The hole also allows the smell to escape.

    The space, when you look inside, is barely larger than the two bodies that fill it; the only other items present are a small pile of wet sticks that look as if they were arranged to be a fire but were never successful lit and a little collection of glass jars, some still sealed and containing what is probably still edible food.

    The bodies are, of course, corpses.  Corpses still well preserved enough that you recognise them.[textinsert2]

    They lie in each other’s arms, Dagmer’s limbs draped loosely around Kristopher, her head turned up and away, while Kristopher’s fingers are locked, digging desperately into the fabric of her clothes, his face pressed hard into her chest.

    Dagmer looks at peace.  Kristopher, on the other hand, is missing clumps of hair, his head a patchwork of bloody scalp.  His knuckles are bloody and it appears as if the bones in the fingers of his left hand are broken.  

    In the corner of the shelter you see a rock spattered with blood.

    A piece of paper, the corner destroyed by rain and snow, pokes out of a pocket on the front of Dagmer’s coat, pinned in place by Kristopher’s head as if he is still trying to protect it, even in death.
    """
    menu:

        "*Leave the couple to rest in peace*":
            $ c=3

        "*Take the remaining food*":
            $ c=2

        "*Examine the piece of paper poking out of Dagmer’s pocket*":
            $ c=1
            """

            You carefully pull the paper, some of it wet, some of it merely moist, from the dead woman’s pocket and unfold it carefully enough that only the most sodden pieces disintegrate in your hand, leaving only the beginning of the letter destroyed.

            The handwriting is shaky, and gets progressively worse as the letter goes on.  A few small drops of blood also stain the paper, although the way they are smudged shows that they fell there while the letter was still being written.

            \"-coming here.  Don’t ever doubt that.  Because we chose each-other.  And that can’t have been wrong.  We had as much time together as the Pantheon would allow, and that is all I ever wanted.

            I’m staying with you.  I know that you know that, but I write it just in case you can’t feel my arms around you, or aren’t watching me.  

            But just in case, I need you to know how much I love you.  How there is nothing that has ever glowed as bright in my life.  In your brightness I hardly notice the sun has gone.  You are all the light I will ever need.

            I believe that the gods have taken you only because they have taken you somewhere better.  They must feel my love and know you are something worth saving.  And I know that if they felt my love for you, then they will feel your love for me.

            I have never felt pain like how I feel pain now.  But I know you do not want to hear about, that my love.

            Oh my god my love, I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you I love you love you I love you I love you I love you

            I LOVE YOU!!

            I don’t know any other way of putting it my love.  I’ve screamed it and I hope you’ve heard.  I screamed it till my throat bled.

            I’m so happy those were my last words.

            Oh gods, my hands are freezing.  I can’t write more.  I don’t know what more to write, but I feel like I should never stop writing, I need to tell you so much, I hope you will always know my love.

            I’ll never let go of you.

            My love, my love my love I love I love I love\"

            The bottom line of the paper has been, clumsily but probably intentionally, blotted out.
            """
            menu:

                "*Leave the couple to rest in peace*":
                    $ c=3

                "*Take the remaining food*":
                    $ c=2
    if c == 3:
        """

        You stand up and look at the bodies one last time: Dagmer so calm, Kristopher twisted and hunched and bloody.

        Both, now, at peace.

        You decide to leave them where they are.  You have the feeling that it does not matter where these two rest, as long as it is together.
        """

        "No reward" #temp

    if c == 2:
        """

        You delicately push the entwined corpses aside and retrieve the jars.  There is a surprising amount of food here, although much of it was not stored properly and has gone bad.  These two did not die of starvation, that’s for sure, although looking at the wet pile of sticks they were attempting to use as a fire, and the hole in the shelter roof, it is not difficult to guess what did kill them.

        Either way, it is too late for them.  Better to use this food to help keep other people alive, rather than just let it go to waste.

        You leave the bodies where they are.  You have the feeling that it does not matter where these two rest, as long as it is together.
        """
        $ game.food += 12
        "get 12 food lol" #temp


    

    $ game.eventlovers = True # temporary
    hide woodssky onlayer skyback
    hide woodsdeepest onlayer farfarback
    hide woodsdeeper onlayer farback
    hide woodsdeep onlayer back
    return
