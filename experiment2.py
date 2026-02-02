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


# 5.Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
import math
a,b,c = map(int, input("enter value of coefficients of quadratic equation\n").split())
d=b**2-4*a*c
r1=(-b + math.sqrt(d))/2*a
r2=(-b - math.sqrt(d))/2*a
if d >=0 :
    print(f"root are real\nroots of given quadratic equation are {r1,r2}")

else:
    print(f"roots are imaginary\nroots of given quadratic equation are {r1,r2}")



#6.Find whether a given year is a leap year or not.
year = int(input("enter a year\n"))
if year%4==0 and (year%100!=0 or year%400==0) :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
