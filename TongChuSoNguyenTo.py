import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if(n % i ==0):
            return "NO"
    if n > 1: return "YES"
    else: return "NO"

T = int(input())
for t in range(T):
    s = input()
    sum = 0
    for i in s:
        sum+= int(i)
    print(isPrime(sum))
