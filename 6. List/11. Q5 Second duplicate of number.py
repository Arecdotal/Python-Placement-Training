# WAP to find the second duplicate of the given number

lst = eval(input("Enter a list : "))
ele = int(input("Enter a element : "))
c = 3

for i in range(0, len(lst)):
    if lst[i] == ele:
        c -= 1
        
    if c == 0:
        print(i)
        break

else:
    print("Duplicate not exist")