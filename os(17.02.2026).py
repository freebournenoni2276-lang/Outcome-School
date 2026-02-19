# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyList:
#     def __init__(self):
#         self.head = None

#     def insert_begin(self, data):
#         new = Node(data)
#         new.next = self.head # TODO: link new node with head
#         self.head = new

# dll = DoublyList()
# dll.insert_begin(10)
# dll.insert_begin(20)
# dll.insert_begin(30)

# temp = dll.head
# while temp:
#     print(temp.data)
#     temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyList:
    
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        if self.head is not None: 
            self.head.prev = new 
        self.head = new

dll = DoublyList()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)

temp = dll.head
while temp:
    print(temp.data)
    temp = temp.next

# class Node:
#     def init(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None
# class DoublyList:
#     def init(self):
#         self.head = None
#     def insert_begin(self, data):
#         new = Node(data)
#         if self.head:  # if list isn't empty
#             new.next = self.head
#             self.head.prev = new
#         self.head = new
# dll = DoublyList()
# dll.insert_begin(10)
# dll.insert_begin(20)
# dll.insert_begin(30)
# print("Forward:")
# temp = dll.head
# while temp:
#     print(temp.data)
#     temp = temp.next