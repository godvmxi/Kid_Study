print ("Which multiplication table would you like?")
number = int (input())
print ("here's your table")
for looper in range (1,11):
    result = looper * number
    print (str (number) + " x " + str (looper) + " = " + str (result) )