'''Q1. You own a parking lot, you have a different pricing for different number of hours you need to hire a developer to calculate the total bill with the help of a program.

1. for the first two hours - 100rs/h
2. for the next three hours - 50rs/h
3. rest or remaining hours - 25 rs/h
'''

time = float(input("Enter the number of hours parked : "))

count = 0

if time<=2:
    count = time * 100

elif 2<time<=5:
    count = 2 * 100+(time)*50
    
else:
    count = 2 * 100 + 3 * 50 + (time - 5)*25

print(count)