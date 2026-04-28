sub1 = int(input("Enter the marks : "))
sub2 = int(input("Enter the marks : "))
sub3 = int(input("Enter the marks : "))
sub4 = int(input("Enter the marks : "))
sub5 = int(input("Enter the marks : "))

avg = (sub1+sub2+sub3+sub4+sub5)/5

if (sub1 and sub2 and sub3 and sub4 and sub5)>33:
    print("All clear for the result")
else:
    print("No result for it")

if avg >= 75:
    print("Distinction")
elif avg >= 60:
    print("First class")
elif avg >= 50:
    print("First class")
else:
    print("Pass")

