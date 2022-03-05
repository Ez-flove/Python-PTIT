T = int(input())
for t in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    dict = {}
    for i in a:
        if i not in dict:
            dict[i] = 0
        dict[i]+=1
    for i in a:
        if dict[i]%2!=0:
            print(i)
            break
