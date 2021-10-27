
p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while True:
    s= input().split()  
    k= int(s[0])  # chuoi s tra ve xau s va so k duoi dang list vd: nhap 1 ABCD ---> ['1', 'ABCD'] nen k= int(s[0])

    if k==0 :
        break
    s=s[1]
    res=''

    for i in s:
        pos = p.find(i)  # tra ve vi tri tim kiem phan tu do neu ko co thi in ra -1
        res=p[ (pos+k) % 28] + res
    
    print(res)