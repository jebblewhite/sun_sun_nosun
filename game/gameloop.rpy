label gameloop:
    while game.day < 30:
        $ game.actions = 5
        $ game.initday()
        show screen Mapscreen
        call wakeup
        $ game.resetvars()
        while game.actions > 0:
            call maploop
        $ game.endofday()
        call endoday
        $ game.initnight()
        call sleep
    
    jump end

label endDayChoices:




label wakeup:
    scene home_intr
     # place holder stuff VVV
    #call wakemessage
    "You wake up"
    "The weather is shit"
    "temp: [game.temp], wind: [game.windadj], precipitation: [game.precipadj]"
    scene town_map
    "You trudge along to the town centre where workers are gathering to leave for the woods"
    "new ill: [game.new_ill], new dead: [game.new_dead]"
    "new recovering: [game.new_recovering], new buried: [game.new_buried]"
    "Overall (morale,cohesion) change : ([game.moralechange],[game.cohesionchange])"
    return
        #### DETERMINE HOW PEOPLE TAKE ILL

label endoday:
    scene town_map
    "You end the day in the same place you started: the town center"
    return

label sleep:
    scene home_intr
    return

label wakemessage:
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

label sleep2:
    scene home_intr
    "you go to sleep after a long day of toil"
    $ food, fuel, herbs, pelts = game.food, game.fuel, game.herbs, game.pelts
    $ game.advanceDay()
    show screen Mapscreen(str(food) + ' (+ ' + str(game.huntedFood+game.fishedFood) + ')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ')')
    "Workers add resources to the stockpiles"
    show screen Mapscreen(str(food) + ' (+ ' + str(game.huntedFood+game.fishedFood) + ' + ' + str(game.playerhuntedFood+game.playerfishedFood)+')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ' + ' + str(game.playerFuel)+')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ' + ' + str(game.playerHerb)+')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ' + ' + str(game.playerPelts)+')')
    "You add your harvest to the pile"
    show screen Mapscreen
    "Morale/Cohesion change"
    call playerChoices
    call eventBlock
    $ game.advanceNight()
    return


label playerChoices:
    show screen Mapscreen
    "Food choice"
    menu:
        "food choice 0.5pp":
            "result 1"
            $ game.foodchoice = 1
        "food choice 1pp":
            "result 2"
            $ game.foodchoice = 2
        "food choice 2pp":
            "result 3"
            $ game.foodchoice = 3
    $ game.updateFood()
    show screen Mapscreen
    "Fuel choice"
    menu:
        "fuel choice 0.5pp":
            "result 1"
            $ game.fuelchoice = 1
        "fuel choice 1pp":
            "result 2"
            $ game.fuelchoice = 2
        "fuel choice 2pp":
            "result 3"
            $ game.fuelchoice = 3
    $ game.updateFuel()
    show screen Mapscreen
    "Herbs -> Medicine or Alcohol?"
    menu:
        "All Medicine (10\% bonus yield)":
            "result 1"
            $ game.herbchoice = 1
        "All Alcohol (10\% bonus yield)":
            "result 2"
            $ game.herbchoice = 2
        "Evenly split":
            "result 3"
            $ game.herbchoice = 3
    $ game.updateHerb()
    show screen Mapscreen
    
    return

label eventBlock:
    if game.eventstag == True and game.eventstagnight == False:
        call thestagnight
        $ game.eventstagnight = True
    return