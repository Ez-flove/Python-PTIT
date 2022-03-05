class Rectangle:
    def __init__(self,dai,rong,mau):
        self.dai=dai
        self.rong=rong
        self.mau=mau
    def perimeter(self):
        return (self.dai + self.rong)*2
    def area(self):
        return self.dai*self.rong
    def color(self):
        return str(self.mau).capitalize()
def main():
    if __name__ == '__main__':
        arr = input().split()
        if int(arr[0])<=0 or int(arr[1])<=0:
            print("INVALID")
        else:
            r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
            print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
main()

