# Python Lists
# obects are palced inside [] and separated by ,
pets = ["dog", "cat", "rabbit", "fish"]
print("\n", pets)

x = ["dog", 21, True]
print(x)

# Indexing
print(pets[0])
print(pets[1])
print(pets[2])

# ******************

# Range of Indexes
range1 = pets[1:3]
print(range1)

range2 = pets[:2]
print(range2)

# ******************

# Adding items to a List. "append()" and "insert()"
pets.append("hamster")

print(pets)

pets.insert(0, "toucan")
pets.insert(2, "parrot")

print(pets)
print(pets[0])
print(pets[2])

# *******************

# Deleting Items from List. "pop()" , "remove()" , del
pets.pop()

print(pets)

pets.remove("parrot")
print(pets)

del pets[0]
print(pets)

# Length of the List 
print(len(pets))

# Changing Item's Value 
pets[2] = "hamster"
print(pets)

# Checking if an Item exists 
print("dog" in pets)
print("python" in pets)
print("\n")

# Looping through a List 
for pet in pets:
    print(pet)

pet = list(("dog", "cat", "rabbit"))
print(pet)