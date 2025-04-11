num1 = float(input("enter the first number") )

str_num2 = input("enter the second number")
num2 = float(str_num2)


if num1 < num2:
    print (str(num1) + " is less than " + str(num2))
if num1 > num2:
    print (str(num1) + " is larger than " + str(num2))
if num1 == num2:
    print (str(num1) + " is same as " + str(num2))

if num1 < num2:
    print (str(num1) + " # is less than " + str(num2))
elif num1 > num2:
    print (str(num1) + " # is larger than " + str(num2))
else:
    print (str(num1) + " # is same as " + str(num2))


if num1 != num2:
    print (str(num1) + " is also not same as " + str(num2))