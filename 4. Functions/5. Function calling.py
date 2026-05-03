# Call by value (For immutable datatypes like string, tuple, etc.)

def update(v):
    v = 10
    print(v)
    
v = 5
update(v)
print(v)

# Call by reference (For mutable datatypes like list, dictionary, etc.)

def update(lst):
    lst[0] = 21
    
lst = [10, 20, 30, 40, 50]
update(lst)
print(lst)
