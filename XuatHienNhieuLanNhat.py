T = int(input())
for t in range(T):
    n = int(input())
    arr = list(int(i) for i in input().split())
    dict={} #dictionary rong de duyet phan tu xuat hien nhieu lan
    for i in arr:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    
    max=0 #val:so lan xuat hien cua so
    res=0 #key:gia tri cua so 
    for key, val in dict.items():
       if val>max:
        max=val
        res=key
    if max>int(n/2):
        print(res)
    else:
        print('NO')
