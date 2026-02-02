#fruits = ["apple","banana","mango","orange"]
#print(fruits)

#print(fruits[0])

#for fruit in fruits:
    #if fruit[1] == "a":
    # print(fruit)


#numbers = [3, 7, 2, 9, 4]
#print("Total:", sum(numbers))

#count = 0
#greaterthan_five = []

#for n in numbers:
    #count += 1

#print("Greater than 5:", greaterthan_five)
#print("Count:", count)

#for i in range(1, 4):
    #for j in range(1, 4):
        #print(i*j, end= " ")
    #print( )
# Print must be within the loop to get the table format. This just moves the cursor to a new line after all the printing is done.
# end=" " keeps the output on the same line with a space instead of going to a new line

for i in range(5):
    for j in range(i + 1):
        print("*", end= " ")
    print( )

for i in range(3):
    for j in range(3):
        print("*", end= " ")
    print( )