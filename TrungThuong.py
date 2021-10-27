# T = int(input())
# for t in range(T):
#     n = int(input())
#     count = {}  #set
#     for i in range(n):
#         x = int(input())
#         if x in count:
#             count[x] = count[x] - 1
#         else:
#             count[x] = -1
#     sorted_count = sorted(count.items(), key = lambda x : (x[1], x[0]))
#     print(sorted_count[0][0])

#cach 2:
T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    myl = []
    while n > 0:
        n-=1
        k = int(input())
        myl.append(k)

    mx = -1;
    #dung count de dem so lan xuat hien cua moi phan tu trong list
    for i in myl:
        tmp = myl.count(i)#tra ve so lan xuat hien cua phan tu i trong list
        if tmp > mx:
            mx = tmp
    #sap xep list theo thu tu tang dan
    myl.sort()
    #neu gap phan tu co so lan xuat hien nhieu nhat(=mx) thi in ra
    for i in myl:
        tmp = myl.count(i)
        if tmp == mx:
            print(i)
            break
