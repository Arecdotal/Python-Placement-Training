#Discount

amount = int(input("Enter the amount = "))
premium = input("If the client premium or not = ")

if amount >= 5000:
    amount = amount*0.8
    
elif amount >= 3000:
    amount = amount*0.9

else:
    print("invalid input")
    
if premium == "yes":
    amount = amount*0.95
    
print(amount)