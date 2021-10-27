T = int(input())
for i in range(0,T):
    n= input()
    length= len(n)
    if length >= 4 and n[0]==n[length-2] and n[1]==n[length-1]:
        print("YES")
    else : 
        print("NO")