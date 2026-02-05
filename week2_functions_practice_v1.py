import statistics

print("Welcome to Python Statistics Calculator")

# To store numbers entered by the user
numbers_list = []

number = input("Please enter a number: ")

# While loop to prompt the user to enter a number
while number != "done":
    numbers_list.append(float(number))
    number = input("Enter a new numbers (or type 'done' to finished): ")

# Prints list from user imputs
print(" Your Numbers List: ", numbers_list)

print("\nStatistics")
# Functions to generate the nim,max,mean, and median of the list provided
def get_min(numbers):
    minimum = min(numbers)
    return minimum

def get_max(numbers):
    maximum = max(numbers)
    return maximum

def get_mean(numbers):
    mean = (sum(numbers)/len(numbers))
    return mean

def get_median(numbers):
    median = statistics.median(numbers)
    return median

# While loop to create a menu that loops until the user is ready to exit
while True:
    print("1. Minimum")
    print("2. Maximum")
    print("3. Mean")
    print("4. Median")
    print("5. Show All Stats")
    print("6. Exit")

    option = input("Choose an option (1-6): ")

    if option == "1":
        print("Minimum: ", get_min(numbers_list))
    
    elif option == "2":
        print("Maximum: ", get_max(numbers_list))
    
    elif option == "3":
        print("Mean: ", get_mean(numbers_list))
    
    elif option == "4":
        print("Median: ", get_median(numbers_list))

    elif option == "5":
        print("Minimum: ", get_min(numbers_list)) 
        print("Maximum: ", get_max(numbers_list))
        print("Mean: ", get_mean(numbers_list))
        print("Median: ", get_median(numbers_list))

    elif option == "6":
        print("Leaving menu.... ", "\nSee you soon :D")
        break
# Break stops the loop
    else:
        print("Error. Please enter a vaild imput (1-6): ")
# To avoid errors in the loop



