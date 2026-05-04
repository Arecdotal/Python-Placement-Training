# WAP to rotate the elemts in a list by k times in anticlockwise direction
#First approach
'''
lst = [10, 20, 30, 40, 50]
k = int(input("Enter a number : "))

lst = lst[k:] + lst[:k]
print(lst)
'''  

# output list = [40, 50, 10, 20, 30]

#Second approach: ->

lst = [10, 20, 30, 40, 50]
k = 2

for i in range(k):
    item = lst.pop()
    lst.insert(0, item)
    
print(lst)
