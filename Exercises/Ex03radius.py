import math
print("\n***This program executes the Area & Circumference of a circle***")

r = float(input("\nEnter the value of radius: "))
print("The value of R given by you is", r, "units\n")
# pi = 3.14159265359
area = math.pi * (r**2)
print("The area is : ", round(area, 2), "sq.units\n")
circumference = 2 * math.pi * r
print("The Circumference is : ", round(circumference, 2), "units")