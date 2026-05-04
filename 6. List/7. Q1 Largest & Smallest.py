# WAP to find second largest and third smallest in the list of element
import math
lst = eval(input("Enter a list : "))
max, smax = lst[0], lst[0]
min, smin, tmin = math.inf, math.inf, math.inf

for i in lst:
    if i > max:
        smax = max
        max = i
    else:
        if i > smax:
            smax = i
            
    if i < min:
        tmin = smin
        smin = min
        min = i
    
    elif i < smin:
        tmin = smin
        smin = i
    
    elif i < tmin:
        tmin = i
        
print("Maximum element : ", max)
print("Seceond largest element : ", smax)

print("Minimun element : ", min)
print("Second Minimun element : ", smin)
print("Third Minimun element : ", tmin)
