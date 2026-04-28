speed = int(input("Enter a speed of vehicle : "))
violation = input("Enter violation (Yes/No) : ")
fine = 0

if speed>100:
    if violation == "yes":
        fine = 1000*2
    else:
        fine = 1000

elif speed > 80:
    if violation == "yes":
        fine = 500 * 2
    else:
        fine = 500

print(fine)

