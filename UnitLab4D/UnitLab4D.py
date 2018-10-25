def main():
    shoppingCart = [['tooth paste', 'q-tips', 'milk'], ['milk', 'candy', 'apples'], ['paper', 'pencils', 'q-tips']]
    allItems = allInOne(shoppingCart)
    print(allItems)
    numTips = countQTips(shoppingCart)
    print('There are ' + str(numTips))


def allInOne(myShoppingCart):
    print('allInOne')
    allItems = []
    list = []
    for item in myShoppingCart:
        for i in item:
            allItems.append(i)
    print(allItems)
    input('pause')
    for i in allItems:
        if i not in list:
            list.append(i)

    return list


def countQTips(myCart):
    numTips = int(0)
    for group in myCart:
        print(group)
        for x in group:
            print(x)
            if x == ('q-tips'):
                numTips += 1
    print(numTips)
    return(numTips)








main()
