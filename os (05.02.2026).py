# class Student:
#     def __init__(self):
#         self.__id = 12345

# s = Student()
# # print(s.__id) ❌ Error  
# print(s._Student__id)   # Works (name mangling)

# class BankAccount:
#     def __init__(self):
#         self.__balance = 0

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Invalid amount")

# acc = BankAccount()
# acc.set_balance(500)
# print(acc.get_balance())

# class Bank:
#     def __init__ (self):
#         self.__balance = 0
#     def deposit (self, amount):
#         self.__balance += amount

# import numpy
# import requests

# print("Modules imported successfully")

# import numpy

# arr_ay = numpy.array([1,2,3,4,5])

# print(arr_ay)

# print(arr_ay + 5)

# nums = [8,2,6,1]
# for i in range(len(nums)):
#     for j in range(len(nums)-1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] =  nums[j + 1], nums[j]
# print(nums)


# num_1 = [2,4,6,8,10]
# for i in range(len(num_1)):
#     for j in range(len(num_1)-1):
#         if num_1[j] > num_1[j + 1]:
#             num_1[j], num_1[j + 1] =  num_1[j + 1], num_1[j]
# print(num_1)

# numbers = [5, 3, 1, 4]

# for i in range(1, len(numbers)):
#     key = numbers[i]
#     j = i - 1

#     # Move elements greater than key one position ahead
#     while j >= 0 and key < numbers[j]:
#         numbers[j + 1] = numbers[j]
#         j -= 1

#     numbers[j + 1] = key

# print(numbers)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# node_1 = Node(1)
# node_2 = Node(3)
# node_3 = Node(5)

# node_1.next = node_2
# node_2.next = node_3
# current = node_1 # head


# while current is not None:
#     print(current.data) 
#     current = current.next


print("Class Acticty")

# Bubble Sort
nums = [8, 3, 6, 1, 4]
for i in range(len(nums)):
    for j in range(len(nums)-1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] =  nums[j + 1], nums[j]
print(nums)


# Insertion sort
numbers = [9, 2, 7, 5]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    # Move elements greater than key one position ahead
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print(numbers)


















