lst = [10, 20, 30]

l = lst
l[0] = 1

print(l)
print(lst)

#apan ne sirf l me update kara to fir bhi lst me changes ho gaye to ye constant pool me gaya isiliye ye copy nahi bani.

# to correct it is.

lst = [10, 20, 30]

l = list(lst)
l[0] = 1

print(l)
print(lst)

