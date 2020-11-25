import random



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



def main():
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

main()