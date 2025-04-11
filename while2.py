while True:
    someInput = input("please input a number")
    if someInput == '3':
        print ("Thank you for the 3. Very kind of you.")
        print ("Type 3 to continue, anything else to quit.")
        continue
    else:
        print ("That's not 3, so I'm quitting now.")
        print("bye")
        break
print("this is end")