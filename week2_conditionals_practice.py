print("Welcome to Walter mart Customer Website!")

# Ask the user for their name
name = input("Enter your name: ")

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask the user how many years that they've been shopping at Walter mart.
loyalty = int(input("How long have you been shopping at Walter mart? (in years): "))

# Determine the discount based on age and loyalty
if age > 65:
    print("Hello, " + name + "! You are eligible for a 50% store discount.")

elif  18 <= age <= 65 and loyalty > 5:
    print("Hello, " + name + "! You are eligible for a 20% store discount.")

elif age < 18 or loyalty <= 5:
    print("Hello, " + name + "! You are eligible for a 10% store discount.")

else:
    print("Hello, " + name + "! You are not eligible for a store discount at this time.")





