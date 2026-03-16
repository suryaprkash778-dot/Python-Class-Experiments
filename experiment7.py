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

