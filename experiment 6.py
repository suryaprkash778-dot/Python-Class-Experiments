#4.	Write a recursive function to print Fibonacci series upto n terms.
def fibonacci(num):
    if num ==1 or num==0:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

for num in range(6):
    print(fibonacci(num))


#3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
def print_num(num):
    if num<0:
        return
    print(num)
    print_num(num-1)
print_num(5)

#5.	Write a lambda function to find volume of cone.
cone_volume = lambda r,h: (3.14*(r**2)*h)/3
print(cone_volume(3,4))



#6.	Write a lambda function which gives tuple of max and min from a list.
