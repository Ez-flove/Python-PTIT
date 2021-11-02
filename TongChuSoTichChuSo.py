T =  int(input())

for t in range (T):
    s = input()
    sum = 0
    tich = 1
    le = 0

    for i in range(0,len(s)):
        if i%2 == 0:
            sum += int(s[i])
        else:
            if s[i] != '0':
                tich *= int(s[i])
            else:
                le+=1 # dem vitri le
    
    if le == len(s) // 2: tich = 0
    print(sum, tich)
    