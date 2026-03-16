#1.	Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.)
def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum
    
sequence = [12, 4, 56, 7, 89, 23, 1]
max_val, min_val = find_max_min(sequence)

print("Maximum:", max_val)
print("Minimum:", min_val)

#2.	Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 
def sum_of_cubes(n):
    if n <= 0:
        return "Please enter a positive integer."
    total = 0
    for i in range(1, n):   
        total += i ** 3    
    return total
    
num = 5
result = sum_of_cubes(num)
print(f"Sum of cubes of numbers less than {num} is: {result}")

#3.	Write a Python function to print 1 to n using recursion. (Note: Do not use loop)
def print_num(num):
    if num<0:
        return
    print(num)
    print_num(num-1)
print_num(5)


#4.	Write a recursive function to print Fibonacci series upto n terms.
def fibonacci(num):
    if num ==1 or num==0:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)

for num in range(6):
    print(fibonacci(num))




#5.	Write a lambda function to find volume of cone.
cone_volume = lambda r,h: (3.14*(r**2)*h)/3
print(cone_volume(3,4))



#6.	Write a lambda function which gives tuple of max and min from a list.
max_min = lambda lst: (sorted(lst)[-1], sorted(lst)[0])
numbers = [10, 6, 8, 90, 12, 56]
print(max_min(numbers))  

#7.	Write functions to explain mentioned concepts:
#a.	Keyword argument
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(name="Alice", age=25)
greet(age=30, name="Bob")   

#b.	Default argument
def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")
greet("Charlie")        
greet("Diana", 22)      

#c.	Variable length argument
# Using *args
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add_numbers(1, 2, 3)
add_numbers(10, 20, 30, 40)

# Using **kwargs
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Eve", age=28, city="Delhi")


#8.	Write a program to check whether all the values in a dictionary are same or not using lambda function.
data = {"a": 10, "b": 10, "c": 10, "d": 10}
all_values_same = lambda d: len(set(d.values())) == 1
print("All values same?" , all_values_same(data))


#9.	Write a program to create two lists and generate a dictionary with keys from list1 and values from list2.
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]
result = dict(zip(list1, list2))
print("Generated Dictionary:", result)






