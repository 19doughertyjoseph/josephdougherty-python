numList1=[2,4,6,8,10,12,14,16,18,20]
print(numList1)

print(len(numList1))

subList=numList1[0:5]
print(subList)

subList.append(12)
print(subList)

subList1=numList1
print(subList1)

subList1.append(22)
print(subList1)

myClasses=['spanish','economics','forensics','calculus','python','comp','gothic']
print(myClasses)

myClasses.remove('comp')
print(myClasses)

favClass=myClasses.pop(4)
print(favClass)

print('My favorite class is ' + favClass)
