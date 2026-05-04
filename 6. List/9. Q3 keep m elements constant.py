# WAP to rotate elements by k times in anticlockwise direction keeping m elements constant at the left side.

lst = [10, 20, 30, 40, 50,60]
k = 3
m = 2

for i in range(k):
    item = lst.pop()
    lst.insert(m, item)
    
print(lst)
