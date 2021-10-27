import math
x = int(input("Nhập Giá trị x: "))
n = int(input("Nhập Giá trị n: "))
s = 0
for i in range(0, n+1):
   tu = x**(2*i+1)
mau = math.factorial(2*i+1)
s = s+(tu/mau)
print(s)
# x + x^3/3! + x^5/5! +  ... + x^(2n+1)/(2n+1)! 