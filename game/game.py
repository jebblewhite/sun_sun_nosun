import random
import math

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
        self.warmth = 100
        self.maxwarmth = 100
        self.hunger = 100
        self.maxhunger = 100
        if self.age > 20:
            self.maxhealth = 120-self.age
        else:
            self.maxhealth = 100

        self.currenthealth = (3*self.maxhealth/4)

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
        self.playerFuel, self.playerHerb, self.playerhuntedFood, self.playerPelts, self.playerfishedFood = 0,0,0,0,0
        

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
        self.popCohesion = 30

        # starting values for resources
        self.worldherbs = 2000
        self.herbs = 0
        self.medicine = 0
        self.alcohol = 0
        self.worldfuel = 9000
        self.fuel = 350
        self.worldpelts = 180
        self.pelts = 0
        self.food = 250
        self.worldfood = 4000
       
        self.fueleffect = 20
        self.foodeffect = 20

        self.foodchoice = 2
        self.fuelchoice = 2
        self.herbchoice = 3
        self.peltchoice = 2

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

    def worldDecay(self):
        def fromWorld(percentage,resource):
            takeaway = round((percentage/1000.0)*self.__dict__['world'+str(resource)]*(2**(self.popMorale/50-1)))
            self.__dict__['world'+str(resource)] = self.subLim(self.__dict__['world'+str(resource)],takeaway,0) 
            return takeaway
        fromWorld(1.5,'fuel')
        fromWorld(1.5,'food')
        fromWorld(1.5,'pelts')
        fromWorld(1.5,'herbs')








    def reschange(self,res,change):
        self.__dict__[res] += change
    
    def initrels(self,characters):
        for i in range(len(characters)):
                characters[i].establishrels(characters)

    
    def advanceDay(self):
        self.endDayMessage()
        self.genworkerRandomChange()
        self.genworkersMiniEvent()
        self.gatheredFuel, self.foragedHerb, self.huntedFood, self.huntedPelts, self.fishedFood = self.workersBack()
        print("gathered " + str(self.gatheredFuel) + " Fuel.")
        print("foraged " + str(self.foragedHerb)+ " Herb.")
        print("hunted " + str(self.huntedFood)+ " Food and " + str(self.huntedPelts) + " Pelts.")
        print("fished " + str(self.fishedFood) + " Food.")
        self.updateRes(self.gatheredFuel, self.foragedHerb, self.huntedFood, self.huntedPelts, self.fishedFood)
        self.updateRes(self.playerFuel, self.playerHerb, self.playerhuntedFood, self.playerPelts, self.playerfishedFood)
        self.morale_yields_main()
        return

    def countAlive(self):
        return(len([peasant.status!= "Dead" for peasant in self.peasants]))

    def updateFood(self):
        self.foodpp = 2**(self.foodchoice-2)
        if self.countAlive()*self.foodpp <= self.food:
            self.distfood = (self.countAlive()*self.foodpp)
        else:
            self.distfood = (self.food)
        self.food -= self.distfood
        
    def updateFuel(self):
        self.fuelpp = 2**(self.fuelchoice-2)
        if self.countAlive()*self.fuelpp <= self.fuel:
            self.distfuel = (self.countAlive()*self.fuelpp)
        else:
            self.distfuel = (self.fuel)
        self.fuel -= self.distfuel
 

    def updateHerb(self):
        if self.herbchoice != 3:
            product = round(1.1*self.herbs)
            if self.herbchoice == 1:
                self.medicine += product
            else:
                self.alcohol += product
        else:
            product =  round(0.5*self.herbs)
            self.medicine += product
            self.alcohol += product
        self.herbs = 0

    def warmcheck(self):
        for peasant in self.peasants:
            heat = 0
            if peasant.hasFire > 0:
                heat = (math.log(peasant.hasFire,2)+2)*self.fueleffect
            print(heat)
            if peasant.hasPelt > 0:
                heat += (self.fueleffect)
            warmthchange = (heat-self.cold)
            print(heat)
            print(self.cold)
            print(warmthchange)
            peasant.warmth = self.addsubLim(peasant.warmth,warmthchange,peasant.maxwarmth) 

            
            a = self.subLim(peasant.currenthealth,(peasant.maxwarmth-peasant.warmth),0)
            peasant.currenthealth = a

    def hungercheck(self):
        for peasant in self.peasants:
            hunger = 0
            if peasant.hasFood > 0:
                hunger = (math.log(peasant.hasFood,2)+2)*self.foodeffect
            
            hungerchange = (hunger-self.cold)
            peasant.hunger = self.addsubLim(peasant.hunger,hungerchange,peasant.maxhunger)
            print(peasant.hunger)
            print(peasant.currenthealth)
            a = peasant.currenthealth = self.addsubLim(peasant.currenthealth,(peasant.hunger-50)/10,peasant.maxhealth)
            peasant.currenthealth = a
            print(peasant.currenthealth)
            print(" Name : {name} - Occupation : {occ} - Health : {health}/{maxhealth}".format(name=peasant.name,occ=peasant.occupation,health=peasant.currenthealth,maxhealth=peasant.maxhealth))
    

    def advanceNight(self):
        self.bigFeast()
        self.bigBurn()

        self.distributePelts()

        self.giveMedicine()

        self.recovered()
        self.sickDie()
        self.newSick()

        self.warmcheck()
        self.hungercheck()

        # morning here
        self.morale_sick_dead()
        self.checkPop()

        self.day += 1
        self.startDayMessage()
        if self.day<30:
            self.playerFuel, self.playerHerb, self.playerPelts, self.playerhuntedFood, self.playerfishedFood = 0,0,0,0,0
            self.actions = 5
        self.rollevent = random.randint(1,4)
        self.weatherMake()
        self.newWorkers()
        self.worldDecay()
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
        print(a)
        print(b)
        print(c)
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
            return self.subLim(a, b, downlim)

    def genworkersMiniEvent(self): # if too few townspeople for nonworkers and resource management, lose cohesion, morale or resources / else vice versa
        pass

    def morale_yields_main(self): # gain if good yields, loss if casualties
        pass

    def bigFeast(self):
        def eatFood(peasant):
            peasant.hasFood = 0
            if self.distfood > 0:
                self.distfood -= self.foodpp
                peasant.hasFood = (self.foodpp)

        random.shuffle(self.peasants)
        for peasant in self.peasants:
            eatFood(peasant)
        

    def bigBurn(self):
        def burnLog(peasant):
            peasant.hasFire = 0
            if self.distfuel > 0:
                self.distfuel -= self.fuelpp
                peasant.hasFire = (self.fuelpp)

        random.shuffle(self.peasants)
        for peasant in self.peasants:
            burnLog(peasant)

    def giveMedicine(self):
        def takeMeds(peasant):
            if self.medicine > 0:
                self.medicine -= 1
                peasant.hasMeds = 1

        random.shuffle(self.peasants)
        for peasant in self.peasants:
            peasant.hasMeds = 0
            if peasant.status == "Sick":
                takeMeds(peasant)

    def morale_sick_dead(self): 
        pass

    def distributePelts(self):
        self.used_pelts = 0
        def peltTime(peasant):
            peasant.hasPelt = 0
            if self.used_pelts < self.pelts:
                peasant.hasPelt = 1
                self.used_pelts += 1
        for peasant in self.peasants:
            peltTime(peasant)

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
            takeaway = round((percentage/1000.0)*self.__dict__['world'+str(resource)])
            self.__dict__['world'+str(resource)] = self.subLim(self.__dict__['world'+str(resource)],takeaway,0) 
            return takeaway

        def fromWorldAbs(absol,resource):
            takeaway = absol
            self.__dict__['world'+str(resource)] = self.subLim(self.__dict__['world'+str(resource)],takeaway,0) 
            return takeaway

        gatheredsucc = 0
        gatheredFuel = 0
        foragedsucc = 0
        foragedHerb = 0
        huntedsucc = 0
        huntedPelts = 0
        huntedFood = 0
        fishedsucc = 0
        fishedFood = 0
        for i in range(len(self.gatherers)): # all workers roll for success, and can either fail or choose to half succeed with a consequence
            
            gatheredsucc += skillRoll(self.gatherers[i],'passionGathering',1)
            self.gatherers[i].currenthealth = self.subLim(self.gatherers[i].currenthealth,2*random.randint(1,5),0) 
        for i in range(len(self.foragers)):
            foragedsucc += skillRoll(self.foragers[i],'passionForaging',1)
            self.foragers[i].currenthealth = self.subLim(self.foragers[i].currenthealth, 2*random.randint(1,5),0)
        for i in range(len(self.hunters)):
            huntedsucc += skillRoll(self.hunters[i],'passionHunting',1)
            self.hunters[i].currenthealth = self.subLim(self.hunters[i].currenthealth, 2*random.randint(1,5),0)
        for i in range(len(self.fishermen)):
            fishedsucc += skillRoll(self.fishermen[i],'passionFishing',1)
            self.fishermen[i].currenthealth = self.subLim(self.fishermen[i].currenthealth, 2*random.randint(1,5),0)

        gatheredFuel = fromWorld(gatheredsucc,'fuel')
        foragedHerb = fromWorld(foragedsucc,'herbs')
        huntedFood = fromWorld(huntedsucc,'food')
        ## change this VV
        huntedpeltssucc = 0
        for i in range(int(huntedFood)):
            if random.randint(1,100) >= 99:
                huntedpeltssucc+=1
        huntedPelts = fromWorldAbs(huntedpeltssucc,'pelts')
        fishedFood = fromWorld(fishedsucc,'food')
        return gatheredFuel, foragedHerb, huntedFood, huntedPelts, fishedFood

    def updateRes(self, gatheredFuel, foragedHerb, huntedFood, huntedPelts, fishedFood):
        self.food += fishedFood
        self.fuel += gatheredFuel
        self.herbs += foragedHerb
        self.food += huntedFood
        self.pelts += huntedPelts
        return


    def genworkerRandomChange(self):
        for i in range(len(self.genworkers)):
            self.genworkers[i].currenthealth = self.addsubLim(self.genworkers[i].currenthealth,random.randint(-10,10),self.genworkers[i].maxhealth)
            

    def recovered(self):
        for i in range(len(self.peasants)):
            if self.peasants[i].status == 'Recovering from Sickness':
                self.peasants[i].status = 'Alive and Well'
    
    def sickDie(self):
        
        self.newRecovered = 0
        self.newDead = 0
        def tryTakeMeds(sicko):
            if sicko.hasMeds > 0:
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
                    print(sicko.name + " is recovering from sickness despite the lack of medicine")
                    sicko.status = 'Recovering from Sickness'
                    self.newRecovered += 1

        for i in range(len(self.peasants)):
            if self.peasants[i].currenthealth == 0:
                self.peasants[i].status = 'Dead'
                self.newDead += 1
            if self.peasants[i].status == 'Dead':
                self.peasants[i].currenthealth = 0
            if self.peasants[i].status == 'Sick':
                tryTakeMeds(self.peasants[i])



    
    def newSick(self):
        self.newIll = 0
        for i in range(len(self.peasants)):
            if self.peasants[i].status == 'Alive and Well' and self.peasants[i].currenthealth < 40:
                if random.randint(1,100) > self.peasants[i].currenthealth:
                    print(self.peasants[i].name + " (" + self.peasants[i].occupation + ") has taken ill")
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
        """
        self.weatherPrecip=0 # dry
        self.weatherWind=0 # calm
        self.weatherCold=0 # mild
        """

        self.precip = yeet+self.day # ranges from 0-70 day 0, to 30-100 day 30
        """
        if precip > 60:
            self.weatherPrecip = 2 # snow
        elif precip > 30:
            self.weatherPrecip = 1 # rain
        """
        self.wind = yote+self.day # ranges from 0-70 day 0, to 30-100 day 30

        """
        if wind > 60:
            self.weatherWind = 2 # gale
        elif wind > 30:
            self.weatherWind = 1 # breezy
        """

        self.cold = (self.precip + self.wind)*0.75# ranges from 0-70 day 0, to 30-100 day 30 // now 0-105 tending to 52

        """
        if cold > 80:
            self.weatherCold = 4 # deathly
        elif cold > 60:
            self.weatherCold = 3 # freezing
        elif cold > 40:
            self.weatherCold = 2 # brisk
        elif cold > 20:
            self.weatherCold = 1 # chilly
        """
        
        
        
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
    print(game.countAlive)
        
main()