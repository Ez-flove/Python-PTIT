def Prime():
    n=int(input())
    print("1",end=" ")
    for i in range(2, int(n**0.5)+1): # for 2 --> can bac 2 cua n 
        if n%i==0:
           count=0
           while n%i==0:
               count+=1
               n//=i    #Chia lam tron xuong
           print("* "+str(i)+"^"+str(count), end=" ")
    if n>1:  print("* "+str(n)+"^1",end=" ")
    print()  

for i in range(int(input())): Prime()

