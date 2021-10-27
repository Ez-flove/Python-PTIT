# def greater(x, y):
#     if len(x) > len(y):
#         return True
#     elif len(x) < len(y):
#         return False
#     else:
#         return x > y

# while True:
#     N= int(input())
#     if N == 0:
#         break
#     resMax = '0'
#     resMin = ' '
#     for i in range(N):
#         x = input()
#         while x[0] == '0':
#             x = x.lstrip('0')  #ham cat cac ki tu chars trong chuoi () de in ra chuoi khong co ki tu do
#         if (greater(x, resMax)):
#             resMax = x
#         if (len(resMin) == 0) or (greater(resMin, x)):
#             resMin = x
#     if (resMax == resMin):
#         print('BANG NHAU')
#     else:
#         print(resMin)
T = 10
while T > 0:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        tmp = int(input())
        l.append(tmp)
    mx = max(l)
    mn = min(l)
    if mx == mn:
        print("BANG NHAU")
    else:
        print(mn, mx)