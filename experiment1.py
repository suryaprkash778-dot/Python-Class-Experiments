# 2.Create a variable to store your age and print its type using type().
age = input("what is your age\n")
print(type(age))

# 3.Declare a string variable called x and assign it the value “Hello”.
X="hello"

# 4.Print out the value of x
print(X)

#4.Take different data types and print values using print function.
age = input("what is your age\n")
name = input("what is your name\n")
height=input("what is your height in feet\n")
print(age)
print(name)
print(height)

#5.Declare these variables (x, y and z) as integers. Assign a value
# of 9 to x, Assign a value of 7 to y, perform addition, multiplication,
# division and subtraction on these two variables and Print out the result.
x=9
y=7
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#6.	Write a program to compute the length of the hypotenuse (c)
# of a right triangle using Pythagoras theorem.
length = float(input("enter length of triangle"))
base = float(input("enter base of triangle"))
h = length**2 + base**2
print(h**(1/2))

#7.	Write a program to find simple interest.
p = float(input("enter the amount"))
t = float(input("enter time"))
r = float(input("enter rate of interest"))
SI=(p*t*r)/100
print(SI)

#8.	Write a program to find area of triangle when length of sides are given.
a,b,c= map(int,input("enter sides of triangle").split())
S=(a+b+c)/2
area=(S*(S-a)*(S-b)*(S-c))**1/2
print(area)

#9.	Write a program to convert given seconds into hours,
# minutes and remaining seconds.
time = int(input("enter time in seconds\n"))
hour = (time//3600)
minutes = (time%3600)//60
rsec = minutes % 60

#10.Write a program to swap two numbers without taking additional variable.
var1 = int(input("enter first number"))
var2 = int(input("enter second number"))

var1 = var1 ^ var2
var2 = var1 ^ var2
var1 = var1 ^ var2

print(f"before swap {var1, var2}")
print(f"after swap {var1, var2}")

#11.Write a program to find sum of first n natural numbers.
sum=0
num = int(input("enter the number\n"))
for n in range(1,num+1):
    sum+=n
print(sum)





