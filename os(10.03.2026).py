# Task (5–10 min)
#  Use NumPy to analyze a small dataset.
# 1️⃣ Create an Array
# import numpy as np
# temps = np.array([22, 25, 28, 30, 27, 31, 29])
# 2️⃣ Analyze the Data
# Calculate:
# • Average temperature → np.mean(temps)
#  • Highest value → np.max(temps)
#  • Lowest value → np.min(temps)
# 3️⃣ Filter the Dataset
# Find temperatures above 28°C
# temps[temps > 28]
# Goal
# Practice using:
# • NumPy arrays
# • Statistical functions
# • Boolean filtering


import numpy as np

sales = np.array([450,300,410,503,781,675,453,250, 170])

sales = sales.astype(float)

print(sales)

s_average = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)

print("Data Analysis: ")

print("Average Sales:", round(s_average,2))
print("Maximum Sales:", max_sales)
print("Minimum Sales:", min_sales)

print("Filtered Sales: ")
f_sales = sales[sales > 400]

print(f_sales)



