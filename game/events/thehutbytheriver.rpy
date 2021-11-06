#river event - must be first of the day ??
label thehutbytheriver:
image woodssky = im.Scale("woodssky.png", 3072, 1920)
image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)

show woodssky onlayer skyback
show woodsdeepest onlayer farfarback
show woodsdeeper onlayer farback
show woodsdeep onlayer back

$ textinsert = ""
$ textinsert2 = ""

if game.playerbackground != "deserter":
    $ textinsert = "Your eyes move up to the man's face again, and you suddenly feel a jolt of recognition.  The man is Einar, an old farmer with a reputation for madness and paranoia.  He went missing some time ago.  To think that all that time, he's been hiding here, just outside of town."

if game.playerbackground == "marked":
    $ textinsert2 = "All is quiet, but still, you feel a waiting.  Not inside the hut, but outside, gently pressing in."


"""

It is not a surprise that you have never noticed the hut before.  True, it is small and the thick snow that surrounds it makes it hard to spot, but the real reason that you have not seen it before is simply that you rarely journey this far down the river.

No, there is nothing mysterious or unsettling about your discovery of the little hut.  You only start to feel uneasy as you push open the door, the metallic snapping sound informing you too late that in doing so you broke some long ago rusted lock.

The hut, as you had guessed it would be, judging by its size, is a single room.  A single bed, neatly made, stretches along the back wall, while a simple wooden chair sits in what you judge to be the dead centre of the room, facing towards the door.  The rest of the small space is taken up by containers of every kind: cupboards, barrels, chests, baskets, etc.

All of this, however, you only notice the second time you look into the room.  The first time you had recoiled almost instantly as the long enclosed space disgorged its contents of foul air, the competition between the stenches of rot and waste passed as both escaped into the freezing night air.

And, of course, it was not the furniture you really noticed first when you looked in that second time.  Really it was the corpse, desiccated and skeletal but still very much in the process of rotting, propped up stiffly on the chair, its frozen eyes still watching the door.

You take a step inside, maybe holding something over your nose, maybe simply breathing the thick air in through your mouth.  As you cross the threshold your lantern picks out what you first take to be a semi-circle of frost around the door, but quickly deduce, from the way that this hut was more or less securely isolated from the outside world, that it must instead be salt.

There is more salt on the window sills, and the glints of white indicate that there is salt in the corpse's hair, and a small pile pooled in his lap.  Probably none inside him though, judging from the smell.

And then you notice the tattoos.  Dark, muddy ink scrawls, each one about an inch tall, cover the right side of the man's torso, from the palm of his hand up to his shoulder and down across the front of his ribs to his pelvis, stopping just short of the man's belt.  

They look like letters, but if they are they are not letters of any language you have ever seen.  Of that you are sure, despite the fact that an entire row of the letters on his arm is bisected by a long, deep scar.

The knife lying in a pool of long dried blood beneath his hanging left hand leaves little question as to where the cut came from.  Or, indeed, how the man had died.  Although his body is so thin you imagine that it would not have been long before starvation would have done the job the knife did.

[textinsert]

You take a step away from the body, listening to the silence of the night. [textinsert2]
"""
menu:
    "Leave.":
        $c=6

    "Search the many containers.":
        $c=1
        """

        Many of the containers are empty.  Many others, well sealed barrels, contain the substances usually produced when an individual doesn't leave an enclosed space for a significant amount of time.

        Only one container, a small chest pushed under the bed, contains anything of note.  A small notebook about half filled with small, neat writing.
        """
        menu:
            "Leave.":
                $c=6

            "Read the notebook.":
                $c=2
                """

                The notes are mostly more or less incomprehensible.  You make out dates and times, what might be locations around the hut and what appears to be a regularly updated inventory of the hut's supplies, but everything is written in a kind of short hand you don't understand.

                That is, until you read the last page.  Everything else up till that point had been bureaucratic, almost scientific.  There were as many numbers as letters.  But the last page reads like a diary:

                'No records for yesterday.  No records for today either.  Probably no more going forward.  No more food anyway.

                I fear I was mad.  I fear that all these weeks, I was wrong.  I fear that there really was nothing out there.  I fear that I wasted all that time hiding from something that really did not exist.

                I fear that, because I now know I did not know there was something there.

                And I know that because I now know that I do know that there is something out there now.

                I thought I could feel it before but I couldn't, but now I can.

                It's out there, waiting for me.  I can hear it, I can feel it, I can sense it.  Now all those other 'clues' I saw before mean nothing.  I have evidence now.

                Now, for the first time, I really can't leave.

                P.S. Yes, I have wondered if maybe only now I am mad and before I was sane.  After all, it feels as if this night has been going on for days.  But to that, I have no answer.  I must simply trust what I see now.

                This night has been far too long.  I can hear bells.  They sound like they are coming from town, but perhaps they are in my head.  Calling me.  I can't leave, not now.  Perhaps it is time to end?'
                """
                #{Set £HutReadBook = "True"}
                menu:
                    "Leave.":
                        $c=6

                    "Rip some pages from the back of the notebook to copy the man's tattoos onto.":
                        $c=5

                    "Mark the man's symbols onto your own arm.":
                        $c=3

                    "Wipe the salt off the windowsill.":
                        $c=4



            "Rip some pages from the back of the notebook to copy the man's tattoos onto.":
                $c=5

            "Mark the man's symbols onto your own arm.":
                $c=3

            "Wipe the salt off the windowsill.":
                $c=4


    "Mark the man's symbols onto your own arm.":
        $c=3

    "Wipe the salt off the windowsill.":
        $c=4

if c==3:

    """

    You kneel down next to the corpse and spend some time copying the symbols of the man's tattoos onto your own arm.  Your ink and tools are imperfect and the work is intricate, so it takes you some time before you are satisfied that you have accurately transcribed all of the marks onto your own skin and by that time you feel that you should be getting back.

    You take one last quick glance around the shack before stepping out into the fresh air of the outside world.
    """

    "Voice"  "You wear his dream, but I do not feel it within you."

    "Your vision goes black."  #black screen.

    "Voice"  "But I must fulfil my destiny.  At least in part.  At least superficially."

    """

    For a moment, you cannot feel your arm.  Without sight, for all you know, it has ceased to exist.  

    The only proof that anything is happening at all is the sound.  A tearing, a slurping, a ripping.  And then there is pain where your arm had been.

    Your eyes burn as vision slowly returns, but that is not important.  Your body and mind will allow you to think about only one thing and that thing is the pain that is your arm.

    Later, you are told that you screamed.  You remember how your vision slowly returned and you saw it, rivers of blood running down your flayed flesh and pooling in the snow, how that sight had blurred again before everything turned black.

    """
    #Return vision, UI shows that it is the following day and they have lost as many actions as they spent the day before (5 total lost actions)
    """
    They found you in the snow, near death from blood loss, and took you straight to Fyodora.  Now your arm is thickly bandaged and you are told that the scarring beneath will never heal.  

    The strange symbols, the only bits of skin left intact, as if something deliberately flayed around them to leave them as a raised relief on your flesh, will forever stand out against the scar tissue.

    But while the damage is great, a blood transfusion saved your life, and miraculously no muscle tissue was permanently damaged.

    The scars, with time, will be all that you took away from that hut by the river.
    """

    #{Gain a serious injury}

    jump thehutbytheriverend




if c==4:
    $ textinsert3 = ""
    # (if multiple actions were given to fishing) condition
    if game.actions < 3:
        $ textinsert3 = "Maybe fishing will still your beating heart?"

    """

    You move over to the windowsill and, your hand cupped, sweep and handful of salt into the air.

    And, against all the laws of gravity, into your eyes.

    You stagger back, clawing at your burning eyes.  """

    #The screen goes black

    """
    You hear the window shatter.

    There is a thud that you more feel than see, the sound of something heavy landing on the windowsill.

    A presence is in the room with you, something you don't hear or feel or smell but which you know is there even before it speaks.
    """

    "Voice"  """

    My destiny…nothing but old meat.

    Still.  I must.
    """

    """
    A sharp sound, like a quick exhalation through teeth.

    The presence leaves, not through the door or through the window.

    You blink the salt out of your red and tearing eyes.

    Bones lie heaped on the chair and floor where they fell.

    On the left they lie on dry blood.

    On the right they lie on a small pile of what looks like paper, white on one side and black with ink on the other.  Little cut-outs of strange letters.

    Little flakes of skin.

    Of the little flesh that was left on the man, only the runes remain.

    Whether out of fear or not, you leave.  There is nothing more for you here.

    [textinsert3]
    """

    jump thehutbytheriverend

if c==5:

    """

    You spend some time meticulously sketching and copying and by the time you are satisfied that you have an accurate picture of the man's tattoos and their layout you feel that it is time for you to be getting back to town.

    You take one last quick glance around the shack before stepping out into the fresh air of the outside world.
    """

    "Voice"  "He had no idea what he did, and yet you think to meddle with things you understand even less?"

    "Your vision goes black."  
    #black screen.

    "Voice"  "But I must fulfil my destiny.  Even on this woeful facsimile."

    """

    You do not feel anything, and yet you know it is there, brushing up against the skin of your leg beneath your trousers, under the pocket in which you stored your notes.  Your skin rashes with goose pimples even before you feel the stinging cold, the snowflakes landing on your suddenly exposed flesh.

    You stagger away from the presence, your vision slowly returning as your hand gropes the hand-sized hole that has somehow been rent in the fabric of your clothes.

    The pocket is gone.

    Your other hand, outstretched and waving back and forth, strikes against a tree, and you stand for several minutes as the world slowly stops swimming.

    You look behind you.  The only tracks in the snow are your own.

    But there.  Something black against the white.  A small pile of scrap paper, slowly turning to wet mush in the snow.

    Not your notes.  There is far too little here to be your notes.  No.  Every tiny bit of blank paper, every letter of your own language, is gone.  Just the runes, perfectly cut out with a master's care, remain, slowly destroying themselves in the sludge.

    You feel your leg begin to numb.  Frostbite won't kick in if you just keep moving, you judge.

    Besides, there is nothing left for you here anyway.
    """

    #{All actions dedicated to fishing lost}

    jump thehutbytheriverend

if c==6:

    """

    Whatever happened here, it is not good.  You and your town have enough problems without involving yourself in this.

    And the smell isn't getting any better besides.

    No, best to just return to work, and leave this hut how you found it.

    Forgotten.
    """

    #{2/3 normal fishing reward}








label thehutbytheriverend:
$ game.riverevents['thehutbytheriver'] = False # temporary
hide woodssky onlayer skyback
hide woodsdeepest onlayer farfarback
hide woodsdeeper onlayer farback
hide woodsdeep onlayer back
return
