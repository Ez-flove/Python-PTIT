m = int(input())
a = [[int(j) for j in input().split()] for i in range(m)]
k = int(input())
tt = 0
td = 0
for i in range(m):
  for j in range(m):
      if i+j<m:
          tt+=a[i][j]
      if i+j>m:
          td+=a[i][j]
print(tt)
print(td)
if abs(tt-td)<=k:
    print('YES')
    print(abs(tt-td))
else:
    print('NO')
    print(abs(tt-td))


