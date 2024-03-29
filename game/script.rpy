﻿# The script of the game goes in this file.



"""
GAME START #########################################################################################################################################
"""
# The game starts here.
label splashscreen:
    scene susnun (2)
    image ssnow = Snow("snowflake.png", max_particles=500, speed=120, wind=200, xborder=(0,100), yborder=(50,400))
    show ssnow zorder 2
    with Pause(1)
    show text "A Game by A. Barker, J. Ebblewhite, and M. van Mesdag" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "Untitled Sun Game" with dissolve
    with Pause(2)
return
""" CHARACTERS AND VARIABLES LOAD """
# CHARACTERS and scenes DEFINED

#define landowner = Character("Izzy") HOW I WANT IT TO BE
#image landownerimg = "landowner.png"

#define game.char.name = Character(game._dict_[char].ide)
 

""" CHANGE THIS """
label start:
    init python:
        from game2 import Charac
        from game2 import Game
        game = Game()

    define crier = Character(game.__dict__['crier'].name)
    define alderman = Character(game.__dict__['alderman'].name)
    define innkeeper = Character(game.__dict__['innkeeper'].name)
    define landowner = Character(game.__dict__['landowner'].name)
    define herbalist = Character(game.__dict__['herbalist'].name)
    define doctor = Character(game.__dict__['doctor'].name)
    define butcher = Character(game.__dict__['butcher'].name)
    define widow = Character(game.__dict__['widow'].name)
    define alina = Character(game.__dict__['nazi'].name)
    define noah =  Character(game.__dict__['noah'].name)
    define mila =  Character(game.__dict__['mila'].name)
      
    #play music "automato.ogg" fadein 1.0
    #$ renpy.block_rollback()
    #call nameask
    #call hintcheck
    #call intro_sequence
    #show bachnight with dissolve
    $ game.playerbackground = "woodsman"
    "Jason or Angus?"
    menu:
        "Angus":
            jump angus
        "Jason":
            "What background ????"
            menu:
                "marked":
                    $ game.playerbackground = "marked"
                
                "woodsman":
                    $ game.playerbackground = "woodsman"
                
                "merchant":
                    $ game.playerbackground = "merchant"
                
                "deserter":
                    $ game.playerbackground = "deserter"
        "Debug":
            jump debugScenes
                
    jump prolog_run

label nameask:
    $ game.player_name = renpy.input("What is your name, Magical Boy?")
    $ game.player_name = game.player_name.strip()
    return
label hintcheck:
    menu:
        "First time playing / I want an overview of the game's mechanics":
            $ hints = 1
        "I am a seasoned veteran / Skip overview and hints":
            $ hints = 0
    return
label intro_sequence:
    show text "Winter is fast approaching." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "The harvest was plentiful this year, although with prosperity comes a certain measure of greed." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "Tensions between influential members of the community have been strained recently, and without intervention could evolve into something more sinister." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "I think it's usually this time that the crier would be waking you, but it's still very dark" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show ssnow zorder 2
    with Pause(1)
    $ flash = Fade(.25, 0, .75, color="#fff")
    return


"""
_________A______________ C______________ T______________        O______________ N______________ E______________ ####################################################

"""

label act1start:
    "<ACT 1 START>"
    call gameloop
    jump end




screen Mapscreen(food = game.food,fuel = game.fuel, herbs = game.herbs, pelts = game.pelts):
    text "{color=#f00}Day [game.day] // Actions left: [game.actions]{/color}" xalign 0.01 yalign 0
    text "{color=#f00}Food: [food]{/color}" xalign 0.99 yalign 0
    text "{color=#f00}Fuel: [fuel]{/color}" xalign 0.99 yalign 0.05
    text "{color=#f00}Herbs: [herbs]{/color}" xalign 0.99 yalign 0.1
    text "{color=#f00}Pelts: [pelts]{/color}" xalign 0.99 yalign 0.15

    text "{color=#f00}Healthy: [game.popHealthy]{/color}" xalign 0.99 yalign 0.25
    text "{color=#f00}Ill: [game.popIll]{/color}" xalign 0.99 yalign 0.3
    text "{color=#f00}Dead: [game.popDead]{/color}" xalign 0.99 yalign 0.35
    text "{color=#f00}Morale: [game.popMorale]{/color}" xalign 0.99 yalign 0.4
    text "{color=#f00}Cohesion: [game.popCohesion]{/color}" xalign 0.99 yalign 0.45
    text "{color=#f00}Medicine: [game.medicine]{/color}" xalign 0.99 yalign 0.5
    text "{color=#f00}Alcohol: [game.alcohol]{/color}" xalign 0.99 yalign 0.55

label maploop:
    scene mapscreen1
    show screen Mapscreen
    menu:
        "Herbalist":
            call herbs
        "River":
            call river
        "Woods":
            call woods
        "Inn":
            call inn
        "Tower":
            call tower
        "Town Proper":
            call maptown
    return


label maptown:
    scene town_map
    show screen Mapscreen
    menu:
        "Home":
            call home
        "Town Hall":
            call hall
        "Landowner":
            call landowhouse
        "Widow":
            call widowhouse
        "Butcher":
            call butcherhouse
        "Doctor":
            call doctorhouse
        "Approach Nat, the Town Crier" if game.crier.scene == 1:
            call crierscene1
            $game.crier.scene += 1
            $game.actions -= 1
        "Is that .. Nat?" if game.crier.scene == 4:
            call crierscene4
            $game.crier.scene += 1
            $game.actions -= 1
        "Run towards the screams" if game.crier.scene == 8:
            call crierscene8
            $game.crier.scene += 1
            $game.actions -= 1
        "You find Nat in the street" if game.crier.scene == 9 and game.creaturefate == 'Dead':
            call crierscene9
            $game.crier.scene += 1
            $game.actions -= 1
        "Talk to the Alderman" if game.alderman.scene == 7:
            call aldermanscene7
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "A crowd is gathering in the square" if game.alderman.scene == 8 and game.coup == 'Not Involved':
            call aldermanscene8
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Another crowd has gathered in the square" if game.alderman.scene == 9:
            call aldermanscene9
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Is that a chair in the street?" if game.butcher.scene == 3:
            call butcherscene3
            $game.butcher.scene += 1
            $game.actions -= 1
        "Approach the crowd in the square" if game.butcher.scene == 7:
            call butcherscene7
            $game.butcher.scene += 1
            $game.actions -= 1
        "Go back":
            call maploop
    return

label home:
    scene home_intr
    show screen Mapscreen
    menu:
        "Take a nap":
            "You doze off"
            $ game.actions -= 1

        "Sleep the entire day away":
            "Oh no"
            $ game.actions = 0
        "Read the note that has been slipped under your door" if game.crier.scene == 6:
            call crierscene6
            $game.crier.scene += 1
            $game.actions -= 1
        "You hear a knock at your door" if game.crier.scene == 9 and game.creaturefate != 'Dead':
            call crierscene9
            $game.crier.scene += 1
            $game.actions -= 1
        "You hear a knock at your door" if game.alderman.scene == 8 and game.coup != 'Not Involved':
            call aldermanscene8
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "You hear a knock at your door" if (game.butcher.resp > 25 or game.butcher.romance == True) and game.butcher.scene == 8:
            call butcherscene8
            $ game.butcher.scene += 1
            $ game.actions -= 1
        "Get out of bed" if game.butcher.scene == 9:
            call butcherscene9
            $ game.butcher.scene += 1
            $ game.actions -= 1
        "Go back":
            call maptown
    return

label widowhouse:
    scene widow_intr
    show screen Mapscreen
    show widowimg at right
    menu:
        "Go back":
            call maptown
    return

label hall:
    scene hall_intr
    show screen Mapscreen
    menu:
        "Look for the Alderman" if game.alderman.scene == 1:
            call aldermanscene1
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Speak with the Alderman" if game.alderman.scene == 3:
            call aldermanscene3
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Speak with the Alderman" if game.alderman.scene == 4:
            call aldermanscene4
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Seek out the Alderman" if game.alderman.scene == 5:
            call aldermanscene5
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Go back":
            call maptown
    return


label landowhouse:
    scene landow_intr
    show screen Mapscreen
    show landownerimg at right
    menu:
        "Go back":
            call maptown
    return


label butcherhouse:
    scene butcher_intr
    show screen Mapscreen
    show butcherimg at right
    menu:
        "Go back":
            call maptown
        "Approach the butcher" if game.butcher.scene == 1:
            call butcherscene1
            $game.butcher.scene += 1
            $game.actions -= 1
        "Approach Mik" if game.butcher.scene == 2:
            call butcherscene2
            $game.butcher.scene += 1
            $game.actions -= 1
        "Step inside" if game.butcher.scene == 4:
            call butcherscene4
            $game.butcher.scene += 1
            $game.actions -= 1
        "Approach Mik" if not(game.butcher.resp > 25 or game.butcher.romance == True) and game.butcher.scene == 8:
            call butcherscene8
            $ game.butcher.scene += 1
            $ game.actions -= 1
    return


label doctorhouse:
    scene doctor_intr
    show screen Mapscreen
    show doctorimg at right
    menu:
        "Go back":
            call maptown
    return


label herbs:
    scene herbs_intr
    show screen Mapscreen
    
    menu:
        "Go back":
            call maploop
    return


label river:
    scene river_extr
    show screen Mapscreen
    "You come to the river."
    if game.alderman.scene == 2:
        "You see a figure, wrapped in blankets, sitting on the riverbank."
    menu:
        "Go Fishing":
            menu:
                "fish 1":
                    if game.event_check(1) == True:
                        $ game.event_choose('river')
                        "event"
                    else:
                        $ game.playerHarvest("fish",1)
                        "fish 1"
                "fish 2" if game.actions > 1:
                    if game.event_check(2) == True:
                        $ game.event_choose('river')
                        "event"
                    else:
                        $ game.playerHarvest("fish",2)
                        "fish 2"
                "fish 3" if game.actions > 2:
                    if game.event_check(3) == True:
                        $ game.event_choose('river')
                        "event"
                    else:
                        $ game.playerHarvest("fish",3)
                        "fish 3"
        "Approach the blanketed figure" if game.alderman.scene == 2:
            call aldermanscene2
            $ game.alderman.scene += 1
            $ game.actions -= 1
            
            
        "Join Nat by the river" if game.crier.scene == 2:
            call crierscene2
            $game.crier.scene += 1
            $game.actions -= 1
        "(debug) the threesome event":
            call thethreesome
        "(debug) the leviathan event":
            call theleviathan
        "(debug) the hut by the river event":
            call thehutbytheriver
        "Go back":
            call maploop
    return


label inn:
    scene inn_intr
    show screen Mapscreen
    menu:
        "Sit with the Alderman" if game.alderman.scene == 6:
            call aldermanscene6
            $ game.alderman.scene += 1
            $ game.actions -= 1
        "Approach Mik" if game.butcher.scene == 5:
            call butcherscene5
            $game.butcher.scene += 1
            $game.actions -= 1
        "Go back":
            call maploop
    return


label woods:
    scene woods_extr
    show screen Mapscreen
    menu:
        "Gather Wood":
            menu:
                "gather wood 1":
                    if game.event_check(1) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("gather",1)
                        "gather wood 1"
                "gather wood 2":
                    if game.event_check(2) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("gather",2)
                        "gather wood 2"
                "gather wood 3" if game.actions > 2:
                    if game.event_check(3) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("gather",3)
                        "gather wood 3"
            

        "Forage":
            menu:
                "forage herbs 1":
                    if game.event_check(1) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("forage",1)
                        "forage herbs 1"
                "forage herbs 2" if game.actions > 1:
                    if game.event_check(2) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("forage",2)
                        "forage herbs 2"
                "forage herbs 3" if game.actions > 2:
                    if game.event_check(3) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("forage",3)
                        "forage herbs 3"
            
        "Hunt":
            menu:
                "hunt 1":
                    if game.event_check(1) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("hunt",1)
                        "hunt 1"
                "hunt 2" if game.actions > 1:
                    if game.event_check(2) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("hunt",2)
                        "hunt 2"
                "hunt 3" if game.actions > 2:
                    if game.event_check(3) == True:
                        $ game.event_choose('forest')
                        "event"
                    else:
                        $ game.playerHarvest("hunt",3)
                        "hunt 3"
        "Walk through the forest" if game.butcher.scene == 6:
            call butcherscene6
            $game.butcher.scene += 1
            $game.actions -= 1
        "(debug) the stag event":
            call thestag
        "(debug) the ghouls event":
            call theghouls
        "(debug) the lovers event":
            call thelovers
        
        "Go back":
            call maploop
    return

label woodsFamiliarise:
    "You familiarise yourself with the woods"
    $ exploredWoods = 1
    return

label tower:
    scene tower_intr
    show screen Mapscreen
    menu:
        "Look for Nat" if game.crier.scene == 3:
            call crierscene3
            $game.crier.scene += 1
            $game.actions -= 1
        "Look for Nat" if game.crier.scene == 5:
            call crierscene5
            $game.crier.scene += 1
            $game.actions -= 1
        "Look for Nat" if game.crier.scene == 7:
            call crierscene7
            $game.crier.scene += 1
            $game.actions -= 1
        "Go back":
            call maploop
    return


label char_gen:
    
    #"How old are you?"
    #menu:
    #    "A young'un":
    #        $ age = 0
    #        $ wits, lore, grit, vigour, fantasy = 2, 1, 1, 2, 5
    #    "An adult":
    #        $ age = 1
    #        $ wits, lore, grit, vigour, fantasy = 2, 2, 3, 3, 1
    #    "An elder":
    #        $ age = 2
    #        $ wits, lore, grit, vigour, fantasy = 2, 3, 2, 1, 3
    "<You are a person. A person with a past.>"
    "Who were you before?"
    menu:
        "Deserter":
            $ profession = "deserter"
            $ combat = 50
            $ evade = 30
            "You used to be a soldier before you abandoned your post, tired of all the death."
            "You're still not bad in a fight but you've spent much of your time in the village worried that your past will one day catch up with you."
        "Woodsman":
            $ profession = "woodsman"
            $ gather = 50
            $ forage = 30
            "Born near the edge of the `Harath'Garr' forest, you have spent most of your waking days amongst the trees."
            "In these barren and fruitless times, your home has been reduced to nothing but ash in an attempt to appease the Gods."
            "The search for a new life purpose has driven you here."
            "You have left nothing but memories and, of course, your trusty axe."
        "Butcher":
            $ profession = "butcher"
            $ butchery = 50
            $ crafts = 30
        "Craftsman":
            $ profession = "craftsman"
            $ crafts = 50
            $ butchery = 30
        "Hunter":
            $ profession = "hunter"
            $ hunt = 50
        "Herbalist":
            $ profession = "herbalist"
            $ forage = 50
            $ gather = 30
        "Marked":
            $ profession = "marked"
            $ fantasy = 6
            "You're a strange one, there's no doubt about that; there's always been something funny about you."
            "You can see things that others can't and all the dark and uncanny things in the woods always seem to find you."
    
    "That was how it used to be. But things have changed."
    "The people of VILLAGE look to you now, in these desperate times, to help in any way that you can."
    jump prolog_run






