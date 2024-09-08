name = input("Enter your name: ")

print("Hello, " + name + "! Welcome to Hola Fresh Grocery Store Website!")

shopping_list = []
groceries = input("Enter the name of the item you want to add to your shopping list: ")

while groceries != "done":
    shopping_list.append(groceries)
    groceries = input(" Enter the name of the items you want to add to your shopping list (or type 'done' to finish): ")
   
print("Your shopping list")
   
for groceries in shopping_list:
    print("- " + groceries)

completed_shoppinglist = len(shopping_list)

print("Total items on shopping list: " + str(completed_shoppinglist))

print("Checking shopping list ... ")

for groceries in shopping_list:

 if len(groceries) < 1:
    print(groceries + "  --> " + "Empty item found")
 elif   1 <=len(groceries) < 4:
    print(groceries + "  --> " + "Short item")
 elif 4 <= len(groceries) < 8:
    print(groceries + "  --> " + "Medium item")
 else:
    print(groceries + "  -->" +"Long item")


