person = {
    "name": "Jack",
    "gender": "Male",
    "age": 16, 
    "address": "Miami", 
    "phone": +19123456789
    }
# Name = person["name"]
# Gender = person["gender"]
# Age = person["age"]
# Address = person["address"]
# Phone = person["phone"]
key = input("What do you what to know about the person ?")
result = person.get(key, "Invalid")
print = (result)