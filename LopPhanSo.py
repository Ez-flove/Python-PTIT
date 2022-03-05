import math


import math
class PS:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def pstg(self):
        temp = int(math.gcd(self.x,self.y))
        self.x = self.x//temp
        self.y = self.y//temp
        print(self.x,self.y,sep='/')

m,n = map(int,input().split())
p1 = PS(m,n)
p1.pstg()







        

