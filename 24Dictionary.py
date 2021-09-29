
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}
print(person)
print(type(person))

# Accessing Items 
x = person["first_name"]
y = person["last_name"]
z = person["age"]
print("First Name:", x)
print("Last Name:", y)
print("The Age is:", z)
        # 2nd Method
print(person.get("first_name"))

# Changing an Item's Value
person["first_name"] = "Jane"
print(person)

# Removing an Item 
person.pop("age")
print(person)

# Nested Dictionary
employees = {
    "manager": {
        "name": "Jane Doe",
        "age": 29
    },
    "programmer": {
        "name": "John Doe",
        "age": 20
    }
}
print(employees)