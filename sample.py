print("Hi! I sell different varieties of beads. Do you want to buy one?")
print("(1)Yes (2)No")
bead=input('Enter your choice: ')
if bead=='1':
    print('OK! Which one do you want?')
    print('(1)Ruby (2)Sapphire (3)Emerald (4)Pearl (5)None')
    choice1=input('Enter your choice: ')
    if choice1=='1':
        print('Take your rubies. No need to pay and Bye!')
    elif choice1=='2':
        print('Take your sapphires. No need to pay and Bye!')
    elif choice1=='3':
        print('Take your emeralds. No need to pay and Bye!')
    elif choice1=='4':
        print('Take your pearls. No need to pay and Bye!')
    else:
        print('Do you want to see more collections?')
        print('(1)Yes (2)No')
        choice2=input('Enter your choice')
        if choice2=='2':
            print('OK.. Goodbye and have a nice day!')
        else:
            print('OK')
            print('(1)Amethyst (2)Beryl (3)Coral (4)Diamond (5)None')
            choice3=input('Enter your choice: ')
            if choice3=='1' :
                print('Here take your amethysts. No need to pay and Bye!')
            elif choice3=='2' :
                print('Here take your beryls. No need to pay and Bye!')
            elif choice3=='3' :
                print('Here take your corals. No need to pay and Bye!')
            elif choice3=='4' :
                print('Here take your diamonds. No need to pay and Bye!')
            else:
                print('Go to jaipur.')
else:
    print('OK.. Goodbye and have a nice day!')
    