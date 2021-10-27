def Fibo():
    listfibo=[]
    f1=0
    f2=1
    for i in range(1,94):
        listfibo.append(f1)
        tmp=f1
        f1=f2
        f2=f1+tmp
    return listfibo

listfibo = Fibo()
T = int(input())
for t in range(0,T):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        print(listfibo[i], end=' ')
    print()


