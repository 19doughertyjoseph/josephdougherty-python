import random

DICENUM = 2

def main():
    count = 0
    play = input('Want to play a game? (y/n)- ')
    setOfDice = buildDice()

    while(play) == 'y':
        diceSet = [0] * DICENUM
        addSets = []

        for i in range(DICENUM):
            roll = randInt()
            addSets.append(roll + 1)
            diceSet[i] = setOfDice[roll]

        dicePrint(diceSet)
        print(addSets)
        count += 1
        play = input('Want to play a game?- ')

    print('you played ', count, 'times')


def buildDice():
    topBottom = ' ------- '
    leftOne =   '| *     |'
    middleOne = '|   *   |'
    rightOne =  '|     * |'
    middleTwo = '| *   * |'
    empty =     '|       |'

    one =   [topBottom, empty, middleOne, empty, topBottom ]
    two =   [topBottom, leftOne, empty, rightOne, topBottom]
    three = [topBottom, leftOne, middleOne, rightOne, topBottom]
    four =  [topBottom, middleTwo, empty, middleTwo, topBottom]
    five =  [topBottom, middleTwo, middleOne, middleTwo, topBottom]
    six =   [topBottom, middleTwo, middleTwo, middleTwo, topBottom]
    allDice = [one, two, three, four, five, six]
    return allDice


def playCount(countDice):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for i in range(len(countDice)):
        if countDice[i] == 1:
            count1 += 1
        if countDice[i] == 2:
            count2 += 1
        if countDice[i] == 3:
            count3 += 1
        if countDice[i] == 4:
            count4 += 1
        if countDice[i] == 4:
            count4 += 1
        if countDice[i] == 5:
           count5 += 1
        if countDice[i] == 6:
           count6 += 1

def dicePrint(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print(allDice[side][dice], end = '\t')
        print()


def randInt():
    return random.randint(0, 5)


main()
