numblocks = int (input("how many block of stars do you want"))
for block in range (1, numblocks + 1):
    print ("block = " + str (block))
    for line in range (1, block * 2):
        for star in range (1, (block + line) * 2):
            print("*", end="")
        print (" line = " + str (line) + "star = " + str (star))
    print("")
