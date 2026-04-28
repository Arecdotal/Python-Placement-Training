available = 0
seats = int(input("Enter seats requiered : "))

vip = input("Enter if vip or not : ")

if vip == "yes" or seats <= available:
    print("Confirm tciket")
else:
    print("Waiting")

