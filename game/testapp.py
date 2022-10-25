import random
from game2 import Game


def foodgathered(foodinworld):
    harvested = 0.01*foodinworld
    harvested += playerfood(foodinworld)
    return harvested

def playerfood(foodinworld):
    if random.randint(1,4) == 1:
        return (0.01*foodinworld)
    else:
        return (0)


def decaytime(foodinworld):
    decay = 0.015*foodinworld
    return decay

def choose_random_peasant():
    bigollist = [1,2,3,4,5,6,7]
    print(random.shuffle(bigollist))
    



def main():
    #thistext = "braces"
    #print(f"{{{{{{{{thistext}}}}}}}}")
    """
    foodinworld = 10000
    foodstocks = 100
    people = 100
    for day in range(30):
        print('day ' + str(day))
        harvested = foodgathered(foodinworld)
        print('harvested ' + str(harvested))
        foodinworld -= harvested
        foodstocks += harvested
        print('stocks ' + str(foodstocks))
        foodinworld -= decaytime(foodinworld)
        foodstocks -= people
        print('new foodinworld ' + str(foodinworld))
        print('new foodstocks ' + str(foodstocks))
        print('')

    """
    """
    choose_random_peasant()
    """
    game = Game()
    print(game.food)
    
    print([peasant.status!="Dead" for peasant in game.peasants].count(True))
    print([2**i for i in range(4)])


main()