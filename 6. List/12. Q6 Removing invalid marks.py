# a teacher stored marks but some entries are invalid remove them and return valid marks (invalid = -1)
# [45, 67, -1, 89, -1, 76]
# the correct list should be [45, 67, 89, 76]

lst = eval(input("Enter a list of marks : "))
lst2 = []

for i in lst:
    if i > 0:
        lst2.append(i)
   
print(lst2)
