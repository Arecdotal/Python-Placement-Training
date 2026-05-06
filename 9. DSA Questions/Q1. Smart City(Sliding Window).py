lst = eval(input("Enter list : "))
k = int(input("Enter the value of k : "))
sum, max = 0,0

for element in range(k):
    sum += lst[element]
if sum > max:
    max = sum
for i in range(k, len(lst)):
    sum -= lst[i-k]
    sum += lst[i]
    if sum > max:
        max = sum
        
print(max)
