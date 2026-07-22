# creating json data

import json

data = {
    "name" : "shashank" ,
    "age" : "21" ,
    "location": "india"
}

data2 = '{"name": "shashank", "age": "21", "location": "india"}'

# loads is used to convert string to json/dict

loads_output = json.loads(data2)
print(loads_output)

# dumps is used to convert json/dict to string

dumps_output = json.dumps(data)
print(dumps_output)