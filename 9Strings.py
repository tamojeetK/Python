#Strings in python
text = "\nHello World"
print(text)
# *****************

# Single or Double Quotes
text1 = 'He said "I love Python"'
print(text1)
# *****************
text2 = "Let's have fun learning Python!"
print(text2)
# *****************

# Multi Line Strings
text3 = '''Python
is fun to learn
for sure you are having
fun too.'''
print(text3)
# *****************

# Concatenating Strings
a = "Namaste"
b = "Duniya"
c = "!!"
d = a + b + c
print(d)
# *****************

# Escaping Characters in a String
x = 'Lets\'s learn python. '
y = "He said \"Come let's code together\""
print(x+y)
# ******************

# Indexing
text4 = "Hi everyone"
print(text4[0]) #prints H
print(text4[1]) #prints i
print(text[-1]) #prints e
print(text[-2]) #prints n

#Slicing
print(text4[3:7]) #prints ever (while slicing the end index is not included)