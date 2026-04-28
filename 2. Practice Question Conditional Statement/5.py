amount = int(input("Enter the amount to be withdrawn = "))
balance = int(input("Enter the balance you have = "))

if (balance-1000) >= amount:
    print("Transaction Complete")

else:
    print("Transaction failed")
    
