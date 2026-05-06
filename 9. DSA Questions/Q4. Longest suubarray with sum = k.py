# Find the longest subarray with sum = k

# Find the longest subarray with sum <= k

lst = [1,2,1,0,1,1,0]
k = 6
l, sum, max = 0, 0, 0

for i in range(len(lst)):
    sum += lst[i]
    if sum == k and i-l+1 > max:
        max = i-l+1
    while sum > k:
        sum -= lst[l]
        l += 1
        
print(max)

