# a = {1,2,2,3,4,5}
# b = {11,1,2,4,5}

# print(a|b)

# print("\n", a & b)

# print("\n", a - b)

# class student:
#     def __init__ (self,name,activity):
#         self.name = name
#         self.activity = activity

# s1 = student("Joe","Chess Club")
# s2 = student("Joanna", "Choir")

# print(s1.name,s1.activity)
# print(s2.name,s2.activity)

# Activity
# class Student:
#     def __init__ (self,name,age):
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print("Hello")

# s1 = Student("Joe", 12)
# s2 = Student("Joanna", 13)

# s1.introduce()
# s2.introduce()


# stack = []
# numbers = stack
# stack.extend([5, 10, 15])
# stack.pop()
# print(stack[-1])
# print(stack)

# queue = []
# numbers = queue
# queue.append(10)
# queue.append(20)
# queue.append(30)

# front_value = queue.pop(0)
# print(front_value)
# print(queue)

class Animal:
    def __init__(self,name,species,activities):
        self.name = name
        self.species = species
        self.activities = activities

    def add_activity(self,activity):
        self.activity =  []
        self.activity.append(activity)

    def show_activities(self):
        print(self.activity)



