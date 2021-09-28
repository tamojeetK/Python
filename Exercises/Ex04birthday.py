# DD-MM-YYYY
# You were born in [month]
months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

birthday=input("Enter your DOB in DD-MM-YYYY format: ") #15-08-2004
index = int(birthday[3:5]) - 1
show_bd = months[index]
print("Your birthday is in :", show_bd)