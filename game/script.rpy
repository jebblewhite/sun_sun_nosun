# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tree")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bliss

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tree_proto

    # These display lines of dialogue.

    t "Hey, I'm a tree."

    t "Please end my suffering."

    show tree_1 at left

    t "Now i am over here and bigger because Angus finished me."

    t "This is all I currently have"

    money = 0

    if money <1:
        t "here, have some money"
        money += 1
        "money now: " + string(money)
    # This ends the game.

    return
