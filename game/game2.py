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
        self.romance = False
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

    def attraction_matrix(self):
        return (self.resp+self.like*2+self.att*4)/7

    def relationship_matrix(self):
        return (self.resp+self.like+self.att)/3


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
        Age Group assignment and conditions
        """
        self.occupation = "General Worker"
        self.location = "inside"
        self.status = "Alive and Well"

        self.sickness = 0
        self.injury = 0
        self.hasPelt = 0
        self.hasFire = 0
        self.hasFood = 0
        self.hasMeds = 0
        self.hasBeer = 0

        self.staging_flag = "initialisation"

        if self.age > 60:
            self.occupation = "Elder"
            elders.append(self)
        elif self.age < 20:
            self.occupation = "Child"
            children.append(self)
        else:
            workers.append(self)
        peasants.append(self)

    def display(self):
        display_string_header = "Name : {} | Age : {} | Status : {} | Occupation : {} | Location : {}\n -- ".format(self.name, self.age, self.status, self.occupation, self.location)
        display_string_passion = "Passions // {} Hunting | {} Fishing | {} Foraging | {} Gathering \n -- ".format(self.passionHunting, self.passionFishing, self.passionForaging, self.passionGathering)
        display_string_stats = "Stats // Health : {}/{} | Energy : {}/{} | Warmth : {}/{} | Fedness : {}/{} | Wetness {}/{}  \n -- ".format(self.currenthealth, self.maxhealth, self.energy, self.maxenergy, self.warmth, self.maxwarmth, self.fedness, self.maxfedness, self.wetness, self.maxwetness)
        display_string_conds = "Conditions // Injury : {} | Sickness : {} | Food : {} | Fire : {} | Pelt : {} | Meds : {} | Beer : {}\n - ".format(self.injury, self.sickness, self.hasFood, self.hasFire, self.hasPelt, self.hasMeds, self.hasBeer)
        display_string_flag = "Staging flag : {} \n ".format(self.staging_flag)
        display_string_final = display_string_header + display_string_passion + display_string_stats + display_string_conds + display_string_flag
        
        return display_string_final

class Game(object):
    def __init__(self):
        self.characters = []
        self.crier = Charac(0,0,0,'Nat',"image!!!","crier",self.characters)
        self.butcher = Charac(0,0,0,'Mik',"image!!!","butcher",self.characters)
        self.herbalist = Charac(0,0,0,'Joan',"image!!!","herbalist",self.characters)
        self.widow = Charac(0,0,0,'Elena',"image!!!","widow",self.characters)
        self.landowner = Charac(0,0,0,'Elisabetta',"image!!!","landowner",self.characters)
        self.innkeeper = Charac(0,0,0,'Henryk',"image!!!","innkeeper",self.characters)
        self.doctor = Charac(0,0,0,'Fyodora',"image!!!","doctor",self.characters)
        self.alderman = Charac(0,0,0,'Alexi',"image!!!","alderman",self.characters)
        self.nazi = Charac(0,0,0,'Alina',"image!!!","alina",self.characters)
        self.noah = Charac(0,0,0,'Noah',"image!!!","noah",self.characters)
        self.mila = Charac(0,0,0,'Mila',"image!!!","mila",self.characters)
        self.initrels(self.characters)

        self.peasants = []
        self.workers = []
        self.elders = []
        self.children = []

        self.player_name = "Jim"
        self.actions = 5
        self.playerFuel, self.playerHerb, self.playerhuntedFood, self.playerPelts, self.playerfishedFood = 0,0,0,0,0
        """
        Initialise potential events as viable based on environments
        """
        self.forestevents = {"thestag":True, "theghouls":True, "thelovers":True, "themachineman":True, "themusic":True}
        self.riverevents = {"ontheotherbank":True, "thehutbytheriver":True, "theleviathan":True, "thestatues":True, "thethreesome":True}
        self.townevents = {"thestagnight":False}
        self.vocationexertion = {"General Worker":30, "Child":20, "Elder":20, "Hunter":40, "Fisherman":40, "Forager":40, "Gatherer":40}
        self.progress = 0
    

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
       
        self.fueleffect = 40
        self.foodeffect = 40

        self.foodchoice = 2
        self.foodpp = 1
        self.fuelchoice = 2
        self.fuelpp = 1
        self.herbchoice = 3
        self.peltchoice = 2

        self.day = 0
        self.initeventchance = 0.05
        self.temp = None
        self.coldness = 0
        self.wetness = 0

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
        self.popInjured = 0
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
            if peasant.injury > 0:
                self.popInjured += 1
        self.popAlive = self.popHealthy+self.popIll+self.popRecovering

    def resetvars(self):
        self.new_ill = 0
        self.new_dead = 0
        self.new_buried = 0
        self.new_recovering = 0
        self.new_injured = 0

        self.moralechange = 0
        self.cohesionchange = 0

        self.newherbs = 0
        self.newfuel = 0
        self.newfish = 0
        self.newfood = 0
        self.newpelts = 0

    def display_new(self):
        self.checkPopStatus()
        display_stuff = " --DAY{}|| herb/meds/alc: {}/{}/{}, fuel: {}, food: {}, pelts: {}   /// alive: {}, dead: {}, sick: {}, injured: {}, morale: {}, cohesion: {} \n -- ".format(self.day,self.herbs,self.medicine,self.alcohol,self.fuel,self.food,self.pelts,self.popAlive,self.popDead,self.popIll,self.popInjured,self.popMorale,self.popCohesion)
        display_new_pops = "new_ill: {}, new_dead: {}, new_buried: {}, new_recovering: {}, new_injured {}\n -- ".format(self.new_ill,self.new_dead,self.new_buried,self.new_recovering,self.new_injured)
        display_new_stuff = "newherb: {}, newfuel: {}, newfish: {}, newfood: {}, newpelts: {}, foodpp: {}, fuelpp: {}\n -- ".format(self.newherbs,self.newfuel,self.newfish,self.newfood,self.newpelts,self.foodpp,self.fuelpp)
        display_new_change = "moralechange: {}, cohesionchange: {}, coldness: {}, wetness: {}\n   ".format(self.moralechange,self.cohesionchange,self.coldness,self.wetness)
        display_new = display_stuff+display_new_pops+display_new_stuff+display_new_change
        return display_new

    def initday(self):
        day = self.day
        temp = self.temp
        self.community_change("day")
        self.weather_make(day,temp)
        self.assign_workers()
        self.eventchance = (self.initeventchance)

    def endofday(self):
        self.vocations()
        self.tudortakedamage()
        self.internalsystemsbalance()
        self.community_change("night")

    def initnight(self, sim=0):
        day = self.day
        temp = self.temp
        self.weather_make(day,temp)
        if sim==1:
            self.updateFood()
            self.updateFuel()
            self.updateHerb()

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
            if self.fuel < self.countAlive():
                self.moralechange -= 5
            if self.food < self.countAlive():
                self.cohesionchange -= 5
        if dayornight == 'night':
            self.moralechange += self.new_buried - 2*self.new_dead - self.new_injured
            self.cohesionchange += self.new_recovering - self.new_ill - self.new_injured
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
                if high[count].occupation == 'General Worker' and high[count].status != "Dead" and high[count].status != "Sick" and high[count].injury == 0:
                    high[count].occupation = occTag
                    high[count].location = "woods"
                    professionlist.append(high[count])
                    tagged = 1
                else:
                    if count<len(high)-1:
                        count += 1
                    else:
                        tagged = 1
                        self.nonviable = 1
        self.genworkers = []
        self.sickppl = []
        self.hunters = []
        self.gatherers = []
        self.fishermen = []
        self.foragers = []
        self.nonviable = 0
        if self.workersorder == 0:
            while len(self.hunters) < self.workersnum and self.checkforatt('occupation','General Worker') == True and self.nonviable == 0:
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
                if self.workers[i].status == "Sick" or self.workers[i].status == "Recovering from Sickness":
                    self.sickppl.append(self.workers[i])
                    self.workers[i].location = "inside"
                else:
                    self.genworkers.append(self.workers[i])
                    self.workers[i].location = "outside"
        for peasant in self.peasants:
            peasant.staging_flag = "work_assignment"
    
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

    def playerHarvest(self,harvesttype,actioncost):
        
        gatheredsucc = 0

        foragedsucc = 0

        huntedsucc = 0

        fishedsucc = 0

        self.playersuccess = 4*actioncost
        if harvesttype == "hunt":
            huntedsucc = (self.playersuccess)
        elif harvesttype == "fish":
            fishedsucc = (self.playersuccess)
        elif harvesttype == "gather":
            gatheredsucc = (self.playersuccess)
        else:
            foragedsucc = (self.playersuccess)
            

        self.newherbs += 4*foragedsucc*0.5*random.randint(1,4)
        self.newfuel += 24*gatheredsucc*0.5*random.randint(1,4)
        self.newfish += 12*fishedsucc*0.5*random.randint(1,4)
        self.newfood += 8*huntedsucc*0.5*random.randint(1,4)
        self.newpelts += 4*huntedsucc*0.5*random.randint(1,4)

        self.herbs += self.newherbs
        self.fuel += self.newfuel
        self.food += self.newfish + self.newfood
        self.pelts += self.newpelts

        self.actions -= (actioncost)
    
    def vocations(self):
        self.workers_harvest()
        self.workers_project()
        self.elders_inspire()
        self.children_play()
        self.sick_rest()
        self.unassign_workers()

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
                peasant.currenthealth = self.subLim(peasant.currenthealth, 5, 0)
                self.new_injured += 1
            elif random.randint(1,10) < peasant.__dict__[passion]:
                peasant.injury += 2
                peasant.currenthealth = self.subLim(peasant.currenthealth, 10, 0)
                self.new_injured += 1
            else:
                peasant.injury += 3
                peasant.currenthealth = self.subLim(peasant.currenthealth, 20, 0)
                self.new_injured += 1
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
            gatherer.staging_flag = 'gathering'
        for forager in self.foragers:
            foragedsucc += getYields(forager, 'passionForaging')
            getInjuries(forager, 'passionForaging')
            forager.staging_flag = 'foraging'
        for hunter in self.hunters:
            huntedsucc += getYields(hunter, 'passionHunting')
            getInjuries(hunter, 'passionHunting')
            hunter.staging_flag = 'hunting'
        for fisher in self.fishermen:
            fishedsucc += getYields(fisher, 'passionFishing')
            getInjuries(fisher, 'passionFishing')
            fisher.staging_flag = 'fishing'
        print([peasant.passionForaging for peasant in self.foragers])
        print("{} / {} / {} / {}".format(foragedsucc,gatheredsucc,fishedsucc,huntedsucc))
        self.newherbs += 4*foragedsucc*0.5*random.randint(1,4)
        self.newfuel += 24*gatheredsucc*0.5*random.randint(1,4)
        self.newfish += 12*fishedsucc*0.5*random.randint(1,4)
        self.newfood += 8*huntedsucc*0.5*random.randint(1,4)
        self.newpelts += 4*huntedsucc*0.5*random.randint(1,4)

        self.herbs += self.newherbs
        self.fuel += self.newfuel
        self.food += self.newfish + self.newfood
        self.pelts += self.newpelts

    def workers_project(self):
        for worker in self.genworkers:
            self.progress += 1
            worker.staging_flag = 'project'

    def elders_inspire(self):
        for elder in self.elders:
            self.cohesionchange += 0.1*random.randint(-2,4)
            elder.staging_flag = 'inspire'

    def children_play(self):
        for child in self.children:
            self.moralechange += 0.1*random.randint(-2,4)
            child.staging_flag = 'play'

    def sick_rest(self):
        for sick in self.sickppl:
            sick.energy += 20

    def unassign_workers(self):
        for peasant in self.peasants:
            if peasant.occupation != "Child" and peasant.occupation != "Elder":
                peasant.occupation = "General Worker"

    def tudortakedamage(self):
        for tudor in self.peasants:
            if tudor.location == 'inside':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness*0.5)
            elif tudor.location == 'outside':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness)
                tudor.wetness = self.addLim(tudor.wetness,self.wetness*0.5)
            elif tudor.location == 'woods':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness*1.5)
                tudor.wetness = self.addLim(tudor.wetness,self.wetness)
            tudor.currenthealth = self.subLim(tudor.currenthealth,damage*0.5)
            tudor.energy, damage = self.subLimRem(tudor.energy,self.vocationexertion[tudor.occupation])
            tudor.fedness, damage = self.subLimRem(tudor.fedness,damage)
            tudor.currenthealth = self.subLim(tudor.currenthealth,damage*0.5)
            if tudor.currenthealth < 0.1 and tudor.status != "Dead":
                tudor.status = "Dead"
                self.new_dead += 1
            tudor.staging_flag = 'take_damage'

    def tudortakedamage2(self):
        for tudor in self.peasants:
            if tudor.location == 'inside':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness*0.5)
            elif tudor.location == 'outside':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness)
                tudor.wetness = self.addLim(tudor.wetness,self.wetness*0.5)
            elif tudor.location == 'woods':
                tudor.warmth, damage = self.subLimRem(tudor.warmth,self.coldness*1.5)
                tudor.wetness = self.addLim(tudor.wetness,self.wetness)
            tudor.currenthealth = self.subLim(tudor.currenthealth,damage*0.5)
            if tudor.currenthealth < 0.1 and tudor.status != "Dead":
                tudor.status = "Dead"
                self.new_dead += 1
            tudor.staging_flag = 'take_damage2'
        

    def internalsystemsbalance(self):
        for tudor in self.peasants:
            tudor.warmth = self.addLim(tudor.warmth,tudor.energy/2,tudor.maxenergy)
            tudor.energy = tudor.energy/2
            tudor.energy, leftover = self.addLimRem(tudor.energy,tudor.fedness,tudor.maxenergy)
            tudor.fedness = self.addLim(0,leftover,tudor.maxfedness)
            tudor.staging_flag = 'internal_balance'

    def internalsystemsbalance2(self):
        for tudor in self.peasants:
            tudor.warmth = self.addLim(tudor.warmth,tudor.energy/2,tudor.maxenergy)
            tudor.energy = tudor.energy/2
            tudor.energy, leftover = self.addLimRem(tudor.energy,tudor.fedness,tudor.maxenergy)
            tudor.fedness = self.addLim(0,leftover,tudor.maxfedness)
            if tudor.injury > 0:
                #make this work better
                tudor.injury = 0
            tudor.staging_flag = 'internal_balance2'

    def sickcheck(self):
        def tryTakeMeds(sicko):
            if sicko.hasMeds > 0:
                print(sicko.name + " is recovering from sickness after being treated")
                sicko.status = 'Recovering from Sickness'
                self.new_recovering += 1
            else:
                if random.randint(1,100) > (sicko.currenthealth+sicko.warmth)/2:
                    print(sicko.name + " has died.")
                    sicko.status = 'Dead'
                    self.new_dead += 1
                else:
                    sicko.currenthealth = self.addLim(sicko.currenthealth, round(0.1*sicko.currenthealth),sicko.maxhealth)
                    print(sicko.name + " is recovering from sickness despite the lack of medicine")
                    sicko.status = 'Recovering from Sickness'
                    self.new_recovering += 1

        for i in range(len(self.peasants)):
            if self.peasants[i].currenthealth <= 0 and self.peasants[i].status != 'Dead':
                self.peasants[i].status = 'Dead'
                self.new_dead += 1
            if self.peasants[i].status == 'Dead':
                self.peasants[i].currenthealth = 0
            if self.peasants[i].status == 'Sick':
                tryTakeMeds(self.peasants[i])

        for tudor in self.peasants:
            tudor.staging_flag = 'sickcheck'

    def newsick(self):
        for i in range(len(self.peasants)):
            if self.peasants[i].status == 'Alive and Well' and (self.peasants[i].currenthealth+self.peasants[i].warmth)/2 < 40:
                if random.randint(1,100) > self.peasants[i].currenthealth:
                    print(self.peasants[i].name + " (" + self.peasants[i].occupation + ") has taken ill")
                    self.peasants[i].status = 'Sick'
                    self.new_ill += 1
                else:
                    self.peasants[i].currenthealth = self.addLim(self.peasants[i].currenthealth, round(0.1*self.peasants[i].currenthealth),self.peasants[i].maxhealth)
        for tudor in self.peasants:
            tudor.staging_flag = 'newsick'

    def countAlive(self):
        return([peasant.status != "Dead" for peasant in self.peasants].count(True))

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

    def bigFeast(self):
        def eatFood(peasant):
            peasant.hasFood = 0
            if self.distfood > 0:
                self.distfood -= self.foodpp
                peasant.hasFood = (self.foodpp)
            if peasant.hasFood >= 2:
                self.cohesionchange += 1
            elif peasant.hasFood == 1:
                self.cohesionchange += 0.1
            elif peasant.hasFood < 1 and peasant.hasFood > 0:
                self.moralechange -= 0.1
            else:
                self.moralechange -= 1
                self.cohesionchange -= 1

        random.shuffle(self.peasants)
        for peasant in self.peasants:
            eatFood(peasant)
        

    def bigBurn(self):
        def burnLog(peasant):
            peasant.hasFire = 0
            if self.distfuel > 0:
                self.distfuel -= self.fuelpp
                peasant.hasFire = (self.fuelpp)
            if peasant.hasFire >= 2:
                self.moralechange += 1
            elif peasant.hasFire == 1:
                self.moralechange += 0.1
            elif peasant.hasFire < 1 and peasant.hasFire > 0:
                self.cohesionchange -= 0.1
            else:
                self.moralechange -= 1
                self.cohesionchange -= 1

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

    def consume(self):
        self.bigFeast()
        self.bigBurn()
        self.giveMedicine()

        for tudor in self.peasants:
            tudor.fedness += self.foodeffect*tudor.hasFood
            tudor.warmth += self.fueleffect*tudor.hasFire
            tudor.staging_flag = 'consume'

    def addLim(self, a, b, limit=100):
        c = a+b
        if c>limit:
            return limit
        else:
            return c

    def addLimRem(self, a, b, limit=100):
        c = a+b
        if c>limit:
            return limit, (c-limit)
        else:
            return c, 0

    def subLim(self, a, b, limit=0):
        d = a-b
        if d<limit:
            return limit
        else:
            return d

    def subLimRem(self, a, b, limit=0):
        d = a-b
        if d<limit:
            return limit, (-d)
        else:
            return d, 0

    def addsubLim(self,a,b,uplim=100,downlim=0):
        if b>=0:
            return self.addLim(a,b,uplim)
        else:
            return self.subLim(a, -b, downlim)

    def returnRandomDeadName(self):
        deadpeasants = [peasant for peasant in self.peasants if peasant.status == "Dead"]
        lengthdead = len(deadpeasants)
        randomdead = deadpeasants[random.randint(0,lengthdead-1)]
        return randomdead.name

"""
--------------------------- END OF CLASS -   - -- -  -- - -
"""

def display(x,occ=False):
        if occ == True:
            print(" __ __ __ " + str((x[0].occupation)) + " __ __ __")
        else:
            print(" __ __ __ Workers __ __ __")
        for i in range(len(x)):
            print(x[i].display())
"""
def main():
    import sys
    def entry_to_71():
        for peasant in game.peasants:
            if peasant.name == "Tudor 71":
                print(peasant.display(), file=f)
        print(game.display_new(), file=f)
    print('Tudor 71 report generating...')

    with open('tudor71report.txt', 'w') as f:
        print('Start of report', file=f)
        game = Game()
        
        #print(display(game.peasants), file=f)
        for i in range(30):
            entry_to_71()
            game.initday()
            entry_to_71()
            game.resetvars()
            game.vocations()
            entry_to_71()
            game.tudortakedamage()
            entry_to_71()
            game.internalsystemsbalance()
            entry_to_71()
            game.community_change("night")
            entry_to_71()
            game.initnight()

            # sim player choices
            entry_to_71()
            game.consume()
            entry_to_71()
            game.tudortakedamage2()
            entry_to_71()
            game.sickcheck()
            entry_to_71()
            game.internalsystemsbalance2()
            entry_to_71()
            game.newsick()
            entry_to_71()
            game.day += 1



main()
"""
