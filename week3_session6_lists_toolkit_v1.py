print("Welcome to Outcome Interactive Menu Program")

numbers = []   # list to store numbers

print("Enter numbers one at a time. Type 'done' to finish.")

user_input = input("Enter a number: ")

while user_input != "done":
    numbers.append(float(user_input))     
    user_input = input("Enter a number: ")  

print("\nNumber list:")

for user_input in numbers:
    print("-", user_input)



# Slicing
print("\nThe first 3 and last 3 numbers of your list are: ") 
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])


while True:
    print("\n===== Number List Menu =====")
    print("1. Show List")
    print("2. Add Number")
    print("3. Remove Number")
    print("4. Pop by Index")
    print("5. Sort List")
    print("6. Reverse List")
    print("7. Show Min & Max")
    print("8. Remove Duplicates")
    print("9. Exit")

    option = input("Choose an option (1-9): ")

    # Show List
    if option == "1":
        print("Current list:", numbers)

    # Add Number
    elif option == "2":
        value = float(input("Enter number to add: "))
        numbers.append(value)
        print("Number added.")

    # Remove Number
    elif option == "3":
        value = float(input("Enter number to remove: "))
        numbers.remove(value)
        print("Number removed.")

    # Pop by Index
    elif option == "4":
        index = int(input("Enter index: "))
        removed = numbers.pop(index)
        print("Removed:", removed)

    # Sort List
    elif option == "5":
        numbers.sort()
        print("List sorted.")

    # Reverse List
    elif option == "6":
        numbers.reverse()
        print("List reversed.")

    # Show Min & Max
    elif option == "7":
        if numbers:
            print("Minimum:", min(numbers))
            print("Maximum:", max(numbers))
        else:
            print("List is empty.")

    # Remove Duplicates
    elif option == "8":
        numbers = list(set(numbers))
        print("Duplicates removed.")

    # Exit
    elif option == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-9.")

   
