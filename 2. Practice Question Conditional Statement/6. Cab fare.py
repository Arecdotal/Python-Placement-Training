trip = int(input("Enter the trip distance = "))
amount = 0
night = input("Enter the night stay or not : ")

if trip <= 5:
    amount = trip * 50

elif trip <=10:
    amount = (5 * 50) + (trip - 5) * 40
    
else:
    amount = (5*50)+(5*40)+ (trip - 10) * 30
    
if night == "yes":
    amount += amount *0.2

print(amount)