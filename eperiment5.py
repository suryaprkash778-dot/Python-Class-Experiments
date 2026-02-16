# WAP to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output.

n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

max_score = max(scores)

new_list = []
for i in scores:
    if i != max_score:
        new_list.append(i)

runner_up = max(new_list)
print("Runner-up score:", runner_up)

# Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks.

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
