#Odd Even game

num = int(input("Enter numbers : "))
even,odd = 0,0 #respectivevalue assign karte hai

while num:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        
    num = int(input("Enter number again : "))
    
print("Even : ", even)
print("Odd : ", odd)
