#1.	Add few names, one name in each row, in “name.txt file”.
vowel_name = 0
name_list = []
num = int(input("how many names you want to add"))
with open("name.txt","w+") as f:
    for i in range(num):
        name = input("enter name")
        name_list.append(name)
        f.write(name)
        if name[0] in ["a","e","i","o","u","A","E","I","O","U"] :
            vowel_name+=1
#a.	Count no of names
print(len(name_list))
#b.	Count all names starting with vowel
print(max(name_list,key = len))
#c.	Find longest name
print(vowel_name)


#2.	Store integers in a file.
count = 0
with open("file.txt","w") as f:
    f.write(input("enter numbers with space"))
with open("file.txt","r") as f:
    num_list = list(map(int,f.readline().split()))
# a.	Find the max number
print(max(num_list))
#b.	Find average of all numbers
print(sum(num_list)/len(num_list))
#c.	Count number of numbers greater than 100
for num in num_list:
    if num>100:
        count+=1
print(count)

#3.	Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
#Example:
#Dehradun 5.78 308.20
#Delhi 190 1484
#Open file city.txt and read to:
#a.	Display details of all cities
#b.	Display city names with population more than 10Lakhs
#c.	Display sum of areas of all cities
# Program to read city.txt and process city details

def read_city_file(filename):
    cities = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                city = parts[0]
                population = float(parts[1])   # in lakhs
                area = float(parts[2])         # in sq km
                cities.append((city, population, area))
    return cities

def display_all(cities):
    print("\n--- All City Details ---")
    for city, pop, area in cities:
        print(f"City: {city}, Population: {pop} lakhs, Area: {area} sq km")

def display_pop_gt_10(cities):
    print("\n--- Cities with Population > 10 lakhs ---")
    for city, pop, area in cities:
        if pop > 10:
            print(city)

def display_sum_area(cities):
    total_area = sum(area for _, _, area in cities)
    print("\n--- Sum of Areas of All Cities ---")
    print(f"Total Area = {total_area:.2f} sq km")


# --- Main Program ---
filename = "city.txt"
cities = read_city_file(filename)

display_all(cities)
display_pop_gt_10(cities)
display_sum_area(cities)

#4.	 Input two values from user where the first line contains N, the number of test cases. 
#The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError. 
#Sample input
#1 0
#2 $
#3 1 
# Program to perform integer division with exception handling

N = int(input("Enter number of test cases: "))

for i in range(N):
    try:
        # Read space-separated values
        a, b = input().split()
        a, b = int(a), int(b)   # Convert to integers
        print(a // b)           # Perform integer division
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

#5.	Create multiple suitable exceptions for a file handling program. 
# Custom Exceptions
class FileNotFoundCustomError(Exception):
    pass

class FileEmptyError(Exception):
    pass

class FileFormatError(Exception):
    pass


def read_file(filename):
    try:
        # Try opening the file
        with open(filename, "r") as f:
            content = f.read()

            # Check if file is empty
            if not content.strip():
                raise FileEmptyError("The file is empty.")

            # Example: check format (must contain at least one space)
            if " " not in content:
                raise FileFormatError("Invalid file format: expected space-separated values.")

            print("File content:\n", content)

    except FileNotFoundError:
        raise FileNotFoundCustomError(f"File '{filename}' not found.")
    except FileEmptyError as e:
        print("Error:", e)
    except FileFormatError as e:
        print("Error:", e)


# --- Main Program ---
filename = input("Enter filename: ")

try:
    read_file(filename)
except FileNotFoundCustomError as e:
    print("Error:", e)


#6.	Write a program to create a counter to show that how many times the program is executed.
# Program to count how many times it has been executed

def read_counter(filename):
    try:
        with open(filename, "r") as f:
            return int(f.read().strip())
    except FileNotFoundError:
        # If file doesn't exist, start counter at 0
        return 0
    except ValueError:
        # If file content is invalid, reset counter
        return 0

def write_counter(filename, count):
    with open(filename, "w") as f:
        f.write(str(count))

# --- Main Program ---
filename = "counter.txt"

# Read current count
count = read_counter(filename)

# Increment count
count += 1

# Save updated count
write_counter(filename, count)

# Display result
print(f"This program has been executed {count} times.")

