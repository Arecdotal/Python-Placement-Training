def palindrome(s):
    #abcba -> 0 1 2 3 4
    n = len(s)
    for i in range(0, (n-1)//2 + 1):
        if s[i] != s[n-1-i]:
            print("Not palindrome")
            return
        
    print("Palindrome")
    
palindrome("HellolleH")