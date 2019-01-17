def main():
    list1 = input('give me words')
    print(list1)
    newList = deVowel(list1)
    print(newList)
    list2 = (4, 6, 2, 8)
    math = mathStuff(list2,2)



def deVowel(myList):
    print('DeVowel')
    resultList = ""
    for i in myList:
        if(i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u'):
            resultList = resultList + i
            print(resultList)
    return resultList



def mathStuff(numbers,num):
    print('mathStuff')
    resultList2 = []
    for i in numbers:
        resultList2.append(i * num)
    print(resultList2)



main()
