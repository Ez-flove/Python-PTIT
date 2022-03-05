t=int(input())
for i in range(t):
    s=input()
    a=[]
    i=0
    r=""
    while(i<len(s)):
        if s[i].isdigit():
            r+=s[i]
        elif s[i].isalpha() and r!="":
            a.append(int(r))
            r=""
        if i==len(s)-1 and r!="":
            a.append(int(r))
        i+=1
    a.sort()
    print(a[0])