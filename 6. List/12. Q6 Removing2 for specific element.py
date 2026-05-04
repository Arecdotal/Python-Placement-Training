lst = eval(input("Enter a list : "))
ele = int(input("Enter a element : "))

for i in range(len(lst)-1, -1, -1):
    if lst[i] == ele:
        lst.pop(i)
        
print(lst)
