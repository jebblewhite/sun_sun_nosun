label gameloop:
    while game.day < 30:
        call wakeup
        while game.actions > 0:
            call maploop
            $ game.actions -= 1
        call sleep
    
    jump end

label endDayChoices:




label wakeup:
    scene home_intr
     # place holder stuff VVV
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
    $ food, fuel, herbs, pelts = game.food, game.fuel, game.herbs, game.pelts
    $ game.advanceDay()
    show screen Mapscreen(str(food) + ' (+ ' + str(game.huntedFood+game.fishedFood) + ')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ')')
    "Workers add resources to the stockpiles"
    show screen Mapscreen(str(food) + ' (+ ' + str(game.huntedFood+game.fishedFood) + ' + ' + str(game.playerhuntedFood+game.playerfishedFood)+')', str(fuel) + ' (+ ' + str(game.gatheredFuel)+ ' + ' + str(game.playerFuel)+')', str(herbs) + ' (+ ' + str(game.foragedHerb)+ ' + ' + str(game.playerHerb)+')', str(pelts) + ' (+ ' + str(game.huntedPelts)+ ' + ' + str(game.playerPelts)+')')
    "You add your harvest to the pile"
    show screen Mapscreen
    "Morale/Cohesion change"
    call playerChoices
    $ game.advanceNight()
    return


label playerChoices:
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
            $ game.foodchoice = 1
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
    "Herbs choice"
    menu:
        "herbs choice 1":
            "result 1"
            $ game.herbchoice = 1
        "herbs choice 2":
            "result 2"
            $ game.herbchoice = 2
        "herbs choice 3":
            "result 3"
            $ game.herbchoice = 3
    "Pelts choice"
    menu:
        "pelts choice 1":
            "result 1"
            $ game.peltchoice = 1
        "pelts choice 2":
            "result 2"
            $ game.peltchoice = 2
        "pelts choice 3":
            "result 3"
            $ game.peltchoice = 3
    return