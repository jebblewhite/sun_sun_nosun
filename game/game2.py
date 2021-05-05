import random
import math

"""
Character class, for each named 'romanceable' character
Mostly perfect for what is required

"""
class Charac(object):
    def __init__(self,like,respect,attract,name,img,ide,characters):
        self.like = like
        self.resp = respect
        self.att = attract
        self.name = name
        self.ide = ide
        self.scene = 1
        characters.append(self)
        """
        for character in characters:
            print(character.ide)
        """

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


"""
Peasant, or, Tudor class, for 'expendable' pops
"""
class Peasant(object):
    def __init__(self, name,peasants,children,elders,workers):
        def getRandomAge():
            age = -1
            mu = 40
            sigma = 35
            while age < 1 or age > 80:
                age = int(round(random.gauss(mu, sigma)))
            return age

        """
        DEFINE STATS
        """    
        self.name = name
        self.age = getRandomAge()

        self.energy = 50
        self.maxenergy = 100

        self.warmth = 100
        self.maxwarmth = 100

        self.fedness = 100
        self.maxfedness = 100

        self.wetness = 0
        self.maxwetness = 100

        self.sickness = 0
        self.injury = 0

        if self.age > 20:
            self.maxhealth = 120-self.age
        else:
            self.maxhealth = 100

        self.currenthealth = (3*self.maxhealth/4)
        """
        Vocational Stats
        """
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

        """
        Age Group assignment
        """
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
        """
        Initialise potential events as viable based on environments
        """
        self.forestevents = {"thestag":True, "theghouls":True, "thelovers":True, "themachineman":True, "themusic":True}
        self.riverevents = {"ontheotherbank":True, "thehutbytheriver":True, "theleviathan":True, "thestatues":True, "thethreesome":True}
        self.townevents = {"thestagnight":False}
    

        for i in range(100):
            Peasant('Tudor ' + str(i),self.peasants,self.children,self.elders,self.workers)

        
        self.workersnum = 5
        self.workersorder = 0

        self.popMorale = 50
        self.popCohesion = 30

        # starting values for resources
        self.herbs = 0
        self.medicine = 0
        self.alcohol = 0
        self.fuel = 200
        self.pelts = 0
        self.food = 250
       
        self.fueleffect = 20
        self.foodeffect = 20

        self.foodchoice = 2
        self.fuelchoice = 2
        self.herbchoice = 3
        self.peltchoice = 2

        self.day = 0
        self.initeventchance = 0.05
        self.temp = None

        self.checkPopStatus()
        self.resetvars()

    def initrels(self,characters):
        for i in range(len(characters)):
                characters[i].establishrels(characters)

    def checkPopStatus(self):
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
        self.popAlive = self.popHealthy+self.popIll+self.popRecovering

    def resetvars(self):
        self.new_ill = 0
        self.new_dead = 0
        self.new_buried = 0
        self.new_recovering = 0

        self.moralechange = 0
        self.cohesionchange = 0

    def initday(self):
        day = self.day
        temp = self.temp
        self.community_change("day")
        self.weather_make(day,temp)
        self.assign_workers()
        self.eventchance = (self.initeventchance)

    def endofday(self):
        self.workers_harvest()
        self.workers_project()
        self.elders_inspire()
        self.children_play()
        self.tudortakedamage()
        self.internalsystemsbalance()
        self.community_change("night")

    def initnight(self):
        day = self.day
        temp = self.temp
        self.weather_make(day,temp)

    def weather_make(self, day, temp, time='day'):
        # weather /
        cold_upper_lim = 10-math.floor(day/6)
        cold_lower_lim = 0-math.floor(day/2)
        cold_range = cold_upper_lim-cold_lower_lim
        maxchange = round(cold_range)
        minchange = round(cold_range/2)
        if temp != None:
            change = random.randint(minchange,maxchange)
            if time == 'day':
                temp = self.addLim(temp,change,cold_upper_lim)
            else:
                temp = self.subLim(temp,change,cold_lower_lim)
        else:
            temp = random.randint(cold_lower_lim,cold_upper_lim)
    
        windarray = [0,0,0,0,0.3,0.3,0.6,0.6,1,1]
        preciparray = [0,0,0,0,0.3,0.3,0.6,0.6,1,1]
        windno = random.randint(0,9)
        precipno = random.randint(0,9)
        
        if windno > 7:
            windadj = "heavy wind"
        elif windno > 5:
            windadj = "moderate wind"
        elif windno > 3:
            windadj = "light wind"
        else:
            windadj = "no wind"
    
        if precipno > 7:
            precipadj = "heavy precipitation"
        elif precipno > 5:
            precipadj = "moderate precipitation"
        elif precipno > 3:
            precipadj = "light precipitation"
        else:
            precipadj = "no precipitation"
    
        windmulti = windarray[windno]
        precipmulti = preciparray[precipno]
    
        coldness = 2*(20-temp)
        coldness += coldness*windmulti
        wetness = precipmulti*coldness
        
        self.coldness = coldness
        self.wetness = wetness
        self.temp = temp
        self.windadj = windadj
        self.precipadj = precipadj
 
        return coldness, wetness, temp, windadj, precipadj

    def community_change(self,dayornight):
        # check if fuel and food provisions are enough for everyone at current, else subtract morale or cohesion
        if dayornight == 'day':
            self.moralechange += self.new_buried - 2*self.new_dead
            self.cohesionchange += self.new_recovering - self.new_ill
            if self.fuel < self.popAlive:
                self.moralechange -= 5
            if self.food < self.popAlive:
                self.cohesionchange -= 5
        self.popMorale = self.addsubLim(self.popMorale, self.moralechange)
        self.popCohesion = self.addsubLim(self.popCohesion, self.cohesionchange)

    def assign_workers(self):
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
            while len(self.hunters) < self.workersnum and self.checkforatt('occupation','General Worker') == True:
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
    
    def checkforatt(self,att,value):
        for i in range(len(self.workers)):
            if self.workers[i].__dict__[att] == (value):
                return True
        else:
            return False
    
    def viable_events(self):
        pass

    def check_for_event(self):
        pass

    def harvest_action(self):
        pass
    
    def workers_harvest(self):
        def getYields(peasant,passion):
            if random.randint(1,10) < peasant.__dict__[passion]:
                return 1
            elif random.randint(1,10) < peasant.__dict__[passion]:
                return 0.5
            elif random.randint(1,10) < peasant.__dict__[passion]:
                return 0.25
            else:
                return 0

        def getInjuries(peasant,passion):
            if random.randint(1,10) < peasant.__dict__[passion]:
                peasant.injury += 0
            elif random.randint(1,10) < peasant.__dict__[passion]:
                peasant.injury += 1
            elif random.randint(1,10) < peasant.__dict__[passion]:
                peasant.injury += 2
            else:
                peasant.injury += 3
            return

        gatheredsucc = 0
        gatheredFuel = 0

        foragedsucc = 0
        foragedHerb = 0

        huntedsucc = 0
        huntedPelts = 0
        huntedFood = 0

        fishedsucc = 0
        fishedFood = 0

        for gatherer in self.gatherers:
            gatheredsucc += getYields(gatherer, 'passionGathering')
            getInjuries(gatherer, 'passionGathering')
        for forager in self.foragers:
            foragedsucc += getYields(forager, 'passionForaging')
            getInjuries(forager, 'passionForaging')
        for hunter in self.hunters:
            huntedsucc += getYields(hunter, 'passionHunting')
            getInjuries(hunter, 'passionHunting')
        for fisher in self.fishermen:
            fishedsucc += getYields(fisher, 'passionFishing')
            getInjuries(fisher, 'passionFishing')

    def workers_project(self):
        pass

    def elders_inspire(self):
        for elder in self.elders:
            self.cohesionchange += 1

    def children_play(self):
        for child in self.children:
            self.moralechange += 1

    def tudortakedamage(self):
        pass

    def internalsystemsbalance(self):
        pass

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

    def addsubLim(self,a,b,uplim=100,downlim=0):
        if b>=0:
            return self.addLim(a,b,uplim)
        else:
            return self.subLim(a, -b, downlim)

"""
--------------------------- END OF CLASS -   - -- -  -- - -
"""

def display(x,occ=False):
        if occ == True:
            print(" __ __ __ " + str((x[0].occupation)) + " __ __ __")
        else:
            print(" __ __ __ Workers __ __ __")
        for i in range(len(x)):
            print(x[i].__dict__)

def main():
    game = Game()
    display(game.peasants)


main()