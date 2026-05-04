lst = [10, 20, 30, 50, 70, 60, 40]

'''SORT is a Method'''
lst.sort() # ascending order me sort karega
print(lst)

lst.sort(reverse = True) # descending order me sort kar dega.

print(lst)

'''SORTED is a Function'''
lst2 = [5, 2, 1, 7, 9, 8]
lst3 = sorted(lst2)
print(lst2)

lst3 = sorted(lst2, reverse = True)
print(lst3)
