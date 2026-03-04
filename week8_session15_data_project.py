import pandas as pd
import os

# To find csv file location
print(os.getcwd())

class DataProject:
    def __init__(self, d_project):
        # Store the dataset inside the object
        self.d_project = d_project
        self.df = None
        self.sort_data = None
        self.fil_data = None
        self.drop_dup = None
        self.grouped_data = None

    def load_data(self):
        # Convert dictionary to DataFrame and store it in self.df
        self.df = pd.DataFrame(self.d_project)

        # Save to CSV
        self.df.to_csv("dataproject.csv", index=False)

        # Read it back and update self.df
        self.df = pd.read_csv("dataproject.csv")

        print(self.df)

    def clean_data(self):
        # Make sure dataframe exists
        if self.df is not None:

            # Cleaning operations
            self.sort_data = self.df.sort_values("Age", ascending=False)
            self.drop_dup = self.df.drop_duplicates()

            print("\nCleaned Data (Sorted):")
            print(self.sort_data)

           

    def filter_data(self):
        # Ensure dataframe exists
        if self.df is not None:

            self.fil_data = self.df[self.df["Age"] >= 20]

            print("\nStudents Over 19:")
            print(self.fil_data)

    def group_data(self):
        #Groups data based on a criteria
        if self.df is not None:
            self.grouped_data = self.df.groupby("Age").max()

            print("\nStudent count: ")
            print(self.grouped_data)

class Node:
        def __init__(self,data): 
           self.data = data    # Stores the value inside the node
           self.next = None    # Pointer to the next node

class CircularLinkedList:
        def __init__(self):
           self.head = None
        
        def insert_begin(self, data):
            new_node = Node(data) # Create a new node with the given data
           
            # Case 1: Empty list
            # make the new node point to itself to form a circular structure
            if self.head is None:
                new_node.next = new_node
                self.head = new_node

             # Case 2: List has nodes
             # find the last node (the one whose next points to head)    
            else:
                temp = self.head

                while temp.next != self.head:
                  temp = temp.next
            
                # Link last node to new node
                temp.next = new_node

                # Make new node point to old head
                new_node.next = self.head

                # Update head to the new node
                self.head = new_node

        
# Create data
d_project = {
    "Name": ["Abby","Ben","Conner","Daisy","Eric","Fay","Gabrielle","Henry"],
    "Age": [18, 20, 23, 19, 24, 21, 22, 17],
    "Course": ["Computer Science","Mathematics","Business Administration",
                "Accounting","Psychology","Biology",
                "Economics","Information Technology"]
}

# Create instance and call methods
project = DataProject(d_project)

project.load_data()
project.clean_data()
project.filter_data()
project.group_data()

clist = CircularLinkedList()
clist.insert_begin("First")
clist.insert_begin("Second")

print("\nCircular Linked List: ")
print("Head:",clist.head.data)
print("Next:",clist.head.next.data)
print("Loop:",clist.head.next.next.data)





