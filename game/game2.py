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
        forestevents = {"thestag":True,}
        riverevents = {}
        townevents = {"thestagnight":False,}
    

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

        self.initday()

    def initday(self):
        self.weather_make()
        self.community_change()
        self.assign_workers()

    def weather_make(self):
        pass

    def community_change(self):
        pass

    def assign_workers(self):
        pass
    
    def viable_events(self):
        pass

    def check_for_event(self):
        pass