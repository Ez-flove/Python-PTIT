N = int(input())
le = []
chan = []
sl = 0
arr = []
while sl < N:
    arrtmp=list(int(i) for i in input().split())
    for so in arrtmp:
        sl+=1
        if so%2==0:
            chan.append(so)
        else:
            le.append(so)
    arr.extend(arrtmp) # cap nhat them phan tu vao seq(Danh sach cac phan tu cuoi list)
le.sort(reverse=True) # xep giam dan
chan.sort() #xep tang dan
i=0
j=0
for x in arr:
    if x%2!=0:
        print(le[i],end=' ')
        i+=1
    else:
        print(chan[j],end=' ')
        j+=1
print()