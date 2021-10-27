'''def check1(n) :
    n=str(n)
    a=[int(i) for i in n]  ## chuyen thanh 1 list
    b=a.copy; b.reverse()
    if a==b: return 1
    else: return 0
def check2(n):
    n= str(n)
    for i in n:
        if int (i)%2==1 : return 0
    if len(n)%2==1: return 0   #Tong cac phan tu cua n: len(n)
    return 1
for i in range (int(input())):
    n= int(input())
    for i in range(n):  # a la list gom cac so thoa man
        #if check1(i)==1 && check2(i)==2:
            #a.append(i)
'''
a=[22,44,66,88,2002,2222,2442,2662,2882,4004,4224,4444,4664,4884,6006,6226,6446,6666,6886,8008,8228,8448,8668,8888,200002,202202,204420,206620,208820,]
for i in range(int(input())):
    n= int(input())
    for i in a:
        if i<n: print(i,end=" ")
        else: break
    print()       
