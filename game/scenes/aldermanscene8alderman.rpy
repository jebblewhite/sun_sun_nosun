label aldermanscene8alderman:


"""

The knock on your door is timid and slow.

The Alderman, when you open the door, looks at you with red eyes, although his face is currently dry.
"""

alderman  """

I heard that she is probably going to come for me today.

Alina, that is.  One of Jacob's friends told me that she wants him to help her kick me out of office today.

I had very much hoped that I would not need your help, even though you said you would help if I needed it.  But I've hurt myself [game.player_name], and I don't think I can finish it all today.  So I need you after all.

I would...feel more comfortable not talking about it here.  Can you accompany me to the Town Hall?
"""

"""

You nod and follow the Alderman as he leads you wordlessly, and with many glances over his shoulder, through back alleys, finally slipping through one of the Town Hall's back doors.

The building is dark, none of the fires or lamps that the Alderman's maid usually maintains have been lit.  Just enough light comes through the windows at the top of the large stairs for you to see by.

The Alderman, rather than leading you up to his office as you had expected, instead guides you through a door on the ground floor, half hidden against the stairs.

The room inside is small and neat.  A little desk, cheap and old, rests against one wall, but apart from that and a simple wooden stool, the room is bare.

The room feels dark, even with a single candle burning, because of its position under the stairs, with no plaster or board to disguise the stepped slope above.  The desk is on the far side, underneath the tallest part of the room, the point where the stairs almost reach the floor above.

The Alderman gestures towards a cloth on the floor, upon which lie a number of well organised tools, and then indicates that you should let your gaze rise upwards.

It only takes a few seconds to notice the tampering.  Loosed screws, new wood, removed supports.  Two steps of the stairs above you have been reworked.  Reworked in such a way that…

The Alderman nods.
"""


if game.AldermanGrieved:
    $textinsert = " my brother died"
else:
    $textinsert = "...well, before"

alderman  """

They still need to be connected, and one of the supports still needs to be removed.  But yes, I can see you have realised it already.

As I said before, I am not proud.

I have thought about it long and hard.  But I am confident, well, as confident as I can be, that when she falls through, she will not die.

Of course, there are always factors that you cannot account for.  And I know that falls just from standing height can be fatal.

But a risk must be taken.  I pray to the Pantheon that that is right.  But I used to hike some in my youth, up in the mountains, before[textinsert], so I do know something about this.

This is as safe as I can make it [game.player_name].  As safe as I can make it while making it effective.
"""
menu:
    "This is evil":
        $c=2

    "I hate that this is necessary, but I will help you":
        #{Slight respect increase}
        $c=5

    "I'm impressed, I didn't know you had this in you":
        $c=1



if c==1:

    "The Alderman shakes his head, sadness, anger and disappointment all mixing on his face."

    alderman  """

    There is nothing impressive about this [game.player_name].  This is dirty and dark.  But it is necessary.

    I do not like that you, or anyone, could be impressed by this.

    But you are here now.  And I do need your help.  So stand there and I'll pass you the tools you need and tell you exactly what needs to be done.
    """

    #{Significant like and attraction loss with the Alderman}

    $c=8




if c==2:

    "The Alderman nods, looking as if he barely has the strength to do so."

    alderman  """

    Yes, yes it is.  This is abhorrent and disgusting, dirty and dark.  But Alina cannot be allowed to take control of this town.

    This will put her in the hospital.  It will give me more time, more time to persuade this town that what she proposes is evil itself.

    And - if an old, foolish man can hope - maybe give her time to think herself.  See what charity and care can do.  Yes, I know that she only just limped out Fyodora's and it did not seem to change a thing, but maybe, just maybe a second stint could work.

    Either way, the people of Lotosk, they care too much.  They won't let someone in her … they won't let someone seriously injured take on the responsibilities of leadership.  They know leading is difficult and painful and they won't let her put herself through that.

    The people here see being a politician as a service, not an ambition.  We are different from the city folk.

    I know the people here [game.player_name].  I know I do.

    They will care for her [game.player_name].  I know they will.  And I will too, as much as she will let me.

    Oh [game.player_name], don't make me justify it any more.  I know it is evil.  I know.  I wish, I wish by all the Pantheon and all the spirits that I didn't have to do this.

    But I do.  And please [game.player_name], please, you have to help me.
    """

    #{Slight respect, like and attraction increase with the Alderman}
    menu:
        "No":
            $c=3

        "I hate that this is necessary, but I will help you":
            $c=5


if c==3:

    alderman  """

    Then you must give me your word, your promise on your gods and your life, that you will not tell anyone.

    You have already given me your word that you would help, and now you refuse.  I will forgive that before the gods, but only if you make a second oath, and keep that.
    """

    """

    You open your mouth to speak, but before you can, a sudden sensation grips you.
    """

    if game.playerbackground == "deserter":
        """
        You have had your chance, you realise.  You have been an oath breaker before.  You have fled pain and suffering once before.  If the gods, or the world, or the spirits or whatever it is that governs your life and the universe forgave you then, you know that they would not forgive you a second time.

        You have little dignity.  Do not let yourself lose the last of it.
        """

    elif game.playerbackground == "merchant":
        """
        You had a contract.  You had given the Alderman your word.  Was he acting in bad faith?  No, you cannot honestly say that he was.  He told you that what he must do was abhorrent, and you agreed.

        Your entire trade, your entire livelihood, is based on contracts, oaths, agreements.  Or at least it was before the dark stole all of that away.

        You cannot let it take this last feature.  You cannot let it take your dignity.

        """

    elif game.playerbackground == "marked":
        """
        A shiver down your spine.  Something not really there, in the corner of your eye.  A pressure pushing up against the edges of your hairs.

        Something is watching you.  Divine or occult, you do not know.  But something powerful, and powerfully arcane, is waiting for your decision.  And it is letting you know that really, you only have one choice.  You are only permitted to make one choice.

        So you make it.

        """

    else:
        """
        You look at the man who has led this town for as long as you remember.  The man whose leadership saw you learn the ways of the forest, whose leadership let you excel, find who you wanted to be, who you were born to be.

        He never forgot you, never forgot the woods.  Always supported you and your colleagues, even when the farmers told him that he was a fool, that the forest should be cut down for fields for their crops and animals.

        You may think that what this man is doing now is evil.  But as he says, you have already broken your word.  You owe him, at the very least, this one last thing.

        """

    

    "'Yes', you say, and then you swear it.  The Alderman gives you a small smile, not out of happiness, but in support."

    alderman  "I know that I have made you do a bad thing.  But still, I believe it was the right thing.  Now go.  If you wish to be here when it happens, to help, then stay close by.  If not then just go.  I will make sure you hear what happens."
    menu:
        "*Go*":
            $c=4

        "*Leave, but stay nearby*":
            $c=13

if c==4:

    """

    The Alderman is true to his word.  

    You never know how he managed to fix the work on his own, although watching him closely you realise that he is never able to lift his arm fully over his head again.

    Later in the day, Nat walks the streets, crying out the tragedy.  Alina, visiting the Alderman, fell through the stairs.  She broke a leg and hit her head badly.  

    She is yet to wake up, but Fyodora is confident that she will survive.
    """

if c==5:

    #{Slight attraction increase with the Alderman}

    alderman  """

    I hate it too.  I hate it with all my heart.

    What we will do today is evil.

    But sometimes good people have to do evil things, to prevent further evil.
    """
    #mm
    if game.alderman.attraction_matrix >= 10 and game.AldermanGrieved:
        "The Alderman stoops to pick a tool off the cloth on the floor, but then he stops himself and stands up straight."

        alderman  """

        Before … before we do this [game.player_name], I feel like I owe you something.

        You have accepted this terrible, terrible burden, so I feel that I should be honest with you.

        This is … difficult to say.  I have not said this to anyone since my parents died.

        This is hardly the best place to do it.  Or the best circumstances.  But in a way, maybe that makes it the best time and the best place?

        I don't know.  Maybe I just feel that if you are ever going to be honest with me, it will be now, when my debt to you is so clear and so great.

        I might just be an old fool who doesn't know what he's doing.

        But [game.player_name], I love you.

        I think I realised it, when telling you about my brother.

        Firstly, you listened.

        But also, you made me realise, that he died so that I could live.  And I haven't been doing that.

        So I realised, I love you.  
        """
        menu:
            "I love you too":
                $c=6

            "I am glad you told me.  And I'm happy for you.  But I am sorry, I don't feel the same way":
                $c=7
    else:

        alderman """
        We should not delay.  It will not make what we are doing any less wrong.

        If you could step on there for me, I will pass you these tools and tell you what to do…
        """

        $c=8


if c==6:
    alderman  "Is that true?"

    "You nod.  The Alderman smiles, almost meekly."

    alderman  """

    I … I had thought you would say that you didn't.  But I am glad.  Very glad.

    But now I regret asking you here and now.

    We have work to do.

    But later, later we should talk.  Once this is all over, I will come and visit you.  Or you could visit me, I do not mind, whichever you prefer.

    Oh, and [game.player_name].  I do not want to give you the wrong impression.  I have been a bachelor all my life.  In the spirit of being honest, I should tell you that I do not really know what I am doing.

    I do not want you to miss out.  Polyamory is common in Alexisgrad.

    They say some people are simply polyamorous, and some are monogamous.  I will be honest [game.player_name], I do not yet know which I am.  But if you are, or if you discover you are, polyamorous, I would not want to stop you.

    Not that I am saying that I would … you know…

    Ahem.

    We have work to do.  

    I think you understand my point.

    If you could step on there for me, I will pass you these tools and tell you what to do, for the stair…
    """
    $ game.alderman.romance == True
    $ c=8




return
