#5.	Given a string containing both upper and lower case alphabets.
# Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
from collections import Counter
string = input("enter string").upper()
count = Counter(c for c in  string if string.isalpha())
for char , fre in count.items():
    print(fre ,char)
