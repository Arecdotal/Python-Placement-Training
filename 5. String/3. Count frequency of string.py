def countfrequency(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        
    return dict

s = input("Enter a string : ")

print(countfrequency(s))

