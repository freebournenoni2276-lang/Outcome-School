# 1. How many seconds are there in 42 minutes 42 seconds?
sec = 42
min = 42

total_seconds = min * 60 + sec

print("There are " + str(total_seconds) + " " "seconds in 42 minutes and 42 seconds.")
# str converts integer to string to avoid errors (Type Casting)

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

km = 10

mile = km / 1.61

print("There are " + str(mile) + " " " miles in 10 kilometers.")

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)?

sec_mile = total_seconds / mile
# stores variable for time per mile in seconds ONLY

min_mile = int(sec_mile / 60)
# converts sec_mile to minutes

s_mile = int(sec_mile % 60)
# stores the remainder/seconds from the min_mile variable 

print("Your average pace is " + str(min_mile) + " minutes and " + str(s_mile) + " " " seconds per mile.")

# Bonus Question:
# Ask the user for the number of minutes and seconds it takes them to run 10km and calculate their average speed in miles per hour.


print(" Hello there! Here's a bonus question for you. How many minutes and seconds does it take you to run 10km?")

user_min = int(input("Please enter the number of minutes: "))
user_sec = int(input("Please enter the number of seconds: "))

user_total_sec = user_min * 60 + user_sec
user_total_hours = user_total_sec / 3600

avg_speed_mph = mile / user_total_hours

print("Your average speed is " + str(avg_speed_mph) + " " " miles per hour.")