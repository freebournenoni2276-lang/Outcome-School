# print("=" * 20)

#print ("Hello\nWorld")

#word = "Python"
#print(word[0]) #P
#print(word[1]) #y
#print(word[5]) #n

#print(word[-1]) #n
#print(word[-2]) #o

#nums = [10,20,30,40,50,60]
#print(nums[::-1])
#print(nums[-3:])
#print(nums[::2])

#names = ["Ali", "Sara","Omar"]
#names[0] = "Aisha"
#print(names)

#nums[1:4] = [100,110,120]
#print(nums)

#nums = [10,20,30,40,50]
#total = 0
#for n in nums:
    #total += n
#print("Sum =", total)
#print(sum(nums))

for parent in range(1,11):
    for child in range(1,11):
        print(parent*child, end= "\t")
    print()