print("Welcome to Outcome School Student Portal")

# Stores the student name and student ID using a tuple
student_info = ("John Doe", "53719")

# Stores student details (course, year) using a dictionary 
student_details = {"Course": "Python Foundations", "Year":"Freshman"}

# Stores completed activities in a set
c_activities = set()

# Stores actvities for random selection
activities = ["Student Government",
    "Math Club",
    "Computer Science Club",
    "Debate Team",
    "Volunteer Tutoring",
    "Robotics Club",
    "Environmental Club",
    "Student Newspaper",
    "Cultural Association",
    "Sports Club"]

import datetime

import random

# Menu Loop
while True:
    print("***** Student Activity Tracker *****")
    print("a. Add student details: ")
    print("b. Add Activity: ")
    print("b.a See suggested activtites: ")
    print("c. Show student details: ")
    print("d. Show completed activities: ")
    print("e. Exit")

    option = input("Choose an option(a-e): ")

# Update Student Details
    if option == "a":
        key = input("Enter student details to be updated (e.g: course,year): ")
        value = input("Enter value: ")
        student_details[key] = value
        print("Student details Updated")

# Adds student activity
    elif option == "b":
        activity = input("Enter an activity: ")
        date = datetime.datetime.now()
        c_activities.add((activity,date))
        print("Activity added")

# Suggests a random activity
    elif option == "b.a":
        activity = random.choice(activities)
        print(activity)
        date = datetime.datetime.now()
        c_activities.add((activity, date))
        print("Activity added")

# Shows student Information
    elif option == "c":
        print("\n Student Information: ")
        print("Name: ", student_info[0])
        print("Student ID: ", student_info[1])

        print("\n Student Details: ")
        for key, value in student_details.items():
            print(f"{key}: {value}")

#Shows completed activities
    elif option == "d":
        if activities:
            print("\n Completed Activities: ")
            for activities,date in c_activities:
                print(f" * {activity} (added on {date})")
        else:
            print("No activities recorded.")

# Exits the portal
    elif option == "e":
        print("Leaving Portal. See you soon!")
        break
    else:
        print(" Error. Please enter a valid input(a-e,b.a).")
# To avoid any errors in the program



        









