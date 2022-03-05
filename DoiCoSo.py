def doi(n,b):
    s=""
    t=n
    while(t>0):
        du=t%b
        if(du>=10): s+=str(chr(du+55))
        else:s+=str(du)
        t=int(t/b)
    
    print(s[::-1])
t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    doi(n,b)