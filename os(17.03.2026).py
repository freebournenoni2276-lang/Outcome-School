# class Node:
#     def __init__(self, data):
#         self.data = data   # value stored in the node
#         self.next = None   # reference to the next node


# class LinkedList:
#     def __init__(self):
#         self.head = None   # start of the list

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         current = self.head
#         while current.next is not None:
#             current = current.next

#         current.next = new_node

#     def insert_at_index(self, index, data):

#         if index < 0:
#             raise IndexError("Negative index not allowed")

#         if index == 0:
#             self.insert_at_beginning(data)
#             return

#         new_node = Node(data)
#         current = self.head
#         current_index = 0

#         # move to node before the desired index
#         while current is not None and current_index < index - 1:
#             current = current.next
#             current_index += 1

#         if current is None:
#             raise IndexError("Index out of bounds")

#         new_node.next = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")


# linked_list = LinkedList()

# linked_list.insert_at_beginning(50)
# linked_list.insert_at_beginning(40)
# linked_list.insert_at_beginning(30)

# linked_list.insert_at_end(60)
# linked_list.insert_at_end(70)
# linked_list.insert_at_end(80)

# linked_list.display()

# 🟦 Exercise Part 1 — Practice Inserting Nodes
# Goal: Build a linked list by inserting values at the beginning, end, and a specific index.
# What she should do
# Create a new linked list object at the bottom of the file.
# Insert three values at the beginning to see how the list grows from the front.
# Insert two values at the end to see how the list grows from the back.
# Insert one value at a specific index to see how the list changes in the middle.
# Exact instructions
# Add the value 100 at the beginning.
# Add the value 90 at the beginning.
# Add the value 80 at the beginning.
# Add the value 200 at the end.
# Add the value 300 at the end.
# Insert the value 95 at index 2 (this should appear between 90 and 80).
# What she should expect
# The list should show the new values in the correct order.
# Values added at the beginning appear at the front.
# Values added at the end appear at the back.
# The value inserted at index 2 should appear in the middle.
# 🟩 Exercise Part 2 — Practice Deleting Nodes
# Goal: Remove nodes using both deletion methods and observe how the list changes.
# What she should do
# Use the delete_by_value function to remove a specific value.
# Use the delete_at_index function to remove a node at a specific position.
# Exact instructions
# Delete the value 95 (the one inserted in the middle).
# Delete the value 300 (the last value).
# Delete the node at index 0 (this removes the head).
# Delete the node at index 2 (removes a middle node).
# What she should expect
# After deleting by value, the list should no longer contain that number.
# After deleting at index 0, the head should move to the next node.
# After deleting at index 2, the list should “skip over” that node.
# The list should shrink correctly each time.
# 🟨 Exercise Part 3 — Display and Check Your Work
# Goal: Confirm that insertions and deletions worked correctly.
# What she should do
# Use the display() function after each major step.
# Check that the list updates exactly as expected.
# Make sure no values appear twice and no values remain after deletion.
# What she should expect
# A clean, correct linked list after each operation.
# No errors unless she tries to delete an invalid index (which is good practice too).

class Node:
    def __init__(self, data):
        self.data = data   # value stored in the node
        self.next = None   # reference to the next node
class LinkedList:
    def __init__(self):
        self.head = None   # start of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Negative index not allowed")
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        current_index = 0
        # move to node before the desired index
        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1
        if current is None:
            raise IndexError("Index out of bounds")
        new_node.next = current.next
        current.next = new_node
    def delete_by_value(self, value):
        if self.head is None:
            return  # or raise an error
        # if the head node is to be deleted
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next
        if current.next is None:
            # value not found
            return  # or raise ValueError("Value not found")
        # skip the node with the target value
        current.next = current.next.next
    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Negative index not allowed")
        if self.head is None:
            raise IndexError("Delete from empty list")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        current_index = 0
        while current is not None and current_index < index - 1:
            current = current.next
            current_index += 1
        if current is None or current.next is None:
            raise IndexError("Index out of bounds")
        current.next = current.next.next
    def search(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # not found
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def display(self):
        current = self.head 
        while current is not None: 
            print(current.data, end=" -> ")
            current = current.next 
        print("None")
# Example usage
if __name__ == "__main__": 
    ll = LinkedList()
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(90)
    ll.insert_at_beginning(80)
    print("Linked List after insertions at the beginning:")
    ll.display()

    ll.insert_at_end(200)
    ll.insert_at_end(300)
    print("Linked List after insertions at the end:")
    ll.display()
    
    ll.insert_at_index(2,95)
    print("Linked List after insertions at an index:")
    ll.display()

    ll.delete_by_value(95)
    print("Linked List after deleting value 95:")
    ll.display()

    ll.delete_by_value(300)
    print("Linked List after deleting value 300:")
    ll.display()

    ll.delete_at_index(0)
    print("Linked List after deleting index 0:")
    ll.display()

    ll.delete_at_index(2)
    print("Linked List after deleting index 2:")
    ll.display()




    # ll.insert_at_end(10)
    # ll.insert_at_end(20)
    # ll.insert_at_end(30)
    # ll.insert_at_beginning(5)
    # ll.insert_at_index(2, 15)
    # print("Linked List after insertions:")
    # ll.display()
    # print(f"Length of the list: {ll.length()}")
    # print(f"Index of value 20: {ll.search(20)}")
    # print(f"Index of value 40: {ll.search(40)}")
    # ll.delete_by_value(15)
    # print("Linked List after deleting value 15:")
    # ll.display()
    # ll.delete_at_index(1)
    # print("Linked List after deleting index 1:")
    # ll.display()


#      Real‑Life Scenario
# A person behaves differently depending on where they are:
# At home → relaxing
# At school → studying
# At work → working
# Question:  
# What OOP concept does this represent, and why?
# 2️⃣ Python Code — Predict the Output
# python
# class Bird:
#     def move(self):
#         return "Flying"

# class Fish:
#     def move(self):
#         return "Swimming"

# animals = [Bird(), Fish()]

# for a in animals:
#     print(a.move())
# Question:  
# What will this code print, and how does it show polymorphism?
# 3️⃣ Real‑Life Scenario
# A “start” button is pressed:
# On a car, it starts the engine
# On a computer, it boots the system
# On a washing machine, it starts washing
# Question:  
# How is this similar to calling the same method name on different objects in Python?
# 4️⃣ Python Code — Identify the Polymorphism
# python
# class Teacher:
#     def speak(self):
#         return "Explaining a lesson"

# class Student:
#     def speak(self):
#         return "Asking a question"

# class Principal:
#     def speak(self):
#         return "Giving an announcement"

# people = [Teacher(), Student(), Principal()]

# for p in people:
#     print(p.speak())
# Question:  
# What type of polymorphism is this (method overriding, overloading, or operator overloading)?
# 5️⃣ Python Code — What Happens?
# python
# class Dog:
#     def sound(self):
#         return "Bark!"

# class RobotDog:
#     def sound(self):
#         return "Electronic bark!"

# def make_sound(obj):
#     print(obj.sound())

# make_sound(Dog())
# make_sound(RobotDog())
# Question:  
# Why does the same function make_sound() work for both objects even though they are different classes?