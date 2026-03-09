# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# plt.plot(x,y)
# plt.title('Prime Numbers')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt

# sizes = [40,25,20,15]
# labels = ['Apples','Bananas','Cherries','Dates']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%')
# plt.title('Pie Chart Example')
# plt.show()

# print('Pie chart displayed sucessfully \\n')

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]

# plt.scatter(x, y, color='red')
# plt.title('Prime Numbers Scatter Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# data = [np.random.randn(100), np.random.randn(100) + 2]

# plt.boxplot(data)
# plt.title('Box Plot Example')
# plt.xlabel('Dataset')
# plt.ylabel('Value')
# plt.show()

# import seaborn as sns
# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.DataFrame({
#     'x': [1,2,3,4,5],
#     'y': [2,3,5,7,11]
# })



# import pandas as pd
# # -----------------------------------------
# # Create a small sample sales dataset
# # -----------------------------------------
# sales = pd.DataFrame({
#     'product': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
#     'region':  ['North', 'South', 'West',
#                 'North', 'South', 'West',
#                 'North', 'South', 'West'],
#     'price':   [10, 12, 11,
#                 20, 22, 19,
#                 15, 14, 16]
# })
# print("Original Sales Data:")
# print(sales)
# # -----------------------------------------
# # Create a pivot table with multiple metrics
# # -----------------------------------------
# pivot = pd.pivot_table(
#     sales,
#     values="price",
#     index="product",
#     columns="region",
#     aggfunc=["mean", "max", "count"]
# )
# print("\nPivot Table:")
# print(pivot)
# Pivot Table:
#          mean               max            count
# region  North South  West North South West North South West
# product
# A        10.0  12.0  11.0    10    12   11     1     1    1
# B        20.0  22.0  19.0    20    22   19     1     1    1
# C        15.0  14.0  16.0    15    14   16     1     1    1

# region  product  price
# 0     EU   Laptop   1300
# 1     EU    Phone    800
# 2     US   Laptop   1200
# 3     US    Phone    750
# 4     US   Tablet    500

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1. Load your dataset
#    (Instructor: students will already have df loaded)
# ----------------------------------------------------
# Example placeholder:
# df = pd.read_csv("your_file.csv")

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Brian", "Chloe", "David", "Ella", "Frank", "Grace", "Henry"],
    "Age": [18, 19, 20, 21, 18, 22, 19, 20],
    "Course": [
        "Computer Science",
        "Mathematics",
        "Business Administration",
        "Accounting",
        "Psychology",
        "Biology",
        "Economics",
        "Information Technology"
    ],
    "GPA": [3.5, 3.7, 3.2, 3.8, 3.6, 3.1, 3.9, 3.4]
}

df = pd.DataFrame(data)

df.to_csv("practice.csv", index=False)

df = pd.read_csv("practice.csv")

print("Dataset preview:")
print(df.head())


# ----------------------------------------------------
# 2. Group data by product and calculate average sales
#    (STUDENTS: write your groupby + mean here)
# ----------------------------------------------------
# avg_sales = ...

# print("\nAverage sales per product:")
# print(avg_sales)


# ----------------------------------------------------
# 3. Sort results (highest first)
#    (STUDENTS: write your sort_values here)
# ----------------------------------------------------
# avg_sales_sorted = ...

# print("\nSorted results:")
# print(avg_sales_sorted)


# ----------------------------------------------------
# 4. Create a bar chart
#    (STUDENTS: write your plotting code here)
# ----------------------------------------------------
# plt.bar(...)
# plt.title(...)
# plt.xlabel(...)
# plt.ylabel(...)
# plt.show()


# ----------------------------------------------------
# 5. Simple error handling example
#    (STUDENTS: wrap input() in try/except)
# ----------------------------------------------------
# try:
#     user_value = int(input("Enter a number: "))
#     print("You entered:", user_value)
# except ValueError:
#     print("Invalid input")



# Task (10 min)
# Using the dataset in your notebook:
# 1️⃣ Group data by product
#  Calculate the average sales
# 2️⃣ Sort results
#  Show highest values first
# 3️⃣ Create a bar chart
#  Visualize average sales per product
# 4️⃣ Add simple error handling
# Expected Workflow
# Group → Average → Sort → Plot
# Goal
# Practice using:
# groupby()

# mean()

# sort_values()

# visualization

# basic try/excepta