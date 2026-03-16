#1 Input number of values
n = int(input("Enter how many values: "))

values = [int(input(f"Enter value {i+1} (0-3): ")) for i in range(n)]

count_0 = values.count(0)
count_1 = values.count(1)
count_2 = values.count(2)
count_3 = values.count(3)

print("0:", count_0)
print("1:", count_1)
print("2:", count_2)
print("3:", count_3)


#2 Create a tuple with n numeric values and Find the average of all values
numbers = (10, 20, 30, 40, 50)   # Example tuple

average = sum(numbers) / len(numbers)

print("Numbers:", numbers)
print("Average:", average)


#3 WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.

n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

max_score = max(scores)

new_list = []
for i in scores:
    if i != max_score:
        new_list.append(i)

runner_up = max(new_list)
print("Runner-up score:", runner_up)

#4.	Create a dictionary of n persons where key is name and value is city.
students = {
    "surya":"jaipur",
    "praneesh":"mumbai",
    "divay":"karnal",
    "ved":"pune",
    "saxena":"bareli"
}
#a) Display all names
for x in students:
    print(x)

#b) Display all city names
print("\n")
for x in students:
    print(students[x])

#c) Display student name and city of all students.
for x,y  in students.items():
    print(x,y)

#d) Count number of students in each city.
print("\nNumber of Students in Each City:")
city_count = {}
for city in students.values():
    city_count[city] = city_count.get(city, 0) + 1

for city, count in city_count.items():
    print(f"{city}: {count}")

#5.	Store details of n movies in a dictionary by taking input from the user.
#Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :-
movies ={}
n = int(input("enter number of movies\n"))
for i in range(n):
    print(f"\nEnter details for movie {i + 1}:")
    name = input("Movie Name: ")
    year = int(input("Release Year: "))
    director = input("Director Name: ")
    production_cost = float(input("Production Cost: "))
    collection = float(input("Collection Made : "))

    movies[name] = {
        "year": year,
        "director": director,
        "production_cost": production_cost,
        "collection": collection
    }
#a)	print all movie details
for name, details in movies.items():
    print(f"{name} → {details}")

#b)	display name of movies released before 2015
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

#c)	print movies that made a profit.
for name, details in movies.items():
        if details["collection"]-details["production_cost"] > 0:
            print(name)

#d)	print movies directed by a particular director.
director_name = input("\nEnter director name to search: ")
for name, details in movies.items():
    if details["director"].lower() == director_name.lower():
        print(name)

#6.	Create a contact book where users can store, search, update, and delete contacts. Use dictionary for storing contacts.
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        if name in contacts:
            print("Contact already exists.")
        else:
            contacts[name] = {"phone": phone, "email": email}
            print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            if phone:
                contacts[name]["phone"] = phone
            if email:
                contacts[name]["email"] = email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        if contacts:
            print("\n--- All Contacts ---")
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("No contacts available.")

    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")



#7 Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.

tasks = []

while True:
    print("\n--- Todo List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting Todo List Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
