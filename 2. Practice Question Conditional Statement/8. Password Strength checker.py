password = input("Enter a password : ")

hasUpper = False
hasDigit = False
hasSymbol = False
hasLower = False
hasLength = len(password)>=8

for i in password:
    if i.isdigit():
        hadDigit = True

    elif i.isupper():
        hasUpper = True
        
    elif i.islower():
        hasLower = True
    
    else:
        hasSymbol = True

if hasSymbol and hasDigit and hasUpper and hasLength:
    print("Strong")
else:
    print("Weak")
    
