import random

class Charac(object):
    def __init__(self,like,respect,attract,name,img,ide,characters):
        self.like = like
        self.resp = respect
        self.att = attract
        self.name = name
        self.ide = ide
        self.scene = 1
        characters.append(self)
        print(characters)

    def __str__(self):
        print(self.ide)

    def statchange(self,stat,change):
        self.__dict__[stat] += change
        print(self.name + "'s " + str(stat) + " stat changed by " + str(change))

    def relchange(self,other,change):
        self.__dict__[other.ide] += change
        other.__dict__[self.ide] += change
        print(self.name + " and " + str(other.name) + "'s relationship changed by " + str(change))

    def establishrels(self,characters):
        for i in range(len(characters)):
            if characters[i].ide != self.ide:
                setattr(self, characters[i].ide, 0)



class Peasant(object):
    def __init__(self, name,peasants,children,elders,workers):
        def getRandomAge():
            age = -1
            mu = 40
            sigma = 35
            while age < 1 or age > 80:
                age = int(round(random.gauss(mu, sigma)))
            return age
        self.name = name
        self.age = getRandomAge()
        if self.age > 20:
            self.maxhealth = 120-self.age
        else:
            self.maxhealth = 100

        self.currenthealth = round(3*self.maxhealth/4)

        self.passionHunting = random.randint(random.randint(1,4),random.randint(6,10))
        self.passionFishing = random.randint(random.randint(1,4),random.randint(6,10))
        self.passionForaging = random.randint(random.randint(1,4),random.randint(6,10))
        self.passionGathering = random.randint(random.randint(1,4),random.randint(6,10))

        choice = random.randint(1,4)
        if choice == 1:
            self.passionHunting = random.randint(1,10)
        elif choice == 2:
            self.passionFishing = random.randint(1,10)
        elif choice == 3:
            self.passionForaging = random.randint(1,10)
        else:
            self.passionGathering = random.randint(1,10)

        self.occupation = "General Worker"
        self.status = "Alive and Well"
        self.hasPelt = 0
        self.hasFire = 0
        if self.age > 60:
            self.occupation = "Elder"
            elders.append(self)
        elif self.age < 20:
            self.occupation = "Child"
            children.append(self)
        else:
            workers.append(self)
        peasants.append(self)

class Game(object):
    def __init__(self):
        self.characters = []
        self.crier = Charac(0,0,0,'Nat',"image!!!","crier",self.characters)
        self.butcher = Charac(0,0,0,'Mik',"image!!!","butcher",self.characters)
        self.herbalist = Charac(0,0,0,'Joan',"image!!!","herbalist",self.characters)
        self.widow = Charac(0,0,0,'Elena',"image!!!","widow",self.characters)
        self.landowner = Charac(0,0,0,'Elisabeta',"image!!!","landowner",self.characters)
        self.innkeeper = Charac(0,0,0,'Henryk',"image!!!","innkeeper",self.characters)
        self.doctor = Charac(0,0,0,'Fyodora',"image!!!","doctor",self.characters)
        self.alderman = Charac(0,0,0,'Alexi',"image!!!","alderman",self.characters)
        self.initrels(self.characters)

        self.peasants = []
        self.workers = []
        self.elders = []
        self.children = []

        self.actions = 5
        self.playerFuel, self.playerHerb, self.playerVeg, self.playerMeats, self.playerPelts, self.playerFish = 0,0,0,0,0,0
        

        for i in range(100):
            Peasant('Tudor ' + str(i),self.peasants,self.children,self.elders,self.workers)

        
        self.workersnum = 10
        self.workersorder = 0
        self.initialiseWorkers()

        
        
        self.popHealthy = 100
        self.popIll = 0
        self.popDead = 0
        self.popRecovering = 0
        self.popBuried = 0

        self.newRecovered = 0
        self.newIll = 0
        self.newDead = 0


        self.popMorale = 50
        self.popCohesion = 20


        self.worldherbs = 200
        self.herbs = 20
        self.worldfuel = 1000
        self.fuel = 100
        self.worldpelts = 180
        self.pelts = 0
        self.cereals = 70
        self.worldmeats = 400
        self.meats = 10
        self.worldveg = 500
        self.veg = 10
        self.worldfish = 800
        self.fish = 10


        self.day = 0
        self.adjectivePrecip = ['dry','raining','snowing']
        self.adjectiveWind = ['calm','windy','blowing a gale']
        self.adjectiveCold = ['mild','chilly','brisk','freezing','deathly']

    def initialiseWorkers(self):
        def topWorker(professionlist, occTag, passion):
            tagged = 0
            count = 0
            #print(passion)
            high = sorted(self.workers, key=lambda x: x.__dict__[passion], reverse=True)
            while tagged == 0:
                #print(count)
                #print(high[count].occupation)
                if high[count].occupation == 'General Worker':
                    high[count].occupation = occTag
                    professionlist.append(high[count])
                    tagged = 1
                else:
                    if count<len(high)-1:
                        count += 1
                    else:
                        tagged = 1
            

        self.genworkers = []
        self.hunters = []
        self.gatherers = []
        self.fishermen = []
        self.foragers = []
        if self.workersorder == 0:
            while len(self.hunters) < self.workersnum and self.check('occupation','General Worker') == True:
                order = [1,2,3,4]
                random.shuffle(order)
                #print(order)
                for i in range(4):
                    #print(i)
                    if order[i] == 1:
                        topWorker(self.hunters, "Hunter", "passionHunting")
                    elif order[i] == 2:
                        topWorker(self.gatherers, "Gatherer", "passionGathering")
                    elif order[i] == 3:
                        topWorker(self.fishermen, "Fisherman", "passionFishing")
                    else:
                        topWorker(self.foragers, "Forager", "passionForaging")
        for i in range(len(self.workers)):
            if self.workers[i].occupation == "General Worker":
                self.genworkers.append(self.workers[i])

    def check(self,att,value):
        for i in range(len(self.workers)):
            if self.workers[i].__dict__[att] == (value):
                return True
        else:
            return False

    def newWorkers(self):
        for i in range(len(self.workers)):
            if self.workers[i].status != 'Alive and Well':
                self.workers[i].occupation = 'Invalid'
            else:
                self.workers[i].occupation = "General Worker"
        self.initialiseWorkers()







    def foodstuffs(self):
        foodstuff = self.cereals+self.fish+self.meats+self.veg
        return foodstuff

    def playerfoodstuffs(self):
        foodstuff = self.playerVeg+self.playerMeats+self.playerFish
        return foodstuff

    def foragedfoodstuffs(self):
        foodstuff = self.foragedVeg+self.huntedMeats+self.fishedFish
        return foodstuff

    def reschange(self,res,change):
        self.__dict__[res] += change
    
    def initrels(self,characters):
        for i in range(len(characters)):
                characters[i].establishrels(characters)

    
    def advanceDay(self):
        self.endDayMessage()
        self.genworkerRandomChange()
        self.genworkersMiniEvent()
        self.gatheredFuel, self.foragedHerb, self.foragedVeg, self.huntedMeats, self.huntedPelts, self.fishedFish = self.workersBack()
        print("gathered " + str(self.gatheredFuel) + " Fuel.")
        print("foraged " + str(self.foragedHerb)+ " Herb and " + str(self.foragedVeg) + " Veg.")
        print("hunted " + str(self.huntedMeats)+ " Meat and " + str(self.huntedPelts) + " Pelts.")
        print("fished " + str(self.fishedFish) + " Fish.")
        self.updateRes(self.gatheredFuel, self.foragedHerb, self.foragedVeg, self.huntedMeats, self.huntedPelts, self.fishedFish)
        self.updateRes(self.playerFuel, self.playerHerb, self.playerVeg, self.playerMeats, self.playerPelts, self.playerFish)
        self.morale_yields_main()
        return


    def advanceNight(self):
        self.bigFeast()
        self.bigBurn()
        self.distributePelts()
        self.recovered()
        self.sickDie()
        self.newSick()
        self.morale_sick_dead()
        self.checkPop()
        self.day += 1
        self.startDayMessage()
        if self.day<30:
            self.playerFuel, self.playerHerb, self.playerVeg, self.playerMeats, self.playerPelts, self.playerFish = 0,0,0,0,0,0
            self.actions = 5
        self.rollevent = random.randint(1,4)
        self.weatherMake()
        self.newWorkers()
        return

    def startDayMessage(self):
        print("")
        print("Day " + str(self.day) + " has begun")

    def endDayMessage(self):
        print("")
        print("Day " + str(self.day) + " has ended")
        print("End of day report:")

    def addLim(self, a, b, limit):
        c = a+b
        if c>limit:
            return limit
        else:
            return c

    def subLim(self, a, b, limit):
        d = a-b
        if d<limit:
            return limit
        else:
            return d

    def addsubLim(self,a,b,uplim,downlim=0):
        if b>=0:
            return self.addLim(a,b,uplim)
        else:
            return self.subLim(a, (-b), downlim)

    def genworkersMiniEvent(self): # if too few townspeople for nonworkers and resource management, lose cohesion, morale or resources / else vice versa
        pass

    def morale_yields_main(self): # gain if good yields, loss if casualties
        pass

    def bigFeast(self):
        def eatFood(peasant):
            food = 0
            if self.veg > 0:
                self.veg-= 1
                food += 2

            if self.meats > 0:
                self.meats -= 1
                food += 3
            elif self.fish > 0:
                self.fish -= 1
                food += 3
            
            if self.cereals > 0:
                self.cereals -= 1
                food += 4

            if food == 0:
                food = -5
            
            
            peasant.currenthealth = self.addLim(peasant.currenthealth,food,peasant.maxhealth)
        for peasant in self.peasants:
            eatFood(peasant)
        

    def bigBurn(self):
        def burnLog(peasant):
            peasant.hasFire = 0
            if self.fuel > 0:
                self.fuel -= 1
                peasant.hasFire = 1

        for peasant in self.peasants:
            burnLog(peasant)

    def morale_sick_dead(self): 
        pass

    def distributePelts(self):
        used_pelts = 0
        def peltTime(peasant,used_pelts):
            peasant.hasPelt = 0
            if used_pelts < self.pelts:
                peasant.hasPelt = 1
                used_pelts += 1
        for peasant in self.peasants:
            peltTime(peasant,used_pelts)

    def checkPop(self):
        self.popIll = 0
        self.popHealthy = 0
        self.popDead = 0
        self.popRecovering = 0
        self.popBuried = 0
        for peasant in self.peasants:
            if peasant.status == "Alive and Well":
                self.popHealthy += 1
            elif peasant.status == "Sick":
                self.popIll += 1
            elif peasant.status == "Recovering from Sickness":
                self.popHealthy += 1
            elif peasant.status == "Dead":
                self.popDead += 1
            else:
                self.popBuried += 1

        
    def workersBack(self): # make more probabilistic and proportional to value of resources
        def skillRoll(worker,skill,m_yield):
            rnd = random.randint(1,10)
            if rnd < worker.__dict__[skill]:
                return m_yield
            else:
                worker.currenthealth = self.subLim(worker.currenthealth, rnd, 0)
                return m_yield/2

        def fromWorld(percentage,resource):
            takeaway = round((percentage/100.0)*self.__dict__['world'+str(resource)])
            self.__dict__['world'+str(resource)] = self.subLim(self.__dict__['world'+str(resource)],takeaway,0) 
            return takeaway

        gatheredsucc = 0
        gatheredFuel = 0
        foragedsucc = 0
        foragedHerb = 0
        foragedVeg = 0
        huntedsucc = 0
        huntedPelts = 0
        huntedMeats = 0
        fishedsucc = 0
        fishedFish = 0
        for i in range(len(self.gatherers)): # all workers roll for success, and can either fail or choose to half succeed with a consequence
            
            gatheredsucc += skillRoll(self.gatherers[i],'passionGathering',1)
            self.gatherers[i].currenthealth = self.subLim(self.gatherers[i].currenthealth,random.randint(1,5),0) 
        for i in range(len(self.foragers)):
            foragedsucc += skillRoll(self.foragers[i],'passionForaging',1)
            self.foragers[i].currenthealth = self.subLim(self.foragers[i].currenthealth, random.randint(1,5),0)
        for i in range(len(self.hunters)):
            huntedsucc += skillRoll(self.hunters[i],'passionHunting',1)
            self.hunters[i].currenthealth = self.subLim(self.hunters[i].currenthealth, random.randint(1,5),0)
        for i in range(len(self.fishermen)):
            fishedsucc += skillRoll(self.fishermen[i],'passionFishing',1)
            self.fishermen[i].currenthealth = self.subLim(self.fishermen[i].currenthealth, random.randint(1,5),0)

        gatheredFuel = fromWorld(gatheredsucc,'fuel')
        foragedHerb = fromWorld(foragedsucc,'herbs')
        foragedVeg = fromWorld(foragedsucc,'veg')
        huntedMeats = fromWorld(huntedsucc,'meats')
        huntedPelts = fromWorld(huntedsucc,'pelts')
        fishedFish = fromWorld(fishedsucc,'fish')
        return gatheredFuel, foragedHerb, foragedVeg, huntedMeats, huntedPelts, fishedFish

    def updateRes(self, gatheredFuel, foragedHerb, foragedVeg, huntedMeats, huntedPelts, fishedFish):
        self.fish += fishedFish
        self.fuel += gatheredFuel
        self.veg += foragedVeg
        self.herbs += foragedHerb
        self.meats += huntedMeats
        self.pelts += huntedPelts
        return


    def genworkerRandomChange(self):
        for i in range(len(self.genworkers)):
            self.genworkers[i].currenthealth = self.addsubLim(self.genworkers[i].currenthealth,random.randint(-5,5),self.genworkers[i].maxhealth)

    def recovered(self):
        for i in range(len(self.peasants)):
            if self.peasants[i].status == 'Recovering from Sickness':
                self.peasants[i].status = 'Alive and Well'
    
    def sickDie(self):
        self.newRecovered = 0
        self.newDead = 0
        def tryTakeMeds(sicko):
            if self.herbs > 0:
                self.herbs -= 1
                print(sicko.name + " is recovering from sickness after being treated")
                sicko.status = 'Recovering from Sickness'
                self.newRecovered += 1
            else:
                if random.randint(1,100) > sicko.currenthealth:
                    print(sicko.name + " has died.")
                    sicko.status = 'Dead'
                    self.newDead += 1
                else:
                    sicko.currenthealth = self.addLim(sicko.currenthealth, round(0.2*sicko.currenthealth),sicko.maxhealth)
                    print(sicko.name + " is recovering from sickness despite the lack of herbs")
                    sicko.status = 'Recovering from Sickness'
                    self.newRecovered += 1
                
        for i in range(len(self.peasants)):
            if self.peasants[i].currenthealth == 0:
                self.peasants[i].status = 'Dead'
                self.newDead += 1
            if self.peasants[i].status == 'Sick':
                tryTakeMeds(self.peasants[i])



    
    def newSick(self):
        self.newIll = 0
        for i in range(len(self.peasants)):
            if self.peasants[i].status == 'Alive and Well' and self.peasants[i].currenthealth < 50:
                if random.randint(1,100) > self.peasants[i].currenthealth:
                    print(self.peasants[i].name + " has taken ill")
                    self.peasants[i].status = 'Sick'
                    self.newIll += 1
                else:
                    self.peasants[i].currenthealth = self.addLim(self.peasants[i].currenthealth, round(0.1*self.peasants[i].currenthealth),self.peasants[i].maxhealth)
        



    
    """
    def communityChange(self):
        self.newill = self.newIll()
        self.newdead, self.newrecovered = self.newDead()
        self.pophealthy += self.newrecovered - self.newill
        self.popill += self.newill - self.newdead - self.newrecovered
        self.popdead += self.newdead

    def newIll(self):
        return self.weatherCold*3 # placeholder !!

    def newDead(self):
        dead = 0
        recover = 0
        for i in range(self.popill):
            if self.herbs > 0:
                self.herbs -= 1
                recover += 1
            else:
                dead += 1


        return dead, recover
    """
        

    def weatherMake(self):
        # weather / 
        yeet = random.randint(1,40)
        yote = random.randint(1,40)
        self.weatherPrecip=0 # dry
        self.weatherWind=0 # calm
        self.weatherCold=0 # mild
        precip = yeet+self.day # ranges from 0-70 day 0, to 30-100 day 30
        if precip > 60:
            self.weatherPrecip = 2 # snow
        elif precip > 30:
            self.weatherPrecip = 1 # rain
        
        wind = yote+self.day # ranges from 0-70 day 0, to 30-100 day 30
        if wind > 60:
            self.weatherWind = 2 # gale
        elif wind > 30:
            self.weatherWind = 1 # breezy

        cold = (precip + wind)*0.5 # ranges from 0-70 day 0, to 30-100 day 30
        if cold > 80:
            self.weatherCold = 4 # deathly
        elif cold > 60:
            self.weatherCold = 3 # freezing
        elif cold > 40:
            self.weatherCold = 2 # brisk
        elif cold > 20:
            self.weatherCold = 1 # chilly
        
        self.coldness = cold
        
        return
        


    
  
def main():

    game = Game()

    """
    print(game.crier.widow)
    print(game.crier.like)
    game.crier.statchange("like",1)
    print(game.crier.like)
    print(game.crier.widow)
    game.crier.relchange(game.widow,9)
    print(game.crier.widow)
    print(game.widow.crier)

    print(game.__dict__)
    print(game.foodstuffs())
    game.reschange("fish",-22)
    print(game.foodstuffs())

    print(game.crier.name)

    print(game.day)
    game.advanceDay(game)

    print(game.day)
    print(game.adjectiveWind[game.weatherWind])
    print(game.adjectivePrecip[game.weatherPrecip])
    print(game.adjectiveCold[game.weatherCold])


    print(game.characters)
    for i in range(len(game.peasants)):
        print(game.peasants[i].__dict__)

    print(len(game.workers))
    print(len(game.children))
    print(len(game.elders))

    """

    def display(x,occ=False):
        if occ == True:
            print(" __ __ __ " + str((x[0].occupation)) + " __ __ __")
        else:
            print(" __ __ __ Workers __ __ __")
        for i in range(len(x)):
            print(x[i].__dict__)

    display(game.hunters,True)
    display(game.foragers,True)
    display(game.gatherers,True)
    display(game.fishermen,True)
    display(game.genworkers,True)

    display(sorted(game.workers, key=lambda x: x.occupation, reverse=True))

    game.advanceDay()
    
    game.advanceDay()
    game.advanceDay()
    game.advanceDay()
    game.advanceDay()
    game.advanceDay()
    game.advanceDay()
    game.advanceDay()
    

    display(sorted(game.peasants, key=lambda x: x.occupation, reverse=True))
        
main()