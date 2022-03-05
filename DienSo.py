T= int(input())
for t in range(T):
    n=int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        if i not in b: 
            b.append(i)
    q = max(b)
    p = min(b)
    print(q-p-len(b)+1)
    
    
    