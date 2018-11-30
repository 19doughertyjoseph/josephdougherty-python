def main () :
    dict = {'omw':'on my way','gg':'good game','tbh':'to be honest'}
    d = 'y'
    while d=='y':
        i = input("Would you like to use, modify, or view the dictionary? (use/modify/view) - ")
        if i=='use':
            dict = normal(dict)
        elif i=='modify':
            dict = modify(dict)
        else:
            dict = view(dict)


def normal(dict) :
    x='y'
    while x=='y' :
        c = input('Put in code - ')
        if c in dict :
            print(dict[c])
        else :
            print("This isnt in the dictionary")
            a = input("Add it to the dictionary? (yes/no) - ")
            if a=='yes' :
                s = input("What is the value - ")
                dict[c] = s
        x = input('Define another? (yes/no) - ')
        print()
    return(dict)

def modify (dict) :
    x = 'y'
    while x=='y' :
        f = input("Would you like to remove or edit a text code (remove/edit) - ")
        if f=='remove' :
            l = input("What abreviation would you like to remove? - ")
            del dict[l]
        elif f=='edit' :
            e = input("What abreviation would you like to edit? - ")
            s = input("What does that abreviation actually stand for? - ")
            del dict[e]
            dict[e] = s
        else :
            print('Please enter either remove or enter')
        x = input("Would you like to remove another item(y/n) - ")
        print()
    return(dict)

def view(dict) :
    for x in dict :
        print(x + ' : ' + dict[x] + '      ', end='')
    print()
    print()
    return (dict)


main ()
