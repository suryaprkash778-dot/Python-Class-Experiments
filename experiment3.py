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
