base = int(input("Enter the base price : "))
demand = input("Enter high or low : ")
weekend = input("Is there weekend(Yes/no) : ")

if demand == "high" and weekend == "yes":
    base = base * 1.3 #1.3 isiliye kara hai kyuki qo 100% pe extra 30% kar rahe hai
elif demand == "high":
    base = base * 1.2
elif weekend == "yes":
    base = base * 1.1
else:
    print("Wrong input")

print(base)

