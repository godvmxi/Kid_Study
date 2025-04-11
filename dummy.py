import time
for i in range (1, 9):
    time.sleep (0.7)
    print ("i =  " +str(i), end="")
    print (" hallo ", end ="")
    if i == 3:
        #print("")
        continue
    print ("idoit")