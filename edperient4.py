#  Write a program to count and display the number of capital letters in a given string.

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        count += 1

print("Number of capital letters:", count)

#  Count total number of vowels in a given string.

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch in 'aeiouAEIOU':
        count += 1

print("Total number of vowels:", count)

# Input a sentence and print words in separate lines.

sentence = input("Enter a sentence: ")
words = sentence.split()

for word in words:
    print(word)

# WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

s = input("Enter the string: ")
sub = input("Enter the substring: ")

count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        count += 1

print("Substring occurs", count, "times")

# Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.

text = input("Enter a string: ")
count = {}

for ch in text:
    ch = ch.upper()
    if ch.isalpha():
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

for key in sorted(count):
    print(count[key], key, sep="")

# Program to count number of unique words in a given sentence using sets.

sentence = input("Enter a sentence: ")

words = sentence.lower().split()
unique_words = set(words)

print("Number of unique words:", len(unique_words))

# Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#a)Fruits which are in both sets s1 and s2
#b)Fruits only in s1 but not in s2
#c)Count of all fruits from s1 and s2

n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("Enter fruits for set s1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for set s2:")
for i in range(n):
    s2.add(input())


print("Fruits in both s1 and s2:", s1.intersection(s2))


print("Fruits only in s1:", s1.difference(s2))


all_fruits = s1.union(s2)
print("Count of all fruits:", len(all_fruits))

# Take two sets and apply various set operations on them :
#S1 = {Red ,yellow, orange , blue }
#S2 = {violet, blue , purple}


S1 = {"Red", "Yellow", "Orange", "Blue"}
S2 = {"Violet", "Blue", "Purple"}


print("Union:", S1 | S2)


print("Intersection:", S1 & S2)


print("S1 - S2:", S1 - S2)


print("S2 - S1:", S2 - S1)


print("Symmetric Difference:", S1 ^ S2)

print("Is S1 subset of S2?", S1.issubset(S2))
print("Is S2 subset of S1?", S2.issubset(S1))


print("Number of elements in S1:", len(S1))
print("Number of elements in S2:", len(S2))
