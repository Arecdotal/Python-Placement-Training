#1. Positional arguments (isme position ke according apan print karwaenge)
def profile(name, age):
    print("Name : ", name)
    print("Age : ", age)
    print(name, age)

profile(24, "Aditya")

#2. Default argument (isme alive default dal rakha hai yes to automatically print kar dega, jab value me "no" likhenge tab value change hogi alive ki)
def profile(name, age, alive = "Yes"):
    print("Name : ", name)
    print("Age : ", age)
    print("Alive : ", alive)
    print(name, age, alive)

profile("Chitransh", 19)

#3. keyword arguments (isme ham profile print karwate time define kar denge keyword to print hoye tab sequence me aaye , eg:- 24 aditya ki jagah aditya 24 print hoga)
def profile(name, age):
    print("Name : ", name)
    print("Age : ", age)
    print(name, age)

profile(age = 24, name = "Aditya")

#4. Multipe arguments (*args se use karte hai lik additu=ion me 2 ya 3 number i jagah 1 bar *num dal diya)
def add(*num):
    sum = 0
    for i in num:
        sum += i
    print(sum)
        
add(5)

#5. Multipe Keyword arguments (**kwargs isme keywords ke sath multiple arguments de sakte hai and ye dictionary ke format me aayenga.)
def profile(**data):
    for i in data:
        print(data[i])
    
    
profile(name = "Chitransh", age = 19, phone = 9301843193)

