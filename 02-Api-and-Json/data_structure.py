# list

data = [ "aws", "azure" ,"gcp"]

print(data[0])

for i in data:  # print all the values of list
    print(i)

print(type(data)) # print type 

# dictionary    

data2 = {
    "name" : "shashank" ,
    "age" : "21" ,
    "interest" : ["devops" , "ai" , "cloud"]
}

print(data2["name"])
print(type(data2))

for key,value in data2.items():
    print(key , ":" , value)


# tuples

data3 = ("monday", "tuesday")
print(data3)
print(type(data3))


# set

data4 = {1 , 1 , 2 , 2 , 2 , 3 , 3 , 4 , 4 , 4 , 4 } # remove the duplicate values
print(type(data4))
print(data4)