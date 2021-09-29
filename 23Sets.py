# Creating a Set 
pets = {"dog", "cat", "parrot", "fish"}
print(pets)

x = {"dog", 21, True}
print(x)

# Accessing Items 
for pet in pets:
    print(pet)

# Adding Items 
pets.add("hamster")
print(pets)

# Removing an Item 
pets.remove("hamster")
print(pets)

# Combining Two Sets 
x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 10}
x.update(y)     #this methods excludes duplicate items
print(x)
# Difference
print("x - y:", x - y)
print("y - x:", y - x)