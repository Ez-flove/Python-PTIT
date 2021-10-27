t = 10
r = []
while t>0:
    s = input().split()
    t = t - len(s)
    for i in s:
        k = int(i) % 42
        if k not in r:
            r.append(k)
print(len(r))