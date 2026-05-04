lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

lst.pop() # last se element delete karega
lst.pop(2) # specific position se delete karega

del lst[0:2] # 0 se 1 tak remove karega
lst.remove(40) # specific declared element delete karega
lst.clear() # list empty kar dega but list rehegi blank []

print(lst)
