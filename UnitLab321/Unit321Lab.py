def main():
    numlist1 = (93.4, 92.5, 93.5, 85.6, 98.9)
    gradeIn = input('What grade are you in -?')
    grade1 = getYearInSchool(gradeIn)
    print('you are a ' + str(grade1))
    percent = calcAverageGrade(numlist1)
    print('your average grade is ' + str(percent))
    Grade = getLetterGrade(int(percent))
    print('Your letter grade is ' + str(Grade))
    if percent >= 65:
        print('Yay you are passing!')
    else:
        print('You failed. Study more')


def getYearInSchool(grade1):
    if grade1 == '9':
        return 'Freshman'
    elif grade1 == '10':
        return 'Sophomore'
    elif grade1 == '11':
        return 'Junior'
    elif grade1 == '12':
        return 'Senior'
    else:
        return 'not in highschool'



def calcAverageGrade(numbers):
    percent = sum(numbers)/float(len(numbers))
    return(percent)


def getLetterGrade(avgLetterGrade):
    if avgLetterGrade >= 90:
        return 'A'
    elif avgLetterGrade >= 80:
        return 'B'
    elif avgLetterGrade >= 70:
        return 'C'
    elif avgLetterGrade >= 65:
        return 'D'
    else:
        return 'F'


main()
