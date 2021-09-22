from typing import List


pets = ("dog", "cat", "rabbit", "fish", "salamander")
print(pets)

x = ("dog", 21, True)
print(x)

# ******************

# Indexing
print(pets[0])
print(pets[1])
print(pets[2])

# Range of Indexes
print(pets[1:2])

print(pets[:3])

print(pets[3:])

print(pets[-3:])

print(pets[:-3])

# *******************

# Finding Length
print("The length of the Tuple is: ",len(pets))
# *******************

# Looping through a Tuple 
for pet in pets:
    print(pet)

# *******************
# Checking Availability
print("dog" in pets)

print("hamster" in pets)
# *******************

# Another way of Creating a Tuple
print(tuple(("dog", "cat", "parrot", "hamster","cockatoo")))
# print(list(("dog", "cat", "parrot", "hamster","cockatoo"))) #test
# *******************

# Combining Tuples 
genere1 = ("adventure", "si-fi", "action")
genere2 = ("horror", "comedy", "thriller")
all_genere = genere1 + genere2
print(all_genere)