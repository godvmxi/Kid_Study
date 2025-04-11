number = input("please input a number ")
i  = 1
while i != 11:
    #print(i)
    result = i * int(number)
    
    print (number + " x " + str(i) + " = " + str(result))
    i = i + 1 
print("end")

i  = 1
while True:
    #print(i)
    result = i * int(number)    
    print (number + " x " + str(i) + " = " + str(result))
    i = i + 1 
    if i >= 11:
        break
print("end")