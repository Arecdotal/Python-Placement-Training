'''Q2. You need to calculate the total bill based on the number of units

1. 0-100 units = 1.5rs/unit
2. 101-200 units = 3.5/unit
3. remaining units = 5rs/unit
4. you need to add 50rs as a fixed charged
5. if the bill exceed 2000rs then add a surplus charge of 10% of the total bill.
'''

unit = int(input("Enter the unit spent : "))

count = 0

if unit<=100:
    count = (unit * 1.5)

elif unit<=200:
    count = (100 * 1.5) + (unit - 100)*3.5 
    
else:
    count = (100 * 1.5) + (100 * 3.5) + (unit - 200)*5
  
count += 50
  
if count>2000:
    count += count*0.1


print(count)

