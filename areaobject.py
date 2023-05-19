# class rect():
#     length=10;
#     breadth=5;
#     area=length*breadth
#     print(area)
# obj=rect()

class reacts():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def peri(self):
        return 2*(self.breadth*self.length)
a=int(input("length"))
b=int(input("breadth"))
obj=reacts(a,b)
# ob=peri(a,b)4

print("area",obj.area())
print("perimeter",obj.peri(a,b))


    