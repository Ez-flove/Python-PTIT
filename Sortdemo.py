#4:
location =['HaNoi','HaiPhong','HoChiMinh','DaNang','BinhDuong']
print(location)

print(sorted(location))
print(location)

location.sort()
print(location)

location.reverse()
print(location)

location.sort(reverse=True)
print(location)

#5:
a=[1,'a',34,'a','b',1,'c']
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(len(b))
print(b)

#6
a=(1,2,3,4,5)
print(type(a))

