#1.	Find a factorial of given number.
num = int(input("enter  number"))
fac = 1
while num >0:
    fac *=num
    num-=1
print(fac)

#2.	Find whether the given number is Armstrong number.
num1 = int(input("enter  number"))
digit = str(num1)
power=len(digit)
summ=0
for num in digit:
    summ += int(num) ** power
if summ == num1:
    print("its an armstrong number")
else:
    print("it  is not an armstrong numnber")


#3.	Print Fibonacci series up to given term.
num2 = int(input("enter  number"))
a,b=0,1
for _ in range(num2):
    a,b= b,a+b
    print(a)

#4.	Write a program to find if given number is prime number or not.
num3 = int(input("enter  number"))
is_prime=True
for num in range(2,num3) :
    if num3%num == 0:
        is_prime = False
        break
if is_prime:
    print("num is prime")
else:
    print("num is not prime")

#5.	Check whether given number is palindrome or not.
num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")



#6.	Write a program to print sum of digits.
num5 = int(input("enter  number"))
digit=str(num5)
sum1 =0
for num in digit:
    sum1 += int(num)
print(sum1)


#7.	Count and print all numbers divisible by 5 or 7 between 1 to 100.
count=0
for _ in range(1,101):
    if _%5==0 or _%7==0:
        count+=1
        print(_)



#8.	Convert all lower cases to upper case in a string.
string = input("enter  a string")
print(string.upper())


#9.	Print the table for a given number:
num6 = int(input("enter  number"))
for num in range(11):
    print(f"5 * {num} = {5*num}")


#10.	Write a program to print the following pattern
#123454321
#1234 *4321
#123  * * 321
#12   * * *  21
#1    * * * *   1
n = 5 
for i in range(n):
    for j in range(1, n - i + 1):
        print(j, end="")
    for j in range(i):
        print(" *", end="")
    for j in range(n - i, 0, -1):
        print(j, end="")
    print() 


#11.	Write a program to print the sum of the following series
#1+ ½ + 1/3 + ¼ +….+1/n

n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += 1 / i

print("Sum of the series up to 1/", n, "is:", sum_series)


