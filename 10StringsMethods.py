# Capitalize String 
text = "the text goes like this."
print(text) #normal

x = text.capitalize()
print(x)

# ********************

# Covert to UPPERCASE
y = text.upper()
print(y)

# Convert to lowercase
text1 = "THe text1 GoEs LiKe ThIs."

print(text1.lower())
        # or
a = text1.lower()
print(a)

# ********************

# Get Length of a String
print("length of the string is" , len(text))

# ********************

# Replacing Parts of String >> string.replace(old substring, new substring)
b = text.replace("text" , "string")
print(b)

text2 = "Hello World! I love World! World is amazing!"
print(text2)

c = text2.replace("World", "Everyone")
print(c)

d = text2.replace("World", "Everyone", 2)
print(d)

# *********************

# Checking Presence of Value on a String
m = "goes" in text
print(m)

n = "nope" in text
print(n)

o = "nope" not in text
print(o)