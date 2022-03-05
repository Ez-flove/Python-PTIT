
T = int(input())
for t in range(T):
    s = input()
    check = True
    for i in range(0,len(s)):
        if i % 2 == 0:
            if s[i] != s[0]: 
                check = False
                break
        else:
            if s[i] != s[1]:
                check = False
    
    if check: print("YES")
    else: print("NO")