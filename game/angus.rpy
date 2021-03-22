label angus:
    define elena = Character(_("Elena"), color="#c8c8ff")
    image widowimg = im.Scale("elena.jpg", 722, 1024)

    #image woodsimg = im.Scale("woods.jpg", 3072, 1920)
    #show woodsimg zorder 0
    image woodssky = im.Scale("woodssky.png", 3072, 1920)
    image woodsdeepest = im.Scale("woodsdeepest.png", 3072, 1920)
    image woodsdeeper = im.Scale("woodsdeeper.png", 3072, 1920)
    image woodsdeep = im.Scale("woodsdeep.png", 3072, 1920)
    "The Widow Elena enters..."
    show widowimg onlayer front:
        xalign 0.05 yalign 0.25
    show woodssky onlayer skyback
    show woodsdeepest onlayer farfarback
    show woodsdeeper onlayer farback
    show woodsdeep onlayer back
    elena "YO YO YO WHAT IS UP MY HOMIE?"

