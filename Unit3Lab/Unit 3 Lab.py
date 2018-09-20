from random import *

def myFunc():
    print('bellarminePrep')
    print('pythonProgramming')
myFunc()



def myGrade():
    x = input('What grade are you in - ?')
    y = int(x)-1
    y = print(str(y))
myGrade()



def myCity(city, age):
    print('my city is ' + city)
    print('my grade is ' + age)

x = input('What city are you from - ?')
y = input('What grade are you in')

myCity(x, y)



def twoNums():
    x = input(' What is my start value? - ')
    y = input(' What is my end value? - ')
    myNum = randint(int(x), int(y))
    print(myNum)

twoNums()


def boxArea(num1, num2):
     myArea = int(num1) * int(num2)
     return(myArea)

length = input('enter a number - ')
width = input('enter a second number')
myArea = boxArea(length, width)
print('The area is - ' + str(myArea))



def boxPer(num1, num2):
    myPer = int(num1) * 2 + int(num2) * 2
    return(myPer)

myPer = boxPer(length, width)
print('The perimeter is - ' + str(myPer))
