# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import random
    
    random.seed()
    from game import Charac
    from game import Game
    game = Game()
    
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
            self.max_particles = max_particles
            
            self.speed = speed
            
            self.wind = wind
            
            self.xborder = xborder
            self.yborder = yborder
            
            self.depth = kwargs.get("depth", 10)
            
            self.image = self.image_init(image)
            

        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            if particles is None or len(particles) < self.max_particles:
                
                depth = random.randint(1, self.depth)
                
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
            
            for depth in range(self.depth):
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
            
            self.image = image
            
            if speed <= 0:
                speed = 1
                
            self.wind = wind
            
            self.speed = speed

            self.oldst = None
                      
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
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
               
            if self.ypos > renpy.config.screen_height or\
               (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                return None
                
            return int(self.xpos), int(self.ypos), st, self.image

    



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
define crier = Character(game.__dict__['crier'].name)




    

""" CHANGE THIS """
label start:
    play music "automato.ogg" fadein 1.0
    #$ renpy.block_rollback()
    $ player_name = renpy.input("What is your name, Magical Boy?")
    $ player_name = player_name.strip()
    menu:
        "First time playing / I want an overview of the game's mechanics":
            $ hints = 1
        "I am a seasoned veteran / Skip overview and hints":
            $ hints = 0
    
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
    #show bachnight with dissolve
    jump prolog_run

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
    if prologB == 2:
        "You lie in bed, feeling restless. You find yourself going through a cycle."
        "As good a starting point as any is your restlessness, the way your mind cannot help but think and your body itches to move."
        "Then you try and quell this by thinking how you should sleep, but this comes with its own problems."
        "You cannot convince yourself that you are tired, so you bargain, you point out that you are offering something very rare: extra sleep."
        "But then you start thinking about that. How can it be extra sleep if it is still the middle of the night?"
        "How can i feel that if I slept now I would be getting more sleep than usual, when in fact I have already had less?"
        "Then, despite yourself, you start to worry. But either you think what Nat has said was ridiculous, or it scares you too much, so you distract yourself with other thoughts, and then your body starts to become fidgety and the process starts again."
        "Only a knock on the door finally brings you out of it."

        innkeeper "%(player_name)s, are you there? (It's the Innkeeper) You need to come out, Alderman's getting everyone together down in the town square."
        "You quickly throw on some clothes and open the door."
        innkeeper "Ah good. Sorry to drag you out like this, but it's important, I think. I'd explain, but it's probably best to let the Alderman do it."
        innkeeper "I'm just here because I happened to be around when he decided he wanted folks rounded up. Say, you wouldn't mind doing me a favour would you?"
        innkeeper "I suspect Mik (The Butcher) isn't going to shift for me, we had a falling out over how much I charge for their pies, and they certainly aren't going to shift for the Alderman."
        innkeeper "Could you go and speak to them?"
        menu:
            "Alright":
                innkeeper "Thanks %(player_name)s, I'll owe you one. Maybe I'll get you one of those pies, throw a bone to Mik and their spirit of sharing."
                "The walk to Mik's is short, they live a little further down your own street, but you are wishing that you had put more layers on by the time you arrive."
                "You knock heavily on the door to the shop, knowing, as everyone in town does, that Mik sleeps under the counter."
                "The door is answered quickly, Mik already awake and dressed, apron draped over one shoulder and eyes lightly painted with purple shadow. Despite this, they still start with:"
                butcher "It's the middle of the night, %(player_name)s. I presume you've not come to apologise for Nat's racket?"
                menu:
                    "Actually I have.":
                        $ prologG = 1
                    "The Alderman is calling a town meeting, probably about Nat's... thing.":
                        $ prologG = 2
                $ innkeeperLike += 1
                call prolog_sceneG
            "I'm not taking that on. I'll see you at the town square.":
                pass

            
        
    else:
        if prologB == 1:
            "You catch up with Nat as he comes level with the Alderman's house, the front door of which slides open to reveal Karl, the Alderman."
        elif prologB == 4:
            "You walk beside Nat along the dark road until you reach the Alderman's house, the front door of which slides open to reveal Karl, the Alderman."
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
                jump prolog_sceneD
            "No, it’s clearly the middle of the night and I’m going back to bed":
                $ prologB = 2
                $ aldermanResp -= 1
                jump prolog_sceneB
    jump prolog_square


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

label prolog_sceneD:
    "You head into the Alderman's house <desc> and quickly find there's no water for the kettle."
    # this sentence is wack
    "You leave, walk to the well, get the water and bring it back, build a fire and tend it, boil the water and find some bread and butter."
    "It is still dark by the time you bring it all out. Karl thanks you, and asks if you can walk to (The Doctor) Chaney's house and bring her."
    "You walk the short distance and knock on her door. She opens it quickly, already dressed in her full uniform."

    doctor "Ah, %(player_name)s, what can I do for you?"

    "you explain quickly: Nat has been waking everyone claiming that it is time to rise and the Alderman thinks that something may be wrong with him."

    doctor "Curious. I was already up myself and I was sure it should be light by now... maybe I just heard the commotion in the distance and that woke me up."
    doctor "Still, I do feel as though I've had a good night's sleep. It can't be that long til sun up."
    doctor "Anyway, let's go have a look at the poor man. He's such a dear, but I must say I'm not surprised something like this has happened."
    doctor "He has such an amazing gift and sadly these things often come with a price: unseen stresses than can result in illness if not alleviated."
    doctor "It's so unfair, but I suppose no more unfair than a broken leg or a bad cut."

    "You walk back across to the bench to find Nat pacing quickly back and forth, the Alderman standing to one side gently trying, and failing, to keep him calm."

    crier "But the sun always rises, it's just how things are. But if the sun doesn't rise, then we're going to run out of oil for the lamps."
    crier "We're going to run out of oil for the lamps Mr Alderman."
    crier "And it's already getting cold, already getting cold and we'll need more wood for fires, and that's alright and it's alright..."
    crier "...But wood doesn't grow without sunlight... Oh Gods, Sir, the crops!"
    crier "If the sun doesn't rise, Sir, what of the crops?"

    "Chaney and you reach the bench before Nat can continue his downward spiral."

    doctor "Good morning, Nat. %(player_name)s tells me that you're worried about the dark."
    doctor "And you are right, if the sun doesn't rise then bad things will happen, you're right that the crops and trees need sun to grow."
    doctor "But we're not going to get anywhere by worrying about it like that."
    doctor "I know it's hard, but why don't we just sit down and talk about it, you, me and the Alderman. And %(player_name)s can run to (The Herbalist) Lizbett's and get her to bring her basket and we can get you something to calm you down."
    doctor "I promise you, it won't affect your count, not if we do it just this once."
    doctor "{i}Chaney turns to you and smiles.{/i} Sorry to make you do this, I'll buy you a drink at the Flying Donkey later to make up for it, okay? You're a good friend."

    "You take the long walk to Lizbett's cottage, just outside of town. By the time you reach it a light snow has begun to fall."
    "The sun has not risen."
    "Like Chaney, Lizbett answers the door almost immediately when you knock."

    herbalist "Ah, %(player_name)s, I'm glad to see you dear. I woke with a sense that something was wrong, but I'm glad that you have come to tell me what it is."
    menu:
        "The sun hasn't risen":
            $ prologE = 1
        "There's something wrong with Nat, Chaney wants you to bring your herbs":
            $ prologE = 2
    $ aldermanResp += 1
    $ doctorResp += 1
    if prologE == 1:
        herbalist "Oh dear. Oh deary me. I suppose Nat has confirmed it?"
        "You nod."
        herbalist "Oh dear. He'll be struggling, that's why you've come to me really isn't it, to bring herbs for Nat?"
        "Again you nod."
        herbalist "Of course. Wait one moment while I fetch my basket."
        "She disappears back inside her small cabin, which smells strongly of earth even from outside, and reappears again with a large wicker basket in the nook of one arm."
        herbalist "We should go, and fast."
        herbalist "I'm afraid I'm a little too old now to march and talk at the same time, but I just want to apologise for my shock. I feel I must be honest with someone, and since you are here it might as well be you."
        herbalist "This is bad, very bad. Even if it is just a sign, people will be scared. We've got a good community here %(player_name)s, good people, but we'll have to pull together because of this. Otherwise..."
        herbalist "But we must hurry, enough of this chatter. But oh, thank you for telling me."
        herbalist "Others might not have believed Nat, but he's honest and true and taking his word shows that you are too."
        $ herbalistResp += 1

    elif prologE == 2:
        herbalist "A panic attack, it sounds like {i}she says after you explain how he's been acting.{/i} That's not like Nat."
        herbalist "It makes me worried. The poor dear does have his moments, but I've always felt that he was blessed by his happiness."
        herbalist "Something very bad must have happened. Oh dear. Let's get there quickly, I don't like the idea of keeping him in that state."
        herbalist "Let me just grab my basket and we'll go."
        "She disappears back inside her small cabin, which smells strongly of earth even from outside, and reappears again with a large wicker basket in the nook of one arm."
        herbalist "You're a dear for coming all the way out here for Nat's sake. Now let's get going."
        "With that she bustles down the dirt path and towards the centre of town."
        $ herbalistLike += 1
    return

label prolog_sceneG:
    "beans"
    return
label prolog_square:
    "beans"
""" 

_________A______________ C______________ T______________        O______________ N______________ E______________ ####################################################

"""

label act1start:
    "t his is the bugening f the game lol"
    call gameloop
    jump end


label endDayChoices:


label gameloop:
    while game.day < 30:
        call wakeup
        while game.actions > 0:
            call maploop
            $ game.actions -= 1
        call sleep
    
    jump end

label wakeup:
    scene home_intr
    $ game.weatherMake()
    $ day = game.day
    "you wake up! it is day [day]."
    $ precip = game.weatherPrecip
    $ wind = game.weatherWind
    $ cold = game.weatherCold
    "It is precipitation [precip], wind [wind] and cold [cold]"
    $ doodoo = game.adjectivePrecip[game.weatherPrecip]
    $ deedee = game.adjectiveWind[game.weatherWind]
    $ daadaa = game.adjectiveCold[game.weatherCold]
    crier "Time to rise everybody!"
    "You stretch your eyes open; it must be 'morning' again."
    "Nat continues to shamble his way down the streets, welcoming everyone back into the embrace of the endless night."
    "Wandering over to the window, you see that it is [doodoo] outside."
    if game.weatherWind > 0:
        "From the creaking of your wooden beams it must be [deedee]."
    "Cracking open your window slightly to replace some of the musty air, the wind that blows in is [daadaa] to the touch."

    "New Recovered: [game.newRecovered]  New Ill:[game.newIll]  New Dead: [game.newDead]"
    "Healthy: [game.popHealthy]  Ill:[game.popIll]  Dead: [game.popDead]"
    return
        #### DETERMINE HOW PEOPLE TAKE ILL
        

label sleep:
    scene home_intr
    "you go to sleep after a long day of toil"
    $ food, fuel, herbs, pelts = game.foodstuffs(), game.fuel, game.herbs, game.pelts
    $ game.advanceDay()
    show screen Mapscreen(str(food) + ' (+ ' + str(game.foragedfoodstuffs()) + ')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ')')
    "Workers add resources to the stockpiles"
    show screen Mapscreen(str(food) + ' (+ ' + str(game.foragedfoodstuffs()) + ' + ' + str(game.playerfoodstuffs())+')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ' + ' + str(game.playerFuel)+')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ' + ' + str(game.playerHerb)+')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ' + ' + str(game.playerPelts)+')')
    "You add your harvest to the pile"
    show screen Mapscreen
    "Morale/Cohesion change"
    call playerChoices
    $ game.advanceNight()
    return


label playerChoices:
    "Food choice"
    menu:
        "food choice 1":
            "result 1"
        "food choice 2":
            "result 2"
        "food choice 3":
            "result 3"
    "Fuel choice"
    menu:
        "fuel choice 1":
            "result 1"
        "fuel choice 2":
            "result 2"
        "fuel choice 3":
            "result 3"
    "Herbs choice"
    menu:
        "herbs choice 1":
            "result 1"
        "herbs choice 2":
            "result 2"
        "herbs choice 3":
            "result 3"
    "Pelts choice"
    menu:
        "pelts choice 1":
            "result 1"
        "pelts choice 2":
            "result 2"
        "pelts choice 3":
            "result 3"
    return

screen Mapscreen(food = game.foodstuffs(),fuel = game.fuel, herbs = game.herbs, pelts = game.pelts):
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

label maploop:
    scene main_map
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
        "Go back":
            call maploop
    return

label home:
    scene home_intr
    show screen Mapscreen
    menu:
        "Take a nap":
            "You doze off"

        "Sleep the entire day away":
            "Oh no"
            $ game.actions = 1

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
    menu:
        "Go Fishing":
            if game.rollevent == 1: # 1 of the 4 actions
                $ fishfunc = random.randint(1,100)
                if fishfunc > 95:
                    "eventvrare"
                elif fishfunc > 90:
                    "eventvrare"
                elif fishfunc > 85:
                    "eventrare"
                elif fishfunc > 80:
                    "eventrare"
                elif fishfunc > 70:
                    "eventuncommon"
                elif fishfunc > 60:
                    "eventuncommon"
                elif fishfunc > 50:
                    "eventuncommon"
                elif fishfunc > 40:
                    "eventcommon"
                elif fishfunc > 30:
                    "eventcommon"
                elif fishfunc > 20:
                    "eventcommon"
                elif fishfunc > 10:
                    "eventcommon"
                else:
                    "done all events lol"
                if random.randint(1,2)>1:
                    $ rollevent = random.randint(1,4)
                else:
                    $ rollevent = 0
            else:
                "get fish"
                $foodFish += 6 + random.randint(1,6)

        "Investigate the light in the distance" if weatherCold > 2:
            "You begin walking."
            "You follow along the river as it winds up to a fork, you see that the light you were chasing is on the other side, it must be at the end of the other section of the river."
            menu:
                "Go back while you can":
                    call river
                "Try to cross to the other side":
                    call lighthouse
        "Go back":
            call maploop
    return

label lighthouse:
    scene river_extr
    "HAAAAAARK"

label inn:
    scene inn_intr
    show screen Mapscreen
    menu:
        "Go back":
            call maploop
    return


label woods:
    scene woods_extr
    show screen Mapscreen
    menu:
        "Gather Wood":
            if game.rollevent == 2: # 1 of the 4 actions
                $ gatherfunc = random.randint(1,100)
                if gatherfunc > 95:
                    "eventvrare"
                elif gatherfunc > 90:
                    "eventvrare"
                elif gatherfunc > 85:
                    "eventrare"
                elif gatherfunc > 80:
                    "eventrare"
                elif gatherfunc > 70:
                    "eventuncommon"
                elif gatherfunc > 60:
                    "eventuncommon"
                elif gatherfunc > 50:
                    "eventuncommon"
                elif gatherfunc > 40:
                    "eventcommon"
                elif gatherfunc > 30:
                    "eventcommon"
                elif gatherfunc > 20:
                    "eventrcommon"
                elif gatherfunc > 10:
                    "eventcommon"
                else:
                    "done all events lol"
                if random.randint(1,2)>1:
                    $ game.rollevent = random.randint(1,4)
                else:
                    $ rollevent = 0
            else:
                "get fuel"

        "Forage":
            if rollevent == 3: # 1 of the 4 actions
                $ foragefunc = random.randint(1,100)
                if foragefunc > 95:
                    "eventvrare"
                elif foragefunc > 90:
                    "eventvrare"
                elif foragefunc > 85:
                    "eventrare"
                elif foragefunc > 80:
                    "eventrare"
                elif foragefunc > 70:
                    "eventuncommon"
                elif foragefunc > 60:
                    "eventuncommon"
                elif foragefunc > 50:
                    "eventuncommon"
                elif foragefunc > 40:
                    "eventcommon"
                elif foragefunc > 30:
                    "eventcommon"
                elif foragefunc > 20:
                    "eventrcommon"
                elif foragefunc > 10:
                    "eventcommon"
                else:
                    "done all events lol"
                if random.randint(1,2)>1:
                    $ rollevent = random.randint(1,4)
                else:
                    $ rollevent = 0
            else:
                "get herb n veg"
        "Hunt":
            if rollevent == 4: # 1 of the 4 actions
                $ huntfunc = random.randint(1,100)
                if huntfunc > 95:
                    "eventvrare"
                elif huntfunc > 90:
                    "eventvrare"
                elif huntfunc > 85:
                    "eventrare"
                elif huntfunc > 80:
                    "eventrare"
                elif huntfunc > 70:
                    "eventuncommon"
                elif huntfunc > 60:
                    "eventuncommon"
                elif huntfunc > 50:
                    "eventuncommon"
                elif huntfunc > 40:
                    "eventcommon"
                elif huntfunc > 30:
                    "eventcommon"
                elif huntfunc > 20:
                    "eventrcommon"
                elif huntfunc > 10:
                    "eventcommon"
                else:
                    "done all events lol"
                if random.randint(1,2)>1:
                    $ rollevent = random.randint(1,4)
                else:
                    $ rollevent = 0
            else:
                "get meat n pelts"
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






