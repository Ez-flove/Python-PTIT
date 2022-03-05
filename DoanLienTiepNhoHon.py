t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    st=[]
    for i in range(n):
        while(len(st)>0 and a[i]>=a[st[len(st)-1]]):
            st.pop()
        if len(st)==0:
            print(i+1,end=" ")
        else:
            print(i-st[len(st)-1],end=" ")
        st.append(i)
    print()
