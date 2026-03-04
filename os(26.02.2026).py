# numbers = [1, 2, 3, 4, 5]
# # Square each number
# squared_numbers = map(lambda x: x**2, numbers)
# print(list(squared_numbers))
# # Output: [1, 4, 9, 16, 25]

# fruits = ['apple', 'banana', 'cherry']
# # Convert all strings to uppercase
# upper_fruits = map(str.upper, fruits)
# print(list(upper_fruits))
# # Output: ['APPLE', 'BANANA', 'CHERRY']
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# # Add corresponding elements from both lists
# added_numbers = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(added_numbers))
# # Output: [5, 7, 9]

# from functools import reduce
# import operator

# numbers = [2, 3, 4, 5]
# product = reduce(operator.mul, numbers)
# # Result: 120 (equivalent to (((2*3)*4)*5))
# from functools import reduce

# numbers = [3, 2, 5, 4, 1]
# max_element = reduce(lambda x, y: x if x > y else y, numbers)
# # Result: 5

# import matplotlib.pyplot as plt

# # Data
# months = ["Jan", "Feb", "Mar", "Apr", "May"]
# scores = [65, 70, 72, 80, 85]

# # Create line graph
# plt.plot(months, scores)

# # Labels
# plt.xlabel("Month")
# plt.ylabel("Test Score")
# plt.title("Student Test Scores Over Time")

# # Show graph
# plt.show()

# def double(x):
#    return x * 2
# numbers = [5, 10, 15, 20]
# result = list(map(double, numbers))
# print(result)

# def is_positive(x):
#    return x > 0
# values = [100, -50, 200, -10, 300]
# filtered = list(filter(is_positive, values))
# print(filtered)

from functools import reduce
def add(x, y):
   return x + y
data = [1, 2, 3, 4]
total = reduce(add, data)
print(total)