from operator import length_hint
from traceback import print_tb


s = input()
h = int(input())
a =[]
b =[]
c =[]
i=0
j=1
while(j<len(s)): 
    d = int(s[i])*10+int(s[j])
    a.append(d)
    i+=2
    j+=2
    if d not in b:
        b.append(d)
if len(s)%2==1:
    a.append(int(s[len(s)-1]))
    if int(s[len(s)-1]) not in b:
        b.append(int(s[len(s)-1]))
for k in b:
    c.append([k,a.count(k)])
c = sorted(c)
test = True
for q,p in c:
    if p>=h:
        print(q,p,sep=' ')
        test = False
if test:
    print('NOT FOUND')





