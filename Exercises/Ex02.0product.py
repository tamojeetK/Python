lot_number = "037-00901-00027"

# countrycode = str(input("Enter your country code: "))
# productcode = str(input("Enter your product code: "))
# batchnumber = str(input("Enter the batch number: "))
# print("Country code: ", countrycode)
# print("Product code: ", productcode)
# print("BatchNumber: ", batchnumber)

countrycode = lot_number[:3]
productcode = lot_number[4:9]
batch = lot_number[-5:]
print("Country code: ", countrycode)
print("Product code: ", productcode)
print("Batch Number: ", batch)
