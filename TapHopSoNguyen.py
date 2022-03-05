m,n = input().split()
a = [int(i) for i in input().split()]
b = [int(j) for j in input().split()]

a =list(set(a))
b =list(set(b))
g =[]
h =[]
k =[]

for i in a:
    if i not in b:
        g.append(i)
g.sort()
for i in b:
    if i not in a:
        h.append(i)
h.sort()
for i in a:
    if i in b:
        k.append(i)
k.sort()

for i in k:
    print(i,end=' ')
print()
for i in g:
    print(i,end=' ')
print()
for i in h:
    print(i,end=' ')
print()