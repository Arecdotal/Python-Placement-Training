#WAP to print prime number from 1 to n

num = int(input("Enter a number : "))

for i in range(2, num+1):
    for j in range(2, (i//2)+1):
        if i % j == 0:
            break
        
    else:
        print(i)
        
