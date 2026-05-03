total_bill = 0
count = 0

while True:
    tray = int(input("Enter a tray (1/2/3/0) : "))
    sum = 0

    if tray == 1:
        print("Snacks : \n", "a. Lays - 25Rs. \n b. Uncle chips - 15Rs. \n c. Doritos - 30Rs")
        snacks = input("Enter the snacks you want to select (a/b/c) : ")
        if snacks == "a":
            price = 25
            print("You have selected lays chips")
        elif snacks == "b":
            price = 15
            print("you have selected Uncle chips")
        elif snacks == "c":
            price = 30
            print("You have selected Doritos")
        else:
            print("Invalid choice")
            continue
    
        count += 1
        
        money = int(input("Enter the amount = "))
        
        if money == price:
            total_bill = total_bill + price
            
        else:
            print("Not enough money")
        
    elif tray == 2:
        print("Beverages : \n", "a. Coke - 40Rs. \n b. Sprite - 35Rs. \n c. Monster - 125Rs.")
        beverage = input("Enter the beverage you want : ")
        if beverage == "a":
            price = 40
            print("you have selected Coke")
        elif beverage == "b":
            price = 35
            print("you have selected Sprite")
        elif beverage =="c":
            price = 125
            print("you have selected Monster")    
        else:
            print("Invalid choice")
            continue
        
        count += 1
        
        money = int(input("Enter the amount : "))
        
        if money >= price:
            total_bill = total_bill + price
            
        else:
            print("Not enough money")
            
    elif tray == 3:
        print("Chocolates : \n", "a. Kit-Kat 20Rs. \n b. Dairymilk 40Rs. \n c. Bournville - 80Rs.")
        chocolate = input("Enter your chocolate choice : ")
        if chocolate == "a":
            price = 20
            print("you have selected Kit-Kat") 
        elif chocolate == "b":
            price = 40
            print("you have selected Dairymilk")  
        elif chocolate == "c":
                price = 80
                print("you have selected Bournville")
        else:
            print("Invalid choice")
            continue
        
        count += 1
            
        money = int(input("Enter the amount : "))
        
        if money >= price:
            total_bill = total_bill + price
        else:
            print("Not enough money")
            
    elif tray == 0:
            print("Final bill = ", total_bill)
            print("Items Selected : ", count)
            print("Thank you for using vending machine!")
            
            break
        
