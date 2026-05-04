lst = [10, 20]

lst.append(30) # adds at end of list
lst.insert(2,25) # adds at any defined index in loist
#lst.append([40, 50, 60])
# is append se wo 1 single element me create kargea and extend se each element ko individually add karega
lst.extend([40, 50, 60])

print(lst)
