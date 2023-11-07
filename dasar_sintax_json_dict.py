users = {
    "id" : 1,
    "name" : "Leanne Graham",
    "username" : "Bert",
    "email" : "Sincere@april.biz",
    "address" : {
        "street" : "Kulas Light",
        "suite" : "Apt. 556",
        "city" : "Gwenborough",
        "zipcode" : "02009-3874",
        "geo": {
            "lat" : "-37.3159",
            "lang": "81.1496"
        }
    }
}

print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"])
print(users["address"]["geo"]["lat"])

print("\ntype data user (python)")
print(type(users))

print("\nubah dict ke json")
import json
result = json.dumps(users)
print(type(result))
print(result)

with open('result.json','w') as file:
    json.dump(users, file)






