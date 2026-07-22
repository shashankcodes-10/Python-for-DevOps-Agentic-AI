import json

# read a file

# f = open("demo.txt")
# print(f.readlines())
# f.close()



with open("demo.txt") as f : # another method to read a file
    print(f.readlines())  # read all lines into a list

with open("demo.txt") as f : # another method to read a file
    print(f.readline())  # read file line by line

with open("demo.txt") as f : # another method to read a file
    print(f.read())  # read file into one string


valid_json = {"age" : "21", "location" : "india"}    


# write something in file

with open("demo.txt" , "w") as file:
    json.dump(valid_json,file)