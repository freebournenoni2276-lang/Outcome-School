# import requests as req
# r = req.get("https://chatgpt.com")

# from colorama import Fore
# print(Fore.GREEN + "Success")

# file = open("sample.txt","w")
# file.write("Hello World First Time")
# file.close()

# file = open("sample.txt","r")
# content = file.read()
# print(content)

# file = open("sample.txt","a")
# file.write("\nHello World Second Time")
# file.close()

# # file = open("sample.txt","r")
# # content = file.read()
# # print(content)

# file = open("sample.txt", "a")
# file.write("\nNew Line Added")
# file.close()

# with open("sample.txt","r") as f:
#     line1 = f.readline()
#     line2 = f.readline()
#     line3 = f.readline()

#     print(line1)
#     print(line2)
#     print(line3)

# import json
# data = {
#     "name":"Noni",
#     "age":19,
#     "skills": ["Math","Python"],
#     "is_stundent": True
# }

# data = {
#     "name":"Noni",
#     "age":19,
#     "skills": ["Math","Python"],
#     "is_stundent": True
# }

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)

# print("JSON file created!")


# import json

# with open("data.json","r", encoding="utf-8") as f:
#     info = json.load(f)
#     print(data["name"])

import csv

file = open("data.csv","w")
file.write("Hello World First Time")
file.close()

with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)