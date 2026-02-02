# This function checks if the entered password is correct
def check_password(user):
    return user == "Password"   # Returns True if correct, False if not

# This variable keeps track of how many wrong attempts were made
count = 0

# Ask the user to enter a password for the first time
user = input("Enter your password: ")

# This loop runs as long as the password is NOT correct
while not check_password(user):
    print("Incorrect password")  # Tell the user the password is wrong
    
    count += 1                   # Increase the attempt counter by 1
    
    # Ask the user to try again
    user = input("Enter your password: ")

# This runs ONLY when the correct password is entered
print("Access granted")

# Display how many wrong attempts were made
print("Attempts:", count)
