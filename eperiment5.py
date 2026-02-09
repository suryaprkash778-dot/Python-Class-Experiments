#3.	WAP to input a list of scores for N students in a list data type.
# Find the score of the runner-up and print the output.
num = int(input("enter number of players"))
scores = map(int, input("enter scores").split())
largest  = 0
second = 0
for num in scores :
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

print(f"runner up score is {second}")
