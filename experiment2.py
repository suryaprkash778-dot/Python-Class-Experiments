#1.	Check whether the given number is divisible by 3 and 5 both.
num = int(input("enter a number"))
if num % 3==0:
    if num % 5 ==0:
        print("num is divisible by 3 and 5 both")
    else:
        print(" num is divisible by 3 not 5")
else:
    print(" num is not divisible by either 3 or 5")


#2.Check whether a given number is multiple of five or not.
Num = int(input("enter a number"))
if Num % 5==0:
    print("num is multiple of 5")
else:
    print("num is not multiple of 5")


#3.	Find the greatest among the two numbers.
# If numbers are equal than print “numbers are equal”.
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if num1>num2:
    print("first number is greater")
elif num2>num1:
    print("second number is greater")
else:
    print("first and second numbers are same")

#4.Find the greatest among three numbers assuming no two values are same. 
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if num1>num2 and num1>num3:
    print("first number is greatest")
elif num2>num3 and num2>num1:
    print("second number is greatest")
else:
    print("third number is greatest")
