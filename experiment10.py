#1.	Create numpy array to find sum of all elements in an array.
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

total_sum = np.sum(arr)

print("Array:", arr)
print("Sum of all elements:", total_sum)

#2.	 Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 
import numpy as np
arr = np.array([[12, 7, 9],
                [8, 15, 3],
                [4, 10, 6]])

print("Array:\n", arr)
# 1. Sum of all rows individually
row_sum = np.sum(arr, axis=1)
print("Sum of each row:", row_sum)

# 2. Sum of all columns individually
col_sum = np.sum(arr, axis=0)
print("Sum of each column:", col_sum)

# 3. Find 2nd maximum element in the array
flattened = arr.flatten()
sorted_arr = np.sort(flattened)
second_max = sorted_arr[-2]
print("Second maximum element:", second_max)

#3.	Perform Matrix multiplication of any 2 n*n matrices.
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

C = np.dot(A, B)   # or use A @ B

print("Result of Matrix Multiplication:\n", C)

#Write a Pandas program to get the powers of an array values element-wise. 
#Note: First array elements raised to powers from second array
#Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
import pandas as pd
import numpy as np
data = {'X':[78,85,96,80,86],
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Element-wise power: first array elements raised to powers from second array
# Example: X^Y, Y^Z, Z^X
df_power = pd.DataFrame({
    'X^Y': np.power(df['X'], df['Y']),
    'Y^Z': np.power(df['Y'], df['Z']),
    'Z^X': np.power(df['Z'], df['X'])
})

print("\nElement-wise Powers:\n", df_power)

#5. Write a Pandas program to get the first 3 rows of a given DataFrame.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 
                'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a','b','c','d','e','f','g','h','i','j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:\n", df)

# Get first 3 rows
print("\nFirst three rows of the data frame:\n")
print(df.iloc[:3])

#6. Write a Pandas program to find and replace the missing values in a given DataFrame which do not have any valuable information.
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a','b','c','d','e','f','g','h','i','j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

print("Original DataFrame:\n", df)

# Detect missing values
print("\nMissing values summary:\n", df.isnull().sum())

# Replace missing values with 0 (or any placeholder since they have no valuable info)
df_cleaned = df.fillna(0)

print("\nDataFrame after replacing missing values:\n", df_cleaned)

#7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 6)
y = np.array([10, 15, 20, 25, 30])

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# 1. Line Plot
axs[0, 0].plot(x, y, marker='o', color='blue')
axs[0, 0].set_title("Line Plot")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")

# 2. Bar Chart
axs[0, 1].bar(x, y, color='green')
axs[0, 1].set_title("Bar Chart")
axs[0, 1].set_xlabel("Categories")
axs[0, 1].set_ylabel("Values")

# 3. Scatter Plot
axs[0, 2].scatter(x, y, color='red')
axs[0, 2].set_title("Scatter Plot")
axs[0, 2].set_xlabel("X-axis")
axs[0, 2].set_ylabel("Y-axis")

# 4. Histogram
data = np.random.randn(1000)
axs[1, 0].hist(data, bins=20, color='purple', edgecolor='black')
axs[1, 0].set_title("Histogram")
axs[1, 0].set_xlabel("Bins")
axs[1, 0].set_ylabel("Frequency")

# 5. Pie Chart
labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [40, 25, 20, 15]
axs[1, 1].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title("Pie Chart")

# Hide the empty subplot (bottom-right)
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()





