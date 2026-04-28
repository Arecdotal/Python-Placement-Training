Amount = int(input("Enter the amount : "))
location = input("Enter the location mismatch or not : ")
transaction = int(input("Enter the transaction in 1 min : "))

if (Amount>50000 and location.lower == "no"):
    print("Tansaction complete")
    
elif transaction < 3:
   print("Transaction complete")

else:
    print("transaction incomplete")    