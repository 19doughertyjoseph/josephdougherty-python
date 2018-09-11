numGrade = int(input("enter a number"))

if numGrade >= 90:
    print('Yahoo you got an A!')

elif numGrade >= 80:
    print('Good you got a B!')

elif numGrade >= 70:
    print('Okay you got a C!')

else:
    print('You better study harder')


userinput = str(input('type favorite color'))
print(userinput)
if userinput == 'blue':
    print('The sky is blue')

elif userinput == 'green':
    print('The forest is green')

elif userinput == 'red':
    print('I love red')

elif userinput == 'yellow':
    print('Yuck yellow')

else:
    print('I am a dumb computer - I only know 4 colors')
