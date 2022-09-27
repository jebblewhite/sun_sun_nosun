label debugScenes:
$ scenechooser = "thestag"
$ scenechooser = renpy.input("Which scene would you like? i.e. crierscene2, thestag")
$ scenechooser = scenechooser.strip()

jump expression scenechooser
return