# Node class represents a single element (node) in a linked list
class Node:
    def __init__(self, data):
        self.data = data      # stores the SmartList object (student)
        self.next = None      # pointer to the next node in the list (None if last)

# LinkedList class manages the chain of nodes
class LinkedList:
    def __init__(self):
        self.head = None      # first node in the linked list, starts empty

    # Method to add a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)   # create a new node with the provided data

        # If list is empty, new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Attach the new node at the end
        current.next = new_node

# SmartList class represents a student with subjects and grades
class SmartList:
    def __init__(self, student_name, subject_grades):
        self.student_name = student_name
        self.subjects = subject_grades   # dictionary {subject: grade}

    # Prints the student's name
    def show_student_name(self):
        print(self.student_name)

    # Prints all subjects and their grades
    def show_subjects(self):
        print(self.subjects)

    # Returns the average grade across all subjects
    def avg_grade(self):
        if len(self.subjects) == 0:   # prevent division by zero
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

# Create an empty linked list to store all student objects
students = LinkedList()

# Loop to collect student data from user input
while True:
    name = input("Enter student name (or done): ")  # ask for student name
    if name.lower() == "done":                      # exit loop if done
        break
    
    subjects = {}                                   # dictionary to store subject:grade
    for i in range(4):  # 4 subjects per student
        subject = input("Enter subject name: ")    # ask for subject name
        grade = float(input("Enter grade: "))      # ask for grade and convert to float
        subjects[subject] = grade                  # store subject-grade in dictionary

    student_obj = SmartList(name, subjects)        # create a SmartList object for student
    students.append(student_obj)                   # add student to linked list

# Create an empty list to store student names and their averages
avg_list = []

# If no students were entered, print a message
if len(avg_list) == 0:
    print("No students entered.")

# Traverse the linked list to extract averages into a normal list
current = students.head
while current is not None:
    student = current.data
    avg_list.append([student.student_name, student.avg_grade()])  # store [name, average]
    current = current.next

# Bubble sort the avg_list based on student averages
for i in range(len(avg_list)):
    for j in range(len(avg_list)-1-i):
        if avg_list[j][1] > avg_list[j+1][1]:                # compare averages
            avg_list[j], avg_list[j+1] = avg_list[j+1], avg_list[j]  # swap if out of order

# Display the sorted student ranking
print("\nStudent Ranking:")
for student in avg_list:
    print(student[0], "-", round(student[1],2))  # print name and average (rounded to 2 decimals)
