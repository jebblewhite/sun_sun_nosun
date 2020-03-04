# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    
    #################################################################
    # Here we use random module for some random stuffs (since we don't
    # want Ren'Py saving the random number's we'll generate.
    import random
    import numpy as np
    
    # initialize random numbers
    random.seed()
    
    #################################################################
    # Snow particles
    # ----------------
    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)
        
        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.
        
        @parm {int} max_particles:
            The maximum number of particles at once in the screen.
            
        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1
            
        @parm {float} wind:
            The max wind force that'll be applyed to the particles.
            
        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.
            
        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))
    
    # ---------------------------------------------------------------
    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """            
            # the maximum number of particles we can have on screen at once
            self.max_particles = max_particles
            
            # the particle's speed
            self.speed = speed
            
            # the wind's speed
            self.wind = wind
            
            # the horizontal/vertical range to create particles
            self.xborder = xborder
            self.yborder = yborder
            
            # the maximum depth of the screen. Higher values lead to more varying particles size,
            # but it also uses more memory. Default value is 10 and it should be okay for most
            # games, since particles sizes are calculated as percentage of this value.
            self.depth = kwargs.get("depth", 10)
            
            # initialize the images
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            # if we can create a new particle...
            if particles is None or len(particles) < self.max_particles:
                
                # generate a random depth for the particle
                depth = random.randint(1, self.depth)
                
                # We expect that particles falling far from the screen will move slowly than those
                # that are falling near the screen. So we change the speed of particles based on
                # its depth =D
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      # the image used by the particle 
                                      random.uniform(-self.wind, self.wind)*depth_speed,  # wind's force
                                      self.speed*depth_speed,  # the vertical speed of the particle
                                      random.randint(self.xborder[0], self.xborder[1]), # horizontal border
                                      random.randint(self.yborder[0], self.yborder[1]), # vertical border
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.            
            """
            rv = [ ]
            
            # generate the array of images for each possible depth value.
            for depth in range(self.depth):
                # Resize and adjust the alpha value based on the depth of the image
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )

            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """ 
            return self.image
            
    # ---------------------------------------------------------------
    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            # The image used by this particle
            self.image = image
            
            # For safety (and since we don't have snow going from the floor to the sky o.o)
            # if the vertical speed of the particle is lower than 1, we use 1.
            # This prevents the particles of being stuck in the screen forever and not falling at all.
            if speed <= 0:
                speed = 1
                
            # wind's speed
            self.wind = wind
            
            # particle's speed
            self.speed = speed

            # The last time when this particle was updated (used to calculate the unexpected delay
            # between updates, aka lag)
            self.oldst = None
            
            # the horizontal/vertical positions of this particle            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
            
            
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            # calculate lag
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            # update the position
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            # verify if the particle went out of the screen so we can destroy it.
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                ##  print "Dead"
                return None
                
            # returns the particle as a Tuple (xpos, ypos, time, image)
            # since it expects horizontal and vertical positions to be integers, we have to convert
            # it (internal positions use float for smooth movements =D)
            return int(self.xpos), int(self.ypos), st, self.image

"""
GAME START #########################################################################################################################################
"""
# The game starts here.
label splashscreen:
    scene susnun
    image ssnow = Snow("snowflake.png", max_particles=500, speed=120, wind=200, xborder=(0,100), yborder=(50,400))
    show ssnow zorder 2
    with Pause(1)
    #play sound "audio/well_done.ogg"
    show text "A Game by A. Barker, J. Ebblewhite, and M. van Mesdag" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    #play sound "audio/undead-1.ogg"
    show text "Untitled Sun Game" with dissolve
    with Pause(2)
return
""" CHARACTERS AND VARIABLES LOAD """
# CHARACTERS and scenes DEFINED
define jim = Character("Dead Jim")
define crier = Character("Nat")
define butcher = Character("Zish")
define herbalist = Character("Lizbett")
define widow = Character("Sadana")
define alderman = Character("Karl")
define landowner = Character("Brenda")
define doctor = Character("Chaney")
define innkeeper = Character("Stu")

init python:
    crierLike = 0
    crierResp = 0
    crierAtt = 0
    butcherLike = 0
    butcherResp = 0
    butcherAtt = 0
    herbalistLike = 0
    herbalistResp = 0
    herbalistAtt = 0
    widowLike = 0
    widowResp = 0
    widowAtt = 0
    aldermanLike = 0
    aldermanResp = 0
    aldermanAtt = 0
    landownerLike = 0
    landownerResp = 0
    landownerAtt = 0
    doctorLike = 0
    doctorResp = 0
    doctorAtt = 0
    innkeeperLike = 0
    innkeeperResp = 0
    innkeeperAtt = 0

    exploredWoods = 0
    exploredRiver = 0
    exploredCave = 0
    exploredCrypt = 0
    

""" CHANGE THIS """
label start:
    #play music "audio/Ove Melaa - Psycho Behind The Keys.mp3"
    show text "You are asleep." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "Mmmmmm sleep" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    show text "Who is the awake you?" with dissolve
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
    #show bachnight with dissolve
    jump char_gen
    # lol
return

label prolog_run:
    jump act1start
    $ prologC = 0
    show text "PROLOGUE" with dissolve
    with Pause(3)
    hide text with dissolve
    scene bachnight
    "Crier (silhouette)"  "Time to rise, time to rise!"
    if profession == "deserter": 
        "But it surely can’t be time yet, it’s too cold, the powder won’t light and the moon isn’t nearly bright enough for you to see, you’ll run blind and straight into their bayonets and oh gods they’ve given up on you and they’re getting rid of you and oh gods-"
    "Crier (silhouette)"  "Time to rise, time to rise!"
    "The dream breaks, something appropriate about how you wake up and open your eyes.  Continuing the previous example: [leaving nothing but the panic, holding you in place before the next call, a voice from a different time and place.  This time.   This place."
    "Your eyes open and for a moment the panic is back.  Was the crier the dream and that dark field the reality?  Did some lucky enemy shot find its mark before you could run and now you are here, opening your eyes onto nothing?"
    "Then the starlight through your thin curtain helps you pick out the angles of your ceiling and you realise where you are.  Home.]  Another noise from outside:"
    "Woman"  "It’s the middle of the night, shut up won’t you!"
    menu:
        "Look out the window":
            $ prologA = 1
            "Across the street your neighbour stands in the doorway to her house, a lamp shaking slightly in her hand.  It illuminates Nat, the town crier, still swinging his bell as he turns to talk to her."
        "Throw on your coat and go outside":
            $ prologA = 2
            "As you get dressed, you hear the conversation continue outside."
        "Stay in bed":
            $ prologA = 3
            "You lie in bed, warm in your rough sheets as you listen to the argument outside."
 
    jump prolog_sceneA


label prolog_sceneA:
    "Crier"  "It’s not I’m afraid Madam, it’s eight-o-four."
    if prologA < 2:
        $ added = " She points up at the sky."
    else:
        $ added = ""
    "Woman"  "No it isn’t, look at that!{i}%(added)s{/i} You’ve finally cracked!  Now stop your ringing and let us go back to bed."

    if prologA == 1:
        "Your neighbour closes the door and goes back inside."
    else:
        "You hear your neighbour’s door close."
    "Crier" "Do you feel like you’ve had enough sleep Madam?  I swear to you, by my gifts, it is eight-o-four, and it is Time to rise, time to rise!"
    if prologA ==1:
        "Across the street your neighbour stands in the doorway to her house, a lamp shaking slightly in her hand.  It illuminates Nat, the town crier, still swinging his bell as he turns to talk to her."
    "Nat goes on chanting as he walks down the street, the sound of his bell slowly disappearing into the night."
    if prologA ==1:
        menu:
            "Follow Nat":
                $ prologB = 1
            "Return to bed":
                $ prologB = 2
    if prologA ==2:
        "You step out into the cool night air, glad you brought your coat.  It’s the cold season, but this is even colder than it should be.  Nat turns to you, and nods grimly."
        crier "Morning there Sir.  It’s time to rise."
        menu:
            "Nod, then ask if you can help him wake people":
                $ prologC = 1
            "Ask him why he thinks that it’s time to rise":
                $ prologC = 2
            "Tell him that the woman was right, he’s cracked and should go home":
                $ prologC = 3
        call prolog_sceneC
    if prologA ==3:
        "Nat goes on chanting as he walks down the street, the sound of his bell slowly disappearing into the night.  As it does, you realise that Nat was right.  Your bed is warm and comforting, but you do not feel like you need it."  
        "Despite yourself, you’ve risen into full wakefulness.  And yet the light sneaking through the holes of your curtain indicates a dark, moonless night."
        menu:
            "Get out of bed and follow Nat":
                $ prologB = 1
            "Stay in bed":
                $ prologB = 2
    jump prolog_sceneB
    return

label prolog_sceneB:
    "The alderman walks towards Nat quickly but calmly, holding out a hand that he gently places on Nat’s shoulder when he comes close enough.  He talks in a hushed, measured voice."
    alderman "What’s all this Nat?  This isn’t like you.  Put the bell down and come have a sit over here with me on the bench and tell me what’s happened to you this morning."
    crier "Nothing out of the ordinary Sir, I woke just before the sun, as I always do, when my counting comes into my dreams to tell my body when to wake up.  So I rose and dressed and went for my rounds.  Normal as any other day Sir, save that the sun hasn’t risen."
    alderman "Nothing out of the ordinary?  You’ve always been right before."
    crier "Nothing strange Sir, nothing save the sun.  Sir, may I tell you something?"
    alderman "Of course Nat, what is it?"
    crier """
    Well Sir, I’m scared.
    I suppose I should be scared about my gift Sir, that something’s gone wrong.  I’ve had people yelling that at me as I’ve passed.  But I’m not scared of that.
    I don’t feel any different.  I’m scared about the sun.  It’s already colder, can you feel it?
    I haven’t really let myself think about it, because I wanted to get everyone up and then we would talk about it and figure out what’s going on.
    But now that I’m talking to you Sir, I’m thinking about it, and I’m scared Sir.  I thought that the sun not rising was supposed to come with devils or floods.  Do you think they’re coming Sir?
    """
    alderman """
    There there Nat, stop your worrying.  I’m sure there’s some reasonable explanation.
    I must admit that I cannot think of any, save that you might have messed up your time a little bit in your sleep, which would be more than understandable Nat given how brilliant what you do is, but I’m sure there are other reasons besides.
    Listen, why don’t we sit here and wait for the sun to rise, okay Nat?
    You, Player, would you kindly do me a few favours?  Poor Nat here is having a little trouble and I think that a nice cup of tea and some breakfast would do him some good.
    Could you go into my house and make something up for him?
    """
    menu:
        "Of course sir":
            $ prologD = 1
        "No, it’s clearly the middle of the night and I’m going back to bed":
            $ prologB = 2


label prolog_sceneC:
    if prologC ==1:
        crier  "That’s very kind of you to offer Sir/Madam.  I don’t think I’ll need help, what with my bell, but a little company would be nice.  Maybe best silent company mind, what with the bell and the calling and the keeping up with the seconds, but I’ll appreciate having you here nonetheless."
        menu:
            "Nod and continue down the road":
                $ prologB = 4
                $ crierLike += 1
    if prologC ==2:
        crier "You don’t know?  Well, I reckon many round here would call you fortunate. {i} He chuckles {/i}  I say that ‘cause I’ve bored most of them with it more times than they can count.  And while I’d love to bore you with it now, I don’t think it’s quite the time, eh?"  
        crier "Let’s just say I have a gift for it.  Don’t matter what happens, I know the time.  But I’ve got people to wake, so I best be off."
        "And with that, he turns and walks down the road, ringing his bell."
        menu:
            "Follow Nat":
                $ prologB = 4
            "Shrug and go back to bed":
                $ prologB = 2
        $ crierLike += 1
    if prologC ==3:
        "Nat looks at you for a moment, his face still save for a slight quiver of his lower lip."
        crier "I may very well have cracked in some way, Sir/Madam, but in this I’m right.  My counting’s as reliable as the sun ri- he chuckles."
        crier "Well I promise you on my gift for counting, ‘cause that’s all I got save my bell and the Alderman won’t be too pleased if he finds I’ve been betting with that, that I’m right.  And as I said to your neighbour, you don’t feel tired, do you?"
        crier "Now if you’ll excuse me, Time to rise, time to rise!"
        "He turns away from you and continues down the street, ringing his bell."
        menu:
            "Follow him":
                $ prologB = 4
            "Ignore the madman and go back to bed":
                $ prologB = 2
    return
""""""
"""
_________A______________ C______________ T______________        O______________ N______________ E______________ ####################################################
"""
""""""
label act1start:
    $ day = 0
    while day<30:
        call wakeup
        $ actions = 5
        while actions > 0:
            call maploop
            $ actions -= 1
        call sleep
        $ day += 1
    jump end
return

label wakeup:
    scene home_intr
    "you wake up!"
    # weather / 
    init python:
        weatherPrecip=0 # dry
        weatherWind=0 # calm
        weatherCold=0 # mild

        precip = (renpy.random.randint(1,70)+day) # ranges from 0-70 day 0, to 30-100 day 30
        if precip > 70:
            weatherPrecip = 2 # snow
        elif precip > 40:
            weatherPrecip = 1 # rain
        
        wind = (renpy.random.randint(1,70)+day) # ranges from 0-70 day 0, to 30-100 day 30
        if wind > 70:
            weatherWind = 2 # gale
        elif wind > 40:
            weatherWind = 1 # breezy

        cold = (precip + wind)*0.5 # ranges from 0-70 day 0, to 30-100 day 30
        if cold > 85:
            weatherCold = 4 # deathly
        elif cold > 65:
            weatherCold = 3 # freezing
        elif cold > 45:
            weatherCold = 2 # brisk
        elif cold > 25:
            weatherCold = 1 # chilly
    return
        #### DETERMINE HOW PEOPLE TAKE ILL
        

label sleep:
    scene home_intr
    "you go to sleep after a long day of toil"
    return

label maploop:
    scene main_map
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
        "Go back":
            call maploop
    return

label home:
    scene home_intr
    menu:
        "Take a nap":
            "You doze off"

        "Go back":
            call maptown
    return

label widowhouse:
    scene widow_intr
    menu:
        "Go back":
            call maptown
    return

label hall:
    scene hall_intr
    menu:
        "Go back":
            call maptown
    return


label landowhouse:
    scene landow_intr
    menu:
        "Go back":
            call maptown
    return


label butcherhouse:
    scene butcher_intr
    menu:
        "Go back":
            call maptown
    return


label doctorhouse:
    scene doctor_intr
    menu:
        "Go back":
            call maptown
    return


label herbs:
    scene herbs_intr
    menu:
        "Go back":
            call maploop
    return


label river:
    scene river_extr
    menu:
        "Go back":
            call maploop
    return


label inn:
    scene inn_intr
    menu:
        "Go back":
            call maploop
    return


label woods:
    scene woods_extr
    menu:
        "Familiarise yourself with the woods" if exploredWoods == 0: # Add more exploration options
            call woodsFamiliarise
        "Gather wood":
            woodsGather
        "Go back":
            call maploop
    return

label woodsFamiliarise:
    "You familiarise yourself with the woods"
    return

label tower:
    scene tower_intr
    menu:
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
return





