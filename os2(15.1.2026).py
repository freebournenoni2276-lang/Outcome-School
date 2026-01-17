grocery = []
# creates an empty list to store grocery items

item = input("Enter the item you want to add to the grocery list: ")
# asks the user to enter a grocery item and stores it in the variable 'item'

while item != "done":
# keeps looping as long as the user does not type "done"

    grocery.append(item)
    # adds the current item to the grocery list

    item = input("Enter the item you want to add to the grocery list (or type 'done' to finish): ")
    # asks the user for another item and updates the variable 'item'

print("Your grocery list:")
# prints a heading before displaying the list

for item in grocery:
# loops through each item stored in the grocery list

    print("- " + item)
    # prints each grocery item with a dash in front
