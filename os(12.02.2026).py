# import numpy as np

# arr_ay = np.array([1,2,3,4])
# print(arr_ay)

# print(arr_ay + 2)
# print(arr_ay * 2)

#NOTES FOR BUBBLE SORTING#
#list = [5,2,4,6,1,3]
# key: 2
# numbers[j + 1] 2
# numbers[j + 1] 5
# numbers:  [5, 5, 4, 6, 1, 3]
# out side the while loop: numbers[j + 1] 2
# out numbers:  [2, 5, 4, 6, 1, 3]
# key: 4
# numbers[j + 1] 4
# numbers[j + 1] 5
# numbers:  [2, 5, 5, 6, 1, 3]
# out side the while loop: numbers[j + 1] 4
# out numbers:  [2, 4, 5, 6, 1, 3]
# key: 6
# out side the while loop: numbers[j + 1] 6
# out numbers:  [2, 4, 5, 6, 1, 3]
# key: 1
# numbers[j + 1] 1
# numbers[j + 1] 6
# numbers:  [2, 4, 5, 6, 6, 3]
# numbers[j + 1] 6
# numbers[j + 1] 5
# numbers:  [2, 4, 5, 5, 6, 3]
# numbers[j + 1] 5
# numbers[j + 1] 4
# numbers:  [2, 4, 4, 5, 6, 3]
# numbers[j + 1] 4
# numbers[j + 1] 2
# numbers:  [2, 2, 4, 5, 6, 3]
# out side the while loop: numbers[j + 1] 1
# out numbers:  [1, 2, 4, 5, 6, 3]
# key: 3
# numbers[j + 1] 3
# numbers[j + 1] 6
# numbers:  [1, 2, 4, 5, 6, 6]
# numbers[j + 1] 6
# numbers[j + 1] 5
# numbers:  [1, 2, 4, 5, 5, 6]
# numbers[j + 1] 5
# numbers[j + 1] 4
# numbers:  [1, 2, 4, 4, 5, 6]
# out side the while loop: numbers[j + 1] 3
# out numbers:  [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]


# Content (Small Code Block):
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# first = Node(10)
# second = Node(20)
# first.next = second
# temp = first
# while temp:
#     print(temp.data, end=" -> ")
#     temp = temp.next
# Bottom Instruction:
#  “Change the numbers or add one more node.”