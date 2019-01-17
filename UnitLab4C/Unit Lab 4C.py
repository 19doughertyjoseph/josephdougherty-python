def draw7():
    input('Pause')
    for i in range(0, 7):
       starLoops()



def starLoops():
    for i in range(0 , 7):
        starString = ''
        for i in range(0, 7):
            starString = (starString + '*')
    print(starString)



draw7()



def starsAndStripes():
    input('Pause')
    for i in range(0, 3):
        string1 = ''
        string2 = ''
        for i in range (0, 7):
            string1 = (string1 + '*')
            string2 = (string2 + '-')
        print(string1)
        print(string2)

starsAndStripes()
