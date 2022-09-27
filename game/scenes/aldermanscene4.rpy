label aldermanscene4:

# determine most scarce resource textinsert = (most scarce resource)
# if at least one resource is under what it would be expected to be textinsert2 = "...but yes, I suppose that is all a long way of saying that I feel we should be focussing on [textinsert].  Would it be possible for you to speak to-"
# else textinsert2 = "...but yes, I suppose that is all a long way of saying that I think we are doing quite well, all things considered, but you never can be too careful.  With that in mind, would it be possible for you to speak to-" 

alderman  " "

"You are talking to the Alderman in his meeting room, when suddenly the door bursts open and his maid steps breathless into the room."

"Maid"  "I'm sorry to interrupt you both, but there's someone who wants to see you and she's being very insistent about it."

alderman  "Who is it?"

"Maid"  "She says her name is Alina."

alderman  "What do you mean she says her name is Alina?  There isn't an Alina here in town, is there [game.player_name]?"

"The Alderman turns to you, but before you can answer the maid interrupts."

"Maid"  "She's not from here.  She says she's a Senate Outlands Officer.  She says she's from Alexisgrad."

alderman  "She's from Alexisgrad?  Oh this is wonderful news, send her up immediately!"

"The maid nods and ducks out of the room."

alderman  "Oh this is marvellous, isn't it [game.player_name]?  A representative of the Senate, here to bring news of what is happening in the city.  Our first contact with the rest of the Republic, and it comes directly from the senate!"

"""

The Alderman is beaming like a child, but his face quickly falls as the door opens again and his maid helps the Senate Outlands Officer into the room.

The woman is leaning on the maid for support.  Most of the fingers of her left hand are black and dead from frostbite.  Her clothes, smart but fashionable travelling gear, are dirty and ripped.

The maid helps her to the nearest chair and she sits down heavily, wincing at the impact.
"""

alderman  "Oh my word, we must fetch a doctor, you-"

"The woman holds out her hand to stop him."

alina  "You are the Alderman here?  Alexi?"

alderman  "Yes, yes I am."

alina  "I was sent to write a report on your town, for the Senate census.  Lotosk has also been flagged by the Outlands Select Committee for a survey.  It is for those reasons that I present myself and this Senate writ."

"The woman produces a roll of paper from her coat pocket which the Alderman takes and begins to read."

menu:
    "Excuse me Alderman, but surely that should wait.  We need to get this woman to the doctor.":
        #{Very slight respect increase}
        $c=1

    "Sorry, um, maid, but could you please call for Fyodora?":
        #{Slight like increase}
        $c=1

    "I'll check through those quickly for you Alderman, you and Alina should talk now." if game.playerbackground == "merchant" or game.playerbackground == "deserter":
        $c=8

    "*Wait*":
        $c=2

if c == 1:
    "The Alderman looks up guiltily from his reading."

    alderman  "Ah yes, we must get you a doctor straight away!"

    "The woman holds up her hand to stop him, but the maid, who had been nervously shuffling from foot to foot in the corner, has already rushed off."

    alina  """

    I will see your doctor once I have finished my first enquiries.

    Tell me Alexi, what do you know of the disappearance of the sun?  Order your associate out of the room if you cannot be honest with me while someone else is here.
    """

    #{Slight respect increase with the Alderman}
    menu:

        "Of course the Alderman can be honest in front of me, he's an honest and open politician.":
            $c=3

        "Have you been keeping secrets from us Alderman?":
            $c=4

        "*Raise an eyebrow*":
            $c=5
if c == 2:


    """

    The Alderman takes his time with the documents.  Alina continues to sag into her seat, looking more ill by the second.  At some point the maid silently excuses herself and leaves.  You suspect that she has gone on her own initiative to fetch Fyodora.

    Eventually the Alderman places the papers down on the table and turns to Alina.  He begins to speak, seems to notice her appearance again, stops, and then starts on a different track.
    """

    alderman  "This all seems in order, although I do have some questions about it all.  But I think I should save those for another time.  We should get you to our doctor now."

    alina  """

    No, not yet.  I will see your doctor once I have finished my first enquiries.

    Tell me, Alexi, what do you know of the disappearance of the sun?  Order your associate out of the room if you cannot be honest with me while someone else is here.
    """
    menu:

        "Of course the Alderman can be honest in front of me, he's an honest and open politician.":
            $c=3

        "Have you been keeping secrets from us Alderman?":
            $c=4

        "*Raise an eyebrow*":
            $c=5

if c == 3:
    # change this to correct threshold (if attraction is above a certain threshold)
    if game.alderman.attraction > 3:
        $ textinsert3 = "and blushes "
    else:
        $ textinsert3 = ""
    "The Alderman smiles [textinsert3]slightly at your words, but turns to address Alina."

    alderman  "As [game.player_name] says, I try to be as open and honest with the people of Lotosk as I can be.  It's part of the liberal ideal of our Republic, is it not?"

    "Alina narrows her eyes and purses her dark, frozen lips, but simply says:"

    alina  "Go on then.  What do you know?"

    #{Slight like and attraction increase with the Alderman}

    $c=6

if c==4:
    # change this to correct threshold (if attraction is above a certain threshold)
    if game.alderman.attraction > 3:
        $ textinsert3 = "I had hoped you...oh never mind."
    else:
        $ textinsert3 = ""
    "The Alderman turns to you, a sad frown covering his features."

    alderman  "Absolutely not.  I try to be as open and honest with everyone as I can be.  I abhor liars and lying.  [textinsert3]"

    "Alina nods knowingly, as if this is the kind of speech she has heard many times before."

    alina  "Well, if you're sure, then tell me what you know."

    #{Slight like and attraction loss with the Alderman}

    $c=6

if c==5:

    ##alderman  "[game.player_name] is a (if like is above a certain threshold)[good friend and ]trusted advisor of mine, and a (if respect is above a certain threshold)[hero to this town.](else)[respected citizen.]  Besides, I try to be open and honest with everyone."

    "Alina ignores your look and nods slowly."

    alina  "Okay.  Well then, tell me what you know."

    $c=6

if c==6:
    $textinsert7 = ""
    # (if Elisabetta scene >= 4)[only showing any sign of an emotion, specifically disgust, when the Alderman mentions Elisabetta's theories, but otherwise](else)[and so]
    """

    The Alderman spends several minutes saying what he could have achieved with a single word: 'nothing'.  Alina seemed to get the gist very early on, [textinsert7] she spent the time looking as if she just wanted the Alderman to get on with it.

    Eventually, however, he does stop by finally asking the question that he had clearly wanted to ask from the moment that she entered the room.
    """

    $c=7

if c==7:

    alderman  "So, you've come from the city?  What are things like there?"

    alina  "I don't know I'm afraid.  When my contingent left the sun shone there.  It may still.  I am yet to ascertain whether this is a local phenomenon."

    "The Alderman nods thoughtfully."
    menu:
        "Wait, what do you mean by 'contingent'?":
            $c=9

        "Wait, why have you really come here?":
            $c=11

        "Wait, what were things like in the city, when you left?":
            $c=12

        "*Say nothing*":
            #{Very slight attraction increase with the Alderman}
            $c=13

if c==8:

    "The Alderman turns to look at you, then Alina, then back at you."

    alderman  "Yes, yes sorry, forgive me, priorities.  Please, Officer, I'm sure you have questions."
    if game.playerbackground == "deserter":
        $textinsert8 = ", but in the same way as a court martial, which sends shivers down your spine."
    elif game.playerbackground == "merchant":
        $textinsert8 = ", but you've read enough official documents to know when someone is trying to hide censure behind officialdom."
    else:
        $textinsert8 = "."
    """

    The Alderman passes you the papers.  Alina's eyes follow them like a wolf tracking deer, but she does not comment as, still watching the papers, she asks the Alderman what he knows about the sun's disappearance.

    You half listen as the Alderman takes far too long explaining that he knows nothing while you skim the documentation that she has given him.

    There are several forms, and they all looks like they are standard issue, which is odd considering how harsh the language is in most of them.  It's all very professional and official[textinsert8]

    What is surprising is the powers that this Alina has been given.  One of the documents, in one clause, gives her 'the full backing of the senate', even if it does then qualify that with: 'as derived from the majority vote of the Outlands Select Committee'.

    In other words, while she would have to justify it to her superiors, she could invoke emergency powers and take control of Lotosk.  Assuming that Republic control still means anything…

    All in all, this woman was sent here to do more than simply take information for a survey.  She was sent to make sure that the Alderman is conforming to some standard, a standard that the forms leave implicit but also subtly imply he isn't meeting.

    You flick to the last page just as the Alderman finishes his ramble and finally asks the question that he had clearly wanted to ask from the moment that Alina entered the room.
    """

    #{Respect increase with the Alderman}

    $c=7


return
