#Login attempt Lock

flag = 0

for i in range(3):
    password = input("Enter the password : ")
    
    if password == "Hello123":
        print("Login successful")
        flag = 1
        break
    
    else:
        print("Wrong Passsword")

if not flag:
    print("Account Block")
    
