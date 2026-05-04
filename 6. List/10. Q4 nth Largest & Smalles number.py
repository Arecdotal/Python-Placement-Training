# WAP to find nth largest and nth smallest number in a list

lst = eval(input("Enter a list : "))

n = int(input("Enter the element : "))

lst.sort()
print(lst)

print(lst[-n])
print(lst[n-1])

