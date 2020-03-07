import json

input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input)
print("Number of Users :", len(info))
for item in info : 
    print('Name: ',item["name"],', Id: ',item["id"],', Attributes: ',item["x"])
