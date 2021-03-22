label angus:
    define elena = Character(_("Elena"), color="#c8c8ff")
    image widowimg = im.Scale("elena.jpg", 722, 1024)
    image woodsimg = im.Scale("woods.jpg", 3072, 1920)
    show woodsimg zorder 0
    "The Widow Elena enters..."
    show widowimg zorder 1:
        xalign 0.05 yalign 0.25
    elena "YO YO YO WHAT IS UP MY HOMIE?"

